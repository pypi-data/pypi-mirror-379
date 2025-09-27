# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dynamodb import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ArchivalSummary:
    boto3_raw_data: "type_defs.ArchivalSummaryTypeDef" = dataclasses.field()

    ArchivalDateTime = field("ArchivalDateTime")
    ArchivalReason = field("ArchivalReason")
    ArchivalBackupArn = field("ArchivalBackupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchivalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArchivalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDefinition:
    boto3_raw_data: "type_defs.AttributeDefinitionTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeType = field("AttributeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValue:
    boto3_raw_data: "type_defs.AttributeValueTypeDef" = dataclasses.field()

    S = field("S")
    N = field("N")
    B = field("B")
    SS = field("SS")
    NS = field("NS")
    BS = field("BS")
    M = field("M")
    L = field("L")
    NULL = field("NULL")
    BOOL = field("BOOL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingTargetTrackingScalingPolicyConfigurationDescription:
    boto3_raw_data: "type_defs.AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef" = (dataclasses.field())

    TargetValue = field("TargetValue")
    DisableScaleIn = field("DisableScaleIn")
    ScaleInCooldown = field("ScaleInCooldown")
    ScaleOutCooldown = field("ScaleOutCooldown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef"
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
                "type_defs.AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingTargetTrackingScalingPolicyConfigurationUpdate:
    boto3_raw_data: (
        "type_defs.AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"
    ) = dataclasses.field()

    TargetValue = field("TargetValue")
    DisableScaleIn = field("DisableScaleIn")
    ScaleInCooldown = field("ScaleInCooldown")
    ScaleOutCooldown = field("ScaleOutCooldown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"
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
                "type_defs.AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupDetails:
    boto3_raw_data: "type_defs.BackupDetailsTypeDef" = dataclasses.field()

    BackupArn = field("BackupArn")
    BackupName = field("BackupName")
    BackupStatus = field("BackupStatus")
    BackupType = field("BackupType")
    BackupCreationDateTime = field("BackupCreationDateTime")
    BackupSizeBytes = field("BackupSizeBytes")
    BackupExpiryDateTime = field("BackupExpiryDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupSummary:
    boto3_raw_data: "type_defs.BackupSummaryTypeDef" = dataclasses.field()

    TableName = field("TableName")
    TableId = field("TableId")
    TableArn = field("TableArn")
    BackupArn = field("BackupArn")
    BackupName = field("BackupName")
    BackupCreationDateTime = field("BackupCreationDateTime")
    BackupExpiryDateTime = field("BackupExpiryDateTime")
    BackupStatus = field("BackupStatus")
    BackupType = field("BackupType")
    BackupSizeBytes = field("BackupSizeBytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupSummaryTypeDef"]],
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
class BillingModeSummary:
    boto3_raw_data: "type_defs.BillingModeSummaryTypeDef" = dataclasses.field()

    BillingMode = field("BillingMode")
    LastUpdateToPayPerRequestDateTime = field("LastUpdateToPayPerRequestDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillingModeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingModeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Capacity:
    boto3_raw_data: "type_defs.CapacityTypeDef" = dataclasses.field()

    ReadCapacityUnits = field("ReadCapacityUnits")
    WriteCapacityUnits = field("WriteCapacityUnits")
    CapacityUnits = field("CapacityUnits")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PointInTimeRecoveryDescription:
    boto3_raw_data: "type_defs.PointInTimeRecoveryDescriptionTypeDef" = (
        dataclasses.field()
    )

    PointInTimeRecoveryStatus = field("PointInTimeRecoveryStatus")
    RecoveryPeriodInDays = field("RecoveryPeriodInDays")
    EarliestRestorableDateTime = field("EarliestRestorableDateTime")
    LatestRestorableDateTime = field("LatestRestorableDateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PointInTimeRecoveryDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PointInTimeRecoveryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContributorInsightsSummary:
    boto3_raw_data: "type_defs.ContributorInsightsSummaryTypeDef" = dataclasses.field()

    TableName = field("TableName")
    IndexName = field("IndexName")
    ContributorInsightsStatus = field("ContributorInsightsStatus")
    ContributorInsightsMode = field("ContributorInsightsMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContributorInsightsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContributorInsightsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupInput:
    boto3_raw_data: "type_defs.CreateBackupInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    BackupName = field("BackupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBackupInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeySchemaElement:
    boto3_raw_data: "type_defs.KeySchemaElementTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    KeyType = field("KeyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeySchemaElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeySchemaElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnDemandThroughput:
    boto3_raw_data: "type_defs.OnDemandThroughputTypeDef" = dataclasses.field()

    MaxReadRequestUnits = field("MaxReadRequestUnits")
    MaxWriteRequestUnits = field("MaxWriteRequestUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnDemandThroughputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnDemandThroughputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedThroughput:
    boto3_raw_data: "type_defs.ProvisionedThroughputTypeDef" = dataclasses.field()

    ReadCapacityUnits = field("ReadCapacityUnits")
    WriteCapacityUnits = field("WriteCapacityUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedThroughputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedThroughputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarmThroughput:
    boto3_raw_data: "type_defs.WarmThroughputTypeDef" = dataclasses.field()

    ReadUnitsPerSecond = field("ReadUnitsPerSecond")
    WriteUnitsPerSecond = field("WriteUnitsPerSecond")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarmThroughputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarmThroughputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Replica:
    boto3_raw_data: "type_defs.ReplicaTypeDef" = dataclasses.field()

    RegionName = field("RegionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalTableWitnessGroupMemberAction:
    boto3_raw_data: "type_defs.CreateGlobalTableWitnessGroupMemberActionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGlobalTableWitnessGroupMemberActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalTableWitnessGroupMemberActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicaAction:
    boto3_raw_data: "type_defs.CreateReplicaActionTypeDef" = dataclasses.field()

    RegionName = field("RegionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicaActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicaActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnDemandThroughputOverride:
    boto3_raw_data: "type_defs.OnDemandThroughputOverrideTypeDef" = dataclasses.field()

    MaxReadRequestUnits = field("MaxReadRequestUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnDemandThroughputOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnDemandThroughputOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedThroughputOverride:
    boto3_raw_data: "type_defs.ProvisionedThroughputOverrideTypeDef" = (
        dataclasses.field()
    )

    ReadCapacityUnits = field("ReadCapacityUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionedThroughputOverrideTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedThroughputOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSESpecification:
    boto3_raw_data: "type_defs.SSESpecificationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SSEType = field("SSEType")
    KMSMasterKeyId = field("KMSMasterKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSESpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SSESpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamSpecification:
    boto3_raw_data: "type_defs.StreamSpecificationTypeDef" = dataclasses.field()

    StreamEnabled = field("StreamEnabled")
    StreamViewType = field("StreamViewType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamSpecificationTypeDef"]
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
class CsvOptionsOutput:
    boto3_raw_data: "type_defs.CsvOptionsOutputTypeDef" = dataclasses.field()

    Delimiter = field("Delimiter")
    HeaderList = field("HeaderList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvOptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CsvOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CsvOptions:
    boto3_raw_data: "type_defs.CsvOptionsTypeDef" = dataclasses.field()

    Delimiter = field("Delimiter")
    HeaderList = field("HeaderList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CsvOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CsvOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupInput:
    boto3_raw_data: "type_defs.DeleteBackupInputTypeDef" = dataclasses.field()

    BackupArn = field("BackupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalSecondaryIndexAction:
    boto3_raw_data: "type_defs.DeleteGlobalSecondaryIndexActionTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteGlobalSecondaryIndexActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalSecondaryIndexActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlobalTableWitnessGroupMemberAction:
    boto3_raw_data: "type_defs.DeleteGlobalTableWitnessGroupMemberActionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteGlobalTableWitnessGroupMemberActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlobalTableWitnessGroupMemberActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicaAction:
    boto3_raw_data: "type_defs.DeleteReplicaActionTypeDef" = dataclasses.field()

    RegionName = field("RegionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReplicaActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicaActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationGroupMemberAction:
    boto3_raw_data: "type_defs.DeleteReplicationGroupMemberActionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationGroupMemberActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationGroupMemberActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyInput:
    boto3_raw_data: "type_defs.DeleteResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ExpectedRevisionId = field("ExpectedRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTableInput:
    boto3_raw_data: "type_defs.DeleteTableInputTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTableInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupInput:
    boto3_raw_data: "type_defs.DescribeBackupInputTypeDef" = dataclasses.field()

    BackupArn = field("BackupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContinuousBackupsInput:
    boto3_raw_data: "type_defs.DescribeContinuousBackupsInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeContinuousBackupsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContinuousBackupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContributorInsightsInput:
    boto3_raw_data: "type_defs.DescribeContributorInsightsInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    IndexName = field("IndexName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeContributorInsightsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContributorInsightsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureException:
    boto3_raw_data: "type_defs.FailureExceptionTypeDef" = dataclasses.field()

    ExceptionName = field("ExceptionName")
    ExceptionDescription = field("ExceptionDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureExceptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailureExceptionTypeDef"]
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
    CachePeriodInMinutes = field("CachePeriodInMinutes")

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
class DescribeExportInput:
    boto3_raw_data: "type_defs.DescribeExportInputTypeDef" = dataclasses.field()

    ExportArn = field("ExportArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalTableInput:
    boto3_raw_data: "type_defs.DescribeGlobalTableInputTypeDef" = dataclasses.field()

    GlobalTableName = field("GlobalTableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGlobalTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalTableSettingsInput:
    boto3_raw_data: "type_defs.DescribeGlobalTableSettingsInputTypeDef" = (
        dataclasses.field()
    )

    GlobalTableName = field("GlobalTableName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGlobalTableSettingsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalTableSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImportInput:
    boto3_raw_data: "type_defs.DescribeImportInputTypeDef" = dataclasses.field()

    ImportArn = field("ImportArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImportInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKinesisStreamingDestinationInput:
    boto3_raw_data: "type_defs.DescribeKinesisStreamingDestinationInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeKinesisStreamingDestinationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKinesisStreamingDestinationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisDataStreamDestination:
    boto3_raw_data: "type_defs.KinesisDataStreamDestinationTypeDef" = (
        dataclasses.field()
    )

    StreamArn = field("StreamArn")
    DestinationStatus = field("DestinationStatus")
    DestinationStatusDescription = field("DestinationStatusDescription")
    ApproximateCreationDateTimePrecision = field("ApproximateCreationDateTimePrecision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisDataStreamDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisDataStreamDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableInput:
    boto3_raw_data: "type_defs.DescribeTableInputTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableInputTypeDef"]
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
class DescribeTableReplicaAutoScalingInput:
    boto3_raw_data: "type_defs.DescribeTableReplicaAutoScalingInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTableReplicaAutoScalingInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableReplicaAutoScalingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTimeToLiveInput:
    boto3_raw_data: "type_defs.DescribeTimeToLiveInputTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTimeToLiveInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTimeToLiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeToLiveDescription:
    boto3_raw_data: "type_defs.TimeToLiveDescriptionTypeDef" = dataclasses.field()

    TimeToLiveStatus = field("TimeToLiveStatus")
    AttributeName = field("AttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeToLiveDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeToLiveDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableKinesisStreamingConfiguration:
    boto3_raw_data: "type_defs.EnableKinesisStreamingConfigurationTypeDef" = (
        dataclasses.field()
    )

    ApproximateCreationDateTimePrecision = field("ApproximateCreationDateTimePrecision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableKinesisStreamingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableKinesisStreamingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalExportSpecificationOutput:
    boto3_raw_data: "type_defs.IncrementalExportSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    ExportFromTime = field("ExportFromTime")
    ExportToTime = field("ExportToTime")
    ExportViewType = field("ExportViewType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IncrementalExportSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncrementalExportSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSummary:
    boto3_raw_data: "type_defs.ExportSummaryTypeDef" = dataclasses.field()

    ExportArn = field("ExportArn")
    ExportStatus = field("ExportStatus")
    ExportType = field("ExportType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyInput:
    boto3_raw_data: "type_defs.GetResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndexWarmThroughputDescription:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexWarmThroughputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ReadUnitsPerSecond = field("ReadUnitsPerSecond")
    WriteUnitsPerSecond = field("WriteUnitsPerSecond")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GlobalSecondaryIndexWarmThroughputDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexWarmThroughputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectionOutput:
    boto3_raw_data: "type_defs.ProjectionOutputTypeDef" = dataclasses.field()

    ProjectionType = field("ProjectionType")
    NonKeyAttributes = field("NonKeyAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedThroughputDescription:
    boto3_raw_data: "type_defs.ProvisionedThroughputDescriptionTypeDef" = (
        dataclasses.field()
    )

    LastIncreaseDateTime = field("LastIncreaseDateTime")
    LastDecreaseDateTime = field("LastDecreaseDateTime")
    NumberOfDecreasesToday = field("NumberOfDecreasesToday")
    ReadCapacityUnits = field("ReadCapacityUnits")
    WriteCapacityUnits = field("WriteCapacityUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionedThroughputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedThroughputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalTableWitnessDescription:
    boto3_raw_data: "type_defs.GlobalTableWitnessDescriptionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")
    WitnessStatus = field("WitnessStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlobalTableWitnessDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalTableWitnessDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketSource:
    boto3_raw_data: "type_defs.S3BucketSourceTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3BucketOwner = field("S3BucketOwner")
    S3KeyPrefix = field("S3KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketSourceTypeDef"]],
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
class ListContributorInsightsInput:
    boto3_raw_data: "type_defs.ListContributorInsightsInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContributorInsightsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContributorInsightsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsInput:
    boto3_raw_data: "type_defs.ListExportsInputTypeDef" = dataclasses.field()

    TableArn = field("TableArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListExportsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGlobalTablesInput:
    boto3_raw_data: "type_defs.ListGlobalTablesInputTypeDef" = dataclasses.field()

    ExclusiveStartGlobalTableName = field("ExclusiveStartGlobalTableName")
    Limit = field("Limit")
    RegionName = field("RegionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGlobalTablesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGlobalTablesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsInput:
    boto3_raw_data: "type_defs.ListImportsInputTypeDef" = dataclasses.field()

    TableArn = field("TableArn")
    PageSize = field("PageSize")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImportsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesInput:
    boto3_raw_data: "type_defs.ListTablesInputTypeDef" = dataclasses.field()

    ExclusiveStartTableName = field("ExclusiveStartTableName")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTablesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTablesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsOfResourceInput:
    boto3_raw_data: "type_defs.ListTagsOfResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsOfResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsOfResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PointInTimeRecoverySpecification:
    boto3_raw_data: "type_defs.PointInTimeRecoverySpecificationTypeDef" = (
        dataclasses.field()
    )

    PointInTimeRecoveryEnabled = field("PointInTimeRecoveryEnabled")
    RecoveryPeriodInDays = field("RecoveryPeriodInDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PointInTimeRecoverySpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PointInTimeRecoverySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Projection:
    boto3_raw_data: "type_defs.ProjectionTypeDef" = dataclasses.field()

    ProjectionType = field("ProjectionType")
    NonKeyAttributes = field("NonKeyAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyInput:
    boto3_raw_data: "type_defs.PutResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")
    ExpectedRevisionId = field("ExpectedRevisionId")
    ConfirmRemoveSelfResourceAccess = field("ConfirmRemoveSelfResourceAccess")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableClassSummary:
    boto3_raw_data: "type_defs.TableClassSummaryTypeDef" = dataclasses.field()

    TableClass = field("TableClass")
    LastUpdateDateTime = field("LastUpdateDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableClassSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableClassSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableWarmThroughputDescription:
    boto3_raw_data: "type_defs.TableWarmThroughputDescriptionTypeDef" = (
        dataclasses.field()
    )

    ReadUnitsPerSecond = field("ReadUnitsPerSecond")
    WriteUnitsPerSecond = field("WriteUnitsPerSecond")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TableWarmThroughputDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableWarmThroughputDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreSummary:
    boto3_raw_data: "type_defs.RestoreSummaryTypeDef" = dataclasses.field()

    RestoreDateTime = field("RestoreDateTime")
    RestoreInProgress = field("RestoreInProgress")
    SourceBackupArn = field("SourceBackupArn")
    SourceTableArn = field("SourceTableArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestoreSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSEDescription:
    boto3_raw_data: "type_defs.SSEDescriptionTypeDef" = dataclasses.field()

    Status = field("Status")
    SSEType = field("SSEType")
    KMSMasterKeyArn = field("KMSMasterKeyArn")
    InaccessibleEncryptionDateTime = field("InaccessibleEncryptionDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSEDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSEDescriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableBatchWriterRequest:
    boto3_raw_data: "type_defs.TableBatchWriterRequestTypeDef" = dataclasses.field()

    overwrite_by_pkeys = field("overwrite_by_pkeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableBatchWriterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableBatchWriterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeToLiveSpecification:
    boto3_raw_data: "type_defs.TimeToLiveSpecificationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    AttributeName = field("AttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeToLiveSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeToLiveSpecificationTypeDef"]
        ],
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
class UpdateContributorInsightsInput:
    boto3_raw_data: "type_defs.UpdateContributorInsightsInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    ContributorInsightsAction = field("ContributorInsightsAction")
    IndexName = field("IndexName")
    ContributorInsightsMode = field("ContributorInsightsMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContributorInsightsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContributorInsightsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKinesisStreamingConfiguration:
    boto3_raw_data: "type_defs.UpdateKinesisStreamingConfigurationTypeDef" = (
        dataclasses.field()
    )

    ApproximateCreationDateTimePrecision = field("ApproximateCreationDateTimePrecision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKinesisStreamingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKinesisStreamingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStatementError:
    boto3_raw_data: "type_defs.BatchStatementErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    Item = field("Item")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchStatementErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStatementErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRequestOutput:
    boto3_raw_data: "type_defs.DeleteRequestOutputTypeDef" = dataclasses.field()

    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRequestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemCollectionMetrics:
    boto3_raw_data: "type_defs.ItemCollectionMetricsTypeDef" = dataclasses.field()

    ItemCollectionKey = field("ItemCollectionKey")
    SizeEstimateRangeGB = field("SizeEstimateRangeGB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ItemCollectionMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ItemCollectionMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemResponse:
    boto3_raw_data: "type_defs.ItemResponseTypeDef" = dataclasses.field()

    Item = field("Item")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ItemResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeysAndAttributesOutput:
    boto3_raw_data: "type_defs.KeysAndAttributesOutputTypeDef" = dataclasses.field()

    Keys = field("Keys")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeysAndAttributesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeysAndAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRequestOutput:
    boto3_raw_data: "type_defs.PutRequestOutputTypeDef" = dataclasses.field()

    Item = field("Item")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRequestOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValueUpdateTable:
    boto3_raw_data: "type_defs.AttributeValueUpdateTableTypeDef" = dataclasses.field()

    Value = field("Value")
    Action = field("Action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueUpdateTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueUpdateTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionTable:
    boto3_raw_data: "type_defs.ConditionTableTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    AttributeValueList = field("AttributeValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTableTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRequestServiceResourceOutput:
    boto3_raw_data: "type_defs.DeleteRequestServiceResourceOutputTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRequestServiceResourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRequestServiceResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRequestServiceResource:
    boto3_raw_data: "type_defs.DeleteRequestServiceResourceTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRequestServiceResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRequestServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpectedAttributeValueTable:
    boto3_raw_data: "type_defs.ExpectedAttributeValueTableTypeDef" = dataclasses.field()

    Value = field("Value")
    Exists = field("Exists")
    ComparisonOperator = field("ComparisonOperator")
    AttributeValueList = field("AttributeValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpectedAttributeValueTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpectedAttributeValueTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetItemInputTableGetItem:
    boto3_raw_data: "type_defs.GetItemInputTableGetItemTypeDef" = dataclasses.field()

    Key = field("Key")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetItemInputTableGetItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetItemInputTableGetItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemCollectionMetricsServiceResource:
    boto3_raw_data: "type_defs.ItemCollectionMetricsServiceResourceTypeDef" = (
        dataclasses.field()
    )

    ItemCollectionKey = field("ItemCollectionKey")
    SizeEstimateRangeGB = field("SizeEstimateRangeGB")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ItemCollectionMetricsServiceResourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ItemCollectionMetricsServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemCollectionMetricsTable:
    boto3_raw_data: "type_defs.ItemCollectionMetricsTableTypeDef" = dataclasses.field()

    ItemCollectionKey = field("ItemCollectionKey")
    SizeEstimateRangeGB = field("SizeEstimateRangeGB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ItemCollectionMetricsTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ItemCollectionMetricsTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeysAndAttributesServiceResourceOutput:
    boto3_raw_data: "type_defs.KeysAndAttributesServiceResourceOutputTypeDef" = (
        dataclasses.field()
    )

    Keys = field("Keys")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KeysAndAttributesServiceResourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeysAndAttributesServiceResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeysAndAttributesServiceResource:
    boto3_raw_data: "type_defs.KeysAndAttributesServiceResourceTypeDef" = (
        dataclasses.field()
    )

    Keys = field("Keys")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KeysAndAttributesServiceResourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeysAndAttributesServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRequestServiceResourceOutput:
    boto3_raw_data: "type_defs.PutRequestServiceResourceOutputTypeDef" = (
        dataclasses.field()
    )

    Item = field("Item")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRequestServiceResourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRequestServiceResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRequestServiceResource:
    boto3_raw_data: "type_defs.PutRequestServiceResourceTypeDef" = dataclasses.field()

    Item = field("Item")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRequestServiceResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRequestServiceResourceTypeDef"]
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

    PolicyName = field("PolicyName")

    @cached_property
    def TargetTrackingScalingPolicyConfiguration(self):  # pragma: no cover
        return AutoScalingTargetTrackingScalingPolicyConfigurationDescription.make_one(
            self.boto3_raw_data["TargetTrackingScalingPolicyConfiguration"]
        )

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
class AutoScalingPolicyUpdate:
    boto3_raw_data: "type_defs.AutoScalingPolicyUpdateTypeDef" = dataclasses.field()

    @cached_property
    def TargetTrackingScalingPolicyConfiguration(self):  # pragma: no cover
        return AutoScalingTargetTrackingScalingPolicyConfigurationUpdate.make_one(
            self.boto3_raw_data["TargetTrackingScalingPolicyConfiguration"]
        )

    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingPolicyUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingPolicyUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupOutput:
    boto3_raw_data: "type_defs.CreateBackupOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupDetails(self):  # pragma: no cover
        return BackupDetails.make_one(self.boto3_raw_data["BackupDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyOutput:
    boto3_raw_data: "type_defs.DeleteResourcePolicyOutputTypeDef" = dataclasses.field()

    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLimitsOutput:
    boto3_raw_data: "type_defs.DescribeLimitsOutputTypeDef" = dataclasses.field()

    AccountMaxReadCapacityUnits = field("AccountMaxReadCapacityUnits")
    AccountMaxWriteCapacityUnits = field("AccountMaxWriteCapacityUnits")
    TableMaxReadCapacityUnits = field("TableMaxReadCapacityUnits")
    TableMaxWriteCapacityUnits = field("TableMaxWriteCapacityUnits")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLimitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLimitsOutputTypeDef"]
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
class GetResourcePolicyOutput:
    boto3_raw_data: "type_defs.GetResourcePolicyOutputTypeDef" = dataclasses.field()

    Policy = field("Policy")
    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupsOutput:
    boto3_raw_data: "type_defs.ListBackupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupSummaries(self):  # pragma: no cover
        return BackupSummary.make_many(self.boto3_raw_data["BackupSummaries"])

    LastEvaluatedBackupArn = field("LastEvaluatedBackupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBackupsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesOutput:
    boto3_raw_data: "type_defs.ListTablesOutputTypeDef" = dataclasses.field()

    TableNames = field("TableNames")
    LastEvaluatedTableName = field("LastEvaluatedTableName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTablesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyOutput:
    boto3_raw_data: "type_defs.PutResourcePolicyOutputTypeDef" = dataclasses.field()

    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContributorInsightsOutput:
    boto3_raw_data: "type_defs.UpdateContributorInsightsOutputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    IndexName = field("IndexName")
    ContributorInsightsStatus = field("ContributorInsightsStatus")
    ContributorInsightsMode = field("ContributorInsightsMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContributorInsightsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContributorInsightsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumedCapacity:
    boto3_raw_data: "type_defs.ConsumedCapacityTypeDef" = dataclasses.field()

    TableName = field("TableName")
    CapacityUnits = field("CapacityUnits")
    ReadCapacityUnits = field("ReadCapacityUnits")
    WriteCapacityUnits = field("WriteCapacityUnits")

    @cached_property
    def Table(self):  # pragma: no cover
        return Capacity.make_one(self.boto3_raw_data["Table"])

    LocalSecondaryIndexes = field("LocalSecondaryIndexes")
    GlobalSecondaryIndexes = field("GlobalSecondaryIndexes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConsumedCapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumedCapacityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousBackupsDescription:
    boto3_raw_data: "type_defs.ContinuousBackupsDescriptionTypeDef" = (
        dataclasses.field()
    )

    ContinuousBackupsStatus = field("ContinuousBackupsStatus")

    @cached_property
    def PointInTimeRecoveryDescription(self):  # pragma: no cover
        return PointInTimeRecoveryDescription.make_one(
            self.boto3_raw_data["PointInTimeRecoveryDescription"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContinuousBackupsDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousBackupsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContributorInsightsOutput:
    boto3_raw_data: "type_defs.ListContributorInsightsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContributorInsightsSummaries(self):  # pragma: no cover
        return ContributorInsightsSummary.make_many(
            self.boto3_raw_data["ContributorInsightsSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContributorInsightsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContributorInsightsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceTableDetails:
    boto3_raw_data: "type_defs.SourceTableDetailsTypeDef" = dataclasses.field()

    TableName = field("TableName")
    TableId = field("TableId")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    TableCreationDateTime = field("TableCreationDateTime")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    TableArn = field("TableArn")
    TableSizeBytes = field("TableSizeBytes")

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    ItemCount = field("ItemCount")
    BillingMode = field("BillingMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceTableDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceTableDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalSecondaryIndexAction:
    boto3_raw_data: "type_defs.UpdateGlobalSecondaryIndexActionTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGlobalSecondaryIndexActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalSecondaryIndexActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalTableInput:
    boto3_raw_data: "type_defs.CreateGlobalTableInputTypeDef" = dataclasses.field()

    GlobalTableName = field("GlobalTableName")

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return Replica.make_many(self.boto3_raw_data["ReplicationGroup"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalTable:
    boto3_raw_data: "type_defs.GlobalTableTypeDef" = dataclasses.field()

    GlobalTableName = field("GlobalTableName")

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return Replica.make_many(self.boto3_raw_data["ReplicationGroup"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlobalTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlobalTableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaGlobalSecondaryIndex:
    boto3_raw_data: "type_defs.ReplicaGlobalSecondaryIndexTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughputOverride.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughputOverride.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaGlobalSecondaryIndexTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaGlobalSecondaryIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsOfResourceOutput:
    boto3_raw_data: "type_defs.ListTagsOfResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsOfResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsOfResourceOutputTypeDef"]
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
class InputFormatOptionsOutput:
    boto3_raw_data: "type_defs.InputFormatOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Csv(self):  # pragma: no cover
        return CsvOptionsOutput.make_one(self.boto3_raw_data["Csv"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputFormatOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputFormatOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFormatOptions:
    boto3_raw_data: "type_defs.InputFormatOptionsTypeDef" = dataclasses.field()

    @cached_property
    def Csv(self):  # pragma: no cover
        return CsvOptions.make_one(self.boto3_raw_data["Csv"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputFormatOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputFormatOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalTableWitnessGroupUpdate:
    boto3_raw_data: "type_defs.GlobalTableWitnessGroupUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Create(self):  # pragma: no cover
        return CreateGlobalTableWitnessGroupMemberAction.make_one(
            self.boto3_raw_data["Create"]
        )

    @cached_property
    def Delete(self):  # pragma: no cover
        return DeleteGlobalTableWitnessGroupMemberAction.make_one(
            self.boto3_raw_data["Delete"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlobalTableWitnessGroupUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalTableWitnessGroupUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaUpdate:
    boto3_raw_data: "type_defs.ReplicaUpdateTypeDef" = dataclasses.field()

    @cached_property
    def Create(self):  # pragma: no cover
        return CreateReplicaAction.make_one(self.boto3_raw_data["Create"])

    @cached_property
    def Delete(self):  # pragma: no cover
        return DeleteReplicaAction.make_one(self.boto3_raw_data["Delete"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicaUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicaUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContributorInsightsOutput:
    boto3_raw_data: "type_defs.DescribeContributorInsightsOutputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    IndexName = field("IndexName")
    ContributorInsightsRuleList = field("ContributorInsightsRuleList")
    ContributorInsightsStatus = field("ContributorInsightsStatus")
    LastUpdateDateTime = field("LastUpdateDateTime")

    @cached_property
    def FailureException(self):  # pragma: no cover
        return FailureException.make_one(self.boto3_raw_data["FailureException"])

    ContributorInsightsMode = field("ContributorInsightsMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContributorInsightsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContributorInsightsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKinesisStreamingDestinationOutput:
    boto3_raw_data: "type_defs.DescribeKinesisStreamingDestinationOutputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @cached_property
    def KinesisDataStreamDestinations(self):  # pragma: no cover
        return KinesisDataStreamDestination.make_many(
            self.boto3_raw_data["KinesisDataStreamDestinations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeKinesisStreamingDestinationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKinesisStreamingDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeTableInputWaitExtraTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableInputWait:
    boto3_raw_data: "type_defs.DescribeTableInputWaitTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTimeToLiveOutput:
    boto3_raw_data: "type_defs.DescribeTimeToLiveOutputTypeDef" = dataclasses.field()

    @cached_property
    def TimeToLiveDescription(self):  # pragma: no cover
        return TimeToLiveDescription.make_one(
            self.boto3_raw_data["TimeToLiveDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTimeToLiveOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTimeToLiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamingDestinationInputRequest:
    boto3_raw_data: "type_defs.KinesisStreamingDestinationInputRequestTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    StreamArn = field("StreamArn")

    @cached_property
    def EnableKinesisStreamingConfiguration(self):  # pragma: no cover
        return EnableKinesisStreamingConfiguration.make_one(
            self.boto3_raw_data["EnableKinesisStreamingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisStreamingDestinationInputRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamingDestinationInputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamingDestinationInput:
    boto3_raw_data: "type_defs.KinesisStreamingDestinationInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    StreamArn = field("StreamArn")

    @cached_property
    def EnableKinesisStreamingConfiguration(self):  # pragma: no cover
        return EnableKinesisStreamingConfiguration.make_one(
            self.boto3_raw_data["EnableKinesisStreamingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamingDestinationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamingDestinationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamingDestinationOutput:
    boto3_raw_data: "type_defs.KinesisStreamingDestinationOutputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    StreamArn = field("StreamArn")
    DestinationStatus = field("DestinationStatus")

    @cached_property
    def EnableKinesisStreamingConfiguration(self):  # pragma: no cover
        return EnableKinesisStreamingConfiguration.make_one(
            self.boto3_raw_data["EnableKinesisStreamingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisStreamingDestinationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamingDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportDescription:
    boto3_raw_data: "type_defs.ExportDescriptionTypeDef" = dataclasses.field()

    ExportArn = field("ExportArn")
    ExportStatus = field("ExportStatus")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ExportManifest = field("ExportManifest")
    TableArn = field("TableArn")
    TableId = field("TableId")
    ExportTime = field("ExportTime")
    ClientToken = field("ClientToken")
    S3Bucket = field("S3Bucket")
    S3BucketOwner = field("S3BucketOwner")
    S3Prefix = field("S3Prefix")
    S3SseAlgorithm = field("S3SseAlgorithm")
    S3SseKmsKeyId = field("S3SseKmsKeyId")
    FailureCode = field("FailureCode")
    FailureMessage = field("FailureMessage")
    ExportFormat = field("ExportFormat")
    BilledSizeBytes = field("BilledSizeBytes")
    ItemCount = field("ItemCount")
    ExportType = field("ExportType")

    @cached_property
    def IncrementalExportSpecification(self):  # pragma: no cover
        return IncrementalExportSpecificationOutput.make_one(
            self.boto3_raw_data["IncrementalExportSpecification"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsOutput:
    boto3_raw_data: "type_defs.ListExportsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ExportSummaries(self):  # pragma: no cover
        return ExportSummary.make_many(self.boto3_raw_data["ExportSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListExportsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalExportSpecification:
    boto3_raw_data: "type_defs.IncrementalExportSpecificationTypeDef" = (
        dataclasses.field()
    )

    ExportFromTime = field("ExportFromTime")
    ExportToTime = field("ExportToTime")
    ExportViewType = field("ExportViewType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IncrementalExportSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncrementalExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupsInput:
    boto3_raw_data: "type_defs.ListBackupsInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    Limit = field("Limit")
    TimeRangeLowerBound = field("TimeRangeLowerBound")
    TimeRangeUpperBound = field("TimeRangeUpperBound")
    ExclusiveStartBackupArn = field("ExclusiveStartBackupArn")
    BackupType = field("BackupType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBackupsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaGlobalSecondaryIndexDescription:
    boto3_raw_data: "type_defs.ReplicaGlobalSecondaryIndexDescriptionTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughputOverride.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughputOverride.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return GlobalSecondaryIndexWarmThroughputDescription.make_one(
            self.boto3_raw_data["WarmThroughput"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicaGlobalSecondaryIndexDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaGlobalSecondaryIndexDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndexInfo:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexInfoTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def Projection(self):  # pragma: no cover
        return ProjectionOutput.make_one(self.boto3_raw_data["Projection"])

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalSecondaryIndexInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndexOutput:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexOutputTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def Projection(self):  # pragma: no cover
        return ProjectionOutput.make_one(self.boto3_raw_data["Projection"])

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalSecondaryIndexOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalSecondaryIndexDescription:
    boto3_raw_data: "type_defs.LocalSecondaryIndexDescriptionTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def Projection(self):  # pragma: no cover
        return ProjectionOutput.make_one(self.boto3_raw_data["Projection"])

    IndexSizeBytes = field("IndexSizeBytes")
    ItemCount = field("ItemCount")
    IndexArn = field("IndexArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LocalSecondaryIndexDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalSecondaryIndexDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalSecondaryIndexInfo:
    boto3_raw_data: "type_defs.LocalSecondaryIndexInfoTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def Projection(self):  # pragma: no cover
        return ProjectionOutput.make_one(self.boto3_raw_data["Projection"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalSecondaryIndexInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalSecondaryIndexInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndexDescription:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexDescriptionTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def Projection(self):  # pragma: no cover
        return ProjectionOutput.make_one(self.boto3_raw_data["Projection"])

    IndexStatus = field("IndexStatus")
    Backfilling = field("Backfilling")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughputDescription.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    IndexSizeBytes = field("IndexSizeBytes")
    ItemCount = field("ItemCount")
    IndexArn = field("IndexArn")

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return GlobalSecondaryIndexWarmThroughputDescription.make_one(
            self.boto3_raw_data["WarmThroughput"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlobalSecondaryIndexDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSummary:
    boto3_raw_data: "type_defs.ImportSummaryTypeDef" = dataclasses.field()

    ImportArn = field("ImportArn")
    ImportStatus = field("ImportStatus")
    TableArn = field("TableArn")

    @cached_property
    def S3BucketSource(self):  # pragma: no cover
        return S3BucketSource.make_one(self.boto3_raw_data["S3BucketSource"])

    CloudWatchLogGroupArn = field("CloudWatchLogGroupArn")
    InputFormat = field("InputFormat")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupsInputPaginate:
    boto3_raw_data: "type_defs.ListBackupsInputPaginateTypeDef" = dataclasses.field()

    TableName = field("TableName")
    TimeRangeLowerBound = field("TimeRangeLowerBound")
    TimeRangeUpperBound = field("TimeRangeUpperBound")
    BackupType = field("BackupType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTablesInputPaginate:
    boto3_raw_data: "type_defs.ListTablesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTablesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTablesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsOfResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsOfResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsOfResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsOfResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContinuousBackupsInput:
    boto3_raw_data: "type_defs.UpdateContinuousBackupsInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @cached_property
    def PointInTimeRecoverySpecification(self):  # pragma: no cover
        return PointInTimeRecoverySpecification.make_one(
            self.boto3_raw_data["PointInTimeRecoverySpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContinuousBackupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContinuousBackupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTimeToLiveInput:
    boto3_raw_data: "type_defs.UpdateTimeToLiveInputTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @cached_property
    def TimeToLiveSpecification(self):  # pragma: no cover
        return TimeToLiveSpecification.make_one(
            self.boto3_raw_data["TimeToLiveSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTimeToLiveInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTimeToLiveInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTimeToLiveOutput:
    boto3_raw_data: "type_defs.UpdateTimeToLiveOutputTypeDef" = dataclasses.field()

    @cached_property
    def TimeToLiveSpecification(self):  # pragma: no cover
        return TimeToLiveSpecification.make_one(
            self.boto3_raw_data["TimeToLiveSpecification"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTimeToLiveOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTimeToLiveOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKinesisStreamingDestinationInput:
    boto3_raw_data: "type_defs.UpdateKinesisStreamingDestinationInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    StreamArn = field("StreamArn")

    @cached_property
    def UpdateKinesisStreamingConfiguration(self):  # pragma: no cover
        return UpdateKinesisStreamingConfiguration.make_one(
            self.boto3_raw_data["UpdateKinesisStreamingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKinesisStreamingDestinationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKinesisStreamingDestinationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKinesisStreamingDestinationOutput:
    boto3_raw_data: "type_defs.UpdateKinesisStreamingDestinationOutputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")
    StreamArn = field("StreamArn")
    DestinationStatus = field("DestinationStatus")

    @cached_property
    def UpdateKinesisStreamingConfiguration(self):  # pragma: no cover
        return UpdateKinesisStreamingConfiguration.make_one(
            self.boto3_raw_data["UpdateKinesisStreamingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKinesisStreamingDestinationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKinesisStreamingDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStatementResponse:
    boto3_raw_data: "type_defs.BatchStatementResponseTypeDef" = dataclasses.field()

    @cached_property
    def Error(self):  # pragma: no cover
        return BatchStatementError.make_one(self.boto3_raw_data["Error"])

    TableName = field("TableName")
    Item = field("Item")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchStatementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteRequestOutput:
    boto3_raw_data: "type_defs.WriteRequestOutputTypeDef" = dataclasses.field()

    @cached_property
    def PutRequest(self):  # pragma: no cover
        return PutRequestOutput.make_one(self.boto3_raw_data["PutRequest"])

    @cached_property
    def DeleteRequest(self):  # pragma: no cover
        return DeleteRequestOutput.make_one(self.boto3_raw_data["DeleteRequest"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteRequestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValueUpdate:
    boto3_raw_data: "type_defs.AttributeValueUpdateTypeDef" = dataclasses.field()

    Value = field("Value")
    Action = field("Action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStatementRequest:
    boto3_raw_data: "type_defs.BatchStatementRequestTypeDef" = dataclasses.field()

    Statement = field("Statement")
    Parameters = field("Parameters")
    ConsistentRead = field("ConsistentRead")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchStatementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStatementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionCheck:
    boto3_raw_data: "type_defs.ConditionCheckTypeDef" = dataclasses.field()

    Key = field("Key")
    TableName = field("TableName")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionCheckTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionCheckTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    AttributeValueList = field("AttributeValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRequest:
    boto3_raw_data: "type_defs.DeleteRequestTypeDef" = dataclasses.field()

    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Delete:
    boto3_raw_data: "type_defs.DeleteTypeDef" = dataclasses.field()

    Key = field("Key")
    TableName = field("TableName")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementInput:
    boto3_raw_data: "type_defs.ExecuteStatementInputTypeDef" = dataclasses.field()

    Statement = field("Statement")
    Parameters = field("Parameters")
    ConsistentRead = field("ConsistentRead")
    NextToken = field("NextToken")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    Limit = field("Limit")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpectedAttributeValue:
    boto3_raw_data: "type_defs.ExpectedAttributeValueTypeDef" = dataclasses.field()

    Value = field("Value")
    Exists = field("Exists")
    ComparisonOperator = field("ComparisonOperator")
    AttributeValueList = field("AttributeValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpectedAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpectedAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetItemInput:
    boto3_raw_data: "type_defs.GetItemInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    Key = field("Key")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetItemInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetItemInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Get:
    boto3_raw_data: "type_defs.GetTypeDef" = dataclasses.field()

    Key = field("Key")
    TableName = field("TableName")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeysAndAttributes:
    boto3_raw_data: "type_defs.KeysAndAttributesTypeDef" = dataclasses.field()

    Keys = field("Keys")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    ProjectionExpression = field("ProjectionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeysAndAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeysAndAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterizedStatement:
    boto3_raw_data: "type_defs.ParameterizedStatementTypeDef" = dataclasses.field()

    Statement = field("Statement")
    Parameters = field("Parameters")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterizedStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterizedStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRequest:
    boto3_raw_data: "type_defs.PutRequestTypeDef" = dataclasses.field()

    Item = field("Item")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Put:
    boto3_raw_data: "type_defs.PutTypeDef" = dataclasses.field()

    Item = field("Item")
    TableName = field("TableName")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Update:
    boto3_raw_data: "type_defs.UpdateTypeDef" = dataclasses.field()

    Key = field("Key")
    UpdateExpression = field("UpdateExpression")
    TableName = field("TableName")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInputTableQuery:
    boto3_raw_data: "type_defs.QueryInputTableQueryTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    Select = field("Select")
    AttributesToGet = field("AttributesToGet")
    Limit = field("Limit")
    ConsistentRead = field("ConsistentRead")
    KeyConditions = field("KeyConditions")
    QueryFilter = field("QueryFilter")
    ConditionalOperator = field("ConditionalOperator")
    ScanIndexForward = field("ScanIndexForward")
    ExclusiveStartKey = field("ExclusiveStartKey")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ProjectionExpression = field("ProjectionExpression")
    FilterExpression = field("FilterExpression")
    KeyConditionExpression = field("KeyConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryInputTableQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryInputTableQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanInputTableScan:
    boto3_raw_data: "type_defs.ScanInputTableScanTypeDef" = dataclasses.field()

    IndexName = field("IndexName")
    AttributesToGet = field("AttributesToGet")
    Limit = field("Limit")
    Select = field("Select")
    ScanFilter = field("ScanFilter")
    ConditionalOperator = field("ConditionalOperator")
    ExclusiveStartKey = field("ExclusiveStartKey")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    TotalSegments = field("TotalSegments")
    Segment = field("Segment")
    ProjectionExpression = field("ProjectionExpression")
    FilterExpression = field("FilterExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ConsistentRead = field("ConsistentRead")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanInputTableScanTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanInputTableScanTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteItemInputTableDeleteItem:
    boto3_raw_data: "type_defs.DeleteItemInputTableDeleteItemTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Expected = field("Expected")
    ConditionalOperator = field("ConditionalOperator")
    ReturnValues = field("ReturnValues")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteItemInputTableDeleteItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteItemInputTableDeleteItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutItemInputTablePutItem:
    boto3_raw_data: "type_defs.PutItemInputTablePutItemTypeDef" = dataclasses.field()

    Item = field("Item")
    Expected = field("Expected")
    ReturnValues = field("ReturnValues")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    ConditionalOperator = field("ConditionalOperator")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutItemInputTablePutItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutItemInputTablePutItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateItemInputTableUpdateItem:
    boto3_raw_data: "type_defs.UpdateItemInputTableUpdateItemTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    AttributeUpdates = field("AttributeUpdates")
    Expected = field("Expected")
    ConditionalOperator = field("ConditionalOperator")
    ReturnValues = field("ReturnValues")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    UpdateExpression = field("UpdateExpression")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateItemInputTableUpdateItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateItemInputTableUpdateItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteRequestServiceResourceOutput:
    boto3_raw_data: "type_defs.WriteRequestServiceResourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PutRequest(self):  # pragma: no cover
        return PutRequestServiceResourceOutput.make_one(
            self.boto3_raw_data["PutRequest"]
        )

    @cached_property
    def DeleteRequest(self):  # pragma: no cover
        return DeleteRequestServiceResourceOutput.make_one(
            self.boto3_raw_data["DeleteRequest"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WriteRequestServiceResourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteRequestServiceResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingSettingsDescription:
    boto3_raw_data: "type_defs.AutoScalingSettingsDescriptionTypeDef" = (
        dataclasses.field()
    )

    MinimumUnits = field("MinimumUnits")
    MaximumUnits = field("MaximumUnits")
    AutoScalingDisabled = field("AutoScalingDisabled")
    AutoScalingRoleArn = field("AutoScalingRoleArn")

    @cached_property
    def ScalingPolicies(self):  # pragma: no cover
        return AutoScalingPolicyDescription.make_many(
            self.boto3_raw_data["ScalingPolicies"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoScalingSettingsDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingSettingsUpdate:
    boto3_raw_data: "type_defs.AutoScalingSettingsUpdateTypeDef" = dataclasses.field()

    MinimumUnits = field("MinimumUnits")
    MaximumUnits = field("MaximumUnits")
    AutoScalingDisabled = field("AutoScalingDisabled")
    AutoScalingRoleArn = field("AutoScalingRoleArn")

    @cached_property
    def ScalingPolicyUpdate(self):  # pragma: no cover
        return AutoScalingPolicyUpdate.make_one(
            self.boto3_raw_data["ScalingPolicyUpdate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingSettingsUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingSettingsUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetItemOutputServiceResource:
    boto3_raw_data: "type_defs.BatchGetItemOutputServiceResourceTypeDef" = (
        dataclasses.field()
    )

    Responses = field("Responses")
    UnprocessedKeys = field("UnprocessedKeys")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetItemOutputServiceResourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetItemOutputServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetItemOutput:
    boto3_raw_data: "type_defs.BatchGetItemOutputTypeDef" = dataclasses.field()

    Responses = field("Responses")
    UnprocessedKeys = field("UnprocessedKeys")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteItemOutputTable:
    boto3_raw_data: "type_defs.DeleteItemOutputTableTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ItemCollectionMetrics(self):  # pragma: no cover
        return ItemCollectionMetricsTable.make_one(
            self.boto3_raw_data["ItemCollectionMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteItemOutputTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteItemOutputTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteItemOutput:
    boto3_raw_data: "type_defs.DeleteItemOutputTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ItemCollectionMetrics(self):  # pragma: no cover
        return ItemCollectionMetrics.make_one(
            self.boto3_raw_data["ItemCollectionMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteItemOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStatementOutput:
    boto3_raw_data: "type_defs.ExecuteStatementOutputTypeDef" = dataclasses.field()

    Items = field("Items")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")
    LastEvaluatedKey = field("LastEvaluatedKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteTransactionOutput:
    boto3_raw_data: "type_defs.ExecuteTransactionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Responses(self):  # pragma: no cover
        return ItemResponse.make_many(self.boto3_raw_data["Responses"])

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteTransactionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteTransactionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetItemOutputTable:
    boto3_raw_data: "type_defs.GetItemOutputTableTypeDef" = dataclasses.field()

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    Item = field("Item")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetItemOutputTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetItemOutputTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetItemOutput:
    boto3_raw_data: "type_defs.GetItemOutputTypeDef" = dataclasses.field()

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    Item = field("Item")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetItemOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetItemOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutItemOutputTable:
    boto3_raw_data: "type_defs.PutItemOutputTableTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ItemCollectionMetrics(self):  # pragma: no cover
        return ItemCollectionMetricsTable.make_one(
            self.boto3_raw_data["ItemCollectionMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutItemOutputTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutItemOutputTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutItemOutput:
    boto3_raw_data: "type_defs.PutItemOutputTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ItemCollectionMetrics(self):  # pragma: no cover
        return ItemCollectionMetrics.make_one(
            self.boto3_raw_data["ItemCollectionMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutItemOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutItemOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryOutputTable:
    boto3_raw_data: "type_defs.QueryOutputTableTypeDef" = dataclasses.field()

    Items = field("Items")
    Count = field("Count")
    ScannedCount = field("ScannedCount")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    LastEvaluatedKey = field("LastEvaluatedKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryOutputTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryOutputTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryOutput:
    boto3_raw_data: "type_defs.QueryOutputTypeDef" = dataclasses.field()

    Items = field("Items")
    Count = field("Count")
    ScannedCount = field("ScannedCount")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    LastEvaluatedKey = field("LastEvaluatedKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanOutputTable:
    boto3_raw_data: "type_defs.ScanOutputTableTypeDef" = dataclasses.field()

    Items = field("Items")
    Count = field("Count")
    ScannedCount = field("ScannedCount")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    LastEvaluatedKey = field("LastEvaluatedKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanOutputTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanOutputTableTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanOutput:
    boto3_raw_data: "type_defs.ScanOutputTypeDef" = dataclasses.field()

    Items = field("Items")
    Count = field("Count")
    ScannedCount = field("ScannedCount")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    LastEvaluatedKey = field("LastEvaluatedKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactGetItemsOutput:
    boto3_raw_data: "type_defs.TransactGetItemsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def Responses(self):  # pragma: no cover
        return ItemResponse.make_many(self.boto3_raw_data["Responses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransactGetItemsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactGetItemsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactWriteItemsOutput:
    boto3_raw_data: "type_defs.TransactWriteItemsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    ItemCollectionMetrics = field("ItemCollectionMetrics")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransactWriteItemsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactWriteItemsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateItemOutputTable:
    boto3_raw_data: "type_defs.UpdateItemOutputTableTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ItemCollectionMetrics(self):  # pragma: no cover
        return ItemCollectionMetricsTable.make_one(
            self.boto3_raw_data["ItemCollectionMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateItemOutputTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateItemOutputTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateItemOutput:
    boto3_raw_data: "type_defs.UpdateItemOutputTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_one(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ItemCollectionMetrics(self):  # pragma: no cover
        return ItemCollectionMetrics.make_one(
            self.boto3_raw_data["ItemCollectionMetrics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateItemOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContinuousBackupsOutput:
    boto3_raw_data: "type_defs.DescribeContinuousBackupsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousBackupsDescription(self):  # pragma: no cover
        return ContinuousBackupsDescription.make_one(
            self.boto3_raw_data["ContinuousBackupsDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeContinuousBackupsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContinuousBackupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContinuousBackupsOutput:
    boto3_raw_data: "type_defs.UpdateContinuousBackupsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContinuousBackupsDescription(self):  # pragma: no cover
        return ContinuousBackupsDescription.make_one(
            self.boto3_raw_data["ContinuousBackupsDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContinuousBackupsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContinuousBackupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGlobalTablesOutput:
    boto3_raw_data: "type_defs.ListGlobalTablesOutputTypeDef" = dataclasses.field()

    @cached_property
    def GlobalTables(self):  # pragma: no cover
        return GlobalTable.make_many(self.boto3_raw_data["GlobalTables"])

    LastEvaluatedGlobalTableName = field("LastEvaluatedGlobalTableName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGlobalTablesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGlobalTablesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationGroupMemberAction:
    boto3_raw_data: "type_defs.CreateReplicationGroupMemberActionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")
    KMSMasterKeyId = field("KMSMasterKeyId")

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughputOverride.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughputOverride.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndex.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    TableClassOverride = field("TableClassOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationGroupMemberActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationGroupMemberActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReplicationGroupMemberAction:
    boto3_raw_data: "type_defs.UpdateReplicationGroupMemberActionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")
    KMSMasterKeyId = field("KMSMasterKeyId")

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughputOverride.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughputOverride.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndex.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    TableClassOverride = field("TableClassOverride")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReplicationGroupMemberActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationGroupMemberActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalTableInput:
    boto3_raw_data: "type_defs.UpdateGlobalTableInputTypeDef" = dataclasses.field()

    GlobalTableName = field("GlobalTableName")

    @cached_property
    def ReplicaUpdates(self):  # pragma: no cover
        return ReplicaUpdate.make_many(self.boto3_raw_data["ReplicaUpdates"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportOutput:
    boto3_raw_data: "type_defs.DescribeExportOutputTypeDef" = dataclasses.field()

    @cached_property
    def ExportDescription(self):  # pragma: no cover
        return ExportDescription.make_one(self.boto3_raw_data["ExportDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTableToPointInTimeOutput:
    boto3_raw_data: "type_defs.ExportTableToPointInTimeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExportDescription(self):  # pragma: no cover
        return ExportDescription.make_one(self.boto3_raw_data["ExportDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportTableToPointInTimeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTableToPointInTimeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaDescription:
    boto3_raw_data: "type_defs.ReplicaDescriptionTypeDef" = dataclasses.field()

    RegionName = field("RegionName")
    ReplicaStatus = field("ReplicaStatus")
    ReplicaStatusDescription = field("ReplicaStatusDescription")
    ReplicaStatusPercentProgress = field("ReplicaStatusPercentProgress")
    KMSMasterKeyId = field("KMSMasterKeyId")

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughputOverride.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughputOverride.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return TableWarmThroughputDescription.make_one(
            self.boto3_raw_data["WarmThroughput"]
        )

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndexDescription.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    ReplicaInaccessibleDateTime = field("ReplicaInaccessibleDateTime")

    @cached_property
    def ReplicaTableClassSummary(self):  # pragma: no cover
        return TableClassSummary.make_one(
            self.boto3_raw_data["ReplicaTableClassSummary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableCreationParametersOutput:
    boto3_raw_data: "type_defs.TableCreationParametersOutputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    BillingMode = field("BillingMode")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def SSESpecification(self):  # pragma: no cover
        return SSESpecification.make_one(self.boto3_raw_data["SSESpecification"])

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return GlobalSecondaryIndexOutput.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TableCreationParametersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableCreationParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceTableFeatureDetails:
    boto3_raw_data: "type_defs.SourceTableFeatureDetailsTypeDef" = dataclasses.field()

    @cached_property
    def LocalSecondaryIndexes(self):  # pragma: no cover
        return LocalSecondaryIndexInfo.make_many(
            self.boto3_raw_data["LocalSecondaryIndexes"]
        )

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return GlobalSecondaryIndexInfo.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    @cached_property
    def StreamDescription(self):  # pragma: no cover
        return StreamSpecification.make_one(self.boto3_raw_data["StreamDescription"])

    @cached_property
    def TimeToLiveDescription(self):  # pragma: no cover
        return TimeToLiveDescription.make_one(
            self.boto3_raw_data["TimeToLiveDescription"]
        )

    @cached_property
    def SSEDescription(self):  # pragma: no cover
        return SSEDescription.make_one(self.boto3_raw_data["SSEDescription"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceTableFeatureDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceTableFeatureDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsOutput:
    boto3_raw_data: "type_defs.ListImportsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ImportSummaryList(self):  # pragma: no cover
        return ImportSummary.make_many(self.boto3_raw_data["ImportSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImportsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalSecondaryIndexAction:
    boto3_raw_data: "type_defs.CreateGlobalSecondaryIndexActionTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    Projection = field("Projection")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGlobalSecondaryIndexActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalSecondaryIndexActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndex:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    Projection = field("Projection")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalSecondaryIndexTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalSecondaryIndex:
    boto3_raw_data: "type_defs.LocalSecondaryIndexTypeDef" = dataclasses.field()

    IndexName = field("IndexName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    Projection = field("Projection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LocalSecondaryIndexTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalSecondaryIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchExecuteStatementOutput:
    boto3_raw_data: "type_defs.BatchExecuteStatementOutputTypeDef" = dataclasses.field()

    @cached_property
    def Responses(self):  # pragma: no cover
        return BatchStatementResponse.make_many(self.boto3_raw_data["Responses"])

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchExecuteStatementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchExecuteStatementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteItemOutput:
    boto3_raw_data: "type_defs.BatchWriteItemOutputTypeDef" = dataclasses.field()

    UnprocessedItems = field("UnprocessedItems")
    ItemCollectionMetrics = field("ItemCollectionMetrics")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchWriteItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchExecuteStatementInput:
    boto3_raw_data: "type_defs.BatchExecuteStatementInputTypeDef" = dataclasses.field()

    @cached_property
    def Statements(self):  # pragma: no cover
        return BatchStatementRequest.make_many(self.boto3_raw_data["Statements"])

    ReturnConsumedCapacity = field("ReturnConsumedCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchExecuteStatementInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchExecuteStatementInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInputPaginate:
    boto3_raw_data: "type_defs.QueryInputPaginateTypeDef" = dataclasses.field()

    TableName = field("TableName")
    IndexName = field("IndexName")
    Select = field("Select")
    AttributesToGet = field("AttributesToGet")
    ConsistentRead = field("ConsistentRead")
    KeyConditions = field("KeyConditions")
    QueryFilter = field("QueryFilter")
    ConditionalOperator = field("ConditionalOperator")
    ScanIndexForward = field("ScanIndexForward")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ProjectionExpression = field("ProjectionExpression")
    FilterExpression = field("FilterExpression")
    KeyConditionExpression = field("KeyConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInput:
    boto3_raw_data: "type_defs.QueryInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    IndexName = field("IndexName")
    Select = field("Select")
    AttributesToGet = field("AttributesToGet")
    Limit = field("Limit")
    ConsistentRead = field("ConsistentRead")
    KeyConditions = field("KeyConditions")
    QueryFilter = field("QueryFilter")
    ConditionalOperator = field("ConditionalOperator")
    ScanIndexForward = field("ScanIndexForward")
    ExclusiveStartKey = field("ExclusiveStartKey")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ProjectionExpression = field("ProjectionExpression")
    FilterExpression = field("FilterExpression")
    KeyConditionExpression = field("KeyConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanInputPaginate:
    boto3_raw_data: "type_defs.ScanInputPaginateTypeDef" = dataclasses.field()

    TableName = field("TableName")
    IndexName = field("IndexName")
    AttributesToGet = field("AttributesToGet")
    Select = field("Select")
    ScanFilter = field("ScanFilter")
    ConditionalOperator = field("ConditionalOperator")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    TotalSegments = field("TotalSegments")
    Segment = field("Segment")
    ProjectionExpression = field("ProjectionExpression")
    FilterExpression = field("FilterExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ConsistentRead = field("ConsistentRead")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanInputPaginateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanInput:
    boto3_raw_data: "type_defs.ScanInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    IndexName = field("IndexName")
    AttributesToGet = field("AttributesToGet")
    Limit = field("Limit")
    Select = field("Select")
    ScanFilter = field("ScanFilter")
    ConditionalOperator = field("ConditionalOperator")
    ExclusiveStartKey = field("ExclusiveStartKey")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    TotalSegments = field("TotalSegments")
    Segment = field("Segment")
    ProjectionExpression = field("ProjectionExpression")
    FilterExpression = field("FilterExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ConsistentRead = field("ConsistentRead")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteItemInput:
    boto3_raw_data: "type_defs.DeleteItemInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    Key = field("Key")
    Expected = field("Expected")
    ConditionalOperator = field("ConditionalOperator")
    ReturnValues = field("ReturnValues")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteItemInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteItemInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutItemInput:
    boto3_raw_data: "type_defs.PutItemInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    Item = field("Item")
    Expected = field("Expected")
    ReturnValues = field("ReturnValues")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    ConditionalOperator = field("ConditionalOperator")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutItemInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutItemInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateItemInput:
    boto3_raw_data: "type_defs.UpdateItemInputTypeDef" = dataclasses.field()

    TableName = field("TableName")
    Key = field("Key")
    AttributeUpdates = field("AttributeUpdates")
    Expected = field("Expected")
    ConditionalOperator = field("ConditionalOperator")
    ReturnValues = field("ReturnValues")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    UpdateExpression = field("UpdateExpression")
    ConditionExpression = field("ConditionExpression")
    ExpressionAttributeNames = field("ExpressionAttributeNames")
    ExpressionAttributeValues = field("ExpressionAttributeValues")
    ReturnValuesOnConditionCheckFailure = field("ReturnValuesOnConditionCheckFailure")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateItemInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateItemInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactGetItem:
    boto3_raw_data: "type_defs.TransactGetItemTypeDef" = dataclasses.field()

    @cached_property
    def Get(self):  # pragma: no cover
        return Get.make_one(self.boto3_raw_data["Get"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransactGetItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransactGetItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteTransactionInput:
    boto3_raw_data: "type_defs.ExecuteTransactionInputTypeDef" = dataclasses.field()

    @cached_property
    def TransactStatements(self):  # pragma: no cover
        return ParameterizedStatement.make_many(
            self.boto3_raw_data["TransactStatements"]
        )

    ClientRequestToken = field("ClientRequestToken")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteTransactionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteTransactionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactWriteItem:
    boto3_raw_data: "type_defs.TransactWriteItemTypeDef" = dataclasses.field()

    @cached_property
    def ConditionCheck(self):  # pragma: no cover
        return ConditionCheck.make_one(self.boto3_raw_data["ConditionCheck"])

    @cached_property
    def Put(self):  # pragma: no cover
        return Put.make_one(self.boto3_raw_data["Put"])

    @cached_property
    def Delete(self):  # pragma: no cover
        return Delete.make_one(self.boto3_raw_data["Delete"])

    @cached_property
    def Update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["Update"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransactWriteItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactWriteItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetItemInputServiceResourceBatchGetItem:
    boto3_raw_data: "type_defs.BatchGetItemInputServiceResourceBatchGetItemTypeDef" = (
        dataclasses.field()
    )

    RequestItems = field("RequestItems")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetItemInputServiceResourceBatchGetItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetItemInputServiceResourceBatchGetItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteItemOutputServiceResource:
    boto3_raw_data: "type_defs.BatchWriteItemOutputServiceResourceTypeDef" = (
        dataclasses.field()
    )

    UnprocessedItems = field("UnprocessedItems")
    ItemCollectionMetrics = field("ItemCollectionMetrics")

    @cached_property
    def ConsumedCapacity(self):  # pragma: no cover
        return ConsumedCapacity.make_many(self.boto3_raw_data["ConsumedCapacity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchWriteItemOutputServiceResourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteItemOutputServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteRequestServiceResource:
    boto3_raw_data: "type_defs.WriteRequestServiceResourceTypeDef" = dataclasses.field()

    PutRequest = field("PutRequest")
    DeleteRequest = field("DeleteRequest")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WriteRequestServiceResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteRequestServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaGlobalSecondaryIndexAutoScalingDescription:
    boto3_raw_data: (
        "type_defs.ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"
    ) = dataclasses.field()

    IndexName = field("IndexName")
    IndexStatus = field("IndexStatus")

    @cached_property
    def ProvisionedReadCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ProvisionedReadCapacityAutoScalingSettings"]
        )

    @cached_property
    def ProvisionedWriteCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ProvisionedWriteCapacityAutoScalingSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"
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
                "type_defs.ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaGlobalSecondaryIndexSettingsDescription:
    boto3_raw_data: (
        "type_defs.ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
    ) = dataclasses.field()

    IndexName = field("IndexName")
    IndexStatus = field("IndexStatus")
    ProvisionedReadCapacityUnits = field("ProvisionedReadCapacityUnits")

    @cached_property
    def ProvisionedReadCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ProvisionedReadCapacityAutoScalingSettings"]
        )

    ProvisionedWriteCapacityUnits = field("ProvisionedWriteCapacityUnits")

    @cached_property
    def ProvisionedWriteCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ProvisionedWriteCapacityAutoScalingSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
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
                "type_defs.ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndexAutoScalingUpdate:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexAutoScalingUpdateTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def ProvisionedWriteCapacityAutoScalingUpdate(self):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data["ProvisionedWriteCapacityAutoScalingUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GlobalSecondaryIndexAutoScalingUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexAutoScalingUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalTableGlobalSecondaryIndexSettingsUpdate:
    boto3_raw_data: "type_defs.GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")
    ProvisionedWriteCapacityUnits = field("ProvisionedWriteCapacityUnits")

    @cached_property
    def ProvisionedWriteCapacityAutoScalingSettingsUpdate(self):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data["ProvisionedWriteCapacityAutoScalingSettingsUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaGlobalSecondaryIndexAutoScalingUpdate:
    boto3_raw_data: "type_defs.ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")

    @cached_property
    def ProvisionedReadCapacityAutoScalingUpdate(self):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data["ProvisionedReadCapacityAutoScalingUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaGlobalSecondaryIndexSettingsUpdate:
    boto3_raw_data: "type_defs.ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef" = (
        dataclasses.field()
    )

    IndexName = field("IndexName")
    ProvisionedReadCapacityUnits = field("ProvisionedReadCapacityUnits")

    @cached_property
    def ProvisionedReadCapacityAutoScalingSettingsUpdate(self):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data["ProvisionedReadCapacityAutoScalingSettingsUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationGroupUpdate:
    boto3_raw_data: "type_defs.ReplicationGroupUpdateTypeDef" = dataclasses.field()

    @cached_property
    def Create(self):  # pragma: no cover
        return CreateReplicationGroupMemberAction.make_one(
            self.boto3_raw_data["Create"]
        )

    @cached_property
    def Update(self):  # pragma: no cover
        return UpdateReplicationGroupMemberAction.make_one(
            self.boto3_raw_data["Update"]
        )

    @cached_property
    def Delete(self):  # pragma: no cover
        return DeleteReplicationGroupMemberAction.make_one(
            self.boto3_raw_data["Delete"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationGroupUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationGroupUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTableToPointInTimeInput:
    boto3_raw_data: "type_defs.ExportTableToPointInTimeInputTypeDef" = (
        dataclasses.field()
    )

    TableArn = field("TableArn")
    S3Bucket = field("S3Bucket")
    ExportTime = field("ExportTime")
    ClientToken = field("ClientToken")
    S3BucketOwner = field("S3BucketOwner")
    S3Prefix = field("S3Prefix")
    S3SseAlgorithm = field("S3SseAlgorithm")
    S3SseKmsKeyId = field("S3SseKmsKeyId")
    ExportFormat = field("ExportFormat")
    ExportType = field("ExportType")
    IncrementalExportSpecification = field("IncrementalExportSpecification")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportTableToPointInTimeInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTableToPointInTimeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalTableDescription:
    boto3_raw_data: "type_defs.GlobalTableDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationGroup(self):  # pragma: no cover
        return ReplicaDescription.make_many(self.boto3_raw_data["ReplicationGroup"])

    GlobalTableArn = field("GlobalTableArn")
    CreationDateTime = field("CreationDateTime")
    GlobalTableStatus = field("GlobalTableStatus")
    GlobalTableName = field("GlobalTableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalTableDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalTableDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableDescription:
    boto3_raw_data: "type_defs.TableDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    TableName = field("TableName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    TableStatus = field("TableStatus")
    CreationDateTime = field("CreationDateTime")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughputDescription.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    TableSizeBytes = field("TableSizeBytes")
    ItemCount = field("ItemCount")
    TableArn = field("TableArn")
    TableId = field("TableId")

    @cached_property
    def BillingModeSummary(self):  # pragma: no cover
        return BillingModeSummary.make_one(self.boto3_raw_data["BillingModeSummary"])

    @cached_property
    def LocalSecondaryIndexes(self):  # pragma: no cover
        return LocalSecondaryIndexDescription.make_many(
            self.boto3_raw_data["LocalSecondaryIndexes"]
        )

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return GlobalSecondaryIndexDescription.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    @cached_property
    def StreamSpecification(self):  # pragma: no cover
        return StreamSpecification.make_one(self.boto3_raw_data["StreamSpecification"])

    LatestStreamLabel = field("LatestStreamLabel")
    LatestStreamArn = field("LatestStreamArn")
    GlobalTableVersion = field("GlobalTableVersion")

    @cached_property
    def Replicas(self):  # pragma: no cover
        return ReplicaDescription.make_many(self.boto3_raw_data["Replicas"])

    @cached_property
    def GlobalTableWitnesses(self):  # pragma: no cover
        return GlobalTableWitnessDescription.make_many(
            self.boto3_raw_data["GlobalTableWitnesses"]
        )

    @cached_property
    def RestoreSummary(self):  # pragma: no cover
        return RestoreSummary.make_one(self.boto3_raw_data["RestoreSummary"])

    @cached_property
    def SSEDescription(self):  # pragma: no cover
        return SSEDescription.make_one(self.boto3_raw_data["SSEDescription"])

    @cached_property
    def ArchivalSummary(self):  # pragma: no cover
        return ArchivalSummary.make_one(self.boto3_raw_data["ArchivalSummary"])

    @cached_property
    def TableClassSummary(self):  # pragma: no cover
        return TableClassSummary.make_one(self.boto3_raw_data["TableClassSummary"])

    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return TableWarmThroughputDescription.make_one(
            self.boto3_raw_data["WarmThroughput"]
        )

    MultiRegionConsistency = field("MultiRegionConsistency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTableDescription:
    boto3_raw_data: "type_defs.ImportTableDescriptionTypeDef" = dataclasses.field()

    ImportArn = field("ImportArn")
    ImportStatus = field("ImportStatus")
    TableArn = field("TableArn")
    TableId = field("TableId")
    ClientToken = field("ClientToken")

    @cached_property
    def S3BucketSource(self):  # pragma: no cover
        return S3BucketSource.make_one(self.boto3_raw_data["S3BucketSource"])

    ErrorCount = field("ErrorCount")
    CloudWatchLogGroupArn = field("CloudWatchLogGroupArn")
    InputFormat = field("InputFormat")

    @cached_property
    def InputFormatOptions(self):  # pragma: no cover
        return InputFormatOptionsOutput.make_one(
            self.boto3_raw_data["InputFormatOptions"]
        )

    InputCompressionType = field("InputCompressionType")

    @cached_property
    def TableCreationParameters(self):  # pragma: no cover
        return TableCreationParametersOutput.make_one(
            self.boto3_raw_data["TableCreationParameters"]
        )

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ProcessedSizeBytes = field("ProcessedSizeBytes")
    ProcessedItemCount = field("ProcessedItemCount")
    ImportedItemCount = field("ImportedItemCount")
    FailureCode = field("FailureCode")
    FailureMessage = field("FailureMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportTableDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTableDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupDescription:
    boto3_raw_data: "type_defs.BackupDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def BackupDetails(self):  # pragma: no cover
        return BackupDetails.make_one(self.boto3_raw_data["BackupDetails"])

    @cached_property
    def SourceTableDetails(self):  # pragma: no cover
        return SourceTableDetails.make_one(self.boto3_raw_data["SourceTableDetails"])

    @cached_property
    def SourceTableFeatureDetails(self):  # pragma: no cover
        return SourceTableFeatureDetails.make_one(
            self.boto3_raw_data["SourceTableFeatureDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalSecondaryIndexUpdate:
    boto3_raw_data: "type_defs.GlobalSecondaryIndexUpdateTypeDef" = dataclasses.field()

    @cached_property
    def Update(self):  # pragma: no cover
        return UpdateGlobalSecondaryIndexAction.make_one(self.boto3_raw_data["Update"])

    @cached_property
    def Create(self):  # pragma: no cover
        return CreateGlobalSecondaryIndexAction.make_one(self.boto3_raw_data["Create"])

    @cached_property
    def Delete(self):  # pragma: no cover
        return DeleteGlobalSecondaryIndexAction.make_one(self.boto3_raw_data["Delete"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlobalSecondaryIndexUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalSecondaryIndexUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableCreationParameters:
    boto3_raw_data: "type_defs.TableCreationParametersTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    BillingMode = field("BillingMode")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def SSESpecification(self):  # pragma: no cover
        return SSESpecification.make_one(self.boto3_raw_data["SSESpecification"])

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return GlobalSecondaryIndex.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableCreationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableCreationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactGetItemsInput:
    boto3_raw_data: "type_defs.TransactGetItemsInputTypeDef" = dataclasses.field()

    @cached_property
    def TransactItems(self):  # pragma: no cover
        return TransactGetItem.make_many(self.boto3_raw_data["TransactItems"])

    ReturnConsumedCapacity = field("ReturnConsumedCapacity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransactGetItemsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactGetItemsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetItemInput:
    boto3_raw_data: "type_defs.BatchGetItemInputTypeDef" = dataclasses.field()

    RequestItems = field("RequestItems")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchGetItemInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteRequest:
    boto3_raw_data: "type_defs.WriteRequestTypeDef" = dataclasses.field()

    PutRequest = field("PutRequest")
    DeleteRequest = field("DeleteRequest")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WriteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WriteRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransactWriteItemsInput:
    boto3_raw_data: "type_defs.TransactWriteItemsInputTypeDef" = dataclasses.field()

    @cached_property
    def TransactItems(self):  # pragma: no cover
        return TransactWriteItem.make_many(self.boto3_raw_data["TransactItems"])

    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransactWriteItemsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransactWriteItemsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaAutoScalingDescription:
    boto3_raw_data: "type_defs.ReplicaAutoScalingDescriptionTypeDef" = (
        dataclasses.field()
    )

    RegionName = field("RegionName")

    @cached_property
    def GlobalSecondaryIndexes(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndexAutoScalingDescription.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexes"]
        )

    @cached_property
    def ReplicaProvisionedReadCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ReplicaProvisionedReadCapacityAutoScalingSettings"]
        )

    @cached_property
    def ReplicaProvisionedWriteCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ReplicaProvisionedWriteCapacityAutoScalingSettings"]
        )

    ReplicaStatus = field("ReplicaStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicaAutoScalingDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaAutoScalingDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaSettingsDescription:
    boto3_raw_data: "type_defs.ReplicaSettingsDescriptionTypeDef" = dataclasses.field()

    RegionName = field("RegionName")
    ReplicaStatus = field("ReplicaStatus")

    @cached_property
    def ReplicaBillingModeSummary(self):  # pragma: no cover
        return BillingModeSummary.make_one(
            self.boto3_raw_data["ReplicaBillingModeSummary"]
        )

    ReplicaProvisionedReadCapacityUnits = field("ReplicaProvisionedReadCapacityUnits")

    @cached_property
    def ReplicaProvisionedReadCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ReplicaProvisionedReadCapacityAutoScalingSettings"]
        )

    ReplicaProvisionedWriteCapacityUnits = field("ReplicaProvisionedWriteCapacityUnits")

    @cached_property
    def ReplicaProvisionedWriteCapacityAutoScalingSettings(self):  # pragma: no cover
        return AutoScalingSettingsDescription.make_one(
            self.boto3_raw_data["ReplicaProvisionedWriteCapacityAutoScalingSettings"]
        )

    @cached_property
    def ReplicaGlobalSecondaryIndexSettings(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndexSettingsDescription.make_many(
            self.boto3_raw_data["ReplicaGlobalSecondaryIndexSettings"]
        )

    @cached_property
    def ReplicaTableClassSummary(self):  # pragma: no cover
        return TableClassSummary.make_one(
            self.boto3_raw_data["ReplicaTableClassSummary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaSettingsDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaAutoScalingUpdate:
    boto3_raw_data: "type_defs.ReplicaAutoScalingUpdateTypeDef" = dataclasses.field()

    RegionName = field("RegionName")

    @cached_property
    def ReplicaGlobalSecondaryIndexUpdates(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndexAutoScalingUpdate.make_many(
            self.boto3_raw_data["ReplicaGlobalSecondaryIndexUpdates"]
        )

    @cached_property
    def ReplicaProvisionedReadCapacityAutoScalingUpdate(self):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data["ReplicaProvisionedReadCapacityAutoScalingUpdate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaAutoScalingUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaAutoScalingUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaSettingsUpdate:
    boto3_raw_data: "type_defs.ReplicaSettingsUpdateTypeDef" = dataclasses.field()

    RegionName = field("RegionName")
    ReplicaProvisionedReadCapacityUnits = field("ReplicaProvisionedReadCapacityUnits")

    @cached_property
    def ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate(
        self,
    ):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data[
                "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"
            ]
        )

    @cached_property
    def ReplicaGlobalSecondaryIndexSettingsUpdate(self):  # pragma: no cover
        return ReplicaGlobalSecondaryIndexSettingsUpdate.make_many(
            self.boto3_raw_data["ReplicaGlobalSecondaryIndexSettingsUpdate"]
        )

    ReplicaTableClass = field("ReplicaTableClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaSettingsUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaSettingsUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlobalTableOutput:
    boto3_raw_data: "type_defs.CreateGlobalTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def GlobalTableDescription(self):  # pragma: no cover
        return GlobalTableDescription.make_one(
            self.boto3_raw_data["GlobalTableDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlobalTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlobalTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalTableOutput:
    boto3_raw_data: "type_defs.DescribeGlobalTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def GlobalTableDescription(self):  # pragma: no cover
        return GlobalTableDescription.make_one(
            self.boto3_raw_data["GlobalTableDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGlobalTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalTableOutput:
    boto3_raw_data: "type_defs.UpdateGlobalTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def GlobalTableDescription(self):  # pragma: no cover
        return GlobalTableDescription.make_one(
            self.boto3_raw_data["GlobalTableDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableOutput:
    boto3_raw_data: "type_defs.CreateTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def TableDescription(self):  # pragma: no cover
        return TableDescription.make_one(self.boto3_raw_data["TableDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTableOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTableOutput:
    boto3_raw_data: "type_defs.DeleteTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def TableDescription(self):  # pragma: no cover
        return TableDescription.make_one(self.boto3_raw_data["TableDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTableOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableOutput:
    boto3_raw_data: "type_defs.DescribeTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def Table(self):  # pragma: no cover
        return TableDescription.make_one(self.boto3_raw_data["Table"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromBackupOutput:
    boto3_raw_data: "type_defs.RestoreTableFromBackupOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TableDescription(self):  # pragma: no cover
        return TableDescription.make_one(self.boto3_raw_data["TableDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTableFromBackupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromBackupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableToPointInTimeOutput:
    boto3_raw_data: "type_defs.RestoreTableToPointInTimeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TableDescription(self):  # pragma: no cover
        return TableDescription.make_one(self.boto3_raw_data["TableDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTableToPointInTimeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableToPointInTimeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableOutput:
    boto3_raw_data: "type_defs.UpdateTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def TableDescription(self):  # pragma: no cover
        return TableDescription.make_one(self.boto3_raw_data["TableDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTableOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImportOutput:
    boto3_raw_data: "type_defs.DescribeImportOutputTypeDef" = dataclasses.field()

    @cached_property
    def ImportTableDescription(self):  # pragma: no cover
        return ImportTableDescription.make_one(
            self.boto3_raw_data["ImportTableDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTableOutput:
    boto3_raw_data: "type_defs.ImportTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def ImportTableDescription(self):  # pragma: no cover
        return ImportTableDescription.make_one(
            self.boto3_raw_data["ImportTableDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTableOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupOutput:
    boto3_raw_data: "type_defs.DeleteBackupOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupDescription(self):  # pragma: no cover
        return BackupDescription.make_one(self.boto3_raw_data["BackupDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupOutput:
    boto3_raw_data: "type_defs.DescribeBackupOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupDescription(self):  # pragma: no cover
        return BackupDescription.make_one(self.boto3_raw_data["BackupDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableInputTableUpdate:
    boto3_raw_data: "type_defs.UpdateTableInputTableUpdateTypeDef" = dataclasses.field()

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    BillingMode = field("BillingMode")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def GlobalSecondaryIndexUpdates(self):  # pragma: no cover
        return GlobalSecondaryIndexUpdate.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexUpdates"]
        )

    @cached_property
    def StreamSpecification(self):  # pragma: no cover
        return StreamSpecification.make_one(self.boto3_raw_data["StreamSpecification"])

    @cached_property
    def SSESpecification(self):  # pragma: no cover
        return SSESpecification.make_one(self.boto3_raw_data["SSESpecification"])

    @cached_property
    def ReplicaUpdates(self):  # pragma: no cover
        return ReplicationGroupUpdate.make_many(self.boto3_raw_data["ReplicaUpdates"])

    TableClass = field("TableClass")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    MultiRegionConsistency = field("MultiRegionConsistency")

    @cached_property
    def GlobalTableWitnessUpdates(self):  # pragma: no cover
        return GlobalTableWitnessGroupUpdate.make_many(
            self.boto3_raw_data["GlobalTableWitnessUpdates"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTableInputTableUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableInputTableUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableInput:
    boto3_raw_data: "type_defs.UpdateTableInputTypeDef" = dataclasses.field()

    TableName = field("TableName")

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    BillingMode = field("BillingMode")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def GlobalSecondaryIndexUpdates(self):  # pragma: no cover
        return GlobalSecondaryIndexUpdate.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexUpdates"]
        )

    @cached_property
    def StreamSpecification(self):  # pragma: no cover
        return StreamSpecification.make_one(self.boto3_raw_data["StreamSpecification"])

    @cached_property
    def SSESpecification(self):  # pragma: no cover
        return SSESpecification.make_one(self.boto3_raw_data["SSESpecification"])

    @cached_property
    def ReplicaUpdates(self):  # pragma: no cover
        return ReplicationGroupUpdate.make_many(self.boto3_raw_data["ReplicaUpdates"])

    TableClass = field("TableClass")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    MultiRegionConsistency = field("MultiRegionConsistency")

    @cached_property
    def GlobalTableWitnessUpdates(self):  # pragma: no cover
        return GlobalTableWitnessGroupUpdate.make_many(
            self.boto3_raw_data["GlobalTableWitnessUpdates"]
        )

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTableInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableInputServiceResourceCreateTable:
    boto3_raw_data: "type_defs.CreateTableInputServiceResourceCreateTableTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    TableName = field("TableName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def LocalSecondaryIndexes(self):  # pragma: no cover
        return LocalSecondaryIndex.make_many(
            self.boto3_raw_data["LocalSecondaryIndexes"]
        )

    GlobalSecondaryIndexes = field("GlobalSecondaryIndexes")
    BillingMode = field("BillingMode")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def StreamSpecification(self):  # pragma: no cover
        return StreamSpecification.make_one(self.boto3_raw_data["StreamSpecification"])

    @cached_property
    def SSESpecification(self):  # pragma: no cover
        return SSESpecification.make_one(self.boto3_raw_data["SSESpecification"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TableClass = field("TableClass")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    ResourcePolicy = field("ResourcePolicy")

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTableInputServiceResourceCreateTableTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableInputServiceResourceCreateTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTableInput:
    boto3_raw_data: "type_defs.CreateTableInputTypeDef" = dataclasses.field()

    @cached_property
    def AttributeDefinitions(self):  # pragma: no cover
        return AttributeDefinition.make_many(
            self.boto3_raw_data["AttributeDefinitions"]
        )

    TableName = field("TableName")

    @cached_property
    def KeySchema(self):  # pragma: no cover
        return KeySchemaElement.make_many(self.boto3_raw_data["KeySchema"])

    @cached_property
    def LocalSecondaryIndexes(self):  # pragma: no cover
        return LocalSecondaryIndex.make_many(
            self.boto3_raw_data["LocalSecondaryIndexes"]
        )

    GlobalSecondaryIndexes = field("GlobalSecondaryIndexes")
    BillingMode = field("BillingMode")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    @cached_property
    def StreamSpecification(self):  # pragma: no cover
        return StreamSpecification.make_one(self.boto3_raw_data["StreamSpecification"])

    @cached_property
    def SSESpecification(self):  # pragma: no cover
        return SSESpecification.make_one(self.boto3_raw_data["SSESpecification"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TableClass = field("TableClass")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def WarmThroughput(self):  # pragma: no cover
        return WarmThroughput.make_one(self.boto3_raw_data["WarmThroughput"])

    ResourcePolicy = field("ResourcePolicy")

    @cached_property
    def OnDemandThroughput(self):  # pragma: no cover
        return OnDemandThroughput.make_one(self.boto3_raw_data["OnDemandThroughput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTableInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromBackupInput:
    boto3_raw_data: "type_defs.RestoreTableFromBackupInputTypeDef" = dataclasses.field()

    TargetTableName = field("TargetTableName")
    BackupArn = field("BackupArn")
    BillingModeOverride = field("BillingModeOverride")
    GlobalSecondaryIndexOverride = field("GlobalSecondaryIndexOverride")

    @cached_property
    def LocalSecondaryIndexOverride(self):  # pragma: no cover
        return LocalSecondaryIndex.make_many(
            self.boto3_raw_data["LocalSecondaryIndexOverride"]
        )

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughput.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @cached_property
    def SSESpecificationOverride(self):  # pragma: no cover
        return SSESpecification.make_one(
            self.boto3_raw_data["SSESpecificationOverride"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTableFromBackupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromBackupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableToPointInTimeInput:
    boto3_raw_data: "type_defs.RestoreTableToPointInTimeInputTypeDef" = (
        dataclasses.field()
    )

    TargetTableName = field("TargetTableName")
    SourceTableArn = field("SourceTableArn")
    SourceTableName = field("SourceTableName")
    UseLatestRestorableTime = field("UseLatestRestorableTime")
    RestoreDateTime = field("RestoreDateTime")
    BillingModeOverride = field("BillingModeOverride")
    GlobalSecondaryIndexOverride = field("GlobalSecondaryIndexOverride")

    @cached_property
    def LocalSecondaryIndexOverride(self):  # pragma: no cover
        return LocalSecondaryIndex.make_many(
            self.boto3_raw_data["LocalSecondaryIndexOverride"]
        )

    @cached_property
    def ProvisionedThroughputOverride(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughputOverride"]
        )

    @cached_property
    def OnDemandThroughputOverride(self):  # pragma: no cover
        return OnDemandThroughput.make_one(
            self.boto3_raw_data["OnDemandThroughputOverride"]
        )

    @cached_property
    def SSESpecificationOverride(self):  # pragma: no cover
        return SSESpecification.make_one(
            self.boto3_raw_data["SSESpecificationOverride"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTableToPointInTimeInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableToPointInTimeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteItemInputServiceResourceBatchWriteItem:
    boto3_raw_data: (
        "type_defs.BatchWriteItemInputServiceResourceBatchWriteItemTypeDef"
    ) = dataclasses.field()

    RequestItems = field("RequestItems")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchWriteItemInputServiceResourceBatchWriteItemTypeDef"
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
                "type_defs.BatchWriteItemInputServiceResourceBatchWriteItemTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableAutoScalingDescription:
    boto3_raw_data: "type_defs.TableAutoScalingDescriptionTypeDef" = dataclasses.field()

    TableName = field("TableName")
    TableStatus = field("TableStatus")

    @cached_property
    def Replicas(self):  # pragma: no cover
        return ReplicaAutoScalingDescription.make_many(self.boto3_raw_data["Replicas"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableAutoScalingDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableAutoScalingDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalTableSettingsOutput:
    boto3_raw_data: "type_defs.DescribeGlobalTableSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    GlobalTableName = field("GlobalTableName")

    @cached_property
    def ReplicaSettings(self):  # pragma: no cover
        return ReplicaSettingsDescription.make_many(
            self.boto3_raw_data["ReplicaSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeGlobalTableSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalTableSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalTableSettingsOutput:
    boto3_raw_data: "type_defs.UpdateGlobalTableSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    GlobalTableName = field("GlobalTableName")

    @cached_property
    def ReplicaSettings(self):  # pragma: no cover
        return ReplicaSettingsDescription.make_many(
            self.boto3_raw_data["ReplicaSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGlobalTableSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalTableSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableReplicaAutoScalingInput:
    boto3_raw_data: "type_defs.UpdateTableReplicaAutoScalingInputTypeDef" = (
        dataclasses.field()
    )

    TableName = field("TableName")

    @cached_property
    def GlobalSecondaryIndexUpdates(self):  # pragma: no cover
        return GlobalSecondaryIndexAutoScalingUpdate.make_many(
            self.boto3_raw_data["GlobalSecondaryIndexUpdates"]
        )

    @cached_property
    def ProvisionedWriteCapacityAutoScalingUpdate(self):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data["ProvisionedWriteCapacityAutoScalingUpdate"]
        )

    @cached_property
    def ReplicaUpdates(self):  # pragma: no cover
        return ReplicaAutoScalingUpdate.make_many(self.boto3_raw_data["ReplicaUpdates"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTableReplicaAutoScalingInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableReplicaAutoScalingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalTableSettingsInput:
    boto3_raw_data: "type_defs.UpdateGlobalTableSettingsInputTypeDef" = (
        dataclasses.field()
    )

    GlobalTableName = field("GlobalTableName")
    GlobalTableBillingMode = field("GlobalTableBillingMode")
    GlobalTableProvisionedWriteCapacityUnits = field(
        "GlobalTableProvisionedWriteCapacityUnits"
    )

    @cached_property
    def GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate(
        self,
    ):  # pragma: no cover
        return AutoScalingSettingsUpdate.make_one(
            self.boto3_raw_data[
                "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"
            ]
        )

    @cached_property
    def GlobalTableGlobalSecondaryIndexSettingsUpdate(self):  # pragma: no cover
        return GlobalTableGlobalSecondaryIndexSettingsUpdate.make_many(
            self.boto3_raw_data["GlobalTableGlobalSecondaryIndexSettingsUpdate"]
        )

    @cached_property
    def ReplicaSettingsUpdate(self):  # pragma: no cover
        return ReplicaSettingsUpdate.make_many(
            self.boto3_raw_data["ReplicaSettingsUpdate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGlobalTableSettingsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalTableSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTableInput:
    boto3_raw_data: "type_defs.ImportTableInputTypeDef" = dataclasses.field()

    @cached_property
    def S3BucketSource(self):  # pragma: no cover
        return S3BucketSource.make_one(self.boto3_raw_data["S3BucketSource"])

    InputFormat = field("InputFormat")
    TableCreationParameters = field("TableCreationParameters")
    ClientToken = field("ClientToken")
    InputFormatOptions = field("InputFormatOptions")
    InputCompressionType = field("InputCompressionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTableInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteItemInput:
    boto3_raw_data: "type_defs.BatchWriteItemInputTypeDef" = dataclasses.field()

    RequestItems = field("RequestItems")
    ReturnConsumedCapacity = field("ReturnConsumedCapacity")
    ReturnItemCollectionMetrics = field("ReturnItemCollectionMetrics")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchWriteItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableReplicaAutoScalingOutput:
    boto3_raw_data: "type_defs.DescribeTableReplicaAutoScalingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TableAutoScalingDescription(self):  # pragma: no cover
        return TableAutoScalingDescription.make_one(
            self.boto3_raw_data["TableAutoScalingDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTableReplicaAutoScalingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableReplicaAutoScalingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTableReplicaAutoScalingOutput:
    boto3_raw_data: "type_defs.UpdateTableReplicaAutoScalingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TableAutoScalingDescription(self):  # pragma: no cover
        return TableAutoScalingDescription.make_one(
            self.boto3_raw_data["TableAutoScalingDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTableReplicaAutoScalingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTableReplicaAutoScalingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
