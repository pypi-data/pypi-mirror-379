# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sqs import type_defs as bs_td


class SQSCaster:

    def add_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_message_move_task(
        self,
        res: "bs_td.CancelMessageMoveTaskResultTypeDef",
    ) -> "dc_td.CancelMessageMoveTaskResult":
        return dc_td.CancelMessageMoveTaskResult.make_one(res)

    def change_message_visibility(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def change_message_visibility_batch(
        self,
        res: "bs_td.ChangeMessageVisibilityBatchResultTypeDef",
    ) -> "dc_td.ChangeMessageVisibilityBatchResult":
        return dc_td.ChangeMessageVisibilityBatchResult.make_one(res)

    def create_queue(
        self,
        res: "bs_td.CreateQueueResultTypeDef",
    ) -> "dc_td.CreateQueueResult":
        return dc_td.CreateQueueResult.make_one(res)

    def delete_message(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_message_batch(
        self,
        res: "bs_td.DeleteMessageBatchResultTypeDef",
    ) -> "dc_td.DeleteMessageBatchResult":
        return dc_td.DeleteMessageBatchResult.make_one(res)

    def delete_queue(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_queue_attributes(
        self,
        res: "bs_td.GetQueueAttributesResultTypeDef",
    ) -> "dc_td.GetQueueAttributesResult":
        return dc_td.GetQueueAttributesResult.make_one(res)

    def get_queue_url(
        self,
        res: "bs_td.GetQueueUrlResultTypeDef",
    ) -> "dc_td.GetQueueUrlResult":
        return dc_td.GetQueueUrlResult.make_one(res)

    def list_dead_letter_source_queues(
        self,
        res: "bs_td.ListDeadLetterSourceQueuesResultTypeDef",
    ) -> "dc_td.ListDeadLetterSourceQueuesResult":
        return dc_td.ListDeadLetterSourceQueuesResult.make_one(res)

    def list_message_move_tasks(
        self,
        res: "bs_td.ListMessageMoveTasksResultTypeDef",
    ) -> "dc_td.ListMessageMoveTasksResult":
        return dc_td.ListMessageMoveTasksResult.make_one(res)

    def list_queue_tags(
        self,
        res: "bs_td.ListQueueTagsResultTypeDef",
    ) -> "dc_td.ListQueueTagsResult":
        return dc_td.ListQueueTagsResult.make_one(res)

    def list_queues(
        self,
        res: "bs_td.ListQueuesResultTypeDef",
    ) -> "dc_td.ListQueuesResult":
        return dc_td.ListQueuesResult.make_one(res)

    def purge_queue(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def receive_message(
        self,
        res: "bs_td.ReceiveMessageResultTypeDef",
    ) -> "dc_td.ReceiveMessageResult":
        return dc_td.ReceiveMessageResult.make_one(res)

    def remove_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def send_message(
        self,
        res: "bs_td.SendMessageResultTypeDef",
    ) -> "dc_td.SendMessageResult":
        return dc_td.SendMessageResult.make_one(res)

    def send_message_batch(
        self,
        res: "bs_td.SendMessageBatchResultTypeDef",
    ) -> "dc_td.SendMessageBatchResult":
        return dc_td.SendMessageBatchResult.make_one(res)

    def set_queue_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_message_move_task(
        self,
        res: "bs_td.StartMessageMoveTaskResultTypeDef",
    ) -> "dc_td.StartMessageMoveTaskResult":
        return dc_td.StartMessageMoveTaskResult.make_one(res)

    def tag_queue(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_queue(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


sqs_caster = SQSCaster()
