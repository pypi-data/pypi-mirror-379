# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_emr import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class ApplicationOutput:
    boto3_raw_data: "type_defs.ApplicationOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")
    Args = field("Args")
    AdditionalInfo = field("AdditionalInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Application:
    boto3_raw_data: "type_defs.ApplicationTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")
    Args = field("Args")
    AdditionalInfo = field("AdditionalInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConstraints:
    boto3_raw_data: "type_defs.ScalingConstraintsTypeDef" = dataclasses.field()

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingPolicyStateChangeReason:
    boto3_raw_data: "type_defs.AutoScalingPolicyStateChangeReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingPolicyStateChangeReasonTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingPolicyStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTerminationPolicy:
    boto3_raw_data: "type_defs.AutoTerminationPolicyTypeDef" = dataclasses.field()

    IdleTimeout = field("IdleTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTerminationPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTerminationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockPublicAccessConfigurationMetadata:
    boto3_raw_data: "type_defs.BlockPublicAccessConfigurationMetadataTypeDef" = (
        dataclasses.field()
    )

    CreationDateTime = field("CreationDateTime")
    CreatedByArn = field("CreatedByArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BlockPublicAccessConfigurationMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockPublicAccessConfigurationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortRange:
    boto3_raw_data: "type_defs.PortRangeTypeDef" = dataclasses.field()

    MinRange = field("MinRange")
    MaxRange = field("MaxRange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScriptBootstrapActionConfigOutput:
    boto3_raw_data: "type_defs.ScriptBootstrapActionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Path = field("Path")
    Args = field("Args")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScriptBootstrapActionConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScriptBootstrapActionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelStepsInfo:
    boto3_raw_data: "type_defs.CancelStepsInfoTypeDef" = dataclasses.field()

    StepId = field("StepId")
    Status = field("Status")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelStepsInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CancelStepsInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelStepsInput:
    boto3_raw_data: "type_defs.CancelStepsInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    StepIds = field("StepIds")
    StepCancellationOption = field("StepCancellationOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelStepsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelStepsInputTypeDef"]
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

    Key = field("Key")
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
class ClusterStateChangeReason:
    boto3_raw_data: "type_defs.ClusterStateChangeReasonTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterStateChangeReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterTimeline:
    boto3_raw_data: "type_defs.ClusterTimelineTypeDef" = dataclasses.field()

    CreationDateTime = field("CreationDateTime")
    ReadyDateTime = field("ReadyDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTimelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTimelineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorData = field("ErrorData")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOutput:
    boto3_raw_data: "type_defs.ConfigurationOutputTypeDef" = dataclasses.field()

    Classification = field("Classification")
    Configurations = field("Configurations")
    Properties = field("Properties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2InstanceAttributes:
    boto3_raw_data: "type_defs.Ec2InstanceAttributesTypeDef" = dataclasses.field()

    Ec2KeyName = field("Ec2KeyName")
    Ec2SubnetId = field("Ec2SubnetId")
    RequestedEc2SubnetIds = field("RequestedEc2SubnetIds")
    Ec2AvailabilityZone = field("Ec2AvailabilityZone")
    RequestedEc2AvailabilityZones = field("RequestedEc2AvailabilityZones")
    IamInstanceProfile = field("IamInstanceProfile")
    EmrManagedMasterSecurityGroup = field("EmrManagedMasterSecurityGroup")
    EmrManagedSlaveSecurityGroup = field("EmrManagedSlaveSecurityGroup")
    ServiceAccessSecurityGroup = field("ServiceAccessSecurityGroup")
    AdditionalMasterSecurityGroups = field("AdditionalMasterSecurityGroups")
    AdditionalSlaveSecurityGroups = field("AdditionalSlaveSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2InstanceAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2InstanceAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KerberosAttributes:
    boto3_raw_data: "type_defs.KerberosAttributesTypeDef" = dataclasses.field()

    Realm = field("Realm")
    KdcAdminPassword = field("KdcAdminPassword")
    CrossRealmTrustPrincipalPassword = field("CrossRealmTrustPrincipalPassword")
    ADDomainJoinUser = field("ADDomainJoinUser")
    ADDomainJoinPassword = field("ADDomainJoinPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KerberosAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KerberosAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementGroupConfig:
    boto3_raw_data: "type_defs.PlacementGroupConfigTypeDef" = dataclasses.field()

    InstanceRole = field("InstanceRole")
    PlacementStrategy = field("PlacementStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlacementGroupConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementGroupConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Command:
    boto3_raw_data: "type_defs.CommandTypeDef" = dataclasses.field()

    Name = field("Name")
    ScriptPath = field("ScriptPath")
    Args = field("Args")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommandTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeLimits:
    boto3_raw_data: "type_defs.ComputeLimitsTypeDef" = dataclasses.field()

    UnitType = field("UnitType")
    MinimumCapacityUnits = field("MinimumCapacityUnits")
    MaximumCapacityUnits = field("MaximumCapacityUnits")
    MaximumOnDemandCapacityUnits = field("MaximumOnDemandCapacityUnits")
    MaximumCoreCapacityUnits = field("MaximumCoreCapacityUnits")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationPaginator:
    boto3_raw_data: "type_defs.ConfigurationPaginatorTypeDef" = dataclasses.field()

    Classification = field("Classification")
    Configurations = field("Configurations")
    Properties = field("Properties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    Classification = field("Classification")
    Configurations = field("Configurations")
    Properties = field("Properties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EMRContainersConfig:
    boto3_raw_data: "type_defs.EMRContainersConfigTypeDef" = dataclasses.field()

    JobRunId = field("JobRunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EMRContainersConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EMRContainersConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityConfigurationInput:
    boto3_raw_data: "type_defs.CreateSecurityConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SecurityConfiguration = field("SecurityConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSecurityConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStudioSessionMappingInput:
    boto3_raw_data: "type_defs.CreateStudioSessionMappingInputTypeDef" = (
        dataclasses.field()
    )

    StudioId = field("StudioId")
    IdentityType = field("IdentityType")
    SessionPolicyArn = field("SessionPolicyArn")
    IdentityId = field("IdentityId")
    IdentityName = field("IdentityName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStudioSessionMappingInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStudioSessionMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsernamePassword:
    boto3_raw_data: "type_defs.UsernamePasswordTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsernamePasswordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsernamePasswordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSecurityConfigurationInput:
    boto3_raw_data: "type_defs.DeleteSecurityConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSecurityConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSecurityConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStudioInput:
    boto3_raw_data: "type_defs.DeleteStudioInputTypeDef" = dataclasses.field()

    StudioId = field("StudioId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteStudioInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStudioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStudioSessionMappingInput:
    boto3_raw_data: "type_defs.DeleteStudioSessionMappingInputTypeDef" = (
        dataclasses.field()
    )

    StudioId = field("StudioId")
    IdentityType = field("IdentityType")
    IdentityId = field("IdentityId")
    IdentityName = field("IdentityName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteStudioSessionMappingInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStudioSessionMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterInput:
    boto3_raw_data: "type_defs.DescribeClusterInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterInputTypeDef"]
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
class DescribeNotebookExecutionInput:
    boto3_raw_data: "type_defs.DescribeNotebookExecutionInputTypeDef" = (
        dataclasses.field()
    )

    NotebookExecutionId = field("NotebookExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeNotebookExecutionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotebookExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePersistentAppUIInput:
    boto3_raw_data: "type_defs.DescribePersistentAppUIInputTypeDef" = (
        dataclasses.field()
    )

    PersistentAppUIId = field("PersistentAppUIId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePersistentAppUIInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePersistentAppUIInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReleaseLabelInput:
    boto3_raw_data: "type_defs.DescribeReleaseLabelInputTypeDef" = dataclasses.field()

    ReleaseLabel = field("ReleaseLabel")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReleaseLabelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReleaseLabelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OSRelease:
    boto3_raw_data: "type_defs.OSReleaseTypeDef" = dataclasses.field()

    Label = field("Label")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OSReleaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OSReleaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimplifiedApplication:
    boto3_raw_data: "type_defs.SimplifiedApplicationTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimplifiedApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimplifiedApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityConfigurationInput:
    boto3_raw_data: "type_defs.DescribeSecurityConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSecurityConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStepInput:
    boto3_raw_data: "type_defs.DescribeStepInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    StepId = field("StepId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeStepInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStudioInput:
    boto3_raw_data: "type_defs.DescribeStudioInputTypeDef" = dataclasses.field()

    StudioId = field("StudioId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStudioInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStudioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeSpecification:
    boto3_raw_data: "type_defs.VolumeSpecificationTypeDef" = dataclasses.field()

    VolumeType = field("VolumeType")
    SizeInGB = field("SizeInGB")
    Iops = field("Iops")
    Throughput = field("Throughput")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VolumeSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VolumeSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsVolume:
    boto3_raw_data: "type_defs.EbsVolumeTypeDef" = dataclasses.field()

    Device = field("Device")
    VolumeId = field("VolumeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EbsVolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionEngineConfig:
    boto3_raw_data: "type_defs.ExecutionEngineConfigTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    MasterInstanceSecurityGroupId = field("MasterInstanceSecurityGroupId")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionEngineConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionEngineConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureDetails:
    boto3_raw_data: "type_defs.FailureDetailsTypeDef" = dataclasses.field()

    Reason = field("Reason")
    Message = field("Message")
    LogFile = field("LogFile")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoTerminationPolicyInput:
    boto3_raw_data: "type_defs.GetAutoTerminationPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAutoTerminationPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoTerminationPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterSessionCredentialsInput:
    boto3_raw_data: "type_defs.GetClusterSessionCredentialsInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetClusterSessionCredentialsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterSessionCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedScalingPolicyInput:
    boto3_raw_data: "type_defs.GetManagedScalingPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetManagedScalingPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOnClusterAppUIPresignedURLInput:
    boto3_raw_data: "type_defs.GetOnClusterAppUIPresignedURLInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    OnClusterAppUIType = field("OnClusterAppUIType")
    ApplicationId = field("ApplicationId")
    DryRun = field("DryRun")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOnClusterAppUIPresignedURLInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOnClusterAppUIPresignedURLInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersistentAppUIPresignedURLInput:
    boto3_raw_data: "type_defs.GetPersistentAppUIPresignedURLInputTypeDef" = (
        dataclasses.field()
    )

    PersistentAppUIId = field("PersistentAppUIId")
    PersistentAppUIType = field("PersistentAppUIType")
    ApplicationId = field("ApplicationId")
    AuthProxyCall = field("AuthProxyCall")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPersistentAppUIPresignedURLInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersistentAppUIPresignedURLInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStudioSessionMappingInput:
    boto3_raw_data: "type_defs.GetStudioSessionMappingInputTypeDef" = (
        dataclasses.field()
    )

    StudioId = field("StudioId")
    IdentityType = field("IdentityType")
    IdentityId = field("IdentityId")
    IdentityName = field("IdentityName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStudioSessionMappingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStudioSessionMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionMappingDetail:
    boto3_raw_data: "type_defs.SessionMappingDetailTypeDef" = dataclasses.field()

    StudioId = field("StudioId")
    IdentityId = field("IdentityId")
    IdentityName = field("IdentityName")
    IdentityType = field("IdentityType")
    SessionPolicyArn = field("SessionPolicyArn")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionMappingDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionMappingDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValue:
    boto3_raw_data: "type_defs.KeyValueTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HadoopStepConfig:
    boto3_raw_data: "type_defs.HadoopStepConfigTypeDef" = dataclasses.field()

    Jar = field("Jar")
    Properties = field("Properties")
    MainClass = field("MainClass")
    Args = field("Args")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HadoopStepConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HadoopStepConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpotProvisioningSpecification:
    boto3_raw_data: "type_defs.SpotProvisioningSpecificationTypeDef" = (
        dataclasses.field()
    )

    TimeoutDurationMinutes = field("TimeoutDurationMinutes")
    TimeoutAction = field("TimeoutAction")
    BlockDurationMinutes = field("BlockDurationMinutes")
    AllocationStrategy = field("AllocationStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SpotProvisioningSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpotProvisioningSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpotResizingSpecification:
    boto3_raw_data: "type_defs.SpotResizingSpecificationTypeDef" = dataclasses.field()

    TimeoutDurationMinutes = field("TimeoutDurationMinutes")
    AllocationStrategy = field("AllocationStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpotResizingSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpotResizingSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetStateChangeReason:
    boto3_raw_data: "type_defs.InstanceFleetStateChangeReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceFleetStateChangeReasonTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetTimeline:
    boto3_raw_data: "type_defs.InstanceFleetTimelineTypeDef" = dataclasses.field()

    CreationDateTime = field("CreationDateTime")
    ReadyDateTime = field("ReadyDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceFleetTimelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetTimelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupDetail:
    boto3_raw_data: "type_defs.InstanceGroupDetailTypeDef" = dataclasses.field()

    Market = field("Market")
    InstanceRole = field("InstanceRole")
    InstanceType = field("InstanceType")
    InstanceRequestCount = field("InstanceRequestCount")
    InstanceRunningCount = field("InstanceRunningCount")
    State = field("State")
    CreationDateTime = field("CreationDateTime")
    InstanceGroupId = field("InstanceGroupId")
    Name = field("Name")
    BidPrice = field("BidPrice")
    LastStateChangeReason = field("LastStateChangeReason")
    StartDateTime = field("StartDateTime")
    ReadyDateTime = field("ReadyDateTime")
    EndDateTime = field("EndDateTime")
    CustomAmiId = field("CustomAmiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupStateChangeReason:
    boto3_raw_data: "type_defs.InstanceGroupStateChangeReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceGroupStateChangeReasonTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupTimeline:
    boto3_raw_data: "type_defs.InstanceGroupTimelineTypeDef" = dataclasses.field()

    CreationDateTime = field("CreationDateTime")
    ReadyDateTime = field("ReadyDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupTimelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupTimelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceResizePolicyOutput:
    boto3_raw_data: "type_defs.InstanceResizePolicyOutputTypeDef" = dataclasses.field()

    InstancesToTerminate = field("InstancesToTerminate")
    InstancesToProtect = field("InstancesToProtect")
    InstanceTerminationTimeout = field("InstanceTerminationTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceResizePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceResizePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceResizePolicy:
    boto3_raw_data: "type_defs.InstanceResizePolicyTypeDef" = dataclasses.field()

    InstancesToTerminate = field("InstancesToTerminate")
    InstancesToProtect = field("InstancesToProtect")
    InstanceTerminationTimeout = field("InstanceTerminationTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceResizePolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceResizePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceStateChangeReason:
    boto3_raw_data: "type_defs.InstanceStateChangeReasonTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceStateChangeReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTimeline:
    boto3_raw_data: "type_defs.InstanceTimelineTypeDef" = dataclasses.field()

    CreationDateTime = field("CreationDateTime")
    ReadyDateTime = field("ReadyDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTimelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTimelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobFlowExecutionStatusDetail:
    boto3_raw_data: "type_defs.JobFlowExecutionStatusDetailTypeDef" = (
        dataclasses.field()
    )

    State = field("State")
    CreationDateTime = field("CreationDateTime")
    StartDateTime = field("StartDateTime")
    ReadyDateTime = field("ReadyDateTime")
    EndDateTime = field("EndDateTime")
    LastStateChangeReason = field("LastStateChangeReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobFlowExecutionStatusDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobFlowExecutionStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementTypeOutput:
    boto3_raw_data: "type_defs.PlacementTypeOutputTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    AvailabilityZones = field("AvailabilityZones")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlacementTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementTypeOutputTypeDef"]
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
class ListBootstrapActionsInput:
    boto3_raw_data: "type_defs.ListBootstrapActionsInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBootstrapActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBootstrapActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceFleetsInput:
    boto3_raw_data: "type_defs.ListInstanceFleetsInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceFleetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceFleetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceGroupsInput:
    boto3_raw_data: "type_defs.ListInstanceGroupsInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesInput:
    boto3_raw_data: "type_defs.ListInstancesInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    InstanceGroupId = field("InstanceGroupId")
    InstanceGroupTypes = field("InstanceGroupTypes")
    InstanceFleetId = field("InstanceFleetId")
    InstanceFleetType = field("InstanceFleetType")
    InstanceStates = field("InstanceStates")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseLabelFilter:
    boto3_raw_data: "type_defs.ReleaseLabelFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")
    Application = field("Application")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleaseLabelFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseLabelFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigurationsInput:
    boto3_raw_data: "type_defs.ListSecurityConfigurationsInputTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSecurityConfigurationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigurationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityConfigurationSummary:
    boto3_raw_data: "type_defs.SecurityConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    CreationDateTime = field("CreationDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepsInput:
    boto3_raw_data: "type_defs.ListStepsInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    StepStates = field("StepStates")
    StepIds = field("StepIds")
    Marker = field("Marker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStepsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListStepsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStudioSessionMappingsInput:
    boto3_raw_data: "type_defs.ListStudioSessionMappingsInputTypeDef" = (
        dataclasses.field()
    )

    StudioId = field("StudioId")
    IdentityType = field("IdentityType")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStudioSessionMappingsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStudioSessionMappingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionMappingSummary:
    boto3_raw_data: "type_defs.SessionMappingSummaryTypeDef" = dataclasses.field()

    StudioId = field("StudioId")
    IdentityId = field("IdentityId")
    IdentityName = field("IdentityName")
    IdentityType = field("IdentityType")
    SessionPolicyArn = field("SessionPolicyArn")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionMappingSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionMappingSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStudiosInput:
    boto3_raw_data: "type_defs.ListStudiosInputTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStudiosInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStudiosInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StudioSummary:
    boto3_raw_data: "type_defs.StudioSummaryTypeDef" = dataclasses.field()

    StudioId = field("StudioId")
    Name = field("Name")
    VpcId = field("VpcId")
    Description = field("Description")
    Url = field("Url")
    AuthMode = field("AuthMode")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StudioSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StudioSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupportedInstanceTypesInput:
    boto3_raw_data: "type_defs.ListSupportedInstanceTypesInputTypeDef" = (
        dataclasses.field()
    )

    ReleaseLabel = field("ReleaseLabel")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSupportedInstanceTypesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupportedInstanceTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedInstanceType:
    boto3_raw_data: "type_defs.SupportedInstanceTypeTypeDef" = dataclasses.field()

    Type = field("Type")
    MemoryGB = field("MemoryGB")
    StorageGB = field("StorageGB")
    VCPU = field("VCPU")
    Is64BitsOnly = field("Is64BitsOnly")
    InstanceFamilyId = field("InstanceFamilyId")
    EbsOptimizedAvailable = field("EbsOptimizedAvailable")
    EbsOptimizedByDefault = field("EbsOptimizedByDefault")
    NumberOfDisks = field("NumberOfDisks")
    EbsStorageOnly = field("EbsStorageOnly")
    Architecture = field("Architecture")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedInstanceTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedInstanceTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterInput:
    boto3_raw_data: "type_defs.ModifyClusterInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    StepConcurrencyLevel = field("StepConcurrencyLevel")
    ExtendedSupport = field("ExtendedSupport")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotebookS3LocationForOutput:
    boto3_raw_data: "type_defs.NotebookS3LocationForOutputTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotebookS3LocationForOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotebookS3LocationForOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputNotebookS3LocationForOutput:
    boto3_raw_data: "type_defs.OutputNotebookS3LocationForOutputTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OutputNotebookS3LocationForOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputNotebookS3LocationForOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotebookS3LocationFromInput:
    boto3_raw_data: "type_defs.NotebookS3LocationFromInputTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotebookS3LocationFromInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotebookS3LocationFromInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnDemandCapacityReservationOptions:
    boto3_raw_data: "type_defs.OnDemandCapacityReservationOptionsTypeDef" = (
        dataclasses.field()
    )

    UsageStrategy = field("UsageStrategy")
    CapacityReservationPreference = field("CapacityReservationPreference")
    CapacityReservationResourceGroupArn = field("CapacityReservationResourceGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OnDemandCapacityReservationOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnDemandCapacityReservationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputNotebookS3LocationFromInput:
    boto3_raw_data: "type_defs.OutputNotebookS3LocationFromInputTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OutputNotebookS3LocationFromInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputNotebookS3LocationFromInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementType:
    boto3_raw_data: "type_defs.PlacementTypeTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    AvailabilityZones = field("AvailabilityZones")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlacementTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlacementTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAutoScalingPolicyInput:
    boto3_raw_data: "type_defs.RemoveAutoScalingPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")
    InstanceGroupId = field("InstanceGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAutoScalingPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAutoScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAutoTerminationPolicyInput:
    boto3_raw_data: "type_defs.RemoveAutoTerminationPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveAutoTerminationPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAutoTerminationPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveManagedScalingPolicyInput:
    boto3_raw_data: "type_defs.RemoveManagedScalingPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveManagedScalingPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveManagedScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsInput:
    boto3_raw_data: "type_defs.RemoveTagsInputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemoveTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedProductConfig:
    boto3_raw_data: "type_defs.SupportedProductConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    Args = field("Args")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedProductConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedProductConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleScalingPolicyConfiguration:
    boto3_raw_data: "type_defs.SimpleScalingPolicyConfigurationTypeDef" = (
        dataclasses.field()
    )

    ScalingAdjustment = field("ScalingAdjustment")
    AdjustmentType = field("AdjustmentType")
    CoolDown = field("CoolDown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SimpleScalingPolicyConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimpleScalingPolicyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScriptBootstrapActionConfig:
    boto3_raw_data: "type_defs.ScriptBootstrapActionConfigTypeDef" = dataclasses.field()

    Path = field("Path")
    Args = field("Args")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScriptBootstrapActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScriptBootstrapActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetKeepJobFlowAliveWhenNoStepsInput:
    boto3_raw_data: "type_defs.SetKeepJobFlowAliveWhenNoStepsInputTypeDef" = (
        dataclasses.field()
    )

    JobFlowIds = field("JobFlowIds")
    KeepJobFlowAliveWhenNoSteps = field("KeepJobFlowAliveWhenNoSteps")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetKeepJobFlowAliveWhenNoStepsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetKeepJobFlowAliveWhenNoStepsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTerminationProtectionInput:
    boto3_raw_data: "type_defs.SetTerminationProtectionInputTypeDef" = (
        dataclasses.field()
    )

    JobFlowIds = field("JobFlowIds")
    TerminationProtected = field("TerminationProtected")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetTerminationProtectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTerminationProtectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetUnhealthyNodeReplacementInput:
    boto3_raw_data: "type_defs.SetUnhealthyNodeReplacementInputTypeDef" = (
        dataclasses.field()
    )

    JobFlowIds = field("JobFlowIds")
    UnhealthyNodeReplacement = field("UnhealthyNodeReplacement")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetUnhealthyNodeReplacementInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetUnhealthyNodeReplacementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVisibleToAllUsersInput:
    boto3_raw_data: "type_defs.SetVisibleToAllUsersInputTypeDef" = dataclasses.field()

    JobFlowIds = field("JobFlowIds")
    VisibleToAllUsers = field("VisibleToAllUsers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetVisibleToAllUsersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVisibleToAllUsersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepExecutionStatusDetail:
    boto3_raw_data: "type_defs.StepExecutionStatusDetailTypeDef" = dataclasses.field()

    State = field("State")
    CreationDateTime = field("CreationDateTime")
    StartDateTime = field("StartDateTime")
    EndDateTime = field("EndDateTime")
    LastStateChangeReason = field("LastStateChangeReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepExecutionStatusDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepExecutionStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepStateChangeReason:
    boto3_raw_data: "type_defs.StepStateChangeReasonTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepStateChangeReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepTimeline:
    boto3_raw_data: "type_defs.StepTimelineTypeDef" = dataclasses.field()

    CreationDateTime = field("CreationDateTime")
    StartDateTime = field("StartDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepTimelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepTimelineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopNotebookExecutionInput:
    boto3_raw_data: "type_defs.StopNotebookExecutionInputTypeDef" = dataclasses.field()

    NotebookExecutionId = field("NotebookExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopNotebookExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopNotebookExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateJobFlowsInput:
    boto3_raw_data: "type_defs.TerminateJobFlowsInputTypeDef" = dataclasses.field()

    JobFlowIds = field("JobFlowIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateJobFlowsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateJobFlowsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStudioInput:
    boto3_raw_data: "type_defs.UpdateStudioInputTypeDef" = dataclasses.field()

    StudioId = field("StudioId")
    Name = field("Name")
    Description = field("Description")
    SubnetIds = field("SubnetIds")
    DefaultS3Location = field("DefaultS3Location")
    EncryptionKeyArn = field("EncryptionKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateStudioInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStudioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStudioSessionMappingInput:
    boto3_raw_data: "type_defs.UpdateStudioSessionMappingInputTypeDef" = (
        dataclasses.field()
    )

    StudioId = field("StudioId")
    IdentityType = field("IdentityType")
    SessionPolicyArn = field("SessionPolicyArn")
    IdentityId = field("IdentityId")
    IdentityName = field("IdentityName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateStudioSessionMappingInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStudioSessionMappingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddInstanceFleetOutput:
    boto3_raw_data: "type_defs.AddInstanceFleetOutputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    InstanceFleetId = field("InstanceFleetId")
    ClusterArn = field("ClusterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddInstanceFleetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddInstanceFleetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddInstanceGroupsOutput:
    boto3_raw_data: "type_defs.AddInstanceGroupsOutputTypeDef" = dataclasses.field()

    JobFlowId = field("JobFlowId")
    InstanceGroupIds = field("InstanceGroupIds")
    ClusterArn = field("ClusterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddInstanceGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddInstanceGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddJobFlowStepsOutput:
    boto3_raw_data: "type_defs.AddJobFlowStepsOutputTypeDef" = dataclasses.field()

    StepIds = field("StepIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddJobFlowStepsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddJobFlowStepsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePersistentAppUIOutput:
    boto3_raw_data: "type_defs.CreatePersistentAppUIOutputTypeDef" = dataclasses.field()

    PersistentAppUIId = field("PersistentAppUIId")
    RuntimeRoleEnabledCluster = field("RuntimeRoleEnabledCluster")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePersistentAppUIOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePersistentAppUIOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityConfigurationOutput:
    boto3_raw_data: "type_defs.CreateSecurityConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    CreationDateTime = field("CreationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSecurityConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStudioOutput:
    boto3_raw_data: "type_defs.CreateStudioOutputTypeDef" = dataclasses.field()

    StudioId = field("StudioId")
    Url = field("Url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStudioOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStudioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeSecurityConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SecurityConfiguration = field("SecurityConfiguration")
    CreationDateTime = field("CreationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSecurityConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityConfigurationOutputTypeDef"]
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
class GetOnClusterAppUIPresignedURLOutput:
    boto3_raw_data: "type_defs.GetOnClusterAppUIPresignedURLOutputTypeDef" = (
        dataclasses.field()
    )

    PresignedURLReady = field("PresignedURLReady")
    PresignedURL = field("PresignedURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOnClusterAppUIPresignedURLOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOnClusterAppUIPresignedURLOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersistentAppUIPresignedURLOutput:
    boto3_raw_data: "type_defs.GetPersistentAppUIPresignedURLOutputTypeDef" = (
        dataclasses.field()
    )

    PresignedURLReady = field("PresignedURLReady")
    PresignedURL = field("PresignedURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPersistentAppUIPresignedURLOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersistentAppUIPresignedURLOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReleaseLabelsOutput:
    boto3_raw_data: "type_defs.ListReleaseLabelsOutputTypeDef" = dataclasses.field()

    ReleaseLabels = field("ReleaseLabels")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReleaseLabelsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReleaseLabelsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterOutput:
    boto3_raw_data: "type_defs.ModifyClusterOutputTypeDef" = dataclasses.field()

    StepConcurrencyLevel = field("StepConcurrencyLevel")
    ExtendedSupport = field("ExtendedSupport")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunJobFlowOutput:
    boto3_raw_data: "type_defs.RunJobFlowOutputTypeDef" = dataclasses.field()

    JobFlowId = field("JobFlowId")
    ClusterArn = field("ClusterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunJobFlowOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunJobFlowOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartNotebookExecutionOutput:
    boto3_raw_data: "type_defs.StartNotebookExecutionOutputTypeDef" = (
        dataclasses.field()
    )

    NotebookExecutionId = field("NotebookExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartNotebookExecutionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartNotebookExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsInput:
    boto3_raw_data: "type_defs.AddTagsInputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStudioInput:
    boto3_raw_data: "type_defs.CreateStudioInputTypeDef" = dataclasses.field()

    Name = field("Name")
    AuthMode = field("AuthMode")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    ServiceRole = field("ServiceRole")
    WorkspaceSecurityGroupId = field("WorkspaceSecurityGroupId")
    EngineSecurityGroupId = field("EngineSecurityGroupId")
    DefaultS3Location = field("DefaultS3Location")
    Description = field("Description")
    UserRole = field("UserRole")
    IdpAuthUrl = field("IdpAuthUrl")
    IdpRelayStateParameterName = field("IdpRelayStateParameterName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TrustedIdentityPropagationEnabled = field("TrustedIdentityPropagationEnabled")
    IdcUserAssignment = field("IdcUserAssignment")
    IdcInstanceArn = field("IdcInstanceArn")
    EncryptionKeyArn = field("EncryptionKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStudioInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStudioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersistentAppUI:
    boto3_raw_data: "type_defs.PersistentAppUITypeDef" = dataclasses.field()

    PersistentAppUIId = field("PersistentAppUIId")
    PersistentAppUITypeList = field("PersistentAppUITypeList")
    PersistentAppUIStatus = field("PersistentAppUIStatus")
    AuthorId = field("AuthorId")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LastStateChangeReason = field("LastStateChangeReason")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PersistentAppUITypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PersistentAppUITypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Studio:
    boto3_raw_data: "type_defs.StudioTypeDef" = dataclasses.field()

    StudioId = field("StudioId")
    StudioArn = field("StudioArn")
    Name = field("Name")
    Description = field("Description")
    AuthMode = field("AuthMode")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    ServiceRole = field("ServiceRole")
    UserRole = field("UserRole")
    WorkspaceSecurityGroupId = field("WorkspaceSecurityGroupId")
    EngineSecurityGroupId = field("EngineSecurityGroupId")
    Url = field("Url")
    CreationTime = field("CreationTime")
    DefaultS3Location = field("DefaultS3Location")
    IdpAuthUrl = field("IdpAuthUrl")
    IdpRelayStateParameterName = field("IdpRelayStateParameterName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IdcInstanceArn = field("IdcInstanceArn")
    TrustedIdentityPropagationEnabled = field("TrustedIdentityPropagationEnabled")
    IdcUserAssignment = field("IdcUserAssignment")
    EncryptionKeyArn = field("EncryptionKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StudioTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StudioTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingPolicyStatus:
    boto3_raw_data: "type_defs.AutoScalingPolicyStatusTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return AutoScalingPolicyStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingPolicyStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingPolicyStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoTerminationPolicyOutput:
    boto3_raw_data: "type_defs.GetAutoTerminationPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoTerminationPolicy(self):  # pragma: no cover
        return AutoTerminationPolicy.make_one(
            self.boto3_raw_data["AutoTerminationPolicy"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAutoTerminationPolicyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoTerminationPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAutoTerminationPolicyInput:
    boto3_raw_data: "type_defs.PutAutoTerminationPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def AutoTerminationPolicy(self):  # pragma: no cover
        return AutoTerminationPolicy.make_one(
            self.boto3_raw_data["AutoTerminationPolicy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAutoTerminationPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAutoTerminationPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockPublicAccessConfigurationOutput:
    boto3_raw_data: "type_defs.BlockPublicAccessConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    BlockPublicSecurityGroupRules = field("BlockPublicSecurityGroupRules")

    @cached_property
    def PermittedPublicSecurityGroupRuleRanges(self):  # pragma: no cover
        return PortRange.make_many(
            self.boto3_raw_data["PermittedPublicSecurityGroupRuleRanges"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BlockPublicAccessConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockPublicAccessConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockPublicAccessConfiguration:
    boto3_raw_data: "type_defs.BlockPublicAccessConfigurationTypeDef" = (
        dataclasses.field()
    )

    BlockPublicSecurityGroupRules = field("BlockPublicSecurityGroupRules")

    @cached_property
    def PermittedPublicSecurityGroupRuleRanges(self):  # pragma: no cover
        return PortRange.make_many(
            self.boto3_raw_data["PermittedPublicSecurityGroupRuleRanges"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BlockPublicAccessConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockPublicAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BootstrapActionConfigOutput:
    boto3_raw_data: "type_defs.BootstrapActionConfigOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ScriptBootstrapAction(self):  # pragma: no cover
        return ScriptBootstrapActionConfigOutput.make_one(
            self.boto3_raw_data["ScriptBootstrapAction"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BootstrapActionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BootstrapActionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelStepsOutput:
    boto3_raw_data: "type_defs.CancelStepsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CancelStepsInfoList(self):  # pragma: no cover
        return CancelStepsInfo.make_many(self.boto3_raw_data["CancelStepsInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelStepsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelStepsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchAlarmDefinitionOutput:
    boto3_raw_data: "type_defs.CloudWatchAlarmDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    ComparisonOperator = field("ComparisonOperator")
    MetricName = field("MetricName")
    Period = field("Period")
    Threshold = field("Threshold")
    EvaluationPeriods = field("EvaluationPeriods")
    Namespace = field("Namespace")
    Statistic = field("Statistic")
    Unit = field("Unit")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchAlarmDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchAlarmDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchAlarmDefinition:
    boto3_raw_data: "type_defs.CloudWatchAlarmDefinitionTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    MetricName = field("MetricName")
    Period = field("Period")
    Threshold = field("Threshold")
    EvaluationPeriods = field("EvaluationPeriods")
    Namespace = field("Namespace")
    Statistic = field("Statistic")
    Unit = field("Unit")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return MetricDimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchAlarmDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchAlarmDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterStatus:
    boto3_raw_data: "type_defs.ClusterStatusTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return ClusterStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    @cached_property
    def Timeline(self):  # pragma: no cover
        return ClusterTimeline.make_one(self.boto3_raw_data["Timeline"])

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["ErrorDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBootstrapActionsOutput:
    boto3_raw_data: "type_defs.ListBootstrapActionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def BootstrapActions(self):  # pragma: no cover
        return Command.make_many(self.boto3_raw_data["BootstrapActions"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBootstrapActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBootstrapActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedScalingPolicy:
    boto3_raw_data: "type_defs.ManagedScalingPolicyTypeDef" = dataclasses.field()

    @cached_property
    def ComputeLimits(self):  # pragma: no cover
        return ComputeLimits.make_one(self.boto3_raw_data["ComputeLimits"])

    UtilizationPerformanceIndex = field("UtilizationPerformanceIndex")
    ScalingStrategy = field("ScalingStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedScalingPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedScalingPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePersistentAppUIInput:
    boto3_raw_data: "type_defs.CreatePersistentAppUIInputTypeDef" = dataclasses.field()

    TargetResourceArn = field("TargetResourceArn")

    @cached_property
    def EMRContainersConfig(self):  # pragma: no cover
        return EMRContainersConfig.make_one(self.boto3_raw_data["EMRContainersConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    XReferer = field("XReferer")
    ProfilerType = field("ProfilerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePersistentAppUIInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePersistentAppUIInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    @cached_property
    def UsernamePassword(self):  # pragma: no cover
        return UsernamePassword.make_one(self.boto3_raw_data["UsernamePassword"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeClusterInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterInputWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterInputWait:
    boto3_raw_data: "type_defs.DescribeClusterInputWaitTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStepInputWait:
    boto3_raw_data: "type_defs.DescribeStepInputWaitTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    StepId = field("StepId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStepInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStepInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobFlowsInput:
    boto3_raw_data: "type_defs.DescribeJobFlowsInputTypeDef" = dataclasses.field()

    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")
    JobFlowIds = field("JobFlowIds")
    JobFlowStates = field("JobFlowStates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobFlowsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobFlowsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersInput:
    boto3_raw_data: "type_defs.ListClustersInputTypeDef" = dataclasses.field()

    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")
    ClusterStates = field("ClusterStates")
    Marker = field("Marker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListClustersInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotebookExecutionsInput:
    boto3_raw_data: "type_defs.ListNotebookExecutionsInputTypeDef" = dataclasses.field()

    EditorId = field("EditorId")
    Status = field("Status")
    From = field("From")
    To = field("To")
    Marker = field("Marker")
    ExecutionEngineId = field("ExecutionEngineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotebookExecutionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReleaseLabelOutput:
    boto3_raw_data: "type_defs.DescribeReleaseLabelOutputTypeDef" = dataclasses.field()

    ReleaseLabel = field("ReleaseLabel")

    @cached_property
    def Applications(self):  # pragma: no cover
        return SimplifiedApplication.make_many(self.boto3_raw_data["Applications"])

    @cached_property
    def AvailableOSReleases(self):  # pragma: no cover
        return OSRelease.make_many(self.boto3_raw_data["AvailableOSReleases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReleaseLabelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReleaseLabelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsBlockDeviceConfig:
    boto3_raw_data: "type_defs.EbsBlockDeviceConfigTypeDef" = dataclasses.field()

    @cached_property
    def VolumeSpecification(self):  # pragma: no cover
        return VolumeSpecification.make_one(self.boto3_raw_data["VolumeSpecification"])

    VolumesPerInstance = field("VolumesPerInstance")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EbsBlockDeviceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsBlockDeviceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsBlockDevice:
    boto3_raw_data: "type_defs.EbsBlockDeviceTypeDef" = dataclasses.field()

    @cached_property
    def VolumeSpecification(self):  # pragma: no cover
        return VolumeSpecification.make_one(self.boto3_raw_data["VolumeSpecification"])

    Device = field("Device")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsBlockDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EbsBlockDeviceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStudioSessionMappingOutput:
    boto3_raw_data: "type_defs.GetStudioSessionMappingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SessionMapping(self):  # pragma: no cover
        return SessionMappingDetail.make_one(self.boto3_raw_data["SessionMapping"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetStudioSessionMappingOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStudioSessionMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HadoopJarStepConfigOutput:
    boto3_raw_data: "type_defs.HadoopJarStepConfigOutputTypeDef" = dataclasses.field()

    Jar = field("Jar")

    @cached_property
    def Properties(self):  # pragma: no cover
        return KeyValue.make_many(self.boto3_raw_data["Properties"])

    MainClass = field("MainClass")
    Args = field("Args")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HadoopJarStepConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HadoopJarStepConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HadoopJarStepConfig:
    boto3_raw_data: "type_defs.HadoopJarStepConfigTypeDef" = dataclasses.field()

    Jar = field("Jar")

    @cached_property
    def Properties(self):  # pragma: no cover
        return KeyValue.make_many(self.boto3_raw_data["Properties"])

    MainClass = field("MainClass")
    Args = field("Args")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HadoopJarStepConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HadoopJarStepConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetStatus:
    boto3_raw_data: "type_defs.InstanceFleetStatusTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return InstanceFleetStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    @cached_property
    def Timeline(self):  # pragma: no cover
        return InstanceFleetTimeline.make_one(self.boto3_raw_data["Timeline"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceFleetStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupStatus:
    boto3_raw_data: "type_defs.InstanceGroupStatusTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return InstanceGroupStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    @cached_property
    def Timeline(self):  # pragma: no cover
        return InstanceGroupTimeline.make_one(self.boto3_raw_data["Timeline"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShrinkPolicyOutput:
    boto3_raw_data: "type_defs.ShrinkPolicyOutputTypeDef" = dataclasses.field()

    DecommissionTimeout = field("DecommissionTimeout")

    @cached_property
    def InstanceResizePolicy(self):  # pragma: no cover
        return InstanceResizePolicyOutput.make_one(
            self.boto3_raw_data["InstanceResizePolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShrinkPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShrinkPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceStatus:
    boto3_raw_data: "type_defs.InstanceStatusTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return InstanceStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    @cached_property
    def Timeline(self):  # pragma: no cover
        return InstanceTimeline.make_one(self.boto3_raw_data["Timeline"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobFlowInstancesDetail:
    boto3_raw_data: "type_defs.JobFlowInstancesDetailTypeDef" = dataclasses.field()

    MasterInstanceType = field("MasterInstanceType")
    SlaveInstanceType = field("SlaveInstanceType")
    InstanceCount = field("InstanceCount")
    MasterPublicDnsName = field("MasterPublicDnsName")
    MasterInstanceId = field("MasterInstanceId")

    @cached_property
    def InstanceGroups(self):  # pragma: no cover
        return InstanceGroupDetail.make_many(self.boto3_raw_data["InstanceGroups"])

    NormalizedInstanceHours = field("NormalizedInstanceHours")
    Ec2KeyName = field("Ec2KeyName")
    Ec2SubnetId = field("Ec2SubnetId")

    @cached_property
    def Placement(self):  # pragma: no cover
        return PlacementTypeOutput.make_one(self.boto3_raw_data["Placement"])

    KeepJobFlowAliveWhenNoSteps = field("KeepJobFlowAliveWhenNoSteps")
    TerminationProtected = field("TerminationProtected")
    UnhealthyNodeReplacement = field("UnhealthyNodeReplacement")
    HadoopVersion = field("HadoopVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobFlowInstancesDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobFlowInstancesDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBootstrapActionsInputPaginate:
    boto3_raw_data: "type_defs.ListBootstrapActionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBootstrapActionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBootstrapActionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersInputPaginate:
    boto3_raw_data: "type_defs.ListClustersInputPaginateTypeDef" = dataclasses.field()

    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")
    ClusterStates = field("ClusterStates")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceFleetsInputPaginate:
    boto3_raw_data: "type_defs.ListInstanceFleetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceFleetsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceFleetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListInstanceGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceGroupsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListInstancesInputPaginateTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    InstanceGroupId = field("InstanceGroupId")
    InstanceGroupTypes = field("InstanceGroupTypes")
    InstanceFleetId = field("InstanceFleetId")
    InstanceFleetType = field("InstanceFleetType")
    InstanceStates = field("InstanceStates")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotebookExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListNotebookExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    EditorId = field("EditorId")
    Status = field("Status")
    From = field("From")
    To = field("To")
    ExecutionEngineId = field("ExecutionEngineId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotebookExecutionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigurationsInputPaginate:
    boto3_raw_data: "type_defs.ListSecurityConfigurationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityConfigurationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigurationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepsInputPaginate:
    boto3_raw_data: "type_defs.ListStepsInputPaginateTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    StepStates = field("StepStates")
    StepIds = field("StepIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStepsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStepsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStudioSessionMappingsInputPaginate:
    boto3_raw_data: "type_defs.ListStudioSessionMappingsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StudioId = field("StudioId")
    IdentityType = field("IdentityType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStudioSessionMappingsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStudioSessionMappingsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStudiosInputPaginate:
    boto3_raw_data: "type_defs.ListStudiosInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStudiosInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStudiosInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReleaseLabelsInput:
    boto3_raw_data: "type_defs.ListReleaseLabelsInputTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ReleaseLabelFilter.make_one(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReleaseLabelsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReleaseLabelsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigurationsOutput:
    boto3_raw_data: "type_defs.ListSecurityConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityConfigurations(self):  # pragma: no cover
        return SecurityConfigurationSummary.make_many(
            self.boto3_raw_data["SecurityConfigurations"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSecurityConfigurationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStudioSessionMappingsOutput:
    boto3_raw_data: "type_defs.ListStudioSessionMappingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SessionMappings(self):  # pragma: no cover
        return SessionMappingSummary.make_many(self.boto3_raw_data["SessionMappings"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStudioSessionMappingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStudioSessionMappingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStudiosOutput:
    boto3_raw_data: "type_defs.ListStudiosOutputTypeDef" = dataclasses.field()

    @cached_property
    def Studios(self):  # pragma: no cover
        return StudioSummary.make_many(self.boto3_raw_data["Studios"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStudiosOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStudiosOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupportedInstanceTypesOutput:
    boto3_raw_data: "type_defs.ListSupportedInstanceTypesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SupportedInstanceTypes(self):  # pragma: no cover
        return SupportedInstanceType.make_many(
            self.boto3_raw_data["SupportedInstanceTypes"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSupportedInstanceTypesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupportedInstanceTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotebookExecutionSummary:
    boto3_raw_data: "type_defs.NotebookExecutionSummaryTypeDef" = dataclasses.field()

    NotebookExecutionId = field("NotebookExecutionId")
    EditorId = field("EditorId")
    NotebookExecutionName = field("NotebookExecutionName")
    Status = field("Status")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def NotebookS3Location(self):  # pragma: no cover
        return NotebookS3LocationForOutput.make_one(
            self.boto3_raw_data["NotebookS3Location"]
        )

    ExecutionEngineId = field("ExecutionEngineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotebookExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotebookExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotebookExecution:
    boto3_raw_data: "type_defs.NotebookExecutionTypeDef" = dataclasses.field()

    NotebookExecutionId = field("NotebookExecutionId")
    EditorId = field("EditorId")

    @cached_property
    def ExecutionEngine(self):  # pragma: no cover
        return ExecutionEngineConfig.make_one(self.boto3_raw_data["ExecutionEngine"])

    NotebookExecutionName = field("NotebookExecutionName")
    NotebookParams = field("NotebookParams")
    Status = field("Status")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Arn = field("Arn")
    OutputNotebookURI = field("OutputNotebookURI")
    LastStateChangeReason = field("LastStateChangeReason")
    NotebookInstanceSecurityGroupId = field("NotebookInstanceSecurityGroupId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def NotebookS3Location(self):  # pragma: no cover
        return NotebookS3LocationForOutput.make_one(
            self.boto3_raw_data["NotebookS3Location"]
        )

    @cached_property
    def OutputNotebookS3Location(self):  # pragma: no cover
        return OutputNotebookS3LocationForOutput.make_one(
            self.boto3_raw_data["OutputNotebookS3Location"]
        )

    OutputNotebookFormat = field("OutputNotebookFormat")
    EnvironmentVariables = field("EnvironmentVariables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotebookExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotebookExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnDemandProvisioningSpecification:
    boto3_raw_data: "type_defs.OnDemandProvisioningSpecificationTypeDef" = (
        dataclasses.field()
    )

    AllocationStrategy = field("AllocationStrategy")

    @cached_property
    def CapacityReservationOptions(self):  # pragma: no cover
        return OnDemandCapacityReservationOptions.make_one(
            self.boto3_raw_data["CapacityReservationOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OnDemandProvisioningSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnDemandProvisioningSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnDemandResizingSpecification:
    boto3_raw_data: "type_defs.OnDemandResizingSpecificationTypeDef" = (
        dataclasses.field()
    )

    TimeoutDurationMinutes = field("TimeoutDurationMinutes")
    AllocationStrategy = field("AllocationStrategy")

    @cached_property
    def CapacityReservationOptions(self):  # pragma: no cover
        return OnDemandCapacityReservationOptions.make_one(
            self.boto3_raw_data["CapacityReservationOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OnDemandResizingSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnDemandResizingSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartNotebookExecutionInput:
    boto3_raw_data: "type_defs.StartNotebookExecutionInputTypeDef" = dataclasses.field()

    @cached_property
    def ExecutionEngine(self):  # pragma: no cover
        return ExecutionEngineConfig.make_one(self.boto3_raw_data["ExecutionEngine"])

    ServiceRole = field("ServiceRole")
    EditorId = field("EditorId")
    RelativePath = field("RelativePath")
    NotebookExecutionName = field("NotebookExecutionName")
    NotebookParams = field("NotebookParams")
    NotebookInstanceSecurityGroupId = field("NotebookInstanceSecurityGroupId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def NotebookS3Location(self):  # pragma: no cover
        return NotebookS3LocationFromInput.make_one(
            self.boto3_raw_data["NotebookS3Location"]
        )

    @cached_property
    def OutputNotebookS3Location(self):  # pragma: no cover
        return OutputNotebookS3LocationFromInput.make_one(
            self.boto3_raw_data["OutputNotebookS3Location"]
        )

    OutputNotebookFormat = field("OutputNotebookFormat")
    EnvironmentVariables = field("EnvironmentVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartNotebookExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartNotebookExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingAction:
    boto3_raw_data: "type_defs.ScalingActionTypeDef" = dataclasses.field()

    @cached_property
    def SimpleScalingPolicyConfiguration(self):  # pragma: no cover
        return SimpleScalingPolicyConfiguration.make_one(
            self.boto3_raw_data["SimpleScalingPolicyConfiguration"]
        )

    Market = field("Market")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepStatus:
    boto3_raw_data: "type_defs.StepStatusTypeDef" = dataclasses.field()

    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return StepStateChangeReason.make_one(self.boto3_raw_data["StateChangeReason"])

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    @cached_property
    def Timeline(self):  # pragma: no cover
        return StepTimeline.make_one(self.boto3_raw_data["Timeline"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePersistentAppUIOutput:
    boto3_raw_data: "type_defs.DescribePersistentAppUIOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PersistentAppUI(self):  # pragma: no cover
        return PersistentAppUI.make_one(self.boto3_raw_data["PersistentAppUI"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePersistentAppUIOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePersistentAppUIOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStudioOutput:
    boto3_raw_data: "type_defs.DescribeStudioOutputTypeDef" = dataclasses.field()

    @cached_property
    def Studio(self):  # pragma: no cover
        return Studio.make_one(self.boto3_raw_data["Studio"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStudioOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStudioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBlockPublicAccessConfigurationOutput:
    boto3_raw_data: "type_defs.GetBlockPublicAccessConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlockPublicAccessConfiguration(self):  # pragma: no cover
        return BlockPublicAccessConfigurationOutput.make_one(
            self.boto3_raw_data["BlockPublicAccessConfiguration"]
        )

    @cached_property
    def BlockPublicAccessConfigurationMetadata(self):  # pragma: no cover
        return BlockPublicAccessConfigurationMetadata.make_one(
            self.boto3_raw_data["BlockPublicAccessConfigurationMetadata"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBlockPublicAccessConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBlockPublicAccessConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BootstrapActionDetail:
    boto3_raw_data: "type_defs.BootstrapActionDetailTypeDef" = dataclasses.field()

    @cached_property
    def BootstrapActionConfig(self):  # pragma: no cover
        return BootstrapActionConfigOutput.make_one(
            self.boto3_raw_data["BootstrapActionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BootstrapActionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BootstrapActionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingTriggerOutput:
    boto3_raw_data: "type_defs.ScalingTriggerOutputTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchAlarmDefinition(self):  # pragma: no cover
        return CloudWatchAlarmDefinitionOutput.make_one(
            self.boto3_raw_data["CloudWatchAlarmDefinition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingTriggerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingTriggerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSummary:
    boto3_raw_data: "type_defs.ClusterSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Status(self):  # pragma: no cover
        return ClusterStatus.make_one(self.boto3_raw_data["Status"])

    NormalizedInstanceHours = field("NormalizedInstanceHours")
    ClusterArn = field("ClusterArn")
    OutpostArn = field("OutpostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cluster:
    boto3_raw_data: "type_defs.ClusterTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Status(self):  # pragma: no cover
        return ClusterStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Ec2InstanceAttributes(self):  # pragma: no cover
        return Ec2InstanceAttributes.make_one(
            self.boto3_raw_data["Ec2InstanceAttributes"]
        )

    InstanceCollectionType = field("InstanceCollectionType")
    LogUri = field("LogUri")
    LogEncryptionKmsKeyId = field("LogEncryptionKmsKeyId")
    RequestedAmiVersion = field("RequestedAmiVersion")
    RunningAmiVersion = field("RunningAmiVersion")
    ReleaseLabel = field("ReleaseLabel")
    AutoTerminate = field("AutoTerminate")
    TerminationProtected = field("TerminationProtected")
    UnhealthyNodeReplacement = field("UnhealthyNodeReplacement")
    VisibleToAllUsers = field("VisibleToAllUsers")

    @cached_property
    def Applications(self):  # pragma: no cover
        return ApplicationOutput.make_many(self.boto3_raw_data["Applications"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ServiceRole = field("ServiceRole")
    NormalizedInstanceHours = field("NormalizedInstanceHours")
    MasterPublicDnsName = field("MasterPublicDnsName")

    @cached_property
    def Configurations(self):  # pragma: no cover
        return ConfigurationOutput.make_many(self.boto3_raw_data["Configurations"])

    SecurityConfiguration = field("SecurityConfiguration")
    AutoScalingRole = field("AutoScalingRole")
    ScaleDownBehavior = field("ScaleDownBehavior")
    CustomAmiId = field("CustomAmiId")
    EbsRootVolumeSize = field("EbsRootVolumeSize")
    RepoUpgradeOnBoot = field("RepoUpgradeOnBoot")

    @cached_property
    def KerberosAttributes(self):  # pragma: no cover
        return KerberosAttributes.make_one(self.boto3_raw_data["KerberosAttributes"])

    ClusterArn = field("ClusterArn")
    OutpostArn = field("OutpostArn")
    StepConcurrencyLevel = field("StepConcurrencyLevel")

    @cached_property
    def PlacementGroups(self):  # pragma: no cover
        return PlacementGroupConfig.make_many(self.boto3_raw_data["PlacementGroups"])

    OSReleaseLabel = field("OSReleaseLabel")
    EbsRootVolumeIops = field("EbsRootVolumeIops")
    EbsRootVolumeThroughput = field("EbsRootVolumeThroughput")
    ExtendedSupport = field("ExtendedSupport")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedScalingPolicyOutput:
    boto3_raw_data: "type_defs.GetManagedScalingPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedScalingPolicy(self):  # pragma: no cover
        return ManagedScalingPolicy.make_one(
            self.boto3_raw_data["ManagedScalingPolicy"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetManagedScalingPolicyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedScalingPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutManagedScalingPolicyInput:
    boto3_raw_data: "type_defs.PutManagedScalingPolicyInputTypeDef" = (
        dataclasses.field()
    )

    ClusterId = field("ClusterId")

    @cached_property
    def ManagedScalingPolicy(self):  # pragma: no cover
        return ManagedScalingPolicy.make_one(
            self.boto3_raw_data["ManagedScalingPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutManagedScalingPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutManagedScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterSessionCredentialsOutput:
    boto3_raw_data: "type_defs.GetClusterSessionCredentialsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    ExpiresAt = field("ExpiresAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetClusterSessionCredentialsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterSessionCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsConfiguration:
    boto3_raw_data: "type_defs.EbsConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def EbsBlockDeviceConfigs(self):  # pragma: no cover
        return EbsBlockDeviceConfig.make_many(
            self.boto3_raw_data["EbsBlockDeviceConfigs"]
        )

    EbsOptimized = field("EbsOptimized")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTypeSpecificationPaginator:
    boto3_raw_data: "type_defs.InstanceTypeSpecificationPaginatorTypeDef" = (
        dataclasses.field()
    )

    InstanceType = field("InstanceType")
    WeightedCapacity = field("WeightedCapacity")
    BidPrice = field("BidPrice")
    BidPriceAsPercentageOfOnDemandPrice = field("BidPriceAsPercentageOfOnDemandPrice")

    @cached_property
    def Configurations(self):  # pragma: no cover
        return ConfigurationPaginator.make_many(self.boto3_raw_data["Configurations"])

    @cached_property
    def EbsBlockDevices(self):  # pragma: no cover
        return EbsBlockDevice.make_many(self.boto3_raw_data["EbsBlockDevices"])

    EbsOptimized = field("EbsOptimized")
    CustomAmiId = field("CustomAmiId")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceTypeSpecificationPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeSpecificationPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTypeSpecification:
    boto3_raw_data: "type_defs.InstanceTypeSpecificationTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    WeightedCapacity = field("WeightedCapacity")
    BidPrice = field("BidPrice")
    BidPriceAsPercentageOfOnDemandPrice = field("BidPriceAsPercentageOfOnDemandPrice")

    @cached_property
    def Configurations(self):  # pragma: no cover
        return ConfigurationOutput.make_many(self.boto3_raw_data["Configurations"])

    @cached_property
    def EbsBlockDevices(self):  # pragma: no cover
        return EbsBlockDevice.make_many(self.boto3_raw_data["EbsBlockDevices"])

    EbsOptimized = field("EbsOptimized")
    CustomAmiId = field("CustomAmiId")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepConfigOutput:
    boto3_raw_data: "type_defs.StepConfigOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def HadoopJarStep(self):  # pragma: no cover
        return HadoopJarStepConfigOutput.make_one(self.boto3_raw_data["HadoopJarStep"])

    ActionOnFailure = field("ActionOnFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShrinkPolicy:
    boto3_raw_data: "type_defs.ShrinkPolicyTypeDef" = dataclasses.field()

    DecommissionTimeout = field("DecommissionTimeout")
    InstanceResizePolicy = field("InstanceResizePolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShrinkPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShrinkPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    Id = field("Id")
    Ec2InstanceId = field("Ec2InstanceId")
    PublicDnsName = field("PublicDnsName")
    PublicIpAddress = field("PublicIpAddress")
    PrivateDnsName = field("PrivateDnsName")
    PrivateIpAddress = field("PrivateIpAddress")

    @cached_property
    def Status(self):  # pragma: no cover
        return InstanceStatus.make_one(self.boto3_raw_data["Status"])

    InstanceGroupId = field("InstanceGroupId")
    InstanceFleetId = field("InstanceFleetId")
    Market = field("Market")
    InstanceType = field("InstanceType")

    @cached_property
    def EbsVolumes(self):  # pragma: no cover
        return EbsVolume.make_many(self.boto3_raw_data["EbsVolumes"])

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
class ListNotebookExecutionsOutput:
    boto3_raw_data: "type_defs.ListNotebookExecutionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NotebookExecutions(self):  # pragma: no cover
        return NotebookExecutionSummary.make_many(
            self.boto3_raw_data["NotebookExecutions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotebookExecutionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotebookExecutionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotebookExecutionOutput:
    boto3_raw_data: "type_defs.DescribeNotebookExecutionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NotebookExecution(self):  # pragma: no cover
        return NotebookExecution.make_one(self.boto3_raw_data["NotebookExecution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeNotebookExecutionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotebookExecutionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetProvisioningSpecifications:
    boto3_raw_data: "type_defs.InstanceFleetProvisioningSpecificationsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpotSpecification(self):  # pragma: no cover
        return SpotProvisioningSpecification.make_one(
            self.boto3_raw_data["SpotSpecification"]
        )

    @cached_property
    def OnDemandSpecification(self):  # pragma: no cover
        return OnDemandProvisioningSpecification.make_one(
            self.boto3_raw_data["OnDemandSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceFleetProvisioningSpecificationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetProvisioningSpecificationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetResizingSpecifications:
    boto3_raw_data: "type_defs.InstanceFleetResizingSpecificationsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpotResizeSpecification(self):  # pragma: no cover
        return SpotResizingSpecification.make_one(
            self.boto3_raw_data["SpotResizeSpecification"]
        )

    @cached_property
    def OnDemandResizeSpecification(self):  # pragma: no cover
        return OnDemandResizingSpecification.make_one(
            self.boto3_raw_data["OnDemandResizeSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceFleetResizingSpecificationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetResizingSpecificationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BootstrapActionConfig:
    boto3_raw_data: "type_defs.BootstrapActionConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    ScriptBootstrapAction = field("ScriptBootstrapAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BootstrapActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BootstrapActionConfigTypeDef"]
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

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Config(self):  # pragma: no cover
        return HadoopStepConfig.make_one(self.boto3_raw_data["Config"])

    ActionOnFailure = field("ActionOnFailure")

    @cached_property
    def Status(self):  # pragma: no cover
        return StepStatus.make_one(self.boto3_raw_data["Status"])

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
class Step:
    boto3_raw_data: "type_defs.StepTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Config(self):  # pragma: no cover
        return HadoopStepConfig.make_one(self.boto3_raw_data["Config"])

    ActionOnFailure = field("ActionOnFailure")

    @cached_property
    def Status(self):  # pragma: no cover
        return StepStatus.make_one(self.boto3_raw_data["Status"])

    ExecutionRoleArn = field("ExecutionRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBlockPublicAccessConfigurationInput:
    boto3_raw_data: "type_defs.PutBlockPublicAccessConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    BlockPublicAccessConfiguration = field("BlockPublicAccessConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBlockPublicAccessConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBlockPublicAccessConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingRuleOutput:
    boto3_raw_data: "type_defs.ScalingRuleOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Action(self):  # pragma: no cover
        return ScalingAction.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def Trigger(self):  # pragma: no cover
        return ScalingTriggerOutput.make_one(self.boto3_raw_data["Trigger"])

    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingTrigger:
    boto3_raw_data: "type_defs.ScalingTriggerTypeDef" = dataclasses.field()

    CloudWatchAlarmDefinition = field("CloudWatchAlarmDefinition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingTriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingTriggerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersOutput:
    boto3_raw_data: "type_defs.ListClustersOutputTypeDef" = dataclasses.field()

    @cached_property
    def Clusters(self):  # pragma: no cover
        return ClusterSummary.make_many(self.boto3_raw_data["Clusters"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterOutput:
    boto3_raw_data: "type_defs.DescribeClusterOutputTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceTypeConfig:
    boto3_raw_data: "type_defs.InstanceTypeConfigTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    WeightedCapacity = field("WeightedCapacity")
    BidPrice = field("BidPrice")
    BidPriceAsPercentageOfOnDemandPrice = field("BidPriceAsPercentageOfOnDemandPrice")

    @cached_property
    def EbsConfiguration(self):  # pragma: no cover
        return EbsConfiguration.make_one(self.boto3_raw_data["EbsConfiguration"])

    Configurations = field("Configurations")
    CustomAmiId = field("CustomAmiId")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepDetail:
    boto3_raw_data: "type_defs.StepDetailTypeDef" = dataclasses.field()

    @cached_property
    def StepConfig(self):  # pragma: no cover
        return StepConfigOutput.make_one(self.boto3_raw_data["StepConfig"])

    @cached_property
    def ExecutionStatusDetail(self):  # pragma: no cover
        return StepExecutionStatusDetail.make_one(
            self.boto3_raw_data["ExecutionStatusDetail"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepConfig:
    boto3_raw_data: "type_defs.StepConfigTypeDef" = dataclasses.field()

    Name = field("Name")
    HadoopJarStep = field("HadoopJarStep")
    ActionOnFailure = field("ActionOnFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesOutput:
    boto3_raw_data: "type_defs.ListInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetPaginator:
    boto3_raw_data: "type_defs.InstanceFleetPaginatorTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Status(self):  # pragma: no cover
        return InstanceFleetStatus.make_one(self.boto3_raw_data["Status"])

    InstanceFleetType = field("InstanceFleetType")
    TargetOnDemandCapacity = field("TargetOnDemandCapacity")
    TargetSpotCapacity = field("TargetSpotCapacity")
    ProvisionedOnDemandCapacity = field("ProvisionedOnDemandCapacity")
    ProvisionedSpotCapacity = field("ProvisionedSpotCapacity")

    @cached_property
    def InstanceTypeSpecifications(self):  # pragma: no cover
        return InstanceTypeSpecificationPaginator.make_many(
            self.boto3_raw_data["InstanceTypeSpecifications"]
        )

    @cached_property
    def LaunchSpecifications(self):  # pragma: no cover
        return InstanceFleetProvisioningSpecifications.make_one(
            self.boto3_raw_data["LaunchSpecifications"]
        )

    @cached_property
    def ResizeSpecifications(self):  # pragma: no cover
        return InstanceFleetResizingSpecifications.make_one(
            self.boto3_raw_data["ResizeSpecifications"]
        )

    Context = field("Context")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceFleetPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleet:
    boto3_raw_data: "type_defs.InstanceFleetTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @cached_property
    def Status(self):  # pragma: no cover
        return InstanceFleetStatus.make_one(self.boto3_raw_data["Status"])

    InstanceFleetType = field("InstanceFleetType")
    TargetOnDemandCapacity = field("TargetOnDemandCapacity")
    TargetSpotCapacity = field("TargetSpotCapacity")
    ProvisionedOnDemandCapacity = field("ProvisionedOnDemandCapacity")
    ProvisionedSpotCapacity = field("ProvisionedSpotCapacity")

    @cached_property
    def InstanceTypeSpecifications(self):  # pragma: no cover
        return InstanceTypeSpecification.make_many(
            self.boto3_raw_data["InstanceTypeSpecifications"]
        )

    @cached_property
    def LaunchSpecifications(self):  # pragma: no cover
        return InstanceFleetProvisioningSpecifications.make_one(
            self.boto3_raw_data["LaunchSpecifications"]
        )

    @cached_property
    def ResizeSpecifications(self):  # pragma: no cover
        return InstanceFleetResizingSpecifications.make_one(
            self.boto3_raw_data["ResizeSpecifications"]
        )

    Context = field("Context")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceFleetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceFleetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStepsOutput:
    boto3_raw_data: "type_defs.ListStepsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Steps(self):  # pragma: no cover
        return StepSummary.make_many(self.boto3_raw_data["Steps"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStepsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListStepsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStepOutput:
    boto3_raw_data: "type_defs.DescribeStepOutputTypeDef" = dataclasses.field()

    @cached_property
    def Step(self):  # pragma: no cover
        return Step.make_one(self.boto3_raw_data["Step"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStepOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingPolicyDescription:
    boto3_raw_data: "type_defs.AutoScalingPolicyDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Status(self):  # pragma: no cover
        return AutoScalingPolicyStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Constraints(self):  # pragma: no cover
        return ScalingConstraints.make_one(self.boto3_raw_data["Constraints"])

    @cached_property
    def Rules(self):  # pragma: no cover
        return ScalingRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingPolicyDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingPolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetConfig:
    boto3_raw_data: "type_defs.InstanceFleetConfigTypeDef" = dataclasses.field()

    InstanceFleetType = field("InstanceFleetType")
    Name = field("Name")
    TargetOnDemandCapacity = field("TargetOnDemandCapacity")
    TargetSpotCapacity = field("TargetSpotCapacity")

    @cached_property
    def InstanceTypeConfigs(self):  # pragma: no cover
        return InstanceTypeConfig.make_many(self.boto3_raw_data["InstanceTypeConfigs"])

    @cached_property
    def LaunchSpecifications(self):  # pragma: no cover
        return InstanceFleetProvisioningSpecifications.make_one(
            self.boto3_raw_data["LaunchSpecifications"]
        )

    @cached_property
    def ResizeSpecifications(self):  # pragma: no cover
        return InstanceFleetResizingSpecifications.make_one(
            self.boto3_raw_data["ResizeSpecifications"]
        )

    Context = field("Context")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceFleetConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceFleetModifyConfig:
    boto3_raw_data: "type_defs.InstanceFleetModifyConfigTypeDef" = dataclasses.field()

    InstanceFleetId = field("InstanceFleetId")
    TargetOnDemandCapacity = field("TargetOnDemandCapacity")
    TargetSpotCapacity = field("TargetSpotCapacity")

    @cached_property
    def ResizeSpecifications(self):  # pragma: no cover
        return InstanceFleetResizingSpecifications.make_one(
            self.boto3_raw_data["ResizeSpecifications"]
        )

    @cached_property
    def InstanceTypeConfigs(self):  # pragma: no cover
        return InstanceTypeConfig.make_many(self.boto3_raw_data["InstanceTypeConfigs"])

    Context = field("Context")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceFleetModifyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceFleetModifyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobFlowDetail:
    boto3_raw_data: "type_defs.JobFlowDetailTypeDef" = dataclasses.field()

    JobFlowId = field("JobFlowId")
    Name = field("Name")

    @cached_property
    def ExecutionStatusDetail(self):  # pragma: no cover
        return JobFlowExecutionStatusDetail.make_one(
            self.boto3_raw_data["ExecutionStatusDetail"]
        )

    @cached_property
    def Instances(self):  # pragma: no cover
        return JobFlowInstancesDetail.make_one(self.boto3_raw_data["Instances"])

    LogUri = field("LogUri")
    LogEncryptionKmsKeyId = field("LogEncryptionKmsKeyId")
    AmiVersion = field("AmiVersion")

    @cached_property
    def Steps(self):  # pragma: no cover
        return StepDetail.make_many(self.boto3_raw_data["Steps"])

    @cached_property
    def BootstrapActions(self):  # pragma: no cover
        return BootstrapActionDetail.make_many(self.boto3_raw_data["BootstrapActions"])

    SupportedProducts = field("SupportedProducts")
    VisibleToAllUsers = field("VisibleToAllUsers")
    JobFlowRole = field("JobFlowRole")
    ServiceRole = field("ServiceRole")
    AutoScalingRole = field("AutoScalingRole")
    ScaleDownBehavior = field("ScaleDownBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobFlowDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobFlowDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupModifyConfig:
    boto3_raw_data: "type_defs.InstanceGroupModifyConfigTypeDef" = dataclasses.field()

    InstanceGroupId = field("InstanceGroupId")
    InstanceCount = field("InstanceCount")
    EC2InstanceIdsToTerminate = field("EC2InstanceIdsToTerminate")
    ShrinkPolicy = field("ShrinkPolicy")
    ReconfigurationType = field("ReconfigurationType")
    Configurations = field("Configurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupModifyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupModifyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceFleetsOutputPaginator:
    boto3_raw_data: "type_defs.ListInstanceFleetsOutputPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceFleets(self):  # pragma: no cover
        return InstanceFleetPaginator.make_many(self.boto3_raw_data["InstanceFleets"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceFleetsOutputPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceFleetsOutputPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceFleetsOutput:
    boto3_raw_data: "type_defs.ListInstanceFleetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def InstanceFleets(self):  # pragma: no cover
        return InstanceFleet.make_many(self.boto3_raw_data["InstanceFleets"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceFleetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceFleetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupPaginator:
    boto3_raw_data: "type_defs.InstanceGroupPaginatorTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Market = field("Market")
    InstanceGroupType = field("InstanceGroupType")
    BidPrice = field("BidPrice")
    InstanceType = field("InstanceType")
    RequestedInstanceCount = field("RequestedInstanceCount")
    RunningInstanceCount = field("RunningInstanceCount")

    @cached_property
    def Status(self):  # pragma: no cover
        return InstanceGroupStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Configurations(self):  # pragma: no cover
        return ConfigurationPaginator.make_many(self.boto3_raw_data["Configurations"])

    ConfigurationsVersion = field("ConfigurationsVersion")

    @cached_property
    def LastSuccessfullyAppliedConfigurations(self):  # pragma: no cover
        return ConfigurationPaginator.make_many(
            self.boto3_raw_data["LastSuccessfullyAppliedConfigurations"]
        )

    LastSuccessfullyAppliedConfigurationsVersion = field(
        "LastSuccessfullyAppliedConfigurationsVersion"
    )

    @cached_property
    def EbsBlockDevices(self):  # pragma: no cover
        return EbsBlockDevice.make_many(self.boto3_raw_data["EbsBlockDevices"])

    EbsOptimized = field("EbsOptimized")

    @cached_property
    def ShrinkPolicy(self):  # pragma: no cover
        return ShrinkPolicyOutput.make_one(self.boto3_raw_data["ShrinkPolicy"])

    @cached_property
    def AutoScalingPolicy(self):  # pragma: no cover
        return AutoScalingPolicyDescription.make_one(
            self.boto3_raw_data["AutoScalingPolicy"]
        )

    CustomAmiId = field("CustomAmiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroup:
    boto3_raw_data: "type_defs.InstanceGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Market = field("Market")
    InstanceGroupType = field("InstanceGroupType")
    BidPrice = field("BidPrice")
    InstanceType = field("InstanceType")
    RequestedInstanceCount = field("RequestedInstanceCount")
    RunningInstanceCount = field("RunningInstanceCount")

    @cached_property
    def Status(self):  # pragma: no cover
        return InstanceGroupStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Configurations(self):  # pragma: no cover
        return ConfigurationOutput.make_many(self.boto3_raw_data["Configurations"])

    ConfigurationsVersion = field("ConfigurationsVersion")

    @cached_property
    def LastSuccessfullyAppliedConfigurations(self):  # pragma: no cover
        return ConfigurationOutput.make_many(
            self.boto3_raw_data["LastSuccessfullyAppliedConfigurations"]
        )

    LastSuccessfullyAppliedConfigurationsVersion = field(
        "LastSuccessfullyAppliedConfigurationsVersion"
    )

    @cached_property
    def EbsBlockDevices(self):  # pragma: no cover
        return EbsBlockDevice.make_many(self.boto3_raw_data["EbsBlockDevices"])

    EbsOptimized = field("EbsOptimized")

    @cached_property
    def ShrinkPolicy(self):  # pragma: no cover
        return ShrinkPolicyOutput.make_one(self.boto3_raw_data["ShrinkPolicy"])

    @cached_property
    def AutoScalingPolicy(self):  # pragma: no cover
        return AutoScalingPolicyDescription.make_one(
            self.boto3_raw_data["AutoScalingPolicy"]
        )

    CustomAmiId = field("CustomAmiId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAutoScalingPolicyOutput:
    boto3_raw_data: "type_defs.PutAutoScalingPolicyOutputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    InstanceGroupId = field("InstanceGroupId")

    @cached_property
    def AutoScalingPolicy(self):  # pragma: no cover
        return AutoScalingPolicyDescription.make_one(
            self.boto3_raw_data["AutoScalingPolicy"]
        )

    ClusterArn = field("ClusterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAutoScalingPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAutoScalingPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingRule:
    boto3_raw_data: "type_defs.ScalingRuleTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Action(self):  # pragma: no cover
        return ScalingAction.make_one(self.boto3_raw_data["Action"])

    Trigger = field("Trigger")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddInstanceFleetInput:
    boto3_raw_data: "type_defs.AddInstanceFleetInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @cached_property
    def InstanceFleet(self):  # pragma: no cover
        return InstanceFleetConfig.make_one(self.boto3_raw_data["InstanceFleet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddInstanceFleetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddInstanceFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyInstanceFleetInput:
    boto3_raw_data: "type_defs.ModifyInstanceFleetInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @cached_property
    def InstanceFleet(self):  # pragma: no cover
        return InstanceFleetModifyConfig.make_one(self.boto3_raw_data["InstanceFleet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyInstanceFleetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyInstanceFleetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobFlowsOutput:
    boto3_raw_data: "type_defs.DescribeJobFlowsOutputTypeDef" = dataclasses.field()

    @cached_property
    def JobFlows(self):  # pragma: no cover
        return JobFlowDetail.make_many(self.boto3_raw_data["JobFlows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobFlowsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobFlowsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddJobFlowStepsInput:
    boto3_raw_data: "type_defs.AddJobFlowStepsInputTypeDef" = dataclasses.field()

    JobFlowId = field("JobFlowId")
    Steps = field("Steps")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddJobFlowStepsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddJobFlowStepsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyInstanceGroupsInput:
    boto3_raw_data: "type_defs.ModifyInstanceGroupsInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")

    @cached_property
    def InstanceGroups(self):  # pragma: no cover
        return InstanceGroupModifyConfig.make_many(
            self.boto3_raw_data["InstanceGroups"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyInstanceGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyInstanceGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceGroupsOutputPaginator:
    boto3_raw_data: "type_defs.ListInstanceGroupsOutputPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceGroups(self):  # pragma: no cover
        return InstanceGroupPaginator.make_many(self.boto3_raw_data["InstanceGroups"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceGroupsOutputPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceGroupsOutputPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceGroupsOutput:
    boto3_raw_data: "type_defs.ListInstanceGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def InstanceGroups(self):  # pragma: no cover
        return InstanceGroup.make_many(self.boto3_raw_data["InstanceGroups"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingPolicy:
    boto3_raw_data: "type_defs.AutoScalingPolicyTypeDef" = dataclasses.field()

    @cached_property
    def Constraints(self):  # pragma: no cover
        return ScalingConstraints.make_one(self.boto3_raw_data["Constraints"])

    Rules = field("Rules")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoScalingPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceGroupConfig:
    boto3_raw_data: "type_defs.InstanceGroupConfigTypeDef" = dataclasses.field()

    InstanceRole = field("InstanceRole")
    InstanceType = field("InstanceType")
    InstanceCount = field("InstanceCount")
    Name = field("Name")
    Market = field("Market")
    BidPrice = field("BidPrice")
    Configurations = field("Configurations")

    @cached_property
    def EbsConfiguration(self):  # pragma: no cover
        return EbsConfiguration.make_one(self.boto3_raw_data["EbsConfiguration"])

    @cached_property
    def AutoScalingPolicy(self):  # pragma: no cover
        return AutoScalingPolicy.make_one(self.boto3_raw_data["AutoScalingPolicy"])

    CustomAmiId = field("CustomAmiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceGroupConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceGroupConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAutoScalingPolicyInput:
    boto3_raw_data: "type_defs.PutAutoScalingPolicyInputTypeDef" = dataclasses.field()

    ClusterId = field("ClusterId")
    InstanceGroupId = field("InstanceGroupId")

    @cached_property
    def AutoScalingPolicy(self):  # pragma: no cover
        return AutoScalingPolicy.make_one(self.boto3_raw_data["AutoScalingPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAutoScalingPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAutoScalingPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddInstanceGroupsInput:
    boto3_raw_data: "type_defs.AddInstanceGroupsInputTypeDef" = dataclasses.field()

    @cached_property
    def InstanceGroups(self):  # pragma: no cover
        return InstanceGroupConfig.make_many(self.boto3_raw_data["InstanceGroups"])

    JobFlowId = field("JobFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddInstanceGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddInstanceGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobFlowInstancesConfig:
    boto3_raw_data: "type_defs.JobFlowInstancesConfigTypeDef" = dataclasses.field()

    MasterInstanceType = field("MasterInstanceType")
    SlaveInstanceType = field("SlaveInstanceType")
    InstanceCount = field("InstanceCount")

    @cached_property
    def InstanceGroups(self):  # pragma: no cover
        return InstanceGroupConfig.make_many(self.boto3_raw_data["InstanceGroups"])

    @cached_property
    def InstanceFleets(self):  # pragma: no cover
        return InstanceFleetConfig.make_many(self.boto3_raw_data["InstanceFleets"])

    Ec2KeyName = field("Ec2KeyName")
    Placement = field("Placement")
    KeepJobFlowAliveWhenNoSteps = field("KeepJobFlowAliveWhenNoSteps")
    TerminationProtected = field("TerminationProtected")
    UnhealthyNodeReplacement = field("UnhealthyNodeReplacement")
    HadoopVersion = field("HadoopVersion")
    Ec2SubnetId = field("Ec2SubnetId")
    Ec2SubnetIds = field("Ec2SubnetIds")
    EmrManagedMasterSecurityGroup = field("EmrManagedMasterSecurityGroup")
    EmrManagedSlaveSecurityGroup = field("EmrManagedSlaveSecurityGroup")
    ServiceAccessSecurityGroup = field("ServiceAccessSecurityGroup")
    AdditionalMasterSecurityGroups = field("AdditionalMasterSecurityGroups")
    AdditionalSlaveSecurityGroups = field("AdditionalSlaveSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobFlowInstancesConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobFlowInstancesConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunJobFlowInput:
    boto3_raw_data: "type_defs.RunJobFlowInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Instances(self):  # pragma: no cover
        return JobFlowInstancesConfig.make_one(self.boto3_raw_data["Instances"])

    LogUri = field("LogUri")
    LogEncryptionKmsKeyId = field("LogEncryptionKmsKeyId")
    AdditionalInfo = field("AdditionalInfo")
    AmiVersion = field("AmiVersion")
    ReleaseLabel = field("ReleaseLabel")
    Steps = field("Steps")
    BootstrapActions = field("BootstrapActions")
    SupportedProducts = field("SupportedProducts")

    @cached_property
    def NewSupportedProducts(self):  # pragma: no cover
        return SupportedProductConfig.make_many(
            self.boto3_raw_data["NewSupportedProducts"]
        )

    Applications = field("Applications")
    Configurations = field("Configurations")
    VisibleToAllUsers = field("VisibleToAllUsers")
    JobFlowRole = field("JobFlowRole")
    ServiceRole = field("ServiceRole")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SecurityConfiguration = field("SecurityConfiguration")
    AutoScalingRole = field("AutoScalingRole")
    ScaleDownBehavior = field("ScaleDownBehavior")
    CustomAmiId = field("CustomAmiId")
    EbsRootVolumeSize = field("EbsRootVolumeSize")
    RepoUpgradeOnBoot = field("RepoUpgradeOnBoot")

    @cached_property
    def KerberosAttributes(self):  # pragma: no cover
        return KerberosAttributes.make_one(self.boto3_raw_data["KerberosAttributes"])

    StepConcurrencyLevel = field("StepConcurrencyLevel")

    @cached_property
    def ManagedScalingPolicy(self):  # pragma: no cover
        return ManagedScalingPolicy.make_one(
            self.boto3_raw_data["ManagedScalingPolicy"]
        )

    @cached_property
    def PlacementGroupConfigs(self):  # pragma: no cover
        return PlacementGroupConfig.make_many(
            self.boto3_raw_data["PlacementGroupConfigs"]
        )

    @cached_property
    def AutoTerminationPolicy(self):  # pragma: no cover
        return AutoTerminationPolicy.make_one(
            self.boto3_raw_data["AutoTerminationPolicy"]
        )

    OSReleaseLabel = field("OSReleaseLabel")
    EbsRootVolumeIops = field("EbsRootVolumeIops")
    EbsRootVolumeThroughput = field("EbsRootVolumeThroughput")
    ExtendedSupport = field("ExtendedSupport")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunJobFlowInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunJobFlowInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
