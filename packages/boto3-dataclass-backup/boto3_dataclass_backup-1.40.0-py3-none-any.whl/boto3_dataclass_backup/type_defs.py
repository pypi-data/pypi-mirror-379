# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_backup import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AdvancedBackupSettingOutput:
    boto3_raw_data: "type_defs.AdvancedBackupSettingOutputTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    BackupOptions = field("BackupOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedBackupSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedBackupSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedBackupSetting:
    boto3_raw_data: "type_defs.AdvancedBackupSettingTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    BackupOptions = field("BackupOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedBackupSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedBackupSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateBackupVaultMpaApprovalTeamInput:
    boto3_raw_data: "type_defs.AssociateBackupVaultMpaApprovalTeamInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    MpaApprovalTeamArn = field("MpaApprovalTeamArn")
    RequesterComment = field("RequesterComment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateBackupVaultMpaApprovalTeamInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateBackupVaultMpaApprovalTeamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupJobSummary:
    boto3_raw_data: "type_defs.BackupJobSummaryTypeDef" = dataclasses.field()

    Region = field("Region")
    AccountId = field("AccountId")
    State = field("State")
    ResourceType = field("ResourceType")
    MessageCategory = field("MessageCategory")
    Count = field("Count")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPointCreator:
    boto3_raw_data: "type_defs.RecoveryPointCreatorTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    BackupPlanArn = field("BackupPlanArn")
    BackupPlanVersion = field("BackupPlanVersion")
    BackupRuleId = field("BackupRuleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointCreatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryPointCreatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupPlanTemplatesListMember:
    boto3_raw_data: "type_defs.BackupPlanTemplatesListMemberTypeDef" = (
        dataclasses.field()
    )

    BackupPlanTemplateId = field("BackupPlanTemplateId")
    BackupPlanTemplateName = field("BackupPlanTemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackupPlanTemplatesListMemberTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupPlanTemplatesListMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Lifecycle:
    boto3_raw_data: "type_defs.LifecycleTypeDef" = dataclasses.field()

    MoveToColdStorageAfterDays = field("MoveToColdStorageAfterDays")
    DeleteAfterDays = field("DeleteAfterDays")
    OptInToArchiveForSupportedResources = field("OptInToArchiveForSupportedResources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecycleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexActionOutput:
    boto3_raw_data: "type_defs.IndexActionOutputTypeDef" = dataclasses.field()

    ResourceTypes = field("ResourceTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    ConditionType = field("ConditionType")
    ConditionKey = field("ConditionKey")
    ConditionValue = field("ConditionValue")

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
class BackupSelectionsListMember:
    boto3_raw_data: "type_defs.BackupSelectionsListMemberTypeDef" = dataclasses.field()

    SelectionId = field("SelectionId")
    SelectionName = field("SelectionName")
    BackupPlanId = field("BackupPlanId")
    CreationDate = field("CreationDate")
    CreatorRequestId = field("CreatorRequestId")
    IamRoleArn = field("IamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupSelectionsListMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupSelectionsListMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupVaultListMember:
    boto3_raw_data: "type_defs.BackupVaultListMemberTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    VaultType = field("VaultType")
    VaultState = field("VaultState")
    CreationDate = field("CreationDate")
    EncryptionKeyArn = field("EncryptionKeyArn")
    CreatorRequestId = field("CreatorRequestId")
    NumberOfRecoveryPoints = field("NumberOfRecoveryPoints")
    Locked = field("Locked")
    MinRetentionDays = field("MinRetentionDays")
    MaxRetentionDays = field("MaxRetentionDays")
    LockDate = field("LockDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupVaultListMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupVaultListMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculatedLifecycle:
    boto3_raw_data: "type_defs.CalculatedLifecycleTypeDef" = dataclasses.field()

    MoveToColdStorageAt = field("MoveToColdStorageAt")
    DeleteAt = field("DeleteAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculatedLifecycleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculatedLifecycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelLegalHoldInput:
    boto3_raw_data: "type_defs.CancelLegalHoldInputTypeDef" = dataclasses.field()

    LegalHoldId = field("LegalHoldId")
    CancelDescription = field("CancelDescription")
    RetainRecordInDays = field("RetainRecordInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelLegalHoldInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelLegalHoldInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionParameter:
    boto3_raw_data: "type_defs.ConditionParameterTypeDef" = dataclasses.field()

    ConditionKey = field("ConditionKey")
    ConditionValue = field("ConditionValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlInputParameter:
    boto3_raw_data: "type_defs.ControlInputParameterTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlInputParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlInputParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlScopeOutput:
    boto3_raw_data: "type_defs.ControlScopeOutputTypeDef" = dataclasses.field()

    ComplianceResourceIds = field("ComplianceResourceIds")
    ComplianceResourceTypes = field("ComplianceResourceTypes")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlScopeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlScope:
    boto3_raw_data: "type_defs.ControlScopeTypeDef" = dataclasses.field()

    ComplianceResourceIds = field("ComplianceResourceIds")
    ComplianceResourceTypes = field("ComplianceResourceTypes")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlScopeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyJobSummary:
    boto3_raw_data: "type_defs.CopyJobSummaryTypeDef" = dataclasses.field()

    Region = field("Region")
    AccountId = field("AccountId")
    State = field("State")
    ResourceType = field("ResourceType")
    MessageCategory = field("MessageCategory")
    Count = field("Count")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyJobSummaryTypeDef"]],
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
class CreateBackupVaultInput:
    boto3_raw_data: "type_defs.CreateBackupVaultInputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    BackupVaultTags = field("BackupVaultTags")
    EncryptionKeyArn = field("EncryptionKeyArn")
    CreatorRequestId = field("CreatorRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogicallyAirGappedBackupVaultInput:
    boto3_raw_data: "type_defs.CreateLogicallyAirGappedBackupVaultInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    MinRetentionDays = field("MinRetentionDays")
    MaxRetentionDays = field("MaxRetentionDays")
    BackupVaultTags = field("BackupVaultTags")
    CreatorRequestId = field("CreatorRequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLogicallyAirGappedBackupVaultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogicallyAirGappedBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestoreAccessBackupVaultInput:
    boto3_raw_data: "type_defs.CreateRestoreAccessBackupVaultInputTypeDef" = (
        dataclasses.field()
    )

    SourceBackupVaultArn = field("SourceBackupVaultArn")
    BackupVaultName = field("BackupVaultName")
    BackupVaultTags = field("BackupVaultTags")
    CreatorRequestId = field("CreatorRequestId")
    RequesterComment = field("RequesterComment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRestoreAccessBackupVaultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestoreAccessBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateRangeOutput:
    boto3_raw_data: "type_defs.DateRangeOutputTypeDef" = dataclasses.field()

    FromDate = field("FromDate")
    ToDate = field("ToDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateRangeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateRangeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupPlanInput:
    boto3_raw_data: "type_defs.DeleteBackupPlanInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupSelectionInput:
    boto3_raw_data: "type_defs.DeleteBackupSelectionInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    SelectionId = field("SelectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupSelectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupVaultAccessPolicyInput:
    boto3_raw_data: "type_defs.DeleteBackupVaultAccessPolicyInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBackupVaultAccessPolicyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupVaultAccessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupVaultInput:
    boto3_raw_data: "type_defs.DeleteBackupVaultInputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupVaultLockConfigurationInput:
    boto3_raw_data: "type_defs.DeleteBackupVaultLockConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBackupVaultLockConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupVaultLockConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupVaultNotificationsInput:
    boto3_raw_data: "type_defs.DeleteBackupVaultNotificationsInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBackupVaultNotificationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupVaultNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFrameworkInput:
    boto3_raw_data: "type_defs.DeleteFrameworkInputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFrameworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFrameworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecoveryPointInput:
    boto3_raw_data: "type_defs.DeleteRecoveryPointInputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRecoveryPointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecoveryPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReportPlanInput:
    boto3_raw_data: "type_defs.DeleteReportPlanInputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReportPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReportPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRestoreTestingPlanInput:
    boto3_raw_data: "type_defs.DeleteRestoreTestingPlanInputTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRestoreTestingPlanInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRestoreTestingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRestoreTestingSelectionInput:
    boto3_raw_data: "type_defs.DeleteRestoreTestingSelectionInputTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRestoreTestingSelectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRestoreTestingSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupJobInput:
    boto3_raw_data: "type_defs.DescribeBackupJobInputTypeDef" = dataclasses.field()

    BackupJobId = field("BackupJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupVaultInput:
    boto3_raw_data: "type_defs.DescribeBackupVaultInputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    BackupVaultAccountId = field("BackupVaultAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupVaultInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LatestMpaApprovalTeamUpdate:
    boto3_raw_data: "type_defs.LatestMpaApprovalTeamUpdateTypeDef" = dataclasses.field()

    MpaSessionArn = field("MpaSessionArn")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    InitiationDate = field("InitiationDate")
    ExpiryDate = field("ExpiryDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LatestMpaApprovalTeamUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LatestMpaApprovalTeamUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCopyJobInput:
    boto3_raw_data: "type_defs.DescribeCopyJobInputTypeDef" = dataclasses.field()

    CopyJobId = field("CopyJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCopyJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCopyJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFrameworkInput:
    boto3_raw_data: "type_defs.DescribeFrameworkInputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFrameworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFrameworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProtectedResourceInput:
    boto3_raw_data: "type_defs.DescribeProtectedResourceInputTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProtectedResourceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProtectedResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoveryPointInput:
    boto3_raw_data: "type_defs.DescribeRecoveryPointInputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")
    BackupVaultAccountId = field("BackupVaultAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecoveryPointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoveryPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReportJobInput:
    boto3_raw_data: "type_defs.DescribeReportJobInputTypeDef" = dataclasses.field()

    ReportJobId = field("ReportJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReportJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReportJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReportPlanInput:
    boto3_raw_data: "type_defs.DescribeReportPlanInputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReportPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReportPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRestoreJobInput:
    boto3_raw_data: "type_defs.DescribeRestoreJobInputTypeDef" = dataclasses.field()

    RestoreJobId = field("RestoreJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRestoreJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRestoreJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreJobCreator:
    boto3_raw_data: "type_defs.RestoreJobCreatorTypeDef" = dataclasses.field()

    RestoreTestingPlanArn = field("RestoreTestingPlanArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreJobCreatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreJobCreatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateBackupVaultMpaApprovalTeamInput:
    boto3_raw_data: "type_defs.DisassociateBackupVaultMpaApprovalTeamInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RequesterComment = field("RequesterComment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateBackupVaultMpaApprovalTeamInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateBackupVaultMpaApprovalTeamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRecoveryPointFromParentInput:
    boto3_raw_data: "type_defs.DisassociateRecoveryPointFromParentInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateRecoveryPointFromParentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRecoveryPointFromParentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRecoveryPointInput:
    boto3_raw_data: "type_defs.DisassociateRecoveryPointInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateRecoveryPointInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRecoveryPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportBackupPlanTemplateInput:
    boto3_raw_data: "type_defs.ExportBackupPlanTemplateInputTypeDef" = (
        dataclasses.field()
    )

    BackupPlanId = field("BackupPlanId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportBackupPlanTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportBackupPlanTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Framework:
    boto3_raw_data: "type_defs.FrameworkTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")
    FrameworkArn = field("FrameworkArn")
    FrameworkDescription = field("FrameworkDescription")
    NumberOfControls = field("NumberOfControls")
    CreationTime = field("CreationTime")
    DeploymentStatus = field("DeploymentStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrameworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupPlanFromJSONInput:
    boto3_raw_data: "type_defs.GetBackupPlanFromJSONInputTypeDef" = dataclasses.field()

    BackupPlanTemplateJson = field("BackupPlanTemplateJson")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackupPlanFromJSONInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupPlanFromJSONInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupPlanFromTemplateInput:
    boto3_raw_data: "type_defs.GetBackupPlanFromTemplateInputTypeDef" = (
        dataclasses.field()
    )

    BackupPlanTemplateId = field("BackupPlanTemplateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBackupPlanFromTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupPlanFromTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupPlanInput:
    boto3_raw_data: "type_defs.GetBackupPlanInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackupPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupSelectionInput:
    boto3_raw_data: "type_defs.GetBackupSelectionInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    SelectionId = field("SelectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackupSelectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupVaultAccessPolicyInput:
    boto3_raw_data: "type_defs.GetBackupVaultAccessPolicyInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBackupVaultAccessPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupVaultAccessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupVaultNotificationsInput:
    boto3_raw_data: "type_defs.GetBackupVaultNotificationsInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBackupVaultNotificationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupVaultNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLegalHoldInput:
    boto3_raw_data: "type_defs.GetLegalHoldInputTypeDef" = dataclasses.field()

    LegalHoldId = field("LegalHoldId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLegalHoldInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLegalHoldInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecoveryPointIndexDetailsInput:
    boto3_raw_data: "type_defs.GetRecoveryPointIndexDetailsInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecoveryPointIndexDetailsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecoveryPointIndexDetailsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecoveryPointRestoreMetadataInput:
    boto3_raw_data: "type_defs.GetRecoveryPointRestoreMetadataInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")
    BackupVaultAccountId = field("BackupVaultAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecoveryPointRestoreMetadataInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecoveryPointRestoreMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreJobMetadataInput:
    boto3_raw_data: "type_defs.GetRestoreJobMetadataInputTypeDef" = dataclasses.field()

    RestoreJobId = field("RestoreJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRestoreJobMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreJobMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreTestingInferredMetadataInput:
    boto3_raw_data: "type_defs.GetRestoreTestingInferredMetadataInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")
    BackupVaultAccountId = field("BackupVaultAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRestoreTestingInferredMetadataInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreTestingInferredMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreTestingPlanInput:
    boto3_raw_data: "type_defs.GetRestoreTestingPlanInputTypeDef" = dataclasses.field()

    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRestoreTestingPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreTestingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreTestingSelectionInput:
    boto3_raw_data: "type_defs.GetRestoreTestingSelectionInputTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRestoreTestingSelectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreTestingSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexAction:
    boto3_raw_data: "type_defs.IndexActionTypeDef" = dataclasses.field()

    ResourceTypes = field("ResourceTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexedRecoveryPoint:
    boto3_raw_data: "type_defs.IndexedRecoveryPointTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    SourceResourceArn = field("SourceResourceArn")
    IamRoleArn = field("IamRoleArn")
    BackupCreationDate = field("BackupCreationDate")
    ResourceType = field("ResourceType")
    IndexCreationDate = field("IndexCreationDate")
    IndexStatus = field("IndexStatus")
    IndexStatusMessage = field("IndexStatusMessage")
    BackupVaultArn = field("BackupVaultArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexedRecoveryPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexedRecoveryPointTypeDef"]
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
class LatestRevokeRequest:
    boto3_raw_data: "type_defs.LatestRevokeRequestTypeDef" = dataclasses.field()

    MpaSessionArn = field("MpaSessionArn")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    InitiationDate = field("InitiationDate")
    ExpiryDate = field("ExpiryDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LatestRevokeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LatestRevokeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LegalHold:
    boto3_raw_data: "type_defs.LegalHoldTypeDef" = dataclasses.field()

    Title = field("Title")
    Status = field("Status")
    Description = field("Description")
    LegalHoldId = field("LegalHoldId")
    LegalHoldArn = field("LegalHoldArn")
    CreationDate = field("CreationDate")
    CancellationDate = field("CancellationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LegalHoldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LegalHoldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupJobSummariesInput:
    boto3_raw_data: "type_defs.ListBackupJobSummariesInputTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    State = field("State")
    ResourceType = field("ResourceType")
    MessageCategory = field("MessageCategory")
    AggregationPeriod = field("AggregationPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupJobSummariesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupJobSummariesInputTypeDef"]
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
class ListBackupPlanTemplatesInput:
    boto3_raw_data: "type_defs.ListBackupPlanTemplatesInputTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupPlanTemplatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlanTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlanVersionsInput:
    boto3_raw_data: "type_defs.ListBackupPlanVersionsInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupPlanVersionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlanVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlansInput:
    boto3_raw_data: "type_defs.ListBackupPlansInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    IncludeDeleted = field("IncludeDeleted")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupPlansInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlansInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupSelectionsInput:
    boto3_raw_data: "type_defs.ListBackupSelectionsInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupSelectionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupSelectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupVaultsInput:
    boto3_raw_data: "type_defs.ListBackupVaultsInputTypeDef" = dataclasses.field()

    ByVaultType = field("ByVaultType")
    ByShared = field("ByShared")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupVaultsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupVaultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCopyJobSummariesInput:
    boto3_raw_data: "type_defs.ListCopyJobSummariesInputTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    State = field("State")
    ResourceType = field("ResourceType")
    MessageCategory = field("MessageCategory")
    AggregationPeriod = field("AggregationPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCopyJobSummariesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCopyJobSummariesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFrameworksInput:
    boto3_raw_data: "type_defs.ListFrameworksInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFrameworksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFrameworksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLegalHoldsInput:
    boto3_raw_data: "type_defs.ListLegalHoldsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLegalHoldsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLegalHoldsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedResourcesByBackupVaultInput:
    boto3_raw_data: "type_defs.ListProtectedResourcesByBackupVaultInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    BackupVaultAccountId = field("BackupVaultAccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectedResourcesByBackupVaultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedResourcesByBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedResource:
    boto3_raw_data: "type_defs.ProtectedResourceTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    LastBackupTime = field("LastBackupTime")
    ResourceName = field("ResourceName")
    LastBackupVaultArn = field("LastBackupVaultArn")
    LastRecoveryPointArn = field("LastRecoveryPointArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtectedResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedResourcesInput:
    boto3_raw_data: "type_defs.ListProtectedResourcesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtectedResourcesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByLegalHoldInput:
    boto3_raw_data: "type_defs.ListRecoveryPointsByLegalHoldInputTypeDef" = (
        dataclasses.field()
    )

    LegalHoldId = field("LegalHoldId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByLegalHoldInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByLegalHoldInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPointMember:
    boto3_raw_data: "type_defs.RecoveryPointMemberTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    BackupVaultName = field("BackupVaultName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryPointMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByResourceInput:
    boto3_raw_data: "type_defs.ListRecoveryPointsByResourceInputTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ManagedByAWSBackupOnly = field("ManagedByAWSBackupOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByResourceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPointByResource:
    boto3_raw_data: "type_defs.RecoveryPointByResourceTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    CreationDate = field("CreationDate")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    EncryptionKeyArn = field("EncryptionKeyArn")
    BackupSizeBytes = field("BackupSizeBytes")
    BackupVaultName = field("BackupVaultName")
    IsParent = field("IsParent")
    ParentRecoveryPointArn = field("ParentRecoveryPointArn")
    ResourceName = field("ResourceName")
    VaultType = field("VaultType")
    IndexStatus = field("IndexStatus")
    IndexStatusMessage = field("IndexStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointByResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryPointByResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportPlansInput:
    boto3_raw_data: "type_defs.ListReportPlansInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportPlansInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportPlansInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreAccessBackupVaultsInput:
    boto3_raw_data: "type_defs.ListRestoreAccessBackupVaultsInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreAccessBackupVaultsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreAccessBackupVaultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobSummariesInput:
    boto3_raw_data: "type_defs.ListRestoreJobSummariesInputTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    State = field("State")
    ResourceType = field("ResourceType")
    AggregationPeriod = field("AggregationPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRestoreJobSummariesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobSummariesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreJobSummary:
    boto3_raw_data: "type_defs.RestoreJobSummaryTypeDef" = dataclasses.field()

    Region = field("Region")
    AccountId = field("AccountId")
    State = field("State")
    ResourceType = field("ResourceType")
    Count = field("Count")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreTestingPlansInput:
    boto3_raw_data: "type_defs.ListRestoreTestingPlansInputTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRestoreTestingPlansInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreTestingPlansInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingPlanForList:
    boto3_raw_data: "type_defs.RestoreTestingPlanForListTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    RestoreTestingPlanArn = field("RestoreTestingPlanArn")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    ScheduleExpression = field("ScheduleExpression")
    LastExecutionTime = field("LastExecutionTime")
    LastUpdateTime = field("LastUpdateTime")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartWindowHours = field("StartWindowHours")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTestingPlanForListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingPlanForListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreTestingSelectionsInput:
    boto3_raw_data: "type_defs.ListRestoreTestingSelectionsInputTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreTestingSelectionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreTestingSelectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingSelectionForList:
    boto3_raw_data: "type_defs.RestoreTestingSelectionForListTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    IamRoleArn = field("IamRoleArn")
    ProtectedResourceType = field("ProtectedResourceType")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")
    ValidationWindowHours = field("ValidationWindowHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTestingSelectionForListTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingSelectionForListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsInput:
    boto3_raw_data: "type_defs.ListTagsInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBackupVaultAccessPolicyInput:
    boto3_raw_data: "type_defs.PutBackupVaultAccessPolicyInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutBackupVaultAccessPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBackupVaultAccessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBackupVaultLockConfigurationInput:
    boto3_raw_data: "type_defs.PutBackupVaultLockConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    MinRetentionDays = field("MinRetentionDays")
    MaxRetentionDays = field("MaxRetentionDays")
    ChangeableForDays = field("ChangeableForDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBackupVaultLockConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBackupVaultLockConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBackupVaultNotificationsInput:
    boto3_raw_data: "type_defs.PutBackupVaultNotificationsInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    SNSTopicArn = field("SNSTopicArn")
    BackupVaultEvents = field("BackupVaultEvents")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutBackupVaultNotificationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBackupVaultNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRestoreValidationResultInput:
    boto3_raw_data: "type_defs.PutRestoreValidationResultInputTypeDef" = (
        dataclasses.field()
    )

    RestoreJobId = field("RestoreJobId")
    ValidationStatus = field("ValidationStatus")
    ValidationStatusMessage = field("ValidationStatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRestoreValidationResultInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRestoreValidationResultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportDeliveryChannelOutput:
    boto3_raw_data: "type_defs.ReportDeliveryChannelOutputTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    Formats = field("Formats")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportDeliveryChannelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportDeliveryChannelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportDeliveryChannel:
    boto3_raw_data: "type_defs.ReportDeliveryChannelTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    Formats = field("Formats")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportDeliveryChannelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportDeliveryChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportDestination:
    boto3_raw_data: "type_defs.ReportDestinationTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3Keys = field("S3Keys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportSettingOutput:
    boto3_raw_data: "type_defs.ReportSettingOutputTypeDef" = dataclasses.field()

    ReportTemplate = field("ReportTemplate")
    FrameworkArns = field("FrameworkArns")
    NumberOfFrameworks = field("NumberOfFrameworks")
    Accounts = field("Accounts")
    OrganizationUnits = field("OrganizationUnits")
    Regions = field("Regions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportSetting:
    boto3_raw_data: "type_defs.ReportSettingTypeDef" = dataclasses.field()

    ReportTemplate = field("ReportTemplate")
    FrameworkArns = field("FrameworkArns")
    NumberOfFrameworks = field("NumberOfFrameworks")
    Accounts = field("Accounts")
    OrganizationUnits = field("OrganizationUnits")
    Regions = field("Regions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingRecoveryPointSelectionOutput:
    boto3_raw_data: "type_defs.RestoreTestingRecoveryPointSelectionOutputTypeDef" = (
        dataclasses.field()
    )

    Algorithm = field("Algorithm")
    ExcludeVaults = field("ExcludeVaults")
    IncludeVaults = field("IncludeVaults")
    RecoveryPointTypes = field("RecoveryPointTypes")
    SelectionWindowDays = field("SelectionWindowDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreTestingRecoveryPointSelectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingRecoveryPointSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingRecoveryPointSelection:
    boto3_raw_data: "type_defs.RestoreTestingRecoveryPointSelectionTypeDef" = (
        dataclasses.field()
    )

    Algorithm = field("Algorithm")
    ExcludeVaults = field("ExcludeVaults")
    IncludeVaults = field("IncludeVaults")
    RecoveryPointTypes = field("RecoveryPointTypes")
    SelectionWindowDays = field("SelectionWindowDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreTestingRecoveryPointSelectionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingRecoveryPointSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeRestoreAccessBackupVaultInput:
    boto3_raw_data: "type_defs.RevokeRestoreAccessBackupVaultInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RestoreAccessBackupVaultArn = field("RestoreAccessBackupVaultArn")
    RequesterComment = field("RequesterComment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeRestoreAccessBackupVaultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeRestoreAccessBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReportJobInput:
    boto3_raw_data: "type_defs.StartReportJobInputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReportJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReportJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRestoreJobInput:
    boto3_raw_data: "type_defs.StartRestoreJobInputTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    Metadata = field("Metadata")
    IamRoleArn = field("IamRoleArn")
    IdempotencyToken = field("IdempotencyToken")
    ResourceType = field("ResourceType")
    CopySourceTagsToRestoredResource = field("CopySourceTagsToRestoredResource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRestoreJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRestoreJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBackupJobInput:
    boto3_raw_data: "type_defs.StopBackupJobInputTypeDef" = dataclasses.field()

    BackupJobId = field("BackupJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBackupJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBackupJobInputTypeDef"]
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
    Tags = field("Tags")

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
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeyList = field("TagKeyList")

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
class UpdateGlobalSettingsInput:
    boto3_raw_data: "type_defs.UpdateGlobalSettingsInputTypeDef" = dataclasses.field()

    GlobalSettings = field("GlobalSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalSettingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecoveryPointIndexSettingsInput:
    boto3_raw_data: "type_defs.UpdateRecoveryPointIndexSettingsInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")
    Index = field("Index")
    IamRoleArn = field("IamRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecoveryPointIndexSettingsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecoveryPointIndexSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRegionSettingsInput:
    boto3_raw_data: "type_defs.UpdateRegionSettingsInputTypeDef" = dataclasses.field()

    ResourceTypeOptInPreference = field("ResourceTypeOptInPreference")
    ResourceTypeManagementPreference = field("ResourceTypeManagementPreference")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRegionSettingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRegionSettingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupPlansListMember:
    boto3_raw_data: "type_defs.BackupPlansListMemberTypeDef" = dataclasses.field()

    BackupPlanArn = field("BackupPlanArn")
    BackupPlanId = field("BackupPlanId")
    CreationDate = field("CreationDate")
    DeletionDate = field("DeletionDate")
    VersionId = field("VersionId")
    BackupPlanName = field("BackupPlanName")
    CreatorRequestId = field("CreatorRequestId")
    LastExecutionDate = field("LastExecutionDate")

    @cached_property
    def AdvancedBackupSettings(self):  # pragma: no cover
        return AdvancedBackupSettingOutput.make_many(
            self.boto3_raw_data["AdvancedBackupSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupPlansListMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupPlansListMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupJob:
    boto3_raw_data: "type_defs.BackupJobTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BackupJobId = field("BackupJobId")
    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    RecoveryPointArn = field("RecoveryPointArn")
    ResourceArn = field("ResourceArn")
    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    State = field("State")
    StatusMessage = field("StatusMessage")
    PercentDone = field("PercentDone")
    BackupSizeInBytes = field("BackupSizeInBytes")
    IamRoleArn = field("IamRoleArn")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RecoveryPointCreator.make_one(self.boto3_raw_data["CreatedBy"])

    ExpectedCompletionDate = field("ExpectedCompletionDate")
    StartBy = field("StartBy")
    ResourceType = field("ResourceType")
    BytesTransferred = field("BytesTransferred")
    BackupOptions = field("BackupOptions")
    BackupType = field("BackupType")
    ParentJobId = field("ParentJobId")
    IsParent = field("IsParent")
    ResourceName = field("ResourceName")
    InitiationDate = field("InitiationDate")
    MessageCategory = field("MessageCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyJob:
    boto3_raw_data: "type_defs.CopyJobTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    CopyJobId = field("CopyJobId")
    SourceBackupVaultArn = field("SourceBackupVaultArn")
    SourceRecoveryPointArn = field("SourceRecoveryPointArn")
    DestinationBackupVaultArn = field("DestinationBackupVaultArn")
    DestinationRecoveryPointArn = field("DestinationRecoveryPointArn")
    ResourceArn = field("ResourceArn")
    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    State = field("State")
    StatusMessage = field("StatusMessage")
    BackupSizeInBytes = field("BackupSizeInBytes")
    IamRoleArn = field("IamRoleArn")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RecoveryPointCreator.make_one(self.boto3_raw_data["CreatedBy"])

    ResourceType = field("ResourceType")
    ParentJobId = field("ParentJobId")
    IsParent = field("IsParent")
    CompositeMemberIdentifier = field("CompositeMemberIdentifier")
    NumberOfChildJobs = field("NumberOfChildJobs")
    ChildJobsInState = field("ChildJobsInState")
    ResourceName = field("ResourceName")
    MessageCategory = field("MessageCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyAction:
    boto3_raw_data: "type_defs.CopyActionTypeDef" = dataclasses.field()

    DestinationBackupVaultArn = field("DestinationBackupVaultArn")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBackupJobInput:
    boto3_raw_data: "type_defs.StartBackupJobInputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    ResourceArn = field("ResourceArn")
    IamRoleArn = field("IamRoleArn")
    IdempotencyToken = field("IdempotencyToken")
    StartWindowMinutes = field("StartWindowMinutes")
    CompleteWindowMinutes = field("CompleteWindowMinutes")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    RecoveryPointTags = field("RecoveryPointTags")
    BackupOptions = field("BackupOptions")
    Index = field("Index")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBackupJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBackupJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCopyJobInput:
    boto3_raw_data: "type_defs.StartCopyJobInputTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    SourceBackupVaultName = field("SourceBackupVaultName")
    DestinationBackupVaultArn = field("DestinationBackupVaultArn")
    IamRoleArn = field("IamRoleArn")
    IdempotencyToken = field("IdempotencyToken")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartCopyJobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCopyJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecoveryPointLifecycleInput:
    boto3_raw_data: "type_defs.UpdateRecoveryPointLifecycleInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecoveryPointLifecycleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecoveryPointLifecycleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPointByBackupVault:
    boto3_raw_data: "type_defs.RecoveryPointByBackupVaultTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    SourceBackupVaultArn = field("SourceBackupVaultArn")
    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RecoveryPointCreator.make_one(self.boto3_raw_data["CreatedBy"])

    IamRoleArn = field("IamRoleArn")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreationDate = field("CreationDate")
    InitiationDate = field("InitiationDate")
    CompletionDate = field("CompletionDate")
    BackupSizeInBytes = field("BackupSizeInBytes")

    @cached_property
    def CalculatedLifecycle(self):  # pragma: no cover
        return CalculatedLifecycle.make_one(self.boto3_raw_data["CalculatedLifecycle"])

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    EncryptionKeyArn = field("EncryptionKeyArn")
    IsEncrypted = field("IsEncrypted")
    LastRestoreTime = field("LastRestoreTime")
    ParentRecoveryPointArn = field("ParentRecoveryPointArn")
    CompositeMemberIdentifier = field("CompositeMemberIdentifier")
    IsParent = field("IsParent")
    ResourceName = field("ResourceName")
    VaultType = field("VaultType")
    IndexStatus = field("IndexStatus")
    IndexStatusMessage = field("IndexStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointByBackupVaultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryPointByBackupVaultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionsOutput:
    boto3_raw_data: "type_defs.ConditionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def StringEquals(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringEquals"])

    @cached_property
    def StringNotEquals(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringNotEquals"])

    @cached_property
    def StringLike(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringLike"])

    @cached_property
    def StringNotLike(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringNotLike"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Conditions:
    boto3_raw_data: "type_defs.ConditionsTypeDef" = dataclasses.field()

    @cached_property
    def StringEquals(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringEquals"])

    @cached_property
    def StringNotEquals(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringNotEquals"])

    @cached_property
    def StringLike(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringLike"])

    @cached_property
    def StringNotLike(self):  # pragma: no cover
        return ConditionParameter.make_many(self.boto3_raw_data["StringNotLike"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameworkControlOutput:
    boto3_raw_data: "type_defs.FrameworkControlOutputTypeDef" = dataclasses.field()

    ControlName = field("ControlName")

    @cached_property
    def ControlInputParameters(self):  # pragma: no cover
        return ControlInputParameter.make_many(
            self.boto3_raw_data["ControlInputParameters"]
        )

    @cached_property
    def ControlScope(self):  # pragma: no cover
        return ControlScopeOutput.make_one(self.boto3_raw_data["ControlScope"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameworkControlOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameworkControlOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupPlanOutput:
    boto3_raw_data: "type_defs.CreateBackupPlanOutputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    BackupPlanArn = field("BackupPlanArn")
    CreationDate = field("CreationDate")
    VersionId = field("VersionId")

    @cached_property
    def AdvancedBackupSettings(self):  # pragma: no cover
        return AdvancedBackupSettingOutput.make_many(
            self.boto3_raw_data["AdvancedBackupSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupSelectionOutput:
    boto3_raw_data: "type_defs.CreateBackupSelectionOutputTypeDef" = dataclasses.field()

    SelectionId = field("SelectionId")
    BackupPlanId = field("BackupPlanId")
    CreationDate = field("CreationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupSelectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupVaultOutput:
    boto3_raw_data: "type_defs.CreateBackupVaultOutputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    CreationDate = field("CreationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupVaultOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFrameworkOutput:
    boto3_raw_data: "type_defs.CreateFrameworkOutputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")
    FrameworkArn = field("FrameworkArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFrameworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFrameworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogicallyAirGappedBackupVaultOutput:
    boto3_raw_data: "type_defs.CreateLogicallyAirGappedBackupVaultOutputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    CreationDate = field("CreationDate")
    VaultState = field("VaultState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLogicallyAirGappedBackupVaultOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogicallyAirGappedBackupVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReportPlanOutput:
    boto3_raw_data: "type_defs.CreateReportPlanOutputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")
    ReportPlanArn = field("ReportPlanArn")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReportPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReportPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestoreAccessBackupVaultOutput:
    boto3_raw_data: "type_defs.CreateRestoreAccessBackupVaultOutputTypeDef" = (
        dataclasses.field()
    )

    RestoreAccessBackupVaultArn = field("RestoreAccessBackupVaultArn")
    VaultState = field("VaultState")
    RestoreAccessBackupVaultName = field("RestoreAccessBackupVaultName")
    CreationDate = field("CreationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRestoreAccessBackupVaultOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestoreAccessBackupVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestoreTestingPlanOutput:
    boto3_raw_data: "type_defs.CreateRestoreTestingPlanOutputTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    RestoreTestingPlanArn = field("RestoreTestingPlanArn")
    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRestoreTestingPlanOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestoreTestingPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestoreTestingSelectionOutput:
    boto3_raw_data: "type_defs.CreateRestoreTestingSelectionOutputTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    RestoreTestingPlanArn = field("RestoreTestingPlanArn")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRestoreTestingSelectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestoreTestingSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackupPlanOutput:
    boto3_raw_data: "type_defs.DeleteBackupPlanOutputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    BackupPlanArn = field("BackupPlanArn")
    DeletionDate = field("DeletionDate")
    VersionId = field("VersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackupPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackupPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupJobOutput:
    boto3_raw_data: "type_defs.DescribeBackupJobOutputTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    BackupJobId = field("BackupJobId")
    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    RecoveryPointArn = field("RecoveryPointArn")
    ResourceArn = field("ResourceArn")
    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    State = field("State")
    StatusMessage = field("StatusMessage")
    PercentDone = field("PercentDone")
    BackupSizeInBytes = field("BackupSizeInBytes")
    IamRoleArn = field("IamRoleArn")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RecoveryPointCreator.make_one(self.boto3_raw_data["CreatedBy"])

    ResourceType = field("ResourceType")
    BytesTransferred = field("BytesTransferred")
    ExpectedCompletionDate = field("ExpectedCompletionDate")
    StartBy = field("StartBy")
    BackupOptions = field("BackupOptions")
    BackupType = field("BackupType")
    ParentJobId = field("ParentJobId")
    IsParent = field("IsParent")
    NumberOfChildJobs = field("NumberOfChildJobs")
    ChildJobsInState = field("ChildJobsInState")
    ResourceName = field("ResourceName")
    InitiationDate = field("InitiationDate")
    MessageCategory = field("MessageCategory")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGlobalSettingsOutput:
    boto3_raw_data: "type_defs.DescribeGlobalSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    GlobalSettings = field("GlobalSettings")
    LastUpdateTime = field("LastUpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGlobalSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGlobalSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProtectedResourceOutput:
    boto3_raw_data: "type_defs.DescribeProtectedResourceOutputTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")
    LastBackupTime = field("LastBackupTime")
    ResourceName = field("ResourceName")
    LastBackupVaultArn = field("LastBackupVaultArn")
    LastRecoveryPointArn = field("LastRecoveryPointArn")
    LatestRestoreExecutionTimeMinutes = field("LatestRestoreExecutionTimeMinutes")
    LatestRestoreJobCreationDate = field("LatestRestoreJobCreationDate")
    LatestRestoreRecoveryPointCreationDate = field(
        "LatestRestoreRecoveryPointCreationDate"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProtectedResourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProtectedResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoveryPointOutput:
    boto3_raw_data: "type_defs.DescribeRecoveryPointOutputTypeDef" = dataclasses.field()

    RecoveryPointArn = field("RecoveryPointArn")
    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    SourceBackupVaultArn = field("SourceBackupVaultArn")
    ResourceArn = field("ResourceArn")
    ResourceType = field("ResourceType")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RecoveryPointCreator.make_one(self.boto3_raw_data["CreatedBy"])

    IamRoleArn = field("IamRoleArn")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreationDate = field("CreationDate")
    InitiationDate = field("InitiationDate")
    CompletionDate = field("CompletionDate")
    BackupSizeInBytes = field("BackupSizeInBytes")

    @cached_property
    def CalculatedLifecycle(self):  # pragma: no cover
        return CalculatedLifecycle.make_one(self.boto3_raw_data["CalculatedLifecycle"])

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    EncryptionKeyArn = field("EncryptionKeyArn")
    IsEncrypted = field("IsEncrypted")
    StorageClass = field("StorageClass")
    LastRestoreTime = field("LastRestoreTime")
    ParentRecoveryPointArn = field("ParentRecoveryPointArn")
    CompositeMemberIdentifier = field("CompositeMemberIdentifier")
    IsParent = field("IsParent")
    ResourceName = field("ResourceName")
    VaultType = field("VaultType")
    IndexStatus = field("IndexStatus")
    IndexStatusMessage = field("IndexStatusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecoveryPointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoveryPointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegionSettingsOutput:
    boto3_raw_data: "type_defs.DescribeRegionSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    ResourceTypeOptInPreference = field("ResourceTypeOptInPreference")
    ResourceTypeManagementPreference = field("ResourceTypeManagementPreference")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRegionSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegionSettingsOutputTypeDef"]
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
class ExportBackupPlanTemplateOutput:
    boto3_raw_data: "type_defs.ExportBackupPlanTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    BackupPlanTemplateJson = field("BackupPlanTemplateJson")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportBackupPlanTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportBackupPlanTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupVaultAccessPolicyOutput:
    boto3_raw_data: "type_defs.GetBackupVaultAccessPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBackupVaultAccessPolicyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupVaultAccessPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupVaultNotificationsOutput:
    boto3_raw_data: "type_defs.GetBackupVaultNotificationsOutputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    SNSTopicArn = field("SNSTopicArn")
    BackupVaultEvents = field("BackupVaultEvents")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBackupVaultNotificationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupVaultNotificationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecoveryPointIndexDetailsOutput:
    boto3_raw_data: "type_defs.GetRecoveryPointIndexDetailsOutputTypeDef" = (
        dataclasses.field()
    )

    RecoveryPointArn = field("RecoveryPointArn")
    BackupVaultArn = field("BackupVaultArn")
    SourceResourceArn = field("SourceResourceArn")
    IndexCreationDate = field("IndexCreationDate")
    IndexDeletionDate = field("IndexDeletionDate")
    IndexCompletionDate = field("IndexCompletionDate")
    IndexStatus = field("IndexStatus")
    IndexStatusMessage = field("IndexStatusMessage")
    TotalItemsIndexed = field("TotalItemsIndexed")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecoveryPointIndexDetailsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecoveryPointIndexDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecoveryPointRestoreMetadataOutput:
    boto3_raw_data: "type_defs.GetRecoveryPointRestoreMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultArn = field("BackupVaultArn")
    RecoveryPointArn = field("RecoveryPointArn")
    RestoreMetadata = field("RestoreMetadata")
    ResourceType = field("ResourceType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecoveryPointRestoreMetadataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecoveryPointRestoreMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreJobMetadataOutput:
    boto3_raw_data: "type_defs.GetRestoreJobMetadataOutputTypeDef" = dataclasses.field()

    RestoreJobId = field("RestoreJobId")
    Metadata = field("Metadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRestoreJobMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreJobMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreTestingInferredMetadataOutput:
    boto3_raw_data: "type_defs.GetRestoreTestingInferredMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    InferredMetadata = field("InferredMetadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRestoreTestingInferredMetadataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreTestingInferredMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSupportedResourceTypesOutput:
    boto3_raw_data: "type_defs.GetSupportedResourceTypesOutputTypeDef" = (
        dataclasses.field()
    )

    ResourceTypes = field("ResourceTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSupportedResourceTypesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSupportedResourceTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupJobSummariesOutput:
    boto3_raw_data: "type_defs.ListBackupJobSummariesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BackupJobSummaries(self):  # pragma: no cover
        return BackupJobSummary.make_many(self.boto3_raw_data["BackupJobSummaries"])

    AggregationPeriod = field("AggregationPeriod")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupJobSummariesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupJobSummariesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlanTemplatesOutput:
    boto3_raw_data: "type_defs.ListBackupPlanTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BackupPlanTemplatesList(self):  # pragma: no cover
        return BackupPlanTemplatesListMember.make_many(
            self.boto3_raw_data["BackupPlanTemplatesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBackupPlanTemplatesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlanTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupSelectionsOutput:
    boto3_raw_data: "type_defs.ListBackupSelectionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupSelectionsList(self):  # pragma: no cover
        return BackupSelectionsListMember.make_many(
            self.boto3_raw_data["BackupSelectionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupSelectionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupSelectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupVaultsOutput:
    boto3_raw_data: "type_defs.ListBackupVaultsOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupVaultList(self):  # pragma: no cover
        return BackupVaultListMember.make_many(self.boto3_raw_data["BackupVaultList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupVaultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupVaultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCopyJobSummariesOutput:
    boto3_raw_data: "type_defs.ListCopyJobSummariesOutputTypeDef" = dataclasses.field()

    @cached_property
    def CopyJobSummaries(self):  # pragma: no cover
        return CopyJobSummary.make_many(self.boto3_raw_data["CopyJobSummaries"])

    AggregationPeriod = field("AggregationPeriod")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCopyJobSummariesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCopyJobSummariesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsOutput:
    boto3_raw_data: "type_defs.ListTagsOutputTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBackupJobOutput:
    boto3_raw_data: "type_defs.StartBackupJobOutputTypeDef" = dataclasses.field()

    BackupJobId = field("BackupJobId")
    RecoveryPointArn = field("RecoveryPointArn")
    CreationDate = field("CreationDate")
    IsParent = field("IsParent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBackupJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBackupJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCopyJobOutput:
    boto3_raw_data: "type_defs.StartCopyJobOutputTypeDef" = dataclasses.field()

    CopyJobId = field("CopyJobId")
    CreationDate = field("CreationDate")
    IsParent = field("IsParent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCopyJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCopyJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReportJobOutput:
    boto3_raw_data: "type_defs.StartReportJobOutputTypeDef" = dataclasses.field()

    ReportJobId = field("ReportJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReportJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReportJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRestoreJobOutput:
    boto3_raw_data: "type_defs.StartRestoreJobOutputTypeDef" = dataclasses.field()

    RestoreJobId = field("RestoreJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRestoreJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRestoreJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackupPlanOutput:
    boto3_raw_data: "type_defs.UpdateBackupPlanOutputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    BackupPlanArn = field("BackupPlanArn")
    CreationDate = field("CreationDate")
    VersionId = field("VersionId")

    @cached_property
    def AdvancedBackupSettings(self):  # pragma: no cover
        return AdvancedBackupSettingOutput.make_many(
            self.boto3_raw_data["AdvancedBackupSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackupPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackupPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFrameworkOutput:
    boto3_raw_data: "type_defs.UpdateFrameworkOutputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")
    FrameworkArn = field("FrameworkArn")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFrameworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFrameworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecoveryPointIndexSettingsOutput:
    boto3_raw_data: "type_defs.UpdateRecoveryPointIndexSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    RecoveryPointArn = field("RecoveryPointArn")
    IndexStatus = field("IndexStatus")
    Index = field("Index")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecoveryPointIndexSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecoveryPointIndexSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecoveryPointLifecycleOutput:
    boto3_raw_data: "type_defs.UpdateRecoveryPointLifecycleOutputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultArn = field("BackupVaultArn")
    RecoveryPointArn = field("RecoveryPointArn")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    @cached_property
    def CalculatedLifecycle(self):  # pragma: no cover
        return CalculatedLifecycle.make_one(self.boto3_raw_data["CalculatedLifecycle"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRecoveryPointLifecycleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecoveryPointLifecycleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReportPlanOutput:
    boto3_raw_data: "type_defs.UpdateReportPlanOutputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")
    ReportPlanArn = field("ReportPlanArn")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReportPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReportPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRestoreTestingPlanOutput:
    boto3_raw_data: "type_defs.UpdateRestoreTestingPlanOutputTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    RestoreTestingPlanArn = field("RestoreTestingPlanArn")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRestoreTestingPlanOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRestoreTestingPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRestoreTestingSelectionOutput:
    boto3_raw_data: "type_defs.UpdateRestoreTestingSelectionOutputTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    RestoreTestingPlanArn = field("RestoreTestingPlanArn")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRestoreTestingSelectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRestoreTestingSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPointSelectionOutput:
    boto3_raw_data: "type_defs.RecoveryPointSelectionOutputTypeDef" = (
        dataclasses.field()
    )

    VaultNames = field("VaultNames")
    ResourceIdentifiers = field("ResourceIdentifiers")

    @cached_property
    def DateRange(self):  # pragma: no cover
        return DateRangeOutput.make_one(self.boto3_raw_data["DateRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointSelectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryPointSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateRange:
    boto3_raw_data: "type_defs.DateRangeTypeDef" = dataclasses.field()

    FromDate = field("FromDate")
    ToDate = field("ToDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupJobsInput:
    boto3_raw_data: "type_defs.ListBackupJobsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ByResourceArn = field("ByResourceArn")
    ByState = field("ByState")
    ByBackupVaultName = field("ByBackupVaultName")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByResourceType = field("ByResourceType")
    ByAccountId = field("ByAccountId")
    ByCompleteAfter = field("ByCompleteAfter")
    ByCompleteBefore = field("ByCompleteBefore")
    ByParentJobId = field("ByParentJobId")
    ByMessageCategory = field("ByMessageCategory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCopyJobsInput:
    boto3_raw_data: "type_defs.ListCopyJobsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ByResourceArn = field("ByResourceArn")
    ByState = field("ByState")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByResourceType = field("ByResourceType")
    ByDestinationVaultArn = field("ByDestinationVaultArn")
    ByAccountId = field("ByAccountId")
    ByCompleteBefore = field("ByCompleteBefore")
    ByCompleteAfter = field("ByCompleteAfter")
    ByParentJobId = field("ByParentJobId")
    ByMessageCategory = field("ByMessageCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListCopyJobsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCopyJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexedRecoveryPointsInput:
    boto3_raw_data: "type_defs.ListIndexedRecoveryPointsInputTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    SourceResourceArn = field("SourceResourceArn")
    CreatedBefore = field("CreatedBefore")
    CreatedAfter = field("CreatedAfter")
    ResourceType = field("ResourceType")
    IndexStatus = field("IndexStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIndexedRecoveryPointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexedRecoveryPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByBackupVaultInput:
    boto3_raw_data: "type_defs.ListRecoveryPointsByBackupVaultInputTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    BackupVaultAccountId = field("BackupVaultAccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ByResourceArn = field("ByResourceArn")
    ByResourceType = field("ByResourceType")
    ByBackupPlanId = field("ByBackupPlanId")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByParentRecoveryPointArn = field("ByParentRecoveryPointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByBackupVaultInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByBackupVaultInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportJobsInput:
    boto3_raw_data: "type_defs.ListReportJobsInputTypeDef" = dataclasses.field()

    ByReportPlanName = field("ByReportPlanName")
    ByCreationBefore = field("ByCreationBefore")
    ByCreationAfter = field("ByCreationAfter")
    ByStatus = field("ByStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobsByProtectedResourceInput:
    boto3_raw_data: "type_defs.ListRestoreJobsByProtectedResourceInputTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    ByStatus = field("ByStatus")
    ByRecoveryPointCreationDateAfter = field("ByRecoveryPointCreationDateAfter")
    ByRecoveryPointCreationDateBefore = field("ByRecoveryPointCreationDateBefore")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreJobsByProtectedResourceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobsByProtectedResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobsInput:
    boto3_raw_data: "type_defs.ListRestoreJobsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ByAccountId = field("ByAccountId")
    ByResourceType = field("ByResourceType")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByStatus = field("ByStatus")
    ByCompleteBefore = field("ByCompleteBefore")
    ByCompleteAfter = field("ByCompleteAfter")
    ByRestoreTestingPlanArn = field("ByRestoreTestingPlanArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRestoreJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupVaultOutput:
    boto3_raw_data: "type_defs.DescribeBackupVaultOutputTypeDef" = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    BackupVaultArn = field("BackupVaultArn")
    VaultType = field("VaultType")
    VaultState = field("VaultState")
    EncryptionKeyArn = field("EncryptionKeyArn")
    CreationDate = field("CreationDate")
    CreatorRequestId = field("CreatorRequestId")
    NumberOfRecoveryPoints = field("NumberOfRecoveryPoints")
    Locked = field("Locked")
    MinRetentionDays = field("MinRetentionDays")
    MaxRetentionDays = field("MaxRetentionDays")
    LockDate = field("LockDate")
    SourceBackupVaultArn = field("SourceBackupVaultArn")
    MpaApprovalTeamArn = field("MpaApprovalTeamArn")
    MpaSessionArn = field("MpaSessionArn")

    @cached_property
    def LatestMpaApprovalTeamUpdate(self):  # pragma: no cover
        return LatestMpaApprovalTeamUpdate.make_one(
            self.boto3_raw_data["LatestMpaApprovalTeamUpdate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupVaultOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRestoreJobOutput:
    boto3_raw_data: "type_defs.DescribeRestoreJobOutputTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RestoreJobId = field("RestoreJobId")
    RecoveryPointArn = field("RecoveryPointArn")
    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    PercentDone = field("PercentDone")
    BackupSizeInBytes = field("BackupSizeInBytes")
    IamRoleArn = field("IamRoleArn")
    ExpectedCompletionTimeMinutes = field("ExpectedCompletionTimeMinutes")
    CreatedResourceArn = field("CreatedResourceArn")
    ResourceType = field("ResourceType")
    RecoveryPointCreationDate = field("RecoveryPointCreationDate")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RestoreJobCreator.make_one(self.boto3_raw_data["CreatedBy"])

    ValidationStatus = field("ValidationStatus")
    ValidationStatusMessage = field("ValidationStatusMessage")
    DeletionStatus = field("DeletionStatus")
    DeletionStatusMessage = field("DeletionStatusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRestoreJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRestoreJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreJobsListMember:
    boto3_raw_data: "type_defs.RestoreJobsListMemberTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    RestoreJobId = field("RestoreJobId")
    RecoveryPointArn = field("RecoveryPointArn")
    CreationDate = field("CreationDate")
    CompletionDate = field("CompletionDate")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    PercentDone = field("PercentDone")
    BackupSizeInBytes = field("BackupSizeInBytes")
    IamRoleArn = field("IamRoleArn")
    ExpectedCompletionTimeMinutes = field("ExpectedCompletionTimeMinutes")
    CreatedResourceArn = field("CreatedResourceArn")
    ResourceType = field("ResourceType")
    RecoveryPointCreationDate = field("RecoveryPointCreationDate")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return RestoreJobCreator.make_one(self.boto3_raw_data["CreatedBy"])

    ValidationStatus = field("ValidationStatus")
    ValidationStatusMessage = field("ValidationStatusMessage")
    DeletionStatus = field("DeletionStatus")
    DeletionStatusMessage = field("DeletionStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreJobsListMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreJobsListMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFrameworksOutput:
    boto3_raw_data: "type_defs.ListFrameworksOutputTypeDef" = dataclasses.field()

    @cached_property
    def Frameworks(self):  # pragma: no cover
        return Framework.make_many(self.boto3_raw_data["Frameworks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFrameworksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFrameworksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexedRecoveryPointsOutput:
    boto3_raw_data: "type_defs.ListIndexedRecoveryPointsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IndexedRecoveryPoints(self):  # pragma: no cover
        return IndexedRecoveryPoint.make_many(
            self.boto3_raw_data["IndexedRecoveryPoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIndexedRecoveryPointsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexedRecoveryPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedResourceConditionsOutput:
    boto3_raw_data: "type_defs.ProtectedResourceConditionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StringEquals(self):  # pragma: no cover
        return KeyValue.make_many(self.boto3_raw_data["StringEquals"])

    @cached_property
    def StringNotEquals(self):  # pragma: no cover
        return KeyValue.make_many(self.boto3_raw_data["StringNotEquals"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedResourceConditionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedResourceConditionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedResourceConditions:
    boto3_raw_data: "type_defs.ProtectedResourceConditionsTypeDef" = dataclasses.field()

    @cached_property
    def StringEquals(self):  # pragma: no cover
        return KeyValue.make_many(self.boto3_raw_data["StringEquals"])

    @cached_property
    def StringNotEquals(self):  # pragma: no cover
        return KeyValue.make_many(self.boto3_raw_data["StringNotEquals"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedResourceConditionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedResourceConditionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreAccessBackupVaultListMember:
    boto3_raw_data: "type_defs.RestoreAccessBackupVaultListMemberTypeDef" = (
        dataclasses.field()
    )

    RestoreAccessBackupVaultArn = field("RestoreAccessBackupVaultArn")
    CreationDate = field("CreationDate")
    ApprovalDate = field("ApprovalDate")
    VaultState = field("VaultState")

    @cached_property
    def LatestRevokeRequest(self):  # pragma: no cover
        return LatestRevokeRequest.make_one(self.boto3_raw_data["LatestRevokeRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreAccessBackupVaultListMemberTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreAccessBackupVaultListMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLegalHoldsOutput:
    boto3_raw_data: "type_defs.ListLegalHoldsOutputTypeDef" = dataclasses.field()

    @cached_property
    def LegalHolds(self):  # pragma: no cover
        return LegalHold.make_many(self.boto3_raw_data["LegalHolds"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLegalHoldsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLegalHoldsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupJobsInputPaginate:
    boto3_raw_data: "type_defs.ListBackupJobsInputPaginateTypeDef" = dataclasses.field()

    ByResourceArn = field("ByResourceArn")
    ByState = field("ByState")
    ByBackupVaultName = field("ByBackupVaultName")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByResourceType = field("ByResourceType")
    ByAccountId = field("ByAccountId")
    ByCompleteAfter = field("ByCompleteAfter")
    ByCompleteBefore = field("ByCompleteBefore")
    ByParentJobId = field("ByParentJobId")
    ByMessageCategory = field("ByMessageCategory")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupJobsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlanTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListBackupPlanTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBackupPlanTemplatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlanTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlanVersionsInputPaginate:
    boto3_raw_data: "type_defs.ListBackupPlanVersionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BackupPlanId = field("BackupPlanId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBackupPlanVersionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlanVersionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlansInputPaginate:
    boto3_raw_data: "type_defs.ListBackupPlansInputPaginateTypeDef" = (
        dataclasses.field()
    )

    IncludeDeleted = field("IncludeDeleted")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupPlansInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlansInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupSelectionsInputPaginate:
    boto3_raw_data: "type_defs.ListBackupSelectionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BackupPlanId = field("BackupPlanId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBackupSelectionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupSelectionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupVaultsInputPaginate:
    boto3_raw_data: "type_defs.ListBackupVaultsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ByVaultType = field("ByVaultType")
    ByShared = field("ByShared")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBackupVaultsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupVaultsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCopyJobsInputPaginate:
    boto3_raw_data: "type_defs.ListCopyJobsInputPaginateTypeDef" = dataclasses.field()

    ByResourceArn = field("ByResourceArn")
    ByState = field("ByState")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByResourceType = field("ByResourceType")
    ByDestinationVaultArn = field("ByDestinationVaultArn")
    ByAccountId = field("ByAccountId")
    ByCompleteBefore = field("ByCompleteBefore")
    ByCompleteAfter = field("ByCompleteAfter")
    ByParentJobId = field("ByParentJobId")
    ByMessageCategory = field("ByMessageCategory")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCopyJobsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCopyJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexedRecoveryPointsInputPaginate:
    boto3_raw_data: "type_defs.ListIndexedRecoveryPointsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    SourceResourceArn = field("SourceResourceArn")
    CreatedBefore = field("CreatedBefore")
    CreatedAfter = field("CreatedAfter")
    ResourceType = field("ResourceType")
    IndexStatus = field("IndexStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIndexedRecoveryPointsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexedRecoveryPointsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLegalHoldsInputPaginate:
    boto3_raw_data: "type_defs.ListLegalHoldsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLegalHoldsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLegalHoldsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedResourcesByBackupVaultInputPaginate:
    boto3_raw_data: (
        "type_defs.ListProtectedResourcesByBackupVaultInputPaginateTypeDef"
    ) = dataclasses.field()

    BackupVaultName = field("BackupVaultName")
    BackupVaultAccountId = field("BackupVaultAccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectedResourcesByBackupVaultInputPaginateTypeDef"
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
                "type_defs.ListProtectedResourcesByBackupVaultInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedResourcesInputPaginate:
    boto3_raw_data: "type_defs.ListProtectedResourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectedResourcesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedResourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByBackupVaultInputPaginate:
    boto3_raw_data: "type_defs.ListRecoveryPointsByBackupVaultInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")
    BackupVaultAccountId = field("BackupVaultAccountId")
    ByResourceArn = field("ByResourceArn")
    ByResourceType = field("ByResourceType")
    ByBackupPlanId = field("ByBackupPlanId")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByParentRecoveryPointArn = field("ByParentRecoveryPointArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByBackupVaultInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByBackupVaultInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByLegalHoldInputPaginate:
    boto3_raw_data: "type_defs.ListRecoveryPointsByLegalHoldInputPaginateTypeDef" = (
        dataclasses.field()
    )

    LegalHoldId = field("LegalHoldId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByLegalHoldInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByLegalHoldInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByResourceInputPaginate:
    boto3_raw_data: "type_defs.ListRecoveryPointsByResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    ManagedByAWSBackupOnly = field("ManagedByAWSBackupOnly")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByResourceInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreAccessBackupVaultsInputPaginate:
    boto3_raw_data: "type_defs.ListRestoreAccessBackupVaultsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BackupVaultName = field("BackupVaultName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreAccessBackupVaultsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreAccessBackupVaultsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobsByProtectedResourceInputPaginate:
    boto3_raw_data: (
        "type_defs.ListRestoreJobsByProtectedResourceInputPaginateTypeDef"
    ) = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ByStatus = field("ByStatus")
    ByRecoveryPointCreationDateAfter = field("ByRecoveryPointCreationDateAfter")
    ByRecoveryPointCreationDateBefore = field("ByRecoveryPointCreationDateBefore")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreJobsByProtectedResourceInputPaginateTypeDef"
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
                "type_defs.ListRestoreJobsByProtectedResourceInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobsInputPaginate:
    boto3_raw_data: "type_defs.ListRestoreJobsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ByAccountId = field("ByAccountId")
    ByResourceType = field("ByResourceType")
    ByCreatedBefore = field("ByCreatedBefore")
    ByCreatedAfter = field("ByCreatedAfter")
    ByStatus = field("ByStatus")
    ByCompleteBefore = field("ByCompleteBefore")
    ByCompleteAfter = field("ByCompleteAfter")
    ByRestoreTestingPlanArn = field("ByRestoreTestingPlanArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRestoreJobsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreTestingPlansInputPaginate:
    boto3_raw_data: "type_defs.ListRestoreTestingPlansInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreTestingPlansInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreTestingPlansInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreTestingSelectionsInputPaginate:
    boto3_raw_data: "type_defs.ListRestoreTestingSelectionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreTestingSelectionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreTestingSelectionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedResourcesByBackupVaultOutput:
    boto3_raw_data: "type_defs.ListProtectedResourcesByBackupVaultOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Results(self):  # pragma: no cover
        return ProtectedResource.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectedResourcesByBackupVaultOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedResourcesByBackupVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedResourcesOutput:
    boto3_raw_data: "type_defs.ListProtectedResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Results(self):  # pragma: no cover
        return ProtectedResource.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtectedResourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByLegalHoldOutput:
    boto3_raw_data: "type_defs.ListRecoveryPointsByLegalHoldOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecoveryPoints(self):  # pragma: no cover
        return RecoveryPointMember.make_many(self.boto3_raw_data["RecoveryPoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByLegalHoldOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByLegalHoldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByResourceOutput:
    boto3_raw_data: "type_defs.ListRecoveryPointsByResourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecoveryPoints(self):  # pragma: no cover
        return RecoveryPointByResource.make_many(self.boto3_raw_data["RecoveryPoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByResourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobSummariesOutput:
    boto3_raw_data: "type_defs.ListRestoreJobSummariesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreJobSummaries(self):  # pragma: no cover
        return RestoreJobSummary.make_many(self.boto3_raw_data["RestoreJobSummaries"])

    AggregationPeriod = field("AggregationPeriod")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRestoreJobSummariesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobSummariesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreTestingPlansOutput:
    boto3_raw_data: "type_defs.ListRestoreTestingPlansOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreTestingPlans(self):  # pragma: no cover
        return RestoreTestingPlanForList.make_many(
            self.boto3_raw_data["RestoreTestingPlans"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRestoreTestingPlansOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreTestingPlansOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreTestingSelectionsOutput:
    boto3_raw_data: "type_defs.ListRestoreTestingSelectionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreTestingSelections(self):  # pragma: no cover
        return RestoreTestingSelectionForList.make_many(
            self.boto3_raw_data["RestoreTestingSelections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreTestingSelectionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreTestingSelectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportJob:
    boto3_raw_data: "type_defs.ReportJobTypeDef" = dataclasses.field()

    ReportJobId = field("ReportJobId")
    ReportPlanArn = field("ReportPlanArn")
    ReportTemplate = field("ReportTemplate")
    CreationTime = field("CreationTime")
    CompletionTime = field("CompletionTime")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ReportDestination(self):  # pragma: no cover
        return ReportDestination.make_one(self.boto3_raw_data["ReportDestination"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportPlan:
    boto3_raw_data: "type_defs.ReportPlanTypeDef" = dataclasses.field()

    ReportPlanArn = field("ReportPlanArn")
    ReportPlanName = field("ReportPlanName")
    ReportPlanDescription = field("ReportPlanDescription")

    @cached_property
    def ReportSetting(self):  # pragma: no cover
        return ReportSettingOutput.make_one(self.boto3_raw_data["ReportSetting"])

    @cached_property
    def ReportDeliveryChannel(self):  # pragma: no cover
        return ReportDeliveryChannelOutput.make_one(
            self.boto3_raw_data["ReportDeliveryChannel"]
        )

    DeploymentStatus = field("DeploymentStatus")
    CreationTime = field("CreationTime")
    LastAttemptedExecutionTime = field("LastAttemptedExecutionTime")
    LastSuccessfulExecutionTime = field("LastSuccessfulExecutionTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportPlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportPlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingPlanForGet:
    boto3_raw_data: "type_defs.RestoreTestingPlanForGetTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")

    @cached_property
    def RecoveryPointSelection(self):  # pragma: no cover
        return RestoreTestingRecoveryPointSelectionOutput.make_one(
            self.boto3_raw_data["RecoveryPointSelection"]
        )

    RestoreTestingPlanArn = field("RestoreTestingPlanArn")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    ScheduleExpression = field("ScheduleExpression")
    CreatorRequestId = field("CreatorRequestId")
    LastExecutionTime = field("LastExecutionTime")
    LastUpdateTime = field("LastUpdateTime")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartWindowHours = field("StartWindowHours")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTestingPlanForGetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingPlanForGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlanVersionsOutput:
    boto3_raw_data: "type_defs.ListBackupPlanVersionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BackupPlanVersionsList(self):  # pragma: no cover
        return BackupPlansListMember.make_many(
            self.boto3_raw_data["BackupPlanVersionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupPlanVersionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlanVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupPlansOutput:
    boto3_raw_data: "type_defs.ListBackupPlansOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupPlansList(self):  # pragma: no cover
        return BackupPlansListMember.make_many(self.boto3_raw_data["BackupPlansList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupPlansOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupPlansOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackupJobsOutput:
    boto3_raw_data: "type_defs.ListBackupJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupJobs(self):  # pragma: no cover
        return BackupJob.make_many(self.boto3_raw_data["BackupJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackupJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackupJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCopyJobOutput:
    boto3_raw_data: "type_defs.DescribeCopyJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def CopyJob(self):  # pragma: no cover
        return CopyJob.make_one(self.boto3_raw_data["CopyJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCopyJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCopyJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCopyJobsOutput:
    boto3_raw_data: "type_defs.ListCopyJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CopyJobs(self):  # pragma: no cover
        return CopyJob.make_many(self.boto3_raw_data["CopyJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCopyJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCopyJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupRule:
    boto3_raw_data: "type_defs.BackupRuleTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    TargetBackupVaultName = field("TargetBackupVaultName")
    ScheduleExpression = field("ScheduleExpression")
    StartWindowMinutes = field("StartWindowMinutes")
    CompletionWindowMinutes = field("CompletionWindowMinutes")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    RecoveryPointTags = field("RecoveryPointTags")
    RuleId = field("RuleId")

    @cached_property
    def CopyActions(self):  # pragma: no cover
        return CopyAction.make_many(self.boto3_raw_data["CopyActions"])

    EnableContinuousBackup = field("EnableContinuousBackup")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")

    @cached_property
    def IndexActions(self):  # pragma: no cover
        return IndexActionOutput.make_many(self.boto3_raw_data["IndexActions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsByBackupVaultOutput:
    boto3_raw_data: "type_defs.ListRecoveryPointsByBackupVaultOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecoveryPoints(self):  # pragma: no cover
        return RecoveryPointByBackupVault.make_many(
            self.boto3_raw_data["RecoveryPoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsByBackupVaultOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsByBackupVaultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupSelectionOutput:
    boto3_raw_data: "type_defs.BackupSelectionOutputTypeDef" = dataclasses.field()

    SelectionName = field("SelectionName")
    IamRoleArn = field("IamRoleArn")
    Resources = field("Resources")

    @cached_property
    def ListOfTags(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["ListOfTags"])

    NotResources = field("NotResources")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return ConditionsOutput.make_one(self.boto3_raw_data["Conditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupSelectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupSelection:
    boto3_raw_data: "type_defs.BackupSelectionTypeDef" = dataclasses.field()

    SelectionName = field("SelectionName")
    IamRoleArn = field("IamRoleArn")
    Resources = field("Resources")

    @cached_property
    def ListOfTags(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["ListOfTags"])

    NotResources = field("NotResources")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Conditions.make_one(self.boto3_raw_data["Conditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupSelectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupSelectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFrameworkOutput:
    boto3_raw_data: "type_defs.DescribeFrameworkOutputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")
    FrameworkArn = field("FrameworkArn")
    FrameworkDescription = field("FrameworkDescription")

    @cached_property
    def FrameworkControls(self):  # pragma: no cover
        return FrameworkControlOutput.make_many(
            self.boto3_raw_data["FrameworkControls"]
        )

    CreationTime = field("CreationTime")
    DeploymentStatus = field("DeploymentStatus")
    FrameworkStatus = field("FrameworkStatus")
    IdempotencyToken = field("IdempotencyToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFrameworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFrameworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameworkControl:
    boto3_raw_data: "type_defs.FrameworkControlTypeDef" = dataclasses.field()

    ControlName = field("ControlName")

    @cached_property
    def ControlInputParameters(self):  # pragma: no cover
        return ControlInputParameter.make_many(
            self.boto3_raw_data["ControlInputParameters"]
        )

    ControlScope = field("ControlScope")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameworkControlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameworkControlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLegalHoldOutput:
    boto3_raw_data: "type_defs.CreateLegalHoldOutputTypeDef" = dataclasses.field()

    Title = field("Title")
    Status = field("Status")
    Description = field("Description")
    LegalHoldId = field("LegalHoldId")
    LegalHoldArn = field("LegalHoldArn")
    CreationDate = field("CreationDate")

    @cached_property
    def RecoveryPointSelection(self):  # pragma: no cover
        return RecoveryPointSelectionOutput.make_one(
            self.boto3_raw_data["RecoveryPointSelection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLegalHoldOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLegalHoldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLegalHoldOutput:
    boto3_raw_data: "type_defs.GetLegalHoldOutputTypeDef" = dataclasses.field()

    Title = field("Title")
    Status = field("Status")
    Description = field("Description")
    CancelDescription = field("CancelDescription")
    LegalHoldId = field("LegalHoldId")
    LegalHoldArn = field("LegalHoldArn")
    CreationDate = field("CreationDate")
    CancellationDate = field("CancellationDate")
    RetainRecordUntil = field("RetainRecordUntil")

    @cached_property
    def RecoveryPointSelection(self):  # pragma: no cover
        return RecoveryPointSelectionOutput.make_one(
            self.boto3_raw_data["RecoveryPointSelection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLegalHoldOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLegalHoldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPointSelection:
    boto3_raw_data: "type_defs.RecoveryPointSelectionTypeDef" = dataclasses.field()

    VaultNames = field("VaultNames")
    ResourceIdentifiers = field("ResourceIdentifiers")

    @cached_property
    def DateRange(self):  # pragma: no cover
        return DateRange.make_one(self.boto3_raw_data["DateRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointSelectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryPointSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobsByProtectedResourceOutput:
    boto3_raw_data: "type_defs.ListRestoreJobsByProtectedResourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreJobs(self):  # pragma: no cover
        return RestoreJobsListMember.make_many(self.boto3_raw_data["RestoreJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreJobsByProtectedResourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobsByProtectedResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreJobsOutput:
    boto3_raw_data: "type_defs.ListRestoreJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def RestoreJobs(self):  # pragma: no cover
        return RestoreJobsListMember.make_many(self.boto3_raw_data["RestoreJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRestoreJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupRuleInput:
    boto3_raw_data: "type_defs.BackupRuleInputTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    TargetBackupVaultName = field("TargetBackupVaultName")
    ScheduleExpression = field("ScheduleExpression")
    StartWindowMinutes = field("StartWindowMinutes")
    CompletionWindowMinutes = field("CompletionWindowMinutes")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return Lifecycle.make_one(self.boto3_raw_data["Lifecycle"])

    RecoveryPointTags = field("RecoveryPointTags")

    @cached_property
    def CopyActions(self):  # pragma: no cover
        return CopyAction.make_many(self.boto3_raw_data["CopyActions"])

    EnableContinuousBackup = field("EnableContinuousBackup")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    IndexActions = field("IndexActions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupRuleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupRuleInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingSelectionForGet:
    boto3_raw_data: "type_defs.RestoreTestingSelectionForGetTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    IamRoleArn = field("IamRoleArn")
    ProtectedResourceType = field("ProtectedResourceType")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")
    CreatorRequestId = field("CreatorRequestId")
    ProtectedResourceArns = field("ProtectedResourceArns")

    @cached_property
    def ProtectedResourceConditions(self):  # pragma: no cover
        return ProtectedResourceConditionsOutput.make_one(
            self.boto3_raw_data["ProtectedResourceConditions"]
        )

    RestoreMetadataOverrides = field("RestoreMetadataOverrides")
    ValidationWindowHours = field("ValidationWindowHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTestingSelectionForGetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingSelectionForGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRestoreAccessBackupVaultsOutput:
    boto3_raw_data: "type_defs.ListRestoreAccessBackupVaultsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreAccessBackupVaults(self):  # pragma: no cover
        return RestoreAccessBackupVaultListMember.make_many(
            self.boto3_raw_data["RestoreAccessBackupVaults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRestoreAccessBackupVaultsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRestoreAccessBackupVaultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReportJobOutput:
    boto3_raw_data: "type_defs.DescribeReportJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReportJob(self):  # pragma: no cover
        return ReportJob.make_one(self.boto3_raw_data["ReportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReportJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReportJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportJobsOutput:
    boto3_raw_data: "type_defs.ListReportJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReportJobs(self):  # pragma: no cover
        return ReportJob.make_many(self.boto3_raw_data["ReportJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReportPlanOutput:
    boto3_raw_data: "type_defs.DescribeReportPlanOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReportPlan(self):  # pragma: no cover
        return ReportPlan.make_one(self.boto3_raw_data["ReportPlan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReportPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReportPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReportPlansOutput:
    boto3_raw_data: "type_defs.ListReportPlansOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReportPlans(self):  # pragma: no cover
        return ReportPlan.make_many(self.boto3_raw_data["ReportPlans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReportPlansOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReportPlansOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReportPlanInput:
    boto3_raw_data: "type_defs.CreateReportPlanInputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")
    ReportDeliveryChannel = field("ReportDeliveryChannel")
    ReportSetting = field("ReportSetting")
    ReportPlanDescription = field("ReportPlanDescription")
    ReportPlanTags = field("ReportPlanTags")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReportPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReportPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReportPlanInput:
    boto3_raw_data: "type_defs.UpdateReportPlanInputTypeDef" = dataclasses.field()

    ReportPlanName = field("ReportPlanName")
    ReportPlanDescription = field("ReportPlanDescription")
    ReportDeliveryChannel = field("ReportDeliveryChannel")
    ReportSetting = field("ReportSetting")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReportPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReportPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreTestingPlanOutput:
    boto3_raw_data: "type_defs.GetRestoreTestingPlanOutputTypeDef" = dataclasses.field()

    @cached_property
    def RestoreTestingPlan(self):  # pragma: no cover
        return RestoreTestingPlanForGet.make_one(
            self.boto3_raw_data["RestoreTestingPlan"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRestoreTestingPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreTestingPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingPlanForCreate:
    boto3_raw_data: "type_defs.RestoreTestingPlanForCreateTypeDef" = dataclasses.field()

    RecoveryPointSelection = field("RecoveryPointSelection")
    RestoreTestingPlanName = field("RestoreTestingPlanName")
    ScheduleExpression = field("ScheduleExpression")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartWindowHours = field("StartWindowHours")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTestingPlanForCreateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingPlanForCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingPlanForUpdate:
    boto3_raw_data: "type_defs.RestoreTestingPlanForUpdateTypeDef" = dataclasses.field()

    RecoveryPointSelection = field("RecoveryPointSelection")
    ScheduleExpression = field("ScheduleExpression")
    ScheduleExpressionTimezone = field("ScheduleExpressionTimezone")
    StartWindowHours = field("StartWindowHours")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreTestingPlanForUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingPlanForUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupPlan:
    boto3_raw_data: "type_defs.BackupPlanTypeDef" = dataclasses.field()

    BackupPlanName = field("BackupPlanName")

    @cached_property
    def Rules(self):  # pragma: no cover
        return BackupRule.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def AdvancedBackupSettings(self):  # pragma: no cover
        return AdvancedBackupSettingOutput.make_many(
            self.boto3_raw_data["AdvancedBackupSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupPlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupPlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupSelectionOutput:
    boto3_raw_data: "type_defs.GetBackupSelectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupSelection(self):  # pragma: no cover
        return BackupSelectionOutput.make_one(self.boto3_raw_data["BackupSelection"])

    SelectionId = field("SelectionId")
    BackupPlanId = field("BackupPlanId")
    CreationDate = field("CreationDate")
    CreatorRequestId = field("CreatorRequestId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackupSelectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackupPlanInput:
    boto3_raw_data: "type_defs.BackupPlanInputTypeDef" = dataclasses.field()

    BackupPlanName = field("BackupPlanName")

    @cached_property
    def Rules(self):  # pragma: no cover
        return BackupRuleInput.make_many(self.boto3_raw_data["Rules"])

    AdvancedBackupSettings = field("AdvancedBackupSettings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupPlanInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupPlanInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestoreTestingSelectionOutput:
    boto3_raw_data: "type_defs.GetRestoreTestingSelectionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreTestingSelection(self):  # pragma: no cover
        return RestoreTestingSelectionForGet.make_one(
            self.boto3_raw_data["RestoreTestingSelection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRestoreTestingSelectionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestoreTestingSelectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingSelectionForCreate:
    boto3_raw_data: "type_defs.RestoreTestingSelectionForCreateTypeDef" = (
        dataclasses.field()
    )

    IamRoleArn = field("IamRoleArn")
    ProtectedResourceType = field("ProtectedResourceType")
    RestoreTestingSelectionName = field("RestoreTestingSelectionName")
    ProtectedResourceArns = field("ProtectedResourceArns")
    ProtectedResourceConditions = field("ProtectedResourceConditions")
    RestoreMetadataOverrides = field("RestoreMetadataOverrides")
    ValidationWindowHours = field("ValidationWindowHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTestingSelectionForCreateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingSelectionForCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTestingSelectionForUpdate:
    boto3_raw_data: "type_defs.RestoreTestingSelectionForUpdateTypeDef" = (
        dataclasses.field()
    )

    IamRoleArn = field("IamRoleArn")
    ProtectedResourceArns = field("ProtectedResourceArns")
    ProtectedResourceConditions = field("ProtectedResourceConditions")
    RestoreMetadataOverrides = field("RestoreMetadataOverrides")
    ValidationWindowHours = field("ValidationWindowHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTestingSelectionForUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTestingSelectionForUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestoreTestingPlanInput:
    boto3_raw_data: "type_defs.CreateRestoreTestingPlanInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreTestingPlan(self):  # pragma: no cover
        return RestoreTestingPlanForCreate.make_one(
            self.boto3_raw_data["RestoreTestingPlan"]
        )

    CreatorRequestId = field("CreatorRequestId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRestoreTestingPlanInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestoreTestingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRestoreTestingPlanInput:
    boto3_raw_data: "type_defs.UpdateRestoreTestingPlanInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RestoreTestingPlan(self):  # pragma: no cover
        return RestoreTestingPlanForUpdate.make_one(
            self.boto3_raw_data["RestoreTestingPlan"]
        )

    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRestoreTestingPlanInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRestoreTestingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupPlanFromJSONOutput:
    boto3_raw_data: "type_defs.GetBackupPlanFromJSONOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupPlan(self):  # pragma: no cover
        return BackupPlan.make_one(self.boto3_raw_data["BackupPlan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackupPlanFromJSONOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupPlanFromJSONOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupPlanFromTemplateOutput:
    boto3_raw_data: "type_defs.GetBackupPlanFromTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BackupPlanDocument(self):  # pragma: no cover
        return BackupPlan.make_one(self.boto3_raw_data["BackupPlanDocument"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBackupPlanFromTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupPlanFromTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackupPlanOutput:
    boto3_raw_data: "type_defs.GetBackupPlanOutputTypeDef" = dataclasses.field()

    @cached_property
    def BackupPlan(self):  # pragma: no cover
        return BackupPlan.make_one(self.boto3_raw_data["BackupPlan"])

    BackupPlanId = field("BackupPlanId")
    BackupPlanArn = field("BackupPlanArn")
    VersionId = field("VersionId")
    CreatorRequestId = field("CreatorRequestId")
    CreationDate = field("CreationDate")
    DeletionDate = field("DeletionDate")
    LastExecutionDate = field("LastExecutionDate")

    @cached_property
    def AdvancedBackupSettings(self):  # pragma: no cover
        return AdvancedBackupSettingOutput.make_many(
            self.boto3_raw_data["AdvancedBackupSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackupPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackupPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupSelectionInput:
    boto3_raw_data: "type_defs.CreateBackupSelectionInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")
    BackupSelection = field("BackupSelection")
    CreatorRequestId = field("CreatorRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupSelectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFrameworkInput:
    boto3_raw_data: "type_defs.CreateFrameworkInputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")
    FrameworkControls = field("FrameworkControls")
    FrameworkDescription = field("FrameworkDescription")
    IdempotencyToken = field("IdempotencyToken")
    FrameworkTags = field("FrameworkTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFrameworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFrameworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFrameworkInput:
    boto3_raw_data: "type_defs.UpdateFrameworkInputTypeDef" = dataclasses.field()

    FrameworkName = field("FrameworkName")
    FrameworkDescription = field("FrameworkDescription")
    FrameworkControls = field("FrameworkControls")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFrameworkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFrameworkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLegalHoldInput:
    boto3_raw_data: "type_defs.CreateLegalHoldInputTypeDef" = dataclasses.field()

    Title = field("Title")
    Description = field("Description")
    IdempotencyToken = field("IdempotencyToken")
    RecoveryPointSelection = field("RecoveryPointSelection")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLegalHoldInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLegalHoldInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackupPlanInput:
    boto3_raw_data: "type_defs.CreateBackupPlanInputTypeDef" = dataclasses.field()

    @cached_property
    def BackupPlan(self):  # pragma: no cover
        return BackupPlanInput.make_one(self.boto3_raw_data["BackupPlan"])

    BackupPlanTags = field("BackupPlanTags")
    CreatorRequestId = field("CreatorRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackupPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackupPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackupPlanInput:
    boto3_raw_data: "type_defs.UpdateBackupPlanInputTypeDef" = dataclasses.field()

    BackupPlanId = field("BackupPlanId")

    @cached_property
    def BackupPlan(self):  # pragma: no cover
        return BackupPlanInput.make_one(self.boto3_raw_data["BackupPlan"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackupPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackupPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestoreTestingSelectionInput:
    boto3_raw_data: "type_defs.CreateRestoreTestingSelectionInputTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @cached_property
    def RestoreTestingSelection(self):  # pragma: no cover
        return RestoreTestingSelectionForCreate.make_one(
            self.boto3_raw_data["RestoreTestingSelection"]
        )

    CreatorRequestId = field("CreatorRequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRestoreTestingSelectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestoreTestingSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRestoreTestingSelectionInput:
    boto3_raw_data: "type_defs.UpdateRestoreTestingSelectionInputTypeDef" = (
        dataclasses.field()
    )

    RestoreTestingPlanName = field("RestoreTestingPlanName")

    @cached_property
    def RestoreTestingSelection(self):  # pragma: no cover
        return RestoreTestingSelectionForUpdate.make_one(
            self.boto3_raw_data["RestoreTestingSelection"]
        )

    RestoreTestingSelectionName = field("RestoreTestingSelectionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRestoreTestingSelectionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRestoreTestingSelectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
