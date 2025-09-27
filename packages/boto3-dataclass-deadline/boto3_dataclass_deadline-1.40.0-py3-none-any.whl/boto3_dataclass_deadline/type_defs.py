# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_deadline import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceleratorCountRange:
    boto3_raw_data: "type_defs.AcceleratorCountRangeTypeDef" = dataclasses.field()

    min = field("min")
    max = field("max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceleratorCountRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorCountRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceleratorSelection:
    boto3_raw_data: "type_defs.AcceleratorSelectionTypeDef" = dataclasses.field()

    name = field("name")
    runtime = field("runtime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceleratorSelectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceleratorTotalMemoryMiBRange:
    boto3_raw_data: "type_defs.AcceleratorTotalMemoryMiBRangeTypeDef" = (
        dataclasses.field()
    )

    min = field("min")
    max = field("max")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceleratorTotalMemoryMiBRangeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorTotalMemoryMiBRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcquiredLimit:
    boto3_raw_data: "type_defs.AcquiredLimitTypeDef" = dataclasses.field()

    limitId = field("limitId")
    count = field("count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcquiredLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcquiredLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedEnvironmentEnterSessionActionDefinition:
    boto3_raw_data: (
        "type_defs.AssignedEnvironmentEnterSessionActionDefinitionTypeDef"
    ) = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssignedEnvironmentEnterSessionActionDefinitionTypeDef"
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
                "type_defs.AssignedEnvironmentEnterSessionActionDefinitionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedEnvironmentExitSessionActionDefinition:
    boto3_raw_data: (
        "type_defs.AssignedEnvironmentExitSessionActionDefinitionTypeDef"
    ) = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssignedEnvironmentExitSessionActionDefinitionTypeDef"
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
                "type_defs.AssignedEnvironmentExitSessionActionDefinitionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedSyncInputJobAttachmentsSessionActionDefinition:
    boto3_raw_data: (
        "type_defs.AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef"
    ) = dataclasses.field()

    stepId = field("stepId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef"
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
                "type_defs.AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfiguration:
    boto3_raw_data: "type_defs.LogConfigurationTypeDef" = dataclasses.field()

    logDriver = field("logDriver")
    options = field("options")
    parameters = field("parameters")
    error = field("error")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskParameterValue:
    boto3_raw_data: "type_defs.TaskParameterValueTypeDef" = dataclasses.field()

    int = field("int")
    float = field("float")
    string = field("string")
    path = field("path")
    chunkInt = field("chunkInt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskParameterValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskParameterValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberToFarmRequest:
    boto3_raw_data: "type_defs.AssociateMemberToFarmRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateMemberToFarmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberToFarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberToFleetRequest:
    boto3_raw_data: "type_defs.AssociateMemberToFleetRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateMemberToFleetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberToFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberToJobRequest:
    boto3_raw_data: "type_defs.AssociateMemberToJobRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateMemberToJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberToJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberToQueueRequest:
    boto3_raw_data: "type_defs.AssociateMemberToQueueRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateMemberToQueueRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberToQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeFleetRoleForReadRequest:
    boto3_raw_data: "type_defs.AssumeFleetRoleForReadRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeFleetRoleForReadRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeFleetRoleForReadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsCredentials:
    boto3_raw_data: "type_defs.AwsCredentialsTypeDef" = dataclasses.field()

    accessKeyId = field("accessKeyId")
    secretAccessKey = field("secretAccessKey")
    sessionToken = field("sessionToken")
    expiration = field("expiration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsCredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsCredentialsTypeDef"]],
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
class AssumeFleetRoleForWorkerRequest:
    boto3_raw_data: "type_defs.AssumeFleetRoleForWorkerRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeFleetRoleForWorkerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeFleetRoleForWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeQueueRoleForReadRequest:
    boto3_raw_data: "type_defs.AssumeQueueRoleForReadRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeQueueRoleForReadRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeQueueRoleForReadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeQueueRoleForUserRequest:
    boto3_raw_data: "type_defs.AssumeQueueRoleForUserRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeQueueRoleForUserRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeQueueRoleForUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeQueueRoleForWorkerRequest:
    boto3_raw_data: "type_defs.AssumeQueueRoleForWorkerRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")
    queueId = field("queueId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeQueueRoleForWorkerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeQueueRoleForWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestPropertiesOutput:
    boto3_raw_data: "type_defs.ManifestPropertiesOutputTypeDef" = dataclasses.field()

    rootPath = field("rootPath")
    rootPathFormat = field("rootPathFormat")
    fileSystemLocationName = field("fileSystemLocationName")
    outputRelativeDirectories = field("outputRelativeDirectories")
    inputManifestPath = field("inputManifestPath")
    inputManifestHash = field("inputManifestHash")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManifestPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManifestPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestProperties:
    boto3_raw_data: "type_defs.ManifestPropertiesTypeDef" = dataclasses.field()

    rootPath = field("rootPath")
    rootPathFormat = field("rootPathFormat")
    fileSystemLocationName = field("fileSystemLocationName")
    outputRelativeDirectories = field("outputRelativeDirectories")
    inputManifestPath = field("inputManifestPath")
    inputManifestHash = field("inputManifestHash")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManifestPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManifestPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetActionToAdd:
    boto3_raw_data: "type_defs.BudgetActionToAddTypeDef" = dataclasses.field()

    type = field("type")
    thresholdPercentage = field("thresholdPercentage")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetActionToAddTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BudgetActionToAddTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetActionToRemove:
    boto3_raw_data: "type_defs.BudgetActionToRemoveTypeDef" = dataclasses.field()

    type = field("type")
    thresholdPercentage = field("thresholdPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BudgetActionToRemoveTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BudgetActionToRemoveTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedBudgetScheduleOutput:
    boto3_raw_data: "type_defs.FixedBudgetScheduleOutputTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FixedBudgetScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedBudgetScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumedUsages:
    boto3_raw_data: "type_defs.ConsumedUsagesTypeDef" = dataclasses.field()

    approximateDollarUsage = field("approximateDollarUsage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConsumedUsagesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConsumedUsagesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageTrackingResource:
    boto3_raw_data: "type_defs.UsageTrackingResourceTypeDef" = dataclasses.field()

    queueId = field("queueId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageTrackingResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageTrackingResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFarmRequest:
    boto3_raw_data: "type_defs.CreateFarmRequestTypeDef" = dataclasses.field()

    displayName = field("displayName")
    clientToken = field("clientToken")
    description = field("description")
    kmsKeyArn = field("kmsKeyArn")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFarmRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostConfiguration:
    boto3_raw_data: "type_defs.HostConfigurationTypeDef" = dataclasses.field()

    scriptBody = field("scriptBody")
    scriptTimeoutSeconds = field("scriptTimeoutSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobParameter:
    boto3_raw_data: "type_defs.JobParameterTypeDef" = dataclasses.field()

    int = field("int")
    float = field("float")
    string = field("string")
    path = field("path")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLicenseEndpointRequest:
    boto3_raw_data: "type_defs.CreateLicenseEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLicenseEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLimitRequest:
    boto3_raw_data: "type_defs.CreateLimitRequestTypeDef" = dataclasses.field()

    displayName = field("displayName")
    amountRequirementName = field("amountRequirementName")
    maxCount = field("maxCount")
    farmId = field("farmId")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorRequest:
    boto3_raw_data: "type_defs.CreateMonitorRequestTypeDef" = dataclasses.field()

    displayName = field("displayName")
    identityCenterInstanceArn = field("identityCenterInstanceArn")
    subdomain = field("subdomain")
    roleArn = field("roleArn")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateQueueEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    priority = field("priority")
    templateType = field("templateType")
    template = field("template")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateQueueEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueFleetAssociationRequest:
    boto3_raw_data: "type_defs.CreateQueueFleetAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateQueueFleetAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueFleetAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueLimitAssociationRequest:
    boto3_raw_data: "type_defs.CreateQueueLimitAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateQueueLimitAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueLimitAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobAttachmentSettings:
    boto3_raw_data: "type_defs.JobAttachmentSettingsTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    rootPrefix = field("rootPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobAttachmentSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobAttachmentSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemLocation:
    boto3_raw_data: "type_defs.FileSystemLocationTypeDef" = dataclasses.field()

    name = field("name")
    path = field("path")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetAmountCapability:
    boto3_raw_data: "type_defs.FleetAmountCapabilityTypeDef" = dataclasses.field()

    name = field("name")
    min = field("min")
    max = field("max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FleetAmountCapabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetAmountCapabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetAttributeCapabilityOutput:
    boto3_raw_data: "type_defs.FleetAttributeCapabilityOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FleetAttributeCapabilityOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetAttributeCapabilityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryMiBRange:
    boto3_raw_data: "type_defs.MemoryMiBRangeTypeDef" = dataclasses.field()

    min = field("min")
    max = field("max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemoryMiBRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemoryMiBRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VCpuCountRange:
    boto3_raw_data: "type_defs.VCpuCountRangeTypeDef" = dataclasses.field()

    min = field("min")
    max = field("max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VCpuCountRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VCpuCountRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetAttributeCapability:
    boto3_raw_data: "type_defs.FleetAttributeCapabilityTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FleetAttributeCapabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetAttributeCapabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBudgetRequest:
    boto3_raw_data: "type_defs.DeleteBudgetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    budgetId = field("budgetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFarmRequest:
    boto3_raw_data: "type_defs.DeleteFarmRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFarmRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetRequest:
    boto3_raw_data: "type_defs.DeleteFleetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLicenseEndpointRequest:
    boto3_raw_data: "type_defs.DeleteLicenseEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    licenseEndpointId = field("licenseEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLicenseEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLicenseEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLimitRequest:
    boto3_raw_data: "type_defs.DeleteLimitRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    limitId = field("limitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMeteredProductRequest:
    boto3_raw_data: "type_defs.DeleteMeteredProductRequestTypeDef" = dataclasses.field()

    licenseEndpointId = field("licenseEndpointId")
    productId = field("productId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMeteredProductRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMeteredProductRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMonitorRequest:
    boto3_raw_data: "type_defs.DeleteMonitorRequestTypeDef" = dataclasses.field()

    monitorId = field("monitorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueueEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteQueueEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    queueEnvironmentId = field("queueEnvironmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteQueueEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueueEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueueFleetAssociationRequest:
    boto3_raw_data: "type_defs.DeleteQueueFleetAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteQueueFleetAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueueFleetAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueueLimitAssociationRequest:
    boto3_raw_data: "type_defs.DeleteQueueLimitAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteQueueLimitAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueueLimitAssociationRequestTypeDef"]
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

    farmId = field("farmId")
    queueId = field("queueId")

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
class DeleteStorageProfileRequest:
    boto3_raw_data: "type_defs.DeleteStorageProfileRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    storageProfileId = field("storageProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStorageProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkerRequest:
    boto3_raw_data: "type_defs.DeleteWorkerRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DependencyCounts:
    boto3_raw_data: "type_defs.DependencyCountsTypeDef" = dataclasses.field()

    dependenciesResolved = field("dependenciesResolved")
    dependenciesUnresolved = field("dependenciesUnresolved")
    consumersResolved = field("consumersResolved")
    consumersUnresolved = field("consumersUnresolved")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DependencyCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DependencyCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberFromFarmRequest:
    boto3_raw_data: "type_defs.DisassociateMemberFromFarmRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    principalId = field("principalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMemberFromFarmRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberFromFarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberFromFleetRequest:
    boto3_raw_data: "type_defs.DisassociateMemberFromFleetRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")
    principalId = field("principalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMemberFromFleetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberFromFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberFromJobRequest:
    boto3_raw_data: "type_defs.DisassociateMemberFromJobRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    principalId = field("principalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateMemberFromJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberFromJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberFromQueueRequest:
    boto3_raw_data: "type_defs.DisassociateMemberFromQueueRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    principalId = field("principalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMemberFromQueueRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberFromQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2EbsVolume:
    boto3_raw_data: "type_defs.Ec2EbsVolumeTypeDef" = dataclasses.field()

    sizeGiB = field("sizeGiB")
    iops = field("iops")
    throughputMiB = field("throughputMiB")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2EbsVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ec2EbsVolumeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDetailsEntity:
    boto3_raw_data: "type_defs.EnvironmentDetailsEntityTypeDef" = dataclasses.field()

    jobId = field("jobId")
    environmentId = field("environmentId")
    schemaVersion = field("schemaVersion")
    template = field("template")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentDetailsEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDetailsEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDetailsError:
    boto3_raw_data: "type_defs.EnvironmentDetailsErrorTypeDef" = dataclasses.field()

    jobId = field("jobId")
    environmentId = field("environmentId")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentDetailsErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDetailsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDetailsIdentifiers:
    boto3_raw_data: "type_defs.EnvironmentDetailsIdentifiersTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentDetailsIdentifiersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDetailsIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentEnterSessionActionDefinitionSummary:
    boto3_raw_data: (
        "type_defs.EnvironmentEnterSessionActionDefinitionSummaryTypeDef"
    ) = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentEnterSessionActionDefinitionSummaryTypeDef"
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
                "type_defs.EnvironmentEnterSessionActionDefinitionSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentEnterSessionActionDefinition:
    boto3_raw_data: "type_defs.EnvironmentEnterSessionActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentEnterSessionActionDefinitionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentEnterSessionActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentExitSessionActionDefinitionSummary:
    boto3_raw_data: "type_defs.EnvironmentExitSessionActionDefinitionSummaryTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentExitSessionActionDefinitionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentExitSessionActionDefinitionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentExitSessionActionDefinition:
    boto3_raw_data: "type_defs.EnvironmentExitSessionActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentExitSessionActionDefinitionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentExitSessionActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FarmMember:
    boto3_raw_data: "type_defs.FarmMemberTypeDef" = dataclasses.field()

    farmId = field("farmId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FarmMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FarmMemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FarmSummary:
    boto3_raw_data: "type_defs.FarmSummaryTypeDef" = dataclasses.field()

    farmId = field("farmId")
    displayName = field("displayName")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    kmsKeyArn = field("kmsKeyArn")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FarmSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FarmSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldSortExpression:
    boto3_raw_data: "type_defs.FieldSortExpressionTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldSortExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldSortExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetMember:
    boto3_raw_data: "type_defs.FleetMemberTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetMemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBudgetRequest:
    boto3_raw_data: "type_defs.GetBudgetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    budgetId = field("budgetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBudgetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseBudgetAction:
    boto3_raw_data: "type_defs.ResponseBudgetActionTypeDef" = dataclasses.field()

    type = field("type")
    thresholdPercentage = field("thresholdPercentage")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseBudgetActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseBudgetActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFarmRequest:
    boto3_raw_data: "type_defs.GetFarmRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFarmRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFarmRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFleetRequest:
    boto3_raw_data: "type_defs.GetFleetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFleetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFleetRequestTypeDef"]],
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
class JobAttachmentDetailsError:
    boto3_raw_data: "type_defs.JobAttachmentDetailsErrorTypeDef" = dataclasses.field()

    jobId = field("jobId")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobAttachmentDetailsErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobAttachmentDetailsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDetailsError:
    boto3_raw_data: "type_defs.JobDetailsErrorTypeDef" = dataclasses.field()

    jobId = field("jobId")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDetailsErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDetailsErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepDetailsError:
    boto3_raw_data: "type_defs.StepDetailsErrorTypeDef" = dataclasses.field()

    jobId = field("jobId")
    stepId = field("stepId")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepDetailsErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepDetailsErrorTypeDef"]
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

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")

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
class GetLicenseEndpointRequest:
    boto3_raw_data: "type_defs.GetLicenseEndpointRequestTypeDef" = dataclasses.field()

    licenseEndpointId = field("licenseEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLicenseEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLimitRequest:
    boto3_raw_data: "type_defs.GetLimitRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    limitId = field("limitId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLimitRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetLimitRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitorRequest:
    boto3_raw_data: "type_defs.GetMonitorRequestTypeDef" = dataclasses.field()

    monitorId = field("monitorId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMonitorRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueEnvironmentRequest:
    boto3_raw_data: "type_defs.GetQueueEnvironmentRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    queueEnvironmentId = field("queueEnvironmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueFleetAssociationRequest:
    boto3_raw_data: "type_defs.GetQueueFleetAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueueFleetAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueFleetAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueLimitAssociationRequest:
    boto3_raw_data: "type_defs.GetQueueLimitAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueueLimitAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueLimitAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueRequest:
    boto3_raw_data: "type_defs.GetQueueRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQueueRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionActionRequest:
    boto3_raw_data: "type_defs.GetSessionActionRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    sessionActionId = field("sessionActionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskRunManifestPropertiesResponse:
    boto3_raw_data: "type_defs.TaskRunManifestPropertiesResponseTypeDef" = (
        dataclasses.field()
    )

    outputManifestPath = field("outputManifestPath")
    outputManifestHash = field("outputManifestHash")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TaskRunManifestPropertiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskRunManifestPropertiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
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
class GetSessionsStatisticsAggregationRequest:
    boto3_raw_data: "type_defs.GetSessionsStatisticsAggregationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    aggregationId = field("aggregationId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSessionsStatisticsAggregationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionsStatisticsAggregationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStepRequest:
    boto3_raw_data: "type_defs.GetStepRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStepRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStepRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageProfileForQueueRequest:
    boto3_raw_data: "type_defs.GetStorageProfileForQueueRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    storageProfileId = field("storageProfileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetStorageProfileForQueueRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageProfileForQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageProfileRequest:
    boto3_raw_data: "type_defs.GetStorageProfileRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    storageProfileId = field("storageProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStorageProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaskRequest:
    boto3_raw_data: "type_defs.GetTaskRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")
    taskId = field("taskId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTaskRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkerRequest:
    boto3_raw_data: "type_defs.GetWorkerRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWorkerRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAddressesOutput:
    boto3_raw_data: "type_defs.IpAddressesOutputTypeDef" = dataclasses.field()

    ipV4Addresses = field("ipV4Addresses")
    ipV6Addresses = field("ipV6Addresses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAddressesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpAddressesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAddresses:
    boto3_raw_data: "type_defs.IpAddressesTypeDef" = dataclasses.field()

    ipV4Addresses = field("ipV4Addresses")
    ipV6Addresses = field("ipV6Addresses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAddressesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpAddressesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobAttachmentDetailsIdentifiers:
    boto3_raw_data: "type_defs.JobAttachmentDetailsIdentifiersTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JobAttachmentDetailsIdentifiersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobAttachmentDetailsIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathMappingRule:
    boto3_raw_data: "type_defs.PathMappingRuleTypeDef" = dataclasses.field()

    sourcePathFormat = field("sourcePathFormat")
    sourcePath = field("sourcePath")
    destinationPath = field("destinationPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathMappingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathMappingRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDetailsIdentifiers:
    boto3_raw_data: "type_defs.JobDetailsIdentifiersTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobDetailsIdentifiersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobDetailsIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepDetailsIdentifiers:
    boto3_raw_data: "type_defs.StepDetailsIdentifiersTypeDef" = dataclasses.field()

    jobId = field("jobId")
    stepId = field("stepId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepDetailsIdentifiersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepDetailsIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepDetailsEntity:
    boto3_raw_data: "type_defs.StepDetailsEntityTypeDef" = dataclasses.field()

    jobId = field("jobId")
    stepId = field("stepId")
    schemaVersion = field("schemaVersion")
    template = field("template")
    dependencies = field("dependencies")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepDetailsEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepDetailsEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobMember:
    boto3_raw_data: "type_defs.JobMemberTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobMemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PosixUser:
    boto3_raw_data: "type_defs.PosixUserTypeDef" = dataclasses.field()

    user = field("user")
    group = field("group")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PosixUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PosixUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WindowsUser:
    boto3_raw_data: "type_defs.WindowsUserTypeDef" = dataclasses.field()

    user = field("user")
    passwordArn = field("passwordArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WindowsUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WindowsUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    name = field("name")
    lifecycleStatus = field("lifecycleStatus")
    lifecycleStatusMessage = field("lifecycleStatusMessage")
    priority = field("priority")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    taskRunStatus = field("taskRunStatus")
    targetTaskRunStatus = field("targetTaskRunStatus")
    taskRunStatusCounts = field("taskRunStatusCounts")
    taskFailureRetryCount = field("taskFailureRetryCount")
    maxFailedTasksCount = field("maxFailedTasksCount")
    maxRetriesPerTask = field("maxRetriesPerTask")
    maxWorkerCount = field("maxWorkerCount")
    sourceJobId = field("sourceJobId")

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
class LicenseEndpointSummary:
    boto3_raw_data: "type_defs.LicenseEndpointSummaryTypeDef" = dataclasses.field()

    licenseEndpointId = field("licenseEndpointId")
    status = field("status")
    statusMessage = field("statusMessage")
    vpcId = field("vpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LicenseEndpointSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LicenseEndpointSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LimitSummary:
    boto3_raw_data: "type_defs.LimitSummaryTypeDef" = dataclasses.field()

    displayName = field("displayName")
    amountRequirementName = field("amountRequirementName")
    maxCount = field("maxCount")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    farmId = field("farmId")
    limitId = field("limitId")
    currentCount = field("currentCount")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LimitSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableMeteredProductsRequest:
    boto3_raw_data: "type_defs.ListAvailableMeteredProductsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableMeteredProductsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableMeteredProductsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeteredProductSummary:
    boto3_raw_data: "type_defs.MeteredProductSummaryTypeDef" = dataclasses.field()

    productId = field("productId")
    family = field("family")
    vendor = field("vendor")
    port = field("port")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MeteredProductSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MeteredProductSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBudgetsRequest:
    boto3_raw_data: "type_defs.ListBudgetsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBudgetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBudgetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFarmMembersRequest:
    boto3_raw_data: "type_defs.ListFarmMembersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFarmMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFarmMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFarmsRequest:
    boto3_raw_data: "type_defs.ListFarmsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    principalId = field("principalId")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFarmsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFarmsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetMembersRequest:
    boto3_raw_data: "type_defs.ListFleetMembersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsRequest:
    boto3_raw_data: "type_defs.ListFleetsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    principalId = field("principalId")
    displayName = field("displayName")
    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobMembersRequest:
    boto3_raw_data: "type_defs.ListJobMembersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobParameterDefinitionsRequest:
    boto3_raw_data: "type_defs.ListJobParameterDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    jobId = field("jobId")
    queueId = field("queueId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobParameterDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobParameterDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    principalId = field("principalId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseEndpointsRequest:
    boto3_raw_data: "type_defs.ListLicenseEndpointsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLicenseEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLimitsRequest:
    boto3_raw_data: "type_defs.ListLimitsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLimitsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMeteredProductsRequest:
    boto3_raw_data: "type_defs.ListMeteredProductsRequestTypeDef" = dataclasses.field()

    licenseEndpointId = field("licenseEndpointId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMeteredProductsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMeteredProductsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsRequest:
    boto3_raw_data: "type_defs.ListMonitorsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorSummary:
    boto3_raw_data: "type_defs.MonitorSummaryTypeDef" = dataclasses.field()

    monitorId = field("monitorId")
    displayName = field("displayName")
    subdomain = field("subdomain")
    url = field("url")
    roleArn = field("roleArn")
    identityCenterInstanceArn = field("identityCenterInstanceArn")
    identityCenterApplicationArn = field("identityCenterApplicationArn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListQueueEnvironmentsRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueueEnvironmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueEnvironmentSummary:
    boto3_raw_data: "type_defs.QueueEnvironmentSummaryTypeDef" = dataclasses.field()

    queueEnvironmentId = field("queueEnvironmentId")
    name = field("name")
    priority = field("priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueEnvironmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueEnvironmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueFleetAssociationsRequest:
    boto3_raw_data: "type_defs.ListQueueFleetAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueFleetAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueFleetAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueFleetAssociationSummary:
    boto3_raw_data: "type_defs.QueueFleetAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    queueId = field("queueId")
    fleetId = field("fleetId")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueFleetAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueFleetAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueLimitAssociationsRequest:
    boto3_raw_data: "type_defs.ListQueueLimitAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueLimitAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueLimitAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueLimitAssociationSummary:
    boto3_raw_data: "type_defs.QueueLimitAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    queueId = field("queueId")
    limitId = field("limitId")
    status = field("status")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueLimitAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueLimitAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueMembersRequest:
    boto3_raw_data: "type_defs.ListQueueMembersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueueMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueMember:
    boto3_raw_data: "type_defs.QueueMemberTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    principalId = field("principalId")
    principalType = field("principalType")
    identityStoreId = field("identityStoreId")
    membershipLevel = field("membershipLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueMemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesRequest:
    boto3_raw_data: "type_defs.ListQueuesRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    principalId = field("principalId")
    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

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
class QueueSummary:
    boto3_raw_data: "type_defs.QueueSummaryTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    displayName = field("displayName")
    status = field("status")
    defaultBudgetAction = field("defaultBudgetAction")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    blockedReason = field("blockedReason")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionActionsRequest:
    boto3_raw_data: "type_defs.ListSessionActionsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    sessionId = field("sessionId")
    taskId = field("taskId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsForWorkerRequest:
    boto3_raw_data: "type_defs.ListSessionsForWorkerRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsForWorkerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsForWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerSessionSummary:
    boto3_raw_data: "type_defs.WorkerSessionSummaryTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    queueId = field("queueId")
    jobId = field("jobId")
    startedAt = field("startedAt")
    lifecycleStatus = field("lifecycleStatus")
    endedAt = field("endedAt")
    targetLifecycleStatus = field("targetLifecycleStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerSessionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerSessionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequest:
    boto3_raw_data: "type_defs.ListSessionsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSummary:
    boto3_raw_data: "type_defs.SessionSummaryTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    fleetId = field("fleetId")
    workerId = field("workerId")
    startedAt = field("startedAt")
    lifecycleStatus = field("lifecycleStatus")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    targetLifecycleStatus = field("targetLifecycleStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepConsumersRequest:
    boto3_raw_data: "type_defs.ListStepConsumersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStepConsumersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepConsumersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepConsumer:
    boto3_raw_data: "type_defs.StepConsumerTypeDef" = dataclasses.field()

    stepId = field("stepId")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepConsumerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepConsumerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepDependenciesRequest:
    boto3_raw_data: "type_defs.ListStepDependenciesRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStepDependenciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepDependenciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepDependency:
    boto3_raw_data: "type_defs.StepDependencyTypeDef" = dataclasses.field()

    stepId = field("stepId")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepDependencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepDependencyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepsRequest:
    boto3_raw_data: "type_defs.ListStepsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStepsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageProfilesForQueueRequest:
    boto3_raw_data: "type_defs.ListStorageProfilesForQueueRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageProfilesForQueueRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageProfilesForQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageProfileSummary:
    boto3_raw_data: "type_defs.StorageProfileSummaryTypeDef" = dataclasses.field()

    storageProfileId = field("storageProfileId")
    displayName = field("displayName")
    osFamily = field("osFamily")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageProfilesRequest:
    boto3_raw_data: "type_defs.ListStorageProfilesRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStorageProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageProfilesRequestTypeDef"]
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
class ListTasksRequest:
    boto3_raw_data: "type_defs.ListTasksRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkersRequest:
    boto3_raw_data: "type_defs.ListWorkersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterFilterExpression:
    boto3_raw_data: "type_defs.ParameterFilterExpressionTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterFilterExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterFilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterSortExpression:
    boto3_raw_data: "type_defs.ParameterSortExpressionTypeDef" = dataclasses.field()

    sortOrder = field("sortOrder")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterSortExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterSortExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepParameter:
    boto3_raw_data: "type_defs.StepParameterTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMeteredProductRequest:
    boto3_raw_data: "type_defs.PutMeteredProductRequestTypeDef" = dataclasses.field()

    licenseEndpointId = field("licenseEndpointId")
    productId = field("productId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMeteredProductRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMeteredProductRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTermFilterExpression:
    boto3_raw_data: "type_defs.SearchTermFilterExpressionTypeDef" = dataclasses.field()

    searchTerm = field("searchTerm")
    matchType = field("matchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTermFilterExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTermFilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringFilterExpression:
    boto3_raw_data: "type_defs.StringFilterExpressionTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StringFilterExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StringFilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserJobsFirst:
    boto3_raw_data: "type_defs.UserJobsFirstTypeDef" = dataclasses.field()

    userIdentityId = field("userIdentityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserJobsFirstTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserJobsFirstTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEc2InstanceMarketOptions:
    boto3_raw_data: "type_defs.ServiceManagedEc2InstanceMarketOptionsTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEc2InstanceMarketOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEc2InstanceMarketOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigurationOutput:
    boto3_raw_data: "type_defs.VpcConfigurationOutputTypeDef" = dataclasses.field()

    resourceConfigurationArns = field("resourceConfigurationArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    resourceConfigurationArns = field("resourceConfigurationArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncInputJobAttachmentsSessionActionDefinitionSummary:
    boto3_raw_data: (
        "type_defs.SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef"
    ) = dataclasses.field()

    stepId = field("stepId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef"
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
                "type_defs.SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncInputJobAttachmentsSessionActionDefinition:
    boto3_raw_data: (
        "type_defs.SyncInputJobAttachmentsSessionActionDefinitionTypeDef"
    ) = dataclasses.field()

    stepId = field("stepId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SyncInputJobAttachmentsSessionActionDefinitionTypeDef"
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
                "type_defs.SyncInputJobAttachmentsSessionActionDefinitionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionsStatisticsResources:
    boto3_raw_data: "type_defs.SessionsStatisticsResourcesTypeDef" = dataclasses.field()

    queueIds = field("queueIds")
    fleetIds = field("fleetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionsStatisticsResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionsStatisticsResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stats:
    boto3_raw_data: "type_defs.StatsTypeDef" = dataclasses.field()

    min = field("min")
    max = field("max")
    avg = field("avg")
    sum = field("sum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepAmountCapability:
    boto3_raw_data: "type_defs.StepAmountCapabilityTypeDef" = dataclasses.field()

    name = field("name")
    min = field("min")
    max = field("max")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepAmountCapabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepAmountCapabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepAttributeCapability:
    boto3_raw_data: "type_defs.StepAttributeCapabilityTypeDef" = dataclasses.field()

    name = field("name")
    anyOf = field("anyOf")
    allOf = field("allOf")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepAttributeCapabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepAttributeCapabilityTypeDef"]
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
class TaskRunManifestPropertiesRequest:
    boto3_raw_data: "type_defs.TaskRunManifestPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    outputManifestPath = field("outputManifestPath")
    outputManifestHash = field("outputManifestHash")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskRunManifestPropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskRunManifestPropertiesRequestTypeDef"]
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
class UpdateFarmRequest:
    boto3_raw_data: "type_defs.UpdateFarmRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    displayName = field("displayName")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFarmRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFarmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobRequest:
    boto3_raw_data: "type_defs.UpdateJobRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    clientToken = field("clientToken")
    targetTaskRunStatus = field("targetTaskRunStatus")
    priority = field("priority")
    maxFailedTasksCount = field("maxFailedTasksCount")
    maxRetriesPerTask = field("maxRetriesPerTask")
    lifecycleStatus = field("lifecycleStatus")
    maxWorkerCount = field("maxWorkerCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLimitRequest:
    boto3_raw_data: "type_defs.UpdateLimitRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    limitId = field("limitId")
    displayName = field("displayName")
    description = field("description")
    maxCount = field("maxCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitorRequest:
    boto3_raw_data: "type_defs.UpdateMonitorRequestTypeDef" = dataclasses.field()

    monitorId = field("monitorId")
    subdomain = field("subdomain")
    displayName = field("displayName")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateQueueEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    queueEnvironmentId = field("queueEnvironmentId")
    clientToken = field("clientToken")
    priority = field("priority")
    templateType = field("templateType")
    template = field("template")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQueueEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueFleetAssociationRequest:
    boto3_raw_data: "type_defs.UpdateQueueFleetAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQueueFleetAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueFleetAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueLimitAssociationRequest:
    boto3_raw_data: "type_defs.UpdateQueueLimitAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQueueLimitAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueLimitAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionRequest:
    boto3_raw_data: "type_defs.UpdateSessionRequestTypeDef" = dataclasses.field()

    targetLifecycleStatus = field("targetLifecycleStatus")
    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    sessionId = field("sessionId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStepRequest:
    boto3_raw_data: "type_defs.UpdateStepRequestTypeDef" = dataclasses.field()

    targetTaskRunStatus = field("targetTaskRunStatus")
    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateStepRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskRequest:
    boto3_raw_data: "type_defs.UpdateTaskRequestTypeDef" = dataclasses.field()

    targetRunStatus = field("targetRunStatus")
    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")
    taskId = field("taskId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerAmountCapability:
    boto3_raw_data: "type_defs.WorkerAmountCapabilityTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerAmountCapabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerAmountCapabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerAttributeCapability:
    boto3_raw_data: "type_defs.WorkerAttributeCapabilityTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerAttributeCapabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerAttributeCapabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceleratorCapabilitiesOutput:
    boto3_raw_data: "type_defs.AcceleratorCapabilitiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def selections(self):  # pragma: no cover
        return AcceleratorSelection.make_many(self.boto3_raw_data["selections"])

    @cached_property
    def count(self):  # pragma: no cover
        return AcceleratorCountRange.make_one(self.boto3_raw_data["count"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceleratorCapabilitiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorCapabilitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceleratorCapabilities:
    boto3_raw_data: "type_defs.AcceleratorCapabilitiesTypeDef" = dataclasses.field()

    @cached_property
    def selections(self):  # pragma: no cover
        return AcceleratorSelection.make_many(self.boto3_raw_data["selections"])

    @cached_property
    def count(self):  # pragma: no cover
        return AcceleratorCountRange.make_one(self.boto3_raw_data["count"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceleratorCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedTaskRunSessionActionDefinition:
    boto3_raw_data: "type_defs.AssignedTaskRunSessionActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    stepId = field("stepId")
    parameters = field("parameters")
    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssignedTaskRunSessionActionDefinitionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignedTaskRunSessionActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskRunSessionActionDefinitionSummary:
    boto3_raw_data: "type_defs.TaskRunSessionActionDefinitionSummaryTypeDef" = (
        dataclasses.field()
    )

    stepId = field("stepId")
    taskId = field("taskId")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TaskRunSessionActionDefinitionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskRunSessionActionDefinitionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskRunSessionActionDefinition:
    boto3_raw_data: "type_defs.TaskRunSessionActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    stepId = field("stepId")
    parameters = field("parameters")
    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskRunSessionActionDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskRunSessionActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSearchSummary:
    boto3_raw_data: "type_defs.TaskSearchSummaryTypeDef" = dataclasses.field()

    taskId = field("taskId")
    stepId = field("stepId")
    jobId = field("jobId")
    queueId = field("queueId")
    runStatus = field("runStatus")
    targetRunStatus = field("targetRunStatus")
    parameters = field("parameters")
    failureRetryCount = field("failureRetryCount")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskSearchSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSummary:
    boto3_raw_data: "type_defs.TaskSummaryTypeDef" = dataclasses.field()

    taskId = field("taskId")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    runStatus = field("runStatus")
    targetRunStatus = field("targetRunStatus")
    failureRetryCount = field("failureRetryCount")
    parameters = field("parameters")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    latestSessionActionId = field("latestSessionActionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeFleetRoleForReadResponse:
    boto3_raw_data: "type_defs.AssumeFleetRoleForReadResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeFleetRoleForReadResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeFleetRoleForReadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeFleetRoleForWorkerResponse:
    boto3_raw_data: "type_defs.AssumeFleetRoleForWorkerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeFleetRoleForWorkerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeFleetRoleForWorkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeQueueRoleForReadResponse:
    boto3_raw_data: "type_defs.AssumeQueueRoleForReadResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeQueueRoleForReadResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeQueueRoleForReadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeQueueRoleForUserResponse:
    boto3_raw_data: "type_defs.AssumeQueueRoleForUserResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeQueueRoleForUserResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeQueueRoleForUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeQueueRoleForWorkerResponse:
    boto3_raw_data: "type_defs.AssumeQueueRoleForWorkerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentials(self):  # pragma: no cover
        return AwsCredentials.make_one(self.boto3_raw_data["credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeQueueRoleForWorkerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeQueueRoleForWorkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyJobTemplateResponse:
    boto3_raw_data: "type_defs.CopyJobTemplateResponseTypeDef" = dataclasses.field()

    templateType = field("templateType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBudgetResponse:
    boto3_raw_data: "type_defs.CreateBudgetResponseTypeDef" = dataclasses.field()

    budgetId = field("budgetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBudgetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBudgetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFarmResponse:
    boto3_raw_data: "type_defs.CreateFarmResponseTypeDef" = dataclasses.field()

    farmId = field("farmId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFarmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFarmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetResponse:
    boto3_raw_data: "type_defs.CreateFleetResponseTypeDef" = dataclasses.field()

    fleetId = field("fleetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetResponseTypeDef"]
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

    jobId = field("jobId")

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
class CreateLicenseEndpointResponse:
    boto3_raw_data: "type_defs.CreateLicenseEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    licenseEndpointId = field("licenseEndpointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLicenseEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLicenseEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLimitResponse:
    boto3_raw_data: "type_defs.CreateLimitResponseTypeDef" = dataclasses.field()

    limitId = field("limitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorResponse:
    boto3_raw_data: "type_defs.CreateMonitorResponseTypeDef" = dataclasses.field()

    monitorId = field("monitorId")
    identityCenterApplicationArn = field("identityCenterApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateQueueEnvironmentResponseTypeDef" = (
        dataclasses.field()
    )

    queueEnvironmentId = field("queueEnvironmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateQueueEnvironmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueueResponse:
    boto3_raw_data: "type_defs.CreateQueueResponseTypeDef" = dataclasses.field()

    queueId = field("queueId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageProfileResponse:
    boto3_raw_data: "type_defs.CreateStorageProfileResponseTypeDef" = (
        dataclasses.field()
    )

    storageProfileId = field("storageProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStorageProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkerResponse:
    boto3_raw_data: "type_defs.CreateWorkerResponseTypeDef" = dataclasses.field()

    workerId = field("workerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFarmResponse:
    boto3_raw_data: "type_defs.GetFarmResponseTypeDef" = dataclasses.field()

    farmId = field("farmId")
    displayName = field("displayName")
    description = field("description")
    kmsKeyArn = field("kmsKeyArn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFarmResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFarmResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseEndpointResponse:
    boto3_raw_data: "type_defs.GetLicenseEndpointResponseTypeDef" = dataclasses.field()

    licenseEndpointId = field("licenseEndpointId")
    status = field("status")
    statusMessage = field("statusMessage")
    vpcId = field("vpcId")
    dnsName = field("dnsName")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLicenseEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLimitResponse:
    boto3_raw_data: "type_defs.GetLimitResponseTypeDef" = dataclasses.field()

    displayName = field("displayName")
    amountRequirementName = field("amountRequirementName")
    maxCount = field("maxCount")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    farmId = field("farmId")
    limitId = field("limitId")
    currentCount = field("currentCount")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLimitResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitorResponse:
    boto3_raw_data: "type_defs.GetMonitorResponseTypeDef" = dataclasses.field()

    monitorId = field("monitorId")
    displayName = field("displayName")
    subdomain = field("subdomain")
    url = field("url")
    roleArn = field("roleArn")
    identityCenterInstanceArn = field("identityCenterInstanceArn")
    identityCenterApplicationArn = field("identityCenterApplicationArn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMonitorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMonitorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueEnvironmentResponse:
    boto3_raw_data: "type_defs.GetQueueEnvironmentResponseTypeDef" = dataclasses.field()

    queueEnvironmentId = field("queueEnvironmentId")
    name = field("name")
    priority = field("priority")
    templateType = field("templateType")
    template = field("template")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueFleetAssociationResponse:
    boto3_raw_data: "type_defs.GetQueueFleetAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    queueId = field("queueId")
    fleetId = field("fleetId")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueueFleetAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueFleetAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueLimitAssociationResponse:
    boto3_raw_data: "type_defs.GetQueueLimitAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    queueId = field("queueId")
    limitId = field("limitId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueueLimitAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueLimitAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaskResponse:
    boto3_raw_data: "type_defs.GetTaskResponseTypeDef" = dataclasses.field()

    taskId = field("taskId")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    runStatus = field("runStatus")
    targetRunStatus = field("targetRunStatus")
    failureRetryCount = field("failureRetryCount")
    parameters = field("parameters")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    latestSessionActionId = field("latestSessionActionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTaskResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTaskResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobParameterDefinitionsResponse:
    boto3_raw_data: "type_defs.ListJobParameterDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    jobParameterDefinitions = field("jobParameterDefinitions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobParameterDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobParameterDefinitionsResponseTypeDef"]
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
class StartSessionsStatisticsAggregationResponse:
    boto3_raw_data: "type_defs.StartSessionsStatisticsAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    aggregationId = field("aggregationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSessionsStatisticsAggregationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionsStatisticsAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentsOutput:
    boto3_raw_data: "type_defs.AttachmentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def manifests(self):  # pragma: no cover
        return ManifestPropertiesOutput.make_many(self.boto3_raw_data["manifests"])

    fileSystem = field("fileSystem")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attachments:
    boto3_raw_data: "type_defs.AttachmentsTypeDef" = dataclasses.field()

    @cached_property
    def manifests(self):  # pragma: no cover
        return ManifestProperties.make_many(self.boto3_raw_data["manifests"])

    fileSystem = field("fileSystem")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetScheduleOutput:
    boto3_raw_data: "type_defs.BudgetScheduleOutputTypeDef" = dataclasses.field()

    @cached_property
    def fixed(self):  # pragma: no cover
        return FixedBudgetScheduleOutput.make_one(self.boto3_raw_data["fixed"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BudgetScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BudgetScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetSummary:
    boto3_raw_data: "type_defs.BudgetSummaryTypeDef" = dataclasses.field()

    budgetId = field("budgetId")

    @cached_property
    def usageTrackingResource(self):  # pragma: no cover
        return UsageTrackingResource.make_one(
            self.boto3_raw_data["usageTrackingResource"]
        )

    status = field("status")
    displayName = field("displayName")
    approximateDollarLimit = field("approximateDollarLimit")

    @cached_property
    def usages(self):  # pragma: no cover
        return ConsumedUsages.make_one(self.boto3_raw_data["usages"])

    createdBy = field("createdBy")
    createdAt = field("createdAt")
    description = field("description")
    updatedBy = field("updatedBy")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BudgetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyJobTemplateRequest:
    boto3_raw_data: "type_defs.CopyJobTemplateRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    jobId = field("jobId")
    queueId = field("queueId")

    @cached_property
    def targetS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["targetS3Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkerResponse:
    boto3_raw_data: "type_defs.UpdateWorkerResponseTypeDef" = dataclasses.field()

    @cached_property
    def log(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["log"])

    @cached_property
    def hostConfiguration(self):  # pragma: no cover
        return HostConfiguration.make_one(self.boto3_raw_data["hostConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSearchSummary:
    boto3_raw_data: "type_defs.JobSearchSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    queueId = field("queueId")
    name = field("name")
    lifecycleStatus = field("lifecycleStatus")
    lifecycleStatusMessage = field("lifecycleStatusMessage")
    taskRunStatus = field("taskRunStatus")
    targetTaskRunStatus = field("targetTaskRunStatus")
    taskRunStatusCounts = field("taskRunStatusCounts")
    taskFailureRetryCount = field("taskFailureRetryCount")
    priority = field("priority")
    maxFailedTasksCount = field("maxFailedTasksCount")
    maxRetriesPerTask = field("maxRetriesPerTask")
    createdBy = field("createdBy")
    createdAt = field("createdAt")
    endedAt = field("endedAt")
    startedAt = field("startedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    jobParameters = field("jobParameters")
    maxWorkerCount = field("maxWorkerCount")
    sourceJobId = field("sourceJobId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSearchSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageProfileRequest:
    boto3_raw_data: "type_defs.CreateStorageProfileRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    displayName = field("displayName")
    osFamily = field("osFamily")
    clientToken = field("clientToken")

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return FileSystemLocation.make_many(self.boto3_raw_data["fileSystemLocations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStorageProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageProfileForQueueResponse:
    boto3_raw_data: "type_defs.GetStorageProfileForQueueResponseTypeDef" = (
        dataclasses.field()
    )

    storageProfileId = field("storageProfileId")
    displayName = field("displayName")
    osFamily = field("osFamily")

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return FileSystemLocation.make_many(self.boto3_raw_data["fileSystemLocations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStorageProfileForQueueResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageProfileForQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageProfileResponse:
    boto3_raw_data: "type_defs.GetStorageProfileResponseTypeDef" = dataclasses.field()

    storageProfileId = field("storageProfileId")
    displayName = field("displayName")
    osFamily = field("osFamily")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def fileSystemLocations(self):  # pragma: no cover
        return FileSystemLocation.make_many(self.boto3_raw_data["fileSystemLocations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStorageProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStorageProfileRequest:
    boto3_raw_data: "type_defs.UpdateStorageProfileRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    storageProfileId = field("storageProfileId")
    clientToken = field("clientToken")
    displayName = field("displayName")
    osFamily = field("osFamily")

    @cached_property
    def fileSystemLocationsToAdd(self):  # pragma: no cover
        return FileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocationsToAdd"]
        )

    @cached_property
    def fileSystemLocationsToRemove(self):  # pragma: no cover
        return FileSystemLocation.make_many(
            self.boto3_raw_data["fileSystemLocationsToRemove"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStorageProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStorageProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetCapabilities:
    boto3_raw_data: "type_defs.FleetCapabilitiesTypeDef" = dataclasses.field()

    @cached_property
    def amounts(self):  # pragma: no cover
        return FleetAmountCapability.make_many(self.boto3_raw_data["amounts"])

    @cached_property
    def attributes(self):  # pragma: no cover
        return FleetAttributeCapabilityOutput.make_many(
            self.boto3_raw_data["attributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetCapabilitiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedWorkerCapabilitiesOutput:
    boto3_raw_data: "type_defs.CustomerManagedWorkerCapabilitiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vCpuCount(self):  # pragma: no cover
        return VCpuCountRange.make_one(self.boto3_raw_data["vCpuCount"])

    @cached_property
    def memoryMiB(self):  # pragma: no cover
        return MemoryMiBRange.make_one(self.boto3_raw_data["memoryMiB"])

    osFamily = field("osFamily")
    cpuArchitectureType = field("cpuArchitectureType")
    acceleratorTypes = field("acceleratorTypes")

    @cached_property
    def acceleratorCount(self):  # pragma: no cover
        return AcceleratorCountRange.make_one(self.boto3_raw_data["acceleratorCount"])

    @cached_property
    def acceleratorTotalMemoryMiB(self):  # pragma: no cover
        return AcceleratorTotalMemoryMiBRange.make_one(
            self.boto3_raw_data["acceleratorTotalMemoryMiB"]
        )

    @cached_property
    def customAmounts(self):  # pragma: no cover
        return FleetAmountCapability.make_many(self.boto3_raw_data["customAmounts"])

    @cached_property
    def customAttributes(self):  # pragma: no cover
        return FleetAttributeCapabilityOutput.make_many(
            self.boto3_raw_data["customAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedWorkerCapabilitiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedWorkerCapabilitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedWorkerCapabilities:
    boto3_raw_data: "type_defs.CustomerManagedWorkerCapabilitiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vCpuCount(self):  # pragma: no cover
        return VCpuCountRange.make_one(self.boto3_raw_data["vCpuCount"])

    @cached_property
    def memoryMiB(self):  # pragma: no cover
        return MemoryMiBRange.make_one(self.boto3_raw_data["memoryMiB"])

    osFamily = field("osFamily")
    cpuArchitectureType = field("cpuArchitectureType")
    acceleratorTypes = field("acceleratorTypes")

    @cached_property
    def acceleratorCount(self):  # pragma: no cover
        return AcceleratorCountRange.make_one(self.boto3_raw_data["acceleratorCount"])

    @cached_property
    def acceleratorTotalMemoryMiB(self):  # pragma: no cover
        return AcceleratorTotalMemoryMiBRange.make_one(
            self.boto3_raw_data["acceleratorTotalMemoryMiB"]
        )

    @cached_property
    def customAmounts(self):  # pragma: no cover
        return FleetAmountCapability.make_many(self.boto3_raw_data["customAmounts"])

    @cached_property
    def customAttributes(self):  # pragma: no cover
        return FleetAttributeCapability.make_many(
            self.boto3_raw_data["customAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedWorkerCapabilitiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedWorkerCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateTimeFilterExpression:
    boto3_raw_data: "type_defs.DateTimeFilterExpressionTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    dateTime = field("dateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DateTimeFilterExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateTimeFilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedBudgetSchedule:
    boto3_raw_data: "type_defs.FixedBudgetScheduleTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FixedBudgetScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedBudgetScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepSummary:
    boto3_raw_data: "type_defs.StepSummaryTypeDef" = dataclasses.field()

    stepId = field("stepId")
    name = field("name")
    lifecycleStatus = field("lifecycleStatus")
    taskRunStatus = field("taskRunStatus")
    taskRunStatusCounts = field("taskRunStatusCounts")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    lifecycleStatusMessage = field("lifecycleStatusMessage")
    taskFailureRetryCount = field("taskFailureRetryCount")
    targetTaskRunStatus = field("targetTaskRunStatus")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    startedAt = field("startedAt")
    endedAt = field("endedAt")

    @cached_property
    def dependencyCounts(self):  # pragma: no cover
        return DependencyCounts.make_one(self.boto3_raw_data["dependencyCounts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFarmMembersResponse:
    boto3_raw_data: "type_defs.ListFarmMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def members(self):  # pragma: no cover
        return FarmMember.make_many(self.boto3_raw_data["members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFarmMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFarmMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFarmsResponse:
    boto3_raw_data: "type_defs.ListFarmsResponseTypeDef" = dataclasses.field()

    @cached_property
    def farms(self):  # pragma: no cover
        return FarmSummary.make_many(self.boto3_raw_data["farms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFarmsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFarmsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetMembersResponse:
    boto3_raw_data: "type_defs.ListFleetMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def members(self):  # pragma: no cover
        return FleetMember.make_many(self.boto3_raw_data["members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFleetRequestWait:
    boto3_raw_data: "type_defs.GetFleetRequestWaitTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFleetRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFleetRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRequestWait:
    boto3_raw_data: "type_defs.GetJobRequestWaitTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRequestWaitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseEndpointRequestWaitExtra:
    boto3_raw_data: "type_defs.GetLicenseEndpointRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    licenseEndpointId = field("licenseEndpointId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLicenseEndpointRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseEndpointRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLicenseEndpointRequestWait:
    boto3_raw_data: "type_defs.GetLicenseEndpointRequestWaitTypeDef" = (
        dataclasses.field()
    )

    licenseEndpointId = field("licenseEndpointId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLicenseEndpointRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLicenseEndpointRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueFleetAssociationRequestWait:
    boto3_raw_data: "type_defs.GetQueueFleetAssociationRequestWaitTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueueFleetAssociationRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueFleetAssociationRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueLimitAssociationRequestWait:
    boto3_raw_data: "type_defs.GetQueueLimitAssociationRequestWaitTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueueLimitAssociationRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueLimitAssociationRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueRequestWaitExtra:
    boto3_raw_data: "type_defs.GetQueueRequestWaitExtraTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueueRequestWait:
    boto3_raw_data: "type_defs.GetQueueRequestWaitTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueueRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobEntityError:
    boto3_raw_data: "type_defs.GetJobEntityErrorTypeDef" = dataclasses.field()

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetailsError.make_one(self.boto3_raw_data["jobDetails"])

    @cached_property
    def jobAttachmentDetails(self):  # pragma: no cover
        return JobAttachmentDetailsError.make_one(
            self.boto3_raw_data["jobAttachmentDetails"]
        )

    @cached_property
    def stepDetails(self):  # pragma: no cover
        return StepDetailsError.make_one(self.boto3_raw_data["stepDetails"])

    @cached_property
    def environmentDetails(self):  # pragma: no cover
        return EnvironmentDetailsError.make_one(
            self.boto3_raw_data["environmentDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobEntityErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobEntityErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionsStatisticsAggregationRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetSessionsStatisticsAggregationRequestPaginateTypeDef"
    ) = dataclasses.field()

    farmId = field("farmId")
    aggregationId = field("aggregationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSessionsStatisticsAggregationRequestPaginateTypeDef"
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
                "type_defs.GetSessionsStatisticsAggregationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableMeteredProductsRequestPaginate:
    boto3_raw_data: "type_defs.ListAvailableMeteredProductsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableMeteredProductsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableMeteredProductsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBudgetsRequestPaginate:
    boto3_raw_data: "type_defs.ListBudgetsRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBudgetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBudgetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFarmMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListFarmMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFarmMembersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFarmMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFarmsRequestPaginate:
    boto3_raw_data: "type_defs.ListFarmsRequestPaginateTypeDef" = dataclasses.field()

    principalId = field("principalId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFarmsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFarmsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListFleetMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFleetMembersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsRequestPaginate:
    boto3_raw_data: "type_defs.ListFleetsRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    principalId = field("principalId")
    displayName = field("displayName")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListJobMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobMembersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobParameterDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobParameterDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    jobId = field("jobId")
    queueId = field("queueId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobParameterDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobParameterDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    principalId = field("principalId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListLicenseEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLicenseEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLimitsRequestPaginate:
    boto3_raw_data: "type_defs.ListLimitsRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLimitsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLimitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMeteredProductsRequestPaginate:
    boto3_raw_data: "type_defs.ListMeteredProductsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    licenseEndpointId = field("licenseEndpointId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMeteredProductsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMeteredProductsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsRequestPaginate:
    boto3_raw_data: "type_defs.ListMonitorsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListQueueEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueEnvironmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueFleetAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListQueueFleetAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    fleetId = field("fleetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueFleetAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueFleetAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueLimitAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListQueueLimitAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    limitId = field("limitId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueLimitAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueLimitAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListQueueMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueueMembersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueMembersRequestPaginateTypeDef"]
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

    farmId = field("farmId")
    principalId = field("principalId")
    status = field("status")

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
class ListSessionActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    sessionId = field("sessionId")
    taskId = field("taskId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSessionActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsForWorkerRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionsForWorkerRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSessionsForWorkerRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsForWorkerRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionsRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepConsumersRequestPaginate:
    boto3_raw_data: "type_defs.ListStepConsumersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStepConsumersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepConsumersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepDependenciesRequestPaginate:
    boto3_raw_data: "type_defs.ListStepDependenciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStepDependenciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepDependenciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepsRequestPaginate:
    boto3_raw_data: "type_defs.ListStepsRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStepsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageProfilesForQueueRequestPaginate:
    boto3_raw_data: "type_defs.ListStorageProfilesForQueueRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")
    queueId = field("queueId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageProfilesForQueueRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageProfilesForQueueRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListStorageProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksRequestPaginate:
    boto3_raw_data: "type_defs.ListTasksRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    jobId = field("jobId")
    stepId = field("stepId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTasksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkersRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkersRequestPaginateTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostPropertiesResponse:
    boto3_raw_data: "type_defs.HostPropertiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ipAddresses(self):  # pragma: no cover
        return IpAddressesOutput.make_one(self.boto3_raw_data["ipAddresses"])

    hostName = field("hostName")
    ec2InstanceArn = field("ec2InstanceArn")
    ec2InstanceType = field("ec2InstanceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HostPropertiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostPropertiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobEntityIdentifiersUnion:
    boto3_raw_data: "type_defs.JobEntityIdentifiersUnionTypeDef" = dataclasses.field()

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetailsIdentifiers.make_one(self.boto3_raw_data["jobDetails"])

    @cached_property
    def jobAttachmentDetails(self):  # pragma: no cover
        return JobAttachmentDetailsIdentifiers.make_one(
            self.boto3_raw_data["jobAttachmentDetails"]
        )

    @cached_property
    def stepDetails(self):  # pragma: no cover
        return StepDetailsIdentifiers.make_one(self.boto3_raw_data["stepDetails"])

    @cached_property
    def environmentDetails(self):  # pragma: no cover
        return EnvironmentDetailsIdentifiers.make_one(
            self.boto3_raw_data["environmentDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobEntityIdentifiersUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobEntityIdentifiersUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobMembersResponse:
    boto3_raw_data: "type_defs.ListJobMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def members(self):  # pragma: no cover
        return JobMember.make_many(self.boto3_raw_data["members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunAsUser:
    boto3_raw_data: "type_defs.JobRunAsUserTypeDef" = dataclasses.field()

    runAs = field("runAs")

    @cached_property
    def posix(self):  # pragma: no cover
        return PosixUser.make_one(self.boto3_raw_data["posix"])

    @cached_property
    def windows(self):  # pragma: no cover
        return WindowsUser.make_one(self.boto3_raw_data["windows"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunAsUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunAsUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResponse:
    boto3_raw_data: "type_defs.ListJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLicenseEndpointsResponse:
    boto3_raw_data: "type_defs.ListLicenseEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def licenseEndpoints(self):  # pragma: no cover
        return LicenseEndpointSummary.make_many(self.boto3_raw_data["licenseEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLicenseEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLicenseEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLimitsResponse:
    boto3_raw_data: "type_defs.ListLimitsResponseTypeDef" = dataclasses.field()

    @cached_property
    def limits(self):  # pragma: no cover
        return LimitSummary.make_many(self.boto3_raw_data["limits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLimitsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLimitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableMeteredProductsResponse:
    boto3_raw_data: "type_defs.ListAvailableMeteredProductsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def meteredProducts(self):  # pragma: no cover
        return MeteredProductSummary.make_many(self.boto3_raw_data["meteredProducts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableMeteredProductsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableMeteredProductsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMeteredProductsResponse:
    boto3_raw_data: "type_defs.ListMeteredProductsResponseTypeDef" = dataclasses.field()

    @cached_property
    def meteredProducts(self):  # pragma: no cover
        return MeteredProductSummary.make_many(self.boto3_raw_data["meteredProducts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMeteredProductsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMeteredProductsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsResponse:
    boto3_raw_data: "type_defs.ListMonitorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def monitors(self):  # pragma: no cover
        return MonitorSummary.make_many(self.boto3_raw_data["monitors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueEnvironmentsResponse:
    boto3_raw_data: "type_defs.ListQueueEnvironmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environments(self):  # pragma: no cover
        return QueueEnvironmentSummary.make_many(self.boto3_raw_data["environments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueueEnvironmentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueFleetAssociationsResponse:
    boto3_raw_data: "type_defs.ListQueueFleetAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def queueFleetAssociations(self):  # pragma: no cover
        return QueueFleetAssociationSummary.make_many(
            self.boto3_raw_data["queueFleetAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueFleetAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueFleetAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueLimitAssociationsResponse:
    boto3_raw_data: "type_defs.ListQueueLimitAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def queueLimitAssociations(self):  # pragma: no cover
        return QueueLimitAssociationSummary.make_many(
            self.boto3_raw_data["queueLimitAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueLimitAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueLimitAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueMembersResponse:
    boto3_raw_data: "type_defs.ListQueueMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def members(self):  # pragma: no cover
        return QueueMember.make_many(self.boto3_raw_data["members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueueMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuesResponse:
    boto3_raw_data: "type_defs.ListQueuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def queues(self):  # pragma: no cover
        return QueueSummary.make_many(self.boto3_raw_data["queues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsForWorkerResponse:
    boto3_raw_data: "type_defs.ListSessionsForWorkerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sessions(self):  # pragma: no cover
        return WorkerSessionSummary.make_many(self.boto3_raw_data["sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSessionsForWorkerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsForWorkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsResponse:
    boto3_raw_data: "type_defs.ListSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessions(self):  # pragma: no cover
        return SessionSummary.make_many(self.boto3_raw_data["sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepConsumersResponse:
    boto3_raw_data: "type_defs.ListStepConsumersResponseTypeDef" = dataclasses.field()

    @cached_property
    def consumers(self):  # pragma: no cover
        return StepConsumer.make_many(self.boto3_raw_data["consumers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStepConsumersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepConsumersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepDependenciesResponse:
    boto3_raw_data: "type_defs.ListStepDependenciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dependencies(self):  # pragma: no cover
        return StepDependency.make_many(self.boto3_raw_data["dependencies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStepDependenciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepDependenciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageProfilesForQueueResponse:
    boto3_raw_data: "type_defs.ListStorageProfilesForQueueResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageProfiles(self):  # pragma: no cover
        return StorageProfileSummary.make_many(self.boto3_raw_data["storageProfiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageProfilesForQueueResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageProfilesForQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageProfilesResponse:
    boto3_raw_data: "type_defs.ListStorageProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def storageProfiles(self):  # pragma: no cover
        return StorageProfileSummary.make_many(self.boto3_raw_data["storageProfiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStorageProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterSpace:
    boto3_raw_data: "type_defs.ParameterSpaceTypeDef" = dataclasses.field()

    @cached_property
    def parameters(self):  # pragma: no cover
        return StepParameter.make_many(self.boto3_raw_data["parameters"])

    combination = field("combination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterSpaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterSpaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSortExpression:
    boto3_raw_data: "type_defs.SearchSortExpressionTypeDef" = dataclasses.field()

    @cached_property
    def userJobsFirst(self):  # pragma: no cover
        return UserJobsFirst.make_one(self.boto3_raw_data["userJobsFirst"])

    @cached_property
    def fieldSort(self):  # pragma: no cover
        return FieldSortExpression.make_one(self.boto3_raw_data["fieldSort"])

    @cached_property
    def parameterSort(self):  # pragma: no cover
        return ParameterSortExpression.make_one(self.boto3_raw_data["parameterSort"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchSortExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSortExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSessionsStatisticsAggregationRequest:
    boto3_raw_data: "type_defs.StartSessionsStatisticsAggregationRequestTypeDef" = (
        dataclasses.field()
    )

    farmId = field("farmId")

    @cached_property
    def resourceIds(self):  # pragma: no cover
        return SessionsStatisticsResources.make_one(self.boto3_raw_data["resourceIds"])

    startTime = field("startTime")
    endTime = field("endTime")
    groupBy = field("groupBy")
    statistics = field("statistics")
    timezone = field("timezone")
    period = field("period")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSessionsStatisticsAggregationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionsStatisticsAggregationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statistics:
    boto3_raw_data: "type_defs.StatisticsTypeDef" = dataclasses.field()

    count = field("count")

    @cached_property
    def costInUsd(self):  # pragma: no cover
        return Stats.make_one(self.boto3_raw_data["costInUsd"])

    @cached_property
    def runtimeInSeconds(self):  # pragma: no cover
        return Stats.make_one(self.boto3_raw_data["runtimeInSeconds"])

    queueId = field("queueId")
    fleetId = field("fleetId")
    jobId = field("jobId")
    jobName = field("jobName")
    userId = field("userId")
    usageType = field("usageType")
    licenseProduct = field("licenseProduct")
    instanceType = field("instanceType")
    aggregationStartTime = field("aggregationStartTime")
    aggregationEndTime = field("aggregationEndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepRequiredCapabilities:
    boto3_raw_data: "type_defs.StepRequiredCapabilitiesTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return StepAttributeCapability.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def amounts(self):  # pragma: no cover
        return StepAmountCapability.make_many(self.boto3_raw_data["amounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepRequiredCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepRequiredCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatedSessionActionInfo:
    boto3_raw_data: "type_defs.UpdatedSessionActionInfoTypeDef" = dataclasses.field()

    completedStatus = field("completedStatus")
    processExitCode = field("processExitCode")
    progressMessage = field("progressMessage")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    progressPercent = field("progressPercent")

    @cached_property
    def manifests(self):  # pragma: no cover
        return TaskRunManifestPropertiesRequest.make_many(
            self.boto3_raw_data["manifests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatedSessionActionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatedSessionActionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerCapabilities:
    boto3_raw_data: "type_defs.WorkerCapabilitiesTypeDef" = dataclasses.field()

    @cached_property
    def amounts(self):  # pragma: no cover
        return WorkerAmountCapability.make_many(self.boto3_raw_data["amounts"])

    @cached_property
    def attributes(self):  # pragma: no cover
        return WorkerAttributeCapability.make_many(self.boto3_raw_data["attributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEc2InstanceCapabilitiesOutput:
    boto3_raw_data: "type_defs.ServiceManagedEc2InstanceCapabilitiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vCpuCount(self):  # pragma: no cover
        return VCpuCountRange.make_one(self.boto3_raw_data["vCpuCount"])

    @cached_property
    def memoryMiB(self):  # pragma: no cover
        return MemoryMiBRange.make_one(self.boto3_raw_data["memoryMiB"])

    osFamily = field("osFamily")
    cpuArchitectureType = field("cpuArchitectureType")

    @cached_property
    def rootEbsVolume(self):  # pragma: no cover
        return Ec2EbsVolume.make_one(self.boto3_raw_data["rootEbsVolume"])

    @cached_property
    def acceleratorCapabilities(self):  # pragma: no cover
        return AcceleratorCapabilitiesOutput.make_one(
            self.boto3_raw_data["acceleratorCapabilities"]
        )

    allowedInstanceTypes = field("allowedInstanceTypes")
    excludedInstanceTypes = field("excludedInstanceTypes")

    @cached_property
    def customAmounts(self):  # pragma: no cover
        return FleetAmountCapability.make_many(self.boto3_raw_data["customAmounts"])

    @cached_property
    def customAttributes(self):  # pragma: no cover
        return FleetAttributeCapabilityOutput.make_many(
            self.boto3_raw_data["customAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEc2InstanceCapabilitiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEc2InstanceCapabilitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEc2InstanceCapabilities:
    boto3_raw_data: "type_defs.ServiceManagedEc2InstanceCapabilitiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vCpuCount(self):  # pragma: no cover
        return VCpuCountRange.make_one(self.boto3_raw_data["vCpuCount"])

    @cached_property
    def memoryMiB(self):  # pragma: no cover
        return MemoryMiBRange.make_one(self.boto3_raw_data["memoryMiB"])

    osFamily = field("osFamily")
    cpuArchitectureType = field("cpuArchitectureType")

    @cached_property
    def rootEbsVolume(self):  # pragma: no cover
        return Ec2EbsVolume.make_one(self.boto3_raw_data["rootEbsVolume"])

    @cached_property
    def acceleratorCapabilities(self):  # pragma: no cover
        return AcceleratorCapabilities.make_one(
            self.boto3_raw_data["acceleratorCapabilities"]
        )

    allowedInstanceTypes = field("allowedInstanceTypes")
    excludedInstanceTypes = field("excludedInstanceTypes")

    @cached_property
    def customAmounts(self):  # pragma: no cover
        return FleetAmountCapability.make_many(self.boto3_raw_data["customAmounts"])

    @cached_property
    def customAttributes(self):  # pragma: no cover
        return FleetAttributeCapability.make_many(
            self.boto3_raw_data["customAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEc2InstanceCapabilitiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEc2InstanceCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedSessionActionDefinition:
    boto3_raw_data: "type_defs.AssignedSessionActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def envEnter(self):  # pragma: no cover
        return AssignedEnvironmentEnterSessionActionDefinition.make_one(
            self.boto3_raw_data["envEnter"]
        )

    @cached_property
    def envExit(self):  # pragma: no cover
        return AssignedEnvironmentExitSessionActionDefinition.make_one(
            self.boto3_raw_data["envExit"]
        )

    @cached_property
    def taskRun(self):  # pragma: no cover
        return AssignedTaskRunSessionActionDefinition.make_one(
            self.boto3_raw_data["taskRun"]
        )

    @cached_property
    def syncInputJobAttachments(self):  # pragma: no cover
        return AssignedSyncInputJobAttachmentsSessionActionDefinition.make_one(
            self.boto3_raw_data["syncInputJobAttachments"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssignedSessionActionDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignedSessionActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionActionDefinitionSummary:
    boto3_raw_data: "type_defs.SessionActionDefinitionSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def envEnter(self):  # pragma: no cover
        return EnvironmentEnterSessionActionDefinitionSummary.make_one(
            self.boto3_raw_data["envEnter"]
        )

    @cached_property
    def envExit(self):  # pragma: no cover
        return EnvironmentExitSessionActionDefinitionSummary.make_one(
            self.boto3_raw_data["envExit"]
        )

    @cached_property
    def taskRun(self):  # pragma: no cover
        return TaskRunSessionActionDefinitionSummary.make_one(
            self.boto3_raw_data["taskRun"]
        )

    @cached_property
    def syncInputJobAttachments(self):  # pragma: no cover
        return SyncInputJobAttachmentsSessionActionDefinitionSummary.make_one(
            self.boto3_raw_data["syncInputJobAttachments"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SessionActionDefinitionSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionActionDefinitionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionActionDefinition:
    boto3_raw_data: "type_defs.SessionActionDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def envEnter(self):  # pragma: no cover
        return EnvironmentEnterSessionActionDefinition.make_one(
            self.boto3_raw_data["envEnter"]
        )

    @cached_property
    def envExit(self):  # pragma: no cover
        return EnvironmentExitSessionActionDefinition.make_one(
            self.boto3_raw_data["envExit"]
        )

    @cached_property
    def taskRun(self):  # pragma: no cover
        return TaskRunSessionActionDefinition.make_one(self.boto3_raw_data["taskRun"])

    @cached_property
    def syncInputJobAttachments(self):  # pragma: no cover
        return SyncInputJobAttachmentsSessionActionDefinition.make_one(
            self.boto3_raw_data["syncInputJobAttachments"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTasksResponse:
    boto3_raw_data: "type_defs.SearchTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return TaskSearchSummary.make_many(self.boto3_raw_data["tasks"])

    nextItemOffset = field("nextItemOffset")
    totalResults = field("totalResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksResponse:
    boto3_raw_data: "type_defs.ListTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return TaskSummary.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksResponseTypeDef"]
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

    jobId = field("jobId")
    name = field("name")
    lifecycleStatus = field("lifecycleStatus")
    lifecycleStatusMessage = field("lifecycleStatusMessage")
    priority = field("priority")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    taskRunStatus = field("taskRunStatus")
    targetTaskRunStatus = field("targetTaskRunStatus")
    taskRunStatusCounts = field("taskRunStatusCounts")
    taskFailureRetryCount = field("taskFailureRetryCount")
    storageProfileId = field("storageProfileId")
    maxFailedTasksCount = field("maxFailedTasksCount")
    maxRetriesPerTask = field("maxRetriesPerTask")
    parameters = field("parameters")

    @cached_property
    def attachments(self):  # pragma: no cover
        return AttachmentsOutput.make_one(self.boto3_raw_data["attachments"])

    description = field("description")
    maxWorkerCount = field("maxWorkerCount")
    sourceJobId = field("sourceJobId")

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


@dataclasses.dataclass(frozen=True)
class JobAttachmentDetailsEntity:
    boto3_raw_data: "type_defs.JobAttachmentDetailsEntityTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def attachments(self):  # pragma: no cover
        return AttachmentsOutput.make_one(self.boto3_raw_data["attachments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobAttachmentDetailsEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobAttachmentDetailsEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBudgetResponse:
    boto3_raw_data: "type_defs.GetBudgetResponseTypeDef" = dataclasses.field()

    budgetId = field("budgetId")

    @cached_property
    def usageTrackingResource(self):  # pragma: no cover
        return UsageTrackingResource.make_one(
            self.boto3_raw_data["usageTrackingResource"]
        )

    status = field("status")
    displayName = field("displayName")
    description = field("description")
    approximateDollarLimit = field("approximateDollarLimit")

    @cached_property
    def usages(self):  # pragma: no cover
        return ConsumedUsages.make_one(self.boto3_raw_data["usages"])

    @cached_property
    def actions(self):  # pragma: no cover
        return ResponseBudgetAction.make_many(self.boto3_raw_data["actions"])

    @cached_property
    def schedule(self):  # pragma: no cover
        return BudgetScheduleOutput.make_one(self.boto3_raw_data["schedule"])

    createdBy = field("createdBy")
    createdAt = field("createdAt")
    updatedBy = field("updatedBy")
    updatedAt = field("updatedAt")
    queueStoppedAt = field("queueStoppedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBudgetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBudgetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBudgetsResponse:
    boto3_raw_data: "type_defs.ListBudgetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def budgets(self):  # pragma: no cover
        return BudgetSummary.make_many(self.boto3_raw_data["budgets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBudgetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBudgetsResponseTypeDef"]
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
        return JobSearchSummary.make_many(self.boto3_raw_data["jobs"])

    nextItemOffset = field("nextItemOffset")
    totalResults = field("totalResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class CustomerManagedFleetConfigurationOutput:
    boto3_raw_data: "type_defs.CustomerManagedFleetConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    mode = field("mode")

    @cached_property
    def workerCapabilities(self):  # pragma: no cover
        return CustomerManagedWorkerCapabilitiesOutput.make_one(
            self.boto3_raw_data["workerCapabilities"]
        )

    storageProfileId = field("storageProfileId")
    tagPropagationMode = field("tagPropagationMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedFleetConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedFleetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedFleetConfiguration:
    boto3_raw_data: "type_defs.CustomerManagedFleetConfigurationTypeDef" = (
        dataclasses.field()
    )

    mode = field("mode")

    @cached_property
    def workerCapabilities(self):  # pragma: no cover
        return CustomerManagedWorkerCapabilities.make_one(
            self.boto3_raw_data["workerCapabilities"]
        )

    storageProfileId = field("storageProfileId")
    tagPropagationMode = field("tagPropagationMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerManagedFleetConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedFleetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFilterExpression:
    boto3_raw_data: "type_defs.SearchFilterExpressionTypeDef" = dataclasses.field()

    @cached_property
    def dateTimeFilter(self):  # pragma: no cover
        return DateTimeFilterExpression.make_one(self.boto3_raw_data["dateTimeFilter"])

    @cached_property
    def parameterFilter(self):  # pragma: no cover
        return ParameterFilterExpression.make_one(
            self.boto3_raw_data["parameterFilter"]
        )

    @cached_property
    def searchTermFilter(self):  # pragma: no cover
        return SearchTermFilterExpression.make_one(
            self.boto3_raw_data["searchTermFilter"]
        )

    @cached_property
    def stringFilter(self):  # pragma: no cover
        return StringFilterExpression.make_one(self.boto3_raw_data["stringFilter"])

    groupFilter = field("groupFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchFilterExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchFilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BudgetSchedule:
    boto3_raw_data: "type_defs.BudgetScheduleTypeDef" = dataclasses.field()

    @cached_property
    def fixed(self):  # pragma: no cover
        return FixedBudgetSchedule.make_one(self.boto3_raw_data["fixed"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BudgetScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepsResponse:
    boto3_raw_data: "type_defs.ListStepsResponseTypeDef" = dataclasses.field()

    @cached_property
    def steps(self):  # pragma: no cover
        return StepSummary.make_many(self.boto3_raw_data["steps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStepsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    fleetId = field("fleetId")
    workerId = field("workerId")
    startedAt = field("startedAt")

    @cached_property
    def log(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["log"])

    lifecycleStatus = field("lifecycleStatus")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    targetLifecycleStatus = field("targetLifecycleStatus")

    @cached_property
    def hostProperties(self):  # pragma: no cover
        return HostPropertiesResponse.make_one(self.boto3_raw_data["hostProperties"])

    @cached_property
    def workerLog(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["workerLog"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkerResponse:
    boto3_raw_data: "type_defs.GetWorkerResponseTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")

    @cached_property
    def hostProperties(self):  # pragma: no cover
        return HostPropertiesResponse.make_one(self.boto3_raw_data["hostProperties"])

    status = field("status")

    @cached_property
    def log(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["log"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetWorkerResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerSearchSummary:
    boto3_raw_data: "type_defs.WorkerSearchSummaryTypeDef" = dataclasses.field()

    fleetId = field("fleetId")
    workerId = field("workerId")
    status = field("status")

    @cached_property
    def hostProperties(self):  # pragma: no cover
        return HostPropertiesResponse.make_one(self.boto3_raw_data["hostProperties"])

    createdBy = field("createdBy")
    createdAt = field("createdAt")
    updatedBy = field("updatedBy")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerSearchSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerSummary:
    boto3_raw_data: "type_defs.WorkerSummaryTypeDef" = dataclasses.field()

    workerId = field("workerId")
    farmId = field("farmId")
    fleetId = field("fleetId")
    status = field("status")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def hostProperties(self):  # pragma: no cover
        return HostPropertiesResponse.make_one(self.boto3_raw_data["hostProperties"])

    @cached_property
    def log(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["log"])

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostPropertiesRequest:
    boto3_raw_data: "type_defs.HostPropertiesRequestTypeDef" = dataclasses.field()

    ipAddresses = field("ipAddresses")
    hostName = field("hostName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HostPropertiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetJobEntityRequest:
    boto3_raw_data: "type_defs.BatchGetJobEntityRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")

    @cached_property
    def identifiers(self):  # pragma: no cover
        return JobEntityIdentifiersUnion.make_many(self.boto3_raw_data["identifiers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetJobEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetJobEntityRequestTypeDef"]
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

    farmId = field("farmId")
    displayName = field("displayName")
    clientToken = field("clientToken")
    description = field("description")
    defaultBudgetAction = field("defaultBudgetAction")

    @cached_property
    def jobAttachmentSettings(self):  # pragma: no cover
        return JobAttachmentSettings.make_one(
            self.boto3_raw_data["jobAttachmentSettings"]
        )

    roleArn = field("roleArn")

    @cached_property
    def jobRunAsUser(self):  # pragma: no cover
        return JobRunAsUser.make_one(self.boto3_raw_data["jobRunAsUser"])

    requiredFileSystemLocationNames = field("requiredFileSystemLocationNames")
    allowedStorageProfileIds = field("allowedStorageProfileIds")
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
class GetQueueResponse:
    boto3_raw_data: "type_defs.GetQueueResponseTypeDef" = dataclasses.field()

    queueId = field("queueId")
    displayName = field("displayName")
    description = field("description")
    farmId = field("farmId")
    status = field("status")
    defaultBudgetAction = field("defaultBudgetAction")
    blockedReason = field("blockedReason")

    @cached_property
    def jobAttachmentSettings(self):  # pragma: no cover
        return JobAttachmentSettings.make_one(
            self.boto3_raw_data["jobAttachmentSettings"]
        )

    roleArn = field("roleArn")
    requiredFileSystemLocationNames = field("requiredFileSystemLocationNames")
    allowedStorageProfileIds = field("allowedStorageProfileIds")

    @cached_property
    def jobRunAsUser(self):  # pragma: no cover
        return JobRunAsUser.make_one(self.boto3_raw_data["jobRunAsUser"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueueResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDetailsEntity:
    boto3_raw_data: "type_defs.JobDetailsEntityTypeDef" = dataclasses.field()

    jobId = field("jobId")
    logGroupName = field("logGroupName")
    schemaVersion = field("schemaVersion")

    @cached_property
    def jobAttachmentSettings(self):  # pragma: no cover
        return JobAttachmentSettings.make_one(
            self.boto3_raw_data["jobAttachmentSettings"]
        )

    @cached_property
    def jobRunAsUser(self):  # pragma: no cover
        return JobRunAsUser.make_one(self.boto3_raw_data["jobRunAsUser"])

    queueRoleArn = field("queueRoleArn")
    parameters = field("parameters")

    @cached_property
    def pathMappingRules(self):  # pragma: no cover
        return PathMappingRule.make_many(self.boto3_raw_data["pathMappingRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDetailsEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobDetailsEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueRequest:
    boto3_raw_data: "type_defs.UpdateQueueRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    clientToken = field("clientToken")
    displayName = field("displayName")
    description = field("description")
    defaultBudgetAction = field("defaultBudgetAction")

    @cached_property
    def jobAttachmentSettings(self):  # pragma: no cover
        return JobAttachmentSettings.make_one(
            self.boto3_raw_data["jobAttachmentSettings"]
        )

    roleArn = field("roleArn")

    @cached_property
    def jobRunAsUser(self):  # pragma: no cover
        return JobRunAsUser.make_one(self.boto3_raw_data["jobRunAsUser"])

    requiredFileSystemLocationNamesToAdd = field("requiredFileSystemLocationNamesToAdd")
    requiredFileSystemLocationNamesToRemove = field(
        "requiredFileSystemLocationNamesToRemove"
    )
    allowedStorageProfileIdsToAdd = field("allowedStorageProfileIdsToAdd")
    allowedStorageProfileIdsToRemove = field("allowedStorageProfileIdsToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepSearchSummary:
    boto3_raw_data: "type_defs.StepSearchSummaryTypeDef" = dataclasses.field()

    stepId = field("stepId")
    jobId = field("jobId")
    queueId = field("queueId")
    name = field("name")
    lifecycleStatus = field("lifecycleStatus")
    lifecycleStatusMessage = field("lifecycleStatusMessage")
    taskRunStatus = field("taskRunStatus")
    targetTaskRunStatus = field("targetTaskRunStatus")
    taskRunStatusCounts = field("taskRunStatusCounts")
    taskFailureRetryCount = field("taskFailureRetryCount")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def parameterSpace(self):  # pragma: no cover
        return ParameterSpace.make_one(self.boto3_raw_data["parameterSpace"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepSearchSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionsStatisticsAggregationResponse:
    boto3_raw_data: "type_defs.GetSessionsStatisticsAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def statistics(self):  # pragma: no cover
        return Statistics.make_many(self.boto3_raw_data["statistics"])

    status = field("status")
    statusMessage = field("statusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSessionsStatisticsAggregationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionsStatisticsAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStepResponse:
    boto3_raw_data: "type_defs.GetStepResponseTypeDef" = dataclasses.field()

    stepId = field("stepId")
    name = field("name")
    lifecycleStatus = field("lifecycleStatus")
    lifecycleStatusMessage = field("lifecycleStatusMessage")
    taskRunStatus = field("taskRunStatus")
    taskRunStatusCounts = field("taskRunStatusCounts")
    taskFailureRetryCount = field("taskFailureRetryCount")
    targetTaskRunStatus = field("targetTaskRunStatus")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    startedAt = field("startedAt")
    endedAt = field("endedAt")

    @cached_property
    def dependencyCounts(self):  # pragma: no cover
        return DependencyCounts.make_one(self.boto3_raw_data["dependencyCounts"])

    @cached_property
    def requiredCapabilities(self):  # pragma: no cover
        return StepRequiredCapabilities.make_one(
            self.boto3_raw_data["requiredCapabilities"]
        )

    @cached_property
    def parameterSpace(self):  # pragma: no cover
        return ParameterSpace.make_one(self.boto3_raw_data["parameterSpace"])

    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStepResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStepResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkerScheduleRequest:
    boto3_raw_data: "type_defs.UpdateWorkerScheduleRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")
    updatedSessionActions = field("updatedSessionActions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkerScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkerScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEc2FleetConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceManagedEc2FleetConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instanceCapabilities(self):  # pragma: no cover
        return ServiceManagedEc2InstanceCapabilitiesOutput.make_one(
            self.boto3_raw_data["instanceCapabilities"]
        )

    @cached_property
    def instanceMarketOptions(self):  # pragma: no cover
        return ServiceManagedEc2InstanceMarketOptions.make_one(
            self.boto3_raw_data["instanceMarketOptions"]
        )

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["vpcConfiguration"])

    storageProfileId = field("storageProfileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEc2FleetConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEc2FleetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEc2FleetConfiguration:
    boto3_raw_data: "type_defs.ServiceManagedEc2FleetConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instanceCapabilities(self):  # pragma: no cover
        return ServiceManagedEc2InstanceCapabilities.make_one(
            self.boto3_raw_data["instanceCapabilities"]
        )

    @cached_property
    def instanceMarketOptions(self):  # pragma: no cover
        return ServiceManagedEc2InstanceMarketOptions.make_one(
            self.boto3_raw_data["instanceMarketOptions"]
        )

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["vpcConfiguration"])

    storageProfileId = field("storageProfileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEc2FleetConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEc2FleetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedSessionAction:
    boto3_raw_data: "type_defs.AssignedSessionActionTypeDef" = dataclasses.field()

    sessionActionId = field("sessionActionId")

    @cached_property
    def definition(self):  # pragma: no cover
        return AssignedSessionActionDefinition.make_one(
            self.boto3_raw_data["definition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignedSessionActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignedSessionActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionActionSummary:
    boto3_raw_data: "type_defs.SessionActionSummaryTypeDef" = dataclasses.field()

    sessionActionId = field("sessionActionId")
    status = field("status")

    @cached_property
    def definition(self):  # pragma: no cover
        return SessionActionDefinitionSummary.make_one(
            self.boto3_raw_data["definition"]
        )

    startedAt = field("startedAt")
    endedAt = field("endedAt")
    workerUpdatedAt = field("workerUpdatedAt")
    progressPercent = field("progressPercent")

    @cached_property
    def manifests(self):  # pragma: no cover
        return TaskRunManifestPropertiesResponse.make_many(
            self.boto3_raw_data["manifests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionActionResponse:
    boto3_raw_data: "type_defs.GetSessionActionResponseTypeDef" = dataclasses.field()

    sessionActionId = field("sessionActionId")
    status = field("status")
    startedAt = field("startedAt")
    endedAt = field("endedAt")
    workerUpdatedAt = field("workerUpdatedAt")
    progressPercent = field("progressPercent")
    sessionId = field("sessionId")
    processExitCode = field("processExitCode")
    progressMessage = field("progressMessage")

    @cached_property
    def definition(self):  # pragma: no cover
        return SessionActionDefinition.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def acquiredLimits(self):  # pragma: no cover
        return AcquiredLimit.make_many(self.boto3_raw_data["acquiredLimits"])

    @cached_property
    def manifests(self):  # pragma: no cover
        return TaskRunManifestPropertiesResponse.make_many(
            self.boto3_raw_data["manifests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueId = field("queueId")
    priority = field("priority")
    clientToken = field("clientToken")
    template = field("template")
    templateType = field("templateType")
    parameters = field("parameters")
    attachments = field("attachments")
    storageProfileId = field("storageProfileId")
    targetTaskRunStatus = field("targetTaskRunStatus")
    maxFailedTasksCount = field("maxFailedTasksCount")
    maxRetriesPerTask = field("maxRetriesPerTask")
    maxWorkerCount = field("maxWorkerCount")
    sourceJobId = field("sourceJobId")

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
class SearchGroupedFilterExpressions:
    boto3_raw_data: "type_defs.SearchGroupedFilterExpressionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return SearchFilterExpression.make_many(self.boto3_raw_data["filters"])

    operator = field("operator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchGroupedFilterExpressionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupedFilterExpressionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchWorkersResponse:
    boto3_raw_data: "type_defs.SearchWorkersResponseTypeDef" = dataclasses.field()

    @cached_property
    def workers(self):  # pragma: no cover
        return WorkerSearchSummary.make_many(self.boto3_raw_data["workers"])

    nextItemOffset = field("nextItemOffset")
    totalResults = field("totalResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchWorkersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchWorkersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkersResponse:
    boto3_raw_data: "type_defs.ListWorkersResponseTypeDef" = dataclasses.field()

    @cached_property
    def workers(self):  # pragma: no cover
        return WorkerSummary.make_many(self.boto3_raw_data["workers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkerRequest:
    boto3_raw_data: "type_defs.CreateWorkerRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")

    @cached_property
    def hostProperties(self):  # pragma: no cover
        return HostPropertiesRequest.make_one(self.boto3_raw_data["hostProperties"])

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkerRequest:
    boto3_raw_data: "type_defs.UpdateWorkerRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    workerId = field("workerId")
    status = field("status")

    @cached_property
    def capabilities(self):  # pragma: no cover
        return WorkerCapabilities.make_one(self.boto3_raw_data["capabilities"])

    @cached_property
    def hostProperties(self):  # pragma: no cover
        return HostPropertiesRequest.make_one(self.boto3_raw_data["hostProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobEntity:
    boto3_raw_data: "type_defs.JobEntityTypeDef" = dataclasses.field()

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetailsEntity.make_one(self.boto3_raw_data["jobDetails"])

    @cached_property
    def jobAttachmentDetails(self):  # pragma: no cover
        return JobAttachmentDetailsEntity.make_one(
            self.boto3_raw_data["jobAttachmentDetails"]
        )

    @cached_property
    def stepDetails(self):  # pragma: no cover
        return StepDetailsEntity.make_one(self.boto3_raw_data["stepDetails"])

    @cached_property
    def environmentDetails(self):  # pragma: no cover
        return EnvironmentDetailsEntity.make_one(
            self.boto3_raw_data["environmentDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobEntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchStepsResponse:
    boto3_raw_data: "type_defs.SearchStepsResponseTypeDef" = dataclasses.field()

    @cached_property
    def steps(self):  # pragma: no cover
        return StepSearchSummary.make_many(self.boto3_raw_data["steps"])

    nextItemOffset = field("nextItemOffset")
    totalResults = field("totalResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchStepsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetConfigurationOutput:
    boto3_raw_data: "type_defs.FleetConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def customerManaged(self):  # pragma: no cover
        return CustomerManagedFleetConfigurationOutput.make_one(
            self.boto3_raw_data["customerManaged"]
        )

    @cached_property
    def serviceManagedEc2(self):  # pragma: no cover
        return ServiceManagedEc2FleetConfigurationOutput.make_one(
            self.boto3_raw_data["serviceManagedEc2"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FleetConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetConfiguration:
    boto3_raw_data: "type_defs.FleetConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def customerManaged(self):  # pragma: no cover
        return CustomerManagedFleetConfiguration.make_one(
            self.boto3_raw_data["customerManaged"]
        )

    @cached_property
    def serviceManagedEc2(self):  # pragma: no cover
        return ServiceManagedEc2FleetConfiguration.make_one(
            self.boto3_raw_data["serviceManagedEc2"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FleetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignedSession:
    boto3_raw_data: "type_defs.AssignedSessionTypeDef" = dataclasses.field()

    queueId = field("queueId")
    jobId = field("jobId")

    @cached_property
    def sessionActions(self):  # pragma: no cover
        return AssignedSessionAction.make_many(self.boto3_raw_data["sessionActions"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssignedSessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssignedSessionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionActionsResponse:
    boto3_raw_data: "type_defs.ListSessionActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessionActions(self):  # pragma: no cover
        return SessionActionSummary.make_many(self.boto3_raw_data["sessionActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionActionsResponseTypeDef"]
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

    farmId = field("farmId")
    queueIds = field("queueIds")
    itemOffset = field("itemOffset")

    @cached_property
    def filterExpressions(self):  # pragma: no cover
        return SearchGroupedFilterExpressions.make_one(
            self.boto3_raw_data["filterExpressions"]
        )

    @cached_property
    def sortExpressions(self):  # pragma: no cover
        return SearchSortExpression.make_many(self.boto3_raw_data["sortExpressions"])

    pageSize = field("pageSize")

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
class SearchStepsRequest:
    boto3_raw_data: "type_defs.SearchStepsRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueIds = field("queueIds")
    itemOffset = field("itemOffset")
    jobId = field("jobId")

    @cached_property
    def filterExpressions(self):  # pragma: no cover
        return SearchGroupedFilterExpressions.make_one(
            self.boto3_raw_data["filterExpressions"]
        )

    @cached_property
    def sortExpressions(self):  # pragma: no cover
        return SearchSortExpression.make_many(self.boto3_raw_data["sortExpressions"])

    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchStepsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTasksRequest:
    boto3_raw_data: "type_defs.SearchTasksRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    queueIds = field("queueIds")
    itemOffset = field("itemOffset")
    jobId = field("jobId")

    @cached_property
    def filterExpressions(self):  # pragma: no cover
        return SearchGroupedFilterExpressions.make_one(
            self.boto3_raw_data["filterExpressions"]
        )

    @cached_property
    def sortExpressions(self):  # pragma: no cover
        return SearchSortExpression.make_many(self.boto3_raw_data["sortExpressions"])

    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchWorkersRequest:
    boto3_raw_data: "type_defs.SearchWorkersRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetIds = field("fleetIds")
    itemOffset = field("itemOffset")

    @cached_property
    def filterExpressions(self):  # pragma: no cover
        return SearchGroupedFilterExpressions.make_one(
            self.boto3_raw_data["filterExpressions"]
        )

    @cached_property
    def sortExpressions(self):  # pragma: no cover
        return SearchSortExpression.make_many(self.boto3_raw_data["sortExpressions"])

    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchWorkersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchWorkersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBudgetRequest:
    boto3_raw_data: "type_defs.CreateBudgetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")

    @cached_property
    def usageTrackingResource(self):  # pragma: no cover
        return UsageTrackingResource.make_one(
            self.boto3_raw_data["usageTrackingResource"]
        )

    displayName = field("displayName")
    approximateDollarLimit = field("approximateDollarLimit")

    @cached_property
    def actions(self):  # pragma: no cover
        return BudgetActionToAdd.make_many(self.boto3_raw_data["actions"])

    schedule = field("schedule")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBudgetRequest:
    boto3_raw_data: "type_defs.UpdateBudgetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    budgetId = field("budgetId")
    clientToken = field("clientToken")
    displayName = field("displayName")
    description = field("description")
    status = field("status")
    approximateDollarLimit = field("approximateDollarLimit")

    @cached_property
    def actionsToAdd(self):  # pragma: no cover
        return BudgetActionToAdd.make_many(self.boto3_raw_data["actionsToAdd"])

    @cached_property
    def actionsToRemove(self):  # pragma: no cover
        return BudgetActionToRemove.make_many(self.boto3_raw_data["actionsToRemove"])

    schedule = field("schedule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBudgetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBudgetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetJobEntityResponse:
    boto3_raw_data: "type_defs.BatchGetJobEntityResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return JobEntity.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def errors(self):  # pragma: no cover
        return GetJobEntityError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetJobEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetJobEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetSummary:
    boto3_raw_data: "type_defs.FleetSummaryTypeDef" = dataclasses.field()

    fleetId = field("fleetId")
    farmId = field("farmId")
    displayName = field("displayName")
    status = field("status")
    workerCount = field("workerCount")
    minWorkerCount = field("minWorkerCount")
    maxWorkerCount = field("maxWorkerCount")

    @cached_property
    def configuration(self):  # pragma: no cover
        return FleetConfigurationOutput.make_one(self.boto3_raw_data["configuration"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    statusMessage = field("statusMessage")
    autoScalingStatus = field("autoScalingStatus")
    targetWorkerCount = field("targetWorkerCount")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFleetResponse:
    boto3_raw_data: "type_defs.GetFleetResponseTypeDef" = dataclasses.field()

    fleetId = field("fleetId")
    farmId = field("farmId")
    displayName = field("displayName")
    description = field("description")
    status = field("status")
    statusMessage = field("statusMessage")
    autoScalingStatus = field("autoScalingStatus")
    targetWorkerCount = field("targetWorkerCount")
    workerCount = field("workerCount")
    minWorkerCount = field("minWorkerCount")
    maxWorkerCount = field("maxWorkerCount")

    @cached_property
    def configuration(self):  # pragma: no cover
        return FleetConfigurationOutput.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def hostConfiguration(self):  # pragma: no cover
        return HostConfiguration.make_one(self.boto3_raw_data["hostConfiguration"])

    @cached_property
    def capabilities(self):  # pragma: no cover
        return FleetCapabilities.make_one(self.boto3_raw_data["capabilities"])

    roleArn = field("roleArn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFleetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkerScheduleResponse:
    boto3_raw_data: "type_defs.UpdateWorkerScheduleResponseTypeDef" = (
        dataclasses.field()
    )

    assignedSessions = field("assignedSessions")
    cancelSessionActions = field("cancelSessionActions")
    desiredWorkerStatus = field("desiredWorkerStatus")
    updateIntervalSeconds = field("updateIntervalSeconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkerScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkerScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsResponse:
    boto3_raw_data: "type_defs.ListFleetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def fleets(self):  # pragma: no cover
        return FleetSummary.make_many(self.boto3_raw_data["fleets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetRequest:
    boto3_raw_data: "type_defs.CreateFleetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    displayName = field("displayName")
    roleArn = field("roleArn")
    maxWorkerCount = field("maxWorkerCount")
    configuration = field("configuration")
    clientToken = field("clientToken")
    description = field("description")
    minWorkerCount = field("minWorkerCount")
    tags = field("tags")

    @cached_property
    def hostConfiguration(self):  # pragma: no cover
        return HostConfiguration.make_one(self.boto3_raw_data["hostConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetRequest:
    boto3_raw_data: "type_defs.UpdateFleetRequestTypeDef" = dataclasses.field()

    farmId = field("farmId")
    fleetId = field("fleetId")
    clientToken = field("clientToken")
    displayName = field("displayName")
    description = field("description")
    roleArn = field("roleArn")
    minWorkerCount = field("minWorkerCount")
    maxWorkerCount = field("maxWorkerCount")
    configuration = field("configuration")

    @cached_property
    def hostConfiguration(self):  # pragma: no cover
        return HostConfiguration.make_one(self.boto3_raw_data["hostConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
