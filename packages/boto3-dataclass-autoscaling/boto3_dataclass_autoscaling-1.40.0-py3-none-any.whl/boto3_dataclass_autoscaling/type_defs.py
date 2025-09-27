# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_autoscaling import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceleratorCountRequest:
    boto3_raw_data: "type_defs.AcceleratorCountRequestTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceleratorCountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorCountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceleratorTotalMemoryMiBRequest:
    boto3_raw_data: "type_defs.AcceleratorTotalMemoryMiBRequestTypeDef" = (
        dataclasses.field()
    )

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceleratorTotalMemoryMiBRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceleratorTotalMemoryMiBRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Activity:
    boto3_raw_data: "type_defs.ActivityTypeDef" = dataclasses.field()

    ActivityId = field("ActivityId")
    AutoScalingGroupName = field("AutoScalingGroupName")
    Cause = field("Cause")
    StartTime = field("StartTime")
    StatusCode = field("StatusCode")
    Description = field("Description")
    EndTime = field("EndTime")
    StatusMessage = field("StatusMessage")
    Progress = field("Progress")
    Details = field("Details")
    AutoScalingGroupState = field("AutoScalingGroupState")
    AutoScalingGroupARN = field("AutoScalingGroupARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityTypeDef"]]
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
class AdjustmentType:
    boto3_raw_data: "type_defs.AdjustmentTypeTypeDef" = dataclasses.field()

    AdjustmentType = field("AdjustmentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdjustmentTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdjustmentTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmSpecificationOutput:
    boto3_raw_data: "type_defs.AlarmSpecificationOutputTypeDef" = dataclasses.field()

    Alarms = field("Alarms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlarmSpecification:
    boto3_raw_data: "type_defs.AlarmSpecificationTypeDef" = dataclasses.field()

    Alarms = field("Alarms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    AlarmName = field("AlarmName")
    AlarmARN = field("AlarmARN")

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
class AttachInstancesQuery:
    boto3_raw_data: "type_defs.AttachInstancesQueryTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachInstancesQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachInstancesQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachLoadBalancerTargetGroupsType:
    boto3_raw_data: "type_defs.AttachLoadBalancerTargetGroupsTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    TargetGroupARNs = field("TargetGroupARNs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachLoadBalancerTargetGroupsTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachLoadBalancerTargetGroupsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachLoadBalancersType:
    boto3_raw_data: "type_defs.AttachLoadBalancersTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    LoadBalancerNames = field("LoadBalancerNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachLoadBalancersTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachLoadBalancersTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficSourceIdentifier:
    boto3_raw_data: "type_defs.TrafficSourceIdentifierTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficSourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficSourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
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
class AvailabilityZoneDistribution:
    boto3_raw_data: "type_defs.AvailabilityZoneDistributionTypeDef" = (
        dataclasses.field()
    )

    CapacityDistributionStrategy = field("CapacityDistributionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneDistributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneDistributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZoneImpairmentPolicy:
    boto3_raw_data: "type_defs.AvailabilityZoneImpairmentPolicyTypeDef" = (
        dataclasses.field()
    )

    ZonalShiftEnabled = field("ZonalShiftEnabled")
    ImpairedZoneHealthCheckBehavior = field("ImpairedZoneHealthCheckBehavior")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AvailabilityZoneImpairmentPolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneImpairmentPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnabledMetric:
    boto3_raw_data: "type_defs.EnabledMetricTypeDef" = dataclasses.field()

    Metric = field("Metric")
    Granularity = field("Granularity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnabledMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnabledMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMaintenancePolicy:
    boto3_raw_data: "type_defs.InstanceMaintenancePolicyTypeDef" = dataclasses.field()

    MinHealthyPercentage = field("MinHealthyPercentage")
    MaxHealthyPercentage = field("MaxHealthyPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceMaintenancePolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMaintenancePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecification:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationTypeDef" = dataclasses.field()

    LaunchTemplateId = field("LaunchTemplateId")
    LaunchTemplateName = field("LaunchTemplateName")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuspendedProcess:
    boto3_raw_data: "type_defs.SuspendedProcessTypeDef" = dataclasses.field()

    ProcessName = field("ProcessName")
    SuspensionReason = field("SuspensionReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuspendedProcessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuspendedProcessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagDescription:
    boto3_raw_data: "type_defs.TagDescriptionTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    Key = field("Key")
    Value = field("Value")
    PropagateAtLaunch = field("PropagateAtLaunch")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagDescriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaselineEbsBandwidthMbpsRequest:
    boto3_raw_data: "type_defs.BaselineEbsBandwidthMbpsRequestTypeDef" = (
        dataclasses.field()
    )

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BaselineEbsBandwidthMbpsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaselineEbsBandwidthMbpsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedScheduledUpdateGroupActionRequest:
    boto3_raw_data: "type_defs.FailedScheduledUpdateGroupActionRequestTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailedScheduledUpdateGroupActionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedScheduledUpdateGroupActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteScheduledActionType:
    boto3_raw_data: "type_defs.BatchDeleteScheduledActionTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScheduledActionNames = field("ScheduledActionNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteScheduledActionTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteScheduledActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ebs:
    boto3_raw_data: "type_defs.EbsTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    VolumeSize = field("VolumeSize")
    VolumeType = field("VolumeType")
    DeleteOnTermination = field("DeleteOnTermination")
    Iops = field("Iops")
    Encrypted = field("Encrypted")
    Throughput = field("Throughput")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EbsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelInstanceRefreshType:
    boto3_raw_data: "type_defs.CancelInstanceRefreshTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    WaitForTransitioningInstances = field("WaitForTransitioningInstances")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelInstanceRefreshTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelInstanceRefreshTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityForecast:
    boto3_raw_data: "type_defs.CapacityForecastTypeDef" = dataclasses.field()

    Timestamps = field("Timestamps")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityForecastTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityForecastTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationTargetOutput:
    boto3_raw_data: "type_defs.CapacityReservationTargetOutputTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationIds = field("CapacityReservationIds")
    CapacityReservationResourceGroupArns = field("CapacityReservationResourceGroupArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CapacityReservationTargetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationTarget:
    boto3_raw_data: "type_defs.CapacityReservationTargetTypeDef" = dataclasses.field()

    CapacityReservationIds = field("CapacityReservationIds")
    CapacityReservationResourceGroupArns = field("CapacityReservationResourceGroupArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityReservationTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteLifecycleActionType:
    boto3_raw_data: "type_defs.CompleteLifecycleActionTypeTypeDef" = dataclasses.field()

    LifecycleHookName = field("LifecycleHookName")
    AutoScalingGroupName = field("AutoScalingGroupName")
    LifecycleActionResult = field("LifecycleActionResult")
    LifecycleActionToken = field("LifecycleActionToken")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteLifecycleActionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteLifecycleActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceFactorReferenceRequest:
    boto3_raw_data: "type_defs.PerformanceFactorReferenceRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceFamily = field("InstanceFamily")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PerformanceFactorReferenceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceFactorReferenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleHookSpecification:
    boto3_raw_data: "type_defs.LifecycleHookSpecificationTypeDef" = dataclasses.field()

    LifecycleHookName = field("LifecycleHookName")
    LifecycleTransition = field("LifecycleTransition")
    NotificationMetadata = field("NotificationMetadata")
    HeartbeatTimeout = field("HeartbeatTimeout")
    DefaultResult = field("DefaultResult")
    NotificationTargetARN = field("NotificationTargetARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleHookSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleHookSpecificationTypeDef"]
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
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    Value = field("Value")
    PropagateAtLaunch = field("PropagateAtLaunch")

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
class InstanceMetadataOptions:
    boto3_raw_data: "type_defs.InstanceMetadataOptionsTypeDef" = dataclasses.field()

    HttpTokens = field("HttpTokens")
    HttpPutResponseHopLimit = field("HttpPutResponseHopLimit")
    HttpEndpoint = field("HttpEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceMetadataOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMetadataOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMonitoring:
    boto3_raw_data: "type_defs.InstanceMonitoringTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceMonitoringTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMonitoringTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDimension:
    boto3_raw_data: "type_defs.MetricDimensionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutoScalingGroupType:
    boto3_raw_data: "type_defs.DeleteAutoScalingGroupTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ForceDelete = field("ForceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAutoScalingGroupTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutoScalingGroupTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecycleHookType:
    boto3_raw_data: "type_defs.DeleteLifecycleHookTypeTypeDef" = dataclasses.field()

    LifecycleHookName = field("LifecycleHookName")
    AutoScalingGroupName = field("AutoScalingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLifecycleHookTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecycleHookTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNotificationConfigurationType:
    boto3_raw_data: "type_defs.DeleteNotificationConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    TopicARN = field("TopicARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteNotificationConfigurationTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNotificationConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyType:
    boto3_raw_data: "type_defs.DeletePolicyTypeTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    AutoScalingGroupName = field("AutoScalingGroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduledActionType:
    boto3_raw_data: "type_defs.DeleteScheduledActionTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScheduledActionName = field("ScheduledActionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduledActionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWarmPoolType:
    boto3_raw_data: "type_defs.DeleteWarmPoolTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ForceDelete = field("ForceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWarmPoolTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWarmPoolTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoScalingInstancesType:
    boto3_raw_data: "type_defs.DescribeAutoScalingInstancesTypeTypeDef" = (
        dataclasses.field()
    )

    InstanceIds = field("InstanceIds")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAutoScalingInstancesTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoScalingInstancesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceRefreshesType:
    boto3_raw_data: "type_defs.DescribeInstanceRefreshesTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    InstanceRefreshIds = field("InstanceRefreshIds")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstanceRefreshesTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceRefreshesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleHook:
    boto3_raw_data: "type_defs.LifecycleHookTypeDef" = dataclasses.field()

    LifecycleHookName = field("LifecycleHookName")
    AutoScalingGroupName = field("AutoScalingGroupName")
    LifecycleTransition = field("LifecycleTransition")
    NotificationTargetARN = field("NotificationTargetARN")
    RoleARN = field("RoleARN")
    NotificationMetadata = field("NotificationMetadata")
    HeartbeatTimeout = field("HeartbeatTimeout")
    GlobalTimeout = field("GlobalTimeout")
    DefaultResult = field("DefaultResult")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecycleHookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecycleHookTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLifecycleHooksType:
    boto3_raw_data: "type_defs.DescribeLifecycleHooksTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    LifecycleHookNames = field("LifecycleHookNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLifecycleHooksTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLifecycleHooksTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerTargetGroupsRequest:
    boto3_raw_data: "type_defs.DescribeLoadBalancerTargetGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerTargetGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerTargetGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerTargetGroupState:
    boto3_raw_data: "type_defs.LoadBalancerTargetGroupStateTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerTargetGroupARN = field("LoadBalancerTargetGroupARN")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTargetGroupStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerTargetGroupStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersRequest:
    boto3_raw_data: "type_defs.DescribeLoadBalancersRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLoadBalancersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerState:
    boto3_raw_data: "type_defs.LoadBalancerStateTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricCollectionType:
    boto3_raw_data: "type_defs.MetricCollectionTypeTypeDef" = dataclasses.field()

    Metric = field("Metric")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricCollectionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricCollectionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricGranularityType:
    boto3_raw_data: "type_defs.MetricGranularityTypeTypeDef" = dataclasses.field()

    Granularity = field("Granularity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricGranularityTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricGranularityTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    TopicARN = field("TopicARN")
    NotificationType = field("NotificationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationConfigurationsType:
    boto3_raw_data: "type_defs.DescribeNotificationConfigurationsTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupNames = field("AutoScalingGroupNames")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationConfigurationsTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationConfigurationsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePoliciesType:
    boto3_raw_data: "type_defs.DescribePoliciesTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    PolicyNames = field("PolicyNames")
    PolicyTypes = field("PolicyTypes")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePoliciesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePoliciesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingActivitiesType:
    boto3_raw_data: "type_defs.DescribeScalingActivitiesTypeTypeDef" = (
        dataclasses.field()
    )

    ActivityIds = field("ActivityIds")
    AutoScalingGroupName = field("AutoScalingGroupName")
    IncludeDeletedGroups = field("IncludeDeletedGroups")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalingActivitiesTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingActivitiesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrafficSourcesRequest:
    boto3_raw_data: "type_defs.DescribeTrafficSourcesRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    TrafficSourceType = field("TrafficSourceType")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTrafficSourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrafficSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficSourceState:
    boto3_raw_data: "type_defs.TrafficSourceStateTypeDef" = dataclasses.field()

    TrafficSource = field("TrafficSource")
    State = field("State")
    Identifier = field("Identifier")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficSourceStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficSourceStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWarmPoolType:
    boto3_raw_data: "type_defs.DescribeWarmPoolTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWarmPoolTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWarmPoolTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachInstancesQuery:
    boto3_raw_data: "type_defs.DetachInstancesQueryTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ShouldDecrementDesiredCapacity = field("ShouldDecrementDesiredCapacity")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachInstancesQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachInstancesQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachLoadBalancerTargetGroupsType:
    boto3_raw_data: "type_defs.DetachLoadBalancerTargetGroupsTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    TargetGroupARNs = field("TargetGroupARNs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachLoadBalancerTargetGroupsTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachLoadBalancerTargetGroupsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachLoadBalancersType:
    boto3_raw_data: "type_defs.DetachLoadBalancersTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    LoadBalancerNames = field("LoadBalancerNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachLoadBalancersTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachLoadBalancersTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableMetricsCollectionQuery:
    boto3_raw_data: "type_defs.DisableMetricsCollectionQueryTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableMetricsCollectionQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableMetricsCollectionQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableMetricsCollectionQuery:
    boto3_raw_data: "type_defs.EnableMetricsCollectionQueryTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    Granularity = field("Granularity")
    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableMetricsCollectionQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableMetricsCollectionQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnterStandbyQuery:
    boto3_raw_data: "type_defs.EnterStandbyQueryTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ShouldDecrementDesiredCapacity = field("ShouldDecrementDesiredCapacity")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnterStandbyQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnterStandbyQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutePolicyType:
    boto3_raw_data: "type_defs.ExecutePolicyTypeTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    AutoScalingGroupName = field("AutoScalingGroupName")
    HonorCooldown = field("HonorCooldown")
    MetricValue = field("MetricValue")
    BreachThreshold = field("BreachThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutePolicyTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutePolicyTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExitStandbyQuery:
    boto3_raw_data: "type_defs.ExitStandbyQueryTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExitStandbyQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExitStandbyQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRefreshLivePoolProgress:
    boto3_raw_data: "type_defs.InstanceRefreshLivePoolProgressTypeDef" = (
        dataclasses.field()
    )

    PercentageComplete = field("PercentageComplete")
    InstancesToUpdate = field("InstancesToUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceRefreshLivePoolProgressTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRefreshLivePoolProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRefreshWarmPoolProgress:
    boto3_raw_data: "type_defs.InstanceRefreshWarmPoolProgressTypeDef" = (
        dataclasses.field()
    )

    PercentageComplete = field("PercentageComplete")
    InstancesToUpdate = field("InstancesToUpdate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceRefreshWarmPoolProgressTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRefreshWarmPoolProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryGiBPerVCpuRequest:
    boto3_raw_data: "type_defs.MemoryGiBPerVCpuRequestTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryGiBPerVCpuRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryGiBPerVCpuRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryMiBRequest:
    boto3_raw_data: "type_defs.MemoryMiBRequestTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemoryMiBRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryMiBRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkBandwidthGbpsRequest:
    boto3_raw_data: "type_defs.NetworkBandwidthGbpsRequestTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkBandwidthGbpsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkBandwidthGbpsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterfaceCountRequest:
    boto3_raw_data: "type_defs.NetworkInterfaceCountRequestTypeDef" = (
        dataclasses.field()
    )

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceCountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceCountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TotalLocalStorageGBRequest:
    boto3_raw_data: "type_defs.TotalLocalStorageGBRequestTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TotalLocalStorageGBRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TotalLocalStorageGBRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VCpuCountRequest:
    boto3_raw_data: "type_defs.VCpuCountRequestTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VCpuCountRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VCpuCountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceReusePolicy:
    boto3_raw_data: "type_defs.InstanceReusePolicyTypeDef" = dataclasses.field()

    ReuseOnScaleIn = field("ReuseOnScaleIn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceReusePolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceReusePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancesDistribution:
    boto3_raw_data: "type_defs.InstancesDistributionTypeDef" = dataclasses.field()

    OnDemandAllocationStrategy = field("OnDemandAllocationStrategy")
    OnDemandBaseCapacity = field("OnDemandBaseCapacity")
    OnDemandPercentageAboveBaseCapacity = field("OnDemandPercentageAboveBaseCapacity")
    SpotAllocationStrategy = field("SpotAllocationStrategy")
    SpotInstancePools = field("SpotInstancePools")
    SpotMaxPrice = field("SpotMaxPrice")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancesDistributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancesDistributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationNameType:
    boto3_raw_data: "type_defs.LaunchConfigurationNameTypeTypeDef" = dataclasses.field()

    LaunchConfigurationName = field("LaunchConfigurationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationNameTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationNameTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationNamesType:
    boto3_raw_data: "type_defs.LaunchConfigurationNamesTypeTypeDef" = (
        dataclasses.field()
    )

    LaunchConfigurationNames = field("LaunchConfigurationNames")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationNamesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationNamesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedMetricSpecification:
    boto3_raw_data: "type_defs.PredefinedMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredefinedMetricSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPredefinedLoadMetric:
    boto3_raw_data: "type_defs.PredictiveScalingPredefinedLoadMetricTypeDef" = (
        dataclasses.field()
    )

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPredefinedLoadMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingPredefinedLoadMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPredefinedMetricPair:
    boto3_raw_data: "type_defs.PredictiveScalingPredefinedMetricPairTypeDef" = (
        dataclasses.field()
    )

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPredefinedMetricPairTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingPredefinedMetricPairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingPredefinedScalingMetric:
    boto3_raw_data: "type_defs.PredictiveScalingPredefinedScalingMetricTypeDef" = (
        dataclasses.field()
    )

    PredefinedMetricType = field("PredefinedMetricType")
    ResourceLabel = field("ResourceLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingPredefinedScalingMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingPredefinedScalingMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessType:
    boto3_raw_data: "type_defs.ProcessTypeTypeDef" = dataclasses.field()

    ProcessName = field("ProcessName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLifecycleHookType:
    boto3_raw_data: "type_defs.PutLifecycleHookTypeTypeDef" = dataclasses.field()

    LifecycleHookName = field("LifecycleHookName")
    AutoScalingGroupName = field("AutoScalingGroupName")
    LifecycleTransition = field("LifecycleTransition")
    RoleARN = field("RoleARN")
    NotificationTargetARN = field("NotificationTargetARN")
    NotificationMetadata = field("NotificationMetadata")
    HeartbeatTimeout = field("HeartbeatTimeout")
    DefaultResult = field("DefaultResult")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLifecycleHookTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLifecycleHookTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutNotificationConfigurationType:
    boto3_raw_data: "type_defs.PutNotificationConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    TopicARN = field("TopicARN")
    NotificationTypes = field("NotificationTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutNotificationConfigurationTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutNotificationConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepAdjustment:
    boto3_raw_data: "type_defs.StepAdjustmentTypeDef" = dataclasses.field()

    ScalingAdjustment = field("ScalingAdjustment")
    MetricIntervalLowerBound = field("MetricIntervalLowerBound")
    MetricIntervalUpperBound = field("MetricIntervalUpperBound")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepAdjustmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepAdjustmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordLifecycleActionHeartbeatType:
    boto3_raw_data: "type_defs.RecordLifecycleActionHeartbeatTypeTypeDef" = (
        dataclasses.field()
    )

    LifecycleHookName = field("LifecycleHookName")
    AutoScalingGroupName = field("AutoScalingGroupName")
    LifecycleActionToken = field("LifecycleActionToken")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecordLifecycleActionHeartbeatTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordLifecycleActionHeartbeatTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackInstanceRefreshType:
    boto3_raw_data: "type_defs.RollbackInstanceRefreshTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackInstanceRefreshTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackInstanceRefreshTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingProcessQueryRequest:
    boto3_raw_data: "type_defs.ScalingProcessQueryRequestTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScalingProcesses = field("ScalingProcesses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingProcessQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingProcessQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingProcessQuery:
    boto3_raw_data: "type_defs.ScalingProcessQueryTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScalingProcesses = field("ScalingProcesses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingProcessQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingProcessQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledUpdateGroupAction:
    boto3_raw_data: "type_defs.ScheduledUpdateGroupActionTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScheduledActionName = field("ScheduledActionName")
    ScheduledActionARN = field("ScheduledActionARN")
    Time = field("Time")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Recurrence = field("Recurrence")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    DesiredCapacity = field("DesiredCapacity")
    TimeZone = field("TimeZone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledUpdateGroupActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledUpdateGroupActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDesiredCapacityType:
    boto3_raw_data: "type_defs.SetDesiredCapacityTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    DesiredCapacity = field("DesiredCapacity")
    HonorCooldown = field("HonorCooldown")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDesiredCapacityTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDesiredCapacityTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetInstanceHealthQuery:
    boto3_raw_data: "type_defs.SetInstanceHealthQueryTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    HealthStatus = field("HealthStatus")
    ShouldRespectGracePeriod = field("ShouldRespectGracePeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetInstanceHealthQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetInstanceHealthQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetInstanceProtectionQuery:
    boto3_raw_data: "type_defs.SetInstanceProtectionQueryTypeDef" = dataclasses.field()

    InstanceIds = field("InstanceIds")
    AutoScalingGroupName = field("AutoScalingGroupName")
    ProtectedFromScaleIn = field("ProtectedFromScaleIn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetInstanceProtectionQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetInstanceProtectionQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateInstanceInAutoScalingGroupType:
    boto3_raw_data: "type_defs.TerminateInstanceInAutoScalingGroupTypeTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ShouldDecrementDesiredCapacity = field("ShouldDecrementDesiredCapacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TerminateInstanceInAutoScalingGroupTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateInstanceInAutoScalingGroupTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivitiesType:
    boto3_raw_data: "type_defs.ActivitiesTypeTypeDef" = dataclasses.field()

    @cached_property
    def Activities(self):  # pragma: no cover
        return Activity.make_many(self.boto3_raw_data["Activities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivitiesTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivitiesTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityType:
    boto3_raw_data: "type_defs.ActivityTypeTypeDef" = dataclasses.field()

    @cached_property
    def Activity(self):  # pragma: no cover
        return Activity.make_one(self.boto3_raw_data["Activity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelInstanceRefreshAnswer:
    boto3_raw_data: "type_defs.CancelInstanceRefreshAnswerTypeDef" = dataclasses.field()

    InstanceRefreshId = field("InstanceRefreshId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelInstanceRefreshAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelInstanceRefreshAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsAnswer:
    boto3_raw_data: "type_defs.DescribeAccountLimitsAnswerTypeDef" = dataclasses.field()

    MaxNumberOfAutoScalingGroups = field("MaxNumberOfAutoScalingGroups")
    MaxNumberOfLaunchConfigurations = field("MaxNumberOfLaunchConfigurations")
    NumberOfAutoScalingGroups = field("NumberOfAutoScalingGroups")
    NumberOfLaunchConfigurations = field("NumberOfLaunchConfigurations")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoScalingNotificationTypesAnswer:
    boto3_raw_data: "type_defs.DescribeAutoScalingNotificationTypesAnswerTypeDef" = (
        dataclasses.field()
    )

    AutoScalingNotificationTypes = field("AutoScalingNotificationTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutoScalingNotificationTypesAnswerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoScalingNotificationTypesAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLifecycleHookTypesAnswer:
    boto3_raw_data: "type_defs.DescribeLifecycleHookTypesAnswerTypeDef" = (
        dataclasses.field()
    )

    LifecycleHookTypes = field("LifecycleHookTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLifecycleHookTypesAnswerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLifecycleHookTypesAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTerminationPolicyTypesAnswer:
    boto3_raw_data: "type_defs.DescribeTerminationPolicyTypesAnswerTypeDef" = (
        dataclasses.field()
    )

    TerminationPolicyTypes = field("TerminationPolicyTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTerminationPolicyTypesAnswerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTerminationPolicyTypesAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachInstancesAnswer:
    boto3_raw_data: "type_defs.DetachInstancesAnswerTypeDef" = dataclasses.field()

    @cached_property
    def Activities(self):  # pragma: no cover
        return Activity.make_many(self.boto3_raw_data["Activities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachInstancesAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachInstancesAnswerTypeDef"]
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
class EnterStandbyAnswer:
    boto3_raw_data: "type_defs.EnterStandbyAnswerTypeDef" = dataclasses.field()

    @cached_property
    def Activities(self):  # pragma: no cover
        return Activity.make_many(self.boto3_raw_data["Activities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnterStandbyAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnterStandbyAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExitStandbyAnswer:
    boto3_raw_data: "type_defs.ExitStandbyAnswerTypeDef" = dataclasses.field()

    @cached_property
    def Activities(self):  # pragma: no cover
        return Activity.make_many(self.boto3_raw_data["Activities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExitStandbyAnswerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExitStandbyAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackInstanceRefreshAnswer:
    boto3_raw_data: "type_defs.RollbackInstanceRefreshAnswerTypeDef" = (
        dataclasses.field()
    )

    InstanceRefreshId = field("InstanceRefreshId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RollbackInstanceRefreshAnswerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackInstanceRefreshAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceRefreshAnswer:
    boto3_raw_data: "type_defs.StartInstanceRefreshAnswerTypeDef" = dataclasses.field()

    InstanceRefreshId = field("InstanceRefreshId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInstanceRefreshAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceRefreshAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAdjustmentTypesAnswer:
    boto3_raw_data: "type_defs.DescribeAdjustmentTypesAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AdjustmentTypes(self):  # pragma: no cover
        return AdjustmentType.make_many(self.boto3_raw_data["AdjustmentTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAdjustmentTypesAnswerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAdjustmentTypesAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshPreferencesOutput:
    boto3_raw_data: "type_defs.RefreshPreferencesOutputTypeDef" = dataclasses.field()

    MinHealthyPercentage = field("MinHealthyPercentage")
    InstanceWarmup = field("InstanceWarmup")
    CheckpointPercentages = field("CheckpointPercentages")
    CheckpointDelay = field("CheckpointDelay")
    SkipMatching = field("SkipMatching")
    AutoRollback = field("AutoRollback")
    ScaleInProtectedInstances = field("ScaleInProtectedInstances")
    StandbyInstances = field("StandbyInstances")

    @cached_property
    def AlarmSpecification(self):  # pragma: no cover
        return AlarmSpecificationOutput.make_one(
            self.boto3_raw_data["AlarmSpecification"]
        )

    MaxHealthyPercentage = field("MaxHealthyPercentage")
    BakeTime = field("BakeTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshPreferencesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshPreferencesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshPreferences:
    boto3_raw_data: "type_defs.RefreshPreferencesTypeDef" = dataclasses.field()

    MinHealthyPercentage = field("MinHealthyPercentage")
    InstanceWarmup = field("InstanceWarmup")
    CheckpointPercentages = field("CheckpointPercentages")
    CheckpointDelay = field("CheckpointDelay")
    SkipMatching = field("SkipMatching")
    AutoRollback = field("AutoRollback")
    ScaleInProtectedInstances = field("ScaleInProtectedInstances")
    StandbyInstances = field("StandbyInstances")

    @cached_property
    def AlarmSpecification(self):  # pragma: no cover
        return AlarmSpecification.make_one(self.boto3_raw_data["AlarmSpecification"])

    MaxHealthyPercentage = field("MaxHealthyPercentage")
    BakeTime = field("BakeTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyARNType:
    boto3_raw_data: "type_defs.PolicyARNTypeTypeDef" = dataclasses.field()

    PolicyARN = field("PolicyARN")

    @cached_property
    def Alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["Alarms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyARNTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyARNTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachTrafficSourcesType:
    boto3_raw_data: "type_defs.AttachTrafficSourcesTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")

    @cached_property
    def TrafficSources(self):  # pragma: no cover
        return TrafficSourceIdentifier.make_many(self.boto3_raw_data["TrafficSources"])

    SkipZonalShiftValidation = field("SkipZonalShiftValidation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachTrafficSourcesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachTrafficSourcesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachTrafficSourcesType:
    boto3_raw_data: "type_defs.DetachTrafficSourcesTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")

    @cached_property
    def TrafficSources(self):  # pragma: no cover
        return TrafficSourceIdentifier.make_many(self.boto3_raw_data["TrafficSources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachTrafficSourcesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachTrafficSourcesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupNamesType:
    boto3_raw_data: "type_defs.AutoScalingGroupNamesTypeTypeDef" = dataclasses.field()

    AutoScalingGroupNames = field("AutoScalingGroupNames")
    IncludeInstances = field("IncludeInstances")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingGroupNamesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupNamesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsType:
    boto3_raw_data: "type_defs.DescribeTagsTypeTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupNamesTypePaginate:
    boto3_raw_data: "type_defs.AutoScalingGroupNamesTypePaginateTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupNames = field("AutoScalingGroupNames")
    IncludeInstances = field("IncludeInstances")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingGroupNamesTypePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupNamesTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoScalingInstancesTypePaginate:
    boto3_raw_data: "type_defs.DescribeAutoScalingInstancesTypePaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceIds = field("InstanceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutoScalingInstancesTypePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoScalingInstancesTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerTargetGroupsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef"
    ) = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef"
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
                "type_defs.DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeLoadBalancersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationConfigurationsTypePaginate:
    boto3_raw_data: (
        "type_defs.DescribeNotificationConfigurationsTypePaginateTypeDef"
    ) = dataclasses.field()

    AutoScalingGroupNames = field("AutoScalingGroupNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationConfigurationsTypePaginateTypeDef"
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
                "type_defs.DescribeNotificationConfigurationsTypePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePoliciesTypePaginate:
    boto3_raw_data: "type_defs.DescribePoliciesTypePaginateTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    PolicyNames = field("PolicyNames")
    PolicyTypes = field("PolicyTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePoliciesTypePaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePoliciesTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingActivitiesTypePaginate:
    boto3_raw_data: "type_defs.DescribeScalingActivitiesTypePaginateTypeDef" = (
        dataclasses.field()
    )

    ActivityIds = field("ActivityIds")
    AutoScalingGroupName = field("AutoScalingGroupName")
    IncludeDeletedGroups = field("IncludeDeletedGroups")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingActivitiesTypePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingActivitiesTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsTypePaginate:
    boto3_raw_data: "type_defs.DescribeTagsTypePaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsTypePaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWarmPoolTypePaginate:
    boto3_raw_data: "type_defs.DescribeWarmPoolTypePaginateTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWarmPoolTypePaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWarmPoolTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationNamesTypePaginate:
    boto3_raw_data: "type_defs.LaunchConfigurationNamesTypePaginateTypeDef" = (
        dataclasses.field()
    )

    LaunchConfigurationNames = field("LaunchConfigurationNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LaunchConfigurationNamesTypePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationNamesTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingInstanceDetails:
    boto3_raw_data: "type_defs.AutoScalingInstanceDetailsTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    AutoScalingGroupName = field("AutoScalingGroupName")
    AvailabilityZone = field("AvailabilityZone")
    LifecycleState = field("LifecycleState")
    HealthStatus = field("HealthStatus")
    ProtectedFromScaleIn = field("ProtectedFromScaleIn")
    InstanceType = field("InstanceType")
    LaunchConfigurationName = field("LaunchConfigurationName")

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    WeightedCapacity = field("WeightedCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    AvailabilityZone = field("AvailabilityZone")
    LifecycleState = field("LifecycleState")
    HealthStatus = field("HealthStatus")
    ProtectedFromScaleIn = field("ProtectedFromScaleIn")
    InstanceType = field("InstanceType")
    LaunchConfigurationName = field("LaunchConfigurationName")

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    WeightedCapacity = field("WeightedCapacity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagsType:
    boto3_raw_data: "type_defs.TagsTypeTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagDescription.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteScheduledActionAnswer:
    boto3_raw_data: "type_defs.BatchDeleteScheduledActionAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedScheduledActions(self):  # pragma: no cover
        return FailedScheduledUpdateGroupActionRequest.make_many(
            self.boto3_raw_data["FailedScheduledActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteScheduledActionAnswerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteScheduledActionAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutScheduledUpdateGroupActionAnswer:
    boto3_raw_data: "type_defs.BatchPutScheduledUpdateGroupActionAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedScheduledUpdateGroupActions(self):  # pragma: no cover
        return FailedScheduledUpdateGroupActionRequest.make_many(
            self.boto3_raw_data["FailedScheduledUpdateGroupActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchPutScheduledUpdateGroupActionAnswerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutScheduledUpdateGroupActionAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockDeviceMapping:
    boto3_raw_data: "type_defs.BlockDeviceMappingTypeDef" = dataclasses.field()

    DeviceName = field("DeviceName")
    VirtualName = field("VirtualName")

    @cached_property
    def Ebs(self):  # pragma: no cover
        return Ebs.make_one(self.boto3_raw_data["Ebs"])

    NoDevice = field("NoDevice")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlockDeviceMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockDeviceMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationSpecificationOutput:
    boto3_raw_data: "type_defs.CapacityReservationSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationPreference = field("CapacityReservationPreference")

    @cached_property
    def CapacityReservationTarget(self):  # pragma: no cover
        return CapacityReservationTargetOutput.make_one(
            self.boto3_raw_data["CapacityReservationTarget"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CapacityReservationSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationSpecification:
    boto3_raw_data: "type_defs.CapacityReservationSpecificationTypeDef" = (
        dataclasses.field()
    )

    CapacityReservationPreference = field("CapacityReservationPreference")

    @cached_property
    def CapacityReservationTarget(self):  # pragma: no cover
        return CapacityReservationTarget.make_one(
            self.boto3_raw_data["CapacityReservationTarget"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CapacityReservationSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CpuPerformanceFactorRequestOutput:
    boto3_raw_data: "type_defs.CpuPerformanceFactorRequestOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def References(self):  # pragma: no cover
        return PerformanceFactorReferenceRequest.make_many(
            self.boto3_raw_data["References"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CpuPerformanceFactorRequestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CpuPerformanceFactorRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CpuPerformanceFactorRequest:
    boto3_raw_data: "type_defs.CpuPerformanceFactorRequestTypeDef" = dataclasses.field()

    @cached_property
    def References(self):  # pragma: no cover
        return PerformanceFactorReferenceRequest.make_many(
            self.boto3_raw_data["References"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CpuPerformanceFactorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CpuPerformanceFactorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOrUpdateTagsType:
    boto3_raw_data: "type_defs.CreateOrUpdateTagsTypeTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOrUpdateTagsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOrUpdateTagsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsType:
    boto3_raw_data: "type_defs.DeleteTagsTypeTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteTagsTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricOutput:
    boto3_raw_data: "type_defs.MetricOutputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLifecycleHooksAnswer:
    boto3_raw_data: "type_defs.DescribeLifecycleHooksAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LifecycleHooks(self):  # pragma: no cover
        return LifecycleHook.make_many(self.boto3_raw_data["LifecycleHooks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLifecycleHooksAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLifecycleHooksAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerTargetGroupsResponse:
    boto3_raw_data: "type_defs.DescribeLoadBalancerTargetGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadBalancerTargetGroups(self):  # pragma: no cover
        return LoadBalancerTargetGroupState.make_many(
            self.boto3_raw_data["LoadBalancerTargetGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerTargetGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerTargetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersResponse:
    boto3_raw_data: "type_defs.DescribeLoadBalancersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadBalancers(self):  # pragma: no cover
        return LoadBalancerState.make_many(self.boto3_raw_data["LoadBalancers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLoadBalancersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricCollectionTypesAnswer:
    boto3_raw_data: "type_defs.DescribeMetricCollectionTypesAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metrics(self):  # pragma: no cover
        return MetricCollectionType.make_many(self.boto3_raw_data["Metrics"])

    @cached_property
    def Granularities(self):  # pragma: no cover
        return MetricGranularityType.make_many(self.boto3_raw_data["Granularities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetricCollectionTypesAnswerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricCollectionTypesAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationConfigurationsAnswer:
    boto3_raw_data: "type_defs.DescribeNotificationConfigurationsAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NotificationConfigurations(self):  # pragma: no cover
        return NotificationConfiguration.make_many(
            self.boto3_raw_data["NotificationConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationConfigurationsAnswerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationConfigurationsAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsTypePaginate:
    boto3_raw_data: "type_defs.DescribeScheduledActionsTypePaginateTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScheduledActionNames = field("ScheduledActionNames")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScheduledActionsTypePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsTypePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsType:
    boto3_raw_data: "type_defs.DescribeScheduledActionsTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScheduledActionNames = field("ScheduledActionNames")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeScheduledActionsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPredictiveScalingForecastType:
    boto3_raw_data: "type_defs.GetPredictiveScalingForecastTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    PolicyName = field("PolicyName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPredictiveScalingForecastTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPredictiveScalingForecastTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutScheduledUpdateGroupActionType:
    boto3_raw_data: "type_defs.PutScheduledUpdateGroupActionTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")
    ScheduledActionName = field("ScheduledActionName")
    Time = field("Time")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Recurrence = field("Recurrence")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    DesiredCapacity = field("DesiredCapacity")
    TimeZone = field("TimeZone")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutScheduledUpdateGroupActionTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScheduledUpdateGroupActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledUpdateGroupActionRequest:
    boto3_raw_data: "type_defs.ScheduledUpdateGroupActionRequestTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Recurrence = field("Recurrence")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    DesiredCapacity = field("DesiredCapacity")
    TimeZone = field("TimeZone")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScheduledUpdateGroupActionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledUpdateGroupActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrafficSourcesResponse:
    boto3_raw_data: "type_defs.DescribeTrafficSourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficSources(self):  # pragma: no cover
        return TrafficSourceState.make_many(self.boto3_raw_data["TrafficSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTrafficSourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrafficSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRefreshProgressDetails:
    boto3_raw_data: "type_defs.InstanceRefreshProgressDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LivePoolProgress(self):  # pragma: no cover
        return InstanceRefreshLivePoolProgress.make_one(
            self.boto3_raw_data["LivePoolProgress"]
        )

    @cached_property
    def WarmPoolProgress(self):  # pragma: no cover
        return InstanceRefreshWarmPoolProgress.make_one(
            self.boto3_raw_data["WarmPoolProgress"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceRefreshProgressDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRefreshProgressDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutWarmPoolType:
    boto3_raw_data: "type_defs.PutWarmPoolTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    MaxGroupPreparedCapacity = field("MaxGroupPreparedCapacity")
    MinSize = field("MinSize")
    PoolState = field("PoolState")

    @cached_property
    def InstanceReusePolicy(self):  # pragma: no cover
        return InstanceReusePolicy.make_one(self.boto3_raw_data["InstanceReusePolicy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutWarmPoolTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutWarmPoolTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarmPoolConfiguration:
    boto3_raw_data: "type_defs.WarmPoolConfigurationTypeDef" = dataclasses.field()

    MaxGroupPreparedCapacity = field("MaxGroupPreparedCapacity")
    MinSize = field("MinSize")
    PoolState = field("PoolState")
    Status = field("Status")

    @cached_property
    def InstanceReusePolicy(self):  # pragma: no cover
        return InstanceReusePolicy.make_one(self.boto3_raw_data["InstanceReusePolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WarmPoolConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WarmPoolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessesType:
    boto3_raw_data: "type_defs.ProcessesTypeTypeDef" = dataclasses.field()

    @cached_property
    def Processes(self):  # pragma: no cover
        return ProcessType.make_many(self.boto3_raw_data["Processes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessesTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessesTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledActionsType:
    boto3_raw_data: "type_defs.ScheduledActionsTypeTypeDef" = dataclasses.field()

    @cached_property
    def ScheduledUpdateGroupActions(self):  # pragma: no cover
        return ScheduledUpdateGroupAction.make_many(
            self.boto3_raw_data["ScheduledUpdateGroupActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledActionsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingInstancesType:
    boto3_raw_data: "type_defs.AutoScalingInstancesTypeTypeDef" = dataclasses.field()

    @cached_property
    def AutoScalingInstances(self):  # pragma: no cover
        return AutoScalingInstanceDetails.make_many(
            self.boto3_raw_data["AutoScalingInstances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingInstancesTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingInstancesTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLaunchConfigurationType:
    boto3_raw_data: "type_defs.CreateLaunchConfigurationTypeTypeDef" = (
        dataclasses.field()
    )

    LaunchConfigurationName = field("LaunchConfigurationName")
    ImageId = field("ImageId")
    KeyName = field("KeyName")
    SecurityGroups = field("SecurityGroups")
    ClassicLinkVPCId = field("ClassicLinkVPCId")
    ClassicLinkVPCSecurityGroups = field("ClassicLinkVPCSecurityGroups")
    UserData = field("UserData")
    InstanceId = field("InstanceId")
    InstanceType = field("InstanceType")
    KernelId = field("KernelId")
    RamdiskId = field("RamdiskId")

    @cached_property
    def BlockDeviceMappings(self):  # pragma: no cover
        return BlockDeviceMapping.make_many(self.boto3_raw_data["BlockDeviceMappings"])

    @cached_property
    def InstanceMonitoring(self):  # pragma: no cover
        return InstanceMonitoring.make_one(self.boto3_raw_data["InstanceMonitoring"])

    SpotPrice = field("SpotPrice")
    IamInstanceProfile = field("IamInstanceProfile")
    EbsOptimized = field("EbsOptimized")
    AssociatePublicIpAddress = field("AssociatePublicIpAddress")
    PlacementTenancy = field("PlacementTenancy")

    @cached_property
    def MetadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptions.make_one(self.boto3_raw_data["MetadataOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLaunchConfigurationTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLaunchConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfiguration:
    boto3_raw_data: "type_defs.LaunchConfigurationTypeDef" = dataclasses.field()

    LaunchConfigurationName = field("LaunchConfigurationName")
    ImageId = field("ImageId")
    InstanceType = field("InstanceType")
    CreatedTime = field("CreatedTime")
    LaunchConfigurationARN = field("LaunchConfigurationARN")
    KeyName = field("KeyName")
    SecurityGroups = field("SecurityGroups")
    ClassicLinkVPCId = field("ClassicLinkVPCId")
    ClassicLinkVPCSecurityGroups = field("ClassicLinkVPCSecurityGroups")
    UserData = field("UserData")
    KernelId = field("KernelId")
    RamdiskId = field("RamdiskId")

    @cached_property
    def BlockDeviceMappings(self):  # pragma: no cover
        return BlockDeviceMapping.make_many(self.boto3_raw_data["BlockDeviceMappings"])

    @cached_property
    def InstanceMonitoring(self):  # pragma: no cover
        return InstanceMonitoring.make_one(self.boto3_raw_data["InstanceMonitoring"])

    SpotPrice = field("SpotPrice")
    IamInstanceProfile = field("IamInstanceProfile")
    EbsOptimized = field("EbsOptimized")
    AssociatePublicIpAddress = field("AssociatePublicIpAddress")
    PlacementTenancy = field("PlacementTenancy")

    @cached_property
    def MetadataOptions(self):  # pragma: no cover
        return InstanceMetadataOptions.make_one(self.boto3_raw_data["MetadataOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaselinePerformanceFactorsRequestOutput:
    boto3_raw_data: "type_defs.BaselinePerformanceFactorsRequestOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cpu(self):  # pragma: no cover
        return CpuPerformanceFactorRequestOutput.make_one(self.boto3_raw_data["Cpu"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BaselinePerformanceFactorsRequestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaselinePerformanceFactorsRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaselinePerformanceFactorsRequest:
    boto3_raw_data: "type_defs.BaselinePerformanceFactorsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cpu(self):  # pragma: no cover
        return CpuPerformanceFactorRequest.make_one(self.boto3_raw_data["Cpu"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BaselinePerformanceFactorsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaselinePerformanceFactorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStatOutput:
    boto3_raw_data: "type_defs.MetricStatOutputTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return MetricOutput.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricStatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricStatOutput:
    boto3_raw_data: "type_defs.TargetTrackingMetricStatOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Metric(self):  # pragma: no cover
        return MetricOutput.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")
    Period = field("Period")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricStatOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricStatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricStat:
    boto3_raw_data: "type_defs.MetricStatTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return Metric.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricStatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricStatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricStat:
    boto3_raw_data: "type_defs.TargetTrackingMetricStatTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return Metric.make_one(self.boto3_raw_data["Metric"])

    Stat = field("Stat")
    Unit = field("Unit")
    Period = field("Period")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricStatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricStatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutScheduledUpdateGroupActionType:
    boto3_raw_data: "type_defs.BatchPutScheduledUpdateGroupActionTypeTypeDef" = (
        dataclasses.field()
    )

    AutoScalingGroupName = field("AutoScalingGroupName")

    @cached_property
    def ScheduledUpdateGroupActions(self):  # pragma: no cover
        return ScheduledUpdateGroupActionRequest.make_many(
            self.boto3_raw_data["ScheduledUpdateGroupActions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchPutScheduledUpdateGroupActionTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutScheduledUpdateGroupActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackDetails:
    boto3_raw_data: "type_defs.RollbackDetailsTypeDef" = dataclasses.field()

    RollbackReason = field("RollbackReason")
    RollbackStartTime = field("RollbackStartTime")
    PercentageCompleteOnRollback = field("PercentageCompleteOnRollback")
    InstancesToUpdateOnRollback = field("InstancesToUpdateOnRollback")

    @cached_property
    def ProgressDetailsOnRollback(self):  # pragma: no cover
        return InstanceRefreshProgressDetails.make_one(
            self.boto3_raw_data["ProgressDetailsOnRollback"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RollbackDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RollbackDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWarmPoolAnswer:
    boto3_raw_data: "type_defs.DescribeWarmPoolAnswerTypeDef" = dataclasses.field()

    @cached_property
    def WarmPoolConfiguration(self):  # pragma: no cover
        return WarmPoolConfiguration.make_one(
            self.boto3_raw_data["WarmPoolConfiguration"]
        )

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWarmPoolAnswerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWarmPoolAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationsType:
    boto3_raw_data: "type_defs.LaunchConfigurationsTypeTypeDef" = dataclasses.field()

    @cached_property
    def LaunchConfigurations(self):  # pragma: no cover
        return LaunchConfiguration.make_many(
            self.boto3_raw_data["LaunchConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRequirementsOutput:
    boto3_raw_data: "type_defs.InstanceRequirementsOutputTypeDef" = dataclasses.field()

    @cached_property
    def VCpuCount(self):  # pragma: no cover
        return VCpuCountRequest.make_one(self.boto3_raw_data["VCpuCount"])

    @cached_property
    def MemoryMiB(self):  # pragma: no cover
        return MemoryMiBRequest.make_one(self.boto3_raw_data["MemoryMiB"])

    CpuManufacturers = field("CpuManufacturers")

    @cached_property
    def MemoryGiBPerVCpu(self):  # pragma: no cover
        return MemoryGiBPerVCpuRequest.make_one(self.boto3_raw_data["MemoryGiBPerVCpu"])

    ExcludedInstanceTypes = field("ExcludedInstanceTypes")
    InstanceGenerations = field("InstanceGenerations")
    SpotMaxPricePercentageOverLowestPrice = field(
        "SpotMaxPricePercentageOverLowestPrice"
    )
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice = field(
        "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    )
    OnDemandMaxPricePercentageOverLowestPrice = field(
        "OnDemandMaxPricePercentageOverLowestPrice"
    )
    BareMetal = field("BareMetal")
    BurstablePerformance = field("BurstablePerformance")
    RequireHibernateSupport = field("RequireHibernateSupport")

    @cached_property
    def NetworkInterfaceCount(self):  # pragma: no cover
        return NetworkInterfaceCountRequest.make_one(
            self.boto3_raw_data["NetworkInterfaceCount"]
        )

    LocalStorage = field("LocalStorage")
    LocalStorageTypes = field("LocalStorageTypes")

    @cached_property
    def TotalLocalStorageGB(self):  # pragma: no cover
        return TotalLocalStorageGBRequest.make_one(
            self.boto3_raw_data["TotalLocalStorageGB"]
        )

    @cached_property
    def BaselineEbsBandwidthMbps(self):  # pragma: no cover
        return BaselineEbsBandwidthMbpsRequest.make_one(
            self.boto3_raw_data["BaselineEbsBandwidthMbps"]
        )

    AcceleratorTypes = field("AcceleratorTypes")

    @cached_property
    def AcceleratorCount(self):  # pragma: no cover
        return AcceleratorCountRequest.make_one(self.boto3_raw_data["AcceleratorCount"])

    AcceleratorManufacturers = field("AcceleratorManufacturers")
    AcceleratorNames = field("AcceleratorNames")

    @cached_property
    def AcceleratorTotalMemoryMiB(self):  # pragma: no cover
        return AcceleratorTotalMemoryMiBRequest.make_one(
            self.boto3_raw_data["AcceleratorTotalMemoryMiB"]
        )

    @cached_property
    def NetworkBandwidthGbps(self):  # pragma: no cover
        return NetworkBandwidthGbpsRequest.make_one(
            self.boto3_raw_data["NetworkBandwidthGbps"]
        )

    AllowedInstanceTypes = field("AllowedInstanceTypes")

    @cached_property
    def BaselinePerformanceFactors(self):  # pragma: no cover
        return BaselinePerformanceFactorsRequestOutput.make_one(
            self.boto3_raw_data["BaselinePerformanceFactors"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceRequirementsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRequirementsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRequirements:
    boto3_raw_data: "type_defs.InstanceRequirementsTypeDef" = dataclasses.field()

    @cached_property
    def VCpuCount(self):  # pragma: no cover
        return VCpuCountRequest.make_one(self.boto3_raw_data["VCpuCount"])

    @cached_property
    def MemoryMiB(self):  # pragma: no cover
        return MemoryMiBRequest.make_one(self.boto3_raw_data["MemoryMiB"])

    CpuManufacturers = field("CpuManufacturers")

    @cached_property
    def MemoryGiBPerVCpu(self):  # pragma: no cover
        return MemoryGiBPerVCpuRequest.make_one(self.boto3_raw_data["MemoryGiBPerVCpu"])

    ExcludedInstanceTypes = field("ExcludedInstanceTypes")
    InstanceGenerations = field("InstanceGenerations")
    SpotMaxPricePercentageOverLowestPrice = field(
        "SpotMaxPricePercentageOverLowestPrice"
    )
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice = field(
        "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    )
    OnDemandMaxPricePercentageOverLowestPrice = field(
        "OnDemandMaxPricePercentageOverLowestPrice"
    )
    BareMetal = field("BareMetal")
    BurstablePerformance = field("BurstablePerformance")
    RequireHibernateSupport = field("RequireHibernateSupport")

    @cached_property
    def NetworkInterfaceCount(self):  # pragma: no cover
        return NetworkInterfaceCountRequest.make_one(
            self.boto3_raw_data["NetworkInterfaceCount"]
        )

    LocalStorage = field("LocalStorage")
    LocalStorageTypes = field("LocalStorageTypes")

    @cached_property
    def TotalLocalStorageGB(self):  # pragma: no cover
        return TotalLocalStorageGBRequest.make_one(
            self.boto3_raw_data["TotalLocalStorageGB"]
        )

    @cached_property
    def BaselineEbsBandwidthMbps(self):  # pragma: no cover
        return BaselineEbsBandwidthMbpsRequest.make_one(
            self.boto3_raw_data["BaselineEbsBandwidthMbps"]
        )

    AcceleratorTypes = field("AcceleratorTypes")

    @cached_property
    def AcceleratorCount(self):  # pragma: no cover
        return AcceleratorCountRequest.make_one(self.boto3_raw_data["AcceleratorCount"])

    AcceleratorManufacturers = field("AcceleratorManufacturers")
    AcceleratorNames = field("AcceleratorNames")

    @cached_property
    def AcceleratorTotalMemoryMiB(self):  # pragma: no cover
        return AcceleratorTotalMemoryMiBRequest.make_one(
            self.boto3_raw_data["AcceleratorTotalMemoryMiB"]
        )

    @cached_property
    def NetworkBandwidthGbps(self):  # pragma: no cover
        return NetworkBandwidthGbpsRequest.make_one(
            self.boto3_raw_data["NetworkBandwidthGbps"]
        )

    AllowedInstanceTypes = field("AllowedInstanceTypes")

    @cached_property
    def BaselinePerformanceFactors(self):  # pragma: no cover
        return BaselinePerformanceFactorsRequest.make_one(
            self.boto3_raw_data["BaselinePerformanceFactors"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceRequirementsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceRequirementsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQueryOutput:
    boto3_raw_data: "type_defs.MetricDataQueryOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    Expression = field("Expression")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return MetricStatOutput.make_one(self.boto3_raw_data["MetricStat"])

    Label = field("Label")
    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricDataQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricDataQueryOutput:
    boto3_raw_data: "type_defs.TargetTrackingMetricDataQueryOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Expression = field("Expression")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return TargetTrackingMetricStatOutput.make_one(
            self.boto3_raw_data["MetricStat"]
        )

    Label = field("Label")
    Period = field("Period")
    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingMetricDataQueryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricDataQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataQuery:
    boto3_raw_data: "type_defs.MetricDataQueryTypeDef" = dataclasses.field()

    Id = field("Id")
    Expression = field("Expression")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return MetricStat.make_one(self.boto3_raw_data["MetricStat"])

    Label = field("Label")
    ReturnData = field("ReturnData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDataQueryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingMetricDataQuery:
    boto3_raw_data: "type_defs.TargetTrackingMetricDataQueryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Expression = field("Expression")

    @cached_property
    def MetricStat(self):  # pragma: no cover
        return TargetTrackingMetricStat.make_one(self.boto3_raw_data["MetricStat"])

    Label = field("Label")
    Period = field("Period")
    ReturnData = field("ReturnData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TargetTrackingMetricDataQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingMetricDataQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateOverridesOutput:
    boto3_raw_data: "type_defs.LaunchTemplateOverridesOutputTypeDef" = (
        dataclasses.field()
    )

    InstanceType = field("InstanceType")
    WeightedCapacity = field("WeightedCapacity")

    @cached_property
    def LaunchTemplateSpecification(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplateSpecification"]
        )

    @cached_property
    def InstanceRequirements(self):  # pragma: no cover
        return InstanceRequirementsOutput.make_one(
            self.boto3_raw_data["InstanceRequirements"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LaunchTemplateOverridesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateOverridesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateOverrides:
    boto3_raw_data: "type_defs.LaunchTemplateOverridesTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    WeightedCapacity = field("WeightedCapacity")

    @cached_property
    def LaunchTemplateSpecification(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplateSpecification"]
        )

    @cached_property
    def InstanceRequirements(self):  # pragma: no cover
        return InstanceRequirements.make_one(
            self.boto3_raw_data["InstanceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedCapacityMetricOutput:
    boto3_raw_data: (
        "type_defs.PredictiveScalingCustomizedCapacityMetricOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedCapacityMetricOutputTypeDef"
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
                "type_defs.PredictiveScalingCustomizedCapacityMetricOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedLoadMetricOutput:
    boto3_raw_data: "type_defs.PredictiveScalingCustomizedLoadMetricOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedLoadMetricOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingCustomizedLoadMetricOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedScalingMetricOutput:
    boto3_raw_data: (
        "type_defs.PredictiveScalingCustomizedScalingMetricOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQueryOutput.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedScalingMetricOutputTypeDef"
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
                "type_defs.PredictiveScalingCustomizedScalingMetricOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedMetricSpecificationOutput:
    boto3_raw_data: "type_defs.CustomizedMetricSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Statistic = field("Statistic")
    Unit = field("Unit")
    Period = field("Period")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return TargetTrackingMetricDataQueryOutput.make_many(
            self.boto3_raw_data["Metrics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomizedMetricSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedMetricSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedCapacityMetric:
    boto3_raw_data: "type_defs.PredictiveScalingCustomizedCapacityMetricTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQuery.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedCapacityMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingCustomizedCapacityMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedLoadMetric:
    boto3_raw_data: "type_defs.PredictiveScalingCustomizedLoadMetricTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQuery.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedLoadMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingCustomizedLoadMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingCustomizedScalingMetric:
    boto3_raw_data: "type_defs.PredictiveScalingCustomizedScalingMetricTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricDataQueries(self):  # pragma: no cover
        return MetricDataQuery.make_many(self.boto3_raw_data["MetricDataQueries"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingCustomizedScalingMetricTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingCustomizedScalingMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizedMetricSpecification:
    boto3_raw_data: "type_defs.CustomizedMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    MetricName = field("MetricName")
    Namespace = field("Namespace")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    Statistic = field("Statistic")
    Unit = field("Unit")
    Period = field("Period")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return TargetTrackingMetricDataQuery.make_many(self.boto3_raw_data["Metrics"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomizedMetricSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizedMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateOutput:
    boto3_raw_data: "type_defs.LaunchTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def LaunchTemplateSpecification(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplateSpecification"]
        )

    @cached_property
    def Overrides(self):  # pragma: no cover
        return LaunchTemplateOverridesOutput.make_many(self.boto3_raw_data["Overrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplate:
    boto3_raw_data: "type_defs.LaunchTemplateTypeDef" = dataclasses.field()

    @cached_property
    def LaunchTemplateSpecification(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplateSpecification"]
        )

    @cached_property
    def Overrides(self):  # pragma: no cover
        return LaunchTemplateOverrides.make_many(self.boto3_raw_data["Overrides"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricSpecificationOutput:
    boto3_raw_data: "type_defs.PredictiveScalingMetricSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricPairSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedMetricPair.make_one(
            self.boto3_raw_data["PredefinedMetricPairSpecification"]
        )

    @cached_property
    def PredefinedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedScalingMetric.make_one(
            self.boto3_raw_data["PredefinedScalingMetricSpecification"]
        )

    @cached_property
    def PredefinedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedLoadMetric.make_one(
            self.boto3_raw_data["PredefinedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedScalingMetricOutput.make_one(
            self.boto3_raw_data["CustomizedScalingMetricSpecification"]
        )

    @cached_property
    def CustomizedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedLoadMetricOutput.make_one(
            self.boto3_raw_data["CustomizedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedCapacityMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedCapacityMetricOutput.make_one(
            self.boto3_raw_data["CustomizedCapacityMetricSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingMetricSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingConfigurationOutput:
    boto3_raw_data: "type_defs.TargetTrackingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricSpecification(self):  # pragma: no cover
        return PredefinedMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedMetricSpecification"]
        )

    @cached_property
    def CustomizedMetricSpecification(self):  # pragma: no cover
        return CustomizedMetricSpecificationOutput.make_one(
            self.boto3_raw_data["CustomizedMetricSpecification"]
        )

    DisableScaleIn = field("DisableScaleIn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetTrackingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingMetricSpecification:
    boto3_raw_data: "type_defs.PredictiveScalingMetricSpecificationTypeDef" = (
        dataclasses.field()
    )

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricPairSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedMetricPair.make_one(
            self.boto3_raw_data["PredefinedMetricPairSpecification"]
        )

    @cached_property
    def PredefinedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedScalingMetric.make_one(
            self.boto3_raw_data["PredefinedScalingMetricSpecification"]
        )

    @cached_property
    def PredefinedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingPredefinedLoadMetric.make_one(
            self.boto3_raw_data["PredefinedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedScalingMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedScalingMetric.make_one(
            self.boto3_raw_data["CustomizedScalingMetricSpecification"]
        )

    @cached_property
    def CustomizedLoadMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedLoadMetric.make_one(
            self.boto3_raw_data["CustomizedLoadMetricSpecification"]
        )

    @cached_property
    def CustomizedCapacityMetricSpecification(self):  # pragma: no cover
        return PredictiveScalingCustomizedCapacityMetric.make_one(
            self.boto3_raw_data["CustomizedCapacityMetricSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingMetricSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingMetricSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetTrackingConfiguration:
    boto3_raw_data: "type_defs.TargetTrackingConfigurationTypeDef" = dataclasses.field()

    TargetValue = field("TargetValue")

    @cached_property
    def PredefinedMetricSpecification(self):  # pragma: no cover
        return PredefinedMetricSpecification.make_one(
            self.boto3_raw_data["PredefinedMetricSpecification"]
        )

    @cached_property
    def CustomizedMetricSpecification(self):  # pragma: no cover
        return CustomizedMetricSpecification.make_one(
            self.boto3_raw_data["CustomizedMetricSpecification"]
        )

    DisableScaleIn = field("DisableScaleIn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetTrackingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetTrackingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MixedInstancesPolicyOutput:
    boto3_raw_data: "type_defs.MixedInstancesPolicyOutputTypeDef" = dataclasses.field()

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateOutput.make_one(self.boto3_raw_data["LaunchTemplate"])

    @cached_property
    def InstancesDistribution(self):  # pragma: no cover
        return InstancesDistribution.make_one(
            self.boto3_raw_data["InstancesDistribution"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedInstancesPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedInstancesPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MixedInstancesPolicy:
    boto3_raw_data: "type_defs.MixedInstancesPolicyTypeDef" = dataclasses.field()

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplate.make_one(self.boto3_raw_data["LaunchTemplate"])

    @cached_property
    def InstancesDistribution(self):  # pragma: no cover
        return InstancesDistribution.make_one(
            self.boto3_raw_data["InstancesDistribution"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MixedInstancesPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MixedInstancesPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadForecast:
    boto3_raw_data: "type_defs.LoadForecastTypeDef" = dataclasses.field()

    Timestamps = field("Timestamps")
    Values = field("Values")

    @cached_property
    def MetricSpecification(self):  # pragma: no cover
        return PredictiveScalingMetricSpecificationOutput.make_one(
            self.boto3_raw_data["MetricSpecification"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadForecastTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoadForecastTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingConfigurationOutput:
    boto3_raw_data: "type_defs.PredictiveScalingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricSpecifications(self):  # pragma: no cover
        return PredictiveScalingMetricSpecificationOutput.make_many(
            self.boto3_raw_data["MetricSpecifications"]
        )

    Mode = field("Mode")
    SchedulingBufferTime = field("SchedulingBufferTime")
    MaxCapacityBreachBehavior = field("MaxCapacityBreachBehavior")
    MaxCapacityBuffer = field("MaxCapacityBuffer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredictiveScalingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictiveScalingConfiguration:
    boto3_raw_data: "type_defs.PredictiveScalingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricSpecifications(self):  # pragma: no cover
        return PredictiveScalingMetricSpecification.make_many(
            self.boto3_raw_data["MetricSpecifications"]
        )

    Mode = field("Mode")
    SchedulingBufferTime = field("SchedulingBufferTime")
    MaxCapacityBreachBehavior = field("MaxCapacityBreachBehavior")
    MaxCapacityBuffer = field("MaxCapacityBuffer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredictiveScalingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictiveScalingConfigurationTypeDef"]
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

    AutoScalingGroupName = field("AutoScalingGroupName")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    DesiredCapacity = field("DesiredCapacity")
    DefaultCooldown = field("DefaultCooldown")
    AvailabilityZones = field("AvailabilityZones")
    HealthCheckType = field("HealthCheckType")
    CreatedTime = field("CreatedTime")
    AutoScalingGroupARN = field("AutoScalingGroupARN")
    LaunchConfigurationName = field("LaunchConfigurationName")

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    @cached_property
    def MixedInstancesPolicy(self):  # pragma: no cover
        return MixedInstancesPolicyOutput.make_one(
            self.boto3_raw_data["MixedInstancesPolicy"]
        )

    PredictedCapacity = field("PredictedCapacity")
    LoadBalancerNames = field("LoadBalancerNames")
    TargetGroupARNs = field("TargetGroupARNs")
    HealthCheckGracePeriod = field("HealthCheckGracePeriod")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def SuspendedProcesses(self):  # pragma: no cover
        return SuspendedProcess.make_many(self.boto3_raw_data["SuspendedProcesses"])

    PlacementGroup = field("PlacementGroup")
    VPCZoneIdentifier = field("VPCZoneIdentifier")

    @cached_property
    def EnabledMetrics(self):  # pragma: no cover
        return EnabledMetric.make_many(self.boto3_raw_data["EnabledMetrics"])

    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagDescription.make_many(self.boto3_raw_data["Tags"])

    TerminationPolicies = field("TerminationPolicies")
    NewInstancesProtectedFromScaleIn = field("NewInstancesProtectedFromScaleIn")
    ServiceLinkedRoleARN = field("ServiceLinkedRoleARN")
    MaxInstanceLifetime = field("MaxInstanceLifetime")
    CapacityRebalance = field("CapacityRebalance")

    @cached_property
    def WarmPoolConfiguration(self):  # pragma: no cover
        return WarmPoolConfiguration.make_one(
            self.boto3_raw_data["WarmPoolConfiguration"]
        )

    WarmPoolSize = field("WarmPoolSize")
    Context = field("Context")
    DesiredCapacityType = field("DesiredCapacityType")
    DefaultInstanceWarmup = field("DefaultInstanceWarmup")

    @cached_property
    def TrafficSources(self):  # pragma: no cover
        return TrafficSourceIdentifier.make_many(self.boto3_raw_data["TrafficSources"])

    @cached_property
    def InstanceMaintenancePolicy(self):  # pragma: no cover
        return InstanceMaintenancePolicy.make_one(
            self.boto3_raw_data["InstanceMaintenancePolicy"]
        )

    @cached_property
    def AvailabilityZoneDistribution(self):  # pragma: no cover
        return AvailabilityZoneDistribution.make_one(
            self.boto3_raw_data["AvailabilityZoneDistribution"]
        )

    @cached_property
    def AvailabilityZoneImpairmentPolicy(self):  # pragma: no cover
        return AvailabilityZoneImpairmentPolicy.make_one(
            self.boto3_raw_data["AvailabilityZoneImpairmentPolicy"]
        )

    @cached_property
    def CapacityReservationSpecification(self):  # pragma: no cover
        return CapacityReservationSpecificationOutput.make_one(
            self.boto3_raw_data["CapacityReservationSpecification"]
        )

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
class DesiredConfigurationOutput:
    boto3_raw_data: "type_defs.DesiredConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    @cached_property
    def MixedInstancesPolicy(self):  # pragma: no cover
        return MixedInstancesPolicyOutput.make_one(
            self.boto3_raw_data["MixedInstancesPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DesiredConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DesiredConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DesiredConfiguration:
    boto3_raw_data: "type_defs.DesiredConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    @cached_property
    def MixedInstancesPolicy(self):  # pragma: no cover
        return MixedInstancesPolicy.make_one(
            self.boto3_raw_data["MixedInstancesPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DesiredConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DesiredConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPredictiveScalingForecastAnswer:
    boto3_raw_data: "type_defs.GetPredictiveScalingForecastAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadForecast(self):  # pragma: no cover
        return LoadForecast.make_many(self.boto3_raw_data["LoadForecast"])

    @cached_property
    def CapacityForecast(self):  # pragma: no cover
        return CapacityForecast.make_one(self.boto3_raw_data["CapacityForecast"])

    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPredictiveScalingForecastAnswerTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPredictiveScalingForecastAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingPolicy:
    boto3_raw_data: "type_defs.ScalingPolicyTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    PolicyName = field("PolicyName")
    PolicyARN = field("PolicyARN")
    PolicyType = field("PolicyType")
    AdjustmentType = field("AdjustmentType")
    MinAdjustmentStep = field("MinAdjustmentStep")
    MinAdjustmentMagnitude = field("MinAdjustmentMagnitude")
    ScalingAdjustment = field("ScalingAdjustment")
    Cooldown = field("Cooldown")

    @cached_property
    def StepAdjustments(self):  # pragma: no cover
        return StepAdjustment.make_many(self.boto3_raw_data["StepAdjustments"])

    MetricAggregationType = field("MetricAggregationType")
    EstimatedInstanceWarmup = field("EstimatedInstanceWarmup")

    @cached_property
    def Alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["Alarms"])

    @cached_property
    def TargetTrackingConfiguration(self):  # pragma: no cover
        return TargetTrackingConfigurationOutput.make_one(
            self.boto3_raw_data["TargetTrackingConfiguration"]
        )

    Enabled = field("Enabled")

    @cached_property
    def PredictiveScalingConfiguration(self):  # pragma: no cover
        return PredictiveScalingConfigurationOutput.make_one(
            self.boto3_raw_data["PredictiveScalingConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupsType:
    boto3_raw_data: "type_defs.AutoScalingGroupsTypeTypeDef" = dataclasses.field()

    @cached_property
    def AutoScalingGroups(self):  # pragma: no cover
        return AutoScalingGroup.make_many(self.boto3_raw_data["AutoScalingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingGroupsTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupsTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceRefresh:
    boto3_raw_data: "type_defs.InstanceRefreshTypeDef" = dataclasses.field()

    InstanceRefreshId = field("InstanceRefreshId")
    AutoScalingGroupName = field("AutoScalingGroupName")
    Status = field("Status")
    StatusReason = field("StatusReason")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    PercentageComplete = field("PercentageComplete")
    InstancesToUpdate = field("InstancesToUpdate")

    @cached_property
    def ProgressDetails(self):  # pragma: no cover
        return InstanceRefreshProgressDetails.make_one(
            self.boto3_raw_data["ProgressDetails"]
        )

    @cached_property
    def Preferences(self):  # pragma: no cover
        return RefreshPreferencesOutput.make_one(self.boto3_raw_data["Preferences"])

    @cached_property
    def DesiredConfiguration(self):  # pragma: no cover
        return DesiredConfigurationOutput.make_one(
            self.boto3_raw_data["DesiredConfiguration"]
        )

    @cached_property
    def RollbackDetails(self):  # pragma: no cover
        return RollbackDetails.make_one(self.boto3_raw_data["RollbackDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceRefreshTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceRefreshTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutoScalingGroupType:
    boto3_raw_data: "type_defs.CreateAutoScalingGroupTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    LaunchConfigurationName = field("LaunchConfigurationName")

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    MixedInstancesPolicy = field("MixedInstancesPolicy")
    InstanceId = field("InstanceId")
    DesiredCapacity = field("DesiredCapacity")
    DefaultCooldown = field("DefaultCooldown")
    AvailabilityZones = field("AvailabilityZones")
    LoadBalancerNames = field("LoadBalancerNames")
    TargetGroupARNs = field("TargetGroupARNs")
    HealthCheckType = field("HealthCheckType")
    HealthCheckGracePeriod = field("HealthCheckGracePeriod")
    PlacementGroup = field("PlacementGroup")
    VPCZoneIdentifier = field("VPCZoneIdentifier")
    TerminationPolicies = field("TerminationPolicies")
    NewInstancesProtectedFromScaleIn = field("NewInstancesProtectedFromScaleIn")
    CapacityRebalance = field("CapacityRebalance")

    @cached_property
    def LifecycleHookSpecificationList(self):  # pragma: no cover
        return LifecycleHookSpecification.make_many(
            self.boto3_raw_data["LifecycleHookSpecificationList"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ServiceLinkedRoleARN = field("ServiceLinkedRoleARN")
    MaxInstanceLifetime = field("MaxInstanceLifetime")
    Context = field("Context")
    DesiredCapacityType = field("DesiredCapacityType")
    DefaultInstanceWarmup = field("DefaultInstanceWarmup")

    @cached_property
    def TrafficSources(self):  # pragma: no cover
        return TrafficSourceIdentifier.make_many(self.boto3_raw_data["TrafficSources"])

    @cached_property
    def InstanceMaintenancePolicy(self):  # pragma: no cover
        return InstanceMaintenancePolicy.make_one(
            self.boto3_raw_data["InstanceMaintenancePolicy"]
        )

    @cached_property
    def AvailabilityZoneDistribution(self):  # pragma: no cover
        return AvailabilityZoneDistribution.make_one(
            self.boto3_raw_data["AvailabilityZoneDistribution"]
        )

    @cached_property
    def AvailabilityZoneImpairmentPolicy(self):  # pragma: no cover
        return AvailabilityZoneImpairmentPolicy.make_one(
            self.boto3_raw_data["AvailabilityZoneImpairmentPolicy"]
        )

    SkipZonalShiftValidation = field("SkipZonalShiftValidation")
    CapacityReservationSpecification = field("CapacityReservationSpecification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAutoScalingGroupTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutoScalingGroupTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutoScalingGroupType:
    boto3_raw_data: "type_defs.UpdateAutoScalingGroupTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    LaunchConfigurationName = field("LaunchConfigurationName")

    @cached_property
    def LaunchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["LaunchTemplate"]
        )

    MixedInstancesPolicy = field("MixedInstancesPolicy")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    DesiredCapacity = field("DesiredCapacity")
    DefaultCooldown = field("DefaultCooldown")
    AvailabilityZones = field("AvailabilityZones")
    HealthCheckType = field("HealthCheckType")
    HealthCheckGracePeriod = field("HealthCheckGracePeriod")
    PlacementGroup = field("PlacementGroup")
    VPCZoneIdentifier = field("VPCZoneIdentifier")
    TerminationPolicies = field("TerminationPolicies")
    NewInstancesProtectedFromScaleIn = field("NewInstancesProtectedFromScaleIn")
    ServiceLinkedRoleARN = field("ServiceLinkedRoleARN")
    MaxInstanceLifetime = field("MaxInstanceLifetime")
    CapacityRebalance = field("CapacityRebalance")
    Context = field("Context")
    DesiredCapacityType = field("DesiredCapacityType")
    DefaultInstanceWarmup = field("DefaultInstanceWarmup")

    @cached_property
    def InstanceMaintenancePolicy(self):  # pragma: no cover
        return InstanceMaintenancePolicy.make_one(
            self.boto3_raw_data["InstanceMaintenancePolicy"]
        )

    @cached_property
    def AvailabilityZoneDistribution(self):  # pragma: no cover
        return AvailabilityZoneDistribution.make_one(
            self.boto3_raw_data["AvailabilityZoneDistribution"]
        )

    @cached_property
    def AvailabilityZoneImpairmentPolicy(self):  # pragma: no cover
        return AvailabilityZoneImpairmentPolicy.make_one(
            self.boto3_raw_data["AvailabilityZoneImpairmentPolicy"]
        )

    SkipZonalShiftValidation = field("SkipZonalShiftValidation")
    CapacityReservationSpecification = field("CapacityReservationSpecification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAutoScalingGroupTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutoScalingGroupTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoliciesType:
    boto3_raw_data: "type_defs.PoliciesTypeTypeDef" = dataclasses.field()

    @cached_property
    def ScalingPolicies(self):  # pragma: no cover
        return ScalingPolicy.make_many(self.boto3_raw_data["ScalingPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoliciesTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoliciesTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutScalingPolicyType:
    boto3_raw_data: "type_defs.PutScalingPolicyTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    PolicyName = field("PolicyName")
    PolicyType = field("PolicyType")
    AdjustmentType = field("AdjustmentType")
    MinAdjustmentStep = field("MinAdjustmentStep")
    MinAdjustmentMagnitude = field("MinAdjustmentMagnitude")
    ScalingAdjustment = field("ScalingAdjustment")
    Cooldown = field("Cooldown")
    MetricAggregationType = field("MetricAggregationType")

    @cached_property
    def StepAdjustments(self):  # pragma: no cover
        return StepAdjustment.make_many(self.boto3_raw_data["StepAdjustments"])

    EstimatedInstanceWarmup = field("EstimatedInstanceWarmup")
    TargetTrackingConfiguration = field("TargetTrackingConfiguration")
    Enabled = field("Enabled")
    PredictiveScalingConfiguration = field("PredictiveScalingConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutScalingPolicyTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutScalingPolicyTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceRefreshesAnswer:
    boto3_raw_data: "type_defs.DescribeInstanceRefreshesAnswerTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceRefreshes(self):  # pragma: no cover
        return InstanceRefresh.make_many(self.boto3_raw_data["InstanceRefreshes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstanceRefreshesAnswerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceRefreshesAnswerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInstanceRefreshType:
    boto3_raw_data: "type_defs.StartInstanceRefreshTypeTypeDef" = dataclasses.field()

    AutoScalingGroupName = field("AutoScalingGroupName")
    Strategy = field("Strategy")
    DesiredConfiguration = field("DesiredConfiguration")
    Preferences = field("Preferences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInstanceRefreshTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInstanceRefreshTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
