# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectcampaigns import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AgentlessDialerConfig:
    boto3_raw_data: "type_defs.AgentlessDialerConfigTypeDef" = dataclasses.field()

    dialingCapacity = field("dialingCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentlessDialerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentlessDialerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


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
class CampaignSummary:
    boto3_raw_data: "type_defs.CampaignSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    connectInstanceId = field("connectInstanceId")

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
class PredictiveDialerConfig:
    boto3_raw_data: "type_defs.PredictiveDialerConfigTypeDef" = dataclasses.field()

    bandwidthAllocation = field("bandwidthAllocation")
    dialingCapacity = field("dialingCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictiveDialerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveDialerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProgressiveDialerConfig:
    boto3_raw_data: "type_defs.ProgressiveDialerConfigTypeDef" = dataclasses.field()

    bandwidthAllocation = field("bandwidthAllocation")
    dialingCapacity = field("dialingCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProgressiveDialerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProgressiveDialerConfigTypeDef"]
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
class OutboundCallConfig:
    boto3_raw_data: "type_defs.OutboundCallConfigTypeDef" = dataclasses.field()

    connectContactFlowId = field("connectContactFlowId")
    connectSourcePhoneNumber = field("connectSourcePhoneNumber")
    connectQueueId = field("connectQueueId")

    @cached_property
    def answerMachineDetectionConfig(self):  # pragma: no cover
        return AnswerMachineDetectionConfig.make_one(
            self.boto3_raw_data["answerMachineDetectionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundCallConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundCallConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignOutboundCallConfigRequest:
    boto3_raw_data: "type_defs.UpdateCampaignOutboundCallConfigRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    connectContactFlowId = field("connectContactFlowId")
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
            "type_defs.UpdateCampaignOutboundCallConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignOutboundCallConfigRequestTypeDef"]
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
class DialRequest:
    boto3_raw_data: "type_defs.DialRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    phoneNumber = field("phoneNumber")
    expirationTime = field("expirationTime")
    attributes = field("attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DialRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DialRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialerConfig:
    boto3_raw_data: "type_defs.DialerConfigTypeDef" = dataclasses.field()

    @cached_property
    def progressiveDialerConfig(self):  # pragma: no cover
        return ProgressiveDialerConfig.make_one(
            self.boto3_raw_data["progressiveDialerConfig"]
        )

    @cached_property
    def predictiveDialerConfig(self):  # pragma: no cover
        return PredictiveDialerConfig.make_one(
            self.boto3_raw_data["predictiveDialerConfig"]
        )

    @cached_property
    def agentlessDialerConfig(self):  # pragma: no cover
        return AgentlessDialerConfig.make_one(
            self.boto3_raw_data["agentlessDialerConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DialerConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DialerConfigTypeDef"]],
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
class PutDialRequestBatchResponse:
    boto3_raw_data: "type_defs.PutDialRequestBatchResponseTypeDef" = dataclasses.field()

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
        cls, boto3_raw_data: T.Optional["type_defs.PutDialRequestBatchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDialRequestBatchResponseTypeDef"]
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
class PutDialRequestBatchRequest:
    boto3_raw_data: "type_defs.PutDialRequestBatchRequestTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def dialRequests(self):  # pragma: no cover
        return DialRequest.make_many(self.boto3_raw_data["dialRequests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDialRequestBatchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDialRequestBatchRequestTypeDef"]
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
    def dialerConfig(self):  # pragma: no cover
        return DialerConfig.make_one(self.boto3_raw_data["dialerConfig"])

    @cached_property
    def outboundCallConfig(self):  # pragma: no cover
        return OutboundCallConfig.make_one(self.boto3_raw_data["outboundCallConfig"])

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
class CreateCampaignRequest:
    boto3_raw_data: "type_defs.CreateCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")
    connectInstanceId = field("connectInstanceId")

    @cached_property
    def dialerConfig(self):  # pragma: no cover
        return DialerConfig.make_one(self.boto3_raw_data["dialerConfig"])

    @cached_property
    def outboundCallConfig(self):  # pragma: no cover
        return OutboundCallConfig.make_one(self.boto3_raw_data["outboundCallConfig"])

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
class UpdateCampaignDialerConfigRequest:
    boto3_raw_data: "type_defs.UpdateCampaignDialerConfigRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def dialerConfig(self):  # pragma: no cover
        return DialerConfig.make_one(self.boto3_raw_data["dialerConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCampaignDialerConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignDialerConfigRequestTypeDef"]
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
