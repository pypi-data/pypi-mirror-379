# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codedeploy import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppSpecContent:
    boto3_raw_data: "type_defs.AppSpecContentTypeDef" = dataclasses.field()

    content = field("content")
    sha256 = field("sha256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppSpecContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppSpecContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationInfo:
    boto3_raw_data: "type_defs.ApplicationInfoTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    applicationName = field("applicationName")
    createTime = field("createTime")
    linkedToGitHub = field("linkedToGitHub")
    gitHubAccountName = field("gitHubAccountName")
    computePlatform = field("computePlatform")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoRollbackConfigurationOutput:
    boto3_raw_data: "type_defs.AutoRollbackConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    events = field("events")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoRollbackConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoRollbackConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoRollbackConfiguration:
    boto3_raw_data: "type_defs.AutoRollbackConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")
    events = field("events")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoRollbackConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoRollbackConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroup:
    boto3_raw_data: "type_defs.AutoScalingGroupTypeDef" = dataclasses.field()

    name = field("name")
    hook = field("hook")
    terminationHook = field("terminationHook")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoScalingGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupTypeDef"]
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
class BatchGetApplicationsInput:
    boto3_raw_data: "type_defs.BatchGetApplicationsInputTypeDef" = dataclasses.field()

    applicationNames = field("applicationNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetApplicationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetApplicationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentGroupsInput:
    boto3_raw_data: "type_defs.BatchGetDeploymentGroupsInputTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")
    deploymentGroupNames = field("deploymentGroupNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentGroupsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentInstancesInput:
    boto3_raw_data: "type_defs.BatchGetDeploymentInstancesInputTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")
    instanceIds = field("instanceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentInstancesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentTargetsInput:
    boto3_raw_data: "type_defs.BatchGetDeploymentTargetsInputTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")
    targetIds = field("targetIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentTargetsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentsInput:
    boto3_raw_data: "type_defs.BatchGetDeploymentsInputTypeDef" = dataclasses.field()

    deploymentIds = field("deploymentIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetOnPremisesInstancesInput:
    boto3_raw_data: "type_defs.BatchGetOnPremisesInstancesInputTypeDef" = (
        dataclasses.field()
    )

    instanceNames = field("instanceNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetOnPremisesInstancesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetOnPremisesInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueInstanceTerminationOption:
    boto3_raw_data: "type_defs.BlueInstanceTerminationOptionTypeDef" = (
        dataclasses.field()
    )

    action = field("action")
    terminationWaitTimeInMinutes = field("terminationWaitTimeInMinutes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BlueInstanceTerminationOptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlueInstanceTerminationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentReadyOption:
    boto3_raw_data: "type_defs.DeploymentReadyOptionTypeDef" = dataclasses.field()

    actionOnTimeout = field("actionOnTimeout")
    waitTimeInMinutes = field("waitTimeInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentReadyOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentReadyOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GreenFleetProvisioningOption:
    boto3_raw_data: "type_defs.GreenFleetProvisioningOptionTypeDef" = (
        dataclasses.field()
    )

    action = field("action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GreenFleetProvisioningOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GreenFleetProvisioningOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinueDeploymentInput:
    boto3_raw_data: "type_defs.ContinueDeploymentInputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    deploymentWaitType = field("deploymentWaitType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContinueDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinueDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MinimumHealthyHosts:
    boto3_raw_data: "type_defs.MinimumHealthyHostsTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MinimumHealthyHostsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MinimumHealthyHostsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentStyle:
    boto3_raw_data: "type_defs.DeploymentStyleTypeDef" = dataclasses.field()

    deploymentType = field("deploymentType")
    deploymentOption = field("deploymentOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentStyleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentStyleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2TagFilter:
    boto3_raw_data: "type_defs.EC2TagFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2TagFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EC2TagFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSService:
    boto3_raw_data: "type_defs.ECSServiceTypeDef" = dataclasses.field()

    serviceName = field("serviceName")
    clusterName = field("clusterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ECSServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ECSServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagFilter:
    boto3_raw_data: "type_defs.TagFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationInput:
    boto3_raw_data: "type_defs.DeleteApplicationInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentConfigInput:
    boto3_raw_data: "type_defs.DeleteDeploymentConfigInputTypeDef" = dataclasses.field()

    deploymentConfigName = field("deploymentConfigName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentGroupInput:
    boto3_raw_data: "type_defs.DeleteDeploymentGroupInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGitHubAccountTokenInput:
    boto3_raw_data: "type_defs.DeleteGitHubAccountTokenInputTypeDef" = (
        dataclasses.field()
    )

    tokenName = field("tokenName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteGitHubAccountTokenInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGitHubAccountTokenInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcesByExternalIdInput:
    boto3_raw_data: "type_defs.DeleteResourcesByExternalIdInputTypeDef" = (
        dataclasses.field()
    )

    externalId = field("externalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResourcesByExternalIdInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcesByExternalIdInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastDeploymentInfo:
    boto3_raw_data: "type_defs.LastDeploymentInfoTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    status = field("status")
    endTime = field("endTime")
    createTime = field("createTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LastDeploymentInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LastDeploymentInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggerConfigOutput:
    boto3_raw_data: "type_defs.TriggerConfigOutputTypeDef" = dataclasses.field()

    triggerName = field("triggerName")
    triggerTargetArn = field("triggerTargetArn")
    triggerEvents = field("triggerEvents")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TriggerConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TriggerConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentOverview:
    boto3_raw_data: "type_defs.DeploymentOverviewTypeDef" = dataclasses.field()

    Pending = field("Pending")
    InProgress = field("InProgress")
    Succeeded = field("Succeeded")
    Failed = field("Failed")
    Skipped = field("Skipped")
    Ready = field("Ready")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentOverviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorInformation:
    boto3_raw_data: "type_defs.ErrorInformationTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedDeployments:
    boto3_raw_data: "type_defs.RelatedDeploymentsTypeDef" = dataclasses.field()

    autoUpdateOutdatedInstancesRootDeploymentId = field(
        "autoUpdateOutdatedInstancesRootDeploymentId"
    )
    autoUpdateOutdatedInstancesDeploymentIds = field(
        "autoUpdateOutdatedInstancesDeploymentIds"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedDeploymentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedDeploymentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackInfo:
    boto3_raw_data: "type_defs.RollbackInfoTypeDef" = dataclasses.field()

    rollbackDeploymentId = field("rollbackDeploymentId")
    rollbackTriggeringDeploymentId = field("rollbackTriggeringDeploymentId")
    rollbackMessage = field("rollbackMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RollbackInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RollbackInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterOnPremisesInstanceInput:
    boto3_raw_data: "type_defs.DeregisterOnPremisesInstanceInputTypeDef" = (
        dataclasses.field()
    )

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterOnPremisesInstanceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterOnPremisesInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Diagnostics:
    boto3_raw_data: "type_defs.DiagnosticsTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    scriptName = field("scriptName")
    message = field("message")
    logTail = field("logTail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiagnosticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiagnosticsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupInfo:
    boto3_raw_data: "type_defs.TargetGroupInfoTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetGroupInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetGroupInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ELBInfo:
    boto3_raw_data: "type_defs.ELBInfoTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ELBInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ELBInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenericRevisionInfo:
    boto3_raw_data: "type_defs.GenericRevisionInfoTypeDef" = dataclasses.field()

    description = field("description")
    deploymentGroups = field("deploymentGroups")
    firstUsedTime = field("firstUsedTime")
    lastUsedTime = field("lastUsedTime")
    registerTime = field("registerTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenericRevisionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenericRevisionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationInput:
    boto3_raw_data: "type_defs.GetApplicationInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentConfigInput:
    boto3_raw_data: "type_defs.GetDeploymentConfigInputTypeDef" = dataclasses.field()

    deploymentConfigName = field("deploymentConfigName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentGroupInput:
    boto3_raw_data: "type_defs.GetDeploymentGroupInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentInput:
    boto3_raw_data: "type_defs.GetDeploymentInputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentInputTypeDef"]
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
class GetDeploymentInstanceInput:
    boto3_raw_data: "type_defs.GetDeploymentInstanceInputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    instanceId = field("instanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentTargetInput:
    boto3_raw_data: "type_defs.GetDeploymentTargetInputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    targetId = field("targetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentTargetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOnPremisesInstanceInput:
    boto3_raw_data: "type_defs.GetOnPremisesInstanceInputTypeDef" = dataclasses.field()

    instanceName = field("instanceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOnPremisesInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOnPremisesInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GitHubLocation:
    boto3_raw_data: "type_defs.GitHubLocationTypeDef" = dataclasses.field()

    repository = field("repository")
    commitId = field("commitId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GitHubLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GitHubLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionInfo:
    boto3_raw_data: "type_defs.LambdaFunctionInfoTypeDef" = dataclasses.field()

    functionName = field("functionName")
    functionAlias = field("functionAlias")
    currentVersion = field("currentVersion")
    targetVersion = field("targetVersion")
    targetVersionWeight = field("targetVersionWeight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionInfoTypeDef"]
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
class ListApplicationRevisionsInput:
    boto3_raw_data: "type_defs.ListApplicationRevisionsInputTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    s3Bucket = field("s3Bucket")
    s3KeyPrefix = field("s3KeyPrefix")
    deployed = field("deployed")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationRevisionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationRevisionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsInput:
    boto3_raw_data: "type_defs.ListApplicationsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentConfigsInput:
    boto3_raw_data: "type_defs.ListDeploymentConfigsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentConfigsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentConfigsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentGroupsInput:
    boto3_raw_data: "type_defs.ListDeploymentGroupsInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentInstancesInput:
    boto3_raw_data: "type_defs.ListDeploymentInstancesInputTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")
    nextToken = field("nextToken")
    instanceStatusFilter = field("instanceStatusFilter")
    instanceTypeFilter = field("instanceTypeFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentTargetsInput:
    boto3_raw_data: "type_defs.ListDeploymentTargetsInputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    nextToken = field("nextToken")
    targetFilters = field("targetFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentTargetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGitHubAccountTokenNamesInput:
    boto3_raw_data: "type_defs.ListGitHubAccountTokenNamesInputTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGitHubAccountTokenNamesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGitHubAccountTokenNamesInputTypeDef"]
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

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")

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
class MinimumHealthyHostsPerZone:
    boto3_raw_data: "type_defs.MinimumHealthyHostsPerZoneTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MinimumHealthyHostsPerZoneTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MinimumHealthyHostsPerZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLifecycleEventHookExecutionStatusInput:
    boto3_raw_data: "type_defs.PutLifecycleEventHookExecutionStatusInputTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")
    lifecycleEventHookExecutionId = field("lifecycleEventHookExecutionId")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutLifecycleEventHookExecutionStatusInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLifecycleEventHookExecutionStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RawString:
    boto3_raw_data: "type_defs.RawStringTypeDef" = dataclasses.field()

    content = field("content")
    sha256 = field("sha256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RawStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RawStringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterOnPremisesInstanceInput:
    boto3_raw_data: "type_defs.RegisterOnPremisesInstanceInputTypeDef" = (
        dataclasses.field()
    )

    instanceName = field("instanceName")
    iamSessionArn = field("iamSessionArn")
    iamUserArn = field("iamUserArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterOnPremisesInstanceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterOnPremisesInstanceInputTypeDef"]
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

    bucket = field("bucket")
    key = field("key")
    bundleType = field("bundleType")
    version = field("version")
    eTag = field("eTag")

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
class SkipWaitTimeForInstanceTerminationInput:
    boto3_raw_data: "type_defs.SkipWaitTimeForInstanceTerminationInputTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SkipWaitTimeForInstanceTerminationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SkipWaitTimeForInstanceTerminationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDeploymentInput:
    boto3_raw_data: "type_defs.StopDeploymentInputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    autoRollbackEnabled = field("autoRollbackEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficRouteOutput:
    boto3_raw_data: "type_defs.TrafficRouteOutputTypeDef" = dataclasses.field()

    listenerArns = field("listenerArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficRoute:
    boto3_raw_data: "type_defs.TrafficRouteTypeDef" = dataclasses.field()

    listenerArns = field("listenerArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrafficRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrafficRouteTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeBasedCanary:
    boto3_raw_data: "type_defs.TimeBasedCanaryTypeDef" = dataclasses.field()

    canaryPercentage = field("canaryPercentage")
    canaryInterval = field("canaryInterval")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeBasedCanaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeBasedCanaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeBasedLinear:
    boto3_raw_data: "type_defs.TimeBasedLinearTypeDef" = dataclasses.field()

    linearPercentage = field("linearPercentage")
    linearInterval = field("linearInterval")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeBasedLinearTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeBasedLinearTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggerConfig:
    boto3_raw_data: "type_defs.TriggerConfigTypeDef" = dataclasses.field()

    triggerName = field("triggerName")
    triggerTargetArn = field("triggerTargetArn")
    triggerEvents = field("triggerEvents")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TriggerConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TriggerConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class UpdateApplicationInput:
    boto3_raw_data: "type_defs.UpdateApplicationInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    newApplicationName = field("newApplicationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToOnPremisesInstancesInput:
    boto3_raw_data: "type_defs.AddTagsToOnPremisesInstancesInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    instanceNames = field("instanceNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddTagsToOnPremisesInstancesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToOnPremisesInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationInput:
    boto3_raw_data: "type_defs.CreateApplicationInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    computePlatform = field("computePlatform")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceInfo:
    boto3_raw_data: "type_defs.InstanceInfoTypeDef" = dataclasses.field()

    instanceName = field("instanceName")
    iamSessionArn = field("iamSessionArn")
    iamUserArn = field("iamUserArn")
    instanceArn = field("instanceArn")
    registerTime = field("registerTime")
    deregisterTime = field("deregisterTime")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromOnPremisesInstancesInput:
    boto3_raw_data: "type_defs.RemoveTagsFromOnPremisesInstancesInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    instanceNames = field("instanceNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveTagsFromOnPremisesInstancesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromOnPremisesInstancesInputTypeDef"]
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

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class AlarmConfigurationOutput:
    boto3_raw_data: "type_defs.AlarmConfigurationOutputTypeDef" = dataclasses.field()

    enabled = field("enabled")
    ignorePollAlarmFailure = field("ignorePollAlarmFailure")

    @cached_property
    def alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["alarms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmConfiguration:
    boto3_raw_data: "type_defs.AlarmConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")
    ignorePollAlarmFailure = field("ignorePollAlarmFailure")

    @cached_property
    def alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["alarms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetApplicationsOutput:
    boto3_raw_data: "type_defs.BatchGetApplicationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def applicationsInfo(self):  # pragma: no cover
        return ApplicationInfo.make_many(self.boto3_raw_data["applicationsInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetApplicationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetApplicationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationOutput:
    boto3_raw_data: "type_defs.CreateApplicationOutputTypeDef" = dataclasses.field()

    applicationId = field("applicationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentConfigOutput:
    boto3_raw_data: "type_defs.CreateDeploymentConfigOutputTypeDef" = (
        dataclasses.field()
    )

    deploymentConfigId = field("deploymentConfigId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentGroupOutput:
    boto3_raw_data: "type_defs.CreateDeploymentGroupOutputTypeDef" = dataclasses.field()

    deploymentGroupId = field("deploymentGroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentOutput:
    boto3_raw_data: "type_defs.CreateDeploymentOutputTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentGroupOutput:
    boto3_raw_data: "type_defs.DeleteDeploymentGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def hooksNotCleanedUp(self):  # pragma: no cover
        return AutoScalingGroup.make_many(self.boto3_raw_data["hooksNotCleanedUp"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGitHubAccountTokenOutput:
    boto3_raw_data: "type_defs.DeleteGitHubAccountTokenOutputTypeDef" = (
        dataclasses.field()
    )

    tokenName = field("tokenName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteGitHubAccountTokenOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGitHubAccountTokenOutputTypeDef"]
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
class GetApplicationOutput:
    boto3_raw_data: "type_defs.GetApplicationOutputTypeDef" = dataclasses.field()

    @cached_property
    def application(self):  # pragma: no cover
        return ApplicationInfo.make_one(self.boto3_raw_data["application"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsOutput:
    boto3_raw_data: "type_defs.ListApplicationsOutputTypeDef" = dataclasses.field()

    applications = field("applications")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentConfigsOutput:
    boto3_raw_data: "type_defs.ListDeploymentConfigsOutputTypeDef" = dataclasses.field()

    deploymentConfigsList = field("deploymentConfigsList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentConfigsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentConfigsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentGroupsOutput:
    boto3_raw_data: "type_defs.ListDeploymentGroupsOutputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroups = field("deploymentGroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentInstancesOutput:
    boto3_raw_data: "type_defs.ListDeploymentInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    instancesList = field("instancesList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeploymentInstancesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentTargetsOutput:
    boto3_raw_data: "type_defs.ListDeploymentTargetsOutputTypeDef" = dataclasses.field()

    targetIds = field("targetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentTargetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentTargetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsOutput:
    boto3_raw_data: "type_defs.ListDeploymentsOutputTypeDef" = dataclasses.field()

    deployments = field("deployments")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGitHubAccountTokenNamesOutput:
    boto3_raw_data: "type_defs.ListGitHubAccountTokenNamesOutputTypeDef" = (
        dataclasses.field()
    )

    tokenNameList = field("tokenNameList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGitHubAccountTokenNamesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGitHubAccountTokenNamesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOnPremisesInstancesOutput:
    boto3_raw_data: "type_defs.ListOnPremisesInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    instanceNames = field("instanceNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOnPremisesInstancesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOnPremisesInstancesOutputTypeDef"]
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

    NextToken = field("NextToken")

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
class PutLifecycleEventHookExecutionStatusOutput:
    boto3_raw_data: "type_defs.PutLifecycleEventHookExecutionStatusOutputTypeDef" = (
        dataclasses.field()
    )

    lifecycleEventHookExecutionId = field("lifecycleEventHookExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutLifecycleEventHookExecutionStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLifecycleEventHookExecutionStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDeploymentOutput:
    boto3_raw_data: "type_defs.StopDeploymentOutputTypeDef" = dataclasses.field()

    status = field("status")
    statusMessage = field("statusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDeploymentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeploymentGroupOutput:
    boto3_raw_data: "type_defs.UpdateDeploymentGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def hooksNotCleanedUp(self):  # pragma: no cover
        return AutoScalingGroup.make_many(self.boto3_raw_data["hooksNotCleanedUp"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeploymentGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeploymentGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueGreenDeploymentConfiguration:
    boto3_raw_data: "type_defs.BlueGreenDeploymentConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def terminateBlueInstancesOnDeploymentSuccess(self):  # pragma: no cover
        return BlueInstanceTerminationOption.make_one(
            self.boto3_raw_data["terminateBlueInstancesOnDeploymentSuccess"]
        )

    @cached_property
    def deploymentReadyOption(self):  # pragma: no cover
        return DeploymentReadyOption.make_one(
            self.boto3_raw_data["deploymentReadyOption"]
        )

    @cached_property
    def greenFleetProvisioningOption(self):  # pragma: no cover
        return GreenFleetProvisioningOption.make_one(
            self.boto3_raw_data["greenFleetProvisioningOption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BlueGreenDeploymentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlueGreenDeploymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2TagSetOutput:
    boto3_raw_data: "type_defs.EC2TagSetOutputTypeDef" = dataclasses.field()

    @cached_property
    def ec2TagSetList(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["ec2TagSetList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2TagSetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EC2TagSetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2TagSet:
    boto3_raw_data: "type_defs.EC2TagSetTypeDef" = dataclasses.field()

    @cached_property
    def ec2TagSetList(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["ec2TagSetList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2TagSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EC2TagSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOnPremisesInstancesInput:
    boto3_raw_data: "type_defs.ListOnPremisesInstancesInputTypeDef" = (
        dataclasses.field()
    )

    registrationStatus = field("registrationStatus")

    @cached_property
    def tagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["tagFilters"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOnPremisesInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOnPremisesInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnPremisesTagSetOutput:
    boto3_raw_data: "type_defs.OnPremisesTagSetOutputTypeDef" = dataclasses.field()

    @cached_property
    def onPremisesTagSetList(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["onPremisesTagSetList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnPremisesTagSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnPremisesTagSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnPremisesTagSet:
    boto3_raw_data: "type_defs.OnPremisesTagSetTypeDef" = dataclasses.field()

    @cached_property
    def onPremisesTagSetList(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["onPremisesTagSetList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnPremisesTagSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnPremisesTagSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleEvent:
    boto3_raw_data: "type_defs.LifecycleEventTypeDef" = dataclasses.field()

    lifecycleEventName = field("lifecycleEventName")

    @cached_property
    def diagnostics(self):  # pragma: no cover
        return Diagnostics.make_one(self.boto3_raw_data["diagnostics"])

    startTime = field("startTime")
    endTime = field("endTime")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecycleEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecycleEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSTaskSet:
    boto3_raw_data: "type_defs.ECSTaskSetTypeDef" = dataclasses.field()

    identifer = field("identifer")
    desiredCount = field("desiredCount")
    pendingCount = field("pendingCount")
    runningCount = field("runningCount")
    status = field("status")
    trafficWeight = field("trafficWeight")

    @cached_property
    def targetGroup(self):  # pragma: no cover
        return TargetGroupInfo.make_one(self.boto3_raw_data["targetGroup"])

    taskSetLabel = field("taskSetLabel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ECSTaskSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ECSTaskSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentInputWait:
    boto3_raw_data: "type_defs.GetDeploymentInputWaitTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationRevisionsInputPaginate:
    boto3_raw_data: "type_defs.ListApplicationRevisionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    s3Bucket = field("s3Bucket")
    s3KeyPrefix = field("s3KeyPrefix")
    deployed = field("deployed")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationRevisionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationRevisionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsInputPaginate:
    boto3_raw_data: "type_defs.ListApplicationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentConfigsInputPaginate:
    boto3_raw_data: "type_defs.ListDeploymentConfigsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeploymentConfigsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentConfigsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListDeploymentGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeploymentGroupsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListDeploymentInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")
    instanceStatusFilter = field("instanceStatusFilter")
    instanceTypeFilter = field("instanceTypeFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeploymentInstancesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentTargetsInputPaginate:
    boto3_raw_data: "type_defs.ListDeploymentTargetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    deploymentId = field("deploymentId")
    targetFilters = field("targetFilters")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeploymentTargetsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentTargetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGitHubAccountTokenNamesInputPaginate:
    boto3_raw_data: "type_defs.ListGitHubAccountTokenNamesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGitHubAccountTokenNamesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGitHubAccountTokenNamesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOnPremisesInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListOnPremisesInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    registrationStatus = field("registrationStatus")

    @cached_property
    def tagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["tagFilters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOnPremisesInstancesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOnPremisesInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalConfig:
    boto3_raw_data: "type_defs.ZonalConfigTypeDef" = dataclasses.field()

    firstZoneMonitorDurationInSeconds = field("firstZoneMonitorDurationInSeconds")
    monitorDurationInSeconds = field("monitorDurationInSeconds")

    @cached_property
    def minimumHealthyHostsPerZone(self):  # pragma: no cover
        return MinimumHealthyHostsPerZone.make_one(
            self.boto3_raw_data["minimumHealthyHostsPerZone"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ZonalConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ZonalConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevisionLocation:
    boto3_raw_data: "type_defs.RevisionLocationTypeDef" = dataclasses.field()

    revisionType = field("revisionType")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def gitHubLocation(self):  # pragma: no cover
        return GitHubLocation.make_one(self.boto3_raw_data["gitHubLocation"])

    @cached_property
    def string(self):  # pragma: no cover
        return RawString.make_one(self.boto3_raw_data["string"])

    @cached_property
    def appSpecContent(self):  # pragma: no cover
        return AppSpecContent.make_one(self.boto3_raw_data["appSpecContent"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevisionLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupPairInfoOutput:
    boto3_raw_data: "type_defs.TargetGroupPairInfoOutputTypeDef" = dataclasses.field()

    @cached_property
    def targetGroups(self):  # pragma: no cover
        return TargetGroupInfo.make_many(self.boto3_raw_data["targetGroups"])

    @cached_property
    def prodTrafficRoute(self):  # pragma: no cover
        return TrafficRouteOutput.make_one(self.boto3_raw_data["prodTrafficRoute"])

    @cached_property
    def testTrafficRoute(self):  # pragma: no cover
        return TrafficRouteOutput.make_one(self.boto3_raw_data["testTrafficRoute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetGroupPairInfoOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupPairInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupPairInfo:
    boto3_raw_data: "type_defs.TargetGroupPairInfoTypeDef" = dataclasses.field()

    @cached_property
    def targetGroups(self):  # pragma: no cover
        return TargetGroupInfo.make_many(self.boto3_raw_data["targetGroups"])

    @cached_property
    def prodTrafficRoute(self):  # pragma: no cover
        return TrafficRoute.make_one(self.boto3_raw_data["prodTrafficRoute"])

    @cached_property
    def testTrafficRoute(self):  # pragma: no cover
        return TrafficRoute.make_one(self.boto3_raw_data["testTrafficRoute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetGroupPairInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupPairInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficRoutingConfig:
    boto3_raw_data: "type_defs.TrafficRoutingConfigTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def timeBasedCanary(self):  # pragma: no cover
        return TimeBasedCanary.make_one(self.boto3_raw_data["timeBasedCanary"])

    @cached_property
    def timeBasedLinear(self):  # pragma: no cover
        return TimeBasedLinear.make_one(self.boto3_raw_data["timeBasedLinear"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficRoutingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficRoutingConfigTypeDef"]
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

    start = field("start")
    end = field("end")

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
class BatchGetOnPremisesInstancesOutput:
    boto3_raw_data: "type_defs.BatchGetOnPremisesInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instanceInfos(self):  # pragma: no cover
        return InstanceInfo.make_many(self.boto3_raw_data["instanceInfos"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetOnPremisesInstancesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetOnPremisesInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOnPremisesInstanceOutput:
    boto3_raw_data: "type_defs.GetOnPremisesInstanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def instanceInfo(self):  # pragma: no cover
        return InstanceInfo.make_one(self.boto3_raw_data["instanceInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOnPremisesInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOnPremisesInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetInstancesOutput:
    boto3_raw_data: "type_defs.TargetInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def tagFilters(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["tagFilters"])

    autoScalingGroups = field("autoScalingGroups")

    @cached_property
    def ec2TagSet(self):  # pragma: no cover
        return EC2TagSetOutput.make_one(self.boto3_raw_data["ec2TagSet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetInstances:
    boto3_raw_data: "type_defs.TargetInstancesTypeDef" = dataclasses.field()

    @cached_property
    def tagFilters(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["tagFilters"])

    autoScalingGroups = field("autoScalingGroups")

    @cached_property
    def ec2TagSet(self):  # pragma: no cover
        return EC2TagSet.make_one(self.boto3_raw_data["ec2TagSet"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetInstancesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetInstancesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationTarget:
    boto3_raw_data: "type_defs.CloudFormationTargetTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    targetId = field("targetId")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def lifecycleEvents(self):  # pragma: no cover
        return LifecycleEvent.make_many(self.boto3_raw_data["lifecycleEvents"])

    status = field("status")
    resourceType = field("resourceType")
    targetVersionWeight = field("targetVersionWeight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceSummary:
    boto3_raw_data: "type_defs.InstanceSummaryTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    instanceId = field("instanceId")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def lifecycleEvents(self):  # pragma: no cover
        return LifecycleEvent.make_many(self.boto3_raw_data["lifecycleEvents"])

    instanceType = field("instanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTarget:
    boto3_raw_data: "type_defs.InstanceTargetTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    targetId = field("targetId")
    targetArn = field("targetArn")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def lifecycleEvents(self):  # pragma: no cover
        return LifecycleEvent.make_many(self.boto3_raw_data["lifecycleEvents"])

    instanceLabel = field("instanceLabel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaTarget:
    boto3_raw_data: "type_defs.LambdaTargetTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    targetId = field("targetId")
    targetArn = field("targetArn")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def lifecycleEvents(self):  # pragma: no cover
        return LifecycleEvent.make_many(self.boto3_raw_data["lifecycleEvents"])

    @cached_property
    def lambdaFunctionInfo(self):  # pragma: no cover
        return LambdaFunctionInfo.make_one(self.boto3_raw_data["lambdaFunctionInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECSTarget:
    boto3_raw_data: "type_defs.ECSTargetTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    targetId = field("targetId")
    targetArn = field("targetArn")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def lifecycleEvents(self):  # pragma: no cover
        return LifecycleEvent.make_many(self.boto3_raw_data["lifecycleEvents"])

    status = field("status")

    @cached_property
    def taskSetsInfo(self):  # pragma: no cover
        return ECSTaskSet.make_many(self.boto3_raw_data["taskSetsInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ECSTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ECSTargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetApplicationRevisionsInput:
    boto3_raw_data: "type_defs.BatchGetApplicationRevisionsInputTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")

    @cached_property
    def revisions(self):  # pragma: no cover
        return RevisionLocation.make_many(self.boto3_raw_data["revisions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetApplicationRevisionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetApplicationRevisionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRevisionInput:
    boto3_raw_data: "type_defs.GetApplicationRevisionInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")

    @cached_property
    def revision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["revision"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRevisionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRevisionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRevisionOutput:
    boto3_raw_data: "type_defs.GetApplicationRevisionOutputTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")

    @cached_property
    def revision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["revision"])

    @cached_property
    def revisionInfo(self):  # pragma: no cover
        return GenericRevisionInfo.make_one(self.boto3_raw_data["revisionInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRevisionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRevisionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationRevisionsOutput:
    boto3_raw_data: "type_defs.ListApplicationRevisionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def revisions(self):  # pragma: no cover
        return RevisionLocation.make_many(self.boto3_raw_data["revisions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationRevisionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationRevisionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterApplicationRevisionInput:
    boto3_raw_data: "type_defs.RegisterApplicationRevisionInputTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")

    @cached_property
    def revision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["revision"])

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterApplicationRevisionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterApplicationRevisionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevisionInfo:
    boto3_raw_data: "type_defs.RevisionInfoTypeDef" = dataclasses.field()

    @cached_property
    def revisionLocation(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["revisionLocation"])

    @cached_property
    def genericRevisionInfo(self):  # pragma: no cover
        return GenericRevisionInfo.make_one(self.boto3_raw_data["genericRevisionInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RevisionInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerInfoOutput:
    boto3_raw_data: "type_defs.LoadBalancerInfoOutputTypeDef" = dataclasses.field()

    @cached_property
    def elbInfoList(self):  # pragma: no cover
        return ELBInfo.make_many(self.boto3_raw_data["elbInfoList"])

    @cached_property
    def targetGroupInfoList(self):  # pragma: no cover
        return TargetGroupInfo.make_many(self.boto3_raw_data["targetGroupInfoList"])

    @cached_property
    def targetGroupPairInfoList(self):  # pragma: no cover
        return TargetGroupPairInfoOutput.make_many(
            self.boto3_raw_data["targetGroupPairInfoList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerInfoOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerInfo:
    boto3_raw_data: "type_defs.LoadBalancerInfoTypeDef" = dataclasses.field()

    @cached_property
    def elbInfoList(self):  # pragma: no cover
        return ELBInfo.make_many(self.boto3_raw_data["elbInfoList"])

    @cached_property
    def targetGroupInfoList(self):  # pragma: no cover
        return TargetGroupInfo.make_many(self.boto3_raw_data["targetGroupInfoList"])

    @cached_property
    def targetGroupPairInfoList(self):  # pragma: no cover
        return TargetGroupPairInfo.make_many(
            self.boto3_raw_data["targetGroupPairInfoList"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentConfigInput:
    boto3_raw_data: "type_defs.CreateDeploymentConfigInputTypeDef" = dataclasses.field()

    deploymentConfigName = field("deploymentConfigName")

    @cached_property
    def minimumHealthyHosts(self):  # pragma: no cover
        return MinimumHealthyHosts.make_one(self.boto3_raw_data["minimumHealthyHosts"])

    @cached_property
    def trafficRoutingConfig(self):  # pragma: no cover
        return TrafficRoutingConfig.make_one(
            self.boto3_raw_data["trafficRoutingConfig"]
        )

    computePlatform = field("computePlatform")

    @cached_property
    def zonalConfig(self):  # pragma: no cover
        return ZonalConfig.make_one(self.boto3_raw_data["zonalConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentConfigInfo:
    boto3_raw_data: "type_defs.DeploymentConfigInfoTypeDef" = dataclasses.field()

    deploymentConfigId = field("deploymentConfigId")
    deploymentConfigName = field("deploymentConfigName")

    @cached_property
    def minimumHealthyHosts(self):  # pragma: no cover
        return MinimumHealthyHosts.make_one(self.boto3_raw_data["minimumHealthyHosts"])

    createTime = field("createTime")
    computePlatform = field("computePlatform")

    @cached_property
    def trafficRoutingConfig(self):  # pragma: no cover
        return TrafficRoutingConfig.make_one(
            self.boto3_raw_data["trafficRoutingConfig"]
        )

    @cached_property
    def zonalConfig(self):  # pragma: no cover
        return ZonalConfig.make_one(self.boto3_raw_data["zonalConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentConfigInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentConfigInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsInputPaginate:
    boto3_raw_data: "type_defs.ListDeploymentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")
    externalId = field("externalId")
    includeOnlyStatuses = field("includeOnlyStatuses")

    @cached_property
    def createTimeRange(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["createTimeRange"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsInput:
    boto3_raw_data: "type_defs.ListDeploymentsInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")
    externalId = field("externalId")
    includeOnlyStatuses = field("includeOnlyStatuses")

    @cached_property
    def createTimeRange(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["createTimeRange"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentInstancesOutput:
    boto3_raw_data: "type_defs.BatchGetDeploymentInstancesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def instancesSummary(self):  # pragma: no cover
        return InstanceSummary.make_many(self.boto3_raw_data["instancesSummary"])

    errorMessage = field("errorMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetDeploymentInstancesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentInstanceOutput:
    boto3_raw_data: "type_defs.GetDeploymentInstanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def instanceSummary(self):  # pragma: no cover
        return InstanceSummary.make_one(self.boto3_raw_data["instanceSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentTarget:
    boto3_raw_data: "type_defs.DeploymentTargetTypeDef" = dataclasses.field()

    deploymentTargetType = field("deploymentTargetType")

    @cached_property
    def instanceTarget(self):  # pragma: no cover
        return InstanceTarget.make_one(self.boto3_raw_data["instanceTarget"])

    @cached_property
    def lambdaTarget(self):  # pragma: no cover
        return LambdaTarget.make_one(self.boto3_raw_data["lambdaTarget"])

    @cached_property
    def ecsTarget(self):  # pragma: no cover
        return ECSTarget.make_one(self.boto3_raw_data["ecsTarget"])

    @cached_property
    def cloudFormationTarget(self):  # pragma: no cover
        return CloudFormationTarget.make_one(
            self.boto3_raw_data["cloudFormationTarget"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetApplicationRevisionsOutput:
    boto3_raw_data: "type_defs.BatchGetApplicationRevisionsOutputTypeDef" = (
        dataclasses.field()
    )

    applicationName = field("applicationName")
    errorMessage = field("errorMessage")

    @cached_property
    def revisions(self):  # pragma: no cover
        return RevisionInfo.make_many(self.boto3_raw_data["revisions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetApplicationRevisionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetApplicationRevisionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentGroupInfo:
    boto3_raw_data: "type_defs.DeploymentGroupInfoTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupId = field("deploymentGroupId")
    deploymentGroupName = field("deploymentGroupName")
    deploymentConfigName = field("deploymentConfigName")

    @cached_property
    def ec2TagFilters(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["ec2TagFilters"])

    @cached_property
    def onPremisesInstanceTagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["onPremisesInstanceTagFilters"])

    @cached_property
    def autoScalingGroups(self):  # pragma: no cover
        return AutoScalingGroup.make_many(self.boto3_raw_data["autoScalingGroups"])

    serviceRoleArn = field("serviceRoleArn")

    @cached_property
    def targetRevision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["targetRevision"])

    @cached_property
    def triggerConfigurations(self):  # pragma: no cover
        return TriggerConfigOutput.make_many(
            self.boto3_raw_data["triggerConfigurations"]
        )

    @cached_property
    def alarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["alarmConfiguration"]
        )

    @cached_property
    def autoRollbackConfiguration(self):  # pragma: no cover
        return AutoRollbackConfigurationOutput.make_one(
            self.boto3_raw_data["autoRollbackConfiguration"]
        )

    @cached_property
    def deploymentStyle(self):  # pragma: no cover
        return DeploymentStyle.make_one(self.boto3_raw_data["deploymentStyle"])

    outdatedInstancesStrategy = field("outdatedInstancesStrategy")

    @cached_property
    def blueGreenDeploymentConfiguration(self):  # pragma: no cover
        return BlueGreenDeploymentConfiguration.make_one(
            self.boto3_raw_data["blueGreenDeploymentConfiguration"]
        )

    @cached_property
    def loadBalancerInfo(self):  # pragma: no cover
        return LoadBalancerInfoOutput.make_one(self.boto3_raw_data["loadBalancerInfo"])

    @cached_property
    def lastSuccessfulDeployment(self):  # pragma: no cover
        return LastDeploymentInfo.make_one(
            self.boto3_raw_data["lastSuccessfulDeployment"]
        )

    @cached_property
    def lastAttemptedDeployment(self):  # pragma: no cover
        return LastDeploymentInfo.make_one(
            self.boto3_raw_data["lastAttemptedDeployment"]
        )

    @cached_property
    def ec2TagSet(self):  # pragma: no cover
        return EC2TagSetOutput.make_one(self.boto3_raw_data["ec2TagSet"])

    @cached_property
    def onPremisesTagSet(self):  # pragma: no cover
        return OnPremisesTagSetOutput.make_one(self.boto3_raw_data["onPremisesTagSet"])

    computePlatform = field("computePlatform")

    @cached_property
    def ecsServices(self):  # pragma: no cover
        return ECSService.make_many(self.boto3_raw_data["ecsServices"])

    terminationHookEnabled = field("terminationHookEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentGroupInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentGroupInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentInfo:
    boto3_raw_data: "type_defs.DeploymentInfoTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")
    deploymentConfigName = field("deploymentConfigName")
    deploymentId = field("deploymentId")

    @cached_property
    def previousRevision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["previousRevision"])

    @cached_property
    def revision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["revision"])

    status = field("status")

    @cached_property
    def errorInformation(self):  # pragma: no cover
        return ErrorInformation.make_one(self.boto3_raw_data["errorInformation"])

    createTime = field("createTime")
    startTime = field("startTime")
    completeTime = field("completeTime")

    @cached_property
    def deploymentOverview(self):  # pragma: no cover
        return DeploymentOverview.make_one(self.boto3_raw_data["deploymentOverview"])

    description = field("description")
    creator = field("creator")
    ignoreApplicationStopFailures = field("ignoreApplicationStopFailures")

    @cached_property
    def autoRollbackConfiguration(self):  # pragma: no cover
        return AutoRollbackConfigurationOutput.make_one(
            self.boto3_raw_data["autoRollbackConfiguration"]
        )

    updateOutdatedInstancesOnly = field("updateOutdatedInstancesOnly")

    @cached_property
    def rollbackInfo(self):  # pragma: no cover
        return RollbackInfo.make_one(self.boto3_raw_data["rollbackInfo"])

    @cached_property
    def deploymentStyle(self):  # pragma: no cover
        return DeploymentStyle.make_one(self.boto3_raw_data["deploymentStyle"])

    @cached_property
    def targetInstances(self):  # pragma: no cover
        return TargetInstancesOutput.make_one(self.boto3_raw_data["targetInstances"])

    instanceTerminationWaitTimeStarted = field("instanceTerminationWaitTimeStarted")

    @cached_property
    def blueGreenDeploymentConfiguration(self):  # pragma: no cover
        return BlueGreenDeploymentConfiguration.make_one(
            self.boto3_raw_data["blueGreenDeploymentConfiguration"]
        )

    @cached_property
    def loadBalancerInfo(self):  # pragma: no cover
        return LoadBalancerInfoOutput.make_one(self.boto3_raw_data["loadBalancerInfo"])

    additionalDeploymentStatusInfo = field("additionalDeploymentStatusInfo")
    fileExistsBehavior = field("fileExistsBehavior")
    deploymentStatusMessages = field("deploymentStatusMessages")
    computePlatform = field("computePlatform")
    externalId = field("externalId")

    @cached_property
    def relatedDeployments(self):  # pragma: no cover
        return RelatedDeployments.make_one(self.boto3_raw_data["relatedDeployments"])

    @cached_property
    def overrideAlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["overrideAlarmConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentConfigOutput:
    boto3_raw_data: "type_defs.GetDeploymentConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def deploymentConfigInfo(self):  # pragma: no cover
        return DeploymentConfigInfo.make_one(
            self.boto3_raw_data["deploymentConfigInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentInput:
    boto3_raw_data: "type_defs.CreateDeploymentInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")

    @cached_property
    def revision(self):  # pragma: no cover
        return RevisionLocation.make_one(self.boto3_raw_data["revision"])

    deploymentConfigName = field("deploymentConfigName")
    description = field("description")
    ignoreApplicationStopFailures = field("ignoreApplicationStopFailures")
    targetInstances = field("targetInstances")
    autoRollbackConfiguration = field("autoRollbackConfiguration")
    updateOutdatedInstancesOnly = field("updateOutdatedInstancesOnly")
    fileExistsBehavior = field("fileExistsBehavior")
    overrideAlarmConfiguration = field("overrideAlarmConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentTargetsOutput:
    boto3_raw_data: "type_defs.BatchGetDeploymentTargetsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deploymentTargets(self):  # pragma: no cover
        return DeploymentTarget.make_many(self.boto3_raw_data["deploymentTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentTargetsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentTargetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentTargetOutput:
    boto3_raw_data: "type_defs.GetDeploymentTargetOutputTypeDef" = dataclasses.field()

    @cached_property
    def deploymentTarget(self):  # pragma: no cover
        return DeploymentTarget.make_one(self.boto3_raw_data["deploymentTarget"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentTargetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentGroupsOutput:
    boto3_raw_data: "type_defs.BatchGetDeploymentGroupsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deploymentGroupsInfo(self):  # pragma: no cover
        return DeploymentGroupInfo.make_many(
            self.boto3_raw_data["deploymentGroupsInfo"]
        )

    errorMessage = field("errorMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentGroupsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentGroupOutput:
    boto3_raw_data: "type_defs.GetDeploymentGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def deploymentGroupInfo(self):  # pragma: no cover
        return DeploymentGroupInfo.make_one(self.boto3_raw_data["deploymentGroupInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetDeploymentsOutput:
    boto3_raw_data: "type_defs.BatchGetDeploymentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def deploymentsInfo(self):  # pragma: no cover
        return DeploymentInfo.make_many(self.boto3_raw_data["deploymentsInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetDeploymentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetDeploymentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentOutput:
    boto3_raw_data: "type_defs.GetDeploymentOutputTypeDef" = dataclasses.field()

    @cached_property
    def deploymentInfo(self):  # pragma: no cover
        return DeploymentInfo.make_one(self.boto3_raw_data["deploymentInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentGroupInput:
    boto3_raw_data: "type_defs.CreateDeploymentGroupInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    deploymentGroupName = field("deploymentGroupName")
    serviceRoleArn = field("serviceRoleArn")
    deploymentConfigName = field("deploymentConfigName")

    @cached_property
    def ec2TagFilters(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["ec2TagFilters"])

    @cached_property
    def onPremisesInstanceTagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["onPremisesInstanceTagFilters"])

    autoScalingGroups = field("autoScalingGroups")
    triggerConfigurations = field("triggerConfigurations")
    alarmConfiguration = field("alarmConfiguration")
    autoRollbackConfiguration = field("autoRollbackConfiguration")
    outdatedInstancesStrategy = field("outdatedInstancesStrategy")

    @cached_property
    def deploymentStyle(self):  # pragma: no cover
        return DeploymentStyle.make_one(self.boto3_raw_data["deploymentStyle"])

    @cached_property
    def blueGreenDeploymentConfiguration(self):  # pragma: no cover
        return BlueGreenDeploymentConfiguration.make_one(
            self.boto3_raw_data["blueGreenDeploymentConfiguration"]
        )

    loadBalancerInfo = field("loadBalancerInfo")
    ec2TagSet = field("ec2TagSet")

    @cached_property
    def ecsServices(self):  # pragma: no cover
        return ECSService.make_many(self.boto3_raw_data["ecsServices"])

    onPremisesTagSet = field("onPremisesTagSet")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    terminationHookEnabled = field("terminationHookEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeploymentGroupInput:
    boto3_raw_data: "type_defs.UpdateDeploymentGroupInputTypeDef" = dataclasses.field()

    applicationName = field("applicationName")
    currentDeploymentGroupName = field("currentDeploymentGroupName")
    newDeploymentGroupName = field("newDeploymentGroupName")
    deploymentConfigName = field("deploymentConfigName")

    @cached_property
    def ec2TagFilters(self):  # pragma: no cover
        return EC2TagFilter.make_many(self.boto3_raw_data["ec2TagFilters"])

    @cached_property
    def onPremisesInstanceTagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["onPremisesInstanceTagFilters"])

    autoScalingGroups = field("autoScalingGroups")
    serviceRoleArn = field("serviceRoleArn")
    triggerConfigurations = field("triggerConfigurations")
    alarmConfiguration = field("alarmConfiguration")
    autoRollbackConfiguration = field("autoRollbackConfiguration")
    outdatedInstancesStrategy = field("outdatedInstancesStrategy")

    @cached_property
    def deploymentStyle(self):  # pragma: no cover
        return DeploymentStyle.make_one(self.boto3_raw_data["deploymentStyle"])

    @cached_property
    def blueGreenDeploymentConfiguration(self):  # pragma: no cover
        return BlueGreenDeploymentConfiguration.make_one(
            self.boto3_raw_data["blueGreenDeploymentConfiguration"]
        )

    loadBalancerInfo = field("loadBalancerInfo")
    ec2TagSet = field("ec2TagSet")

    @cached_property
    def ecsServices(self):  # pragma: no cover
        return ECSService.make_many(self.boto3_raw_data["ecsServices"])

    onPremisesTagSet = field("onPremisesTagSet")
    terminationHookEnabled = field("terminationHookEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeploymentGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeploymentGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
