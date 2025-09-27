# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_braket import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActionMetadata:
    boto3_raw_data: "type_defs.ActionMetadataTypeDef" = dataclasses.field()

    actionType = field("actionType")
    programCount = field("programCount")
    executableCount = field("executableCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerImage:
    boto3_raw_data: "type_defs.ContainerImageTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerImageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScriptModeConfig:
    boto3_raw_data: "type_defs.ScriptModeConfigTypeDef" = dataclasses.field()

    entryPoint = field("entryPoint")
    s3Uri = field("s3Uri")
    compressionType = field("compressionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptModeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScriptModeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Association:
    boto3_raw_data: "type_defs.AssociationTypeDef" = dataclasses.field()

    arn = field("arn")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssociationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRequest:
    boto3_raw_data: "type_defs.CancelJobRequestTypeDef" = dataclasses.field()

    jobArn = field("jobArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRequestTypeDef"]
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
class CancelQuantumTaskRequest:
    boto3_raw_data: "type_defs.CancelQuantumTaskRequestTypeDef" = dataclasses.field()

    quantumTaskArn = field("quantumTaskArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelQuantumTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQuantumTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceConfig:
    boto3_raw_data: "type_defs.DeviceConfigTypeDef" = dataclasses.field()

    device = field("device")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfig:
    boto3_raw_data: "type_defs.InstanceConfigTypeDef" = dataclasses.field()

    instanceType = field("instanceType")
    volumeSizeInGb = field("volumeSizeInGb")
    instanceCount = field("instanceCount")

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
class JobCheckpointConfig:
    boto3_raw_data: "type_defs.JobCheckpointConfigTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")
    localPath = field("localPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobCheckpointConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobCheckpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobOutputDataConfig:
    boto3_raw_data: "type_defs.JobOutputDataConfigTypeDef" = dataclasses.field()

    s3Path = field("s3Path")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobOutputDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobStoppingCondition:
    boto3_raw_data: "type_defs.JobStoppingConditionTypeDef" = dataclasses.field()

    maxRuntimeInSeconds = field("maxRuntimeInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobStoppingConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobStoppingConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSource:
    boto3_raw_data: "type_defs.S3DataSourceTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DataSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceQueueInfo:
    boto3_raw_data: "type_defs.DeviceQueueInfoTypeDef" = dataclasses.field()

    queue = field("queue")
    queueSize = field("queueSize")
    queuePriority = field("queuePriority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceQueueInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceQueueInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceSummary:
    boto3_raw_data: "type_defs.DeviceSummaryTypeDef" = dataclasses.field()

    deviceArn = field("deviceArn")
    deviceName = field("deviceName")
    providerName = field("providerName")
    deviceType = field("deviceType")
    deviceStatus = field("deviceStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceRequest:
    boto3_raw_data: "type_defs.GetDeviceRequestTypeDef" = dataclasses.field()

    deviceArn = field("deviceArn")

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
class GetJobRequest:
    boto3_raw_data: "type_defs.GetJobRequestTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    additionalAttributeNames = field("additionalAttributeNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridJobQueueInfo:
    boto3_raw_data: "type_defs.HybridJobQueueInfoTypeDef" = dataclasses.field()

    queue = field("queue")
    position = field("position")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HybridJobQueueInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridJobQueueInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobEventDetails:
    boto3_raw_data: "type_defs.JobEventDetailsTypeDef" = dataclasses.field()

    eventType = field("eventType")
    timeOfEvent = field("timeOfEvent")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobEventDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobEventDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQuantumTaskRequest:
    boto3_raw_data: "type_defs.GetQuantumTaskRequestTypeDef" = dataclasses.field()

    quantumTaskArn = field("quantumTaskArn")
    additionalAttributeNames = field("additionalAttributeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQuantumTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQuantumTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuantumTaskQueueInfo:
    boto3_raw_data: "type_defs.QuantumTaskQueueInfoTypeDef" = dataclasses.field()

    queue = field("queue")
    position = field("position")
    queuePriority = field("queuePriority")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuantumTaskQueueInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuantumTaskQueueInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    status = field("status")
    jobArn = field("jobArn")
    jobName = field("jobName")
    device = field("device")
    createdAt = field("createdAt")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

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
class QuantumTaskSummary:
    boto3_raw_data: "type_defs.QuantumTaskSummaryTypeDef" = dataclasses.field()

    quantumTaskArn = field("quantumTaskArn")
    status = field("status")
    deviceArn = field("deviceArn")
    shots = field("shots")
    outputS3Bucket = field("outputS3Bucket")
    outputS3Directory = field("outputS3Directory")
    createdAt = field("createdAt")
    endedAt = field("endedAt")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuantumTaskSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuantumTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchDevicesFilter:
    boto3_raw_data: "type_defs.SearchDevicesFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchDevicesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDevicesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsFilter:
    boto3_raw_data: "type_defs.SearchJobsFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchJobsFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuantumTasksFilter:
    boto3_raw_data: "type_defs.SearchQuantumTasksFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuantumTasksFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuantumTasksFilterTypeDef"]
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

    resourceArn = field("resourceArn")
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

    resourceArn = field("resourceArn")
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
class AlgorithmSpecification:
    boto3_raw_data: "type_defs.AlgorithmSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def scriptModeConfig(self):  # pragma: no cover
        return ScriptModeConfig.make_one(self.boto3_raw_data["scriptModeConfig"])

    @cached_property
    def containerImage(self):  # pragma: no cover
        return ContainerImage.make_one(self.boto3_raw_data["containerImage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlgorithmSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlgorithmSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuantumTaskRequest:
    boto3_raw_data: "type_defs.CreateQuantumTaskRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    deviceArn = field("deviceArn")
    shots = field("shots")
    outputS3Bucket = field("outputS3Bucket")
    outputS3KeyPrefix = field("outputS3KeyPrefix")
    action = field("action")
    deviceParameters = field("deviceParameters")
    tags = field("tags")
    jobToken = field("jobToken")

    @cached_property
    def associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["associations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQuantumTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuantumTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobResponse:
    boto3_raw_data: "type_defs.CancelJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    cancellationStatus = field("cancellationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelQuantumTaskResponse:
    boto3_raw_data: "type_defs.CancelQuantumTaskResponseTypeDef" = dataclasses.field()

    quantumTaskArn = field("quantumTaskArn")
    cancellationStatus = field("cancellationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelQuantumTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQuantumTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobResponse:
    boto3_raw_data: "type_defs.CreateJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuantumTaskResponse:
    boto3_raw_data: "type_defs.CreateQuantumTaskResponseTypeDef" = dataclasses.field()

    quantumTaskArn = field("quantumTaskArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQuantumTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuantumTaskResponseTypeDef"]
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
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    @cached_property
    def s3DataSource(self):  # pragma: no cover
        return S3DataSource.make_one(self.boto3_raw_data["s3DataSource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceResponse:
    boto3_raw_data: "type_defs.GetDeviceResponseTypeDef" = dataclasses.field()

    deviceArn = field("deviceArn")
    deviceName = field("deviceName")
    providerName = field("providerName")
    deviceType = field("deviceType")
    deviceStatus = field("deviceStatus")
    deviceCapabilities = field("deviceCapabilities")

    @cached_property
    def deviceQueueInfo(self):  # pragma: no cover
        return DeviceQueueInfo.make_many(self.boto3_raw_data["deviceQueueInfo"])

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
class SearchDevicesResponse:
    boto3_raw_data: "type_defs.SearchDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def devices(self):  # pragma: no cover
        return DeviceSummary.make_many(self.boto3_raw_data["devices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQuantumTaskResponse:
    boto3_raw_data: "type_defs.GetQuantumTaskResponseTypeDef" = dataclasses.field()

    quantumTaskArn = field("quantumTaskArn")
    status = field("status")
    failureReason = field("failureReason")
    deviceArn = field("deviceArn")
    deviceParameters = field("deviceParameters")
    shots = field("shots")
    outputS3Bucket = field("outputS3Bucket")
    outputS3Directory = field("outputS3Directory")
    createdAt = field("createdAt")
    endedAt = field("endedAt")
    tags = field("tags")
    jobArn = field("jobArn")

    @cached_property
    def queueInfo(self):  # pragma: no cover
        return QuantumTaskQueueInfo.make_one(self.boto3_raw_data["queueInfo"])

    @cached_property
    def associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["associations"])

    numSuccessfulShots = field("numSuccessfulShots")

    @cached_property
    def actionMetadata(self):  # pragma: no cover
        return ActionMetadata.make_one(self.boto3_raw_data["actionMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQuantumTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQuantumTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsResponse:
    boto3_raw_data: "type_defs.SearchJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuantumTasksResponse:
    boto3_raw_data: "type_defs.SearchQuantumTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def quantumTasks(self):  # pragma: no cover
        return QuantumTaskSummary.make_many(self.boto3_raw_data["quantumTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuantumTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuantumTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchDevicesRequestPaginate:
    boto3_raw_data: "type_defs.SearchDevicesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchDevicesFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchDevicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDevicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchDevicesRequest:
    boto3_raw_data: "type_defs.SearchDevicesRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchDevicesFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsRequestPaginate:
    boto3_raw_data: "type_defs.SearchJobsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchJobsFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchJobsRequest:
    boto3_raw_data: "type_defs.SearchJobsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchJobsFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuantumTasksRequestPaginate:
    boto3_raw_data: "type_defs.SearchQuantumTasksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchQuantumTasksFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchQuantumTasksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuantumTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuantumTasksRequest:
    boto3_raw_data: "type_defs.SearchQuantumTasksRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchQuantumTasksFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuantumTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuantumTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFileConfig:
    boto3_raw_data: "type_defs.InputFileConfigTypeDef" = dataclasses.field()

    channelName = field("channelName")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    contentType = field("contentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputFileConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputFileConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")

    @cached_property
    def algorithmSpecification(self):  # pragma: no cover
        return AlgorithmSpecification.make_one(
            self.boto3_raw_data["algorithmSpecification"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return JobOutputDataConfig.make_one(self.boto3_raw_data["outputDataConfig"])

    jobName = field("jobName")
    roleArn = field("roleArn")

    @cached_property
    def instanceConfig(self):  # pragma: no cover
        return InstanceConfig.make_one(self.boto3_raw_data["instanceConfig"])

    @cached_property
    def deviceConfig(self):  # pragma: no cover
        return DeviceConfig.make_one(self.boto3_raw_data["deviceConfig"])

    @cached_property
    def inputDataConfig(self):  # pragma: no cover
        return InputFileConfig.make_many(self.boto3_raw_data["inputDataConfig"])

    @cached_property
    def checkpointConfig(self):  # pragma: no cover
        return JobCheckpointConfig.make_one(self.boto3_raw_data["checkpointConfig"])

    @cached_property
    def stoppingCondition(self):  # pragma: no cover
        return JobStoppingCondition.make_one(self.boto3_raw_data["stoppingCondition"])

    hyperParameters = field("hyperParameters")
    tags = field("tags")

    @cached_property
    def associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["associations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobResponse:
    boto3_raw_data: "type_defs.GetJobResponseTypeDef" = dataclasses.field()

    status = field("status")
    jobArn = field("jobArn")
    roleArn = field("roleArn")
    failureReason = field("failureReason")
    jobName = field("jobName")
    hyperParameters = field("hyperParameters")

    @cached_property
    def inputDataConfig(self):  # pragma: no cover
        return InputFileConfig.make_many(self.boto3_raw_data["inputDataConfig"])

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return JobOutputDataConfig.make_one(self.boto3_raw_data["outputDataConfig"])

    @cached_property
    def stoppingCondition(self):  # pragma: no cover
        return JobStoppingCondition.make_one(self.boto3_raw_data["stoppingCondition"])

    @cached_property
    def checkpointConfig(self):  # pragma: no cover
        return JobCheckpointConfig.make_one(self.boto3_raw_data["checkpointConfig"])

    @cached_property
    def algorithmSpecification(self):  # pragma: no cover
        return AlgorithmSpecification.make_one(
            self.boto3_raw_data["algorithmSpecification"]
        )

    @cached_property
    def instanceConfig(self):  # pragma: no cover
        return InstanceConfig.make_one(self.boto3_raw_data["instanceConfig"])

    createdAt = field("createdAt")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    billableDuration = field("billableDuration")

    @cached_property
    def deviceConfig(self):  # pragma: no cover
        return DeviceConfig.make_one(self.boto3_raw_data["deviceConfig"])

    @cached_property
    def events(self):  # pragma: no cover
        return JobEventDetails.make_many(self.boto3_raw_data["events"])

    tags = field("tags")

    @cached_property
    def queueInfo(self):  # pragma: no cover
        return HybridJobQueueInfo.make_one(self.boto3_raw_data["queueInfo"])

    @cached_property
    def associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
