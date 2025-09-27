# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sqs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddPermissionRequestQueueAddPermission:
    boto3_raw_data: "type_defs.AddPermissionRequestQueueAddPermissionTypeDef" = (
        dataclasses.field()
    )

    Label = field("Label")
    AWSAccountIds = field("AWSAccountIds")
    Actions = field("Actions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddPermissionRequestQueueAddPermissionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPermissionRequestQueueAddPermissionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddPermissionRequest:
    boto3_raw_data: "type_defs.AddPermissionRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    Label = field("Label")
    AWSAccountIds = field("AWSAccountIds")
    Actions = field("Actions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchResultErrorEntry:
    boto3_raw_data: "type_defs.BatchResultErrorEntryTypeDef" = dataclasses.field()

    Id = field("Id")
    SenderFault = field("SenderFault")
    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchResultErrorEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchResultErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMessageMoveTaskRequest:
    boto3_raw_data: "type_defs.CancelMessageMoveTaskRequestTypeDef" = (
        dataclasses.field()
    )

    TaskHandle = field("TaskHandle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelMessageMoveTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMessageMoveTaskRequestTypeDef"]
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
class ChangeMessageVisibilityBatchRequestEntry:
    boto3_raw_data: "type_defs.ChangeMessageVisibilityBatchRequestEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ReceiptHandle = field("ReceiptHandle")
    VisibilityTimeout = field("VisibilityTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeMessageVisibilityBatchRequestEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeMessageVisibilityBatchRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeMessageVisibilityBatchResultEntry:
    boto3_raw_data: "type_defs.ChangeMessageVisibilityBatchResultEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeMessageVisibilityBatchResultEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeMessageVisibilityBatchResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeMessageVisibilityRequestMessageChangeVisibility:
    boto3_raw_data: (
        "type_defs.ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef"
    ) = dataclasses.field()

    VisibilityTimeout = field("VisibilityTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef"
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
                "type_defs.ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeMessageVisibilityRequest:
    boto3_raw_data: "type_defs.ChangeMessageVisibilityRequestTypeDef" = (
        dataclasses.field()
    )

    QueueUrl = field("QueueUrl")
    ReceiptHandle = field("ReceiptHandle")
    VisibilityTimeout = field("VisibilityTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChangeMessageVisibilityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeMessageVisibilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueRequestServiceResourceCreateQueue:
    boto3_raw_data: "type_defs.CreateQueueRequestServiceResourceCreateQueueTypeDef" = (
        dataclasses.field()
    )

    QueueName = field("QueueName")
    Attributes = field("Attributes")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateQueueRequestServiceResourceCreateQueueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueRequestServiceResourceCreateQueueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueRequest:
    boto3_raw_data: "type_defs.CreateQueueRequestTypeDef" = dataclasses.field()

    QueueName = field("QueueName")
    Attributes = field("Attributes")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageBatchRequestEntry:
    boto3_raw_data: "type_defs.DeleteMessageBatchRequestEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ReceiptHandle = field("ReceiptHandle")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMessageBatchRequestEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageBatchRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageBatchResultEntry:
    boto3_raw_data: "type_defs.DeleteMessageBatchResultEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMessageBatchResultEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageBatchResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageRequest:
    boto3_raw_data: "type_defs.DeleteMessageRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    ReceiptHandle = field("ReceiptHandle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueueRequest:
    boto3_raw_data: "type_defs.DeleteQueueRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueAttributesRequest:
    boto3_raw_data: "type_defs.GetQueueAttributesRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    AttributeNames = field("AttributeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueUrlRequestServiceResourceGetQueueByName:
    boto3_raw_data: (
        "type_defs.GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef"
    ) = dataclasses.field()

    QueueName = field("QueueName")
    QueueOwnerAWSAccountId = field("QueueOwnerAWSAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef"
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
                "type_defs.GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueUrlRequest:
    boto3_raw_data: "type_defs.GetQueueUrlRequestTypeDef" = dataclasses.field()

    QueueName = field("QueueName")
    QueueOwnerAWSAccountId = field("QueueOwnerAWSAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueUrlRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueUrlRequestTypeDef"]
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
class ListDeadLetterSourceQueuesRequest:
    boto3_raw_data: "type_defs.ListDeadLetterSourceQueuesRequestTypeDef" = (
        dataclasses.field()
    )

    QueueUrl = field("QueueUrl")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeadLetterSourceQueuesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeadLetterSourceQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageMoveTasksRequest:
    boto3_raw_data: "type_defs.ListMessageMoveTasksRequestTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessageMoveTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageMoveTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageMoveTasksResultEntry:
    boto3_raw_data: "type_defs.ListMessageMoveTasksResultEntryTypeDef" = (
        dataclasses.field()
    )

    TaskHandle = field("TaskHandle")
    Status = field("Status")
    SourceArn = field("SourceArn")
    DestinationArn = field("DestinationArn")
    MaxNumberOfMessagesPerSecond = field("MaxNumberOfMessagesPerSecond")
    ApproximateNumberOfMessagesMoved = field("ApproximateNumberOfMessagesMoved")
    ApproximateNumberOfMessagesToMove = field("ApproximateNumberOfMessagesToMove")
    FailureReason = field("FailureReason")
    StartedTimestamp = field("StartedTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMessageMoveTasksResultEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageMoveTasksResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueTagsRequest:
    boto3_raw_data: "type_defs.ListQueueTagsRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueueTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequest:
    boto3_raw_data: "type_defs.ListQueuesRequestTypeDef" = dataclasses.field()

    QueueNamePrefix = field("QueueNamePrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQueuesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesRequestTypeDef"]
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

    DataType = field("DataType")
    StringValue = field("StringValue")
    BinaryValue = field("BinaryValue")
    StringListValues = field("StringListValues")
    BinaryListValues = field("BinaryListValues")

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
class PurgeQueueRequest:
    boto3_raw_data: "type_defs.PurgeQueueRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PurgeQueueRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurgeQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiveMessageRequestQueueReceiveMessages:
    boto3_raw_data: "type_defs.ReceiveMessageRequestQueueReceiveMessagesTypeDef" = (
        dataclasses.field()
    )

    AttributeNames = field("AttributeNames")
    MessageSystemAttributeNames = field("MessageSystemAttributeNames")
    MessageAttributeNames = field("MessageAttributeNames")
    MaxNumberOfMessages = field("MaxNumberOfMessages")
    VisibilityTimeout = field("VisibilityTimeout")
    WaitTimeSeconds = field("WaitTimeSeconds")
    ReceiveRequestAttemptId = field("ReceiveRequestAttemptId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReceiveMessageRequestQueueReceiveMessagesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceiveMessageRequestQueueReceiveMessagesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiveMessageRequest:
    boto3_raw_data: "type_defs.ReceiveMessageRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    AttributeNames = field("AttributeNames")
    MessageSystemAttributeNames = field("MessageSystemAttributeNames")
    MessageAttributeNames = field("MessageAttributeNames")
    MaxNumberOfMessages = field("MaxNumberOfMessages")
    VisibilityTimeout = field("VisibilityTimeout")
    WaitTimeSeconds = field("WaitTimeSeconds")
    ReceiveRequestAttemptId = field("ReceiveRequestAttemptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReceiveMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceiveMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemovePermissionRequestQueueRemovePermission:
    boto3_raw_data: "type_defs.RemovePermissionRequestQueueRemovePermissionTypeDef" = (
        dataclasses.field()
    )

    Label = field("Label")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemovePermissionRequestQueueRemovePermissionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemovePermissionRequestQueueRemovePermissionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemovePermissionRequest:
    boto3_raw_data: "type_defs.RemovePermissionRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    Label = field("Label")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemovePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemovePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageBatchResultEntry:
    boto3_raw_data: "type_defs.SendMessageBatchResultEntryTypeDef" = dataclasses.field()

    Id = field("Id")
    MessageId = field("MessageId")
    MD5OfMessageBody = field("MD5OfMessageBody")
    MD5OfMessageAttributes = field("MD5OfMessageAttributes")
    MD5OfMessageSystemAttributes = field("MD5OfMessageSystemAttributes")
    SequenceNumber = field("SequenceNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageBatchResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageBatchResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetQueueAttributesRequestQueueSetAttributes:
    boto3_raw_data: "type_defs.SetQueueAttributesRequestQueueSetAttributesTypeDef" = (
        dataclasses.field()
    )

    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetQueueAttributesRequestQueueSetAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetQueueAttributesRequestQueueSetAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetQueueAttributesRequest:
    boto3_raw_data: "type_defs.SetQueueAttributesRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetQueueAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetQueueAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMessageMoveTaskRequest:
    boto3_raw_data: "type_defs.StartMessageMoveTaskRequestTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    DestinationArn = field("DestinationArn")
    MaxNumberOfMessagesPerSecond = field("MaxNumberOfMessagesPerSecond")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMessageMoveTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMessageMoveTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagQueueRequest:
    boto3_raw_data: "type_defs.TagQueueRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagQueueRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagQueueRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagQueueRequest:
    boto3_raw_data: "type_defs.UntagQueueRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UntagQueueRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagQueueRequestTypeDef"]
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

    DataType = field("DataType")
    StringValue = field("StringValue")
    BinaryValue = field("BinaryValue")
    StringListValues = field("StringListValues")
    BinaryListValues = field("BinaryListValues")

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
class MessageSystemAttributeValue:
    boto3_raw_data: "type_defs.MessageSystemAttributeValueTypeDef" = dataclasses.field()

    DataType = field("DataType")
    StringValue = field("StringValue")
    BinaryValue = field("BinaryValue")
    StringListValues = field("StringListValues")
    BinaryListValues = field("BinaryListValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageSystemAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageSystemAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMessageMoveTaskResult:
    boto3_raw_data: "type_defs.CancelMessageMoveTaskResultTypeDef" = dataclasses.field()

    ApproximateNumberOfMessagesMoved = field("ApproximateNumberOfMessagesMoved")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelMessageMoveTaskResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMessageMoveTaskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueResult:
    boto3_raw_data: "type_defs.CreateQueueResultTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateQueueResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueResultTypeDef"]
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
class GetQueueAttributesResult:
    boto3_raw_data: "type_defs.GetQueueAttributesResultTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueAttributesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueUrlResult:
    boto3_raw_data: "type_defs.GetQueueUrlResultTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueUrlResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueUrlResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeadLetterSourceQueuesResult:
    boto3_raw_data: "type_defs.ListDeadLetterSourceQueuesResultTypeDef" = (
        dataclasses.field()
    )

    queueUrls = field("queueUrls")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeadLetterSourceQueuesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeadLetterSourceQueuesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueTagsResult:
    boto3_raw_data: "type_defs.ListQueueTagsResultTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueueTagsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueTagsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesResult:
    boto3_raw_data: "type_defs.ListQueuesResultTypeDef" = dataclasses.field()

    QueueUrls = field("QueueUrls")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQueuesResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageResult:
    boto3_raw_data: "type_defs.SendMessageResultTypeDef" = dataclasses.field()

    MD5OfMessageBody = field("MD5OfMessageBody")
    MD5OfMessageAttributes = field("MD5OfMessageAttributes")
    MD5OfMessageSystemAttributes = field("MD5OfMessageSystemAttributes")
    MessageId = field("MessageId")
    SequenceNumber = field("SequenceNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendMessageResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMessageMoveTaskResult:
    boto3_raw_data: "type_defs.StartMessageMoveTaskResultTypeDef" = dataclasses.field()

    TaskHandle = field("TaskHandle")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMessageMoveTaskResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMessageMoveTaskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatch:
    boto3_raw_data: "type_defs.ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef" = (dataclasses.field())

    @cached_property
    def Entries(self):  # pragma: no cover
        return ChangeMessageVisibilityBatchRequestEntry.make_many(
            self.boto3_raw_data["Entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef"
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
                "type_defs.ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeMessageVisibilityBatchRequest:
    boto3_raw_data: "type_defs.ChangeMessageVisibilityBatchRequestTypeDef" = (
        dataclasses.field()
    )

    QueueUrl = field("QueueUrl")

    @cached_property
    def Entries(self):  # pragma: no cover
        return ChangeMessageVisibilityBatchRequestEntry.make_many(
            self.boto3_raw_data["Entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeMessageVisibilityBatchRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeMessageVisibilityBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeMessageVisibilityBatchResult:
    boto3_raw_data: "type_defs.ChangeMessageVisibilityBatchResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Successful(self):  # pragma: no cover
        return ChangeMessageVisibilityBatchResultEntry.make_many(
            self.boto3_raw_data["Successful"]
        )

    @cached_property
    def Failed(self):  # pragma: no cover
        return BatchResultErrorEntry.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeMessageVisibilityBatchResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeMessageVisibilityBatchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageBatchRequestQueueDeleteMessages:
    boto3_raw_data: "type_defs.DeleteMessageBatchRequestQueueDeleteMessagesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entries(self):  # pragma: no cover
        return DeleteMessageBatchRequestEntry.make_many(self.boto3_raw_data["Entries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMessageBatchRequestQueueDeleteMessagesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageBatchRequestQueueDeleteMessagesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageBatchRequest:
    boto3_raw_data: "type_defs.DeleteMessageBatchRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @cached_property
    def Entries(self):  # pragma: no cover
        return DeleteMessageBatchRequestEntry.make_many(self.boto3_raw_data["Entries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMessageBatchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMessageBatchResult:
    boto3_raw_data: "type_defs.DeleteMessageBatchResultTypeDef" = dataclasses.field()

    @cached_property
    def Successful(self):  # pragma: no cover
        return DeleteMessageBatchResultEntry.make_many(
            self.boto3_raw_data["Successful"]
        )

    @cached_property
    def Failed(self):  # pragma: no cover
        return BatchResultErrorEntry.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMessageBatchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMessageBatchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeadLetterSourceQueuesRequestPaginate:
    boto3_raw_data: "type_defs.ListDeadLetterSourceQueuesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    QueueUrl = field("QueueUrl")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeadLetterSourceQueuesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeadLetterSourceQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequestPaginate:
    boto3_raw_data: "type_defs.ListQueuesRequestPaginateTypeDef" = dataclasses.field()

    QueueNamePrefix = field("QueueNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMessageMoveTasksResult:
    boto3_raw_data: "type_defs.ListMessageMoveTasksResultTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return ListMessageMoveTasksResultEntry.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMessageMoveTasksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMessageMoveTasksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    ReceiptHandle = field("ReceiptHandle")
    MD5OfBody = field("MD5OfBody")
    Body = field("Body")
    Attributes = field("Attributes")
    MD5OfMessageAttributes = field("MD5OfMessageAttributes")
    MessageAttributes = field("MessageAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageBatchResult:
    boto3_raw_data: "type_defs.SendMessageBatchResultTypeDef" = dataclasses.field()

    @cached_property
    def Successful(self):  # pragma: no cover
        return SendMessageBatchResultEntry.make_many(self.boto3_raw_data["Successful"])

    @cached_property
    def Failed(self):  # pragma: no cover
        return BatchResultErrorEntry.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageBatchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageBatchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiveMessageResult:
    boto3_raw_data: "type_defs.ReceiveMessageResultTypeDef" = dataclasses.field()

    @cached_property
    def Messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["Messages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReceiveMessageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceiveMessageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageBatchRequestEntry:
    boto3_raw_data: "type_defs.SendMessageBatchRequestEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    MessageBody = field("MessageBody")
    DelaySeconds = field("DelaySeconds")
    MessageAttributes = field("MessageAttributes")
    MessageSystemAttributes = field("MessageSystemAttributes")
    MessageDeduplicationId = field("MessageDeduplicationId")
    MessageGroupId = field("MessageGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageBatchRequestEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageBatchRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageRequestQueueSendMessage:
    boto3_raw_data: "type_defs.SendMessageRequestQueueSendMessageTypeDef" = (
        dataclasses.field()
    )

    MessageBody = field("MessageBody")
    DelaySeconds = field("DelaySeconds")
    MessageAttributes = field("MessageAttributes")
    MessageSystemAttributes = field("MessageSystemAttributes")
    MessageDeduplicationId = field("MessageDeduplicationId")
    MessageGroupId = field("MessageGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendMessageRequestQueueSendMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageRequestQueueSendMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageRequest:
    boto3_raw_data: "type_defs.SendMessageRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")
    MessageBody = field("MessageBody")
    DelaySeconds = field("DelaySeconds")
    MessageAttributes = field("MessageAttributes")
    MessageSystemAttributes = field("MessageSystemAttributes")
    MessageDeduplicationId = field("MessageDeduplicationId")
    MessageGroupId = field("MessageGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageBatchRequestQueueSendMessages:
    boto3_raw_data: "type_defs.SendMessageBatchRequestQueueSendMessagesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Entries(self):  # pragma: no cover
        return SendMessageBatchRequestEntry.make_many(self.boto3_raw_data["Entries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendMessageBatchRequestQueueSendMessagesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageBatchRequestQueueSendMessagesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageBatchRequest:
    boto3_raw_data: "type_defs.SendMessageBatchRequestTypeDef" = dataclasses.field()

    QueueUrl = field("QueueUrl")

    @cached_property
    def Entries(self):  # pragma: no cover
        return SendMessageBatchRequestEntry.make_many(self.boto3_raw_data["Entries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageBatchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
