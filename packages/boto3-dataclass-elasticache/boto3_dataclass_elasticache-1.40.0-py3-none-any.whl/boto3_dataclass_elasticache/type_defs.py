# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elasticache import type_defs


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
class AuthenticationMode:
    boto3_raw_data: "type_defs.AuthenticationModeTypeDef" = dataclasses.field()

    Type = field("Type")
    Passwords = field("Passwords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationModeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationModeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Authentication:
    boto3_raw_data: "type_defs.AuthenticationTypeDef" = dataclasses.field()

    Type = field("Type")
    PasswordCount = field("PasswordCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthenticationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthenticationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeCacheSecurityGroupIngressMessage:
    boto3_raw_data: "type_defs.AuthorizeCacheSecurityGroupIngressMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeCacheSecurityGroupIngressMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeCacheSecurityGroupIngressMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZone:
    boto3_raw_data: "type_defs.AvailabilityZoneTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchApplyUpdateActionMessage:
    boto3_raw_data: "type_defs.BatchApplyUpdateActionMessageTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ReplicationGroupIds = field("ReplicationGroupIds")
    CacheClusterIds = field("CacheClusterIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchApplyUpdateActionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchApplyUpdateActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStopUpdateActionMessage:
    boto3_raw_data: "type_defs.BatchStopUpdateActionMessageTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ReplicationGroupIds = field("ReplicationGroupIds")
    CacheClusterIds = field("CacheClusterIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchStopUpdateActionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStopUpdateActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheParameterGroupStatus:
    boto3_raw_data: "type_defs.CacheParameterGroupStatusTypeDef" = dataclasses.field()

    CacheParameterGroupName = field("CacheParameterGroupName")
    ParameterApplyStatus = field("ParameterApplyStatus")
    CacheNodeIdsToReboot = field("CacheNodeIdsToReboot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheParameterGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheParameterGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSecurityGroupMembership:
    boto3_raw_data: "type_defs.CacheSecurityGroupMembershipTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheSecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheSecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    Address = field("Address")
    Port = field("Port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")
    TopicStatus = field("TopicStatus")

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
class SecurityGroupMembership:
    boto3_raw_data: "type_defs.SecurityGroupMembershipTypeDef" = dataclasses.field()

    SecurityGroupId = field("SecurityGroupId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheEngineVersion:
    boto3_raw_data: "type_defs.CacheEngineVersionTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    CacheEngineDescription = field("CacheEngineDescription")
    CacheEngineVersionDescription = field("CacheEngineVersionDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheEngineVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheEngineVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheNodeTypeSpecificValue:
    boto3_raw_data: "type_defs.CacheNodeTypeSpecificValueTypeDef" = dataclasses.field()

    CacheNodeType = field("CacheNodeType")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheNodeTypeSpecificValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheNodeTypeSpecificValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheNodeUpdateStatus:
    boto3_raw_data: "type_defs.CacheNodeUpdateStatusTypeDef" = dataclasses.field()

    CacheNodeId = field("CacheNodeId")
    NodeUpdateStatus = field("NodeUpdateStatus")
    NodeDeletionDate = field("NodeDeletionDate")
    NodeUpdateStartDate = field("NodeUpdateStartDate")
    NodeUpdateEndDate = field("NodeUpdateEndDate")
    NodeUpdateInitiatedBy = field("NodeUpdateInitiatedBy")
    NodeUpdateInitiatedDate = field("NodeUpdateInitiatedDate")
    NodeUpdateStatusModifiedDate = field("NodeUpdateStatusModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheNodeUpdateStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheNodeUpdateStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameter:
    boto3_raw_data: "type_defs.ParameterTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")
    Description = field("Description")
    Source = field("Source")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    MinimumEngineVersion = field("MinimumEngineVersion")
    ChangeType = field("ChangeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheParameterGroup:
    boto3_raw_data: "type_defs.CacheParameterGroupTypeDef" = dataclasses.field()

    CacheParameterGroupName = field("CacheParameterGroupName")
    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    Description = field("Description")
    IsGlobal = field("IsGlobal")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheParameterGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheParameterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2SecurityGroup:
    boto3_raw_data: "type_defs.EC2SecurityGroupTypeDef" = dataclasses.field()

    Status = field("Status")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EC2SecurityGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2SecurityGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataStorage:
    boto3_raw_data: "type_defs.DataStorageTypeDef" = dataclasses.field()

    Unit = field("Unit")
    Maximum = field("Maximum")
    Minimum = field("Minimum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataStorageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ECPUPerSecond:
    boto3_raw_data: "type_defs.ECPUPerSecondTypeDef" = dataclasses.field()

    Maximum = field("Maximum")
    Minimum = field("Minimum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ECPUPerSecondTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ECPUPerSecondTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsDestinationDetails:
    boto3_raw_data: "type_defs.CloudWatchLogsDestinationDetailsTypeDef" = (
        dataclasses.field()
    )

    LogGroup = field("LogGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLogsDestinationDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsDestinationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMigrationMessage:
    boto3_raw_data: "type_defs.CompleteMigrationMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureShard:
    boto3_raw_data: "type_defs.ConfigureShardTypeDef" = dataclasses.field()

    NodeGroupId = field("NodeGroupId")
    NewReplicaCount = field("NewReplicaCount")
    PreferredAvailabilityZones = field("PreferredAvailabilityZones")
    PreferredOutpostArns = field("PreferredOutpostArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigureShardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigureShardTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalReplicationGroupMessage:
    boto3_raw_data: "type_defs.CreateGlobalReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupIdSuffix = field("GlobalReplicationGroupIdSuffix")
    PrimaryReplicationGroupId = field("PrimaryReplicationGroupId")
    GlobalReplicationGroupDescription = field("GlobalReplicationGroupDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGlobalReplicationGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerNodeEndpoint:
    boto3_raw_data: "type_defs.CustomerNodeEndpointTypeDef" = dataclasses.field()

    Address = field("Address")
    Port = field("Port")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerNodeEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerNodeEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecreaseNodeGroupsInGlobalReplicationGroupMessage:
    boto3_raw_data: (
        "type_defs.DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef"
    ) = dataclasses.field()

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    NodeGroupCount = field("NodeGroupCount")
    ApplyImmediately = field("ApplyImmediately")
    GlobalNodeGroupsToRemove = field("GlobalNodeGroupsToRemove")
    GlobalNodeGroupsToRetain = field("GlobalNodeGroupsToRetain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef"
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
                "type_defs.DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheClusterMessage:
    boto3_raw_data: "type_defs.DeleteCacheClusterMessageTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    FinalSnapshotIdentifier = field("FinalSnapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCacheClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheParameterGroupMessage:
    boto3_raw_data: "type_defs.DeleteCacheParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCacheParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheSecurityGroupMessage:
    boto3_raw_data: "type_defs.DeleteCacheSecurityGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCacheSecurityGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheSubnetGroupMessage:
    boto3_raw_data: "type_defs.DeleteCacheSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSubnetGroupName = field("CacheSubnetGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCacheSubnetGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalReplicationGroupMessage:
    boto3_raw_data: "type_defs.DeleteGlobalReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    RetainPrimaryReplicationGroup = field("RetainPrimaryReplicationGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteGlobalReplicationGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationGroupMessage:
    boto3_raw_data: "type_defs.DeleteReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    RetainPrimaryCluster = field("RetainPrimaryCluster")
    FinalSnapshotIdentifier = field("FinalSnapshotIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteReplicationGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServerlessCacheRequest:
    boto3_raw_data: "type_defs.DeleteServerlessCacheRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")
    FinalSnapshotName = field("FinalSnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServerlessCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServerlessCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServerlessCacheSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteServerlessCacheSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServerlessCacheSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServerlessCacheSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotMessage:
    boto3_raw_data: "type_defs.DeleteSnapshotMessageTypeDef" = dataclasses.field()

    SnapshotName = field("SnapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserGroupMessage:
    boto3_raw_data: "type_defs.DeleteUserGroupMessageTypeDef" = dataclasses.field()

    UserGroupId = field("UserGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserMessage:
    boto3_raw_data: "type_defs.DeleteUserMessageTypeDef" = dataclasses.field()

    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserMessageTypeDef"]
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
class DescribeCacheClustersMessage:
    boto3_raw_data: "type_defs.DescribeCacheClustersMessageTypeDef" = (
        dataclasses.field()
    )

    CacheClusterId = field("CacheClusterId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    ShowCacheNodeInfo = field("ShowCacheNodeInfo")
    ShowCacheClustersNotInReplicationGroups = field(
        "ShowCacheClustersNotInReplicationGroups"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCacheClustersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheClustersMessageTypeDef"]
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
class DescribeCacheEngineVersionsMessage:
    boto3_raw_data: "type_defs.DescribeCacheEngineVersionsMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    DefaultOnly = field("DefaultOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheEngineVersionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheEngineVersionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheParameterGroupsMessage:
    boto3_raw_data: "type_defs.DescribeCacheParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheParameterGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheParametersMessage:
    boto3_raw_data: "type_defs.DescribeCacheParametersMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")
    Source = field("Source")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCacheParametersMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheSecurityGroupsMessage:
    boto3_raw_data: "type_defs.DescribeCacheSecurityGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheSecurityGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheSecurityGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheSubnetGroupsMessage:
    boto3_raw_data: "type_defs.DescribeCacheSubnetGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSubnetGroupName = field("CacheSubnetGroupName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCacheSubnetGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheSubnetGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultParametersMessage:
    boto3_raw_data: "type_defs.DescribeEngineDefaultParametersMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalReplicationGroupsMessage:
    boto3_raw_data: "type_defs.DescribeGlobalReplicationGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    ShowMemberInfo = field("ShowMemberInfo")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGlobalReplicationGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalReplicationGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationGroupsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReplicationGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedCacheNodesMessage:
    boto3_raw_data: "type_defs.DescribeReservedCacheNodesMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedCacheNodeId = field("ReservedCacheNodeId")
    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    CacheNodeType = field("CacheNodeType")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedCacheNodesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedCacheNodesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedCacheNodesOfferingsMessage:
    boto3_raw_data: "type_defs.DescribeReservedCacheNodesOfferingsMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    CacheNodeType = field("CacheNodeType")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedCacheNodesOfferingsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedCacheNodesOfferingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerlessCacheSnapshotsRequest:
    boto3_raw_data: "type_defs.DescribeServerlessCacheSnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")
    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")
    SnapshotType = field("SnapshotType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServerlessCacheSnapshotsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerlessCacheSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerlessCachesRequest:
    boto3_raw_data: "type_defs.DescribeServerlessCachesRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServerlessCachesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerlessCachesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceUpdatesMessage:
    boto3_raw_data: "type_defs.DescribeServiceUpdatesMessageTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ServiceUpdateStatus = field("ServiceUpdateStatus")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServiceUpdatesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceUpdatesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsMessage:
    boto3_raw_data: "type_defs.DescribeSnapshotsMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    CacheClusterId = field("CacheClusterId")
    SnapshotName = field("SnapshotName")
    SnapshotSource = field("SnapshotSource")
    Marker = field("Marker")
    MaxRecords = field("MaxRecords")
    ShowNodeGroupConfig = field("ShowNodeGroupConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserGroupsMessage:
    boto3_raw_data: "type_defs.DescribeUserGroupsMessageTypeDef" = dataclasses.field()

    UserGroupId = field("UserGroupId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserGroupsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserGroupsMessageTypeDef"]
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
class KinesisFirehoseDestinationDetails:
    boto3_raw_data: "type_defs.KinesisFirehoseDestinationDetailsTypeDef" = (
        dataclasses.field()
    )

    DeliveryStream = field("DeliveryStream")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisFirehoseDestinationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseDestinationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateGlobalReplicationGroupMessage:
    boto3_raw_data: "type_defs.DisassociateGlobalReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    ReplicationGroupId = field("ReplicationGroupId")
    ReplicationGroupRegion = field("ReplicationGroupRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateGlobalReplicationGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateGlobalReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    Message = field("Message")
    Date = field("Date")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportServerlessCacheSnapshotRequest:
    boto3_raw_data: "type_defs.ExportServerlessCacheSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")
    S3BucketName = field("S3BucketName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportServerlessCacheSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportServerlessCacheSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverGlobalReplicationGroupMessage:
    boto3_raw_data: "type_defs.FailoverGlobalReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    PrimaryRegion = field("PrimaryRegion")
    PrimaryReplicationGroupId = field("PrimaryReplicationGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailoverGlobalReplicationGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverGlobalReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalNodeGroup:
    boto3_raw_data: "type_defs.GlobalNodeGroupTypeDef" = dataclasses.field()

    GlobalNodeGroupId = field("GlobalNodeGroupId")
    Slots = field("Slots")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlobalNodeGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlobalNodeGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalReplicationGroupInfo:
    boto3_raw_data: "type_defs.GlobalReplicationGroupInfoTypeDef" = dataclasses.field()

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    GlobalReplicationGroupMemberRole = field("GlobalReplicationGroupMemberRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalReplicationGroupInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalReplicationGroupInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalReplicationGroupMember:
    boto3_raw_data: "type_defs.GlobalReplicationGroupMemberTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    ReplicationGroupRegion = field("ReplicationGroupRegion")
    Role = field("Role")
    AutomaticFailover = field("AutomaticFailover")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalReplicationGroupMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalReplicationGroupMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowedNodeTypeModificationsMessage:
    boto3_raw_data: "type_defs.ListAllowedNodeTypeModificationsMessageTypeDef" = (
        dataclasses.field()
    )

    CacheClusterId = field("CacheClusterId")
    ReplicationGroupId = field("ReplicationGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAllowedNodeTypeModificationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowedNodeTypeModificationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceMessage:
    boto3_raw_data: "type_defs.ListTagsForResourceMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleConfig:
    boto3_raw_data: "type_defs.ScaleConfigTypeDef" = dataclasses.field()

    ScalePercentage = field("ScalePercentage")
    ScaleIntervalMinutes = field("ScaleIntervalMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScaleConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScaleConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterNameValue:
    boto3_raw_data: "type_defs.ParameterNameValueTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterNameValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterNameValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCacheSubnetGroupMessage:
    boto3_raw_data: "type_defs.ModifyCacheSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSubnetGroupName = field("CacheSubnetGroupName")
    CacheSubnetGroupDescription = field("CacheSubnetGroupDescription")
    SubnetIds = field("SubnetIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyCacheSubnetGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCacheSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyGlobalReplicationGroupMessage:
    boto3_raw_data: "type_defs.ModifyGlobalReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    ApplyImmediately = field("ApplyImmediately")
    CacheNodeType = field("CacheNodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheParameterGroupName = field("CacheParameterGroupName")
    GlobalReplicationGroupDescription = field("GlobalReplicationGroupDescription")
    AutomaticFailoverEnabled = field("AutomaticFailoverEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyGlobalReplicationGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyGlobalReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReshardingConfiguration:
    boto3_raw_data: "type_defs.ReshardingConfigurationTypeDef" = dataclasses.field()

    NodeGroupId = field("NodeGroupId")
    PreferredAvailabilityZones = field("PreferredAvailabilityZones")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReshardingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReshardingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyUserGroupMessage:
    boto3_raw_data: "type_defs.ModifyUserGroupMessageTypeDef" = dataclasses.field()

    UserGroupId = field("UserGroupId")
    UserIdsToAdd = field("UserIdsToAdd")
    UserIdsToRemove = field("UserIdsToRemove")
    Engine = field("Engine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyUserGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyUserGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeGroupConfigurationOutput:
    boto3_raw_data: "type_defs.NodeGroupConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    NodeGroupId = field("NodeGroupId")
    Slots = field("Slots")
    ReplicaCount = field("ReplicaCount")
    PrimaryAvailabilityZone = field("PrimaryAvailabilityZone")
    ReplicaAvailabilityZones = field("ReplicaAvailabilityZones")
    PrimaryOutpostArn = field("PrimaryOutpostArn")
    ReplicaOutpostArns = field("ReplicaOutpostArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeGroupConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeGroupConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeGroupConfiguration:
    boto3_raw_data: "type_defs.NodeGroupConfigurationTypeDef" = dataclasses.field()

    NodeGroupId = field("NodeGroupId")
    Slots = field("Slots")
    ReplicaCount = field("ReplicaCount")
    PrimaryAvailabilityZone = field("PrimaryAvailabilityZone")
    ReplicaAvailabilityZones = field("ReplicaAvailabilityZones")
    PrimaryOutpostArn = field("PrimaryOutpostArn")
    ReplicaOutpostArns = field("ReplicaOutpostArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeGroupConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeGroupMemberUpdateStatus:
    boto3_raw_data: "type_defs.NodeGroupMemberUpdateStatusTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    CacheNodeId = field("CacheNodeId")
    NodeUpdateStatus = field("NodeUpdateStatus")
    NodeDeletionDate = field("NodeDeletionDate")
    NodeUpdateStartDate = field("NodeUpdateStartDate")
    NodeUpdateEndDate = field("NodeUpdateEndDate")
    NodeUpdateInitiatedBy = field("NodeUpdateInitiatedBy")
    NodeUpdateInitiatedDate = field("NodeUpdateInitiatedDate")
    NodeUpdateStatusModifiedDate = field("NodeUpdateStatusModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeGroupMemberUpdateStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeGroupMemberUpdateStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessedUpdateAction:
    boto3_raw_data: "type_defs.ProcessedUpdateActionTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    CacheClusterId = field("CacheClusterId")
    ServiceUpdateName = field("ServiceUpdateName")
    UpdateActionStatus = field("UpdateActionStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProcessedUpdateActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProcessedUpdateActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebalanceSlotsInGlobalReplicationGroupMessage:
    boto3_raw_data: "type_defs.RebalanceSlotsInGlobalReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    ApplyImmediately = field("ApplyImmediately")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RebalanceSlotsInGlobalReplicationGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebalanceSlotsInGlobalReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootCacheClusterMessage:
    boto3_raw_data: "type_defs.RebootCacheClusterMessageTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    CacheNodeIdsToReboot = field("CacheNodeIdsToReboot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootCacheClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootCacheClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurringCharge:
    boto3_raw_data: "type_defs.RecurringChargeTypeDef" = dataclasses.field()

    RecurringChargeAmount = field("RecurringChargeAmount")
    RecurringChargeFrequency = field("RecurringChargeFrequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecurringChargeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecurringChargeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromResourceMessage:
    boto3_raw_data: "type_defs.RemoveTagsFromResourceMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceName = field("ResourceName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveTagsFromResourceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserGroupsUpdateStatus:
    boto3_raw_data: "type_defs.UserGroupsUpdateStatusTypeDef" = dataclasses.field()

    UserGroupIdsToAdd = field("UserGroupIdsToAdd")
    UserGroupIdsToRemove = field("UserGroupIdsToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserGroupsUpdateStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserGroupsUpdateStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotMigration:
    boto3_raw_data: "type_defs.SlotMigrationTypeDef" = dataclasses.field()

    ProgressPercentage = field("ProgressPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotMigrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotMigrationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeCacheSecurityGroupIngressMessage:
    boto3_raw_data: "type_defs.RevokeCacheSecurityGroupIngressMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeCacheSecurityGroupIngressMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeCacheSecurityGroupIngressMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessCacheConfiguration:
    boto3_raw_data: "type_defs.ServerlessCacheConfigurationTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")
    Engine = field("Engine")
    MajorEngineVersion = field("MajorEngineVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerlessCacheConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessCacheConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceUpdate:
    boto3_raw_data: "type_defs.ServiceUpdateTypeDef" = dataclasses.field()

    ServiceUpdateName = field("ServiceUpdateName")
    ServiceUpdateReleaseDate = field("ServiceUpdateReleaseDate")
    ServiceUpdateEndDate = field("ServiceUpdateEndDate")
    ServiceUpdateSeverity = field("ServiceUpdateSeverity")
    ServiceUpdateRecommendedApplyByDate = field("ServiceUpdateRecommendedApplyByDate")
    ServiceUpdateStatus = field("ServiceUpdateStatus")
    ServiceUpdateDescription = field("ServiceUpdateDescription")
    ServiceUpdateType = field("ServiceUpdateType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    AutoUpdateAfterRecommendedApplyByDate = field(
        "AutoUpdateAfterRecommendedApplyByDate"
    )
    EstimatedUpdateTime = field("EstimatedUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubnetOutpost:
    boto3_raw_data: "type_defs.SubnetOutpostTypeDef" = dataclasses.field()

    SubnetOutpostArn = field("SubnetOutpostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetOutpostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetOutpostTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestFailoverMessage:
    boto3_raw_data: "type_defs.TestFailoverMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    NodeGroupId = field("NodeGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestFailoverMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestFailoverMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedUpdateAction:
    boto3_raw_data: "type_defs.UnprocessedUpdateActionTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    CacheClusterId = field("CacheClusterId")
    ServiceUpdateName = field("ServiceUpdateName")
    ErrorType = field("ErrorType")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedUpdateActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedUpdateActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserGroupPendingChanges:
    boto3_raw_data: "type_defs.UserGroupPendingChangesTypeDef" = dataclasses.field()

    UserIdsToRemove = field("UserIdsToRemove")
    UserIdsToAdd = field("UserIdsToAdd")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserGroupPendingChangesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserGroupPendingChangesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceMessage:
    boto3_raw_data: "type_defs.AddTagsToResourceMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyServerlessCacheSnapshotRequest:
    boto3_raw_data: "type_defs.CopyServerlessCacheSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    SourceServerlessCacheSnapshotName = field("SourceServerlessCacheSnapshotName")
    TargetServerlessCacheSnapshotName = field("TargetServerlessCacheSnapshotName")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyServerlessCacheSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyServerlessCacheSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotMessage:
    boto3_raw_data: "type_defs.CopySnapshotMessageTypeDef" = dataclasses.field()

    SourceSnapshotName = field("SourceSnapshotName")
    TargetSnapshotName = field("TargetSnapshotName")
    TargetBucket = field("TargetBucket")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheParameterGroupMessage:
    boto3_raw_data: "type_defs.CreateCacheParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")
    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCacheParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheSecurityGroupMessage:
    boto3_raw_data: "type_defs.CreateCacheSecurityGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCacheSecurityGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheSubnetGroupMessage:
    boto3_raw_data: "type_defs.CreateCacheSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheSubnetGroupName = field("CacheSubnetGroupName")
    CacheSubnetGroupDescription = field("CacheSubnetGroupDescription")
    SubnetIds = field("SubnetIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCacheSubnetGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServerlessCacheSnapshotRequest:
    boto3_raw_data: "type_defs.CreateServerlessCacheSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")
    ServerlessCacheName = field("ServerlessCacheName")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServerlessCacheSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServerlessCacheSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotMessage:
    boto3_raw_data: "type_defs.CreateSnapshotMessageTypeDef" = dataclasses.field()

    SnapshotName = field("SnapshotName")
    ReplicationGroupId = field("ReplicationGroupId")
    CacheClusterId = field("CacheClusterId")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserGroupMessage:
    boto3_raw_data: "type_defs.CreateUserGroupMessageTypeDef" = dataclasses.field()

    UserGroupId = field("UserGroupId")
    Engine = field("Engine")
    UserIds = field("UserIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedCacheNodesOfferingMessage:
    boto3_raw_data: "type_defs.PurchaseReservedCacheNodesOfferingMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    ReservedCacheNodeId = field("ReservedCacheNodeId")
    CacheNodeCount = field("CacheNodeCount")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedCacheNodesOfferingMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedCacheNodesOfferingMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedNodeTypeModificationsMessage:
    boto3_raw_data: "type_defs.AllowedNodeTypeModificationsMessageTypeDef" = (
        dataclasses.field()
    )

    ScaleUpModifications = field("ScaleUpModifications")
    ScaleDownModifications = field("ScaleDownModifications")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AllowedNodeTypeModificationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedNodeTypeModificationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheParameterGroupNameMessage:
    boto3_raw_data: "type_defs.CacheParameterGroupNameMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CacheParameterGroupNameMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheParameterGroupNameMessageTypeDef"]
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
class TagListMessage:
    boto3_raw_data: "type_defs.TagListMessageTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagListMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagListMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserMessage:
    boto3_raw_data: "type_defs.CreateUserMessageTypeDef" = dataclasses.field()

    UserId = field("UserId")
    UserName = field("UserName")
    Engine = field("Engine")
    AccessString = field("AccessString")
    Passwords = field("Passwords")
    NoPasswordRequired = field("NoPasswordRequired")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def AuthenticationMode(self):  # pragma: no cover
        return AuthenticationMode.make_one(self.boto3_raw_data["AuthenticationMode"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyUserMessage:
    boto3_raw_data: "type_defs.ModifyUserMessageTypeDef" = dataclasses.field()

    UserId = field("UserId")
    AccessString = field("AccessString")
    AppendAccessString = field("AppendAccessString")
    Passwords = field("Passwords")
    NoPasswordRequired = field("NoPasswordRequired")

    @cached_property
    def AuthenticationMode(self):  # pragma: no cover
        return AuthenticationMode.make_one(self.boto3_raw_data["AuthenticationMode"])

    Engine = field("Engine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModifyUserMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyUserMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserResponse:
    boto3_raw_data: "type_defs.UserResponseTypeDef" = dataclasses.field()

    UserId = field("UserId")
    UserName = field("UserName")
    Status = field("Status")
    Engine = field("Engine")
    MinimumEngineVersion = field("MinimumEngineVersion")
    AccessString = field("AccessString")
    UserGroupIds = field("UserGroupIds")

    @cached_property
    def Authentication(self):  # pragma: no cover
        return Authentication.make_one(self.boto3_raw_data["Authentication"])

    ARN = field("ARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    UserId = field("UserId")
    UserName = field("UserName")
    Status = field("Status")
    Engine = field("Engine")
    MinimumEngineVersion = field("MinimumEngineVersion")
    AccessString = field("AccessString")
    UserGroupIds = field("UserGroupIds")

    @cached_property
    def Authentication(self):  # pragma: no cover
        return Authentication.make_one(self.boto3_raw_data["Authentication"])

    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheNode:
    boto3_raw_data: "type_defs.CacheNodeTypeDef" = dataclasses.field()

    CacheNodeId = field("CacheNodeId")
    CacheNodeStatus = field("CacheNodeStatus")
    CacheNodeCreateTime = field("CacheNodeCreateTime")

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    ParameterGroupStatus = field("ParameterGroupStatus")
    SourceCacheNodeId = field("SourceCacheNodeId")
    CustomerAvailabilityZone = field("CustomerAvailabilityZone")
    CustomerOutpostArn = field("CustomerOutpostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheNodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeGroupMember:
    boto3_raw_data: "type_defs.NodeGroupMemberTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    CacheNodeId = field("CacheNodeId")

    @cached_property
    def ReadEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ReadEndpoint"])

    PreferredAvailabilityZone = field("PreferredAvailabilityZone")
    PreferredOutpostArn = field("PreferredOutpostArn")
    CurrentRole = field("CurrentRole")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeGroupMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeGroupMemberTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheEngineVersionMessage:
    boto3_raw_data: "type_defs.CacheEngineVersionMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def CacheEngineVersions(self):  # pragma: no cover
        return CacheEngineVersion.make_many(self.boto3_raw_data["CacheEngineVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheEngineVersionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheEngineVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheNodeTypeSpecificParameter:
    boto3_raw_data: "type_defs.CacheNodeTypeSpecificParameterTypeDef" = (
        dataclasses.field()
    )

    ParameterName = field("ParameterName")
    Description = field("Description")
    Source = field("Source")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    MinimumEngineVersion = field("MinimumEngineVersion")

    @cached_property
    def CacheNodeTypeSpecificValues(self):  # pragma: no cover
        return CacheNodeTypeSpecificValue.make_many(
            self.boto3_raw_data["CacheNodeTypeSpecificValues"]
        )

    ChangeType = field("ChangeType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CacheNodeTypeSpecificParameterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheNodeTypeSpecificParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheParameterGroupsMessage:
    boto3_raw_data: "type_defs.CacheParameterGroupsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def CacheParameterGroups(self):  # pragma: no cover
        return CacheParameterGroup.make_many(
            self.boto3_raw_data["CacheParameterGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheParameterGroupsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheParameterGroupResult:
    boto3_raw_data: "type_defs.CreateCacheParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CacheParameterGroup(self):  # pragma: no cover
        return CacheParameterGroup.make_one(self.boto3_raw_data["CacheParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCacheParameterGroupResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSecurityGroup:
    boto3_raw_data: "type_defs.CacheSecurityGroupTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CacheSecurityGroupName = field("CacheSecurityGroupName")
    Description = field("Description")

    @cached_property
    def EC2SecurityGroups(self):  # pragma: no cover
        return EC2SecurityGroup.make_many(self.boto3_raw_data["EC2SecurityGroups"])

    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheSecurityGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheSecurityGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheUsageLimits:
    boto3_raw_data: "type_defs.CacheUsageLimitsTypeDef" = dataclasses.field()

    @cached_property
    def DataStorage(self):  # pragma: no cover
        return DataStorage.make_one(self.boto3_raw_data["DataStorage"])

    @cached_property
    def ECPUPerSecond(self):  # pragma: no cover
        return ECPUPerSecond.make_one(self.boto3_raw_data["ECPUPerSecond"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheUsageLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheUsageLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecreaseReplicaCountMessage:
    boto3_raw_data: "type_defs.DecreaseReplicaCountMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    ApplyImmediately = field("ApplyImmediately")
    NewReplicaCount = field("NewReplicaCount")

    @cached_property
    def ReplicaConfiguration(self):  # pragma: no cover
        return ConfigureShard.make_many(self.boto3_raw_data["ReplicaConfiguration"])

    ReplicasToRemove = field("ReplicasToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DecreaseReplicaCountMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecreaseReplicaCountMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncreaseReplicaCountMessage:
    boto3_raw_data: "type_defs.IncreaseReplicaCountMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    ApplyImmediately = field("ApplyImmediately")
    NewReplicaCount = field("NewReplicaCount")

    @cached_property
    def ReplicaConfiguration(self):  # pragma: no cover
        return ConfigureShard.make_many(self.boto3_raw_data["ReplicaConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IncreaseReplicaCountMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncreaseReplicaCountMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMigrationMessage:
    boto3_raw_data: "type_defs.StartMigrationMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")

    @cached_property
    def CustomerNodeEndpointList(self):  # pragma: no cover
        return CustomerNodeEndpoint.make_many(
            self.boto3_raw_data["CustomerNodeEndpointList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestMigrationMessage:
    boto3_raw_data: "type_defs.TestMigrationMessageTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")

    @cached_property
    def CustomerNodeEndpointList(self):  # pragma: no cover
        return CustomerNodeEndpoint.make_many(
            self.boto3_raw_data["CustomerNodeEndpointList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheClustersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCacheClustersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    CacheClusterId = field("CacheClusterId")
    ShowCacheNodeInfo = field("ShowCacheNodeInfo")
    ShowCacheClustersNotInReplicationGroups = field(
        "ShowCacheClustersNotInReplicationGroups"
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheClustersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheClustersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheEngineVersionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCacheEngineVersionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    DefaultOnly = field("DefaultOnly")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheEngineVersionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheEngineVersionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheParameterGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCacheParameterGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheParameterGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheParameterGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheParametersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCacheParametersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")
    Source = field("Source")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheParametersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheParametersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheSecurityGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCacheSecurityGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    CacheSecurityGroupName = field("CacheSecurityGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheSecurityGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheSecurityGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheSubnetGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCacheSubnetGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    CacheSubnetGroupName = field("CacheSubnetGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheSubnetGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheSubnetGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultParametersMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeEngineDefaultParametersMessagePaginateTypeDef"
    ) = dataclasses.field()

    CacheParameterGroupFamily = field("CacheParameterGroupFamily")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultParametersMessagePaginateTypeDef"
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
                "type_defs.DescribeEngineDefaultParametersMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalReplicationGroupsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeGlobalReplicationGroupsMessagePaginateTypeDef"
    ) = dataclasses.field()

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    ShowMemberInfo = field("ShowMemberInfo")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGlobalReplicationGroupsMessagePaginateTypeDef"
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
                "type_defs.DescribeGlobalReplicationGroupsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReplicationGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedCacheNodesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReservedCacheNodesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReservedCacheNodeId = field("ReservedCacheNodeId")
    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    CacheNodeType = field("CacheNodeType")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedCacheNodesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedCacheNodesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedCacheNodesOfferingsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    CacheNodeType = field("CacheNodeType")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef"
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
                "type_defs.DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerlessCacheSnapshotsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeServerlessCacheSnapshotsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ServerlessCacheName = field("ServerlessCacheName")
    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")
    SnapshotType = field("SnapshotType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServerlessCacheSnapshotsRequestPaginateTypeDef"
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
                "type_defs.DescribeServerlessCacheSnapshotsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerlessCachesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeServerlessCachesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServerlessCachesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerlessCachesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceUpdatesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeServiceUpdatesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ServiceUpdateStatus = field("ServiceUpdateStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceUpdatesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceUpdatesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeSnapshotsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    CacheClusterId = field("CacheClusterId")
    SnapshotName = field("SnapshotName")
    SnapshotSource = field("SnapshotSource")
    ShowNodeGroupConfig = field("ShowNodeGroupConfig")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeUserGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    UserGroupId = field("UserGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheClustersMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeCacheClustersMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    CacheClusterId = field("CacheClusterId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    ShowCacheNodeInfo = field("ShowCacheNodeInfo")
    ShowCacheClustersNotInReplicationGroups = field(
        "ShowCacheClustersNotInReplicationGroups"
    )

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCacheClustersMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheClustersMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCacheClustersMessageWait:
    boto3_raw_data: "type_defs.DescribeCacheClustersMessageWaitTypeDef" = (
        dataclasses.field()
    )

    CacheClusterId = field("CacheClusterId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    ShowCacheNodeInfo = field("ShowCacheNodeInfo")
    ShowCacheClustersNotInReplicationGroups = field(
        "ShowCacheClustersNotInReplicationGroups"
    )

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCacheClustersMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCacheClustersMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationGroupsMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeReplicationGroupsMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationGroupsMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationGroupsMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationGroupsMessageWait:
    boto3_raw_data: "type_defs.DescribeReplicationGroupsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationGroupsMessageWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationGroupsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventsMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessage:
    boto3_raw_data: "type_defs.DescribeEventsMessageTypeDef" = dataclasses.field()

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRangeFilter:
    boto3_raw_data: "type_defs.TimeRangeFilterTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeUsersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    UserId = field("UserId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersMessagePaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersMessage:
    boto3_raw_data: "type_defs.DescribeUsersMessageTypeDef" = dataclasses.field()

    Engine = field("Engine")
    UserId = field("UserId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationDetails:
    boto3_raw_data: "type_defs.DestinationDetailsTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchLogsDetails(self):  # pragma: no cover
        return CloudWatchLogsDestinationDetails.make_one(
            self.boto3_raw_data["CloudWatchLogsDetails"]
        )

    @cached_property
    def KinesisFirehoseDetails(self):  # pragma: no cover
        return KinesisFirehoseDestinationDetails.make_one(
            self.boto3_raw_data["KinesisFirehoseDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsMessage:
    boto3_raw_data: "type_defs.EventsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventsMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventsMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalReplicationGroup:
    boto3_raw_data: "type_defs.GlobalReplicationGroupTypeDef" = dataclasses.field()

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    GlobalReplicationGroupDescription = field("GlobalReplicationGroupDescription")
    Status = field("Status")
    CacheNodeType = field("CacheNodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")

    @cached_property
    def Members(self):  # pragma: no cover
        return GlobalReplicationGroupMember.make_many(self.boto3_raw_data["Members"])

    ClusterEnabled = field("ClusterEnabled")

    @cached_property
    def GlobalNodeGroups(self):  # pragma: no cover
        return GlobalNodeGroup.make_many(self.boto3_raw_data["GlobalNodeGroups"])

    AuthTokenEnabled = field("AuthTokenEnabled")
    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    AtRestEncryptionEnabled = field("AtRestEncryptionEnabled")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalReplicationGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalReplicationGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCacheParameterGroupMessage:
    boto3_raw_data: "type_defs.ModifyCacheParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")

    @cached_property
    def ParameterNameValues(self):  # pragma: no cover
        return ParameterNameValue.make_many(self.boto3_raw_data["ParameterNameValues"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyCacheParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCacheParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetCacheParameterGroupMessage:
    boto3_raw_data: "type_defs.ResetCacheParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    CacheParameterGroupName = field("CacheParameterGroupName")
    ResetAllParameters = field("ResetAllParameters")

    @cached_property
    def ParameterNameValues(self):  # pragma: no cover
        return ParameterNameValue.make_many(self.boto3_raw_data["ParameterNameValues"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResetCacheParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetCacheParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationGroupShardConfigurationMessage:
    boto3_raw_data: (
        "type_defs.ModifyReplicationGroupShardConfigurationMessageTypeDef"
    ) = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    NodeGroupCount = field("NodeGroupCount")
    ApplyImmediately = field("ApplyImmediately")

    @cached_property
    def ReshardingConfiguration(self):  # pragma: no cover
        return ReshardingConfiguration.make_many(
            self.boto3_raw_data["ReshardingConfiguration"]
        )

    NodeGroupsToRemove = field("NodeGroupsToRemove")
    NodeGroupsToRetain = field("NodeGroupsToRetain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyReplicationGroupShardConfigurationMessageTypeDef"
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
                "type_defs.ModifyReplicationGroupShardConfigurationMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionalConfiguration:
    boto3_raw_data: "type_defs.RegionalConfigurationTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    ReplicationGroupRegion = field("ReplicationGroupRegion")

    @cached_property
    def ReshardingConfiguration(self):  # pragma: no cover
        return ReshardingConfiguration.make_many(
            self.boto3_raw_data["ReshardingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegionalConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeSnapshot:
    boto3_raw_data: "type_defs.NodeSnapshotTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    NodeGroupId = field("NodeGroupId")
    CacheNodeId = field("CacheNodeId")

    @cached_property
    def NodeGroupConfiguration(self):  # pragma: no cover
        return NodeGroupConfigurationOutput.make_one(
            self.boto3_raw_data["NodeGroupConfiguration"]
        )

    CacheSize = field("CacheSize")
    CacheNodeCreateTime = field("CacheNodeCreateTime")
    SnapshotCreateTime = field("SnapshotCreateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeSnapshotTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeGroupUpdateStatus:
    boto3_raw_data: "type_defs.NodeGroupUpdateStatusTypeDef" = dataclasses.field()

    NodeGroupId = field("NodeGroupId")

    @cached_property
    def NodeGroupMemberUpdateStatus(self):  # pragma: no cover
        return NodeGroupMemberUpdateStatus.make_many(
            self.boto3_raw_data["NodeGroupMemberUpdateStatus"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeGroupUpdateStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeGroupUpdateStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedCacheNode:
    boto3_raw_data: "type_defs.ReservedCacheNodeTypeDef" = dataclasses.field()

    ReservedCacheNodeId = field("ReservedCacheNodeId")
    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    CacheNodeType = field("CacheNodeType")
    StartTime = field("StartTime")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CacheNodeCount = field("CacheNodeCount")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    State = field("State")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    ReservationARN = field("ReservationARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservedCacheNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedCacheNodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedCacheNodesOffering:
    boto3_raw_data: "type_defs.ReservedCacheNodesOfferingTypeDef" = dataclasses.field()

    ReservedCacheNodesOfferingId = field("ReservedCacheNodesOfferingId")
    CacheNodeType = field("CacheNodeType")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedCacheNodesOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedCacheNodesOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReshardingStatus:
    boto3_raw_data: "type_defs.ReshardingStatusTypeDef" = dataclasses.field()

    @cached_property
    def SlotMigration(self):  # pragma: no cover
        return SlotMigration.make_one(self.boto3_raw_data["SlotMigration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReshardingStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReshardingStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessCacheSnapshot:
    boto3_raw_data: "type_defs.ServerlessCacheSnapshotTypeDef" = dataclasses.field()

    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")
    ARN = field("ARN")
    KmsKeyId = field("KmsKeyId")
    SnapshotType = field("SnapshotType")
    Status = field("Status")
    CreateTime = field("CreateTime")
    ExpiryTime = field("ExpiryTime")
    BytesUsedForCache = field("BytesUsedForCache")

    @cached_property
    def ServerlessCacheConfiguration(self):  # pragma: no cover
        return ServerlessCacheConfiguration.make_one(
            self.boto3_raw_data["ServerlessCacheConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerlessCacheSnapshotTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessCacheSnapshotTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceUpdatesMessage:
    boto3_raw_data: "type_defs.ServiceUpdatesMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ServiceUpdates(self):  # pragma: no cover
        return ServiceUpdate.make_many(self.boto3_raw_data["ServiceUpdates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceUpdatesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceUpdatesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subnet:
    boto3_raw_data: "type_defs.SubnetTypeDef" = dataclasses.field()

    SubnetIdentifier = field("SubnetIdentifier")

    @cached_property
    def SubnetAvailabilityZone(self):  # pragma: no cover
        return AvailabilityZone.make_one(self.boto3_raw_data["SubnetAvailabilityZone"])

    @cached_property
    def SubnetOutpost(self):  # pragma: no cover
        return SubnetOutpost.make_one(self.boto3_raw_data["SubnetOutpost"])

    SupportedNetworkTypes = field("SupportedNetworkTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateActionResultsMessage:
    boto3_raw_data: "type_defs.UpdateActionResultsMessageTypeDef" = dataclasses.field()

    @cached_property
    def ProcessedUpdateActions(self):  # pragma: no cover
        return ProcessedUpdateAction.make_many(
            self.boto3_raw_data["ProcessedUpdateActions"]
        )

    @cached_property
    def UnprocessedUpdateActions(self):  # pragma: no cover
        return UnprocessedUpdateAction.make_many(
            self.boto3_raw_data["UnprocessedUpdateActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateActionResultsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateActionResultsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserGroupResponse:
    boto3_raw_data: "type_defs.UserGroupResponseTypeDef" = dataclasses.field()

    UserGroupId = field("UserGroupId")
    Status = field("Status")
    Engine = field("Engine")
    UserIds = field("UserIds")
    MinimumEngineVersion = field("MinimumEngineVersion")

    @cached_property
    def PendingChanges(self):  # pragma: no cover
        return UserGroupPendingChanges.make_one(self.boto3_raw_data["PendingChanges"])

    ReplicationGroups = field("ReplicationGroups")
    ServerlessCaches = field("ServerlessCaches")
    ARN = field("ARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserGroupResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserGroup:
    boto3_raw_data: "type_defs.UserGroupTypeDef" = dataclasses.field()

    UserGroupId = field("UserGroupId")
    Status = field("Status")
    Engine = field("Engine")
    UserIds = field("UserIds")
    MinimumEngineVersion = field("MinimumEngineVersion")

    @cached_property
    def PendingChanges(self):  # pragma: no cover
        return UserGroupPendingChanges.make_one(self.boto3_raw_data["PendingChanges"])

    ReplicationGroups = field("ReplicationGroups")
    ServerlessCaches = field("ServerlessCaches")
    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersResult:
    boto3_raw_data: "type_defs.DescribeUsersResultTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeGroup:
    boto3_raw_data: "type_defs.NodeGroupTypeDef" = dataclasses.field()

    NodeGroupId = field("NodeGroupId")
    Status = field("Status")

    @cached_property
    def PrimaryEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["PrimaryEndpoint"])

    @cached_property
    def ReaderEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ReaderEndpoint"])

    Slots = field("Slots")

    @cached_property
    def NodeGroupMembers(self):  # pragma: no cover
        return NodeGroupMember.make_many(self.boto3_raw_data["NodeGroupMembers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheParameterGroupDetails:
    boto3_raw_data: "type_defs.CacheParameterGroupDetailsTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def CacheNodeTypeSpecificParameters(self):  # pragma: no cover
        return CacheNodeTypeSpecificParameter.make_many(
            self.boto3_raw_data["CacheNodeTypeSpecificParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheParameterGroupDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheParameterGroupDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineDefaults:
    boto3_raw_data: "type_defs.EngineDefaultsTypeDef" = dataclasses.field()

    CacheParameterGroupFamily = field("CacheParameterGroupFamily")
    Marker = field("Marker")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def CacheNodeTypeSpecificParameters(self):  # pragma: no cover
        return CacheNodeTypeSpecificParameter.make_many(
            self.boto3_raw_data["CacheNodeTypeSpecificParameters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineDefaultsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngineDefaultsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeCacheSecurityGroupIngressResult:
    boto3_raw_data: "type_defs.AuthorizeCacheSecurityGroupIngressResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CacheSecurityGroup(self):  # pragma: no cover
        return CacheSecurityGroup.make_one(self.boto3_raw_data["CacheSecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeCacheSecurityGroupIngressResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeCacheSecurityGroupIngressResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSecurityGroupMessage:
    boto3_raw_data: "type_defs.CacheSecurityGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def CacheSecurityGroups(self):  # pragma: no cover
        return CacheSecurityGroup.make_many(self.boto3_raw_data["CacheSecurityGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheSecurityGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheSecurityGroupResult:
    boto3_raw_data: "type_defs.CreateCacheSecurityGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CacheSecurityGroup(self):  # pragma: no cover
        return CacheSecurityGroup.make_one(self.boto3_raw_data["CacheSecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCacheSecurityGroupResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheSecurityGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeCacheSecurityGroupIngressResult:
    boto3_raw_data: "type_defs.RevokeCacheSecurityGroupIngressResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CacheSecurityGroup(self):  # pragma: no cover
        return CacheSecurityGroup.make_one(self.boto3_raw_data["CacheSecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeCacheSecurityGroupIngressResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeCacheSecurityGroupIngressResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServerlessCacheRequest:
    boto3_raw_data: "type_defs.CreateServerlessCacheRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")
    Engine = field("Engine")
    Description = field("Description")
    MajorEngineVersion = field("MajorEngineVersion")

    @cached_property
    def CacheUsageLimits(self):  # pragma: no cover
        return CacheUsageLimits.make_one(self.boto3_raw_data["CacheUsageLimits"])

    KmsKeyId = field("KmsKeyId")
    SecurityGroupIds = field("SecurityGroupIds")
    SnapshotArnsToRestore = field("SnapshotArnsToRestore")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    UserGroupId = field("UserGroupId")
    SubnetIds = field("SubnetIds")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    DailySnapshotTime = field("DailySnapshotTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServerlessCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServerlessCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyServerlessCacheRequest:
    boto3_raw_data: "type_defs.ModifyServerlessCacheRequestTypeDef" = (
        dataclasses.field()
    )

    ServerlessCacheName = field("ServerlessCacheName")
    Description = field("Description")

    @cached_property
    def CacheUsageLimits(self):  # pragma: no cover
        return CacheUsageLimits.make_one(self.boto3_raw_data["CacheUsageLimits"])

    RemoveUserGroup = field("RemoveUserGroup")
    UserGroupId = field("UserGroupId")
    SecurityGroupIds = field("SecurityGroupIds")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    DailySnapshotTime = field("DailySnapshotTime")
    Engine = field("Engine")
    MajorEngineVersion = field("MajorEngineVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyServerlessCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyServerlessCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessCache:
    boto3_raw_data: "type_defs.ServerlessCacheTypeDef" = dataclasses.field()

    ServerlessCacheName = field("ServerlessCacheName")
    Description = field("Description")
    CreateTime = field("CreateTime")
    Status = field("Status")
    Engine = field("Engine")
    MajorEngineVersion = field("MajorEngineVersion")
    FullEngineVersion = field("FullEngineVersion")

    @cached_property
    def CacheUsageLimits(self):  # pragma: no cover
        return CacheUsageLimits.make_one(self.boto3_raw_data["CacheUsageLimits"])

    KmsKeyId = field("KmsKeyId")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    @cached_property
    def ReaderEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ReaderEndpoint"])

    ARN = field("ARN")
    UserGroupId = field("UserGroupId")
    SubnetIds = field("SubnetIds")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    DailySnapshotTime = field("DailySnapshotTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerlessCacheTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerlessCacheTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateActionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeUpdateActionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ReplicationGroupIds = field("ReplicationGroupIds")
    CacheClusterIds = field("CacheClusterIds")
    Engine = field("Engine")
    ServiceUpdateStatus = field("ServiceUpdateStatus")

    @cached_property
    def ServiceUpdateTimeRange(self):  # pragma: no cover
        return TimeRangeFilter.make_one(self.boto3_raw_data["ServiceUpdateTimeRange"])

    UpdateActionStatus = field("UpdateActionStatus")
    ShowNodeLevelUpdateStatus = field("ShowNodeLevelUpdateStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUpdateActionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateActionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateActionsMessage:
    boto3_raw_data: "type_defs.DescribeUpdateActionsMessageTypeDef" = (
        dataclasses.field()
    )

    ServiceUpdateName = field("ServiceUpdateName")
    ReplicationGroupIds = field("ReplicationGroupIds")
    CacheClusterIds = field("CacheClusterIds")
    Engine = field("Engine")
    ServiceUpdateStatus = field("ServiceUpdateStatus")

    @cached_property
    def ServiceUpdateTimeRange(self):  # pragma: no cover
        return TimeRangeFilter.make_one(self.boto3_raw_data["ServiceUpdateTimeRange"])

    UpdateActionStatus = field("UpdateActionStatus")
    ShowNodeLevelUpdateStatus = field("ShowNodeLevelUpdateStatus")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUpdateActionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDeliveryConfigurationRequest:
    boto3_raw_data: "type_defs.LogDeliveryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    LogType = field("LogType")
    DestinationType = field("DestinationType")

    @cached_property
    def DestinationDetails(self):  # pragma: no cover
        return DestinationDetails.make_one(self.boto3_raw_data["DestinationDetails"])

    LogFormat = field("LogFormat")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LogDeliveryConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDeliveryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDeliveryConfiguration:
    boto3_raw_data: "type_defs.LogDeliveryConfigurationTypeDef" = dataclasses.field()

    LogType = field("LogType")
    DestinationType = field("DestinationType")

    @cached_property
    def DestinationDetails(self):  # pragma: no cover
        return DestinationDetails.make_one(self.boto3_raw_data["DestinationDetails"])

    LogFormat = field("LogFormat")
    Status = field("Status")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogDeliveryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingLogDeliveryConfiguration:
    boto3_raw_data: "type_defs.PendingLogDeliveryConfigurationTypeDef" = (
        dataclasses.field()
    )

    LogType = field("LogType")
    DestinationType = field("DestinationType")

    @cached_property
    def DestinationDetails(self):  # pragma: no cover
        return DestinationDetails.make_one(self.boto3_raw_data["DestinationDetails"])

    LogFormat = field("LogFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PendingLogDeliveryConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingLogDeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalReplicationGroupResult:
    boto3_raw_data: "type_defs.CreateGlobalReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGlobalReplicationGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecreaseNodeGroupsInGlobalReplicationGroupResult:
    boto3_raw_data: (
        "type_defs.DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef"
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
                "type_defs.DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalReplicationGroupResult:
    boto3_raw_data: "type_defs.DeleteGlobalReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteGlobalReplicationGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalReplicationGroupsResult:
    boto3_raw_data: "type_defs.DescribeGlobalReplicationGroupsResultTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def GlobalReplicationGroups(self):  # pragma: no cover
        return GlobalReplicationGroup.make_many(
            self.boto3_raw_data["GlobalReplicationGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGlobalReplicationGroupsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalReplicationGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateGlobalReplicationGroupResult:
    boto3_raw_data: "type_defs.DisassociateGlobalReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateGlobalReplicationGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateGlobalReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverGlobalReplicationGroupResult:
    boto3_raw_data: "type_defs.FailoverGlobalReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailoverGlobalReplicationGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverGlobalReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncreaseNodeGroupsInGlobalReplicationGroupResult:
    boto3_raw_data: (
        "type_defs.IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef"
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
                "type_defs.IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyGlobalReplicationGroupResult:
    boto3_raw_data: "type_defs.ModifyGlobalReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyGlobalReplicationGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyGlobalReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebalanceSlotsInGlobalReplicationGroupResult:
    boto3_raw_data: "type_defs.RebalanceSlotsInGlobalReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalReplicationGroup(self):  # pragma: no cover
        return GlobalReplicationGroup.make_one(
            self.boto3_raw_data["GlobalReplicationGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RebalanceSlotsInGlobalReplicationGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebalanceSlotsInGlobalReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncreaseNodeGroupsInGlobalReplicationGroupMessage:
    boto3_raw_data: (
        "type_defs.IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef"
    ) = dataclasses.field()

    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    NodeGroupCount = field("NodeGroupCount")
    ApplyImmediately = field("ApplyImmediately")

    @cached_property
    def RegionalConfigurations(self):  # pragma: no cover
        return RegionalConfiguration.make_many(
            self.boto3_raw_data["RegionalConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef"
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
                "type_defs.IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Snapshot:
    boto3_raw_data: "type_defs.SnapshotTypeDef" = dataclasses.field()

    SnapshotName = field("SnapshotName")
    ReplicationGroupId = field("ReplicationGroupId")
    ReplicationGroupDescription = field("ReplicationGroupDescription")
    CacheClusterId = field("CacheClusterId")
    SnapshotStatus = field("SnapshotStatus")
    SnapshotSource = field("SnapshotSource")
    CacheNodeType = field("CacheNodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    NumCacheNodes = field("NumCacheNodes")
    PreferredAvailabilityZone = field("PreferredAvailabilityZone")
    PreferredOutpostArn = field("PreferredOutpostArn")
    CacheClusterCreateTime = field("CacheClusterCreateTime")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    TopicArn = field("TopicArn")
    Port = field("Port")
    CacheParameterGroupName = field("CacheParameterGroupName")
    CacheSubnetGroupName = field("CacheSubnetGroupName")
    VpcId = field("VpcId")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    NumNodeGroups = field("NumNodeGroups")
    AutomaticFailover = field("AutomaticFailover")

    @cached_property
    def NodeSnapshots(self):  # pragma: no cover
        return NodeSnapshot.make_many(self.boto3_raw_data["NodeSnapshots"])

    KmsKeyId = field("KmsKeyId")
    ARN = field("ARN")
    DataTiering = field("DataTiering")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAction:
    boto3_raw_data: "type_defs.UpdateActionTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    CacheClusterId = field("CacheClusterId")
    ServiceUpdateName = field("ServiceUpdateName")
    ServiceUpdateReleaseDate = field("ServiceUpdateReleaseDate")
    ServiceUpdateSeverity = field("ServiceUpdateSeverity")
    ServiceUpdateStatus = field("ServiceUpdateStatus")
    ServiceUpdateRecommendedApplyByDate = field("ServiceUpdateRecommendedApplyByDate")
    ServiceUpdateType = field("ServiceUpdateType")
    UpdateActionAvailableDate = field("UpdateActionAvailableDate")
    UpdateActionStatus = field("UpdateActionStatus")
    NodesUpdated = field("NodesUpdated")
    UpdateActionStatusModifiedDate = field("UpdateActionStatusModifiedDate")
    SlaMet = field("SlaMet")

    @cached_property
    def NodeGroupUpdateStatus(self):  # pragma: no cover
        return NodeGroupUpdateStatus.make_many(
            self.boto3_raw_data["NodeGroupUpdateStatus"]
        )

    @cached_property
    def CacheNodeUpdateStatus(self):  # pragma: no cover
        return CacheNodeUpdateStatus.make_many(
            self.boto3_raw_data["CacheNodeUpdateStatus"]
        )

    EstimatedUpdateTime = field("EstimatedUpdateTime")
    Engine = field("Engine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedCacheNodesOfferingResult:
    boto3_raw_data: "type_defs.PurchaseReservedCacheNodesOfferingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedCacheNode(self):  # pragma: no cover
        return ReservedCacheNode.make_one(self.boto3_raw_data["ReservedCacheNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedCacheNodesOfferingResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedCacheNodesOfferingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedCacheNodeMessage:
    boto3_raw_data: "type_defs.ReservedCacheNodeMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ReservedCacheNodes(self):  # pragma: no cover
        return ReservedCacheNode.make_many(self.boto3_raw_data["ReservedCacheNodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedCacheNodeMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedCacheNodeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedCacheNodesOfferingMessage:
    boto3_raw_data: "type_defs.ReservedCacheNodesOfferingMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReservedCacheNodesOfferings(self):  # pragma: no cover
        return ReservedCacheNodesOffering.make_many(
            self.boto3_raw_data["ReservedCacheNodesOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservedCacheNodesOfferingMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedCacheNodesOfferingMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyServerlessCacheSnapshotResponse:
    boto3_raw_data: "type_defs.CopyServerlessCacheSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCacheSnapshot(self):  # pragma: no cover
        return ServerlessCacheSnapshot.make_one(
            self.boto3_raw_data["ServerlessCacheSnapshot"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyServerlessCacheSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyServerlessCacheSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServerlessCacheSnapshotResponse:
    boto3_raw_data: "type_defs.CreateServerlessCacheSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCacheSnapshot(self):  # pragma: no cover
        return ServerlessCacheSnapshot.make_one(
            self.boto3_raw_data["ServerlessCacheSnapshot"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServerlessCacheSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServerlessCacheSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServerlessCacheSnapshotResponse:
    boto3_raw_data: "type_defs.DeleteServerlessCacheSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCacheSnapshot(self):  # pragma: no cover
        return ServerlessCacheSnapshot.make_one(
            self.boto3_raw_data["ServerlessCacheSnapshot"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServerlessCacheSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServerlessCacheSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerlessCacheSnapshotsResponse:
    boto3_raw_data: "type_defs.DescribeServerlessCacheSnapshotsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCacheSnapshots(self):  # pragma: no cover
        return ServerlessCacheSnapshot.make_many(
            self.boto3_raw_data["ServerlessCacheSnapshots"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServerlessCacheSnapshotsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerlessCacheSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportServerlessCacheSnapshotResponse:
    boto3_raw_data: "type_defs.ExportServerlessCacheSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCacheSnapshot(self):  # pragma: no cover
        return ServerlessCacheSnapshot.make_one(
            self.boto3_raw_data["ServerlessCacheSnapshot"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportServerlessCacheSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportServerlessCacheSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSubnetGroup:
    boto3_raw_data: "type_defs.CacheSubnetGroupTypeDef" = dataclasses.field()

    CacheSubnetGroupName = field("CacheSubnetGroupName")
    CacheSubnetGroupDescription = field("CacheSubnetGroupDescription")
    VpcId = field("VpcId")

    @cached_property
    def Subnets(self):  # pragma: no cover
        return Subnet.make_many(self.boto3_raw_data["Subnets"])

    ARN = field("ARN")
    SupportedNetworkTypes = field("SupportedNetworkTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheSubnetGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheSubnetGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserGroupsResult:
    boto3_raw_data: "type_defs.DescribeUserGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def UserGroups(self):  # pragma: no cover
        return UserGroup.make_many(self.boto3_raw_data["UserGroups"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultParametersResult:
    boto3_raw_data: "type_defs.DescribeEngineDefaultParametersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngineDefaults(self):  # pragma: no cover
        return EngineDefaults.make_one(self.boto3_raw_data["EngineDefaults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServerlessCacheResponse:
    boto3_raw_data: "type_defs.CreateServerlessCacheResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCache(self):  # pragma: no cover
        return ServerlessCache.make_one(self.boto3_raw_data["ServerlessCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServerlessCacheResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServerlessCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServerlessCacheResponse:
    boto3_raw_data: "type_defs.DeleteServerlessCacheResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCache(self):  # pragma: no cover
        return ServerlessCache.make_one(self.boto3_raw_data["ServerlessCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServerlessCacheResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServerlessCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServerlessCachesResponse:
    boto3_raw_data: "type_defs.DescribeServerlessCachesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCaches(self):  # pragma: no cover
        return ServerlessCache.make_many(self.boto3_raw_data["ServerlessCaches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServerlessCachesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServerlessCachesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyServerlessCacheResponse:
    boto3_raw_data: "type_defs.ModifyServerlessCacheResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerlessCache(self):  # pragma: no cover
        return ServerlessCache.make_one(self.boto3_raw_data["ServerlessCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyServerlessCacheResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyServerlessCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheClusterMessage:
    boto3_raw_data: "type_defs.CreateCacheClusterMessageTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    ReplicationGroupId = field("ReplicationGroupId")
    AZMode = field("AZMode")
    PreferredAvailabilityZone = field("PreferredAvailabilityZone")
    PreferredAvailabilityZones = field("PreferredAvailabilityZones")
    NumCacheNodes = field("NumCacheNodes")
    CacheNodeType = field("CacheNodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheParameterGroupName = field("CacheParameterGroupName")
    CacheSubnetGroupName = field("CacheSubnetGroupName")
    CacheSecurityGroupNames = field("CacheSecurityGroupNames")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SnapshotArns = field("SnapshotArns")
    SnapshotName = field("SnapshotName")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    Port = field("Port")
    NotificationTopicArn = field("NotificationTopicArn")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    AuthToken = field("AuthToken")
    OutpostMode = field("OutpostMode")
    PreferredOutpostArn = field("PreferredOutpostArn")
    PreferredOutpostArns = field("PreferredOutpostArns")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return LogDeliveryConfigurationRequest.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    NetworkType = field("NetworkType")
    IpDiscovery = field("IpDiscovery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCacheClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationGroupMessage:
    boto3_raw_data: "type_defs.CreateReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    ReplicationGroupDescription = field("ReplicationGroupDescription")
    GlobalReplicationGroupId = field("GlobalReplicationGroupId")
    PrimaryClusterId = field("PrimaryClusterId")
    AutomaticFailoverEnabled = field("AutomaticFailoverEnabled")
    MultiAZEnabled = field("MultiAZEnabled")
    NumCacheClusters = field("NumCacheClusters")
    PreferredCacheClusterAZs = field("PreferredCacheClusterAZs")
    NumNodeGroups = field("NumNodeGroups")
    ReplicasPerNodeGroup = field("ReplicasPerNodeGroup")
    NodeGroupConfiguration = field("NodeGroupConfiguration")
    CacheNodeType = field("CacheNodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheParameterGroupName = field("CacheParameterGroupName")
    CacheSubnetGroupName = field("CacheSubnetGroupName")
    CacheSecurityGroupNames = field("CacheSecurityGroupNames")
    SecurityGroupIds = field("SecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SnapshotArns = field("SnapshotArns")
    SnapshotName = field("SnapshotName")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    Port = field("Port")
    NotificationTopicArn = field("NotificationTopicArn")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    AuthToken = field("AuthToken")
    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    AtRestEncryptionEnabled = field("AtRestEncryptionEnabled")
    KmsKeyId = field("KmsKeyId")
    UserGroupIds = field("UserGroupIds")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return LogDeliveryConfigurationRequest.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    DataTieringEnabled = field("DataTieringEnabled")
    NetworkType = field("NetworkType")
    IpDiscovery = field("IpDiscovery")
    TransitEncryptionMode = field("TransitEncryptionMode")
    ClusterMode = field("ClusterMode")
    ServerlessCacheSnapshotName = field("ServerlessCacheSnapshotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateReplicationGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCacheClusterMessage:
    boto3_raw_data: "type_defs.ModifyCacheClusterMessageTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")
    NumCacheNodes = field("NumCacheNodes")
    CacheNodeIdsToRemove = field("CacheNodeIdsToRemove")
    AZMode = field("AZMode")
    NewAvailabilityZones = field("NewAvailabilityZones")
    CacheSecurityGroupNames = field("CacheSecurityGroupNames")
    SecurityGroupIds = field("SecurityGroupIds")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    NotificationTopicArn = field("NotificationTopicArn")
    CacheParameterGroupName = field("CacheParameterGroupName")
    NotificationTopicStatus = field("NotificationTopicStatus")
    ApplyImmediately = field("ApplyImmediately")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    CacheNodeType = field("CacheNodeType")
    AuthToken = field("AuthToken")
    AuthTokenUpdateStrategy = field("AuthTokenUpdateStrategy")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return LogDeliveryConfigurationRequest.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    IpDiscovery = field("IpDiscovery")

    @cached_property
    def ScaleConfig(self):  # pragma: no cover
        return ScaleConfig.make_one(self.boto3_raw_data["ScaleConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyCacheClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCacheClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationGroupMessage:
    boto3_raw_data: "type_defs.ModifyReplicationGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationGroupId = field("ReplicationGroupId")
    ReplicationGroupDescription = field("ReplicationGroupDescription")
    PrimaryClusterId = field("PrimaryClusterId")
    SnapshottingClusterId = field("SnapshottingClusterId")
    AutomaticFailoverEnabled = field("AutomaticFailoverEnabled")
    MultiAZEnabled = field("MultiAZEnabled")
    NodeGroupId = field("NodeGroupId")
    CacheSecurityGroupNames = field("CacheSecurityGroupNames")
    SecurityGroupIds = field("SecurityGroupIds")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    NotificationTopicArn = field("NotificationTopicArn")
    CacheParameterGroupName = field("CacheParameterGroupName")
    NotificationTopicStatus = field("NotificationTopicStatus")
    ApplyImmediately = field("ApplyImmediately")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    CacheNodeType = field("CacheNodeType")
    AuthToken = field("AuthToken")
    AuthTokenUpdateStrategy = field("AuthTokenUpdateStrategy")
    UserGroupIdsToAdd = field("UserGroupIdsToAdd")
    UserGroupIdsToRemove = field("UserGroupIdsToRemove")
    RemoveUserGroups = field("RemoveUserGroups")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return LogDeliveryConfigurationRequest.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    IpDiscovery = field("IpDiscovery")
    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    TransitEncryptionMode = field("TransitEncryptionMode")
    ClusterMode = field("ClusterMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyReplicationGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingModifiedValues:
    boto3_raw_data: "type_defs.PendingModifiedValuesTypeDef" = dataclasses.field()

    NumCacheNodes = field("NumCacheNodes")
    CacheNodeIdsToRemove = field("CacheNodeIdsToRemove")
    EngineVersion = field("EngineVersion")
    CacheNodeType = field("CacheNodeType")
    AuthTokenStatus = field("AuthTokenStatus")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return PendingLogDeliveryConfiguration.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    TransitEncryptionMode = field("TransitEncryptionMode")

    @cached_property
    def ScaleConfig(self):  # pragma: no cover
        return ScaleConfig.make_one(self.boto3_raw_data["ScaleConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingModifiedValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationGroupPendingModifiedValues:
    boto3_raw_data: "type_defs.ReplicationGroupPendingModifiedValuesTypeDef" = (
        dataclasses.field()
    )

    PrimaryClusterId = field("PrimaryClusterId")
    AutomaticFailoverStatus = field("AutomaticFailoverStatus")

    @cached_property
    def Resharding(self):  # pragma: no cover
        return ReshardingStatus.make_one(self.boto3_raw_data["Resharding"])

    AuthTokenStatus = field("AuthTokenStatus")

    @cached_property
    def UserGroups(self):  # pragma: no cover
        return UserGroupsUpdateStatus.make_one(self.boto3_raw_data["UserGroups"])

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return PendingLogDeliveryConfiguration.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    TransitEncryptionMode = field("TransitEncryptionMode")
    ClusterMode = field("ClusterMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationGroupPendingModifiedValuesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationGroupPendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySnapshotResult:
    boto3_raw_data: "type_defs.CopySnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopySnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopySnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotResult:
    boto3_raw_data: "type_defs.CreateSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotResult:
    boto3_raw_data: "type_defs.DeleteSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsListMessage:
    boto3_raw_data: "type_defs.DescribeSnapshotsListMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Snapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["Snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsListMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsListMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateActionsMessage:
    boto3_raw_data: "type_defs.UpdateActionsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def UpdateActions(self):  # pragma: no cover
        return UpdateAction.make_many(self.boto3_raw_data["UpdateActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateActionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheSubnetGroupMessage:
    boto3_raw_data: "type_defs.CacheSubnetGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def CacheSubnetGroups(self):  # pragma: no cover
        return CacheSubnetGroup.make_many(self.boto3_raw_data["CacheSubnetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheSubnetGroupResult:
    boto3_raw_data: "type_defs.CreateCacheSubnetGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CacheSubnetGroup(self):  # pragma: no cover
        return CacheSubnetGroup.make_one(self.boto3_raw_data["CacheSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCacheSubnetGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCacheSubnetGroupResult:
    boto3_raw_data: "type_defs.ModifyCacheSubnetGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CacheSubnetGroup(self):  # pragma: no cover
        return CacheSubnetGroup.make_one(self.boto3_raw_data["CacheSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyCacheSubnetGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCacheSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheCluster:
    boto3_raw_data: "type_defs.CacheClusterTypeDef" = dataclasses.field()

    CacheClusterId = field("CacheClusterId")

    @cached_property
    def ConfigurationEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ConfigurationEndpoint"])

    ClientDownloadLandingPage = field("ClientDownloadLandingPage")
    CacheNodeType = field("CacheNodeType")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    CacheClusterStatus = field("CacheClusterStatus")
    NumCacheNodes = field("NumCacheNodes")
    PreferredAvailabilityZone = field("PreferredAvailabilityZone")
    PreferredOutpostArn = field("PreferredOutpostArn")
    CacheClusterCreateTime = field("CacheClusterCreateTime")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return PendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    @cached_property
    def CacheSecurityGroups(self):  # pragma: no cover
        return CacheSecurityGroupMembership.make_many(
            self.boto3_raw_data["CacheSecurityGroups"]
        )

    @cached_property
    def CacheParameterGroup(self):  # pragma: no cover
        return CacheParameterGroupStatus.make_one(
            self.boto3_raw_data["CacheParameterGroup"]
        )

    CacheSubnetGroupName = field("CacheSubnetGroupName")

    @cached_property
    def CacheNodes(self):  # pragma: no cover
        return CacheNode.make_many(self.boto3_raw_data["CacheNodes"])

    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")

    @cached_property
    def SecurityGroups(self):  # pragma: no cover
        return SecurityGroupMembership.make_many(self.boto3_raw_data["SecurityGroups"])

    ReplicationGroupId = field("ReplicationGroupId")
    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    AuthTokenEnabled = field("AuthTokenEnabled")
    AuthTokenLastModifiedDate = field("AuthTokenLastModifiedDate")
    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    AtRestEncryptionEnabled = field("AtRestEncryptionEnabled")
    ARN = field("ARN")
    ReplicationGroupLogDeliveryEnabled = field("ReplicationGroupLogDeliveryEnabled")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    NetworkType = field("NetworkType")
    IpDiscovery = field("IpDiscovery")
    TransitEncryptionMode = field("TransitEncryptionMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CacheClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CacheClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationGroup:
    boto3_raw_data: "type_defs.ReplicationGroupTypeDef" = dataclasses.field()

    ReplicationGroupId = field("ReplicationGroupId")
    Description = field("Description")

    @cached_property
    def GlobalReplicationGroupInfo(self):  # pragma: no cover
        return GlobalReplicationGroupInfo.make_one(
            self.boto3_raw_data["GlobalReplicationGroupInfo"]
        )

    Status = field("Status")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return ReplicationGroupPendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    MemberClusters = field("MemberClusters")

    @cached_property
    def NodeGroups(self):  # pragma: no cover
        return NodeGroup.make_many(self.boto3_raw_data["NodeGroups"])

    SnapshottingClusterId = field("SnapshottingClusterId")
    AutomaticFailover = field("AutomaticFailover")
    MultiAZ = field("MultiAZ")

    @cached_property
    def ConfigurationEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ConfigurationEndpoint"])

    SnapshotRetentionLimit = field("SnapshotRetentionLimit")
    SnapshotWindow = field("SnapshotWindow")
    ClusterEnabled = field("ClusterEnabled")
    CacheNodeType = field("CacheNodeType")
    AuthTokenEnabled = field("AuthTokenEnabled")
    AuthTokenLastModifiedDate = field("AuthTokenLastModifiedDate")
    TransitEncryptionEnabled = field("TransitEncryptionEnabled")
    AtRestEncryptionEnabled = field("AtRestEncryptionEnabled")
    MemberClustersOutpostArns = field("MemberClustersOutpostArns")
    KmsKeyId = field("KmsKeyId")
    ARN = field("ARN")
    UserGroupIds = field("UserGroupIds")

    @cached_property
    def LogDeliveryConfigurations(self):  # pragma: no cover
        return LogDeliveryConfiguration.make_many(
            self.boto3_raw_data["LogDeliveryConfigurations"]
        )

    ReplicationGroupCreateTime = field("ReplicationGroupCreateTime")
    DataTiering = field("DataTiering")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    NetworkType = field("NetworkType")
    IpDiscovery = field("IpDiscovery")
    TransitEncryptionMode = field("TransitEncryptionMode")
    ClusterMode = field("ClusterMode")
    Engine = field("Engine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CacheClusterMessage:
    boto3_raw_data: "type_defs.CacheClusterMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def CacheClusters(self):  # pragma: no cover
        return CacheCluster.make_many(self.boto3_raw_data["CacheClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CacheClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CacheClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCacheClusterResult:
    boto3_raw_data: "type_defs.CreateCacheClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def CacheCluster(self):  # pragma: no cover
        return CacheCluster.make_one(self.boto3_raw_data["CacheCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCacheClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCacheClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCacheClusterResult:
    boto3_raw_data: "type_defs.DeleteCacheClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def CacheCluster(self):  # pragma: no cover
        return CacheCluster.make_one(self.boto3_raw_data["CacheCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCacheClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCacheClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCacheClusterResult:
    boto3_raw_data: "type_defs.ModifyCacheClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def CacheCluster(self):  # pragma: no cover
        return CacheCluster.make_one(self.boto3_raw_data["CacheCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyCacheClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCacheClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootCacheClusterResult:
    boto3_raw_data: "type_defs.RebootCacheClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def CacheCluster(self):  # pragma: no cover
        return CacheCluster.make_one(self.boto3_raw_data["CacheCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootCacheClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootCacheClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMigrationResponse:
    boto3_raw_data: "type_defs.CompleteMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompleteMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationGroupResult:
    boto3_raw_data: "type_defs.CreateReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicationGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecreaseReplicaCountResult:
    boto3_raw_data: "type_defs.DecreaseReplicaCountResultTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DecreaseReplicaCountResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecreaseReplicaCountResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationGroupResult:
    boto3_raw_data: "type_defs.DeleteReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReplicationGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncreaseReplicaCountResult:
    boto3_raw_data: "type_defs.IncreaseReplicaCountResultTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IncreaseReplicaCountResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncreaseReplicaCountResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationGroupResult:
    boto3_raw_data: "type_defs.ModifyReplicationGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyReplicationGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationGroupShardConfigurationResult:
    boto3_raw_data: (
        "type_defs.ModifyReplicationGroupShardConfigurationResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyReplicationGroupShardConfigurationResultTypeDef"
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
                "type_defs.ModifyReplicationGroupShardConfigurationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationGroupMessage:
    boto3_raw_data: "type_defs.ReplicationGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ReplicationGroups(self):  # pragma: no cover
        return ReplicationGroup.make_many(self.boto3_raw_data["ReplicationGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMigrationResponse:
    boto3_raw_data: "type_defs.StartMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestFailoverResult:
    boto3_raw_data: "type_defs.TestFailoverResultTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestFailoverResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestFailoverResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestMigrationResponse:
    boto3_raw_data: "type_defs.TestMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicationGroup.make_one(self.boto3_raw_data["ReplicationGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
