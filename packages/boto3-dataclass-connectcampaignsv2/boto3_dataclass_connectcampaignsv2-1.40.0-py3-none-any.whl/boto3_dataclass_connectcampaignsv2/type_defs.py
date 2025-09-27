# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectcampaignsv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AnswerMachineDetectionConfig:
    boto3_raw_data: "type_defs.AnswerMachineDetectionConfigTypeDef" = (
        dataclasses.field()
    )

    enableAnswerMachineDetection = field("enableAnswerMachineDetection")
    awaitAnswerMachinePrompt = field("awaitAnswerMachinePrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnswerMachineDetectionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnswerMachineDetectionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceIdFilter:
    boto3_raw_data: "type_defs.InstanceIdFilterTypeDef" = dataclasses.field()

    value = field("value")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceIdFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleOutput:
    boto3_raw_data: "type_defs.ScheduleOutputTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    refreshFrequency = field("refreshFrequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailChannelSubtypeParameters:
    boto3_raw_data: "type_defs.EmailChannelSubtypeParametersTypeDef" = (
        dataclasses.field()
    )

    destinationEmailAddress = field("destinationEmailAddress")
    templateParameters = field("templateParameters")
    connectSourceEmailAddress = field("connectSourceEmailAddress")
    templateArn = field("templateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EmailChannelSubtypeParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailChannelSubtypeParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsChannelSubtypeParameters:
    boto3_raw_data: "type_defs.SmsChannelSubtypeParametersTypeDef" = dataclasses.field()

    destinationPhoneNumber = field("destinationPhoneNumber")
    templateParameters = field("templateParameters")
    connectSourcePhoneNumberArn = field("connectSourcePhoneNumberArn")
    templateArn = field("templateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SmsChannelSubtypeParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsChannelSubtypeParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationLimit:
    boto3_raw_data: "type_defs.CommunicationLimitTypeDef" = dataclasses.field()

    maxCountPerRecipient = field("maxCountPerRecipient")
    frequency = field("frequency")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommunicationLimitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationLimitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalTimeZoneConfigOutput:
    boto3_raw_data: "type_defs.LocalTimeZoneConfigOutputTypeDef" = dataclasses.field()

    defaultTimeZone = field("defaultTimeZone")
    localTimeZoneDetection = field("localTimeZoneDetection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalTimeZoneConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalTimeZoneConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalTimeZoneConfig:
    boto3_raw_data: "type_defs.LocalTimeZoneConfigTypeDef" = dataclasses.field()

    defaultTimeZone = field("defaultTimeZone")
    localTimeZoneDetection = field("localTimeZoneDetection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalTimeZoneConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalTimeZoneConfigTypeDef"]
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
class CustomerProfilesIntegrationConfig:
    boto3_raw_data: "type_defs.CustomerProfilesIntegrationConfigTypeDef" = (
        dataclasses.field()
    )

    domainArn = field("domainArn")
    objectTypeNames = field("objectTypeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerProfilesIntegrationConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProfilesIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerProfilesIntegrationIdentifier:
    boto3_raw_data: "type_defs.CustomerProfilesIntegrationIdentifierTypeDef" = (
        dataclasses.field()
    )

    domainArn = field("domainArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerProfilesIntegrationIdentifierTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProfilesIntegrationIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerProfilesIntegrationSummary:
    boto3_raw_data: "type_defs.CustomerProfilesIntegrationSummaryTypeDef" = (
        dataclasses.field()
    )

    domainArn = field("domainArn")
    objectTypeNames = field("objectTypeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerProfilesIntegrationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProfilesIntegrationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignChannelSubtypeConfigRequest:
    boto3_raw_data: "type_defs.DeleteCampaignChannelSubtypeConfigRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    channelSubtype = field("channelSubtype")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCampaignChannelSubtypeConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignChannelSubtypeConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignCommunicationLimitsRequest:
    boto3_raw_data: "type_defs.DeleteCampaignCommunicationLimitsRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    config = field("config")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCampaignCommunicationLimitsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignCommunicationLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignCommunicationTimeRequest:
    boto3_raw_data: "type_defs.DeleteCampaignCommunicationTimeRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    config = field("config")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCampaignCommunicationTimeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignCommunicationTimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignRequest:
    boto3_raw_data: "type_defs.DeleteCampaignRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectInstanceConfigRequest:
    boto3_raw_data: "type_defs.DeleteConnectInstanceConfigRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")
    campaignDeletionPolicy = field("campaignDeletionPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConnectInstanceConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectInstanceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceOnboardingJobRequest:
    boto3_raw_data: "type_defs.DeleteInstanceOnboardingJobRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInstanceOnboardingJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceOnboardingJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCampaignRequest:
    boto3_raw_data: "type_defs.DescribeCampaignRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailOutboundConfig:
    boto3_raw_data: "type_defs.EmailOutboundConfigTypeDef" = dataclasses.field()

    connectSourceEmailAddress = field("connectSourceEmailAddress")
    wisdomTemplateArn = field("wisdomTemplateArn")
    sourceEmailAddressDisplayName = field("sourceEmailAddressDisplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailOutboundConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailOutboundConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailOutboundModeOutput:
    boto3_raw_data: "type_defs.EmailOutboundModeOutputTypeDef" = dataclasses.field()

    agentless = field("agentless")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailOutboundModeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailOutboundModeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailOutboundMode:
    boto3_raw_data: "type_defs.EmailOutboundModeTypeDef" = dataclasses.field()

    agentless = field("agentless")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailOutboundModeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailOutboundModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfig:
    boto3_raw_data: "type_defs.EncryptionConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")
    encryptionType = field("encryptionType")
    keyArn = field("keyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTrigger:
    boto3_raw_data: "type_defs.EventTriggerTypeDef" = dataclasses.field()

    customerProfilesDomainArn = field("customerProfilesDomainArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTriggerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedCampaignStateResponse:
    boto3_raw_data: "type_defs.FailedCampaignStateResponseTypeDef" = dataclasses.field()

    campaignId = field("campaignId")
    failureCode = field("failureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedCampaignStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedCampaignStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedProfileOutboundRequest:
    boto3_raw_data: "type_defs.FailedProfileOutboundRequestTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")
    id = field("id")
    failureCode = field("failureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedProfileOutboundRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedProfileOutboundRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedRequest:
    boto3_raw_data: "type_defs.FailedRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    id = field("id")
    failureCode = field("failureCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignStateBatchRequest:
    boto3_raw_data: "type_defs.GetCampaignStateBatchRequestTypeDef" = (
        dataclasses.field()
    )

    campaignIds = field("campaignIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignStateBatchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignStateBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulCampaignStateResponse:
    boto3_raw_data: "type_defs.SuccessfulCampaignStateResponseTypeDef" = (
        dataclasses.field()
    )

    campaignId = field("campaignId")
    state = field("state")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SuccessfulCampaignStateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulCampaignStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignStateRequest:
    boto3_raw_data: "type_defs.GetCampaignStateRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectInstanceConfigRequest:
    boto3_raw_data: "type_defs.GetConnectInstanceConfigRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetConnectInstanceConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectInstanceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceCommunicationLimitsRequest:
    boto3_raw_data: "type_defs.GetInstanceCommunicationLimitsRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInstanceCommunicationLimitsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceCommunicationLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceOnboardingJobStatusRequest:
    boto3_raw_data: "type_defs.GetInstanceOnboardingJobStatusRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInstanceOnboardingJobStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceOnboardingJobStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceOnboardingJobStatus:
    boto3_raw_data: "type_defs.InstanceOnboardingJobStatusTypeDef" = dataclasses.field()

    connectInstanceId = field("connectInstanceId")
    status = field("status")
    failureCode = field("failureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceOnboardingJobStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceOnboardingJobStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QConnectIntegrationConfig:
    boto3_raw_data: "type_defs.QConnectIntegrationConfigTypeDef" = dataclasses.field()

    knowledgeBaseArn = field("knowledgeBaseArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QConnectIntegrationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QConnectIntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QConnectIntegrationIdentifier:
    boto3_raw_data: "type_defs.QConnectIntegrationIdentifierTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseArn = field("knowledgeBaseArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QConnectIntegrationIdentifierTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QConnectIntegrationIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QConnectIntegrationSummary:
    boto3_raw_data: "type_defs.QConnectIntegrationSummaryTypeDef" = dataclasses.field()

    knowledgeBaseArn = field("knowledgeBaseArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QConnectIntegrationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QConnectIntegrationSummaryTypeDef"]
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
class ListConnectInstanceIntegrationsRequest:
    boto3_raw_data: "type_defs.ListConnectInstanceIntegrationsRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectInstanceIntegrationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectInstanceIntegrationsRequestTypeDef"]
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

    arn = field("arn")

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
class TimeRange:
    boto3_raw_data: "type_defs.TimeRangeTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseCampaignRequest:
    boto3_raw_data: "type_defs.PauseCampaignRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveConfig:
    boto3_raw_data: "type_defs.PredictiveConfigTypeDef" = dataclasses.field()

    bandwidthAllocation = field("bandwidthAllocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictiveConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProgressiveConfig:
    boto3_raw_data: "type_defs.ProgressiveConfigTypeDef" = dataclasses.field()

    bandwidthAllocation = field("bandwidthAllocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProgressiveConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProgressiveConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulRequest:
    boto3_raw_data: "type_defs.SuccessfulRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuccessfulRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulProfileOutboundRequest:
    boto3_raw_data: "type_defs.SuccessfulProfileOutboundRequestTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")
    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SuccessfulProfileOutboundRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulProfileOutboundRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestrictedPeriod:
    boto3_raw_data: "type_defs.RestrictedPeriodTypeDef" = dataclasses.field()

    startDate = field("startDate")
    endDate = field("endDate")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestrictedPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestrictedPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeCampaignRequest:
    boto3_raw_data: "type_defs.ResumeCampaignRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsOutboundConfig:
    boto3_raw_data: "type_defs.SmsOutboundConfigTypeDef" = dataclasses.field()

    connectSourcePhoneNumberArn = field("connectSourcePhoneNumberArn")
    wisdomTemplateArn = field("wisdomTemplateArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SmsOutboundConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsOutboundConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsOutboundModeOutput:
    boto3_raw_data: "type_defs.SmsOutboundModeOutputTypeDef" = dataclasses.field()

    agentless = field("agentless")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SmsOutboundModeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsOutboundModeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsOutboundMode:
    boto3_raw_data: "type_defs.SmsOutboundModeTypeDef" = dataclasses.field()

    agentless = field("agentless")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SmsOutboundModeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SmsOutboundModeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCampaignRequest:
    boto3_raw_data: "type_defs.StartCampaignRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCampaignRequest:
    boto3_raw_data: "type_defs.StopCampaignRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCampaignRequestTypeDef"]
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

    arn = field("arn")
    tags = field("tags")

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

    arn = field("arn")
    tagKeys = field("tagKeys")

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
class UpdateCampaignFlowAssociationRequest:
    boto3_raw_data: "type_defs.UpdateCampaignFlowAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    connectCampaignFlowArn = field("connectCampaignFlowArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCampaignFlowAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignFlowAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignNameRequest:
    boto3_raw_data: "type_defs.UpdateCampaignNameRequestTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyChannelSubtypeParameters:
    boto3_raw_data: "type_defs.TelephonyChannelSubtypeParametersTypeDef" = (
        dataclasses.field()
    )

    destinationPhoneNumber = field("destinationPhoneNumber")
    attributes = field("attributes")
    connectSourcePhoneNumber = field("connectSourcePhoneNumber")

    @cached_property
    def answerMachineDetectionConfig(self):  # pragma: no cover
        return AnswerMachineDetectionConfig.make_one(
            self.boto3_raw_data["answerMachineDetectionConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TelephonyChannelSubtypeParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyChannelSubtypeParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyOutboundConfig:
    boto3_raw_data: "type_defs.TelephonyOutboundConfigTypeDef" = dataclasses.field()

    connectContactFlowId = field("connectContactFlowId")
    connectSourcePhoneNumber = field("connectSourcePhoneNumber")

    @cached_property
    def answerMachineDetectionConfig(self):  # pragma: no cover
        return AnswerMachineDetectionConfig.make_one(
            self.boto3_raw_data["answerMachineDetectionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelephonyOutboundConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyOutboundConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignFilters:
    boto3_raw_data: "type_defs.CampaignFiltersTypeDef" = dataclasses.field()

    @cached_property
    def instanceIdFilter(self):  # pragma: no cover
        return InstanceIdFilter.make_one(self.boto3_raw_data["instanceIdFilter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignSummary:
    boto3_raw_data: "type_defs.CampaignSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    connectInstanceId = field("connectInstanceId")
    channelSubtypes = field("channelSubtypes")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleOutput.make_one(self.boto3_raw_data["schedule"])

    connectCampaignFlowArn = field("connectCampaignFlowArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationLimitsOutput:
    boto3_raw_data: "type_defs.CommunicationLimitsOutputTypeDef" = dataclasses.field()

    @cached_property
    def communicationLimitsList(self):  # pragma: no cover
        return CommunicationLimit.make_many(
            self.boto3_raw_data["communicationLimitsList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommunicationLimitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationLimitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationLimits:
    boto3_raw_data: "type_defs.CommunicationLimitsTypeDef" = dataclasses.field()

    @cached_property
    def communicationLimitsList(self):  # pragma: no cover
        return CommunicationLimit.make_many(
            self.boto3_raw_data["communicationLimitsList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommunicationLimitsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignResponse:
    boto3_raw_data: "type_defs.CreateCampaignResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignResponseTypeDef"]
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
class GetCampaignStateResponse:
    boto3_raw_data: "type_defs.GetCampaignStateResponseTypeDef" = dataclasses.field()

    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignStateResponseTypeDef"]
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

    tags = field("tags")

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
class EmailChannelSubtypeConfigOutput:
    boto3_raw_data: "type_defs.EmailChannelSubtypeConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outboundMode(self):  # pragma: no cover
        return EmailOutboundModeOutput.make_one(self.boto3_raw_data["outboundMode"])

    @cached_property
    def defaultOutboundConfig(self):  # pragma: no cover
        return EmailOutboundConfig.make_one(
            self.boto3_raw_data["defaultOutboundConfig"]
        )

    capacity = field("capacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EmailChannelSubtypeConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailChannelSubtypeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailChannelSubtypeConfig:
    boto3_raw_data: "type_defs.EmailChannelSubtypeConfigTypeDef" = dataclasses.field()

    @cached_property
    def outboundMode(self):  # pragma: no cover
        return EmailOutboundMode.make_one(self.boto3_raw_data["outboundMode"])

    @cached_property
    def defaultOutboundConfig(self):  # pragma: no cover
        return EmailOutboundConfig.make_one(
            self.boto3_raw_data["defaultOutboundConfig"]
        )

    capacity = field("capacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailChannelSubtypeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailChannelSubtypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfig:
    boto3_raw_data: "type_defs.InstanceConfigTypeDef" = dataclasses.field()

    connectInstanceId = field("connectInstanceId")
    serviceLinkedRoleArn = field("serviceLinkedRoleArn")

    @cached_property
    def encryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["encryptionConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceOnboardingJobRequest:
    boto3_raw_data: "type_defs.StartInstanceOnboardingJobRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @cached_property
    def encryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["encryptionConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartInstanceOnboardingJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceOnboardingJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    customerProfilesSegmentArn = field("customerProfilesSegmentArn")

    @cached_property
    def eventTrigger(self):  # pragma: no cover
        return EventTrigger.make_one(self.boto3_raw_data["eventTrigger"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignStateBatchResponse:
    boto3_raw_data: "type_defs.GetCampaignStateBatchResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successfulRequests(self):  # pragma: no cover
        return SuccessfulCampaignStateResponse.make_many(
            self.boto3_raw_data["successfulRequests"]
        )

    @cached_property
    def failedRequests(self):  # pragma: no cover
        return FailedCampaignStateResponse.make_many(
            self.boto3_raw_data["failedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCampaignStateBatchResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignStateBatchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceOnboardingJobStatusResponse:
    boto3_raw_data: "type_defs.GetInstanceOnboardingJobStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def connectInstanceOnboardingJobStatus(self):  # pragma: no cover
        return InstanceOnboardingJobStatus.make_one(
            self.boto3_raw_data["connectInstanceOnboardingJobStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInstanceOnboardingJobStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceOnboardingJobStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceOnboardingJobResponse:
    boto3_raw_data: "type_defs.StartInstanceOnboardingJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def connectInstanceOnboardingJobStatus(self):  # pragma: no cover
        return InstanceOnboardingJobStatus.make_one(
            self.boto3_raw_data["connectInstanceOnboardingJobStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartInstanceOnboardingJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceOnboardingJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationConfig:
    boto3_raw_data: "type_defs.IntegrationConfigTypeDef" = dataclasses.field()

    @cached_property
    def customerProfiles(self):  # pragma: no cover
        return CustomerProfilesIntegrationConfig.make_one(
            self.boto3_raw_data["customerProfiles"]
        )

    @cached_property
    def qConnect(self):  # pragma: no cover
        return QConnectIntegrationConfig.make_one(self.boto3_raw_data["qConnect"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegrationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationIdentifier:
    boto3_raw_data: "type_defs.IntegrationIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def customerProfiles(self):  # pragma: no cover
        return CustomerProfilesIntegrationIdentifier.make_one(
            self.boto3_raw_data["customerProfiles"]
        )

    @cached_property
    def qConnect(self):  # pragma: no cover
        return QConnectIntegrationIdentifier.make_one(self.boto3_raw_data["qConnect"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationSummary:
    boto3_raw_data: "type_defs.IntegrationSummaryTypeDef" = dataclasses.field()

    @cached_property
    def customerProfiles(self):  # pragma: no cover
        return CustomerProfilesIntegrationSummary.make_one(
            self.boto3_raw_data["customerProfiles"]
        )

    @cached_property
    def qConnect(self):  # pragma: no cover
        return QConnectIntegrationSummary.make_one(self.boto3_raw_data["qConnect"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectInstanceIntegrationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListConnectInstanceIntegrationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    connectInstanceId = field("connectInstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectInstanceIntegrationsRequestPaginateTypeDef"
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
                "type_defs.ListConnectInstanceIntegrationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenHoursOutput:
    boto3_raw_data: "type_defs.OpenHoursOutputTypeDef" = dataclasses.field()

    dailyHours = field("dailyHours")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenHoursOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenHoursOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenHours:
    boto3_raw_data: "type_defs.OpenHoursTypeDef" = dataclasses.field()

    dailyHours = field("dailyHours")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenHoursTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenHoursTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileOutboundRequest:
    boto3_raw_data: "type_defs.ProfileOutboundRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    profileId = field("profileId")
    expirationTime = field("expirationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileOutboundRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileOutboundRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    refreshFrequency = field("refreshFrequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyOutboundModeOutput:
    boto3_raw_data: "type_defs.TelephonyOutboundModeOutputTypeDef" = dataclasses.field()

    @cached_property
    def progressive(self):  # pragma: no cover
        return ProgressiveConfig.make_one(self.boto3_raw_data["progressive"])

    @cached_property
    def predictive(self):  # pragma: no cover
        return PredictiveConfig.make_one(self.boto3_raw_data["predictive"])

    agentless = field("agentless")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelephonyOutboundModeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyOutboundModeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyOutboundMode:
    boto3_raw_data: "type_defs.TelephonyOutboundModeTypeDef" = dataclasses.field()

    @cached_property
    def progressive(self):  # pragma: no cover
        return ProgressiveConfig.make_one(self.boto3_raw_data["progressive"])

    @cached_property
    def predictive(self):  # pragma: no cover
        return PredictiveConfig.make_one(self.boto3_raw_data["predictive"])

    agentless = field("agentless")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelephonyOutboundModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyOutboundModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOutboundRequestBatchResponse:
    boto3_raw_data: "type_defs.PutOutboundRequestBatchResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successfulRequests(self):  # pragma: no cover
        return SuccessfulRequest.make_many(self.boto3_raw_data["successfulRequests"])

    @cached_property
    def failedRequests(self):  # pragma: no cover
        return FailedRequest.make_many(self.boto3_raw_data["failedRequests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutOutboundRequestBatchResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOutboundRequestBatchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProfileOutboundRequestBatchResponse:
    boto3_raw_data: "type_defs.PutProfileOutboundRequestBatchResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successfulRequests(self):  # pragma: no cover
        return SuccessfulProfileOutboundRequest.make_many(
            self.boto3_raw_data["successfulRequests"]
        )

    @cached_property
    def failedRequests(self):  # pragma: no cover
        return FailedProfileOutboundRequest.make_many(
            self.boto3_raw_data["failedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutProfileOutboundRequestBatchResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProfileOutboundRequestBatchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestrictedPeriodsOutput:
    boto3_raw_data: "type_defs.RestrictedPeriodsOutputTypeDef" = dataclasses.field()

    @cached_property
    def restrictedPeriodList(self):  # pragma: no cover
        return RestrictedPeriod.make_many(self.boto3_raw_data["restrictedPeriodList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestrictedPeriodsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestrictedPeriodsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestrictedPeriods:
    boto3_raw_data: "type_defs.RestrictedPeriodsTypeDef" = dataclasses.field()

    @cached_property
    def restrictedPeriodList(self):  # pragma: no cover
        return RestrictedPeriod.make_many(self.boto3_raw_data["restrictedPeriodList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestrictedPeriodsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestrictedPeriodsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsChannelSubtypeConfigOutput:
    boto3_raw_data: "type_defs.SmsChannelSubtypeConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outboundMode(self):  # pragma: no cover
        return SmsOutboundModeOutput.make_one(self.boto3_raw_data["outboundMode"])

    @cached_property
    def defaultOutboundConfig(self):  # pragma: no cover
        return SmsOutboundConfig.make_one(self.boto3_raw_data["defaultOutboundConfig"])

    capacity = field("capacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SmsChannelSubtypeConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsChannelSubtypeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsChannelSubtypeConfig:
    boto3_raw_data: "type_defs.SmsChannelSubtypeConfigTypeDef" = dataclasses.field()

    @cached_property
    def outboundMode(self):  # pragma: no cover
        return SmsOutboundMode.make_one(self.boto3_raw_data["outboundMode"])

    @cached_property
    def defaultOutboundConfig(self):  # pragma: no cover
        return SmsOutboundConfig.make_one(self.boto3_raw_data["defaultOutboundConfig"])

    capacity = field("capacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SmsChannelSubtypeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SmsChannelSubtypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelSubtypeParameters:
    boto3_raw_data: "type_defs.ChannelSubtypeParametersTypeDef" = dataclasses.field()

    @cached_property
    def telephony(self):  # pragma: no cover
        return TelephonyChannelSubtypeParameters.make_one(
            self.boto3_raw_data["telephony"]
        )

    @cached_property
    def sms(self):  # pragma: no cover
        return SmsChannelSubtypeParameters.make_one(self.boto3_raw_data["sms"])

    @cached_property
    def email(self):  # pragma: no cover
        return EmailChannelSubtypeParameters.make_one(self.boto3_raw_data["email"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelSubtypeParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelSubtypeParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsRequestPaginate:
    boto3_raw_data: "type_defs.ListCampaignsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return CampaignFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsRequest:
    boto3_raw_data: "type_defs.ListCampaignsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filters(self):  # pragma: no cover
        return CampaignFilters.make_one(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsResponse:
    boto3_raw_data: "type_defs.ListCampaignsResponseTypeDef" = dataclasses.field()

    @cached_property
    def campaignSummaryList(self):  # pragma: no cover
        return CampaignSummary.make_many(self.boto3_raw_data["campaignSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationLimitsConfigOutput:
    boto3_raw_data: "type_defs.CommunicationLimitsConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def allChannelSubtypes(self):  # pragma: no cover
        return CommunicationLimitsOutput.make_one(
            self.boto3_raw_data["allChannelSubtypes"]
        )

    instanceLimitsHandling = field("instanceLimitsHandling")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CommunicationLimitsConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationLimitsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceCommunicationLimitsConfigOutput:
    boto3_raw_data: "type_defs.InstanceCommunicationLimitsConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def allChannelSubtypes(self):  # pragma: no cover
        return CommunicationLimitsOutput.make_one(
            self.boto3_raw_data["allChannelSubtypes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceCommunicationLimitsConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceCommunicationLimitsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationLimitsConfig:
    boto3_raw_data: "type_defs.CommunicationLimitsConfigTypeDef" = dataclasses.field()

    @cached_property
    def allChannelSubtypes(self):  # pragma: no cover
        return CommunicationLimits.make_one(self.boto3_raw_data["allChannelSubtypes"])

    instanceLimitsHandling = field("instanceLimitsHandling")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommunicationLimitsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationLimitsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceCommunicationLimitsConfig:
    boto3_raw_data: "type_defs.InstanceCommunicationLimitsConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def allChannelSubtypes(self):  # pragma: no cover
        return CommunicationLimits.make_one(self.boto3_raw_data["allChannelSubtypes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceCommunicationLimitsConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceCommunicationLimitsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectInstanceConfigResponse:
    boto3_raw_data: "type_defs.GetConnectInstanceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def connectInstanceConfig(self):  # pragma: no cover
        return InstanceConfig.make_one(self.boto3_raw_data["connectInstanceConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetConnectInstanceConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectInstanceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignSourceRequest:
    boto3_raw_data: "type_defs.UpdateCampaignSourceRequestTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConnectInstanceIntegrationRequest:
    boto3_raw_data: "type_defs.PutConnectInstanceIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @cached_property
    def integrationConfig(self):  # pragma: no cover
        return IntegrationConfig.make_one(self.boto3_raw_data["integrationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConnectInstanceIntegrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConnectInstanceIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectInstanceIntegrationRequest:
    boto3_raw_data: "type_defs.DeleteConnectInstanceIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")

    @cached_property
    def integrationIdentifier(self):  # pragma: no cover
        return IntegrationIdentifier.make_one(
            self.boto3_raw_data["integrationIdentifier"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConnectInstanceIntegrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectInstanceIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectInstanceIntegrationsResponse:
    boto3_raw_data: "type_defs.ListConnectInstanceIntegrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def integrationSummaryList(self):  # pragma: no cover
        return IntegrationSummary.make_many(
            self.boto3_raw_data["integrationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectInstanceIntegrationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectInstanceIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProfileOutboundRequestBatchRequest:
    boto3_raw_data: "type_defs.PutProfileOutboundRequestBatchRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def profileOutboundRequests(self):  # pragma: no cover
        return ProfileOutboundRequest.make_many(
            self.boto3_raw_data["profileOutboundRequests"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutProfileOutboundRequestBatchRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProfileOutboundRequestBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyChannelSubtypeConfigOutput:
    boto3_raw_data: "type_defs.TelephonyChannelSubtypeConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outboundMode(self):  # pragma: no cover
        return TelephonyOutboundModeOutput.make_one(self.boto3_raw_data["outboundMode"])

    @cached_property
    def defaultOutboundConfig(self):  # pragma: no cover
        return TelephonyOutboundConfig.make_one(
            self.boto3_raw_data["defaultOutboundConfig"]
        )

    capacity = field("capacity")
    connectQueueId = field("connectQueueId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TelephonyChannelSubtypeConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyChannelSubtypeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyChannelSubtypeConfig:
    boto3_raw_data: "type_defs.TelephonyChannelSubtypeConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outboundMode(self):  # pragma: no cover
        return TelephonyOutboundMode.make_one(self.boto3_raw_data["outboundMode"])

    @cached_property
    def defaultOutboundConfig(self):  # pragma: no cover
        return TelephonyOutboundConfig.make_one(
            self.boto3_raw_data["defaultOutboundConfig"]
        )

    capacity = field("capacity")
    connectQueueId = field("connectQueueId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TelephonyChannelSubtypeConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyChannelSubtypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeWindowOutput:
    boto3_raw_data: "type_defs.TimeWindowOutputTypeDef" = dataclasses.field()

    @cached_property
    def openHours(self):  # pragma: no cover
        return OpenHoursOutput.make_one(self.boto3_raw_data["openHours"])

    @cached_property
    def restrictedPeriods(self):  # pragma: no cover
        return RestrictedPeriodsOutput.make_one(
            self.boto3_raw_data["restrictedPeriods"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeWindowOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeWindowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeWindow:
    boto3_raw_data: "type_defs.TimeWindowTypeDef" = dataclasses.field()

    @cached_property
    def openHours(self):  # pragma: no cover
        return OpenHours.make_one(self.boto3_raw_data["openHours"])

    @cached_property
    def restrictedPeriods(self):  # pragma: no cover
        return RestrictedPeriods.make_one(self.boto3_raw_data["restrictedPeriods"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeWindowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundRequest:
    boto3_raw_data: "type_defs.OutboundRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    expirationTime = field("expirationTime")

    @cached_property
    def channelSubtypeParameters(self):  # pragma: no cover
        return ChannelSubtypeParameters.make_one(
            self.boto3_raw_data["channelSubtypeParameters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutboundRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutboundRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceCommunicationLimitsResponse:
    boto3_raw_data: "type_defs.GetInstanceCommunicationLimitsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def communicationLimitsConfig(self):  # pragma: no cover
        return InstanceCommunicationLimitsConfigOutput.make_one(
            self.boto3_raw_data["communicationLimitsConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInstanceCommunicationLimitsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceCommunicationLimitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignScheduleRequest:
    boto3_raw_data: "type_defs.UpdateCampaignScheduleRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    schedule = field("schedule")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCampaignScheduleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelSubtypeConfigOutput:
    boto3_raw_data: "type_defs.ChannelSubtypeConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def telephony(self):  # pragma: no cover
        return TelephonyChannelSubtypeConfigOutput.make_one(
            self.boto3_raw_data["telephony"]
        )

    @cached_property
    def sms(self):  # pragma: no cover
        return SmsChannelSubtypeConfigOutput.make_one(self.boto3_raw_data["sms"])

    @cached_property
    def email(self):  # pragma: no cover
        return EmailChannelSubtypeConfigOutput.make_one(self.boto3_raw_data["email"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelSubtypeConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelSubtypeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelSubtypeConfig:
    boto3_raw_data: "type_defs.ChannelSubtypeConfigTypeDef" = dataclasses.field()

    @cached_property
    def telephony(self):  # pragma: no cover
        return TelephonyChannelSubtypeConfig.make_one(self.boto3_raw_data["telephony"])

    @cached_property
    def sms(self):  # pragma: no cover
        return SmsChannelSubtypeConfig.make_one(self.boto3_raw_data["sms"])

    @cached_property
    def email(self):  # pragma: no cover
        return EmailChannelSubtypeConfig.make_one(self.boto3_raw_data["email"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelSubtypeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelSubtypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationTimeConfigOutput:
    boto3_raw_data: "type_defs.CommunicationTimeConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def localTimeZoneConfig(self):  # pragma: no cover
        return LocalTimeZoneConfigOutput.make_one(
            self.boto3_raw_data["localTimeZoneConfig"]
        )

    @cached_property
    def telephony(self):  # pragma: no cover
        return TimeWindowOutput.make_one(self.boto3_raw_data["telephony"])

    @cached_property
    def sms(self):  # pragma: no cover
        return TimeWindowOutput.make_one(self.boto3_raw_data["sms"])

    @cached_property
    def email(self):  # pragma: no cover
        return TimeWindowOutput.make_one(self.boto3_raw_data["email"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CommunicationTimeConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationTimeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommunicationTimeConfig:
    boto3_raw_data: "type_defs.CommunicationTimeConfigTypeDef" = dataclasses.field()

    @cached_property
    def localTimeZoneConfig(self):  # pragma: no cover
        return LocalTimeZoneConfig.make_one(self.boto3_raw_data["localTimeZoneConfig"])

    @cached_property
    def telephony(self):  # pragma: no cover
        return TimeWindow.make_one(self.boto3_raw_data["telephony"])

    @cached_property
    def sms(self):  # pragma: no cover
        return TimeWindow.make_one(self.boto3_raw_data["sms"])

    @cached_property
    def email(self):  # pragma: no cover
        return TimeWindow.make_one(self.boto3_raw_data["email"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommunicationTimeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommunicationTimeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOutboundRequestBatchRequest:
    boto3_raw_data: "type_defs.PutOutboundRequestBatchRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def outboundRequests(self):  # pragma: no cover
        return OutboundRequest.make_many(self.boto3_raw_data["outboundRequests"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutOutboundRequestBatchRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOutboundRequestBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignCommunicationLimitsRequest:
    boto3_raw_data: "type_defs.UpdateCampaignCommunicationLimitsRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    communicationLimitsOverride = field("communicationLimitsOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCampaignCommunicationLimitsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignCommunicationLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInstanceCommunicationLimitsRequest:
    boto3_raw_data: "type_defs.PutInstanceCommunicationLimitsRequestTypeDef" = (
        dataclasses.field()
    )

    connectInstanceId = field("connectInstanceId")
    communicationLimitsConfig = field("communicationLimitsConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutInstanceCommunicationLimitsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInstanceCommunicationLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Campaign:
    boto3_raw_data: "type_defs.CampaignTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    connectInstanceId = field("connectInstanceId")

    @cached_property
    def channelSubtypeConfig(self):  # pragma: no cover
        return ChannelSubtypeConfigOutput.make_one(
            self.boto3_raw_data["channelSubtypeConfig"]
        )

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    connectCampaignFlowArn = field("connectCampaignFlowArn")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleOutput.make_one(self.boto3_raw_data["schedule"])

    @cached_property
    def communicationTimeConfig(self):  # pragma: no cover
        return CommunicationTimeConfigOutput.make_one(
            self.boto3_raw_data["communicationTimeConfig"]
        )

    @cached_property
    def communicationLimitsOverride(self):  # pragma: no cover
        return CommunicationLimitsConfigOutput.make_one(
            self.boto3_raw_data["communicationLimitsOverride"]
        )

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignChannelSubtypeConfigRequest:
    boto3_raw_data: "type_defs.UpdateCampaignChannelSubtypeConfigRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    channelSubtypeConfig = field("channelSubtypeConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCampaignChannelSubtypeConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignChannelSubtypeConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCampaignResponse:
    boto3_raw_data: "type_defs.DescribeCampaignResponseTypeDef" = dataclasses.field()

    @cached_property
    def campaign(self):  # pragma: no cover
        return Campaign.make_one(self.boto3_raw_data["campaign"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignRequest:
    boto3_raw_data: "type_defs.CreateCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")
    connectInstanceId = field("connectInstanceId")
    channelSubtypeConfig = field("channelSubtypeConfig")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    connectCampaignFlowArn = field("connectCampaignFlowArn")
    schedule = field("schedule")
    communicationTimeConfig = field("communicationTimeConfig")
    communicationLimitsOverride = field("communicationLimitsOverride")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignCommunicationTimeRequest:
    boto3_raw_data: "type_defs.UpdateCampaignCommunicationTimeRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    communicationTimeConfig = field("communicationTimeConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCampaignCommunicationTimeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignCommunicationTimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
