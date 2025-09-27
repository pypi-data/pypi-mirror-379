# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddTagsToStreamInput:
    boto3_raw_data: "type_defs.AddTagsToStreamInputTypeDef" = dataclasses.field()

    Tags = field("Tags")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HashKeyRange:
    boto3_raw_data: "type_defs.HashKeyRangeTypeDef" = dataclasses.field()

    StartingHashKey = field("StartingHashKey")
    EndingHashKey = field("EndingHashKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HashKeyRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HashKeyRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumerDescription:
    boto3_raw_data: "type_defs.ConsumerDescriptionTypeDef" = dataclasses.field()

    ConsumerName = field("ConsumerName")
    ConsumerARN = field("ConsumerARN")
    ConsumerStatus = field("ConsumerStatus")
    ConsumerCreationTimestamp = field("ConsumerCreationTimestamp")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsumerDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumerDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Consumer:
    boto3_raw_data: "type_defs.ConsumerTypeDef" = dataclasses.field()

    ConsumerName = field("ConsumerName")
    ConsumerARN = field("ConsumerARN")
    ConsumerStatus = field("ConsumerStatus")
    ConsumerCreationTimestamp = field("ConsumerCreationTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConsumerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConsumerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamModeDetails:
    boto3_raw_data: "type_defs.StreamModeDetailsTypeDef" = dataclasses.field()

    StreamMode = field("StreamMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamModeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamModeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecreaseStreamRetentionPeriodInput:
    boto3_raw_data: "type_defs.DecreaseStreamRetentionPeriodInputTypeDef" = (
        dataclasses.field()
    )

    RetentionPeriodHours = field("RetentionPeriodHours")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecreaseStreamRetentionPeriodInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecreaseStreamRetentionPeriodInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyInput:
    boto3_raw_data: "type_defs.DeleteResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStreamInput:
    boto3_raw_data: "type_defs.DeleteStreamInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    EnforceConsumerDeletion = field("EnforceConsumerDeletion")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterStreamConsumerInput:
    boto3_raw_data: "type_defs.DeregisterStreamConsumerInputTypeDef" = (
        dataclasses.field()
    )

    StreamARN = field("StreamARN")
    ConsumerName = field("ConsumerName")
    ConsumerARN = field("ConsumerARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterStreamConsumerInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterStreamConsumerInputTypeDef"]
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
class DescribeStreamConsumerInput:
    boto3_raw_data: "type_defs.DescribeStreamConsumerInputTypeDef" = dataclasses.field()

    StreamARN = field("StreamARN")
    ConsumerName = field("ConsumerName")
    ConsumerARN = field("ConsumerARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamConsumerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamConsumerInputTypeDef"]
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
class DescribeStreamInput:
    boto3_raw_data: "type_defs.DescribeStreamInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    Limit = field("Limit")
    ExclusiveStartShardId = field("ExclusiveStartShardId")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamSummaryInput:
    boto3_raw_data: "type_defs.DescribeStreamSummaryInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamSummaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableEnhancedMonitoringInput:
    boto3_raw_data: "type_defs.DisableEnhancedMonitoringInputTypeDef" = (
        dataclasses.field()
    )

    ShardLevelMetrics = field("ShardLevelMetrics")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableEnhancedMonitoringInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableEnhancedMonitoringInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableEnhancedMonitoringInput:
    boto3_raw_data: "type_defs.EnableEnhancedMonitoringInputTypeDef" = (
        dataclasses.field()
    )

    ShardLevelMetrics = field("ShardLevelMetrics")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableEnhancedMonitoringInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableEnhancedMonitoringInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnhancedMetrics:
    boto3_raw_data: "type_defs.EnhancedMetricsTypeDef" = dataclasses.field()

    ShardLevelMetrics = field("ShardLevelMetrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnhancedMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnhancedMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecordsInput:
    boto3_raw_data: "type_defs.GetRecordsInputTypeDef" = dataclasses.field()

    ShardIterator = field("ShardIterator")
    Limit = field("Limit")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRecordsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    SequenceNumber = field("SequenceNumber")
    Data = field("Data")
    PartitionKey = field("PartitionKey")
    ApproximateArrivalTimestamp = field("ApproximateArrivalTimestamp")
    EncryptionType = field("EncryptionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyInput:
    boto3_raw_data: "type_defs.GetResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncreaseStreamRetentionPeriodInput:
    boto3_raw_data: "type_defs.IncreaseStreamRetentionPeriodInputTypeDef" = (
        dataclasses.field()
    )

    RetentionPeriodHours = field("RetentionPeriodHours")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IncreaseStreamRetentionPeriodInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncreaseStreamRetentionPeriodInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalFailureException:
    boto3_raw_data: "type_defs.InternalFailureExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalFailureExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalFailureExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSAccessDeniedException:
    boto3_raw_data: "type_defs.KMSAccessDeniedExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KMSAccessDeniedExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSAccessDeniedExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSDisabledException:
    boto3_raw_data: "type_defs.KMSDisabledExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KMSDisabledExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSDisabledExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSInvalidStateException:
    boto3_raw_data: "type_defs.KMSInvalidStateExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KMSInvalidStateExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSInvalidStateExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSNotFoundException:
    boto3_raw_data: "type_defs.KMSNotFoundExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KMSNotFoundExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSNotFoundExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSOptInRequired:
    boto3_raw_data: "type_defs.KMSOptInRequiredTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KMSOptInRequiredTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSOptInRequiredTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSThrottlingException:
    boto3_raw_data: "type_defs.KMSThrottlingExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KMSThrottlingExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSThrottlingExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInput:
    boto3_raw_data: "type_defs.ListStreamsInputTypeDef" = dataclasses.field()

    Limit = field("Limit")
    ExclusiveStartStreamName = field("ExclusiveStartStreamName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
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
class ListTagsForStreamInput:
    boto3_raw_data: "type_defs.ListTagsForStreamInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    ExclusiveStartTagKey = field("ExclusiveStartTagKey")
    Limit = field("Limit")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeShardsInput:
    boto3_raw_data: "type_defs.MergeShardsInputTypeDef" = dataclasses.field()

    ShardToMerge = field("ShardToMerge")
    AdjacentShardToMerge = field("AdjacentShardToMerge")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MergeShardsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeShardsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordsResultEntry:
    boto3_raw_data: "type_defs.PutRecordsResultEntryTypeDef" = dataclasses.field()

    SequenceNumber = field("SequenceNumber")
    ShardId = field("ShardId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRecordsResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordsResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyInput:
    boto3_raw_data: "type_defs.PutResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterStreamConsumerInput:
    boto3_raw_data: "type_defs.RegisterStreamConsumerInputTypeDef" = dataclasses.field()

    StreamARN = field("StreamARN")
    ConsumerName = field("ConsumerName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterStreamConsumerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterStreamConsumerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromStreamInput:
    boto3_raw_data: "type_defs.RemoveTagsFromStreamInputTypeDef" = dataclasses.field()

    TagKeys = field("TagKeys")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsFromStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceInUseException:
    boto3_raw_data: "type_defs.ResourceInUseExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceInUseExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceInUseExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceNotFoundException:
    boto3_raw_data: "type_defs.ResourceNotFoundExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceNotFoundExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceNotFoundExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SequenceNumberRange:
    boto3_raw_data: "type_defs.SequenceNumberRangeTypeDef" = dataclasses.field()

    StartingSequenceNumber = field("StartingSequenceNumber")
    EndingSequenceNumber = field("EndingSequenceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SequenceNumberRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SequenceNumberRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplitShardInput:
    boto3_raw_data: "type_defs.SplitShardInputTypeDef" = dataclasses.field()

    ShardToSplit = field("ShardToSplit")
    NewStartingHashKey = field("NewStartingHashKey")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SplitShardInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SplitShardInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartStreamEncryptionInput:
    boto3_raw_data: "type_defs.StartStreamEncryptionInputTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KeyId = field("KeyId")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartStreamEncryptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartStreamEncryptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopStreamEncryptionInput:
    boto3_raw_data: "type_defs.StopStreamEncryptionInputTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KeyId = field("KeyId")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopStreamEncryptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopStreamEncryptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    Tags = field("Tags")
    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    TagKeys = field("TagKeys")
    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateShardCountInput:
    boto3_raw_data: "type_defs.UpdateShardCountInputTypeDef" = dataclasses.field()

    TargetShardCount = field("TargetShardCount")
    ScalingType = field("ScalingType")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateShardCountInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateShardCountInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordInput:
    boto3_raw_data: "type_defs.PutRecordInputTypeDef" = dataclasses.field()

    Data = field("Data")
    PartitionKey = field("PartitionKey")
    StreamName = field("StreamName")
    ExplicitHashKey = field("ExplicitHashKey")
    SequenceNumberForOrdering = field("SequenceNumberForOrdering")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRecordInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordsRequestEntry:
    boto3_raw_data: "type_defs.PutRecordsRequestEntryTypeDef" = dataclasses.field()

    Data = field("Data")
    PartitionKey = field("PartitionKey")
    ExplicitHashKey = field("ExplicitHashKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRecordsRequestEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordsRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildShard:
    boto3_raw_data: "type_defs.ChildShardTypeDef" = dataclasses.field()

    ShardId = field("ShardId")
    ParentShards = field("ParentShards")

    @cached_property
    def HashKeyRange(self):  # pragma: no cover
        return HashKeyRange.make_one(self.boto3_raw_data["HashKeyRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChildShardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChildShardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamInput:
    boto3_raw_data: "type_defs.CreateStreamInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    ShardCount = field("ShardCount")

    @cached_property
    def StreamModeDetails(self):  # pragma: no cover
        return StreamModeDetails.make_one(self.boto3_raw_data["StreamModeDetails"])

    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamSummary:
    boto3_raw_data: "type_defs.StreamSummaryTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    StreamStatus = field("StreamStatus")

    @cached_property
    def StreamModeDetails(self):  # pragma: no cover
        return StreamModeDetails.make_one(self.boto3_raw_data["StreamModeDetails"])

    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamModeInput:
    boto3_raw_data: "type_defs.UpdateStreamModeInputTypeDef" = dataclasses.field()

    StreamARN = field("StreamARN")

    @cached_property
    def StreamModeDetails(self):  # pragma: no cover
        return StreamModeDetails.make_one(self.boto3_raw_data["StreamModeDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStreamModeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamModeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLimitsOutput:
    boto3_raw_data: "type_defs.DescribeLimitsOutputTypeDef" = dataclasses.field()

    ShardLimit = field("ShardLimit")
    OpenShardCount = field("OpenShardCount")
    OnDemandStreamCount = field("OnDemandStreamCount")
    OnDemandStreamCountLimit = field("OnDemandStreamCountLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLimitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLimitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamConsumerOutput:
    boto3_raw_data: "type_defs.DescribeStreamConsumerOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConsumerDescription(self):  # pragma: no cover
        return ConsumerDescription.make_one(self.boto3_raw_data["ConsumerDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamConsumerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamConsumerOutputTypeDef"]
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
class EnhancedMonitoringOutput:
    boto3_raw_data: "type_defs.EnhancedMonitoringOutputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    CurrentShardLevelMetrics = field("CurrentShardLevelMetrics")
    DesiredShardLevelMetrics = field("DesiredShardLevelMetrics")
    StreamARN = field("StreamARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnhancedMonitoringOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnhancedMonitoringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyOutput:
    boto3_raw_data: "type_defs.GetResourcePolicyOutputTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShardIteratorOutput:
    boto3_raw_data: "type_defs.GetShardIteratorOutputTypeDef" = dataclasses.field()

    ShardIterator = field("ShardIterator")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShardIteratorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShardIteratorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamConsumersOutput:
    boto3_raw_data: "type_defs.ListStreamConsumersOutputTypeDef" = dataclasses.field()

    @cached_property
    def Consumers(self):  # pragma: no cover
        return Consumer.make_many(self.boto3_raw_data["Consumers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamConsumersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamConsumersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordOutput:
    boto3_raw_data: "type_defs.PutRecordOutputTypeDef" = dataclasses.field()

    ShardId = field("ShardId")
    SequenceNumber = field("SequenceNumber")
    EncryptionType = field("EncryptionType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRecordOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterStreamConsumerOutput:
    boto3_raw_data: "type_defs.RegisterStreamConsumerOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Consumer(self):  # pragma: no cover
        return Consumer.make_one(self.boto3_raw_data["Consumer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterStreamConsumerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterStreamConsumerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateShardCountOutput:
    boto3_raw_data: "type_defs.UpdateShardCountOutputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    CurrentShardCount = field("CurrentShardCount")
    TargetShardCount = field("TargetShardCount")
    StreamARN = field("StreamARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateShardCountOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateShardCountOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamInputPaginate:
    boto3_raw_data: "type_defs.DescribeStreamInputPaginateTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInputPaginate:
    boto3_raw_data: "type_defs.ListStreamsInputPaginateTypeDef" = dataclasses.field()

    ExclusiveStartStreamName = field("ExclusiveStartStreamName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeStreamInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    Limit = field("Limit")
    ExclusiveStartShardId = field("ExclusiveStartShardId")
    StreamARN = field("StreamARN")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamInputWait:
    boto3_raw_data: "type_defs.DescribeStreamInputWaitTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    Limit = field("Limit")
    ExclusiveStartShardId = field("ExclusiveStartShardId")
    StreamARN = field("StreamARN")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamDescriptionSummary:
    boto3_raw_data: "type_defs.StreamDescriptionSummaryTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    StreamStatus = field("StreamStatus")
    RetentionPeriodHours = field("RetentionPeriodHours")
    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @cached_property
    def EnhancedMonitoring(self):  # pragma: no cover
        return EnhancedMetrics.make_many(self.boto3_raw_data["EnhancedMonitoring"])

    OpenShardCount = field("OpenShardCount")

    @cached_property
    def StreamModeDetails(self):  # pragma: no cover
        return StreamModeDetails.make_one(self.boto3_raw_data["StreamModeDetails"])

    EncryptionType = field("EncryptionType")
    KeyId = field("KeyId")
    ConsumerCount = field("ConsumerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamDescriptionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamDescriptionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetShardIteratorInput:
    boto3_raw_data: "type_defs.GetShardIteratorInputTypeDef" = dataclasses.field()

    ShardId = field("ShardId")
    ShardIteratorType = field("ShardIteratorType")
    StreamName = field("StreamName")
    StartingSequenceNumber = field("StartingSequenceNumber")
    Timestamp = field("Timestamp")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetShardIteratorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetShardIteratorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamConsumersInputPaginate:
    boto3_raw_data: "type_defs.ListStreamConsumersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StreamARN = field("StreamARN")
    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStreamConsumersInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamConsumersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamConsumersInput:
    boto3_raw_data: "type_defs.ListStreamConsumersInputTypeDef" = dataclasses.field()

    StreamARN = field("StreamARN")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamConsumersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamConsumersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShardFilter:
    boto3_raw_data: "type_defs.ShardFilterTypeDef" = dataclasses.field()

    Type = field("Type")
    ShardId = field("ShardId")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartingPosition:
    boto3_raw_data: "type_defs.StartingPositionTypeDef" = dataclasses.field()

    Type = field("Type")
    SequenceNumber = field("SequenceNumber")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartingPositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartingPositionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForStreamOutput:
    boto3_raw_data: "type_defs.ListTagsForStreamOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    HasMoreTags = field("HasMoreTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordsOutput:
    boto3_raw_data: "type_defs.PutRecordsOutputTypeDef" = dataclasses.field()

    FailedRecordCount = field("FailedRecordCount")

    @cached_property
    def Records(self):  # pragma: no cover
        return PutRecordsResultEntry.make_many(self.boto3_raw_data["Records"])

    EncryptionType = field("EncryptionType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Shard:
    boto3_raw_data: "type_defs.ShardTypeDef" = dataclasses.field()

    ShardId = field("ShardId")

    @cached_property
    def HashKeyRange(self):  # pragma: no cover
        return HashKeyRange.make_one(self.boto3_raw_data["HashKeyRange"])

    @cached_property
    def SequenceNumberRange(self):  # pragma: no cover
        return SequenceNumberRange.make_one(self.boto3_raw_data["SequenceNumberRange"])

    ParentShardId = field("ParentShardId")
    AdjacentParentShardId = field("AdjacentParentShardId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShardTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordsInput:
    boto3_raw_data: "type_defs.PutRecordsInputTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return PutRecordsRequestEntry.make_many(self.boto3_raw_data["Records"])

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRecordsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecordsOutput:
    boto3_raw_data: "type_defs.GetRecordsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    NextShardIterator = field("NextShardIterator")
    MillisBehindLatest = field("MillisBehindLatest")

    @cached_property
    def ChildShards(self):  # pragma: no cover
        return ChildShard.make_many(self.boto3_raw_data["ChildShards"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRecordsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecordsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribeToShardEvent:
    boto3_raw_data: "type_defs.SubscribeToShardEventTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    ContinuationSequenceNumber = field("ContinuationSequenceNumber")
    MillisBehindLatest = field("MillisBehindLatest")

    @cached_property
    def ChildShards(self):  # pragma: no cover
        return ChildShard.make_many(self.boto3_raw_data["ChildShards"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribeToShardEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribeToShardEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsOutput:
    boto3_raw_data: "type_defs.ListStreamsOutputTypeDef" = dataclasses.field()

    StreamNames = field("StreamNames")
    HasMoreStreams = field("HasMoreStreams")

    @cached_property
    def StreamSummaries(self):  # pragma: no cover
        return StreamSummary.make_many(self.boto3_raw_data["StreamSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamSummaryOutput:
    boto3_raw_data: "type_defs.DescribeStreamSummaryOutputTypeDef" = dataclasses.field()

    @cached_property
    def StreamDescriptionSummary(self):  # pragma: no cover
        return StreamDescriptionSummary.make_one(
            self.boto3_raw_data["StreamDescriptionSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListShardsInputPaginate:
    boto3_raw_data: "type_defs.ListShardsInputPaginateTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    ExclusiveStartShardId = field("ExclusiveStartShardId")
    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @cached_property
    def ShardFilter(self):  # pragma: no cover
        return ShardFilter.make_one(self.boto3_raw_data["ShardFilter"])

    StreamARN = field("StreamARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListShardsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListShardsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListShardsInput:
    boto3_raw_data: "type_defs.ListShardsInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    NextToken = field("NextToken")
    ExclusiveStartShardId = field("ExclusiveStartShardId")
    MaxResults = field("MaxResults")
    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @cached_property
    def ShardFilter(self):  # pragma: no cover
        return ShardFilter.make_one(self.boto3_raw_data["ShardFilter"])

    StreamARN = field("StreamARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListShardsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListShardsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribeToShardInput:
    boto3_raw_data: "type_defs.SubscribeToShardInputTypeDef" = dataclasses.field()

    ConsumerARN = field("ConsumerARN")
    ShardId = field("ShardId")

    @cached_property
    def StartingPosition(self):  # pragma: no cover
        return StartingPosition.make_one(self.boto3_raw_data["StartingPosition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribeToShardInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribeToShardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListShardsOutput:
    boto3_raw_data: "type_defs.ListShardsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Shards(self):  # pragma: no cover
        return Shard.make_many(self.boto3_raw_data["Shards"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListShardsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListShardsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamDescription:
    boto3_raw_data: "type_defs.StreamDescriptionTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    StreamStatus = field("StreamStatus")

    @cached_property
    def Shards(self):  # pragma: no cover
        return Shard.make_many(self.boto3_raw_data["Shards"])

    HasMoreShards = field("HasMoreShards")
    RetentionPeriodHours = field("RetentionPeriodHours")
    StreamCreationTimestamp = field("StreamCreationTimestamp")

    @cached_property
    def EnhancedMonitoring(self):  # pragma: no cover
        return EnhancedMetrics.make_many(self.boto3_raw_data["EnhancedMonitoring"])

    @cached_property
    def StreamModeDetails(self):  # pragma: no cover
        return StreamModeDetails.make_one(self.boto3_raw_data["StreamModeDetails"])

    EncryptionType = field("EncryptionType")
    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribeToShardEventStream:
    boto3_raw_data: "type_defs.SubscribeToShardEventStreamTypeDef" = dataclasses.field()

    @cached_property
    def SubscribeToShardEvent(self):  # pragma: no cover
        return SubscribeToShardEvent.make_one(
            self.boto3_raw_data["SubscribeToShardEvent"]
        )

    @cached_property
    def ResourceNotFoundException(self):  # pragma: no cover
        return ResourceNotFoundException.make_one(
            self.boto3_raw_data["ResourceNotFoundException"]
        )

    @cached_property
    def ResourceInUseException(self):  # pragma: no cover
        return ResourceInUseException.make_one(
            self.boto3_raw_data["ResourceInUseException"]
        )

    @cached_property
    def KMSDisabledException(self):  # pragma: no cover
        return KMSDisabledException.make_one(
            self.boto3_raw_data["KMSDisabledException"]
        )

    @cached_property
    def KMSInvalidStateException(self):  # pragma: no cover
        return KMSInvalidStateException.make_one(
            self.boto3_raw_data["KMSInvalidStateException"]
        )

    @cached_property
    def KMSAccessDeniedException(self):  # pragma: no cover
        return KMSAccessDeniedException.make_one(
            self.boto3_raw_data["KMSAccessDeniedException"]
        )

    @cached_property
    def KMSNotFoundException(self):  # pragma: no cover
        return KMSNotFoundException.make_one(
            self.boto3_raw_data["KMSNotFoundException"]
        )

    @cached_property
    def KMSOptInRequired(self):  # pragma: no cover
        return KMSOptInRequired.make_one(self.boto3_raw_data["KMSOptInRequired"])

    @cached_property
    def KMSThrottlingException(self):  # pragma: no cover
        return KMSThrottlingException.make_one(
            self.boto3_raw_data["KMSThrottlingException"]
        )

    @cached_property
    def InternalFailureException(self):  # pragma: no cover
        return InternalFailureException.make_one(
            self.boto3_raw_data["InternalFailureException"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribeToShardEventStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribeToShardEventStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamOutput:
    boto3_raw_data: "type_defs.DescribeStreamOutputTypeDef" = dataclasses.field()

    @cached_property
    def StreamDescription(self):  # pragma: no cover
        return StreamDescription.make_one(self.boto3_raw_data["StreamDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribeToShardOutput:
    boto3_raw_data: "type_defs.SubscribeToShardOutputTypeDef" = dataclasses.field()

    EventStream = field("EventStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribeToShardOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribeToShardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
