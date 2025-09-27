# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rds import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountQuota:
    boto3_raw_data: "type_defs.AccountQuotaTypeDef" = dataclasses.field()

    AccountQuotaName = field("AccountQuotaName")
    Used = field("Used")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountQuotaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountQuotaTypeDef"]],
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
class AddRoleToDBClusterMessage:
    boto3_raw_data: "type_defs.AddRoleToDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddRoleToDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddRoleToDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddRoleToDBInstanceMessage:
    boto3_raw_data: "type_defs.AddRoleToDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddRoleToDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddRoleToDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddSourceIdentifierToSubscriptionMessage:
    boto3_raw_data: "type_defs.AddSourceIdentifierToSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SourceIdentifier = field("SourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddSourceIdentifierToSubscriptionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddSourceIdentifierToSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSubscription:
    boto3_raw_data: "type_defs.EventSubscriptionTypeDef" = dataclasses.field()

    CustomerAwsId = field("CustomerAwsId")
    CustSubscriptionId = field("CustSubscriptionId")
    SnsTopicArn = field("SnsTopicArn")
    Status = field("Status")
    SubscriptionCreationTime = field("SubscriptionCreationTime")
    SourceType = field("SourceType")
    SourceIdsList = field("SourceIdsList")
    EventCategoriesList = field("EventCategoriesList")
    Enabled = field("Enabled")
    EventSubscriptionArn = field("EventSubscriptionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionTypeDef"]
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
class ApplyPendingMaintenanceActionMessage:
    boto3_raw_data: "type_defs.ApplyPendingMaintenanceActionMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ApplyAction = field("ApplyAction")
    OptInType = field("OptInType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyPendingMaintenanceActionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyPendingMaintenanceActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeDBSecurityGroupIngressMessage:
    boto3_raw_data: "type_defs.AuthorizeDBSecurityGroupIngressMessageTypeDef" = (
        dataclasses.field()
    )

    DBSecurityGroupName = field("DBSecurityGroupName")
    CIDRIP = field("CIDRIP")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupId = field("EC2SecurityGroupId")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeDBSecurityGroupIngressMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeDBSecurityGroupIngressMessageTypeDef"]
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
class AvailableProcessorFeature:
    boto3_raw_data: "type_defs.AvailableProcessorFeatureTypeDef" = dataclasses.field()

    Name = field("Name")
    DefaultValue = field("DefaultValue")
    AllowedValues = field("AllowedValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailableProcessorFeatureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailableProcessorFeatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueGreenDeploymentTask:
    boto3_raw_data: "type_defs.BlueGreenDeploymentTaskTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlueGreenDeploymentTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlueGreenDeploymentTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverDetail:
    boto3_raw_data: "type_defs.SwitchoverDetailTypeDef" = dataclasses.field()

    SourceMember = field("SourceMember")
    TargetMember = field("TargetMember")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SwitchoverDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelExportTaskMessage:
    boto3_raw_data: "type_defs.CancelExportTaskMessageTypeDef" = dataclasses.field()

    ExportTaskIdentifier = field("ExportTaskIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelExportTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelExportTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateDetails:
    boto3_raw_data: "type_defs.CertificateDetailsTypeDef" = dataclasses.field()

    CAIdentifier = field("CAIdentifier")
    ValidTill = field("ValidTill")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    CertificateIdentifier = field("CertificateIdentifier")
    CertificateType = field("CertificateType")
    Thumbprint = field("Thumbprint")
    ValidFrom = field("ValidFrom")
    ValidTill = field("ValidTill")
    CertificateArn = field("CertificateArn")
    CustomerOverride = field("CustomerOverride")
    CustomerOverrideValidTill = field("CustomerOverrideValidTill")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CharacterSet:
    boto3_raw_data: "type_defs.CharacterSetTypeDef" = dataclasses.field()

    CharacterSetName = field("CharacterSetName")
    CharacterSetDescription = field("CharacterSetDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CharacterSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CharacterSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientGenerateDbAuthTokenRequest:
    boto3_raw_data: "type_defs.ClientGenerateDbAuthTokenRequestTypeDef" = (
        dataclasses.field()
    )

    DBHostname = field("DBHostname")
    Port = field("Port")
    DBUsername = field("DBUsername")
    Region = field("Region")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClientGenerateDbAuthTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientGenerateDbAuthTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchLogsExportConfiguration:
    boto3_raw_data: "type_defs.CloudwatchLogsExportConfigurationTypeDef" = (
        dataclasses.field()
    )

    EnableLogTypes = field("EnableLogTypes")
    DisableLogTypes = field("DisableLogTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudwatchLogsExportConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchLogsExportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingCloudwatchLogsExports:
    boto3_raw_data: "type_defs.PendingCloudwatchLogsExportsTypeDef" = (
        dataclasses.field()
    )

    LogTypesToEnable = field("LogTypesToEnable")
    LogTypesToDisable = field("LogTypesToDisable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingCloudwatchLogsExportsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingCloudwatchLogsExportsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsCustomClusterConfiguration:
    boto3_raw_data: "type_defs.RdsCustomClusterConfigurationTypeDef" = (
        dataclasses.field()
    )

    InterconnectSubnetId = field("InterconnectSubnetId")
    TransitGatewayMulticastDomainId = field("TransitGatewayMulticastDomainId")
    ReplicaMode = field("ReplicaMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RdsCustomClusterConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsCustomClusterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionPoolConfigurationInfo:
    boto3_raw_data: "type_defs.ConnectionPoolConfigurationInfoTypeDef" = (
        dataclasses.field()
    )

    MaxConnectionsPercent = field("MaxConnectionsPercent")
    MaxIdleConnectionsPercent = field("MaxIdleConnectionsPercent")
    ConnectionBorrowTimeout = field("ConnectionBorrowTimeout")
    SessionPinningFilters = field("SessionPinningFilters")
    InitQuery = field("InitQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectionPoolConfigurationInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPoolConfigurationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionPoolConfiguration:
    boto3_raw_data: "type_defs.ConnectionPoolConfigurationTypeDef" = dataclasses.field()

    MaxConnectionsPercent = field("MaxConnectionsPercent")
    MaxIdleConnectionsPercent = field("MaxIdleConnectionsPercent")
    ConnectionBorrowTimeout = field("ConnectionBorrowTimeout")
    SessionPinningFilters = field("SessionPinningFilters")
    InitQuery = field("InitQuery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionPoolConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPoolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextAttribute:
    boto3_raw_data: "type_defs.ContextAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContextAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContextAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroup:
    boto3_raw_data: "type_defs.DBClusterParameterGroupTypeDef" = dataclasses.field()

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")
    DBClusterParameterGroupArn = field("DBClusterParameterGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterParameterGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroup:
    boto3_raw_data: "type_defs.DBParameterGroupTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")
    DBParameterGroupArn = field("DBParameterGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConfiguration:
    boto3_raw_data: "type_defs.ScalingConfigurationTypeDef" = dataclasses.field()

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    AutoPause = field("AutoPause")
    SecondsUntilAutoPause = field("SecondsUntilAutoPause")
    TimeoutAction = field("TimeoutAction")
    SecondsBeforeTimeout = field("SecondsBeforeTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessV2ScalingConfiguration:
    boto3_raw_data: "type_defs.ServerlessV2ScalingConfigurationTypeDef" = (
        dataclasses.field()
    )

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    SecondsUntilAutoPause = field("SecondsUntilAutoPause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerlessV2ScalingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessV2ScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessorFeature:
    boto3_raw_data: "type_defs.ProcessorFeatureTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessorFeatureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProcessorFeatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBProxyEndpoint:
    boto3_raw_data: "type_defs.DBProxyEndpointTypeDef" = dataclasses.field()

    DBProxyEndpointName = field("DBProxyEndpointName")
    DBProxyEndpointArn = field("DBProxyEndpointArn")
    DBProxyName = field("DBProxyName")
    Status = field("Status")
    VpcId = field("VpcId")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    VpcSubnetIds = field("VpcSubnetIds")
    Endpoint = field("Endpoint")
    CreatedDate = field("CreatedDate")
    TargetRole = field("TargetRole")
    IsDefault = field("IsDefault")
    EndpointNetworkType = field("EndpointNetworkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBProxyEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBProxyEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAuthConfig:
    boto3_raw_data: "type_defs.UserAuthConfigTypeDef" = dataclasses.field()

    Description = field("Description")
    UserName = field("UserName")
    AuthScheme = field("AuthScheme")
    SecretArn = field("SecretArn")
    IAMAuth = field("IAMAuth")
    ClientPasswordAuthType = field("ClientPasswordAuthType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserAuthConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserAuthConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDBEngineVersionAMI:
    boto3_raw_data: "type_defs.CustomDBEngineVersionAMITypeDef" = dataclasses.field()

    ImageId = field("ImageId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDBEngineVersionAMITypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDBEngineVersionAMITypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreWindow:
    boto3_raw_data: "type_defs.RestoreWindowTypeDef" = dataclasses.field()

    EarliestTime = field("EarliestTime")
    LatestTime = field("LatestTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestoreWindowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterBacktrack:
    boto3_raw_data: "type_defs.DBClusterBacktrackTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    BacktrackIdentifier = field("BacktrackIdentifier")
    BacktrackTo = field("BacktrackTo")
    BacktrackedFrom = field("BacktrackedFrom")
    BacktrackRequestCreationTime = field("BacktrackRequestCreationTime")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterBacktrackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterBacktrackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterEndpoint:
    boto3_raw_data: "type_defs.DBClusterEndpointTypeDef" = dataclasses.field()

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointResourceIdentifier = field("DBClusterEndpointResourceIdentifier")
    Endpoint = field("Endpoint")
    Status = field("Status")
    EndpointType = field("EndpointType")
    CustomEndpointType = field("CustomEndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")
    DBClusterEndpointArn = field("DBClusterEndpointArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterMember:
    boto3_raw_data: "type_defs.DBClusterMemberTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    IsClusterWriter = field("IsClusterWriter")
    DBClusterParameterGroupStatus = field("DBClusterParameterGroupStatus")
    PromotionTier = field("PromotionTier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBClusterMemberTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterOptionGroupStatus:
    boto3_raw_data: "type_defs.DBClusterOptionGroupStatusTypeDef" = dataclasses.field()

    DBClusterOptionGroupName = field("DBClusterOptionGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterOptionGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterOptionGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterOutput:
    boto3_raw_data: "type_defs.ParameterOutputTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")
    Description = field("Description")
    Source = field("Source")
    ApplyType = field("ApplyType")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    MinimumEngineVersion = field("MinimumEngineVersion")
    ApplyMethod = field("ApplyMethod")
    SupportedEngineModes = field("SupportedEngineModes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterRole:
    boto3_raw_data: "type_defs.DBClusterRoleTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    Status = field("Status")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBClusterRoleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshotAttribute:
    boto3_raw_data: "type_defs.DBClusterSnapshotAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValues = field("AttributeValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterSnapshotAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterStatusInfo:
    boto3_raw_data: "type_defs.DBClusterStatusInfoTypeDef" = dataclasses.field()

    StatusType = field("StatusType")
    Normal = field("Normal")
    Status = field("Status")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterStatusInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterStatusInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainMembership:
    boto3_raw_data: "type_defs.DomainMembershipTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Status = field("Status")
    FQDN = field("FQDN")
    IAMRoleName = field("IAMRoleName")
    OU = field("OU")
    AuthSecretArn = field("AuthSecretArn")
    DnsIps = field("DnsIps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainMembershipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LimitlessDatabase:
    boto3_raw_data: "type_defs.LimitlessDatabaseTypeDef" = dataclasses.field()

    Status = field("Status")
    MinRequiredACU = field("MinRequiredACU")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitlessDatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LimitlessDatabaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MasterUserSecret:
    boto3_raw_data: "type_defs.MasterUserSecretTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    SecretStatus = field("SecretStatus")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MasterUserSecretTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MasterUserSecretTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConfigurationInfo:
    boto3_raw_data: "type_defs.ScalingConfigurationInfoTypeDef" = dataclasses.field()

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    AutoPause = field("AutoPause")
    SecondsUntilAutoPause = field("SecondsUntilAutoPause")
    TimeoutAction = field("TimeoutAction")
    SecondsBeforeTimeout = field("SecondsBeforeTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigurationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingConfigurationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessV2ScalingConfigurationInfo:
    boto3_raw_data: "type_defs.ServerlessV2ScalingConfigurationInfoTypeDef" = (
        dataclasses.field()
    )

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")
    SecondsUntilAutoPause = field("SecondsUntilAutoPause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerlessV2ScalingConfigurationInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessV2ScalingConfigurationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcSecurityGroupMembership:
    boto3_raw_data: "type_defs.VpcSecurityGroupMembershipTypeDef" = dataclasses.field()

    VpcSecurityGroupId = field("VpcSecurityGroupId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcSecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcSecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessV2FeaturesSupport:
    boto3_raw_data: "type_defs.ServerlessV2FeaturesSupportTypeDef" = dataclasses.field()

    MinCapacity = field("MinCapacity")
    MaxCapacity = field("MaxCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerlessV2FeaturesSupportTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessV2FeaturesSupportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Timezone:
    boto3_raw_data: "type_defs.TimezoneTypeDef" = dataclasses.field()

    TimezoneName = field("TimezoneName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimezoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimezoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeTarget:
    boto3_raw_data: "type_defs.UpgradeTargetTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    Description = field("Description")
    AutoUpgrade = field("AutoUpgrade")
    IsMajorVersionUpgrade = field("IsMajorVersionUpgrade")
    SupportedEngineModes = field("SupportedEngineModes")
    SupportsParallelQuery = field("SupportsParallelQuery")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")
    SupportsBabelfish = field("SupportsBabelfish")
    SupportsLimitlessDatabase = field("SupportsLimitlessDatabase")
    SupportsLocalWriteForwarding = field("SupportsLocalWriteForwarding")
    SupportsIntegrations = field("SupportsIntegrations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpgradeTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpgradeTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceAutomatedBackupsReplication:
    boto3_raw_data: "type_defs.DBInstanceAutomatedBackupsReplicationTypeDef" = (
        dataclasses.field()
    )

    DBInstanceAutomatedBackupsArn = field("DBInstanceAutomatedBackupsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DBInstanceAutomatedBackupsReplicationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceAutomatedBackupsReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceRole:
    boto3_raw_data: "type_defs.DBInstanceRoleTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBInstanceRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBInstanceRoleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceStatusInfo:
    boto3_raw_data: "type_defs.DBInstanceStatusInfoTypeDef" = dataclasses.field()

    StatusType = field("StatusType")
    Normal = field("Normal")
    Status = field("Status")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBInstanceStatusInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceStatusInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupStatus:
    boto3_raw_data: "type_defs.DBParameterGroupStatusTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")
    ParameterApplyStatus = field("ParameterApplyStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSecurityGroupMembership:
    boto3_raw_data: "type_defs.DBSecurityGroupMembershipTypeDef" = dataclasses.field()

    DBSecurityGroupName = field("DBSecurityGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSecurityGroupMembershipTypeDef"]
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
    HostedZoneId = field("HostedZoneId")

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
class OptionGroupMembership:
    boto3_raw_data: "type_defs.OptionGroupMembershipTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedEngineLifecycle:
    boto3_raw_data: "type_defs.SupportedEngineLifecycleTypeDef" = dataclasses.field()

    LifecycleSupportName = field("LifecycleSupportName")
    LifecycleSupportStartDate = field("LifecycleSupportStartDate")
    LifecycleSupportEndDate = field("LifecycleSupportEndDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedEngineLifecycleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedEngineLifecycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetHealth:
    boto3_raw_data: "type_defs.TargetHealthTypeDef" = dataclasses.field()

    State = field("State")
    Reason = field("Reason")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAuthConfigInfo:
    boto3_raw_data: "type_defs.UserAuthConfigInfoTypeDef" = dataclasses.field()

    Description = field("Description")
    UserName = field("UserName")
    AuthScheme = field("AuthScheme")
    SecretArn = field("SecretArn")
    IAMAuth = field("IAMAuth")
    ClientPasswordAuthType = field("ClientPasswordAuthType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserAuthConfigInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserAuthConfigInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocLink:
    boto3_raw_data: "type_defs.DocLinkTypeDef" = dataclasses.field()

    Text = field("Text")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocLinkTypeDef"]]
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
    EC2SecurityGroupId = field("EC2SecurityGroupId")
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
class IPRange:
    boto3_raw_data: "type_defs.IPRangeTypeDef" = dataclasses.field()

    Status = field("Status")
    CIDRIP = field("CIDRIP")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSnapshotAttribute:
    boto3_raw_data: "type_defs.DBSnapshotAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValues = field("AttributeValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSnapshotAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSnapshotAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBlueGreenDeploymentRequest:
    boto3_raw_data: "type_defs.DeleteBlueGreenDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    BlueGreenDeploymentIdentifier = field("BlueGreenDeploymentIdentifier")
    DeleteTarget = field("DeleteTarget")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBlueGreenDeploymentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBlueGreenDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomDBEngineVersionMessage:
    boto3_raw_data: "type_defs.DeleteCustomDBEngineVersionMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomDBEngineVersionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomDBEngineVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterAutomatedBackupMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterAutomatedBackupMessageTypeDef" = (
        dataclasses.field()
    )

    DbClusterResourceId = field("DbClusterResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDBClusterAutomatedBackupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterAutomatedBackupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterEndpointMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterEndpointMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterEndpointMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    SkipFinalSnapshot = field("SkipFinalSnapshot")
    FinalDBSnapshotIdentifier = field("FinalDBSnapshotIdentifier")
    DeleteAutomatedBackups = field("DeleteAutomatedBackups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.DeleteDBClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterSnapshotMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBInstanceAutomatedBackupMessage:
    boto3_raw_data: "type_defs.DeleteDBInstanceAutomatedBackupMessageTypeDef" = (
        dataclasses.field()
    )

    DbiResourceId = field("DbiResourceId")
    DBInstanceAutomatedBackupsArn = field("DBInstanceAutomatedBackupsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDBInstanceAutomatedBackupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBInstanceAutomatedBackupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBInstanceMessage:
    boto3_raw_data: "type_defs.DeleteDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    SkipFinalSnapshot = field("SkipFinalSnapshot")
    FinalDBSnapshotIdentifier = field("FinalDBSnapshotIdentifier")
    DeleteAutomatedBackups = field("DeleteAutomatedBackups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBParameterGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBProxyEndpointRequest:
    boto3_raw_data: "type_defs.DeleteDBProxyEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyEndpointName = field("DBProxyEndpointName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBProxyEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBProxyEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBProxyRequest:
    boto3_raw_data: "type_defs.DeleteDBProxyRequestTypeDef" = dataclasses.field()

    DBProxyName = field("DBProxyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBProxyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBProxyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBSecurityGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBSecurityGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBSecurityGroupName = field("DBSecurityGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBSecurityGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBShardGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBShardGroupMessageTypeDef" = dataclasses.field()

    DBShardGroupIdentifier = field("DBShardGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBShardGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBShardGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBSnapshotMessage:
    boto3_raw_data: "type_defs.DeleteDBSnapshotMessageTypeDef" = dataclasses.field()

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBSubnetGroupMessage:
    boto3_raw_data: "type_defs.DeleteDBSubnetGroupMessageTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSubscriptionMessage:
    boto3_raw_data: "type_defs.DeleteEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalClusterMessage:
    boto3_raw_data: "type_defs.DeleteGlobalClusterMessageTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationMessage:
    boto3_raw_data: "type_defs.DeleteIntegrationMessageTypeDef" = dataclasses.field()

    IntegrationIdentifier = field("IntegrationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntegrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOptionGroupMessage:
    boto3_raw_data: "type_defs.DeleteOptionGroupMessageTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOptionGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOptionGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTenantDatabaseMessage:
    boto3_raw_data: "type_defs.DeleteTenantDatabaseMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")
    SkipFinalSnapshot = field("SkipFinalSnapshot")
    FinalDBSnapshotIdentifier = field("FinalDBSnapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTenantDatabaseMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTenantDatabaseMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterDBProxyTargetsRequest:
    boto3_raw_data: "type_defs.DeregisterDBProxyTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")
    DBInstanceIdentifiers = field("DBInstanceIdentifiers")
    DBClusterIdentifiers = field("DBClusterIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterDBProxyTargetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterDBProxyTargetsRequestTypeDef"]
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
class DescribeDBClusterSnapshotAttributesMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotAttributesMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotAttributesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotAttributesMessageTypeDef"]
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
class DescribeDBLogFilesDetails:
    boto3_raw_data: "type_defs.DescribeDBLogFilesDetailsTypeDef" = dataclasses.field()

    LogFileName = field("LogFileName")
    LastWritten = field("LastWritten")
    Size = field("Size")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBLogFilesDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBLogFilesDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBMajorEngineVersionsRequest:
    boto3_raw_data: "type_defs.DescribeDBMajorEngineVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    MajorEngineVersion = field("MajorEngineVersion")
    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBMajorEngineVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBMajorEngineVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotAttributesMessage:
    boto3_raw_data: "type_defs.DescribeDBSnapshotAttributesMessageTypeDef" = (
        dataclasses.field()
    )

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotAttributesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotAttributesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeValidDBInstanceModificationsMessage:
    boto3_raw_data: "type_defs.DescribeValidDBInstanceModificationsMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeValidDBInstanceModificationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeValidDBInstanceModificationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableHttpEndpointRequest:
    boto3_raw_data: "type_defs.DisableHttpEndpointRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableHttpEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableHttpEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DoubleRange:
    boto3_raw_data: "type_defs.DoubleRangeTypeDef" = dataclasses.field()

    From = field("From")
    To = field("To")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DoubleRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DoubleRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DownloadDBLogFilePortionMessage:
    boto3_raw_data: "type_defs.DownloadDBLogFilePortionMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    LogFileName = field("LogFileName")
    Marker = field("Marker")
    NumberOfLines = field("NumberOfLines")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DownloadDBLogFilePortionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DownloadDBLogFilePortionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableHttpEndpointRequest:
    boto3_raw_data: "type_defs.EnableHttpEndpointRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableHttpEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableHttpEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventCategoriesMap:
    boto3_raw_data: "type_defs.EventCategoriesMapTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    EventCategories = field("EventCategories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventCategoriesMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventCategoriesMapTypeDef"]
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
    EventCategories = field("EventCategories")
    Date = field("Date")
    SourceArn = field("SourceArn")

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
class ExportTask:
    boto3_raw_data: "type_defs.ExportTaskTypeDef" = dataclasses.field()

    ExportTaskIdentifier = field("ExportTaskIdentifier")
    SourceArn = field("SourceArn")
    ExportOnly = field("ExportOnly")
    SnapshotTime = field("SnapshotTime")
    TaskStartTime = field("TaskStartTime")
    TaskEndTime = field("TaskEndTime")
    S3Bucket = field("S3Bucket")
    S3Prefix = field("S3Prefix")
    IamRoleArn = field("IamRoleArn")
    KmsKeyId = field("KmsKeyId")
    Status = field("Status")
    PercentProgress = field("PercentProgress")
    TotalExtractedDataInGB = field("TotalExtractedDataInGB")
    FailureCause = field("FailureCause")
    WarningMessage = field("WarningMessage")
    SourceType = field("SourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportTaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverDBClusterMessage:
    boto3_raw_data: "type_defs.FailoverDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    TargetDBInstanceIdentifier = field("TargetDBInstanceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverGlobalClusterMessage:
    boto3_raw_data: "type_defs.FailoverGlobalClusterMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    TargetDbClusterIdentifier = field("TargetDbClusterIdentifier")
    AllowDataLoss = field("AllowDataLoss")
    Switchover = field("Switchover")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverState:
    boto3_raw_data: "type_defs.FailoverStateTypeDef" = dataclasses.field()

    Status = field("Status")
    FromDbClusterArn = field("FromDbClusterArn")
    ToDbClusterArn = field("ToDbClusterArn")
    IsDataLossAllowed = field("IsDataLossAllowed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailoverStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailoverStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalClusterMember:
    boto3_raw_data: "type_defs.GlobalClusterMemberTypeDef" = dataclasses.field()

    DBClusterArn = field("DBClusterArn")
    Readers = field("Readers")
    IsWriter = field("IsWriter")
    GlobalWriteForwardingStatus = field("GlobalWriteForwardingStatus")
    SynchronizationStatus = field("SynchronizationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalClusterMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalClusterMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationError:
    boto3_raw_data: "type_defs.IntegrationErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegrationErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MinimumEngineVersionPerAllowedValue:
    boto3_raw_data: "type_defs.MinimumEngineVersionPerAllowedValueTypeDef" = (
        dataclasses.field()
    )

    AllowedValue = field("AllowedValue")
    MinimumEngineVersion = field("MinimumEngineVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MinimumEngineVersionPerAllowedValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MinimumEngineVersionPerAllowedValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyActivityStreamRequest:
    boto3_raw_data: "type_defs.ModifyActivityStreamRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    AuditPolicyState = field("AuditPolicyState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyActivityStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyActivityStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCertificatesMessage:
    boto3_raw_data: "type_defs.ModifyCertificatesMessageTypeDef" = dataclasses.field()

    CertificateIdentifier = field("CertificateIdentifier")
    RemoveCustomerOverride = field("RemoveCustomerOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyCertificatesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCertificatesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCurrentDBClusterCapacityMessage:
    boto3_raw_data: "type_defs.ModifyCurrentDBClusterCapacityMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    Capacity = field("Capacity")
    SecondsBeforeTimeout = field("SecondsBeforeTimeout")
    TimeoutAction = field("TimeoutAction")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyCurrentDBClusterCapacityMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCurrentDBClusterCapacityMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCustomDBEngineVersionMessage:
    boto3_raw_data: "type_defs.ModifyCustomDBEngineVersionMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    Description = field("Description")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyCustomDBEngineVersionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCustomDBEngineVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterEndpointMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterEndpointMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    EndpointType = field("EndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBClusterEndpointMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterSnapshotAttributeMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterSnapshotAttributeMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    AttributeName = field("AttributeName")
    ValuesToAdd = field("ValuesToAdd")
    ValuesToRemove = field("ValuesToRemove")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyDBClusterSnapshotAttributeMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterSnapshotAttributeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBProxyEndpointRequest:
    boto3_raw_data: "type_defs.ModifyDBProxyEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyEndpointName = field("DBProxyEndpointName")
    NewDBProxyEndpointName = field("NewDBProxyEndpointName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBProxyEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBProxyEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedActionUpdate:
    boto3_raw_data: "type_defs.RecommendedActionUpdateTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendedActionUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendedActionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBShardGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBShardGroupMessageTypeDef" = dataclasses.field()

    DBShardGroupIdentifier = field("DBShardGroupIdentifier")
    MaxACU = field("MaxACU")
    MinACU = field("MinACU")
    ComputeRedundancy = field("ComputeRedundancy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBShardGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBShardGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSnapshotAttributeMessage:
    boto3_raw_data: "type_defs.ModifyDBSnapshotAttributeMessageTypeDef" = (
        dataclasses.field()
    )

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    AttributeName = field("AttributeName")
    ValuesToAdd = field("ValuesToAdd")
    ValuesToRemove = field("ValuesToRemove")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBSnapshotAttributeMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSnapshotAttributeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSnapshotMessage:
    boto3_raw_data: "type_defs.ModifyDBSnapshotMessageTypeDef" = dataclasses.field()

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    EngineVersion = field("EngineVersion")
    OptionGroupName = field("OptionGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSubnetGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBSubnetGroupMessageTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")
    SubnetIds = field("SubnetIds")
    DBSubnetGroupDescription = field("DBSubnetGroupDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEventSubscriptionMessage:
    boto3_raw_data: "type_defs.ModifyEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SnsTopicArn = field("SnsTopicArn")
    SourceType = field("SourceType")
    EventCategories = field("EventCategories")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyGlobalClusterMessage:
    boto3_raw_data: "type_defs.ModifyGlobalClusterMessageTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    NewGlobalClusterIdentifier = field("NewGlobalClusterIdentifier")
    DeletionProtection = field("DeletionProtection")
    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyIntegrationMessage:
    boto3_raw_data: "type_defs.ModifyIntegrationMessageTypeDef" = dataclasses.field()

    IntegrationIdentifier = field("IntegrationIdentifier")
    IntegrationName = field("IntegrationName")
    DataFilter = field("DataFilter")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyIntegrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyIntegrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTenantDatabaseMessage:
    boto3_raw_data: "type_defs.ModifyTenantDatabaseMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")
    MasterUserPassword = field("MasterUserPassword")
    NewTenantDBName = field("NewTenantDBName")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    RotateMasterUserPassword = field("RotateMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyTenantDatabaseMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTenantDatabaseMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionSetting:
    boto3_raw_data: "type_defs.OptionSettingTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    DefaultValue = field("DefaultValue")
    Description = field("Description")
    ApplyType = field("ApplyType")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    IsCollection = field("IsCollection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionVersion:
    boto3_raw_data: "type_defs.OptionVersionTypeDef" = dataclasses.field()

    Version = field("Version")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Outpost:
    boto3_raw_data: "type_defs.OutpostTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutpostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutpostTypeDef"]]
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
    ApplyType = field("ApplyType")
    DataType = field("DataType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    MinimumEngineVersion = field("MinimumEngineVersion")
    ApplyMethod = field("ApplyMethod")
    SupportedEngineModes = field("SupportedEngineModes")

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
class PendingMaintenanceAction:
    boto3_raw_data: "type_defs.PendingMaintenanceActionTypeDef" = dataclasses.field()

    Action = field("Action")
    AutoAppliedAfterDate = field("AutoAppliedAfterDate")
    ForcedApplyDate = field("ForcedApplyDate")
    OptInStatus = field("OptInStatus")
    CurrentApplyDate = field("CurrentApplyDate")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingMaintenanceActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsMetricDimensionGroup:
    boto3_raw_data: "type_defs.PerformanceInsightsMetricDimensionGroupTypeDef" = (
        dataclasses.field()
    )

    Dimensions = field("Dimensions")
    Group = field("Group")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PerformanceInsightsMetricDimensionGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsMetricDimensionGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteReadReplicaDBClusterMessage:
    boto3_raw_data: "type_defs.PromoteReadReplicaDBClusterMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromoteReadReplicaDBClusterMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromoteReadReplicaDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteReadReplicaMessage:
    boto3_raw_data: "type_defs.PromoteReadReplicaMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    PreferredBackupWindow = field("PreferredBackupWindow")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromoteReadReplicaMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromoteReadReplicaMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    From = field("From")
    To = field("To")
    Step = field("Step")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBClusterMessage:
    boto3_raw_data: "type_defs.RebootDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBInstanceMessage:
    boto3_raw_data: "type_defs.RebootDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    ForceFailover = field("ForceFailover")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBShardGroupMessage:
    boto3_raw_data: "type_defs.RebootDBShardGroupMessageTypeDef" = dataclasses.field()

    DBShardGroupIdentifier = field("DBShardGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBShardGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBShardGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedActionParameter:
    boto3_raw_data: "type_defs.RecommendedActionParameterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendedActionParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendedActionParameterTypeDef"]
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
class ScalarReferenceDetails:
    boto3_raw_data: "type_defs.ScalarReferenceDetailsTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarReferenceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarReferenceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDBProxyTargetsRequest:
    boto3_raw_data: "type_defs.RegisterDBProxyTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")
    DBInstanceIdentifiers = field("DBInstanceIdentifiers")
    DBClusterIdentifiers = field("DBClusterIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterDBProxyTargetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDBProxyTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFromGlobalClusterMessage:
    boto3_raw_data: "type_defs.RemoveFromGlobalClusterMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    DbClusterIdentifier = field("DbClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFromGlobalClusterMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFromGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveRoleFromDBClusterMessage:
    boto3_raw_data: "type_defs.RemoveRoleFromDBClusterMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveRoleFromDBClusterMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveRoleFromDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveRoleFromDBInstanceMessage:
    boto3_raw_data: "type_defs.RemoveRoleFromDBInstanceMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    RoleArn = field("RoleArn")
    FeatureName = field("FeatureName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveRoleFromDBInstanceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveRoleFromDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveSourceIdentifierFromSubscriptionMessage:
    boto3_raw_data: "type_defs.RemoveSourceIdentifierFromSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SourceIdentifier = field("SourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveSourceIdentifierFromSubscriptionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveSourceIdentifierFromSubscriptionMessageTypeDef"]
        ],
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
class RevokeDBSecurityGroupIngressMessage:
    boto3_raw_data: "type_defs.RevokeDBSecurityGroupIngressMessageTypeDef" = (
        dataclasses.field()
    )

    DBSecurityGroupName = field("DBSecurityGroupName")
    CIDRIP = field("CIDRIP")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupId = field("EC2SecurityGroupId")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeDBSecurityGroupIngressMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeDBSecurityGroupIngressMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceRegion:
    boto3_raw_data: "type_defs.SourceRegionTypeDef" = dataclasses.field()

    RegionName = field("RegionName")
    Endpoint = field("Endpoint")
    Status = field("Status")
    SupportsDBInstanceAutomatedBackupsReplication = field(
        "SupportsDBInstanceAutomatedBackupsReplication"
    )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceRegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceRegionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartActivityStreamRequest:
    boto3_raw_data: "type_defs.StartActivityStreamRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Mode = field("Mode")
    KmsKeyId = field("KmsKeyId")
    ApplyImmediately = field("ApplyImmediately")
    EngineNativeAuditFieldsIncluded = field("EngineNativeAuditFieldsIncluded")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartActivityStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartActivityStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBClusterMessage:
    boto3_raw_data: "type_defs.StartDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBInstanceAutomatedBackupsReplicationMessage:
    boto3_raw_data: (
        "type_defs.StartDBInstanceAutomatedBackupsReplicationMessageTypeDef"
    ) = dataclasses.field()

    SourceDBInstanceArn = field("SourceDBInstanceArn")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    KmsKeyId = field("KmsKeyId")
    PreSignedUrl = field("PreSignedUrl")
    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDBInstanceAutomatedBackupsReplicationMessageTypeDef"
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
                "type_defs.StartDBInstanceAutomatedBackupsReplicationMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBInstanceMessage:
    boto3_raw_data: "type_defs.StartDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExportTaskMessage:
    boto3_raw_data: "type_defs.StartExportTaskMessageTypeDef" = dataclasses.field()

    ExportTaskIdentifier = field("ExportTaskIdentifier")
    SourceArn = field("SourceArn")
    S3BucketName = field("S3BucketName")
    IamRoleArn = field("IamRoleArn")
    KmsKeyId = field("KmsKeyId")
    S3Prefix = field("S3Prefix")
    ExportOnly = field("ExportOnly")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExportTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExportTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopActivityStreamRequest:
    boto3_raw_data: "type_defs.StopActivityStreamRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ApplyImmediately = field("ApplyImmediately")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopActivityStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopActivityStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBClusterMessage:
    boto3_raw_data: "type_defs.StopDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBInstanceAutomatedBackupsReplicationMessage:
    boto3_raw_data: (
        "type_defs.StopDBInstanceAutomatedBackupsReplicationMessageTypeDef"
    ) = dataclasses.field()

    SourceDBInstanceArn = field("SourceDBInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopDBInstanceAutomatedBackupsReplicationMessageTypeDef"
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
                "type_defs.StopDBInstanceAutomatedBackupsReplicationMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBInstanceMessage:
    boto3_raw_data: "type_defs.StopDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverBlueGreenDeploymentRequest:
    boto3_raw_data: "type_defs.SwitchoverBlueGreenDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    BlueGreenDeploymentIdentifier = field("BlueGreenDeploymentIdentifier")
    SwitchoverTimeout = field("SwitchoverTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SwitchoverBlueGreenDeploymentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverBlueGreenDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverGlobalClusterMessage:
    boto3_raw_data: "type_defs.SwitchoverGlobalClusterMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    TargetDbClusterIdentifier = field("TargetDbClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SwitchoverGlobalClusterMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverReadReplicaMessage:
    boto3_raw_data: "type_defs.SwitchoverReadReplicaMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SwitchoverReadReplicaMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverReadReplicaMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantDatabasePendingModifiedValues:
    boto3_raw_data: "type_defs.TenantDatabasePendingModifiedValuesTypeDef" = (
        dataclasses.field()
    )

    MasterUserPassword = field("MasterUserPassword")
    TenantDBName = field("TenantDBName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TenantDatabasePendingModifiedValuesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TenantDatabasePendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAttributesMessage:
    boto3_raw_data: "type_defs.AccountAttributesMessageTypeDef" = dataclasses.field()

    @cached_property
    def AccountQuotas(self):  # pragma: no cover
        return AccountQuota.make_many(self.boto3_raw_data["AccountQuotas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountAttributesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAttributesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterBacktrackResponse:
    boto3_raw_data: "type_defs.DBClusterBacktrackResponseTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    BacktrackIdentifier = field("BacktrackIdentifier")
    BacktrackTo = field("BacktrackTo")
    BacktrackedFrom = field("BacktrackedFrom")
    BacktrackRequestCreationTime = field("BacktrackRequestCreationTime")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterBacktrackResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterBacktrackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterCapacityInfo:
    boto3_raw_data: "type_defs.DBClusterCapacityInfoTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    PendingCapacity = field("PendingCapacity")
    CurrentCapacity = field("CurrentCapacity")
    SecondsBeforeTimeout = field("SecondsBeforeTimeout")
    TimeoutAction = field("TimeoutAction")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterCapacityInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterCapacityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterEndpointResponse:
    boto3_raw_data: "type_defs.DBClusterEndpointResponseTypeDef" = dataclasses.field()

    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointResourceIdentifier = field("DBClusterEndpointResourceIdentifier")
    Endpoint = field("Endpoint")
    Status = field("Status")
    EndpointType = field("EndpointType")
    CustomEndpointType = field("CustomEndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")
    DBClusterEndpointArn = field("DBClusterEndpointArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroupNameMessage:
    boto3_raw_data: "type_defs.DBClusterParameterGroupNameMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DBClusterParameterGroupNameMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupNameMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupNameMessage:
    boto3_raw_data: "type_defs.DBParameterGroupNameMessageTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupNameMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupNameMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableHttpEndpointResponse:
    boto3_raw_data: "type_defs.DisableHttpEndpointResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    HttpEndpointEnabled = field("HttpEndpointEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableHttpEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableHttpEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DownloadDBLogFilePortionDetails:
    boto3_raw_data: "type_defs.DownloadDBLogFilePortionDetailsTypeDef" = (
        dataclasses.field()
    )

    LogFileData = field("LogFileData")
    Marker = field("Marker")
    AdditionalDataPending = field("AdditionalDataPending")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DownloadDBLogFilePortionDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DownloadDBLogFilePortionDetailsTypeDef"]
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
class EnableHttpEndpointResponse:
    boto3_raw_data: "type_defs.EnableHttpEndpointResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    HttpEndpointEnabled = field("HttpEndpointEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableHttpEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableHttpEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskResponse:
    boto3_raw_data: "type_defs.ExportTaskResponseTypeDef" = dataclasses.field()

    ExportTaskIdentifier = field("ExportTaskIdentifier")
    SourceArn = field("SourceArn")
    ExportOnly = field("ExportOnly")
    SnapshotTime = field("SnapshotTime")
    TaskStartTime = field("TaskStartTime")
    TaskEndTime = field("TaskEndTime")
    S3Bucket = field("S3Bucket")
    S3Prefix = field("S3Prefix")
    IamRoleArn = field("IamRoleArn")
    KmsKeyId = field("KmsKeyId")
    Status = field("Status")
    PercentProgress = field("PercentProgress")
    TotalExtractedDataInGB = field("TotalExtractedDataInGB")
    FailureCause = field("FailureCause")
    WarningMessage = field("WarningMessage")
    SourceType = field("SourceType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyActivityStreamResponse:
    boto3_raw_data: "type_defs.ModifyActivityStreamResponseTypeDef" = (
        dataclasses.field()
    )

    KmsKeyId = field("KmsKeyId")
    KinesisStreamName = field("KinesisStreamName")
    Status = field("Status")
    Mode = field("Mode")
    EngineNativeAuditFieldsIncluded = field("EngineNativeAuditFieldsIncluded")
    PolicyStatus = field("PolicyStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyActivityStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyActivityStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartActivityStreamResponse:
    boto3_raw_data: "type_defs.StartActivityStreamResponseTypeDef" = dataclasses.field()

    KmsKeyId = field("KmsKeyId")
    KinesisStreamName = field("KinesisStreamName")
    Status = field("Status")
    Mode = field("Mode")
    ApplyImmediately = field("ApplyImmediately")
    EngineNativeAuditFieldsIncluded = field("EngineNativeAuditFieldsIncluded")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartActivityStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartActivityStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopActivityStreamResponse:
    boto3_raw_data: "type_defs.StopActivityStreamResponseTypeDef" = dataclasses.field()

    KmsKeyId = field("KmsKeyId")
    KinesisStreamName = field("KinesisStreamName")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopActivityStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopActivityStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddSourceIdentifierToSubscriptionResult:
    boto3_raw_data: "type_defs.AddSourceIdentifierToSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddSourceIdentifierToSubscriptionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddSourceIdentifierToSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSubscriptionResult:
    boto3_raw_data: "type_defs.CreateEventSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSubscriptionResult:
    boto3_raw_data: "type_defs.DeleteEventSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSubscriptionsMessage:
    boto3_raw_data: "type_defs.EventSubscriptionsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def EventSubscriptionsList(self):  # pragma: no cover
        return EventSubscription.make_many(
            self.boto3_raw_data["EventSubscriptionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEventSubscriptionResult:
    boto3_raw_data: "type_defs.ModifyEventSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyEventSubscriptionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEventSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveSourceIdentifierFromSubscriptionResult:
    boto3_raw_data: "type_defs.RemoveSourceIdentifierFromSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveSourceIdentifierFromSubscriptionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveSourceIdentifierFromSubscriptionResultTypeDef"]
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
class CopyDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.CopyDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    SourceDBClusterParameterGroupIdentifier = field(
        "SourceDBClusterParameterGroupIdentifier"
    )
    TargetDBClusterParameterGroupIdentifier = field(
        "TargetDBClusterParameterGroupIdentifier"
    )
    TargetDBClusterParameterGroupDescription = field(
        "TargetDBClusterParameterGroupDescription"
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.CopyDBClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    SourceDBClusterSnapshotIdentifier = field("SourceDBClusterSnapshotIdentifier")
    TargetDBClusterSnapshotIdentifier = field("TargetDBClusterSnapshotIdentifier")
    KmsKeyId = field("KmsKeyId")
    PreSignedUrl = field("PreSignedUrl")
    CopyTags = field("CopyTags")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBParameterGroupMessage:
    boto3_raw_data: "type_defs.CopyDBParameterGroupMessageTypeDef" = dataclasses.field()

    SourceDBParameterGroupIdentifier = field("SourceDBParameterGroupIdentifier")
    TargetDBParameterGroupIdentifier = field("TargetDBParameterGroupIdentifier")
    TargetDBParameterGroupDescription = field("TargetDBParameterGroupDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBParameterGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBSnapshotMessage:
    boto3_raw_data: "type_defs.CopyDBSnapshotMessageTypeDef" = dataclasses.field()

    SourceDBSnapshotIdentifier = field("SourceDBSnapshotIdentifier")
    TargetDBSnapshotIdentifier = field("TargetDBSnapshotIdentifier")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CopyTags = field("CopyTags")
    PreSignedUrl = field("PreSignedUrl")
    OptionGroupName = field("OptionGroupName")
    TargetCustomAvailabilityZone = field("TargetCustomAvailabilityZone")
    CopyOptionGroup = field("CopyOptionGroup")
    SnapshotAvailabilityZone = field("SnapshotAvailabilityZone")
    SnapshotTarget = field("SnapshotTarget")
    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyOptionGroupMessage:
    boto3_raw_data: "type_defs.CopyOptionGroupMessageTypeDef" = dataclasses.field()

    SourceOptionGroupIdentifier = field("SourceOptionGroupIdentifier")
    TargetOptionGroupIdentifier = field("TargetOptionGroupIdentifier")
    TargetOptionGroupDescription = field("TargetOptionGroupDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyOptionGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyOptionGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBlueGreenDeploymentRequest:
    boto3_raw_data: "type_defs.CreateBlueGreenDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    BlueGreenDeploymentName = field("BlueGreenDeploymentName")
    Source = field("Source")
    TargetEngineVersion = field("TargetEngineVersion")
    TargetDBParameterGroupName = field("TargetDBParameterGroupName")
    TargetDBClusterParameterGroupName = field("TargetDBClusterParameterGroupName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TargetDBInstanceClass = field("TargetDBInstanceClass")
    UpgradeTargetStorageConfig = field("UpgradeTargetStorageConfig")
    TargetIops = field("TargetIops")
    TargetStorageType = field("TargetStorageType")
    TargetAllocatedStorage = field("TargetAllocatedStorage")
    TargetStorageThroughput = field("TargetStorageThroughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBlueGreenDeploymentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBlueGreenDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomDBEngineVersionMessage:
    boto3_raw_data: "type_defs.CreateCustomDBEngineVersionMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DatabaseInstallationFilesS3BucketName = field(
        "DatabaseInstallationFilesS3BucketName"
    )
    DatabaseInstallationFilesS3Prefix = field("DatabaseInstallationFilesS3Prefix")
    ImageId = field("ImageId")
    KMSKeyId = field("KMSKeyId")
    Description = field("Description")
    Manifest = field("Manifest")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SourceCustomDbEngineVersionIdentifier = field(
        "SourceCustomDbEngineVersionIdentifier"
    )
    UseAwsProvidedLatestImage = field("UseAwsProvidedLatestImage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDBEngineVersionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDBEngineVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterEndpointMessage:
    boto3_raw_data: "type_defs.CreateDBClusterEndpointMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")
    EndpointType = field("EndpointType")
    StaticMembers = field("StaticMembers")
    ExcludedMembers = field("ExcludedMembers")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterEndpointMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.CreateDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.CreateDBClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterSnapshotMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBParameterGroupMessage:
    boto3_raw_data: "type_defs.CreateDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBProxyEndpointRequest:
    boto3_raw_data: "type_defs.CreateDBProxyEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    DBProxyEndpointName = field("DBProxyEndpointName")
    VpcSubnetIds = field("VpcSubnetIds")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    TargetRole = field("TargetRole")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    EndpointNetworkType = field("EndpointNetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBProxyEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBProxyEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSecurityGroupMessage:
    boto3_raw_data: "type_defs.CreateDBSecurityGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBSecurityGroupName = field("DBSecurityGroupName")
    DBSecurityGroupDescription = field("DBSecurityGroupDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSecurityGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBShardGroupMessage:
    boto3_raw_data: "type_defs.CreateDBShardGroupMessageTypeDef" = dataclasses.field()

    DBShardGroupIdentifier = field("DBShardGroupIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    MaxACU = field("MaxACU")
    ComputeRedundancy = field("ComputeRedundancy")
    MinACU = field("MinACU")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBShardGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBShardGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSnapshotMessage:
    boto3_raw_data: "type_defs.CreateDBSnapshotMessageTypeDef" = dataclasses.field()

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSubnetGroupMessage:
    boto3_raw_data: "type_defs.CreateDBSubnetGroupMessageTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")
    DBSubnetGroupDescription = field("DBSubnetGroupDescription")
    SubnetIds = field("SubnetIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSubscriptionMessage:
    boto3_raw_data: "type_defs.CreateEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SnsTopicArn = field("SnsTopicArn")
    SourceType = field("SourceType")
    EventCategories = field("EventCategories")
    SourceIds = field("SourceIds")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalClusterMessage:
    boto3_raw_data: "type_defs.CreateGlobalClusterMessageTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    SourceDBClusterIdentifier = field("SourceDBClusterIdentifier")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    EngineLifecycleSupport = field("EngineLifecycleSupport")
    DeletionProtection = field("DeletionProtection")
    DatabaseName = field("DatabaseName")
    StorageEncrypted = field("StorageEncrypted")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationMessage:
    boto3_raw_data: "type_defs.CreateIntegrationMessageTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    TargetArn = field("TargetArn")
    IntegrationName = field("IntegrationName")
    KMSKeyId = field("KMSKeyId")
    AdditionalEncryptionContext = field("AdditionalEncryptionContext")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DataFilter = field("DataFilter")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntegrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOptionGroupMessage:
    boto3_raw_data: "type_defs.CreateOptionGroupMessageTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")
    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")
    OptionGroupDescription = field("OptionGroupDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOptionGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOptionGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTenantDatabaseMessage:
    boto3_raw_data: "type_defs.CreateTenantDatabaseMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")
    MasterUsername = field("MasterUsername")
    MasterUserPassword = field("MasterUserPassword")
    CharacterSetName = field("CharacterSetName")
    NcharCharacterSetName = field("NcharCharacterSetName")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTenantDatabaseMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTenantDatabaseMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshot:
    boto3_raw_data: "type_defs.DBClusterSnapshotTypeDef" = dataclasses.field()

    AvailabilityZones = field("AvailabilityZones")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    SnapshotCreateTime = field("SnapshotCreateTime")
    Engine = field("Engine")
    EngineMode = field("EngineMode")
    AllocatedStorage = field("AllocatedStorage")
    Status = field("Status")
    Port = field("Port")
    VpcId = field("VpcId")
    ClusterCreateTime = field("ClusterCreateTime")
    MasterUsername = field("MasterUsername")
    EngineVersion = field("EngineVersion")
    LicenseModel = field("LicenseModel")
    SnapshotType = field("SnapshotType")
    PercentProgress = field("PercentProgress")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    DBClusterSnapshotArn = field("DBClusterSnapshotArn")
    SourceDBClusterSnapshotArn = field("SourceDBClusterSnapshotArn")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    DBSystemId = field("DBSystemId")
    StorageType = field("StorageType")
    DbClusterResourceId = field("DbClusterResourceId")
    StorageThroughput = field("StorageThroughput")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBShardGroupResponse:
    boto3_raw_data: "type_defs.DBShardGroupResponseTypeDef" = dataclasses.field()

    DBShardGroupResourceId = field("DBShardGroupResourceId")
    DBShardGroupIdentifier = field("DBShardGroupIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    MaxACU = field("MaxACU")
    MinACU = field("MinACU")
    ComputeRedundancy = field("ComputeRedundancy")
    Status = field("Status")
    PubliclyAccessible = field("PubliclyAccessible")
    Endpoint = field("Endpoint")
    DBShardGroupArn = field("DBShardGroupArn")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBShardGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBShardGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBShardGroup:
    boto3_raw_data: "type_defs.DBShardGroupTypeDef" = dataclasses.field()

    DBShardGroupResourceId = field("DBShardGroupResourceId")
    DBShardGroupIdentifier = field("DBShardGroupIdentifier")
    DBClusterIdentifier = field("DBClusterIdentifier")
    MaxACU = field("MaxACU")
    MinACU = field("MinACU")
    ComputeRedundancy = field("ComputeRedundancy")
    Status = field("Status")
    PubliclyAccessible = field("PubliclyAccessible")
    Endpoint = field("Endpoint")
    DBShardGroupArn = field("DBShardGroupArn")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBShardGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBShardGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSnapshotTenantDatabase:
    boto3_raw_data: "type_defs.DBSnapshotTenantDatabaseTypeDef" = dataclasses.field()

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DbiResourceId = field("DbiResourceId")
    EngineName = field("EngineName")
    SnapshotType = field("SnapshotType")
    TenantDatabaseCreateTime = field("TenantDatabaseCreateTime")
    TenantDBName = field("TenantDBName")
    MasterUsername = field("MasterUsername")
    TenantDatabaseResourceId = field("TenantDatabaseResourceId")
    CharacterSetName = field("CharacterSetName")
    DBSnapshotTenantDatabaseARN = field("DBSnapshotTenantDatabaseARN")
    NcharCharacterSetName = field("NcharCharacterSetName")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSnapshotTenantDatabaseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSnapshotTenantDatabaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedDBInstancesOfferingMessage:
    boto3_raw_data: "type_defs.PurchaseReservedDBInstancesOfferingMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    ReservedDBInstanceId = field("ReservedDBInstanceId")
    DBInstanceCount = field("DBInstanceCount")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedDBInstancesOfferingMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedDBInstancesOfferingMessageTypeDef"]
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
class OrderableDBInstanceOption:
    boto3_raw_data: "type_defs.OrderableDBInstanceOptionTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBInstanceClass = field("DBInstanceClass")
    LicenseModel = field("LicenseModel")
    AvailabilityZoneGroup = field("AvailabilityZoneGroup")

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["AvailabilityZones"])

    MultiAZCapable = field("MultiAZCapable")
    ReadReplicaCapable = field("ReadReplicaCapable")
    Vpc = field("Vpc")
    SupportsStorageEncryption = field("SupportsStorageEncryption")
    StorageType = field("StorageType")
    SupportsIops = field("SupportsIops")
    SupportsEnhancedMonitoring = field("SupportsEnhancedMonitoring")
    SupportsIAMDatabaseAuthentication = field("SupportsIAMDatabaseAuthentication")
    SupportsPerformanceInsights = field("SupportsPerformanceInsights")
    MinStorageSize = field("MinStorageSize")
    MaxStorageSize = field("MaxStorageSize")
    MinIopsPerDbInstance = field("MinIopsPerDbInstance")
    MaxIopsPerDbInstance = field("MaxIopsPerDbInstance")
    MinIopsPerGib = field("MinIopsPerGib")
    MaxIopsPerGib = field("MaxIopsPerGib")

    @cached_property
    def AvailableProcessorFeatures(self):  # pragma: no cover
        return AvailableProcessorFeature.make_many(
            self.boto3_raw_data["AvailableProcessorFeatures"]
        )

    SupportedEngineModes = field("SupportedEngineModes")
    SupportsStorageAutoscaling = field("SupportsStorageAutoscaling")
    SupportsKerberosAuthentication = field("SupportsKerberosAuthentication")
    OutpostCapable = field("OutpostCapable")
    SupportedActivityStreamModes = field("SupportedActivityStreamModes")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")
    SupportsClusters = field("SupportsClusters")
    SupportedNetworkTypes = field("SupportedNetworkTypes")
    SupportsStorageThroughput = field("SupportsStorageThroughput")
    MinStorageThroughputPerDbInstance = field("MinStorageThroughputPerDbInstance")
    MaxStorageThroughputPerDbInstance = field("MaxStorageThroughputPerDbInstance")
    MinStorageThroughputPerIops = field("MinStorageThroughputPerIops")
    MaxStorageThroughputPerIops = field("MaxStorageThroughputPerIops")
    SupportsDedicatedLogVolume = field("SupportsDedicatedLogVolume")
    SupportsHttpEndpoint = field("SupportsHttpEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrderableDBInstanceOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableDBInstanceOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BacktrackDBClusterMessage:
    boto3_raw_data: "type_defs.BacktrackDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    BacktrackTo = field("BacktrackTo")
    Force = field("Force")
    UseEarliestTimeOnPointInTimeUnavailable = field(
        "UseEarliestTimeOnPointInTimeUnavailable"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BacktrackDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BacktrackDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlueGreenDeployment:
    boto3_raw_data: "type_defs.BlueGreenDeploymentTypeDef" = dataclasses.field()

    BlueGreenDeploymentIdentifier = field("BlueGreenDeploymentIdentifier")
    BlueGreenDeploymentName = field("BlueGreenDeploymentName")
    Source = field("Source")
    Target = field("Target")

    @cached_property
    def SwitchoverDetails(self):  # pragma: no cover
        return SwitchoverDetail.make_many(self.boto3_raw_data["SwitchoverDetails"])

    @cached_property
    def Tasks(self):  # pragma: no cover
        return BlueGreenDeploymentTask.make_many(self.boto3_raw_data["Tasks"])

    Status = field("Status")
    StatusDetails = field("StatusDetails")
    CreateTime = field("CreateTime")
    DeleteTime = field("DeleteTime")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BlueGreenDeploymentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlueGreenDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateMessage:
    boto3_raw_data: "type_defs.CertificateMessageTypeDef" = dataclasses.field()

    DefaultCertificateForNewLaunches = field("DefaultCertificateForNewLaunches")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCertificatesResult:
    boto3_raw_data: "type_defs.ModifyCertificatesResultTypeDef" = dataclasses.field()

    @cached_property
    def Certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyCertificatesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCertificatesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterPendingModifiedValues:
    boto3_raw_data: "type_defs.ClusterPendingModifiedValuesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PendingCloudwatchLogsExports(self):  # pragma: no cover
        return PendingCloudwatchLogsExports.make_one(
            self.boto3_raw_data["PendingCloudwatchLogsExports"]
        )

    DBClusterIdentifier = field("DBClusterIdentifier")
    MasterUserPassword = field("MasterUserPassword")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    EngineVersion = field("EngineVersion")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    AllocatedStorage = field("AllocatedStorage")

    @cached_property
    def RdsCustomClusterConfiguration(self):  # pragma: no cover
        return RdsCustomClusterConfiguration.make_one(
            self.boto3_raw_data["RdsCustomClusterConfiguration"]
        )

    Iops = field("Iops")
    StorageType = field("StorageType")

    @cached_property
    def CertificateDetails(self):  # pragma: no cover
        return CertificateDetails.make_one(self.boto3_raw_data["CertificateDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterPendingModifiedValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterPendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBProxyTargetGroup:
    boto3_raw_data: "type_defs.DBProxyTargetGroupTypeDef" = dataclasses.field()

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")
    TargetGroupArn = field("TargetGroupArn")
    IsDefault = field("IsDefault")
    Status = field("Status")

    @cached_property
    def ConnectionPoolConfig(self):  # pragma: no cover
        return ConnectionPoolConfigurationInfo.make_one(
            self.boto3_raw_data["ConnectionPoolConfig"]
        )

    CreatedDate = field("CreatedDate")
    UpdatedDate = field("UpdatedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBProxyTargetGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBProxyTargetGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBProxyTargetGroupRequest:
    boto3_raw_data: "type_defs.ModifyDBProxyTargetGroupRequestTypeDef" = (
        dataclasses.field()
    )

    TargetGroupName = field("TargetGroupName")
    DBProxyName = field("DBProxyName")

    @cached_property
    def ConnectionPoolConfig(self):  # pragma: no cover
        return ConnectionPoolConfiguration.make_one(
            self.boto3_raw_data["ConnectionPoolConfig"]
        )

    NewName = field("NewName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBProxyTargetGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBProxyTargetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterParameterGroupResult:
    boto3_raw_data: "type_defs.CopyDBClusterParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterParameterGroup(self):  # pragma: no cover
        return DBClusterParameterGroup.make_one(
            self.boto3_raw_data["DBClusterParameterGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyDBClusterParameterGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterParameterGroupResult:
    boto3_raw_data: "type_defs.CreateDBClusterParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterParameterGroup(self):  # pragma: no cover
        return DBClusterParameterGroup.make_one(
            self.boto3_raw_data["DBClusterParameterGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDBClusterParameterGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroupsMessage:
    boto3_raw_data: "type_defs.DBClusterParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def DBClusterParameterGroups(self):  # pragma: no cover
        return DBClusterParameterGroup.make_many(
            self.boto3_raw_data["DBClusterParameterGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBClusterParameterGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBParameterGroupResult:
    boto3_raw_data: "type_defs.CopyDBParameterGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBParameterGroup(self):  # pragma: no cover
        return DBParameterGroup.make_one(self.boto3_raw_data["DBParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBParameterGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBParameterGroupResult:
    boto3_raw_data: "type_defs.CreateDBParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBParameterGroup(self):  # pragma: no cover
        return DBParameterGroup.make_one(self.boto3_raw_data["DBParameterGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBParameterGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBParameterGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupsMessage:
    boto3_raw_data: "type_defs.DBParameterGroupsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBParameterGroups(self):  # pragma: no cover
        return DBParameterGroup.make_many(self.boto3_raw_data["DBParameterGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterMessage:
    boto3_raw_data: "type_defs.CreateDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    Engine = field("Engine")
    AvailabilityZones = field("AvailabilityZones")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    CharacterSetName = field("CharacterSetName")
    DatabaseName = field("DatabaseName")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    DBSubnetGroupName = field("DBSubnetGroupName")
    EngineVersion = field("EngineVersion")
    Port = field("Port")
    MasterUsername = field("MasterUsername")
    MasterUserPassword = field("MasterUserPassword")
    OptionGroupName = field("OptionGroupName")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ReplicationSourceIdentifier = field("ReplicationSourceIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    PreSignedUrl = field("PreSignedUrl")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    BacktrackWindow = field("BacktrackWindow")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    EngineMode = field("EngineMode")

    @cached_property
    def ScalingConfiguration(self):  # pragma: no cover
        return ScalingConfiguration.make_one(
            self.boto3_raw_data["ScalingConfiguration"]
        )

    @cached_property
    def RdsCustomClusterConfiguration(self):  # pragma: no cover
        return RdsCustomClusterConfiguration.make_one(
            self.boto3_raw_data["RdsCustomClusterConfiguration"]
        )

    DeletionProtection = field("DeletionProtection")
    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    EnableHttpEndpoint = field("EnableHttpEndpoint")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")
    EnableGlobalWriteForwarding = field("EnableGlobalWriteForwarding")
    DBClusterInstanceClass = field("DBClusterInstanceClass")
    AllocatedStorage = field("AllocatedStorage")
    StorageType = field("StorageType")
    Iops = field("Iops")
    PubliclyAccessible = field("PubliclyAccessible")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EnableLimitlessDatabase = field("EnableLimitlessDatabase")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    NetworkType = field("NetworkType")
    ClusterScalabilityType = field("ClusterScalabilityType")
    DBSystemId = field("DBSystemId")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")
    EnableLocalWriteForwarding = field("EnableLocalWriteForwarding")
    CACertificateIdentifier = field("CACertificateIdentifier")
    EngineLifecycleSupport = field("EngineLifecycleSupport")
    MasterUserAuthenticationType = field("MasterUserAuthenticationType")
    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")
    NewDBClusterIdentifier = field("NewDBClusterIdentifier")
    ApplyImmediately = field("ApplyImmediately")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    Port = field("Port")
    MasterUserPassword = field("MasterUserPassword")
    OptionGroupName = field("OptionGroupName")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    BacktrackWindow = field("BacktrackWindow")

    @cached_property
    def CloudwatchLogsExportConfiguration(self):  # pragma: no cover
        return CloudwatchLogsExportConfiguration.make_one(
            self.boto3_raw_data["CloudwatchLogsExportConfiguration"]
        )

    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")
    DBInstanceParameterGroupName = field("DBInstanceParameterGroupName")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")

    @cached_property
    def ScalingConfiguration(self):  # pragma: no cover
        return ScalingConfiguration.make_one(
            self.boto3_raw_data["ScalingConfiguration"]
        )

    DeletionProtection = field("DeletionProtection")
    EnableHttpEndpoint = field("EnableHttpEndpoint")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    EnableGlobalWriteForwarding = field("EnableGlobalWriteForwarding")
    DBClusterInstanceClass = field("DBClusterInstanceClass")
    AllocatedStorage = field("AllocatedStorage")
    StorageType = field("StorageType")
    Iops = field("Iops")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    NetworkType = field("NetworkType")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    RotateMasterUserPassword = field("RotateMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")
    EngineMode = field("EngineMode")
    AllowEngineModeChange = field("AllowEngineModeChange")
    EnableLocalWriteForwarding = field("EnableLocalWriteForwarding")
    AwsBackupRecoveryPointArn = field("AwsBackupRecoveryPointArn")
    EnableLimitlessDatabase = field("EnableLimitlessDatabase")
    CACertificateIdentifier = field("CACertificateIdentifier")
    MasterUserAuthenticationType = field("MasterUserAuthenticationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterFromS3Message:
    boto3_raw_data: "type_defs.RestoreDBClusterFromS3MessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    Engine = field("Engine")
    MasterUsername = field("MasterUsername")
    SourceEngine = field("SourceEngine")
    SourceEngineVersion = field("SourceEngineVersion")
    S3BucketName = field("S3BucketName")
    S3IngestionRoleArn = field("S3IngestionRoleArn")
    AvailabilityZones = field("AvailabilityZones")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    CharacterSetName = field("CharacterSetName")
    DatabaseName = field("DatabaseName")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    DBSubnetGroupName = field("DBSubnetGroupName")
    EngineVersion = field("EngineVersion")
    Port = field("Port")
    MasterUserPassword = field("MasterUserPassword")
    OptionGroupName = field("OptionGroupName")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    S3Prefix = field("S3Prefix")
    BacktrackWindow = field("BacktrackWindow")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    DeletionProtection = field("DeletionProtection")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    NetworkType = field("NetworkType")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")
    StorageType = field("StorageType")
    EngineLifecycleSupport = field("EngineLifecycleSupport")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreDBClusterFromS3MessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterFromS3MessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterFromSnapshotMessage:
    boto3_raw_data: "type_defs.RestoreDBClusterFromSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    Engine = field("Engine")
    AvailabilityZones = field("AvailabilityZones")
    EngineVersion = field("EngineVersion")
    Port = field("Port")
    DBSubnetGroupName = field("DBSubnetGroupName")
    DatabaseName = field("DatabaseName")
    OptionGroupName = field("OptionGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    BacktrackWindow = field("BacktrackWindow")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    EngineMode = field("EngineMode")

    @cached_property
    def ScalingConfiguration(self):  # pragma: no cover
        return ScalingConfiguration.make_one(
            self.boto3_raw_data["ScalingConfiguration"]
        )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DeletionProtection = field("DeletionProtection")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")
    DBClusterInstanceClass = field("DBClusterInstanceClass")
    StorageType = field("StorageType")
    Iops = field("Iops")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    NetworkType = field("NetworkType")

    @cached_property
    def RdsCustomClusterConfiguration(self):  # pragma: no cover
        return RdsCustomClusterConfiguration.make_one(
            self.boto3_raw_data["RdsCustomClusterConfiguration"]
        )

    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EngineLifecycleSupport = field("EngineLifecycleSupport")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterFromSnapshotMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterFromSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterToPointInTimeMessage:
    boto3_raw_data: "type_defs.RestoreDBClusterToPointInTimeMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    RestoreType = field("RestoreType")
    SourceDBClusterIdentifier = field("SourceDBClusterIdentifier")
    RestoreToTime = field("RestoreToTime")
    UseLatestRestorableTime = field("UseLatestRestorableTime")
    Port = field("Port")
    DBSubnetGroupName = field("DBSubnetGroupName")
    OptionGroupName = field("OptionGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    BacktrackWindow = field("BacktrackWindow")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")
    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    DeletionProtection = field("DeletionProtection")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")

    @cached_property
    def ScalingConfiguration(self):  # pragma: no cover
        return ScalingConfiguration.make_one(
            self.boto3_raw_data["ScalingConfiguration"]
        )

    EngineMode = field("EngineMode")
    DBClusterInstanceClass = field("DBClusterInstanceClass")
    StorageType = field("StorageType")
    PubliclyAccessible = field("PubliclyAccessible")
    Iops = field("Iops")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfiguration.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    NetworkType = field("NetworkType")
    SourceDbClusterResourceId = field("SourceDbClusterResourceId")

    @cached_property
    def RdsCustomClusterConfiguration(self):  # pragma: no cover
        return RdsCustomClusterConfiguration.make_one(
            self.boto3_raw_data["RdsCustomClusterConfiguration"]
        )

    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EngineLifecycleSupport = field("EngineLifecycleSupport")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterToPointInTimeMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterToPointInTimeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBInstanceMessage:
    boto3_raw_data: "type_defs.CreateDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    Engine = field("Engine")
    DBName = field("DBName")
    AllocatedStorage = field("AllocatedStorage")
    MasterUsername = field("MasterUsername")
    MasterUserPassword = field("MasterUserPassword")
    DBSecurityGroups = field("DBSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    AvailabilityZone = field("AvailabilityZone")
    DBSubnetGroupName = field("DBSubnetGroupName")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    DBParameterGroupName = field("DBParameterGroupName")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    PreferredBackupWindow = field("PreferredBackupWindow")
    Port = field("Port")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    CharacterSetName = field("CharacterSetName")
    NcharCharacterSetName = field("NcharCharacterSetName")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DBClusterIdentifier = field("DBClusterIdentifier")
    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    TdeCredentialPassword = field("TdeCredentialPassword")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    Domain = field("Domain")
    DomainFqdn = field("DomainFqdn")
    DomainOu = field("DomainOu")
    DomainAuthSecretArn = field("DomainAuthSecretArn")
    DomainDnsIps = field("DomainDnsIps")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DomainIAMRoleName = field("DomainIAMRoleName")
    PromotionTier = field("PromotionTier")
    Timezone = field("Timezone")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    DeletionProtection = field("DeletionProtection")
    MaxAllocatedStorage = field("MaxAllocatedStorage")
    EnableCustomerOwnedIp = field("EnableCustomerOwnedIp")
    CustomIamInstanceProfile = field("CustomIamInstanceProfile")
    BackupTarget = field("BackupTarget")
    NetworkType = field("NetworkType")
    StorageThroughput = field("StorageThroughput")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")
    CACertificateIdentifier = field("CACertificateIdentifier")
    DBSystemId = field("DBSystemId")
    DedicatedLogVolume = field("DedicatedLogVolume")
    MultiTenant = field("MultiTenant")
    EngineLifecycleSupport = field("EngineLifecycleSupport")
    MasterUserAuthenticationType = field("MasterUserAuthenticationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBInstanceReadReplicaMessage:
    boto3_raw_data: "type_defs.CreateDBInstanceReadReplicaMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    SourceDBInstanceIdentifier = field("SourceDBInstanceIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    AvailabilityZone = field("AvailabilityZone")
    Port = field("Port")
    MultiAZ = field("MultiAZ")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    DBParameterGroupName = field("DBParameterGroupName")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DBSubnetGroupName = field("DBSubnetGroupName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    StorageType = field("StorageType")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    KmsKeyId = field("KmsKeyId")
    PreSignedUrl = field("PreSignedUrl")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    UseDefaultProcessorFeatures = field("UseDefaultProcessorFeatures")
    DeletionProtection = field("DeletionProtection")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")
    DomainFqdn = field("DomainFqdn")
    DomainOu = field("DomainOu")
    DomainAuthSecretArn = field("DomainAuthSecretArn")
    DomainDnsIps = field("DomainDnsIps")
    ReplicaMode = field("ReplicaMode")
    MaxAllocatedStorage = field("MaxAllocatedStorage")
    CustomIamInstanceProfile = field("CustomIamInstanceProfile")
    NetworkType = field("NetworkType")
    StorageThroughput = field("StorageThroughput")
    EnableCustomerOwnedIp = field("EnableCustomerOwnedIp")
    BackupTarget = field("BackupTarget")
    AllocatedStorage = field("AllocatedStorage")
    SourceDBClusterIdentifier = field("SourceDBClusterIdentifier")
    DedicatedLogVolume = field("DedicatedLogVolume")
    UpgradeStorageConfig = field("UpgradeStorageConfig")
    CACertificateIdentifier = field("CACertificateIdentifier")
    SourceRegion = field("SourceRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDBInstanceReadReplicaMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBInstanceReadReplicaMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSnapshot:
    boto3_raw_data: "type_defs.DBSnapshotTypeDef" = dataclasses.field()

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    DBInstanceIdentifier = field("DBInstanceIdentifier")
    SnapshotCreateTime = field("SnapshotCreateTime")
    Engine = field("Engine")
    AllocatedStorage = field("AllocatedStorage")
    Status = field("Status")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")
    VpcId = field("VpcId")
    InstanceCreateTime = field("InstanceCreateTime")
    MasterUsername = field("MasterUsername")
    EngineVersion = field("EngineVersion")
    LicenseModel = field("LicenseModel")
    SnapshotType = field("SnapshotType")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    PercentProgress = field("PercentProgress")
    SourceRegion = field("SourceRegion")
    SourceDBSnapshotIdentifier = field("SourceDBSnapshotIdentifier")
    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    DBSnapshotArn = field("DBSnapshotArn")
    Timezone = field("Timezone")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    DbiResourceId = field("DbiResourceId")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    OriginalSnapshotCreateTime = field("OriginalSnapshotCreateTime")
    SnapshotDatabaseTime = field("SnapshotDatabaseTime")
    SnapshotTarget = field("SnapshotTarget")
    StorageThroughput = field("StorageThroughput")
    DBSystemId = field("DBSystemId")
    DedicatedLogVolume = field("DedicatedLogVolume")
    MultiTenant = field("MultiTenant")
    SnapshotAvailabilityZone = field("SnapshotAvailabilityZone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBSnapshotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBInstanceMessage:
    boto3_raw_data: "type_defs.ModifyDBInstanceMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    AllocatedStorage = field("AllocatedStorage")
    DBInstanceClass = field("DBInstanceClass")
    DBSubnetGroupName = field("DBSubnetGroupName")
    DBSecurityGroups = field("DBSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    ApplyImmediately = field("ApplyImmediately")
    MasterUserPassword = field("MasterUserPassword")
    DBParameterGroupName = field("DBParameterGroupName")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    NewDBInstanceIdentifier = field("NewDBInstanceIdentifier")
    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    TdeCredentialPassword = field("TdeCredentialPassword")
    CACertificateIdentifier = field("CACertificateIdentifier")
    Domain = field("Domain")
    DomainFqdn = field("DomainFqdn")
    DomainOu = field("DomainOu")
    DomainAuthSecretArn = field("DomainAuthSecretArn")
    DomainDnsIps = field("DomainDnsIps")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    DBPortNumber = field("DBPortNumber")
    PubliclyAccessible = field("PubliclyAccessible")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DomainIAMRoleName = field("DomainIAMRoleName")
    DisableDomain = field("DisableDomain")
    PromotionTier = field("PromotionTier")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")

    @cached_property
    def CloudwatchLogsExportConfiguration(self):  # pragma: no cover
        return CloudwatchLogsExportConfiguration.make_one(
            self.boto3_raw_data["CloudwatchLogsExportConfiguration"]
        )

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    UseDefaultProcessorFeatures = field("UseDefaultProcessorFeatures")
    DeletionProtection = field("DeletionProtection")
    MaxAllocatedStorage = field("MaxAllocatedStorage")
    CertificateRotationRestart = field("CertificateRotationRestart")
    ReplicaMode = field("ReplicaMode")
    EnableCustomerOwnedIp = field("EnableCustomerOwnedIp")
    AwsBackupRecoveryPointArn = field("AwsBackupRecoveryPointArn")
    AutomationMode = field("AutomationMode")
    ResumeFullAutomationModeMinutes = field("ResumeFullAutomationModeMinutes")
    NetworkType = field("NetworkType")
    StorageThroughput = field("StorageThroughput")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    RotateMasterUserPassword = field("RotateMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")
    Engine = field("Engine")
    DedicatedLogVolume = field("DedicatedLogVolume")
    MultiTenant = field("MultiTenant")
    MasterUserAuthenticationType = field("MasterUserAuthenticationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBInstanceMessageTypeDef"]
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

    DBInstanceClass = field("DBInstanceClass")
    AllocatedStorage = field("AllocatedStorage")
    MasterUserPassword = field("MasterUserPassword")
    Port = field("Port")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    DBInstanceIdentifier = field("DBInstanceIdentifier")
    StorageType = field("StorageType")
    CACertificateIdentifier = field("CACertificateIdentifier")
    DBSubnetGroupName = field("DBSubnetGroupName")

    @cached_property
    def PendingCloudwatchLogsExports(self):  # pragma: no cover
        return PendingCloudwatchLogsExports.make_one(
            self.boto3_raw_data["PendingCloudwatchLogsExports"]
        )

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    AutomationMode = field("AutomationMode")
    ResumeFullAutomationModeTime = field("ResumeFullAutomationModeTime")
    StorageThroughput = field("StorageThroughput")
    Engine = field("Engine")
    DedicatedLogVolume = field("DedicatedLogVolume")
    MultiTenant = field("MultiTenant")

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
class RestoreDBInstanceFromDBSnapshotMessage:
    boto3_raw_data: "type_defs.RestoreDBInstanceFromDBSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")
    DBSubnetGroupName = field("DBSubnetGroupName")
    MultiAZ = field("MultiAZ")
    PubliclyAccessible = field("PubliclyAccessible")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    DBName = field("DBName")
    Engine = field("Engine")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    TdeCredentialPassword = field("TdeCredentialPassword")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    Domain = field("Domain")
    DomainFqdn = field("DomainFqdn")
    DomainOu = field("DomainOu")
    DomainAuthSecretArn = field("DomainAuthSecretArn")
    DomainDnsIps = field("DomainDnsIps")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    DomainIAMRoleName = field("DomainIAMRoleName")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    UseDefaultProcessorFeatures = field("UseDefaultProcessorFeatures")
    DBParameterGroupName = field("DBParameterGroupName")
    DeletionProtection = field("DeletionProtection")
    EnableCustomerOwnedIp = field("EnableCustomerOwnedIp")
    CustomIamInstanceProfile = field("CustomIamInstanceProfile")
    BackupTarget = field("BackupTarget")
    NetworkType = field("NetworkType")
    StorageThroughput = field("StorageThroughput")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    AllocatedStorage = field("AllocatedStorage")
    DedicatedLogVolume = field("DedicatedLogVolume")
    CACertificateIdentifier = field("CACertificateIdentifier")
    EngineLifecycleSupport = field("EngineLifecycleSupport")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBInstanceFromDBSnapshotMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBInstanceFromDBSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBInstanceFromS3Message:
    boto3_raw_data: "type_defs.RestoreDBInstanceFromS3MessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    Engine = field("Engine")
    SourceEngine = field("SourceEngine")
    SourceEngineVersion = field("SourceEngineVersion")
    S3BucketName = field("S3BucketName")
    S3IngestionRoleArn = field("S3IngestionRoleArn")
    DBName = field("DBName")
    AllocatedStorage = field("AllocatedStorage")
    MasterUsername = field("MasterUsername")
    MasterUserPassword = field("MasterUserPassword")
    DBSecurityGroups = field("DBSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    AvailabilityZone = field("AvailabilityZone")
    DBSubnetGroupName = field("DBSubnetGroupName")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    DBParameterGroupName = field("DBParameterGroupName")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    PreferredBackupWindow = field("PreferredBackupWindow")
    Port = field("Port")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageType = field("StorageType")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    S3Prefix = field("S3Prefix")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    EnablePerformanceInsights = field("EnablePerformanceInsights")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    UseDefaultProcessorFeatures = field("UseDefaultProcessorFeatures")
    DeletionProtection = field("DeletionProtection")
    MaxAllocatedStorage = field("MaxAllocatedStorage")
    NetworkType = field("NetworkType")
    StorageThroughput = field("StorageThroughput")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")
    DedicatedLogVolume = field("DedicatedLogVolume")
    CACertificateIdentifier = field("CACertificateIdentifier")
    EngineLifecycleSupport = field("EngineLifecycleSupport")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreDBInstanceFromS3MessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBInstanceFromS3MessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBInstanceToPointInTimeMessage:
    boto3_raw_data: "type_defs.RestoreDBInstanceToPointInTimeMessageTypeDef" = (
        dataclasses.field()
    )

    TargetDBInstanceIdentifier = field("TargetDBInstanceIdentifier")
    SourceDBInstanceIdentifier = field("SourceDBInstanceIdentifier")
    RestoreTime = field("RestoreTime")
    UseLatestRestorableTime = field("UseLatestRestorableTime")
    DBInstanceClass = field("DBInstanceClass")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")
    DBSubnetGroupName = field("DBSubnetGroupName")
    MultiAZ = field("MultiAZ")
    PubliclyAccessible = field("PubliclyAccessible")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    LicenseModel = field("LicenseModel")
    DBName = field("DBName")
    Engine = field("Engine")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    TdeCredentialPassword = field("TdeCredentialPassword")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    Domain = field("Domain")
    DomainIAMRoleName = field("DomainIAMRoleName")
    DomainFqdn = field("DomainFqdn")
    DomainOu = field("DomainOu")
    DomainAuthSecretArn = field("DomainAuthSecretArn")
    DomainDnsIps = field("DomainDnsIps")
    EnableIAMDatabaseAuthentication = field("EnableIAMDatabaseAuthentication")
    EnableCloudwatchLogsExports = field("EnableCloudwatchLogsExports")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    UseDefaultProcessorFeatures = field("UseDefaultProcessorFeatures")
    DBParameterGroupName = field("DBParameterGroupName")
    DeletionProtection = field("DeletionProtection")
    SourceDbiResourceId = field("SourceDbiResourceId")
    MaxAllocatedStorage = field("MaxAllocatedStorage")
    SourceDBInstanceAutomatedBackupsArn = field("SourceDBInstanceAutomatedBackupsArn")
    EnableCustomerOwnedIp = field("EnableCustomerOwnedIp")
    CustomIamInstanceProfile = field("CustomIamInstanceProfile")
    BackupTarget = field("BackupTarget")
    NetworkType = field("NetworkType")
    StorageThroughput = field("StorageThroughput")
    AllocatedStorage = field("AllocatedStorage")
    DedicatedLogVolume = field("DedicatedLogVolume")
    CACertificateIdentifier = field("CACertificateIdentifier")
    EngineLifecycleSupport = field("EngineLifecycleSupport")
    ManageMasterUserPassword = field("ManageMasterUserPassword")
    MasterUserSecretKmsKeyId = field("MasterUserSecretKmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBInstanceToPointInTimeMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBInstanceToPointInTimeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBProxyEndpointResponse:
    boto3_raw_data: "type_defs.CreateDBProxyEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBProxyEndpoint(self):  # pragma: no cover
        return DBProxyEndpoint.make_one(self.boto3_raw_data["DBProxyEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBProxyEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBProxyEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBProxyEndpointResponse:
    boto3_raw_data: "type_defs.DeleteDBProxyEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBProxyEndpoint(self):  # pragma: no cover
        return DBProxyEndpoint.make_one(self.boto3_raw_data["DBProxyEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBProxyEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBProxyEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeDBProxyEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBProxyEndpoints(self):  # pragma: no cover
        return DBProxyEndpoint.make_many(self.boto3_raw_data["DBProxyEndpoints"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBProxyEndpointsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBProxyEndpointResponse:
    boto3_raw_data: "type_defs.ModifyDBProxyEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBProxyEndpoint(self):  # pragma: no cover
        return DBProxyEndpoint.make_one(self.boto3_raw_data["DBProxyEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBProxyEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBProxyEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBProxyRequest:
    boto3_raw_data: "type_defs.CreateDBProxyRequestTypeDef" = dataclasses.field()

    DBProxyName = field("DBProxyName")
    EngineFamily = field("EngineFamily")
    RoleArn = field("RoleArn")
    VpcSubnetIds = field("VpcSubnetIds")
    DefaultAuthScheme = field("DefaultAuthScheme")

    @cached_property
    def Auth(self):  # pragma: no cover
        return UserAuthConfig.make_many(self.boto3_raw_data["Auth"])

    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    RequireTLS = field("RequireTLS")
    IdleClientTimeout = field("IdleClientTimeout")
    DebugLogging = field("DebugLogging")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    EndpointNetworkType = field("EndpointNetworkType")
    TargetConnectionNetworkType = field("TargetConnectionNetworkType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBProxyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBProxyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBProxyRequest:
    boto3_raw_data: "type_defs.ModifyDBProxyRequestTypeDef" = dataclasses.field()

    DBProxyName = field("DBProxyName")
    NewDBProxyName = field("NewDBProxyName")
    DefaultAuthScheme = field("DefaultAuthScheme")

    @cached_property
    def Auth(self):  # pragma: no cover
        return UserAuthConfig.make_many(self.boto3_raw_data["Auth"])

    RequireTLS = field("RequireTLS")
    IdleClientTimeout = field("IdleClientTimeout")
    DebugLogging = field("DebugLogging")
    RoleArn = field("RoleArn")
    SecurityGroups = field("SecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBProxyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBProxyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterAutomatedBackup:
    boto3_raw_data: "type_defs.DBClusterAutomatedBackupTypeDef" = dataclasses.field()

    Engine = field("Engine")
    VpcId = field("VpcId")
    DBClusterAutomatedBackupsArn = field("DBClusterAutomatedBackupsArn")
    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def RestoreWindow(self):  # pragma: no cover
        return RestoreWindow.make_one(self.boto3_raw_data["RestoreWindow"])

    MasterUsername = field("MasterUsername")
    DbClusterResourceId = field("DbClusterResourceId")
    Region = field("Region")
    LicenseModel = field("LicenseModel")
    Status = field("Status")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    ClusterCreateTime = field("ClusterCreateTime")
    StorageEncrypted = field("StorageEncrypted")
    AllocatedStorage = field("AllocatedStorage")
    EngineVersion = field("EngineVersion")
    DBClusterArn = field("DBClusterArn")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    EngineMode = field("EngineMode")
    AvailabilityZones = field("AvailabilityZones")
    Port = field("Port")
    KmsKeyId = field("KmsKeyId")
    StorageType = field("StorageType")
    Iops = field("Iops")
    AwsBackupRecoveryPointArn = field("AwsBackupRecoveryPointArn")
    StorageThroughput = field("StorageThroughput")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterAutomatedBackupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterAutomatedBackupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterBacktrackMessage:
    boto3_raw_data: "type_defs.DBClusterBacktrackMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusterBacktracks(self):  # pragma: no cover
        return DBClusterBacktrack.make_many(self.boto3_raw_data["DBClusterBacktracks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterBacktrackMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterBacktrackMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterEndpointMessage:
    boto3_raw_data: "type_defs.DBClusterEndpointMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusterEndpoints(self):  # pragma: no cover
        return DBClusterEndpoint.make_many(self.boto3_raw_data["DBClusterEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterEndpointMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterParameterGroupDetails:
    boto3_raw_data: "type_defs.DBClusterParameterGroupDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterOutput.make_many(self.boto3_raw_data["Parameters"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBClusterParameterGroupDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterParameterGroupDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBParameterGroupDetails:
    boto3_raw_data: "type_defs.DBParameterGroupDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterOutput.make_many(self.boto3_raw_data["Parameters"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBParameterGroupDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBParameterGroupDetailsTypeDef"]
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

    DBParameterGroupFamily = field("DBParameterGroupFamily")
    Marker = field("Marker")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterOutput.make_many(self.boto3_raw_data["Parameters"])

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
class DBClusterSnapshotAttributesResult:
    boto3_raw_data: "type_defs.DBClusterSnapshotAttributesResultTypeDef" = (
        dataclasses.field()
    )

    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")

    @cached_property
    def DBClusterSnapshotAttributes(self):  # pragma: no cover
        return DBClusterSnapshotAttribute.make_many(
            self.boto3_raw_data["DBClusterSnapshotAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DBClusterSnapshotAttributesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBEngineVersionResponse:
    boto3_raw_data: "type_defs.DBEngineVersionResponseTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    DBEngineDescription = field("DBEngineDescription")
    DBEngineVersionDescription = field("DBEngineVersionDescription")

    @cached_property
    def DefaultCharacterSet(self):  # pragma: no cover
        return CharacterSet.make_one(self.boto3_raw_data["DefaultCharacterSet"])

    @cached_property
    def Image(self):  # pragma: no cover
        return CustomDBEngineVersionAMI.make_one(self.boto3_raw_data["Image"])

    DBEngineMediaType = field("DBEngineMediaType")

    @cached_property
    def SupportedCharacterSets(self):  # pragma: no cover
        return CharacterSet.make_many(self.boto3_raw_data["SupportedCharacterSets"])

    @cached_property
    def SupportedNcharCharacterSets(self):  # pragma: no cover
        return CharacterSet.make_many(
            self.boto3_raw_data["SupportedNcharCharacterSets"]
        )

    @cached_property
    def ValidUpgradeTarget(self):  # pragma: no cover
        return UpgradeTarget.make_many(self.boto3_raw_data["ValidUpgradeTarget"])

    @cached_property
    def SupportedTimezones(self):  # pragma: no cover
        return Timezone.make_many(self.boto3_raw_data["SupportedTimezones"])

    ExportableLogTypes = field("ExportableLogTypes")
    SupportsLogExportsToCloudwatchLogs = field("SupportsLogExportsToCloudwatchLogs")
    SupportsReadReplica = field("SupportsReadReplica")
    SupportedEngineModes = field("SupportedEngineModes")
    SupportedFeatureNames = field("SupportedFeatureNames")
    Status = field("Status")
    SupportsParallelQuery = field("SupportsParallelQuery")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")
    MajorEngineVersion = field("MajorEngineVersion")
    DatabaseInstallationFilesS3BucketName = field(
        "DatabaseInstallationFilesS3BucketName"
    )
    DatabaseInstallationFilesS3Prefix = field("DatabaseInstallationFilesS3Prefix")
    DBEngineVersionArn = field("DBEngineVersionArn")
    KMSKeyId = field("KMSKeyId")
    CreateTime = field("CreateTime")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    SupportsBabelfish = field("SupportsBabelfish")
    CustomDBEngineVersionManifest = field("CustomDBEngineVersionManifest")
    SupportsLimitlessDatabase = field("SupportsLimitlessDatabase")
    SupportsCertificateRotationWithoutRestart = field(
        "SupportsCertificateRotationWithoutRestart"
    )
    SupportedCACertificateIdentifiers = field("SupportedCACertificateIdentifiers")
    SupportsLocalWriteForwarding = field("SupportsLocalWriteForwarding")
    SupportsIntegrations = field("SupportsIntegrations")

    @cached_property
    def ServerlessV2FeaturesSupport(self):  # pragma: no cover
        return ServerlessV2FeaturesSupport.make_one(
            self.boto3_raw_data["ServerlessV2FeaturesSupport"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBEngineVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBEngineVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBEngineVersion:
    boto3_raw_data: "type_defs.DBEngineVersionTypeDef" = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")
    DBEngineDescription = field("DBEngineDescription")
    DBEngineVersionDescription = field("DBEngineVersionDescription")

    @cached_property
    def DefaultCharacterSet(self):  # pragma: no cover
        return CharacterSet.make_one(self.boto3_raw_data["DefaultCharacterSet"])

    @cached_property
    def Image(self):  # pragma: no cover
        return CustomDBEngineVersionAMI.make_one(self.boto3_raw_data["Image"])

    DBEngineMediaType = field("DBEngineMediaType")

    @cached_property
    def SupportedCharacterSets(self):  # pragma: no cover
        return CharacterSet.make_many(self.boto3_raw_data["SupportedCharacterSets"])

    @cached_property
    def SupportedNcharCharacterSets(self):  # pragma: no cover
        return CharacterSet.make_many(
            self.boto3_raw_data["SupportedNcharCharacterSets"]
        )

    @cached_property
    def ValidUpgradeTarget(self):  # pragma: no cover
        return UpgradeTarget.make_many(self.boto3_raw_data["ValidUpgradeTarget"])

    @cached_property
    def SupportedTimezones(self):  # pragma: no cover
        return Timezone.make_many(self.boto3_raw_data["SupportedTimezones"])

    ExportableLogTypes = field("ExportableLogTypes")
    SupportsLogExportsToCloudwatchLogs = field("SupportsLogExportsToCloudwatchLogs")
    SupportsReadReplica = field("SupportsReadReplica")
    SupportedEngineModes = field("SupportedEngineModes")
    SupportedFeatureNames = field("SupportedFeatureNames")
    Status = field("Status")
    SupportsParallelQuery = field("SupportsParallelQuery")
    SupportsGlobalDatabases = field("SupportsGlobalDatabases")
    MajorEngineVersion = field("MajorEngineVersion")
    DatabaseInstallationFilesS3BucketName = field(
        "DatabaseInstallationFilesS3BucketName"
    )
    DatabaseInstallationFilesS3Prefix = field("DatabaseInstallationFilesS3Prefix")
    DBEngineVersionArn = field("DBEngineVersionArn")
    KMSKeyId = field("KMSKeyId")
    CreateTime = field("CreateTime")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    SupportsBabelfish = field("SupportsBabelfish")
    CustomDBEngineVersionManifest = field("CustomDBEngineVersionManifest")
    SupportsLimitlessDatabase = field("SupportsLimitlessDatabase")
    SupportsCertificateRotationWithoutRestart = field(
        "SupportsCertificateRotationWithoutRestart"
    )
    SupportedCACertificateIdentifiers = field("SupportedCACertificateIdentifiers")
    SupportsLocalWriteForwarding = field("SupportsLocalWriteForwarding")
    SupportsIntegrations = field("SupportsIntegrations")

    @cached_property
    def ServerlessV2FeaturesSupport(self):  # pragma: no cover
        return ServerlessV2FeaturesSupport.make_one(
            self.boto3_raw_data["ServerlessV2FeaturesSupport"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBEngineVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBEngineVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceAutomatedBackup:
    boto3_raw_data: "type_defs.DBInstanceAutomatedBackupTypeDef" = dataclasses.field()

    DBInstanceArn = field("DBInstanceArn")
    DbiResourceId = field("DbiResourceId")
    Region = field("Region")
    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def RestoreWindow(self):  # pragma: no cover
        return RestoreWindow.make_one(self.boto3_raw_data["RestoreWindow"])

    AllocatedStorage = field("AllocatedStorage")
    Status = field("Status")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")
    VpcId = field("VpcId")
    InstanceCreateTime = field("InstanceCreateTime")
    MasterUsername = field("MasterUsername")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")
    OptionGroupName = field("OptionGroupName")
    TdeCredentialArn = field("TdeCredentialArn")
    Encrypted = field("Encrypted")
    StorageType = field("StorageType")
    KmsKeyId = field("KmsKeyId")
    Timezone = field("Timezone")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    DBInstanceAutomatedBackupsArn = field("DBInstanceAutomatedBackupsArn")

    @cached_property
    def DBInstanceAutomatedBackupsReplications(self):  # pragma: no cover
        return DBInstanceAutomatedBackupsReplication.make_many(
            self.boto3_raw_data["DBInstanceAutomatedBackupsReplications"]
        )

    BackupTarget = field("BackupTarget")
    StorageThroughput = field("StorageThroughput")
    AwsBackupRecoveryPointArn = field("AwsBackupRecoveryPointArn")
    DedicatedLogVolume = field("DedicatedLogVolume")
    MultiTenant = field("MultiTenant")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBInstanceAutomatedBackupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceAutomatedBackupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBMajorEngineVersion:
    boto3_raw_data: "type_defs.DBMajorEngineVersionTypeDef" = dataclasses.field()

    Engine = field("Engine")
    MajorEngineVersion = field("MajorEngineVersion")

    @cached_property
    def SupportedEngineLifecycles(self):  # pragma: no cover
        return SupportedEngineLifecycle.make_many(
            self.boto3_raw_data["SupportedEngineLifecycles"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBMajorEngineVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBMajorEngineVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBProxyTarget:
    boto3_raw_data: "type_defs.DBProxyTargetTypeDef" = dataclasses.field()

    TargetArn = field("TargetArn")
    Endpoint = field("Endpoint")
    TrackedClusterId = field("TrackedClusterId")
    RdsResourceId = field("RdsResourceId")
    Port = field("Port")
    Type = field("Type")
    Role = field("Role")

    @cached_property
    def TargetHealth(self):  # pragma: no cover
        return TargetHealth.make_one(self.boto3_raw_data["TargetHealth"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBProxyTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBProxyTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBProxy:
    boto3_raw_data: "type_defs.DBProxyTypeDef" = dataclasses.field()

    DBProxyName = field("DBProxyName")
    DBProxyArn = field("DBProxyArn")
    Status = field("Status")
    EngineFamily = field("EngineFamily")
    VpcId = field("VpcId")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    VpcSubnetIds = field("VpcSubnetIds")
    DefaultAuthScheme = field("DefaultAuthScheme")

    @cached_property
    def Auth(self):  # pragma: no cover
        return UserAuthConfigInfo.make_many(self.boto3_raw_data["Auth"])

    RoleArn = field("RoleArn")
    Endpoint = field("Endpoint")
    RequireTLS = field("RequireTLS")
    IdleClientTimeout = field("IdleClientTimeout")
    DebugLogging = field("DebugLogging")
    CreatedDate = field("CreatedDate")
    UpdatedDate = field("UpdatedDate")
    EndpointNetworkType = field("EndpointNetworkType")
    TargetConnectionNetworkType = field("TargetConnectionNetworkType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBProxyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBProxyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSecurityGroup:
    boto3_raw_data: "type_defs.DBSecurityGroupTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    DBSecurityGroupName = field("DBSecurityGroupName")
    DBSecurityGroupDescription = field("DBSecurityGroupDescription")
    VpcId = field("VpcId")

    @cached_property
    def EC2SecurityGroups(self):  # pragma: no cover
        return EC2SecurityGroup.make_many(self.boto3_raw_data["EC2SecurityGroups"])

    @cached_property
    def IPRanges(self):  # pragma: no cover
        return IPRange.make_many(self.boto3_raw_data["IPRanges"])

    DBSecurityGroupArn = field("DBSecurityGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBSecurityGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBSecurityGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSnapshotAttributesResult:
    boto3_raw_data: "type_defs.DBSnapshotAttributesResultTypeDef" = dataclasses.field()

    DBSnapshotIdentifier = field("DBSnapshotIdentifier")

    @cached_property
    def DBSnapshotAttributes(self):  # pragma: no cover
        return DBSnapshotAttribute.make_many(
            self.boto3_raw_data["DBSnapshotAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSnapshotAttributesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSnapshotAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBlueGreenDeploymentsRequest:
    boto3_raw_data: "type_defs.DescribeBlueGreenDeploymentsRequestTypeDef" = (
        dataclasses.field()
    )

    BlueGreenDeploymentIdentifier = field("BlueGreenDeploymentIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBlueGreenDeploymentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBlueGreenDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificatesMessage:
    boto3_raw_data: "type_defs.DescribeCertificatesMessageTypeDef" = dataclasses.field()

    CertificateIdentifier = field("CertificateIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificatesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificatesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterAutomatedBackupsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterAutomatedBackupsMessageTypeDef" = (
        dataclasses.field()
    )

    DbClusterResourceId = field("DbClusterResourceId")
    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterAutomatedBackupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterAutomatedBackupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterBacktracksMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterBacktracksMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    BacktrackIdentifier = field("BacktrackIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterBacktracksMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterBacktracksMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterEndpointsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterEndpointsMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterEndpointsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterEndpointsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParameterGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterParameterGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParametersMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterParametersMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    Source = field("Source")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotsMessage:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotsMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbClusterResourceId = field("DbClusterResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClustersMessage:
    boto3_raw_data: "type_defs.DescribeDBClustersMessageTypeDef" = dataclasses.field()

    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBClustersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBEngineVersionsMessage:
    boto3_raw_data: "type_defs.DescribeDBEngineVersionsMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    DefaultOnly = field("DefaultOnly")
    ListSupportedCharacterSets = field("ListSupportedCharacterSets")
    ListSupportedTimezones = field("ListSupportedTimezones")
    IncludeAll = field("IncludeAll")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBEngineVersionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBEngineVersionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstanceAutomatedBackupsMessage:
    boto3_raw_data: "type_defs.DescribeDBInstanceAutomatedBackupsMessageTypeDef" = (
        dataclasses.field()
    )

    DbiResourceId = field("DbiResourceId")
    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    DBInstanceAutomatedBackupsArn = field("DBInstanceAutomatedBackupsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBInstanceAutomatedBackupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstanceAutomatedBackupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessage:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBInstancesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBLogFilesMessage:
    boto3_raw_data: "type_defs.DescribeDBLogFilesMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    FilenameContains = field("FilenameContains")
    FileLastWritten = field("FileLastWritten")
    FileSize = field("FileSize")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBLogFilesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBLogFilesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParameterGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBParameterGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParametersMessage:
    boto3_raw_data: "type_defs.DescribeDBParametersMessageTypeDef" = dataclasses.field()

    DBParameterGroupName = field("DBParameterGroupName")
    Source = field("Source")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBParametersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxiesRequest:
    boto3_raw_data: "type_defs.DescribeDBProxiesRequestTypeDef" = dataclasses.field()

    DBProxyName = field("DBProxyName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBProxiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyEndpointsRequest:
    boto3_raw_data: "type_defs.DescribeDBProxyEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    DBProxyEndpointName = field("DBProxyEndpointName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBProxyEndpointsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyTargetGroupsRequest:
    boto3_raw_data: "type_defs.DescribeDBProxyTargetGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBProxyTargetGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyTargetGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyTargetsRequest:
    boto3_raw_data: "type_defs.DescribeDBProxyTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBProxyTargetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBRecommendationsMessage:
    boto3_raw_data: "type_defs.DescribeDBRecommendationsMessageTypeDef" = (
        dataclasses.field()
    )

    LastUpdatedAfter = field("LastUpdatedAfter")
    LastUpdatedBefore = field("LastUpdatedBefore")
    Locale = field("Locale")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBRecommendationsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBRecommendationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSecurityGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBSecurityGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBSecurityGroupName = field("DBSecurityGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBSecurityGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSecurityGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBShardGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBShardGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBShardGroupIdentifier = field("DBShardGroupIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBShardGroupsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBShardGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotTenantDatabasesMessage:
    boto3_raw_data: "type_defs.DescribeDBSnapshotTenantDatabasesMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    DbiResourceId = field("DbiResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotTenantDatabasesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotTenantDatabasesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotsMessage:
    boto3_raw_data: "type_defs.DescribeDBSnapshotsMessageTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbiResourceId = field("DbiResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBSnapshotsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSubnetGroupsMessage:
    boto3_raw_data: "type_defs.DescribeDBSubnetGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    DBSubnetGroupName = field("DBSubnetGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBSubnetGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSubnetGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultClusterParametersMessage:
    boto3_raw_data: "type_defs.DescribeEngineDefaultClusterParametersMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEngineDefaultClusterParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultClusterParametersMessageTypeDef"]
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

    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

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
class DescribeEventCategoriesMessage:
    boto3_raw_data: "type_defs.DescribeEventCategoriesMessageTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventCategoriesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventCategoriesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSubscriptionsMessage:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSubscriptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsMessageTypeDef"]
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
    EventCategories = field("EventCategories")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

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
class DescribeExportTasksMessage:
    boto3_raw_data: "type_defs.DescribeExportTasksMessageTypeDef" = dataclasses.field()

    ExportTaskIdentifier = field("ExportTaskIdentifier")
    SourceArn = field("SourceArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")
    SourceType = field("SourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportTasksMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportTasksMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalClustersMessage:
    boto3_raw_data: "type_defs.DescribeGlobalClustersMessageTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGlobalClustersMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIntegrationsMessage:
    boto3_raw_data: "type_defs.DescribeIntegrationsMessageTypeDef" = dataclasses.field()

    IntegrationIdentifier = field("IntegrationIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIntegrationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIntegrationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptionGroupOptionsMessage:
    boto3_raw_data: "type_defs.DescribeOptionGroupOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOptionGroupOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptionGroupOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptionGroupsMessage:
    boto3_raw_data: "type_defs.DescribeOptionGroupsMessageTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")
    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOptionGroupsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptionGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableDBInstanceOptionsMessage:
    boto3_raw_data: "type_defs.DescribeOrderableDBInstanceOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBInstanceClass = field("DBInstanceClass")
    LicenseModel = field("LicenseModel")
    AvailabilityZoneGroup = field("AvailabilityZoneGroup")
    Vpc = field("Vpc")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableDBInstanceOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrderableDBInstanceOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingMaintenanceActionsMessage:
    boto3_raw_data: "type_defs.DescribePendingMaintenanceActionsMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingMaintenanceActionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePendingMaintenanceActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedDBInstancesMessage:
    boto3_raw_data: "type_defs.DescribeReservedDBInstancesMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedDBInstanceId = field("ReservedDBInstanceId")
    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    DBInstanceClass = field("DBInstanceClass")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MultiAZ = field("MultiAZ")
    LeaseId = field("LeaseId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedDBInstancesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedDBInstancesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedDBInstancesOfferingsMessage:
    boto3_raw_data: "type_defs.DescribeReservedDBInstancesOfferingsMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    DBInstanceClass = field("DBInstanceClass")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MultiAZ = field("MultiAZ")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedDBInstancesOfferingsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedDBInstancesOfferingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceRegionsMessage:
    boto3_raw_data: "type_defs.DescribeSourceRegionsMessageTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSourceRegionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceRegionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTenantDatabasesMessage:
    boto3_raw_data: "type_defs.DescribeTenantDatabasesMessageTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTenantDatabasesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTenantDatabasesMessageTypeDef"]
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

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

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
class DescribeBlueGreenDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeBlueGreenDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    BlueGreenDeploymentIdentifier = field("BlueGreenDeploymentIdentifier")

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
            "type_defs.DescribeBlueGreenDeploymentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBlueGreenDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificatesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCertificatesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    CertificateIdentifier = field("CertificateIdentifier")

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
            "type_defs.DescribeCertificatesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificatesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterAutomatedBackupsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeDBClusterAutomatedBackupsMessagePaginateTypeDef"
    ) = dataclasses.field()

    DbClusterResourceId = field("DbClusterResourceId")
    DBClusterIdentifier = field("DBClusterIdentifier")

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
            "type_defs.DescribeDBClusterAutomatedBackupsMessagePaginateTypeDef"
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
                "type_defs.DescribeDBClusterAutomatedBackupsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterBacktracksMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterBacktracksMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    BacktrackIdentifier = field("BacktrackIdentifier")

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
            "type_defs.DescribeDBClusterBacktracksMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterBacktracksMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterEndpointsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterEndpointsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterEndpointIdentifier = field("DBClusterEndpointIdentifier")

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
            "type_defs.DescribeDBClusterEndpointsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterEndpointsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParameterGroupsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeDBClusterParameterGroupsMessagePaginateTypeDef"
    ) = dataclasses.field()

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")

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
            "type_defs.DescribeDBClusterParameterGroupsMessagePaginateTypeDef"
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
                "type_defs.DescribeDBClusterParameterGroupsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterParametersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterParametersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    Source = field("Source")

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
            "type_defs.DescribeDBClusterParametersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterParametersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbClusterResourceId = field("DbClusterResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClustersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBClustersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    IncludeShared = field("IncludeShared")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClustersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClustersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBEngineVersionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBEngineVersionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBParameterGroupFamily = field("DBParameterGroupFamily")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    DefaultOnly = field("DefaultOnly")
    ListSupportedCharacterSets = field("ListSupportedCharacterSets")
    ListSupportedTimezones = field("ListSupportedTimezones")
    IncludeAll = field("IncludeAll")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBEngineVersionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBEngineVersionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstanceAutomatedBackupsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeDBInstanceAutomatedBackupsMessagePaginateTypeDef"
    ) = dataclasses.field()

    DbiResourceId = field("DbiResourceId")
    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    DBInstanceAutomatedBackupsArn = field("DBInstanceAutomatedBackupsArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBInstanceAutomatedBackupsMessagePaginateTypeDef"
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
                "type_defs.DescribeDBInstanceAutomatedBackupsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

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
            "type_defs.DescribeDBInstancesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBLogFilesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBLogFilesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    FilenameContains = field("FilenameContains")
    FileLastWritten = field("FileLastWritten")
    FileSize = field("FileSize")

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
            "type_defs.DescribeDBLogFilesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBLogFilesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBMajorEngineVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDBMajorEngineVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    MajorEngineVersion = field("MajorEngineVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBMajorEngineVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBMajorEngineVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParameterGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBParameterGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")

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
            "type_defs.DescribeDBParameterGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParameterGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBParametersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBParametersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    Source = field("Source")

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
            "type_defs.DescribeDBParametersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBParametersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxiesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDBProxiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBProxiesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDBProxyEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    DBProxyEndpointName = field("DBProxyEndpointName")

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
            "type_defs.DescribeDBProxyEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyTargetGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDBProxyTargetGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")

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
            "type_defs.DescribeDBProxyTargetGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyTargetGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyTargetsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDBProxyTargetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DBProxyName = field("DBProxyName")
    TargetGroupName = field("TargetGroupName")

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
            "type_defs.DescribeDBProxyTargetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBRecommendationsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBRecommendationsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    LastUpdatedAfter = field("LastUpdatedAfter")
    LastUpdatedBefore = field("LastUpdatedBefore")
    Locale = field("Locale")

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
            "type_defs.DescribeDBRecommendationsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBRecommendationsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSecurityGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBSecurityGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBSecurityGroupName = field("DBSecurityGroupName")

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
            "type_defs.DescribeDBSecurityGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSecurityGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotTenantDatabasesMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeDBSnapshotTenantDatabasesMessagePaginateTypeDef"
    ) = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    DbiResourceId = field("DbiResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotTenantDatabasesMessagePaginateTypeDef"
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
                "type_defs.DescribeDBSnapshotTenantDatabasesMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBSnapshotsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbiResourceId = field("DbiResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSubnetGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDBSubnetGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBSubnetGroupName = field("DBSubnetGroupName")

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
            "type_defs.DescribeDBSubnetGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSubnetGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultClusterParametersMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeEngineDefaultClusterParametersMessagePaginateTypeDef"
    ) = dataclasses.field()

    DBParameterGroupFamily = field("DBParameterGroupFamily")

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
            "type_defs.DescribeEngineDefaultClusterParametersMessagePaginateTypeDef"
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
                "type_defs.DescribeEngineDefaultClusterParametersMessagePaginateTypeDef"
            ]
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

    DBParameterGroupFamily = field("DBParameterGroupFamily")

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
class DescribeEventSubscriptionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

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
            "type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef"]
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
    EventCategories = field("EventCategories")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

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
class DescribeExportTasksMessagePaginate:
    boto3_raw_data: "type_defs.DescribeExportTasksMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ExportTaskIdentifier = field("ExportTaskIdentifier")
    SourceArn = field("SourceArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    SourceType = field("SourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeExportTasksMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportTasksMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalClustersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeGlobalClustersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")

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
            "type_defs.DescribeGlobalClustersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalClustersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIntegrationsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeIntegrationsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    IntegrationIdentifier = field("IntegrationIdentifier")

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
            "type_defs.DescribeIntegrationsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIntegrationsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptionGroupOptionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeOptionGroupOptionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")

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
            "type_defs.DescribeOptionGroupOptionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptionGroupOptionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptionGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeOptionGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    OptionGroupName = field("OptionGroupName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOptionGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptionGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableDBInstanceOptionsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef"
    ) = dataclasses.field()

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DBInstanceClass = field("DBInstanceClass")
    LicenseModel = field("LicenseModel")
    AvailabilityZoneGroup = field("AvailabilityZoneGroup")
    Vpc = field("Vpc")

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
            "type_defs.DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef"
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
                "type_defs.DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingMaintenanceActionsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribePendingMaintenanceActionsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")

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
            "type_defs.DescribePendingMaintenanceActionsMessagePaginateTypeDef"
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
                "type_defs.DescribePendingMaintenanceActionsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedDBInstancesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReservedDBInstancesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReservedDBInstanceId = field("ReservedDBInstanceId")
    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    DBInstanceClass = field("DBInstanceClass")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MultiAZ = field("MultiAZ")
    LeaseId = field("LeaseId")

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
            "type_defs.DescribeReservedDBInstancesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedDBInstancesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedDBInstancesOfferingsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeReservedDBInstancesOfferingsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    DBInstanceClass = field("DBInstanceClass")
    Duration = field("Duration")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MultiAZ = field("MultiAZ")

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
            "type_defs.DescribeReservedDBInstancesOfferingsMessagePaginateTypeDef"
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
                "type_defs.DescribeReservedDBInstancesOfferingsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceRegionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeSourceRegionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")

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
            "type_defs.DescribeSourceRegionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceRegionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTenantDatabasesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeTenantDatabasesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")

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
            "type_defs.DescribeTenantDatabasesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTenantDatabasesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DownloadDBLogFilePortionMessagePaginate:
    boto3_raw_data: "type_defs.DownloadDBLogFilePortionMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    LogFileName = field("LogFileName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DownloadDBLogFilePortionMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DownloadDBLogFilePortionMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotsMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotsMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbClusterResourceId = field("DbClusterResourceId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotsMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotsMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClusterSnapshotsMessageWait:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterSnapshotIdentifier = field("DBClusterSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbClusterResourceId = field("DbClusterResourceId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotsMessageWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClustersMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeDBClustersMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClustersMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClustersMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBClustersMessageWait:
    boto3_raw_data: "type_defs.DescribeDBClustersMessageWaitTypeDef" = (
        dataclasses.field()
    )

    DBClusterIdentifier = field("DBClusterIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBClustersMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClustersMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBInstancesMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBInstancesMessageWait:
    boto3_raw_data: "type_defs.DescribeDBInstancesMessageWaitTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBInstancesMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBInstancesMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotsMessageWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeDBSnapshotsMessageWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbiResourceId = field("DbiResourceId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotsMessageWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotsMessageWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotsMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeDBSnapshotsMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbiResourceId = field("DbiResourceId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotsMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotsMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotsMessageWait:
    boto3_raw_data: "type_defs.DescribeDBSnapshotsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBSnapshotIdentifier = field("DBSnapshotIdentifier")
    SnapshotType = field("SnapshotType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    IncludeShared = field("IncludeShared")
    IncludePublic = field("IncludePublic")
    DbiResourceId = field("DbiResourceId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBSnapshotsMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTenantDatabasesMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeTenantDatabasesMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTenantDatabasesMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTenantDatabasesMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTenantDatabasesMessageWait:
    boto3_raw_data: "type_defs.DescribeTenantDatabasesMessageWaitTypeDef" = (
        dataclasses.field()
    )

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTenantDatabasesMessageWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTenantDatabasesMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBLogFilesResponse:
    boto3_raw_data: "type_defs.DescribeDBLogFilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DescribeDBLogFiles(self):  # pragma: no cover
        return DescribeDBLogFilesDetails.make_many(
            self.boto3_raw_data["DescribeDBLogFiles"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBLogFilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBLogFilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventCategoriesMessage:
    boto3_raw_data: "type_defs.EventCategoriesMessageTypeDef" = dataclasses.field()

    @cached_property
    def EventCategoriesMapList(self):  # pragma: no cover
        return EventCategoriesMap.make_many(
            self.boto3_raw_data["EventCategoriesMapList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventCategoriesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventCategoriesMessageTypeDef"]
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
class ExportTasksMessage:
    boto3_raw_data: "type_defs.ExportTasksMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ExportTasks(self):  # pragma: no cover
        return ExportTask.make_many(self.boto3_raw_data["ExportTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportTasksMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTasksMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalCluster:
    boto3_raw_data: "type_defs.GlobalClusterTypeDef" = dataclasses.field()

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    GlobalClusterResourceId = field("GlobalClusterResourceId")
    GlobalClusterArn = field("GlobalClusterArn")
    Status = field("Status")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    EngineLifecycleSupport = field("EngineLifecycleSupport")
    DatabaseName = field("DatabaseName")
    StorageEncrypted = field("StorageEncrypted")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def GlobalClusterMembers(self):  # pragma: no cover
        return GlobalClusterMember.make_many(
            self.boto3_raw_data["GlobalClusterMembers"]
        )

    Endpoint = field("Endpoint")

    @cached_property
    def FailoverState(self):  # pragma: no cover
        return FailoverState.make_one(self.boto3_raw_data["FailoverState"])

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlobalClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlobalClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationResponse:
    boto3_raw_data: "type_defs.IntegrationResponseTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    TargetArn = field("TargetArn")
    IntegrationName = field("IntegrationName")
    IntegrationArn = field("IntegrationArn")
    KMSKeyId = field("KMSKeyId")
    AdditionalEncryptionContext = field("AdditionalEncryptionContext")
    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreateTime = field("CreateTime")

    @cached_property
    def Errors(self):  # pragma: no cover
        return IntegrationError.make_many(self.boto3_raw_data["Errors"])

    DataFilter = field("DataFilter")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Integration:
    boto3_raw_data: "type_defs.IntegrationTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    TargetArn = field("TargetArn")
    IntegrationName = field("IntegrationName")
    IntegrationArn = field("IntegrationArn")
    KMSKeyId = field("KMSKeyId")
    AdditionalEncryptionContext = field("AdditionalEncryptionContext")
    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreateTime = field("CreateTime")

    @cached_property
    def Errors(self):  # pragma: no cover
        return IntegrationError.make_many(self.boto3_raw_data["Errors"])

    DataFilter = field("DataFilter")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntegrationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionGroupOptionSetting:
    boto3_raw_data: "type_defs.OptionGroupOptionSettingTypeDef" = dataclasses.field()

    SettingName = field("SettingName")
    SettingDescription = field("SettingDescription")
    DefaultValue = field("DefaultValue")
    ApplyType = field("ApplyType")
    AllowedValues = field("AllowedValues")
    IsModifiable = field("IsModifiable")
    IsRequired = field("IsRequired")

    @cached_property
    def MinimumEngineVersionPerAllowedValue(self):  # pragma: no cover
        return MinimumEngineVersionPerAllowedValue.make_many(
            self.boto3_raw_data["MinimumEngineVersionPerAllowedValue"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionGroupOptionSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionGroupOptionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBRecommendationMessage:
    boto3_raw_data: "type_defs.ModifyDBRecommendationMessageTypeDef" = (
        dataclasses.field()
    )

    RecommendationId = field("RecommendationId")
    Locale = field("Locale")
    Status = field("Status")

    @cached_property
    def RecommendedActionUpdates(self):  # pragma: no cover
        return RecommendedActionUpdate.make_many(
            self.boto3_raw_data["RecommendedActionUpdates"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBRecommendationMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBRecommendationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionConfiguration:
    boto3_raw_data: "type_defs.OptionConfigurationTypeDef" = dataclasses.field()

    OptionName = field("OptionName")
    Port = field("Port")
    OptionVersion = field("OptionVersion")
    DBSecurityGroupMemberships = field("DBSecurityGroupMemberships")
    VpcSecurityGroupMemberships = field("VpcSecurityGroupMemberships")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return OptionSetting.make_many(self.boto3_raw_data["OptionSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Option:
    boto3_raw_data: "type_defs.OptionTypeDef" = dataclasses.field()

    OptionName = field("OptionName")
    OptionDescription = field("OptionDescription")
    Persistent = field("Persistent")
    Permanent = field("Permanent")
    Port = field("Port")
    OptionVersion = field("OptionVersion")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return OptionSetting.make_many(self.boto3_raw_data["OptionSettings"])

    @cached_property
    def DBSecurityGroupMemberships(self):  # pragma: no cover
        return DBSecurityGroupMembership.make_many(
            self.boto3_raw_data["DBSecurityGroupMemberships"]
        )

    @cached_property
    def VpcSecurityGroupMemberships(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroupMemberships"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionTypeDef"]]
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
        return Outpost.make_one(self.boto3_raw_data["SubnetOutpost"])

    SubnetStatus = field("SubnetStatus")

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
class ResourcePendingMaintenanceActions:
    boto3_raw_data: "type_defs.ResourcePendingMaintenanceActionsTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def PendingMaintenanceActionDetails(self):  # pragma: no cover
        return PendingMaintenanceAction.make_many(
            self.boto3_raw_data["PendingMaintenanceActionDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourcePendingMaintenanceActionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourcePendingMaintenanceActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceInsightsMetricQuery:
    boto3_raw_data: "type_defs.PerformanceInsightsMetricQueryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GroupBy(self):  # pragma: no cover
        return PerformanceInsightsMetricDimensionGroup.make_one(
            self.boto3_raw_data["GroupBy"]
        )

    Metric = field("Metric")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PerformanceInsightsMetricQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceInsightsMetricQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidStorageOptions:
    boto3_raw_data: "type_defs.ValidStorageOptionsTypeDef" = dataclasses.field()

    StorageType = field("StorageType")

    @cached_property
    def StorageSize(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["StorageSize"])

    @cached_property
    def ProvisionedIops(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["ProvisionedIops"])

    @cached_property
    def IopsToStorageRatio(self):  # pragma: no cover
        return DoubleRange.make_many(self.boto3_raw_data["IopsToStorageRatio"])

    SupportsStorageAutoscaling = field("SupportsStorageAutoscaling")

    @cached_property
    def ProvisionedStorageThroughput(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["ProvisionedStorageThroughput"])

    @cached_property
    def StorageThroughputToIopsRatio(self):  # pragma: no cover
        return DoubleRange.make_many(
            self.boto3_raw_data["StorageThroughputToIopsRatio"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidStorageOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidStorageOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedDBInstance:
    boto3_raw_data: "type_defs.ReservedDBInstanceTypeDef" = dataclasses.field()

    ReservedDBInstanceId = field("ReservedDBInstanceId")
    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    DBInstanceClass = field("DBInstanceClass")
    StartTime = field("StartTime")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    DBInstanceCount = field("DBInstanceCount")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MultiAZ = field("MultiAZ")
    State = field("State")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    ReservedDBInstanceArn = field("ReservedDBInstanceArn")
    LeaseId = field("LeaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedDBInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedDBInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedDBInstancesOffering:
    boto3_raw_data: "type_defs.ReservedDBInstancesOfferingTypeDef" = dataclasses.field()

    ReservedDBInstancesOfferingId = field("ReservedDBInstancesOfferingId")
    DBInstanceClass = field("DBInstanceClass")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    ProductDescription = field("ProductDescription")
    OfferingType = field("OfferingType")
    MultiAZ = field("MultiAZ")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedDBInstancesOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedDBInstancesOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceDetails:
    boto3_raw_data: "type_defs.ReferenceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ScalarReferenceDetails(self):  # pragma: no cover
        return ScalarReferenceDetails.make_one(
            self.boto3_raw_data["ScalarReferenceDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceRegionMessage:
    boto3_raw_data: "type_defs.SourceRegionMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def SourceRegions(self):  # pragma: no cover
        return SourceRegion.make_many(self.boto3_raw_data["SourceRegions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceRegionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceRegionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantDatabase:
    boto3_raw_data: "type_defs.TenantDatabaseTypeDef" = dataclasses.field()

    TenantDatabaseCreateTime = field("TenantDatabaseCreateTime")
    DBInstanceIdentifier = field("DBInstanceIdentifier")
    TenantDBName = field("TenantDBName")
    Status = field("Status")
    MasterUsername = field("MasterUsername")
    DbiResourceId = field("DbiResourceId")
    TenantDatabaseResourceId = field("TenantDatabaseResourceId")
    TenantDatabaseARN = field("TenantDatabaseARN")
    CharacterSetName = field("CharacterSetName")
    NcharCharacterSetName = field("NcharCharacterSetName")
    DeletionProtection = field("DeletionProtection")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return TenantDatabasePendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    @cached_property
    def MasterUserSecret(self):  # pragma: no cover
        return MasterUserSecret.make_one(self.boto3_raw_data["MasterUserSecret"])

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TenantDatabaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TenantDatabaseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBClusterSnapshotResult:
    boto3_raw_data: "type_defs.CopyDBClusterSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def DBClusterSnapshot(self):  # pragma: no cover
        return DBClusterSnapshot.make_one(self.boto3_raw_data["DBClusterSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBClusterSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterSnapshotResult:
    boto3_raw_data: "type_defs.CreateDBClusterSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshot(self):  # pragma: no cover
        return DBClusterSnapshot.make_one(self.boto3_raw_data["DBClusterSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDBClusterSnapshotResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterSnapshotMessage:
    boto3_raw_data: "type_defs.DBClusterSnapshotMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusterSnapshots(self):  # pragma: no cover
        return DBClusterSnapshot.make_many(self.boto3_raw_data["DBClusterSnapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterSnapshotResult:
    boto3_raw_data: "type_defs.DeleteDBClusterSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshot(self):  # pragma: no cover
        return DBClusterSnapshot.make_one(self.boto3_raw_data["DBClusterSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDBClusterSnapshotResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBShardGroupsResponse:
    boto3_raw_data: "type_defs.DescribeDBShardGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBShardGroups(self):  # pragma: no cover
        return DBShardGroup.make_many(self.boto3_raw_data["DBShardGroups"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBShardGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBShardGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSnapshotTenantDatabasesMessage:
    boto3_raw_data: "type_defs.DBSnapshotTenantDatabasesMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def DBSnapshotTenantDatabases(self):  # pragma: no cover
        return DBSnapshotTenantDatabase.make_many(
            self.boto3_raw_data["DBSnapshotTenantDatabases"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBSnapshotTenantDatabasesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSnapshotTenantDatabasesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderableDBInstanceOptionsMessage:
    boto3_raw_data: "type_defs.OrderableDBInstanceOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrderableDBInstanceOptions(self):  # pragma: no cover
        return OrderableDBInstanceOption.make_many(
            self.boto3_raw_data["OrderableDBInstanceOptions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrderableDBInstanceOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableDBInstanceOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBlueGreenDeploymentResponse:
    boto3_raw_data: "type_defs.CreateBlueGreenDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlueGreenDeployment(self):  # pragma: no cover
        return BlueGreenDeployment.make_one(self.boto3_raw_data["BlueGreenDeployment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBlueGreenDeploymentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBlueGreenDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBlueGreenDeploymentResponse:
    boto3_raw_data: "type_defs.DeleteBlueGreenDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlueGreenDeployment(self):  # pragma: no cover
        return BlueGreenDeployment.make_one(self.boto3_raw_data["BlueGreenDeployment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBlueGreenDeploymentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBlueGreenDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBlueGreenDeploymentsResponse:
    boto3_raw_data: "type_defs.DescribeBlueGreenDeploymentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlueGreenDeployments(self):  # pragma: no cover
        return BlueGreenDeployment.make_many(
            self.boto3_raw_data["BlueGreenDeployments"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBlueGreenDeploymentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBlueGreenDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverBlueGreenDeploymentResponse:
    boto3_raw_data: "type_defs.SwitchoverBlueGreenDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BlueGreenDeployment(self):  # pragma: no cover
        return BlueGreenDeployment.make_one(self.boto3_raw_data["BlueGreenDeployment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SwitchoverBlueGreenDeploymentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverBlueGreenDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBCluster:
    boto3_raw_data: "type_defs.DBClusterTypeDef" = dataclasses.field()

    AllocatedStorage = field("AllocatedStorage")
    AvailabilityZones = field("AvailabilityZones")
    BackupRetentionPeriod = field("BackupRetentionPeriod")
    CharacterSetName = field("CharacterSetName")
    DatabaseName = field("DatabaseName")
    DBClusterIdentifier = field("DBClusterIdentifier")
    DBClusterParameterGroup = field("DBClusterParameterGroup")
    DBSubnetGroup = field("DBSubnetGroup")
    Status = field("Status")
    AutomaticRestartTime = field("AutomaticRestartTime")
    PercentProgress = field("PercentProgress")
    EarliestRestorableTime = field("EarliestRestorableTime")
    Endpoint = field("Endpoint")
    ReaderEndpoint = field("ReaderEndpoint")
    CustomEndpoints = field("CustomEndpoints")
    MultiAZ = field("MultiAZ")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    LatestRestorableTime = field("LatestRestorableTime")
    Port = field("Port")
    MasterUsername = field("MasterUsername")

    @cached_property
    def DBClusterOptionGroupMemberships(self):  # pragma: no cover
        return DBClusterOptionGroupStatus.make_many(
            self.boto3_raw_data["DBClusterOptionGroupMemberships"]
        )

    PreferredBackupWindow = field("PreferredBackupWindow")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ReplicationSourceIdentifier = field("ReplicationSourceIdentifier")
    ReadReplicaIdentifiers = field("ReadReplicaIdentifiers")

    @cached_property
    def StatusInfos(self):  # pragma: no cover
        return DBClusterStatusInfo.make_many(self.boto3_raw_data["StatusInfos"])

    @cached_property
    def DBClusterMembers(self):  # pragma: no cover
        return DBClusterMember.make_many(self.boto3_raw_data["DBClusterMembers"])

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    HostedZoneId = field("HostedZoneId")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    DbClusterResourceId = field("DbClusterResourceId")
    DBClusterArn = field("DBClusterArn")

    @cached_property
    def AssociatedRoles(self):  # pragma: no cover
        return DBClusterRole.make_many(self.boto3_raw_data["AssociatedRoles"])

    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    CloneGroupId = field("CloneGroupId")
    ClusterCreateTime = field("ClusterCreateTime")
    EarliestBacktrackTime = field("EarliestBacktrackTime")
    BacktrackWindow = field("BacktrackWindow")
    BacktrackConsumedChangeRecords = field("BacktrackConsumedChangeRecords")
    EnabledCloudwatchLogsExports = field("EnabledCloudwatchLogsExports")
    Capacity = field("Capacity")
    EngineMode = field("EngineMode")

    @cached_property
    def ScalingConfigurationInfo(self):  # pragma: no cover
        return ScalingConfigurationInfo.make_one(
            self.boto3_raw_data["ScalingConfigurationInfo"]
        )

    @cached_property
    def RdsCustomClusterConfiguration(self):  # pragma: no cover
        return RdsCustomClusterConfiguration.make_one(
            self.boto3_raw_data["RdsCustomClusterConfiguration"]
        )

    DeletionProtection = field("DeletionProtection")
    HttpEndpointEnabled = field("HttpEndpointEnabled")
    ActivityStreamMode = field("ActivityStreamMode")
    ActivityStreamStatus = field("ActivityStreamStatus")
    ActivityStreamKmsKeyId = field("ActivityStreamKmsKeyId")
    ActivityStreamKinesisStreamName = field("ActivityStreamKinesisStreamName")
    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    CrossAccountClone = field("CrossAccountClone")

    @cached_property
    def DomainMemberships(self):  # pragma: no cover
        return DomainMembership.make_many(self.boto3_raw_data["DomainMemberships"])

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    GlobalClusterIdentifier = field("GlobalClusterIdentifier")
    GlobalWriteForwardingStatus = field("GlobalWriteForwardingStatus")
    GlobalWriteForwardingRequested = field("GlobalWriteForwardingRequested")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return ClusterPendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    DBClusterInstanceClass = field("DBClusterInstanceClass")
    StorageType = field("StorageType")
    Iops = field("Iops")
    PubliclyAccessible = field("PubliclyAccessible")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    MonitoringInterval = field("MonitoringInterval")
    MonitoringRoleArn = field("MonitoringRoleArn")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    PerformanceInsightsEnabled = field("PerformanceInsightsEnabled")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")

    @cached_property
    def ServerlessV2ScalingConfiguration(self):  # pragma: no cover
        return ServerlessV2ScalingConfigurationInfo.make_one(
            self.boto3_raw_data["ServerlessV2ScalingConfiguration"]
        )

    ServerlessV2PlatformVersion = field("ServerlessV2PlatformVersion")
    NetworkType = field("NetworkType")
    DBSystemId = field("DBSystemId")

    @cached_property
    def MasterUserSecret(self):  # pragma: no cover
        return MasterUserSecret.make_one(self.boto3_raw_data["MasterUserSecret"])

    IOOptimizedNextAllowedModificationTime = field(
        "IOOptimizedNextAllowedModificationTime"
    )
    LocalWriteForwardingStatus = field("LocalWriteForwardingStatus")
    AwsBackupRecoveryPointArn = field("AwsBackupRecoveryPointArn")

    @cached_property
    def LimitlessDatabase(self):  # pragma: no cover
        return LimitlessDatabase.make_one(self.boto3_raw_data["LimitlessDatabase"])

    StorageThroughput = field("StorageThroughput")
    ClusterScalabilityType = field("ClusterScalabilityType")

    @cached_property
    def CertificateDetails(self):  # pragma: no cover
        return CertificateDetails.make_one(self.boto3_raw_data["CertificateDetails"])

    EngineLifecycleSupport = field("EngineLifecycleSupport")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyTargetGroupsResponse:
    boto3_raw_data: "type_defs.DescribeDBProxyTargetGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TargetGroups(self):  # pragma: no cover
        return DBProxyTargetGroup.make_many(self.boto3_raw_data["TargetGroups"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBProxyTargetGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyTargetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBProxyTargetGroupResponse:
    boto3_raw_data: "type_defs.ModifyDBProxyTargetGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBProxyTargetGroup(self):  # pragma: no cover
        return DBProxyTargetGroup.make_one(self.boto3_raw_data["DBProxyTargetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBProxyTargetGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBProxyTargetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyDBSnapshotResult:
    boto3_raw_data: "type_defs.CopyDBSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSnapshot(self):  # pragma: no cover
        return DBSnapshot.make_one(self.boto3_raw_data["DBSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyDBSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyDBSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSnapshotResult:
    boto3_raw_data: "type_defs.CreateDBSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSnapshot(self):  # pragma: no cover
        return DBSnapshot.make_one(self.boto3_raw_data["DBSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSnapshotMessage:
    boto3_raw_data: "type_defs.DBSnapshotMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBSnapshots(self):  # pragma: no cover
        return DBSnapshot.make_many(self.boto3_raw_data["DBSnapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBSnapshotMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBSnapshotResult:
    boto3_raw_data: "type_defs.DeleteDBSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSnapshot(self):  # pragma: no cover
        return DBSnapshot.make_one(self.boto3_raw_data["DBSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSnapshotResult:
    boto3_raw_data: "type_defs.ModifyDBSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSnapshot(self):  # pragma: no cover
        return DBSnapshot.make_one(self.boto3_raw_data["DBSnapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterAutomatedBackupMessage:
    boto3_raw_data: "type_defs.DBClusterAutomatedBackupMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def DBClusterAutomatedBackups(self):  # pragma: no cover
        return DBClusterAutomatedBackup.make_many(
            self.boto3_raw_data["DBClusterAutomatedBackups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBClusterAutomatedBackupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterAutomatedBackupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterAutomatedBackupResult:
    boto3_raw_data: "type_defs.DeleteDBClusterAutomatedBackupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterAutomatedBackup(self):  # pragma: no cover
        return DBClusterAutomatedBackup.make_one(
            self.boto3_raw_data["DBClusterAutomatedBackup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDBClusterAutomatedBackupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterAutomatedBackupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineDefaultClusterParametersResult:
    boto3_raw_data: "type_defs.DescribeEngineDefaultClusterParametersResultTypeDef" = (
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
            "type_defs.DescribeEngineDefaultClusterParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineDefaultClusterParametersResultTypeDef"]
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
class DescribeDBClusterSnapshotAttributesResult:
    boto3_raw_data: "type_defs.DescribeDBClusterSnapshotAttributesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshotAttributesResult(self):  # pragma: no cover
        return DBClusterSnapshotAttributesResult.make_one(
            self.boto3_raw_data["DBClusterSnapshotAttributesResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBClusterSnapshotAttributesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBClusterSnapshotAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterSnapshotAttributeResult:
    boto3_raw_data: "type_defs.ModifyDBClusterSnapshotAttributeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBClusterSnapshotAttributesResult(self):  # pragma: no cover
        return DBClusterSnapshotAttributesResult.make_one(
            self.boto3_raw_data["DBClusterSnapshotAttributesResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyDBClusterSnapshotAttributeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterSnapshotAttributeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBEngineVersionMessage:
    boto3_raw_data: "type_defs.DBEngineVersionMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBEngineVersions(self):  # pragma: no cover
        return DBEngineVersion.make_many(self.boto3_raw_data["DBEngineVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBEngineVersionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBEngineVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceAutomatedBackupMessage:
    boto3_raw_data: "type_defs.DBInstanceAutomatedBackupMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def DBInstanceAutomatedBackups(self):  # pragma: no cover
        return DBInstanceAutomatedBackup.make_many(
            self.boto3_raw_data["DBInstanceAutomatedBackups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DBInstanceAutomatedBackupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceAutomatedBackupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBInstanceAutomatedBackupResult:
    boto3_raw_data: "type_defs.DeleteDBInstanceAutomatedBackupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBInstanceAutomatedBackup(self):  # pragma: no cover
        return DBInstanceAutomatedBackup.make_one(
            self.boto3_raw_data["DBInstanceAutomatedBackup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDBInstanceAutomatedBackupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBInstanceAutomatedBackupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBInstanceAutomatedBackupsReplicationResult:
    boto3_raw_data: (
        "type_defs.StartDBInstanceAutomatedBackupsReplicationResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def DBInstanceAutomatedBackup(self):  # pragma: no cover
        return DBInstanceAutomatedBackup.make_one(
            self.boto3_raw_data["DBInstanceAutomatedBackup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDBInstanceAutomatedBackupsReplicationResultTypeDef"
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
                "type_defs.StartDBInstanceAutomatedBackupsReplicationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBInstanceAutomatedBackupsReplicationResult:
    boto3_raw_data: (
        "type_defs.StopDBInstanceAutomatedBackupsReplicationResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def DBInstanceAutomatedBackup(self):  # pragma: no cover
        return DBInstanceAutomatedBackup.make_one(
            self.boto3_raw_data["DBInstanceAutomatedBackup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopDBInstanceAutomatedBackupsReplicationResultTypeDef"
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
                "type_defs.StopDBInstanceAutomatedBackupsReplicationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBMajorEngineVersionsResponse:
    boto3_raw_data: "type_defs.DescribeDBMajorEngineVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBMajorEngineVersions(self):  # pragma: no cover
        return DBMajorEngineVersion.make_many(
            self.boto3_raw_data["DBMajorEngineVersions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBMajorEngineVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBMajorEngineVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxyTargetsResponse:
    boto3_raw_data: "type_defs.DescribeDBProxyTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Targets(self):  # pragma: no cover
        return DBProxyTarget.make_many(self.boto3_raw_data["Targets"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDBProxyTargetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxyTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDBProxyTargetsResponse:
    boto3_raw_data: "type_defs.RegisterDBProxyTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBProxyTargets(self):  # pragma: no cover
        return DBProxyTarget.make_many(self.boto3_raw_data["DBProxyTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterDBProxyTargetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDBProxyTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBProxyResponse:
    boto3_raw_data: "type_defs.CreateDBProxyResponseTypeDef" = dataclasses.field()

    @cached_property
    def DBProxy(self):  # pragma: no cover
        return DBProxy.make_one(self.boto3_raw_data["DBProxy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBProxyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBProxyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBProxyResponse:
    boto3_raw_data: "type_defs.DeleteDBProxyResponseTypeDef" = dataclasses.field()

    @cached_property
    def DBProxy(self):  # pragma: no cover
        return DBProxy.make_one(self.boto3_raw_data["DBProxy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBProxyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBProxyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBProxiesResponse:
    boto3_raw_data: "type_defs.DescribeDBProxiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DBProxies(self):  # pragma: no cover
        return DBProxy.make_many(self.boto3_raw_data["DBProxies"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDBProxiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBProxiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBProxyResponse:
    boto3_raw_data: "type_defs.ModifyDBProxyResponseTypeDef" = dataclasses.field()

    @cached_property
    def DBProxy(self):  # pragma: no cover
        return DBProxy.make_one(self.boto3_raw_data["DBProxy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBProxyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBProxyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeDBSecurityGroupIngressResult:
    boto3_raw_data: "type_defs.AuthorizeDBSecurityGroupIngressResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBSecurityGroup(self):  # pragma: no cover
        return DBSecurityGroup.make_one(self.boto3_raw_data["DBSecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeDBSecurityGroupIngressResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeDBSecurityGroupIngressResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSecurityGroupResult:
    boto3_raw_data: "type_defs.CreateDBSecurityGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSecurityGroup(self):  # pragma: no cover
        return DBSecurityGroup.make_one(self.boto3_raw_data["DBSecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSecurityGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSecurityGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSecurityGroupMessage:
    boto3_raw_data: "type_defs.DBSecurityGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBSecurityGroups(self):  # pragma: no cover
        return DBSecurityGroup.make_many(self.boto3_raw_data["DBSecurityGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSecurityGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeDBSecurityGroupIngressResult:
    boto3_raw_data: "type_defs.RevokeDBSecurityGroupIngressResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBSecurityGroup(self):  # pragma: no cover
        return DBSecurityGroup.make_one(self.boto3_raw_data["DBSecurityGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeDBSecurityGroupIngressResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeDBSecurityGroupIngressResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDBSnapshotAttributesResult:
    boto3_raw_data: "type_defs.DescribeDBSnapshotAttributesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBSnapshotAttributesResult(self):  # pragma: no cover
        return DBSnapshotAttributesResult.make_one(
            self.boto3_raw_data["DBSnapshotAttributesResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDBSnapshotAttributesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDBSnapshotAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSnapshotAttributeResult:
    boto3_raw_data: "type_defs.ModifyDBSnapshotAttributeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBSnapshotAttributesResult(self):  # pragma: no cover
        return DBSnapshotAttributesResult.make_one(
            self.boto3_raw_data["DBSnapshotAttributesResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBSnapshotAttributeResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSnapshotAttributeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalClusterResult:
    boto3_raw_data: "type_defs.CreateGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalClusterResult:
    boto3_raw_data: "type_defs.DeleteGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverGlobalClusterResult:
    boto3_raw_data: "type_defs.FailoverGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalClustersMessage:
    boto3_raw_data: "type_defs.GlobalClustersMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def GlobalClusters(self):  # pragma: no cover
        return GlobalCluster.make_many(self.boto3_raw_data["GlobalClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalClustersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyGlobalClusterResult:
    boto3_raw_data: "type_defs.ModifyGlobalClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyGlobalClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFromGlobalClusterResult:
    boto3_raw_data: "type_defs.RemoveFromGlobalClusterResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveFromGlobalClusterResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFromGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverGlobalClusterResult:
    boto3_raw_data: "type_defs.SwitchoverGlobalClusterResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GlobalCluster(self):  # pragma: no cover
        return GlobalCluster.make_one(self.boto3_raw_data["GlobalCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SwitchoverGlobalClusterResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverGlobalClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIntegrationsResponse:
    boto3_raw_data: "type_defs.DescribeIntegrationsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Integrations(self):  # pragma: no cover
        return Integration.make_many(self.boto3_raw_data["Integrations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIntegrationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionGroupOption:
    boto3_raw_data: "type_defs.OptionGroupOptionTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")
    MinimumRequiredMinorEngineVersion = field("MinimumRequiredMinorEngineVersion")
    PortRequired = field("PortRequired")
    DefaultPort = field("DefaultPort")
    OptionsDependedOn = field("OptionsDependedOn")
    OptionsConflictsWith = field("OptionsConflictsWith")
    Persistent = field("Persistent")
    Permanent = field("Permanent")
    RequiresAutoMinorEngineVersionUpgrade = field(
        "RequiresAutoMinorEngineVersionUpgrade"
    )
    VpcOnly = field("VpcOnly")
    SupportsOptionVersionDowngrade = field("SupportsOptionVersionDowngrade")

    @cached_property
    def OptionGroupOptionSettings(self):  # pragma: no cover
        return OptionGroupOptionSetting.make_many(
            self.boto3_raw_data["OptionGroupOptionSettings"]
        )

    @cached_property
    def OptionGroupOptionVersions(self):  # pragma: no cover
        return OptionVersion.make_many(self.boto3_raw_data["OptionGroupOptionVersions"])

    CopyableCrossAccount = field("CopyableCrossAccount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionGroupOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionGroupOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyOptionGroupMessage:
    boto3_raw_data: "type_defs.ModifyOptionGroupMessageTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")

    @cached_property
    def OptionsToInclude(self):  # pragma: no cover
        return OptionConfiguration.make_many(self.boto3_raw_data["OptionsToInclude"])

    OptionsToRemove = field("OptionsToRemove")
    ApplyImmediately = field("ApplyImmediately")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyOptionGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyOptionGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionGroup:
    boto3_raw_data: "type_defs.OptionGroupTypeDef" = dataclasses.field()

    OptionGroupName = field("OptionGroupName")
    OptionGroupDescription = field("OptionGroupDescription")
    EngineName = field("EngineName")
    MajorEngineVersion = field("MajorEngineVersion")

    @cached_property
    def Options(self):  # pragma: no cover
        return Option.make_many(self.boto3_raw_data["Options"])

    AllowsVpcAndNonVpcInstanceMemberships = field(
        "AllowsVpcAndNonVpcInstanceMemberships"
    )
    VpcId = field("VpcId")
    OptionGroupArn = field("OptionGroupArn")
    SourceOptionGroup = field("SourceOptionGroup")
    SourceAccountId = field("SourceAccountId")
    CopyTimestamp = field("CopyTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSubnetGroup:
    boto3_raw_data: "type_defs.DBSubnetGroupTypeDef" = dataclasses.field()

    DBSubnetGroupName = field("DBSubnetGroupName")
    DBSubnetGroupDescription = field("DBSubnetGroupDescription")
    VpcId = field("VpcId")
    SubnetGroupStatus = field("SubnetGroupStatus")

    @cached_property
    def Subnets(self):  # pragma: no cover
        return Subnet.make_many(self.boto3_raw_data["Subnets"])

    DBSubnetGroupArn = field("DBSubnetGroupArn")
    SupportedNetworkTypes = field("SupportedNetworkTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBSubnetGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBSubnetGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBParameterGroupMessage:
    boto3_raw_data: "type_defs.ModifyDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDBParameterGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetDBClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.ResetDBClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBClusterParameterGroupName = field("DBClusterParameterGroupName")
    ResetAllParameters = field("ResetAllParameters")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetDBClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDBClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetDBParameterGroupMessage:
    boto3_raw_data: "type_defs.ResetDBParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    DBParameterGroupName = field("DBParameterGroupName")
    ResetAllParameters = field("ResetAllParameters")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetDBParameterGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetDBParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyPendingMaintenanceActionResult:
    boto3_raw_data: "type_defs.ApplyPendingMaintenanceActionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourcePendingMaintenanceActions(self):  # pragma: no cover
        return ResourcePendingMaintenanceActions.make_one(
            self.boto3_raw_data["ResourcePendingMaintenanceActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyPendingMaintenanceActionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyPendingMaintenanceActionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingMaintenanceActionsMessage:
    boto3_raw_data: "type_defs.PendingMaintenanceActionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PendingMaintenanceActions(self):  # pragma: no cover
        return ResourcePendingMaintenanceActions.make_many(
            self.boto3_raw_data["PendingMaintenanceActions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PendingMaintenanceActionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricQuery:
    boto3_raw_data: "type_defs.MetricQueryTypeDef" = dataclasses.field()

    @cached_property
    def PerformanceInsightsMetricQuery(self):  # pragma: no cover
        return PerformanceInsightsMetricQuery.make_one(
            self.boto3_raw_data["PerformanceInsightsMetricQuery"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricQueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidDBInstanceModificationsMessage:
    boto3_raw_data: "type_defs.ValidDBInstanceModificationsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Storage(self):  # pragma: no cover
        return ValidStorageOptions.make_many(self.boto3_raw_data["Storage"])

    @cached_property
    def ValidProcessorFeatures(self):  # pragma: no cover
        return AvailableProcessorFeature.make_many(
            self.boto3_raw_data["ValidProcessorFeatures"]
        )

    SupportsDedicatedLogVolume = field("SupportsDedicatedLogVolume")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidDBInstanceModificationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidDBInstanceModificationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedDBInstancesOfferingResult:
    boto3_raw_data: "type_defs.PurchaseReservedDBInstancesOfferingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedDBInstance(self):  # pragma: no cover
        return ReservedDBInstance.make_one(self.boto3_raw_data["ReservedDBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedDBInstancesOfferingResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedDBInstancesOfferingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedDBInstanceMessage:
    boto3_raw_data: "type_defs.ReservedDBInstanceMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ReservedDBInstances(self):  # pragma: no cover
        return ReservedDBInstance.make_many(self.boto3_raw_data["ReservedDBInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedDBInstanceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedDBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedDBInstancesOfferingMessage:
    boto3_raw_data: "type_defs.ReservedDBInstancesOfferingMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReservedDBInstancesOfferings(self):  # pragma: no cover
        return ReservedDBInstancesOffering.make_many(
            self.boto3_raw_data["ReservedDBInstancesOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservedDBInstancesOfferingMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedDBInstancesOfferingMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricReference:
    boto3_raw_data: "type_defs.MetricReferenceTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ReferenceDetails(self):  # pragma: no cover
        return ReferenceDetails.make_one(self.boto3_raw_data["ReferenceDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTenantDatabaseResult:
    boto3_raw_data: "type_defs.CreateTenantDatabaseResultTypeDef" = dataclasses.field()

    @cached_property
    def TenantDatabase(self):  # pragma: no cover
        return TenantDatabase.make_one(self.boto3_raw_data["TenantDatabase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTenantDatabaseResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTenantDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTenantDatabaseResult:
    boto3_raw_data: "type_defs.DeleteTenantDatabaseResultTypeDef" = dataclasses.field()

    @cached_property
    def TenantDatabase(self):  # pragma: no cover
        return TenantDatabase.make_one(self.boto3_raw_data["TenantDatabase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTenantDatabaseResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTenantDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTenantDatabaseResult:
    boto3_raw_data: "type_defs.ModifyTenantDatabaseResultTypeDef" = dataclasses.field()

    @cached_property
    def TenantDatabase(self):  # pragma: no cover
        return TenantDatabase.make_one(self.boto3_raw_data["TenantDatabase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyTenantDatabaseResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTenantDatabaseResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TenantDatabasesMessage:
    boto3_raw_data: "type_defs.TenantDatabasesMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def TenantDatabases(self):  # pragma: no cover
        return TenantDatabase.make_many(self.boto3_raw_data["TenantDatabases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TenantDatabasesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TenantDatabasesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBClusterResult:
    boto3_raw_data: "type_defs.CreateDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBClusterMessage:
    boto3_raw_data: "type_defs.DBClusterMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBClusters(self):  # pragma: no cover
        return DBCluster.make_many(self.boto3_raw_data["DBClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBClusterMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBClusterResult:
    boto3_raw_data: "type_defs.DeleteDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverDBClusterResult:
    boto3_raw_data: "type_defs.FailoverDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBClusterResult:
    boto3_raw_data: "type_defs.ModifyDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteReadReplicaDBClusterResult:
    boto3_raw_data: "type_defs.PromoteReadReplicaDBClusterResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromoteReadReplicaDBClusterResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromoteReadReplicaDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBClusterResult:
    boto3_raw_data: "type_defs.RebootDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterFromS3Result:
    boto3_raw_data: "type_defs.RestoreDBClusterFromS3ResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreDBClusterFromS3ResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterFromS3ResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterFromSnapshotResult:
    boto3_raw_data: "type_defs.RestoreDBClusterFromSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterFromSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterFromSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBClusterToPointInTimeResult:
    boto3_raw_data: "type_defs.RestoreDBClusterToPointInTimeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBClusterToPointInTimeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBClusterToPointInTimeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBClusterResult:
    boto3_raw_data: "type_defs.StartDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBClusterResult:
    boto3_raw_data: "type_defs.StopDBClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def DBCluster(self):  # pragma: no cover
        return DBCluster.make_one(self.boto3_raw_data["DBCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDBClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDBClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionGroupOptionsMessage:
    boto3_raw_data: "type_defs.OptionGroupOptionsMessageTypeDef" = dataclasses.field()

    @cached_property
    def OptionGroupOptions(self):  # pragma: no cover
        return OptionGroupOption.make_many(self.boto3_raw_data["OptionGroupOptions"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionGroupOptionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionGroupOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyOptionGroupResult:
    boto3_raw_data: "type_defs.CopyOptionGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def OptionGroup(self):  # pragma: no cover
        return OptionGroup.make_one(self.boto3_raw_data["OptionGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyOptionGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyOptionGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOptionGroupResult:
    boto3_raw_data: "type_defs.CreateOptionGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def OptionGroup(self):  # pragma: no cover
        return OptionGroup.make_one(self.boto3_raw_data["OptionGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOptionGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOptionGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyOptionGroupResult:
    boto3_raw_data: "type_defs.ModifyOptionGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def OptionGroup(self):  # pragma: no cover
        return OptionGroup.make_one(self.boto3_raw_data["OptionGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyOptionGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyOptionGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionGroups:
    boto3_raw_data: "type_defs.OptionGroupsTypeDef" = dataclasses.field()

    @cached_property
    def OptionGroupsList(self):  # pragma: no cover
        return OptionGroup.make_many(self.boto3_raw_data["OptionGroupsList"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionGroupsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionGroupsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBSubnetGroupResult:
    boto3_raw_data: "type_defs.CreateDBSubnetGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSubnetGroup(self):  # pragma: no cover
        return DBSubnetGroup.make_one(self.boto3_raw_data["DBSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBSubnetGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstance:
    boto3_raw_data: "type_defs.DBInstanceTypeDef" = dataclasses.field()

    DBInstanceIdentifier = field("DBInstanceIdentifier")
    DBInstanceClass = field("DBInstanceClass")
    Engine = field("Engine")
    DBInstanceStatus = field("DBInstanceStatus")
    AutomaticRestartTime = field("AutomaticRestartTime")
    MasterUsername = field("MasterUsername")
    DBName = field("DBName")

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    AllocatedStorage = field("AllocatedStorage")
    InstanceCreateTime = field("InstanceCreateTime")
    PreferredBackupWindow = field("PreferredBackupWindow")
    BackupRetentionPeriod = field("BackupRetentionPeriod")

    @cached_property
    def DBSecurityGroups(self):  # pragma: no cover
        return DBSecurityGroupMembership.make_many(
            self.boto3_raw_data["DBSecurityGroups"]
        )

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    @cached_property
    def DBParameterGroups(self):  # pragma: no cover
        return DBParameterGroupStatus.make_many(
            self.boto3_raw_data["DBParameterGroups"]
        )

    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def DBSubnetGroup(self):  # pragma: no cover
        return DBSubnetGroup.make_one(self.boto3_raw_data["DBSubnetGroup"])

    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return PendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    LatestRestorableTime = field("LatestRestorableTime")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    ReadReplicaSourceDBInstanceIdentifier = field(
        "ReadReplicaSourceDBInstanceIdentifier"
    )
    ReadReplicaDBInstanceIdentifiers = field("ReadReplicaDBInstanceIdentifiers")
    ReadReplicaDBClusterIdentifiers = field("ReadReplicaDBClusterIdentifiers")
    ReplicaMode = field("ReplicaMode")
    LicenseModel = field("LicenseModel")
    Iops = field("Iops")

    @cached_property
    def OptionGroupMemberships(self):  # pragma: no cover
        return OptionGroupMembership.make_many(
            self.boto3_raw_data["OptionGroupMemberships"]
        )

    CharacterSetName = field("CharacterSetName")
    NcharCharacterSetName = field("NcharCharacterSetName")
    SecondaryAvailabilityZone = field("SecondaryAvailabilityZone")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def StatusInfos(self):  # pragma: no cover
        return DBInstanceStatusInfo.make_many(self.boto3_raw_data["StatusInfos"])

    StorageType = field("StorageType")
    TdeCredentialArn = field("TdeCredentialArn")
    DbInstancePort = field("DbInstancePort")
    DBClusterIdentifier = field("DBClusterIdentifier")
    StorageEncrypted = field("StorageEncrypted")
    KmsKeyId = field("KmsKeyId")
    DbiResourceId = field("DbiResourceId")
    CACertificateIdentifier = field("CACertificateIdentifier")

    @cached_property
    def DomainMemberships(self):  # pragma: no cover
        return DomainMembership.make_many(self.boto3_raw_data["DomainMemberships"])

    CopyTagsToSnapshot = field("CopyTagsToSnapshot")
    MonitoringInterval = field("MonitoringInterval")
    EnhancedMonitoringResourceArn = field("EnhancedMonitoringResourceArn")
    MonitoringRoleArn = field("MonitoringRoleArn")
    PromotionTier = field("PromotionTier")
    DBInstanceArn = field("DBInstanceArn")
    Timezone = field("Timezone")
    IAMDatabaseAuthenticationEnabled = field("IAMDatabaseAuthenticationEnabled")
    DatabaseInsightsMode = field("DatabaseInsightsMode")
    PerformanceInsightsEnabled = field("PerformanceInsightsEnabled")
    PerformanceInsightsKMSKeyId = field("PerformanceInsightsKMSKeyId")
    PerformanceInsightsRetentionPeriod = field("PerformanceInsightsRetentionPeriod")
    EnabledCloudwatchLogsExports = field("EnabledCloudwatchLogsExports")

    @cached_property
    def ProcessorFeatures(self):  # pragma: no cover
        return ProcessorFeature.make_many(self.boto3_raw_data["ProcessorFeatures"])

    DeletionProtection = field("DeletionProtection")

    @cached_property
    def AssociatedRoles(self):  # pragma: no cover
        return DBInstanceRole.make_many(self.boto3_raw_data["AssociatedRoles"])

    @cached_property
    def ListenerEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["ListenerEndpoint"])

    MaxAllocatedStorage = field("MaxAllocatedStorage")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def DBInstanceAutomatedBackupsReplications(self):  # pragma: no cover
        return DBInstanceAutomatedBackupsReplication.make_many(
            self.boto3_raw_data["DBInstanceAutomatedBackupsReplications"]
        )

    CustomerOwnedIpEnabled = field("CustomerOwnedIpEnabled")
    AwsBackupRecoveryPointArn = field("AwsBackupRecoveryPointArn")
    ActivityStreamStatus = field("ActivityStreamStatus")
    ActivityStreamKmsKeyId = field("ActivityStreamKmsKeyId")
    ActivityStreamKinesisStreamName = field("ActivityStreamKinesisStreamName")
    ActivityStreamMode = field("ActivityStreamMode")
    ActivityStreamEngineNativeAuditFieldsIncluded = field(
        "ActivityStreamEngineNativeAuditFieldsIncluded"
    )
    AutomationMode = field("AutomationMode")
    ResumeFullAutomationModeTime = field("ResumeFullAutomationModeTime")
    CustomIamInstanceProfile = field("CustomIamInstanceProfile")
    BackupTarget = field("BackupTarget")
    NetworkType = field("NetworkType")
    ActivityStreamPolicyStatus = field("ActivityStreamPolicyStatus")
    StorageThroughput = field("StorageThroughput")
    DBSystemId = field("DBSystemId")

    @cached_property
    def MasterUserSecret(self):  # pragma: no cover
        return MasterUserSecret.make_one(self.boto3_raw_data["MasterUserSecret"])

    @cached_property
    def CertificateDetails(self):  # pragma: no cover
        return CertificateDetails.make_one(self.boto3_raw_data["CertificateDetails"])

    ReadReplicaSourceDBClusterIdentifier = field("ReadReplicaSourceDBClusterIdentifier")
    PercentProgress = field("PercentProgress")
    DedicatedLogVolume = field("DedicatedLogVolume")
    IsStorageConfigUpgradeAvailable = field("IsStorageConfigUpgradeAvailable")
    MultiTenant = field("MultiTenant")
    EngineLifecycleSupport = field("EngineLifecycleSupport")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DBInstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBSubnetGroupMessage:
    boto3_raw_data: "type_defs.DBSubnetGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBSubnetGroups(self):  # pragma: no cover
        return DBSubnetGroup.make_many(self.boto3_raw_data["DBSubnetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBSubnetGroupResult:
    boto3_raw_data: "type_defs.ModifyDBSubnetGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def DBSubnetGroup(self):  # pragma: no cover
        return DBSubnetGroup.make_one(self.boto3_raw_data["DBSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBSubnetGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeValidDBInstanceModificationsResult:
    boto3_raw_data: "type_defs.DescribeValidDBInstanceModificationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ValidDBInstanceModificationsMessage(self):  # pragma: no cover
        return ValidDBInstanceModificationsMessage.make_one(
            self.boto3_raw_data["ValidDBInstanceModificationsMessage"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeValidDBInstanceModificationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeValidDBInstanceModificationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def References(self):  # pragma: no cover
        return MetricReference.make_many(self.boto3_raw_data["References"])

    StatisticsDetails = field("StatisticsDetails")

    @cached_property
    def MetricQuery(self):  # pragma: no cover
        return MetricQuery.make_one(self.boto3_raw_data["MetricQuery"])

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
class CreateDBInstanceReadReplicaResult:
    boto3_raw_data: "type_defs.CreateDBInstanceReadReplicaResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDBInstanceReadReplicaResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBInstanceReadReplicaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDBInstanceResult:
    boto3_raw_data: "type_defs.CreateDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBInstanceMessage:
    boto3_raw_data: "type_defs.DBInstanceMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def DBInstances(self):  # pragma: no cover
        return DBInstance.make_many(self.boto3_raw_data["DBInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBInstanceMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDBInstanceResult:
    boto3_raw_data: "type_defs.DeleteDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDBInstanceResult:
    boto3_raw_data: "type_defs.ModifyDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteReadReplicaResult:
    boto3_raw_data: "type_defs.PromoteReadReplicaResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromoteReadReplicaResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromoteReadReplicaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootDBInstanceResult:
    boto3_raw_data: "type_defs.RebootDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBInstanceFromDBSnapshotResult:
    boto3_raw_data: "type_defs.RestoreDBInstanceFromDBSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBInstanceFromDBSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBInstanceFromDBSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBInstanceFromS3Result:
    boto3_raw_data: "type_defs.RestoreDBInstanceFromS3ResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreDBInstanceFromS3ResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBInstanceFromS3ResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreDBInstanceToPointInTimeResult:
    boto3_raw_data: "type_defs.RestoreDBInstanceToPointInTimeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreDBInstanceToPointInTimeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreDBInstanceToPointInTimeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDBInstanceResult:
    boto3_raw_data: "type_defs.StartDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDBInstanceResult:
    boto3_raw_data: "type_defs.StopDBInstanceResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDBInstanceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDBInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwitchoverReadReplicaResult:
    boto3_raw_data: "type_defs.SwitchoverReadReplicaResultTypeDef" = dataclasses.field()

    @cached_property
    def DBInstance(self):  # pragma: no cover
        return DBInstance.make_one(self.boto3_raw_data["DBInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SwitchoverReadReplicaResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwitchoverReadReplicaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceIssueDetails:
    boto3_raw_data: "type_defs.PerformanceIssueDetailsTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return Metric.make_many(self.boto3_raw_data["Metrics"])

    Analysis = field("Analysis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceIssueDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceIssueDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssueDetails:
    boto3_raw_data: "type_defs.IssueDetailsTypeDef" = dataclasses.field()

    @cached_property
    def PerformanceIssueDetails(self):  # pragma: no cover
        return PerformanceIssueDetails.make_one(
            self.boto3_raw_data["PerformanceIssueDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IssueDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IssueDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedAction:
    boto3_raw_data: "type_defs.RecommendedActionTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    Title = field("Title")
    Description = field("Description")
    Operation = field("Operation")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return RecommendedActionParameter.make_many(self.boto3_raw_data["Parameters"])

    ApplyModes = field("ApplyModes")
    Status = field("Status")

    @cached_property
    def IssueDetails(self):  # pragma: no cover
        return IssueDetails.make_one(self.boto3_raw_data["IssueDetails"])

    @cached_property
    def ContextAttributes(self):  # pragma: no cover
        return ContextAttribute.make_many(self.boto3_raw_data["ContextAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendedActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendedActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBRecommendation:
    boto3_raw_data: "type_defs.DBRecommendationTypeDef" = dataclasses.field()

    RecommendationId = field("RecommendationId")
    TypeId = field("TypeId")
    Severity = field("Severity")
    ResourceArn = field("ResourceArn")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    UpdatedTime = field("UpdatedTime")
    Detection = field("Detection")
    Recommendation = field("Recommendation")
    Description = field("Description")
    Reason = field("Reason")

    @cached_property
    def RecommendedActions(self):  # pragma: no cover
        return RecommendedAction.make_many(self.boto3_raw_data["RecommendedActions"])

    Category = field("Category")
    Source = field("Source")
    TypeDetection = field("TypeDetection")
    TypeRecommendation = field("TypeRecommendation")
    Impact = field("Impact")
    AdditionalInfo = field("AdditionalInfo")

    @cached_property
    def Links(self):  # pragma: no cover
        return DocLink.make_many(self.boto3_raw_data["Links"])

    @cached_property
    def IssueDetails(self):  # pragma: no cover
        return IssueDetails.make_one(self.boto3_raw_data["IssueDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DBRecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBRecommendationMessage:
    boto3_raw_data: "type_defs.DBRecommendationMessageTypeDef" = dataclasses.field()

    @cached_property
    def DBRecommendation(self):  # pragma: no cover
        return DBRecommendation.make_one(self.boto3_raw_data["DBRecommendation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBRecommendationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBRecommendationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DBRecommendationsMessage:
    boto3_raw_data: "type_defs.DBRecommendationsMessageTypeDef" = dataclasses.field()

    @cached_property
    def DBRecommendations(self):  # pragma: no cover
        return DBRecommendation.make_many(self.boto3_raw_data["DBRecommendations"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DBRecommendationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DBRecommendationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
