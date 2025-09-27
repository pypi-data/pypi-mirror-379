# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesis import type_defs as bs_td


class KINESISCaster:

    def add_tags_to_stream(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_stream(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def decrease_stream_retention_period(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stream(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_stream_consumer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_limits(
        self,
        res: "bs_td.DescribeLimitsOutputTypeDef",
    ) -> "dc_td.DescribeLimitsOutput":
        return dc_td.DescribeLimitsOutput.make_one(res)

    def describe_stream(
        self,
        res: "bs_td.DescribeStreamOutputTypeDef",
    ) -> "dc_td.DescribeStreamOutput":
        return dc_td.DescribeStreamOutput.make_one(res)

    def describe_stream_consumer(
        self,
        res: "bs_td.DescribeStreamConsumerOutputTypeDef",
    ) -> "dc_td.DescribeStreamConsumerOutput":
        return dc_td.DescribeStreamConsumerOutput.make_one(res)

    def describe_stream_summary(
        self,
        res: "bs_td.DescribeStreamSummaryOutputTypeDef",
    ) -> "dc_td.DescribeStreamSummaryOutput":
        return dc_td.DescribeStreamSummaryOutput.make_one(res)

    def disable_enhanced_monitoring(
        self,
        res: "bs_td.EnhancedMonitoringOutputTypeDef",
    ) -> "dc_td.EnhancedMonitoringOutput":
        return dc_td.EnhancedMonitoringOutput.make_one(res)

    def enable_enhanced_monitoring(
        self,
        res: "bs_td.EnhancedMonitoringOutputTypeDef",
    ) -> "dc_td.EnhancedMonitoringOutput":
        return dc_td.EnhancedMonitoringOutput.make_one(res)

    def get_records(
        self,
        res: "bs_td.GetRecordsOutputTypeDef",
    ) -> "dc_td.GetRecordsOutput":
        return dc_td.GetRecordsOutput.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyOutputTypeDef",
    ) -> "dc_td.GetResourcePolicyOutput":
        return dc_td.GetResourcePolicyOutput.make_one(res)

    def get_shard_iterator(
        self,
        res: "bs_td.GetShardIteratorOutputTypeDef",
    ) -> "dc_td.GetShardIteratorOutput":
        return dc_td.GetShardIteratorOutput.make_one(res)

    def increase_stream_retention_period(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def list_shards(
        self,
        res: "bs_td.ListShardsOutputTypeDef",
    ) -> "dc_td.ListShardsOutput":
        return dc_td.ListShardsOutput.make_one(res)

    def list_stream_consumers(
        self,
        res: "bs_td.ListStreamConsumersOutputTypeDef",
    ) -> "dc_td.ListStreamConsumersOutput":
        return dc_td.ListStreamConsumersOutput.make_one(res)

    def list_streams(
        self,
        res: "bs_td.ListStreamsOutputTypeDef",
    ) -> "dc_td.ListStreamsOutput":
        return dc_td.ListStreamsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_tags_for_stream(
        self,
        res: "bs_td.ListTagsForStreamOutputTypeDef",
    ) -> "dc_td.ListTagsForStreamOutput":
        return dc_td.ListTagsForStreamOutput.make_one(res)

    def merge_shards(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_record(
        self,
        res: "bs_td.PutRecordOutputTypeDef",
    ) -> "dc_td.PutRecordOutput":
        return dc_td.PutRecordOutput.make_one(res)

    def put_records(
        self,
        res: "bs_td.PutRecordsOutputTypeDef",
    ) -> "dc_td.PutRecordsOutput":
        return dc_td.PutRecordsOutput.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_stream_consumer(
        self,
        res: "bs_td.RegisterStreamConsumerOutputTypeDef",
    ) -> "dc_td.RegisterStreamConsumerOutput":
        return dc_td.RegisterStreamConsumerOutput.make_one(res)

    def remove_tags_from_stream(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def split_shard(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_stream_encryption(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_stream_encryption(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def subscribe_to_shard(
        self,
        res: "bs_td.SubscribeToShardOutputTypeDef",
    ) -> "dc_td.SubscribeToShardOutput":
        return dc_td.SubscribeToShardOutput.make_one(res)

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

    def update_shard_count(
        self,
        res: "bs_td.UpdateShardCountOutputTypeDef",
    ) -> "dc_td.UpdateShardCountOutput":
        return dc_td.UpdateShardCountOutput.make_one(res)

    def update_stream_mode(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


kinesis_caster = KINESISCaster()
