# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connect import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActionSummary:
    boto3_raw_data: "type_defs.ActionSummaryTypeDef" = dataclasses.field()

    ActionType = field("ActionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateEvaluationFormRequest:
    boto3_raw_data: "type_defs.ActivateEvaluationFormRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateEvaluationFormRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateEvaluationFormRequestTypeDef"]
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
class EmailRecipient:
    boto3_raw_data: "type_defs.EmailRecipientTypeDef" = dataclasses.field()

    Address = field("Address")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailRecipientTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailRecipientTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Distribution:
    boto3_raw_data: "type_defs.DistributionTypeDef" = dataclasses.field()

    Region = field("Region")
    Percentage = field("Percentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DistributionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DistributionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueReference:
    boto3_raw_data: "type_defs.QueueReferenceTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentHierarchyGroup:
    boto3_raw_data: "type_defs.AgentHierarchyGroupTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentHierarchyGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentHierarchyGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentHierarchyGroups:
    boto3_raw_data: "type_defs.AgentHierarchyGroupsTypeDef" = dataclasses.field()

    L1Ids = field("L1Ids")
    L2Ids = field("L2Ids")
    L3Ids = field("L3Ids")
    L4Ids = field("L4Ids")
    L5Ids = field("L5Ids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentHierarchyGroupsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentHierarchyGroupsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceInfo:
    boto3_raw_data: "type_defs.DeviceInfoTypeDef" = dataclasses.field()

    PlatformName = field("PlatformName")
    PlatformVersion = field("PlatformVersion")
    OperatingSystem = field("OperatingSystem")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantCapabilities:
    boto3_raw_data: "type_defs.ParticipantCapabilitiesTypeDef" = dataclasses.field()

    Video = field("Video")
    ScreenShare = field("ScreenShare")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateTransition:
    boto3_raw_data: "type_defs.StateTransitionTypeDef" = dataclasses.field()

    State = field("State")
    StateStartTimestamp = field("StateStartTimestamp")
    StateEndTimestamp = field("StateEndTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StateTransitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StateTransitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioQualityMetricsInfo:
    boto3_raw_data: "type_defs.AudioQualityMetricsInfoTypeDef" = dataclasses.field()

    QualityScore = field("QualityScore")
    PotentialQualityIssues = field("PotentialQualityIssues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioQualityMetricsInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioQualityMetricsInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatusIdentifier:
    boto3_raw_data: "type_defs.AgentStatusIdentifierTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentStatusIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentStatusIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatusReference:
    boto3_raw_data: "type_defs.AgentStatusReferenceTypeDef" = dataclasses.field()

    StatusStartTimestamp = field("StatusStartTimestamp")
    StatusArn = field("StatusArn")
    StatusName = field("StatusName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentStatusReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentStatusReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringCondition:
    boto3_raw_data: "type_defs.StringConditionTypeDef" = dataclasses.field()

    FieldName = field("FieldName")
    Value = field("Value")
    ComparisonType = field("ComparisonType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StringConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StringConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatusSummary:
    boto3_raw_data: "type_defs.AgentStatusSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Type = field("Type")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentStatusSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentStatusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatus:
    boto3_raw_data: "type_defs.AgentStatusTypeDef" = dataclasses.field()

    AgentStatusARN = field("AgentStatusARN")
    AgentStatusId = field("AgentStatusId")
    Name = field("Name")
    Description = field("Description")
    Type = field("Type")
    DisplayOrder = field("DisplayOrder")
    State = field("State")
    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentsCriteriaOutput:
    boto3_raw_data: "type_defs.AgentsCriteriaOutputTypeDef" = dataclasses.field()

    AgentIds = field("AgentIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentsCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentsCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentsCriteria:
    boto3_raw_data: "type_defs.AgentsCriteriaTypeDef" = dataclasses.field()

    AgentIds = field("AgentIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentsCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentsCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsDataAssociationResult:
    boto3_raw_data: "type_defs.AnalyticsDataAssociationResultTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")
    TargetAccountId = field("TargetAccountId")
    ResourceShareId = field("ResourceShareId")
    ResourceShareArn = field("ResourceShareArn")
    ResourceShareStatus = field("ResourceShareStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalyticsDataAssociationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsDataAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsDataSetsResult:
    boto3_raw_data: "type_defs.AnalyticsDataSetsResultTypeDef" = dataclasses.field()

    DataSetId = field("DataSetId")
    DataSetName = field("DataSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsDataSetsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsDataSetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnswerMachineDetectionConfig:
    boto3_raw_data: "type_defs.AnswerMachineDetectionConfigTypeDef" = (
        dataclasses.field()
    )

    EnableAnswerMachineDetection = field("EnableAnswerMachineDetection")
    AwaitAnswerMachinePrompt = field("AwaitAnswerMachinePrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnswerMachineDetectionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnswerMachineDetectionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationOutput:
    boto3_raw_data: "type_defs.ApplicationOutputTypeDef" = dataclasses.field()

    Namespace = field("Namespace")
    ApplicationPermissions = field("ApplicationPermissions")

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

    Namespace = field("Namespace")
    ApplicationPermissions = field("ApplicationPermissions")

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
class AssociateAnalyticsDataSetRequest:
    boto3_raw_data: "type_defs.AssociateAnalyticsDataSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    DataSetId = field("DataSetId")
    TargetAccountId = field("TargetAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateAnalyticsDataSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAnalyticsDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApprovedOriginRequest:
    boto3_raw_data: "type_defs.AssociateApprovedOriginRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Origin = field("Origin")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateApprovedOriginRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApprovedOriginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexBot:
    boto3_raw_data: "type_defs.LexBotTypeDef" = dataclasses.field()

    Name = field("Name")
    LexRegion = field("LexRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LexBotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LexBotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexV2Bot:
    boto3_raw_data: "type_defs.LexV2BotTypeDef" = dataclasses.field()

    AliasArn = field("AliasArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LexV2BotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LexV2BotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDefaultVocabularyRequest:
    boto3_raw_data: "type_defs.AssociateDefaultVocabularyRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    LanguageCode = field("LanguageCode")
    VocabularyId = field("VocabularyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDefaultVocabularyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDefaultVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFlowRequest:
    boto3_raw_data: "type_defs.AssociateFlowRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ResourceId = field("ResourceId")
    FlowId = field("FlowId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLambdaFunctionRequest:
    boto3_raw_data: "type_defs.AssociateLambdaFunctionRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    FunctionArn = field("FunctionArn")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateLambdaFunctionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLambdaFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePhoneNumberContactFlowRequest:
    boto3_raw_data: "type_defs.AssociatePhoneNumberContactFlowRequestTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberId = field("PhoneNumberId")
    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePhoneNumberContactFlowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePhoneNumberContactFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateQueueQuickConnectsRequest:
    boto3_raw_data: "type_defs.AssociateQueueQuickConnectsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    QuickConnectIds = field("QuickConnectIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateQueueQuickConnectsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateQueueQuickConnectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSecurityKeyRequest:
    boto3_raw_data: "type_defs.AssociateSecurityKeyRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Key = field("Key")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateSecurityKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSecurityKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTrafficDistributionGroupUserRequest:
    boto3_raw_data: "type_defs.AssociateTrafficDistributionGroupUserRequestTypeDef" = (
        dataclasses.field()
    )

    TrafficDistributionGroupId = field("TrafficDistributionGroupId")
    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateTrafficDistributionGroupUserRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTrafficDistributionGroupUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserProficiency:
    boto3_raw_data: "type_defs.UserProficiencyTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValue = field("AttributeValue")
    Level = field("Level")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserProficiencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserProficiencyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedContactSummary:
    boto3_raw_data: "type_defs.AssociatedContactSummaryTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    ContactArn = field("ContactArn")
    InitiationTimestamp = field("InitiationTimestamp")
    DisconnectTimestamp = field("DisconnectTimestamp")
    InitialContactId = field("InitialContactId")
    PreviousContactId = field("PreviousContactId")
    RelatedContactId = field("RelatedContactId")
    InitiationMethod = field("InitiationMethod")
    Channel = field("Channel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedContactSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedContactSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachedFileError:
    boto3_raw_data: "type_defs.AttachedFileErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    FileId = field("FileId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachedFileErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachedFileErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatedByInfo:
    boto3_raw_data: "type_defs.CreatedByInfoTypeDef" = dataclasses.field()

    ConnectUserArn = field("ConnectUserArn")
    AWSIdentityArn = field("AWSIdentityArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreatedByInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreatedByInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentReference:
    boto3_raw_data: "type_defs.AttachmentReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    Status = field("Status")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachmentReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attendee:
    boto3_raw_data: "type_defs.AttendeeTypeDef" = dataclasses.field()

    AttendeeId = field("AttendeeId")
    JoinToken = field("JoinToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttendeeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttendeeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyGroupCondition:
    boto3_raw_data: "type_defs.HierarchyGroupConditionTypeDef" = dataclasses.field()

    Value = field("Value")
    HierarchyGroupMatchType = field("HierarchyGroupMatchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchyGroupConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyGroupConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCondition:
    boto3_raw_data: "type_defs.TagConditionTypeDef" = dataclasses.field()

    TagKey = field("TagKey")
    TagValue = field("TagValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    MinProficiencyLevel = field("MinProficiencyLevel")
    MaxProficiencyLevel = field("MaxProficiencyLevel")

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
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    AttributeType = field("AttributeType")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioFeatures:
    boto3_raw_data: "type_defs.AudioFeaturesTypeDef" = dataclasses.field()

    EchoReduction = field("EchoReduction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioFeaturesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioFeaturesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationProfileSummary:
    boto3_raw_data: "type_defs.AuthenticationProfileSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    IsDefault = field("IsDefault")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationProfile:
    boto3_raw_data: "type_defs.AuthenticationProfileTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    AllowedIps = field("AllowedIps")
    BlockedIps = field("BlockedIps")
    IsDefault = field("IsDefault")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")
    PeriodicSessionDuration = field("PeriodicSessionDuration")
    MaxSessionDuration = field("MaxSessionDuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailableNumberSummary:
    boto3_raw_data: "type_defs.AvailableNumberSummaryTypeDef" = dataclasses.field()

    PhoneNumber = field("PhoneNumber")
    PhoneNumberCountryCode = field("PhoneNumberCountryCode")
    PhoneNumberType = field("PhoneNumberType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailableNumberSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailableNumberSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateAnalyticsDataSetRequest:
    boto3_raw_data: "type_defs.BatchAssociateAnalyticsDataSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    DataSetIds = field("DataSetIds")
    TargetAccountId = field("TargetAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateAnalyticsDataSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateAnalyticsDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorResult:
    boto3_raw_data: "type_defs.ErrorResultTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateAnalyticsDataSetRequest:
    boto3_raw_data: "type_defs.BatchDisassociateAnalyticsDataSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    DataSetIds = field("DataSetIds")
    TargetAccountId = field("TargetAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateAnalyticsDataSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateAnalyticsDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAttachedFileMetadataRequest:
    boto3_raw_data: "type_defs.BatchGetAttachedFileMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    FileIds = field("FileIds")
    InstanceId = field("InstanceId")
    AssociatedResourceArn = field("AssociatedResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAttachedFileMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAttachedFileMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFlowAssociationRequest:
    boto3_raw_data: "type_defs.BatchGetFlowAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ResourceIds = field("ResourceIds")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFlowAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFlowAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowAssociationSummary:
    boto3_raw_data: "type_defs.FlowAssociationSummaryTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    FlowId = field("FlowId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedRequest:
    boto3_raw_data: "type_defs.FailedRequestTypeDef" = dataclasses.field()

    RequestIdentifier = field("RequestIdentifier")
    FailureReasonCode = field("FailureReasonCode")
    FailureReasonMessage = field("FailureReasonMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulRequest:
    boto3_raw_data: "type_defs.SuccessfulRequestTypeDef" = dataclasses.field()

    RequestIdentifier = field("RequestIdentifier")
    ContactId = field("ContactId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuccessfulRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Campaign:
    boto3_raw_data: "type_defs.CampaignTypeDef" = dataclasses.field()

    CampaignId = field("CampaignId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValueUnionOutput:
    boto3_raw_data: "type_defs.FieldValueUnionOutputTypeDef" = dataclasses.field()

    BooleanValue = field("BooleanValue")
    DoubleValue = field("DoubleValue")
    EmptyValue = field("EmptyValue")
    StringValue = field("StringValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldValueUnionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValueUnionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatContactMetrics:
    boto3_raw_data: "type_defs.ChatContactMetricsTypeDef" = dataclasses.field()

    MultiParty = field("MultiParty")
    TotalMessages = field("TotalMessages")
    TotalBotMessages = field("TotalBotMessages")
    TotalBotMessageLengthInChars = field("TotalBotMessageLengthInChars")
    ConversationCloseTimeInMillis = field("ConversationCloseTimeInMillis")
    ConversationTurnCount = field("ConversationTurnCount")
    AgentFirstResponseTimestamp = field("AgentFirstResponseTimestamp")
    AgentFirstResponseTimeInMillis = field("AgentFirstResponseTimeInMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChatContactMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatContactMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatEvent:
    boto3_raw_data: "type_defs.ChatEventTypeDef" = dataclasses.field()

    Type = field("Type")
    ContentType = field("ContentType")
    Content = field("Content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatMessage:
    boto3_raw_data: "type_defs.ChatMessageTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Content = field("Content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantMetrics:
    boto3_raw_data: "type_defs.ParticipantMetricsTypeDef" = dataclasses.field()

    ParticipantId = field("ParticipantId")
    ParticipantType = field("ParticipantType")
    ConversationAbandon = field("ConversationAbandon")
    MessagesSent = field("MessagesSent")
    NumResponses = field("NumResponses")
    MessageLengthInChars = field("MessageLengthInChars")
    TotalResponseTimeInMillis = field("TotalResponseTimeInMillis")
    MaxResponseTimeInMillis = field("MaxResponseTimeInMillis")
    LastMessageTimestamp = field("LastMessageTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatStreamingConfiguration:
    boto3_raw_data: "type_defs.ChatStreamingConfigurationTypeDef" = dataclasses.field()

    StreamingEndpointArn = field("StreamingEndpointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChatStreamingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatStreamingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimPhoneNumberRequest:
    boto3_raw_data: "type_defs.ClaimPhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumber = field("PhoneNumber")
    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    PhoneNumberDescription = field("PhoneNumberDescription")
    Tags = field("Tags")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClaimPhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimPhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberStatus:
    boto3_raw_data: "type_defs.PhoneNumberStatusTypeDef" = dataclasses.field()

    Status = field("Status")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteAttachedFileUploadRequest:
    boto3_raw_data: "type_defs.CompleteAttachedFileUploadRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    FileId = field("FileId")
    AssociatedResourceArn = field("AssociatedResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteAttachedFileUploadRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteAttachedFileUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberCondition:
    boto3_raw_data: "type_defs.NumberConditionTypeDef" = dataclasses.field()

    FieldName = field("FieldName")
    MinValue = field("MinValue")
    MaxValue = field("MaxValue")
    ComparisonType = field("ComparisonType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NumberConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NumberConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactConfiguration:
    boto3_raw_data: "type_defs.ContactConfigurationTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    ParticipantRole = field("ParticipantRole")
    IncludeRawMessage = field("IncludeRawMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactConfigurationTypeDef"]
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

    Type = field("Type")
    Address = field("Address")

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
class ContactDetails:
    boto3_raw_data: "type_defs.ContactDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactEvaluation:
    boto3_raw_data: "type_defs.ContactEvaluationTypeDef" = dataclasses.field()

    FormId = field("FormId")
    EvaluationArn = field("EvaluationArn")
    Status = field("Status")
    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")
    DeleteTimestamp = field("DeleteTimestamp")
    ExportLocation = field("ExportLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactEvaluationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactEvaluationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFilter:
    boto3_raw_data: "type_defs.ContactFilterTypeDef" = dataclasses.field()

    ContactStates = field("ContactStates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowModuleSummary:
    boto3_raw_data: "type_defs.ContactFlowModuleSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactFlowModuleSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowModuleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowModule:
    boto3_raw_data: "type_defs.ContactFlowModuleTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    Content = field("Content")
    Description = field("Description")
    State = field("State")
    Status = field("Status")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactFlowModuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowModuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowSummary:
    boto3_raw_data: "type_defs.ContactFlowSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    ContactFlowType = field("ContactFlowType")
    ContactFlowState = field("ContactFlowState")
    ContactFlowStatus = field("ContactFlowStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactFlowSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlow:
    boto3_raw_data: "type_defs.ContactFlowTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    Type = field("Type")
    State = field("State")
    Status = field("Status")
    Description = field("Description")
    Content = field("Content")
    Tags = field("Tags")
    FlowContentSha256 = field("FlowContentSha256")
    Version = field("Version")
    VersionDescription = field("VersionDescription")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactFlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactFlowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowVersionSummary:
    boto3_raw_data: "type_defs.ContactFlowVersionSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    VersionDescription = field("VersionDescription")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactFlowVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactMetricInfo:
    boto3_raw_data: "type_defs.ContactMetricInfoTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactMetricInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactMetricInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactMetricValue:
    boto3_raw_data: "type_defs.ContactMetricValueTypeDef" = dataclasses.field()

    Number = field("Number")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactMetricValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactMetricValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactSearchSummaryAgentInfo:
    boto3_raw_data: "type_defs.ContactSearchSummaryAgentInfoTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ConnectedToAgentTimestamp = field("ConnectedToAgentTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContactSearchSummaryAgentInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactSearchSummaryAgentInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactSearchSummaryQueueInfo:
    boto3_raw_data: "type_defs.ContactSearchSummaryQueueInfoTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    EnqueueTimestamp = field("EnqueueTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContactSearchSummaryQueueInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactSearchSummaryQueueInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactSearchSummarySegmentAttributeValue:
    boto3_raw_data: "type_defs.ContactSearchSummarySegmentAttributeValueTypeDef" = (
        dataclasses.field()
    )

    ValueString = field("ValueString")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContactSearchSummarySegmentAttributeValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactSearchSummarySegmentAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerVoiceActivity:
    boto3_raw_data: "type_defs.CustomerVoiceActivityTypeDef" = dataclasses.field()

    GreetingStartTimestamp = field("GreetingStartTimestamp")
    GreetingEndTimestamp = field("GreetingEndTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerVoiceActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerVoiceActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectDetails:
    boto3_raw_data: "type_defs.DisconnectDetailsTypeDef" = dataclasses.field()

    PotentialDisconnectIssue = field("PotentialDisconnectIssue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisconnectDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointInfo:
    boto3_raw_data: "type_defs.EndpointInfoTypeDef" = dataclasses.field()

    Type = field("Type")
    Address = field("Address")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueInfo:
    boto3_raw_data: "type_defs.QueueInfoTypeDef" = dataclasses.field()

    Id = field("Id")
    EnqueueTimestamp = field("EnqueueTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingInfo:
    boto3_raw_data: "type_defs.RecordingInfoTypeDef" = dataclasses.field()

    StorageType = field("StorageType")
    Location = field("Location")
    MediaStreamType = field("MediaStreamType")
    ParticipantType = field("ParticipantType")
    FragmentStartNumber = field("FragmentStartNumber")
    FragmentStopNumber = field("FragmentStopNumber")
    StartTimestamp = field("StartTimestamp")
    StopTimestamp = field("StopTimestamp")
    Status = field("Status")
    DeletionReason = field("DeletionReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordingInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordingInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentAttributeValueOutput:
    boto3_raw_data: "type_defs.SegmentAttributeValueOutputTypeDef" = dataclasses.field()

    ValueString = field("ValueString")
    ValueMap = field("ValueMap")
    ValueInteger = field("ValueInteger")
    ValueList = field("ValueList")
    ValueArn = field("ValueArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentAttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WisdomInfo:
    boto3_raw_data: "type_defs.WisdomInfoTypeDef" = dataclasses.field()

    SessionArn = field("SessionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WisdomInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WisdomInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentStatusRequest:
    boto3_raw_data: "type_defs.CreateAgentStatusRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    State = field("State")
    Description = field("Description")
    DisplayOrder = field("DisplayOrder")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactFlowModuleRequest:
    boto3_raw_data: "type_defs.CreateContactFlowModuleRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Name = field("Name")
    Content = field("Content")
    Description = field("Description")
    Tags = field("Tags")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContactFlowModuleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactFlowModuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactFlowRequest:
    boto3_raw_data: "type_defs.CreateContactFlowRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    Type = field("Type")
    Content = field("Content")
    Description = field("Description")
    Status = field("Status")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Reference:
    boto3_raw_data: "type_defs.ReferenceTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")
    Status = field("Status")
    Arn = field("Arn")
    StatusReason = field("StatusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserInfo:
    boto3_raw_data: "type_defs.UserInfoTypeDef" = dataclasses.field()

    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailAddressRequest:
    boto3_raw_data: "type_defs.CreateEmailAddressRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    EmailAddress = field("EmailAddress")
    Description = field("Description")
    DisplayName = field("DisplayName")
    Tags = field("Tags")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEmailAddressRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormScoringStrategy:
    boto3_raw_data: "type_defs.EvaluationFormScoringStrategyTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvaluationFormScoringStrategyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormScoringStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceRequest:
    boto3_raw_data: "type_defs.CreateInstanceRequestTypeDef" = dataclasses.field()

    IdentityManagementType = field("IdentityManagementType")
    InboundCallsEnabled = field("InboundCallsEnabled")
    OutboundCallsEnabled = field("OutboundCallsEnabled")
    ClientToken = field("ClientToken")
    InstanceAlias = field("InstanceAlias")
    DirectoryId = field("DirectoryId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationAssociationRequest:
    boto3_raw_data: "type_defs.CreateIntegrationAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    IntegrationType = field("IntegrationType")
    IntegrationArn = field("IntegrationArn")
    SourceApplicationUrl = field("SourceApplicationUrl")
    SourceApplicationName = field("SourceApplicationName")
    SourceType = field("SourceType")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIntegrationAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantTokenCredentials:
    boto3_raw_data: "type_defs.ParticipantTokenCredentialsTypeDef" = dataclasses.field()

    ParticipantToken = field("ParticipantToken")
    Expiry = field("Expiry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantTokenCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantTokenCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePersistentContactAssociationRequest:
    boto3_raw_data: "type_defs.CreatePersistentContactAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    InitialContactId = field("InitialContactId")
    RehydrationType = field("RehydrationType")
    SourceContactId = field("SourceContactId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePersistentContactAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePersistentContactAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputPredefinedAttributeConfiguration:
    boto3_raw_data: "type_defs.InputPredefinedAttributeConfigurationTypeDef" = (
        dataclasses.field()
    )

    EnableValueValidationOnAssociation = field("EnableValueValidationOnAssociation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InputPredefinedAttributeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputPredefinedAttributeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptRequest:
    boto3_raw_data: "type_defs.CreatePromptRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    S3Uri = field("S3Uri")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundCallerConfig:
    boto3_raw_data: "type_defs.OutboundCallerConfigTypeDef" = dataclasses.field()

    OutboundCallerIdName = field("OutboundCallerIdName")
    OutboundCallerIdNumberId = field("OutboundCallerIdNumberId")
    OutboundFlowId = field("OutboundFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundCallerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundCallerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundEmailConfig:
    boto3_raw_data: "type_defs.OutboundEmailConfigTypeDef" = dataclasses.field()

    OutboundEmailAddressId = field("OutboundEmailAddressId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundEmailConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundEmailConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleTriggerEventSource:
    boto3_raw_data: "type_defs.RuleTriggerEventSourceTypeDef" = dataclasses.field()

    EventSourceName = field("EventSourceName")
    IntegrationAssociationId = field("IntegrationAssociationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleTriggerEventSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleTriggerEventSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficDistributionGroupRequest:
    boto3_raw_data: "type_defs.CreateTrafficDistributionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    InstanceId = field("InstanceId")
    Description = field("Description")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTrafficDistributionGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficDistributionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUseCaseRequest:
    boto3_raw_data: "type_defs.CreateUseCaseRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    IntegrationAssociationId = field("IntegrationAssociationId")
    UseCaseType = field("UseCaseType")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUseCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUseCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserHierarchyGroupRequest:
    boto3_raw_data: "type_defs.CreateUserHierarchyGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    InstanceId = field("InstanceId")
    ParentGroupId = field("ParentGroupId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateUserHierarchyGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserHierarchyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserIdentityInfo:
    boto3_raw_data: "type_defs.UserIdentityInfoTypeDef" = dataclasses.field()

    FirstName = field("FirstName")
    LastName = field("LastName")
    Email = field("Email")
    SecondaryEmail = field("SecondaryEmail")
    Mobile = field("Mobile")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserIdentityInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserIdentityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPhoneConfig:
    boto3_raw_data: "type_defs.UserPhoneConfigTypeDef" = dataclasses.field()

    PhoneType = field("PhoneType")
    AutoAccept = field("AutoAccept")
    AfterContactWorkTimeLimit = field("AfterContactWorkTimeLimit")
    DeskPhoneNumber = field("DeskPhoneNumber")
    PersistentConnection = field("PersistentConnection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserPhoneConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserPhoneConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewInputContent:
    boto3_raw_data: "type_defs.ViewInputContentTypeDef" = dataclasses.field()

    Template = field("Template")
    Actions = field("Actions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewInputContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewInputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateViewVersionRequest:
    boto3_raw_data: "type_defs.CreateViewVersionRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")
    VersionDescription = field("VersionDescription")
    ViewContentSha256 = field("ViewContentSha256")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateViewVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateViewVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVocabularyRequest:
    boto3_raw_data: "type_defs.CreateVocabularyRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    VocabularyName = field("VocabularyName")
    LanguageCode = field("LanguageCode")
    Content = field("Content")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVocabularyRequestTypeDef"]
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

    AccessToken = field("AccessToken")
    AccessTokenExpiration = field("AccessTokenExpiration")
    RefreshToken = field("RefreshToken")
    RefreshTokenExpiration = field("RefreshTokenExpiration")

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
class CrossChannelBehavior:
    boto3_raw_data: "type_defs.CrossChannelBehaviorTypeDef" = dataclasses.field()

    BehaviorType = field("BehaviorType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossChannelBehaviorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossChannelBehaviorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentMetric:
    boto3_raw_data: "type_defs.CurrentMetricTypeDef" = dataclasses.field()

    Name = field("Name")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CurrentMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CurrentMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentMetricSortCriteria:
    boto3_raw_data: "type_defs.CurrentMetricSortCriteriaTypeDef" = dataclasses.field()

    SortByMetric = field("SortByMetric")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CurrentMetricSortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrentMetricSortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateCondition:
    boto3_raw_data: "type_defs.DateConditionTypeDef" = dataclasses.field()

    FieldName = field("FieldName")
    Value = field("Value")
    ComparisonType = field("ComparisonType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateReference:
    boto3_raw_data: "type_defs.DateReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateEvaluationFormRequest:
    boto3_raw_data: "type_defs.DeactivateEvaluationFormRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateEvaluationFormRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateEvaluationFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultVocabulary:
    boto3_raw_data: "type_defs.DefaultVocabularyTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    LanguageCode = field("LanguageCode")
    VocabularyId = field("VocabularyId")
    VocabularyName = field("VocabularyName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefaultVocabularyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultVocabularyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttachedFileRequest:
    boto3_raw_data: "type_defs.DeleteAttachedFileRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    FileId = field("FileId")
    AssociatedResourceArn = field("AssociatedResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttachedFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttachedFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactEvaluationRequest:
    boto3_raw_data: "type_defs.DeleteContactEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationId = field("EvaluationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteContactEvaluationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactFlowModuleRequest:
    boto3_raw_data: "type_defs.DeleteContactFlowModuleRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowModuleId = field("ContactFlowModuleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteContactFlowModuleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactFlowModuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactFlowRequest:
    boto3_raw_data: "type_defs.DeleteContactFlowRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactFlowVersionRequest:
    boto3_raw_data: "type_defs.DeleteContactFlowVersionRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")
    ContactFlowVersion = field("ContactFlowVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteContactFlowVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactFlowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailAddressRequest:
    boto3_raw_data: "type_defs.DeleteEmailAddressRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    EmailAddressId = field("EmailAddressId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEmailAddressRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEvaluationFormRequest:
    boto3_raw_data: "type_defs.DeleteEvaluationFormRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEvaluationFormRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEvaluationFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHoursOfOperationOverrideRequest:
    boto3_raw_data: "type_defs.DeleteHoursOfOperationOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    HoursOfOperationOverrideId = field("HoursOfOperationOverrideId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteHoursOfOperationOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHoursOfOperationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHoursOfOperationRequest:
    boto3_raw_data: "type_defs.DeleteHoursOfOperationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteHoursOfOperationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHoursOfOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceRequest:
    boto3_raw_data: "type_defs.DeleteInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationAssociationRequest:
    boto3_raw_data: "type_defs.DeleteIntegrationAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    IntegrationAssociationId = field("IntegrationAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteIntegrationAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePredefinedAttributeRequest:
    boto3_raw_data: "type_defs.DeletePredefinedAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePredefinedAttributeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePredefinedAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePromptRequest:
    boto3_raw_data: "type_defs.DeletePromptRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PromptId = field("PromptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePushNotificationRegistrationRequest:
    boto3_raw_data: "type_defs.DeletePushNotificationRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RegistrationId = field("RegistrationId")
    ContactId = field("ContactId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePushNotificationRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePushNotificationRegistrationRequestTypeDef"]
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

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")

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
class DeleteQuickConnectRequest:
    boto3_raw_data: "type_defs.DeleteQuickConnectRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    QuickConnectId = field("QuickConnectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQuickConnectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQuickConnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRoutingProfileRequest:
    boto3_raw_data: "type_defs.DeleteRoutingProfileRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRoutingProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRoutingProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleRequest:
    boto3_raw_data: "type_defs.DeleteRuleRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    RuleId = field("RuleId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSecurityProfileRequest:
    boto3_raw_data: "type_defs.DeleteSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    SecurityProfileId = field("SecurityProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTaskTemplateRequest:
    boto3_raw_data: "type_defs.DeleteTaskTemplateRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    TaskTemplateId = field("TaskTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTaskTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaskTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrafficDistributionGroupRequest:
    boto3_raw_data: "type_defs.DeleteTrafficDistributionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    TrafficDistributionGroupId = field("TrafficDistributionGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTrafficDistributionGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrafficDistributionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUseCaseRequest:
    boto3_raw_data: "type_defs.DeleteUseCaseRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    IntegrationAssociationId = field("IntegrationAssociationId")
    UseCaseId = field("UseCaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUseCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUseCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserHierarchyGroupRequest:
    boto3_raw_data: "type_defs.DeleteUserHierarchyGroupRequestTypeDef" = (
        dataclasses.field()
    )

    HierarchyGroupId = field("HierarchyGroupId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteUserHierarchyGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserHierarchyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteViewRequest:
    boto3_raw_data: "type_defs.DeleteViewRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteViewRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteViewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteViewVersionRequest:
    boto3_raw_data: "type_defs.DeleteViewVersionRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")
    ViewVersion = field("ViewVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteViewVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteViewVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVocabularyRequest:
    boto3_raw_data: "type_defs.DeleteVocabularyRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    VocabularyId = field("VocabularyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgentStatusRequest:
    boto3_raw_data: "type_defs.DescribeAgentStatusRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    AgentStatusId = field("AgentStatusId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgentStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuthenticationProfileRequest:
    boto3_raw_data: "type_defs.DescribeAuthenticationProfileRequestTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileId = field("AuthenticationProfileId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAuthenticationProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuthenticationProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactEvaluationRequest:
    boto3_raw_data: "type_defs.DescribeContactEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationId = field("EvaluationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeContactEvaluationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactFlowModuleRequest:
    boto3_raw_data: "type_defs.DescribeContactFlowModuleRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowModuleId = field("ContactFlowModuleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeContactFlowModuleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactFlowModuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactFlowRequest:
    boto3_raw_data: "type_defs.DescribeContactFlowRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactRequest:
    boto3_raw_data: "type_defs.DescribeContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEmailAddressRequest:
    boto3_raw_data: "type_defs.DescribeEmailAddressRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    EmailAddressId = field("EmailAddressId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEmailAddressRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEmailAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEvaluationFormRequest:
    boto3_raw_data: "type_defs.DescribeEvaluationFormRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEvaluationFormRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEvaluationFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHoursOfOperationOverrideRequest:
    boto3_raw_data: "type_defs.DescribeHoursOfOperationOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    HoursOfOperationOverrideId = field("HoursOfOperationOverrideId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHoursOfOperationOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHoursOfOperationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHoursOfOperationRequest:
    boto3_raw_data: "type_defs.DescribeHoursOfOperationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeHoursOfOperationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHoursOfOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAttributeRequest:
    boto3_raw_data: "type_defs.DescribeInstanceAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AttributeType = field("AttributeType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstanceAttributeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceRequest:
    boto3_raw_data: "type_defs.DescribeInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceStorageConfigRequest:
    boto3_raw_data: "type_defs.DescribeInstanceStorageConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceStorageConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceStorageConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePhoneNumberRequest:
    boto3_raw_data: "type_defs.DescribePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePredefinedAttributeRequest:
    boto3_raw_data: "type_defs.DescribePredefinedAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePredefinedAttributeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePredefinedAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePromptRequest:
    boto3_raw_data: "type_defs.DescribePromptRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PromptId = field("PromptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Prompt:
    boto3_raw_data: "type_defs.PromptTypeDef" = dataclasses.field()

    PromptARN = field("PromptARN")
    PromptId = field("PromptId")
    Name = field("Name")
    Description = field("Description")
    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueueRequest:
    boto3_raw_data: "type_defs.DescribeQueueRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQuickConnectRequest:
    boto3_raw_data: "type_defs.DescribeQuickConnectRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    QuickConnectId = field("QuickConnectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQuickConnectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQuickConnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRoutingProfileRequest:
    boto3_raw_data: "type_defs.DescribeRoutingProfileRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRoutingProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRoutingProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleRequest:
    boto3_raw_data: "type_defs.DescribeRuleRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    RuleId = field("RuleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityProfileRequest:
    boto3_raw_data: "type_defs.DescribeSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileId = field("SecurityProfileId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSecurityProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfile:
    boto3_raw_data: "type_defs.SecurityProfileTypeDef" = dataclasses.field()

    Id = field("Id")
    OrganizationResourceId = field("OrganizationResourceId")
    Arn = field("Arn")
    SecurityProfileName = field("SecurityProfileName")
    Description = field("Description")
    Tags = field("Tags")
    AllowedAccessControlTags = field("AllowedAccessControlTags")
    TagRestrictedResources = field("TagRestrictedResources")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")
    HierarchyRestrictedResources = field("HierarchyRestrictedResources")
    AllowedAccessControlHierarchyGroupId = field("AllowedAccessControlHierarchyGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecurityProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecurityProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrafficDistributionGroupRequest:
    boto3_raw_data: "type_defs.DescribeTrafficDistributionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    TrafficDistributionGroupId = field("TrafficDistributionGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrafficDistributionGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrafficDistributionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficDistributionGroup:
    boto3_raw_data: "type_defs.TrafficDistributionGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    InstanceArn = field("InstanceArn")
    Status = field("Status")
    Tags = field("Tags")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficDistributionGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficDistributionGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserHierarchyGroupRequest:
    boto3_raw_data: "type_defs.DescribeUserHierarchyGroupRequestTypeDef" = (
        dataclasses.field()
    )

    HierarchyGroupId = field("HierarchyGroupId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserHierarchyGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserHierarchyGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserHierarchyStructureRequest:
    boto3_raw_data: "type_defs.DescribeUserHierarchyStructureRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserHierarchyStructureRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserHierarchyStructureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserRequest:
    boto3_raw_data: "type_defs.DescribeUserRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeViewRequest:
    boto3_raw_data: "type_defs.DescribeViewRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeViewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeViewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVocabularyRequest:
    boto3_raw_data: "type_defs.DescribeVocabularyRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    VocabularyId = field("VocabularyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVocabularyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vocabulary:
    boto3_raw_data: "type_defs.VocabularyTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Arn = field("Arn")
    LanguageCode = field("LanguageCode")
    State = field("State")
    LastModifiedTime = field("LastModifiedTime")
    FailureReason = field("FailureReason")
    Content = field("Content")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VocabularyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VocabularyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileReference:
    boto3_raw_data: "type_defs.RoutingProfileReferenceTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAnalyticsDataSetRequest:
    boto3_raw_data: "type_defs.DisassociateAnalyticsDataSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    DataSetId = field("DataSetId")
    TargetAccountId = field("TargetAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAnalyticsDataSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAnalyticsDataSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateApprovedOriginRequest:
    boto3_raw_data: "type_defs.DisassociateApprovedOriginRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Origin = field("Origin")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateApprovedOriginRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateApprovedOriginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFlowRequest:
    boto3_raw_data: "type_defs.DisassociateFlowRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateInstanceStorageConfigRequest:
    boto3_raw_data: "type_defs.DisassociateInstanceStorageConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")
    ResourceType = field("ResourceType")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateInstanceStorageConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateInstanceStorageConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLambdaFunctionRequest:
    boto3_raw_data: "type_defs.DisassociateLambdaFunctionRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    FunctionArn = field("FunctionArn")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateLambdaFunctionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLambdaFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateLexBotRequest:
    boto3_raw_data: "type_defs.DisassociateLexBotRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    BotName = field("BotName")
    LexRegion = field("LexRegion")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateLexBotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateLexBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePhoneNumberContactFlowRequest:
    boto3_raw_data: "type_defs.DisassociatePhoneNumberContactFlowRequestTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberId = field("PhoneNumberId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePhoneNumberContactFlowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePhoneNumberContactFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateQueueQuickConnectsRequest:
    boto3_raw_data: "type_defs.DisassociateQueueQuickConnectsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    QuickConnectIds = field("QuickConnectIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateQueueQuickConnectsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateQueueQuickConnectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileQueueReference:
    boto3_raw_data: "type_defs.RoutingProfileQueueReferenceTypeDef" = (
        dataclasses.field()
    )

    QueueId = field("QueueId")
    Channel = field("Channel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileQueueReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileQueueReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSecurityKeyRequest:
    boto3_raw_data: "type_defs.DisassociateSecurityKeyRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateSecurityKeyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSecurityKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTrafficDistributionGroupUserRequest:
    boto3_raw_data: (
        "type_defs.DisassociateTrafficDistributionGroupUserRequestTypeDef"
    ) = dataclasses.field()

    TrafficDistributionGroupId = field("TrafficDistributionGroupId")
    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateTrafficDistributionGroupUserRequestTypeDef"
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
                "type_defs.DisassociateTrafficDistributionGroupUserRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserProficiencyDisassociate:
    boto3_raw_data: "type_defs.UserProficiencyDisassociateTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserProficiencyDisassociateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserProficiencyDisassociateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectReason:
    boto3_raw_data: "type_defs.DisconnectReasonTypeDef" = dataclasses.field()

    Code = field("Code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisconnectReasonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DismissUserContactRequest:
    boto3_raw_data: "type_defs.DismissUserContactRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DismissUserContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DismissUserContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DownloadUrlMetadata:
    boto3_raw_data: "type_defs.DownloadUrlMetadataTypeDef" = dataclasses.field()

    Url = field("Url")
    UrlExpiry = field("UrlExpiry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DownloadUrlMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DownloadUrlMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailAddressInfo:
    boto3_raw_data: "type_defs.EmailAddressInfoTypeDef" = dataclasses.field()

    EmailAddress = field("EmailAddress")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailAddressInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailAddressInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailAddressMetadata:
    boto3_raw_data: "type_defs.EmailAddressMetadataTypeDef" = dataclasses.field()

    EmailAddressId = field("EmailAddressId")
    EmailAddressArn = field("EmailAddressArn")
    EmailAddress = field("EmailAddress")
    Description = field("Description")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailAddressMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailAddressMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailAttachment:
    boto3_raw_data: "type_defs.EmailAttachmentTypeDef" = dataclasses.field()

    FileName = field("FileName")
    S3Url = field("S3Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailAttachmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailMessageReference:
    boto3_raw_data: "type_defs.EmailMessageReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailMessageReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailMessageReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailReference:
    boto3_raw_data: "type_defs.EmailReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfig:
    boto3_raw_data: "type_defs.EncryptionConfigTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationAnswerData:
    boto3_raw_data: "type_defs.EvaluationAnswerDataTypeDef" = dataclasses.field()

    StringValue = field("StringValue")
    NumericValue = field("NumericValue")
    NotApplicable = field("NotApplicable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationAnswerDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationAnswerDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSectionOutput:
    boto3_raw_data: "type_defs.EvaluationFormSectionOutputTypeDef" = dataclasses.field()

    Title = field("Title")
    RefId = field("RefId")
    Items = field("Items")
    Instructions = field("Instructions")
    Weight = field("Weight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormSectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormSectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumericQuestionPropertyValueAutomation:
    boto3_raw_data: "type_defs.NumericQuestionPropertyValueAutomationTypeDef" = (
        dataclasses.field()
    )

    Label = field("Label")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NumericQuestionPropertyValueAutomationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NumericQuestionPropertyValueAutomationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormNumericQuestionOption:
    boto3_raw_data: "type_defs.EvaluationFormNumericQuestionOptionTypeDef" = (
        dataclasses.field()
    )

    MinValue = field("MinValue")
    MaxValue = field("MaxValue")
    Score = field("Score")
    AutomaticFail = field("AutomaticFail")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormNumericQuestionOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormNumericQuestionOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSection:
    boto3_raw_data: "type_defs.EvaluationFormSectionTypeDef" = dataclasses.field()

    Title = field("Title")
    RefId = field("RefId")
    Items = field("Items")
    Instructions = field("Instructions")
    Weight = field("Weight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormSectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormSectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleSelectQuestionRuleCategoryAutomation:
    boto3_raw_data: "type_defs.SingleSelectQuestionRuleCategoryAutomationTypeDef" = (
        dataclasses.field()
    )

    Category = field("Category")
    Condition = field("Condition")
    OptionRefId = field("OptionRefId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SingleSelectQuestionRuleCategoryAutomationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleSelectQuestionRuleCategoryAutomationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSingleSelectQuestionOption:
    boto3_raw_data: "type_defs.EvaluationFormSingleSelectQuestionOptionTypeDef" = (
        dataclasses.field()
    )

    RefId = field("RefId")
    Text = field("Text")
    Score = field("Score")
    AutomaticFail = field("AutomaticFail")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormSingleSelectQuestionOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormSingleSelectQuestionOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSummary:
    boto3_raw_data: "type_defs.EvaluationFormSummaryTypeDef" = dataclasses.field()

    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormArn = field("EvaluationFormArn")
    Title = field("Title")
    CreatedTime = field("CreatedTime")
    CreatedBy = field("CreatedBy")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedBy = field("LastModifiedBy")
    LatestVersion = field("LatestVersion")
    LastActivatedTime = field("LastActivatedTime")
    LastActivatedBy = field("LastActivatedBy")
    ActiveVersion = field("ActiveVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormVersionSummary:
    boto3_raw_data: "type_defs.EvaluationFormVersionSummaryTypeDef" = (
        dataclasses.field()
    )

    EvaluationFormArn = field("EvaluationFormArn")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")
    Locked = field("Locked")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    CreatedBy = field("CreatedBy")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedBy = field("LastModifiedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationScore:
    boto3_raw_data: "type_defs.EvaluationScoreTypeDef" = dataclasses.field()

    Percentage = field("Percentage")
    NotApplicable = field("NotApplicable")
    AutomaticFail = field("AutomaticFail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationScoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationNote:
    boto3_raw_data: "type_defs.EvaluationNoteTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationNoteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationNoteTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeActionDefinition:
    boto3_raw_data: "type_defs.EventBridgeActionDefinitionTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventBridgeActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Expiry:
    boto3_raw_data: "type_defs.ExpiryTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")
    ExpiryTimestamp = field("ExpiryTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpiryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpiryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValueUnion:
    boto3_raw_data: "type_defs.FieldValueUnionTypeDef" = dataclasses.field()

    BooleanValue = field("BooleanValue")
    DoubleValue = field("DoubleValue")
    EmptyValue = field("EmptyValue")
    StringValue = field("StringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldValueUnionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldValueUnionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterV2:
    boto3_raw_data: "type_defs.FilterV2TypeDef" = dataclasses.field()

    FilterKey = field("FilterKey")
    FilterValues = field("FilterValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterV2TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filters:
    boto3_raw_data: "type_defs.FiltersTypeDef" = dataclasses.field()

    Queues = field("Queues")
    Channels = field("Channels")
    RoutingProfiles = field("RoutingProfiles")
    RoutingStepExpressions = field("RoutingStepExpressions")
    AgentStatuses = field("AgentStatuses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FiltersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAttachedFileRequest:
    boto3_raw_data: "type_defs.GetAttachedFileRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    FileId = field("FileId")
    AssociatedResourceArn = field("AssociatedResourceArn")
    UrlExpiryInSeconds = field("UrlExpiryInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAttachedFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAttachedFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactAttributesRequest:
    boto3_raw_data: "type_defs.GetContactAttributesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    InitialContactId = field("InitialContactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectiveHoursOfOperationsRequest:
    boto3_raw_data: "type_defs.GetEffectiveHoursOfOperationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    FromDate = field("FromDate")
    ToDate = field("ToDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEffectiveHoursOfOperationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectiveHoursOfOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFederationTokenRequest:
    boto3_raw_data: "type_defs.GetFederationTokenRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFederationTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFederationTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowAssociationRequest:
    boto3_raw_data: "type_defs.GetFlowAssociationRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowAssociationRequestTypeDef"]
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
class IntervalDetails:
    boto3_raw_data: "type_defs.IntervalDetailsTypeDef" = dataclasses.field()

    TimeZone = field("TimeZone")
    IntervalPeriod = field("IntervalPeriod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntervalDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntervalDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPromptFileRequest:
    boto3_raw_data: "type_defs.GetPromptFileRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PromptId = field("PromptId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPromptFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPromptFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaskTemplateRequest:
    boto3_raw_data: "type_defs.GetTaskTemplateRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    TaskTemplateId = field("TaskTemplateId")
    SnapshotVersion = field("SnapshotVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaskTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaskTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficDistributionRequest:
    boto3_raw_data: "type_defs.GetTrafficDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTrafficDistributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyGroupSummaryReference:
    boto3_raw_data: "type_defs.HierarchyGroupSummaryReferenceTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HierarchyGroupSummaryReferenceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyGroupSummaryReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyGroupSummary:
    boto3_raw_data: "type_defs.HierarchyGroupSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchyGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyLevel:
    boto3_raw_data: "type_defs.HierarchyLevelTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HierarchyLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HierarchyLevelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyLevelUpdate:
    boto3_raw_data: "type_defs.HierarchyLevelUpdateTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchyLevelUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyLevelUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Threshold:
    boto3_raw_data: "type_defs.ThresholdTypeDef" = dataclasses.field()

    Comparison = field("Comparison")
    ThresholdValue = field("ThresholdValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThresholdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThresholdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationTimeSlice:
    boto3_raw_data: "type_defs.HoursOfOperationTimeSliceTypeDef" = dataclasses.field()

    Hours = field("Hours")
    Minutes = field("Minutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HoursOfOperationTimeSliceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationTimeSliceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideTimeSlice:
    boto3_raw_data: "type_defs.OverrideTimeSliceTypeDef" = dataclasses.field()

    Hours = field("Hours")
    Minutes = field("Minutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OverrideTimeSliceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideTimeSliceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationSummary:
    boto3_raw_data: "type_defs.HoursOfOperationSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HoursOfOperationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportPhoneNumberRequest:
    boto3_raw_data: "type_defs.ImportPhoneNumberRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    SourcePhoneNumberArn = field("SourcePhoneNumberArn")
    PhoneNumberDescription = field("PhoneNumberDescription")
    Tags = field("Tags")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportPhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportPhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundRawMessage:
    boto3_raw_data: "type_defs.InboundRawMessageTypeDef" = dataclasses.field()

    Subject = field("Subject")
    Body = field("Body")
    ContentType = field("ContentType")
    Headers = field("Headers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InboundRawMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundRawMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceStatusReason:
    boto3_raw_data: "type_defs.InstanceStatusReasonTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceStatusReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceStatusReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseConfig:
    boto3_raw_data: "type_defs.KinesisFirehoseConfigTypeDef" = dataclasses.field()

    FirehoseArn = field("FirehoseArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamConfig:
    boto3_raw_data: "type_defs.KinesisStreamConfigTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisStreamConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamConfigTypeDef"]
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

    Id = field("Id")
    Arn = field("Arn")
    IdentityManagementType = field("IdentityManagementType")
    InstanceAlias = field("InstanceAlias")
    CreatedTime = field("CreatedTime")
    ServiceRole = field("ServiceRole")
    InstanceStatus = field("InstanceStatus")
    InboundCallsEnabled = field("InboundCallsEnabled")
    OutboundCallsEnabled = field("OutboundCallsEnabled")
    InstanceAccessUrl = field("InstanceAccessUrl")

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
class IntegrationAssociationSummary:
    boto3_raw_data: "type_defs.IntegrationAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    IntegrationAssociationId = field("IntegrationAssociationId")
    IntegrationAssociationArn = field("IntegrationAssociationArn")
    InstanceId = field("InstanceId")
    IntegrationType = field("IntegrationType")
    IntegrationArn = field("IntegrationArn")
    SourceApplicationUrl = field("SourceApplicationUrl")
    SourceApplicationName = field("SourceApplicationName")
    SourceType = field("SourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntegrationAssociationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateFieldIdentifier:
    boto3_raw_data: "type_defs.TaskTemplateFieldIdentifierTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateFieldIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateFieldIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentStatusRequest:
    boto3_raw_data: "type_defs.ListAgentStatusRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    AgentStatusTypes = field("AgentStatusTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyticsDataAssociationsRequest:
    boto3_raw_data: "type_defs.ListAnalyticsDataAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    DataSetId = field("DataSetId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalyticsDataAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyticsDataAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyticsDataLakeDataSetsRequest:
    boto3_raw_data: "type_defs.ListAnalyticsDataLakeDataSetsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalyticsDataLakeDataSetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyticsDataLakeDataSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovedOriginsRequest:
    boto3_raw_data: "type_defs.ListApprovedOriginsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApprovedOriginsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovedOriginsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedContactsRequest:
    boto3_raw_data: "type_defs.ListAssociatedContactsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssociatedContactsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedContactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuthenticationProfilesRequest:
    boto3_raw_data: "type_defs.ListAuthenticationProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuthenticationProfilesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuthenticationProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsRequest:
    boto3_raw_data: "type_defs.ListBotsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    LexVersion = field("LexVersion")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBotsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListBotsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactEvaluationsRequest:
    boto3_raw_data: "type_defs.ListContactEvaluationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactEvaluationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactEvaluationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowModulesRequest:
    boto3_raw_data: "type_defs.ListContactFlowModulesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ContactFlowModuleState = field("ContactFlowModuleState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactFlowModulesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowModulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowVersionsRequest:
    boto3_raw_data: "type_defs.ListContactFlowVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactFlowVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowsRequest:
    boto3_raw_data: "type_defs.ListContactFlowsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactFlowTypes = field("ContactFlowTypes")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactFlowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactReferencesRequest:
    boto3_raw_data: "type_defs.ListContactReferencesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    ReferenceTypes = field("ReferenceTypes")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactReferencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactReferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDefaultVocabulariesRequest:
    boto3_raw_data: "type_defs.ListDefaultVocabulariesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    LanguageCode = field("LanguageCode")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDefaultVocabulariesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDefaultVocabulariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationFormVersionsRequest:
    boto3_raw_data: "type_defs.ListEvaluationFormVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEvaluationFormVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationFormVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationFormsRequest:
    boto3_raw_data: "type_defs.ListEvaluationFormsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEvaluationFormsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationFormsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowAssociationsRequest:
    boto3_raw_data: "type_defs.ListFlowAssociationsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ResourceType = field("ResourceType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowAssociationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHoursOfOperationOverridesRequest:
    boto3_raw_data: "type_defs.ListHoursOfOperationOverridesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHoursOfOperationOverridesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHoursOfOperationOverridesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHoursOfOperationsRequest:
    boto3_raw_data: "type_defs.ListHoursOfOperationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHoursOfOperationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHoursOfOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceAttributesRequest:
    boto3_raw_data: "type_defs.ListInstanceAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceStorageConfigsRequest:
    boto3_raw_data: "type_defs.ListInstanceStorageConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ResourceType = field("ResourceType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceStorageConfigsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceStorageConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequest:
    boto3_raw_data: "type_defs.ListInstancesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationAssociationsRequest:
    boto3_raw_data: "type_defs.ListIntegrationAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    IntegrationType = field("IntegrationType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    IntegrationArn = field("IntegrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIntegrationAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLambdaFunctionsRequest:
    boto3_raw_data: "type_defs.ListLambdaFunctionsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLambdaFunctionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLambdaFunctionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLexBotsRequest:
    boto3_raw_data: "type_defs.ListLexBotsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLexBotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLexBotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersRequest:
    boto3_raw_data: "type_defs.ListPhoneNumbersRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PhoneNumberTypes = field("PhoneNumberTypes")
    PhoneNumberCountryCodes = field("PhoneNumberCountryCodes")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberSummary:
    boto3_raw_data: "type_defs.PhoneNumberSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    PhoneNumber = field("PhoneNumber")
    PhoneNumberType = field("PhoneNumberType")
    PhoneNumberCountryCode = field("PhoneNumberCountryCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersSummary:
    boto3_raw_data: "type_defs.ListPhoneNumbersSummaryTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    PhoneNumberArn = field("PhoneNumberArn")
    PhoneNumber = field("PhoneNumber")
    PhoneNumberCountryCode = field("PhoneNumberCountryCode")
    PhoneNumberType = field("PhoneNumberType")
    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    PhoneNumberDescription = field("PhoneNumberDescription")
    SourcePhoneNumberArn = field("SourcePhoneNumberArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersV2Request:
    boto3_raw_data: "type_defs.ListPhoneNumbersV2RequestTypeDef" = dataclasses.field()

    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    PhoneNumberCountryCodes = field("PhoneNumberCountryCodes")
    PhoneNumberTypes = field("PhoneNumberTypes")
    PhoneNumberPrefix = field("PhoneNumberPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredefinedAttributesRequest:
    boto3_raw_data: "type_defs.ListPredefinedAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPredefinedAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredefinedAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttributeSummary:
    boto3_raw_data: "type_defs.PredefinedAttributeSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredefinedAttributeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptsRequest:
    boto3_raw_data: "type_defs.ListPromptsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSummary:
    boto3_raw_data: "type_defs.PromptSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueQuickConnectsRequest:
    boto3_raw_data: "type_defs.ListQueueQuickConnectsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueueQuickConnectsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueQuickConnectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickConnectSummary:
    boto3_raw_data: "type_defs.QuickConnectSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    QuickConnectType = field("QuickConnectType")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickConnectSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickConnectSummaryTypeDef"]
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

    InstanceId = field("InstanceId")
    QueueTypes = field("QueueTypes")
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
class QueueSummary:
    boto3_raw_data: "type_defs.QueueSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    QueueType = field("QueueType")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

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
class ListQuickConnectsRequest:
    boto3_raw_data: "type_defs.ListQuickConnectsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    QuickConnectTypes = field("QuickConnectTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQuickConnectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuickConnectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRealtimeContactAnalysisSegmentsV2Request:
    boto3_raw_data: "type_defs.ListRealtimeContactAnalysisSegmentsV2RequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    OutputType = field("OutputType")
    SegmentTypes = field("SegmentTypes")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRealtimeContactAnalysisSegmentsV2RequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRealtimeContactAnalysisSegmentsV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingProfileQueuesRequest:
    boto3_raw_data: "type_defs.ListRoutingProfileQueuesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRoutingProfileQueuesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingProfileQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileQueueConfigSummary:
    boto3_raw_data: "type_defs.RoutingProfileQueueConfigSummaryTypeDef" = (
        dataclasses.field()
    )

    QueueId = field("QueueId")
    QueueArn = field("QueueArn")
    QueueName = field("QueueName")
    Priority = field("Priority")
    Delay = field("Delay")
    Channel = field("Channel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RoutingProfileQueueConfigSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileQueueConfigSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingProfilesRequest:
    boto3_raw_data: "type_defs.ListRoutingProfilesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutingProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileSummary:
    boto3_raw_data: "type_defs.RoutingProfileSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequest:
    boto3_raw_data: "type_defs.ListRulesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PublishStatus = field("PublishStatus")
    EventSourceName = field("EventSourceName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityKeysRequest:
    boto3_raw_data: "type_defs.ListSecurityKeysRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityKey:
    boto3_raw_data: "type_defs.SecurityKeyTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    Key = field("Key")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecurityKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecurityKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfileApplicationsRequest:
    boto3_raw_data: "type_defs.ListSecurityProfileApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileId = field("SecurityProfileId")
    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfileApplicationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfileApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilePermissionsRequest:
    boto3_raw_data: "type_defs.ListSecurityProfilePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileId = field("SecurityProfileId")
    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilePermissionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesRequest:
    boto3_raw_data: "type_defs.ListSecurityProfilesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileSummary:
    boto3_raw_data: "type_defs.SecurityProfileSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileSummaryTypeDef"]
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
class ListTaskTemplatesRequest:
    boto3_raw_data: "type_defs.ListTaskTemplatesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaskTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateMetadata:
    boto3_raw_data: "type_defs.TaskTemplateMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")
    LastModifiedTime = field("LastModifiedTime")
    CreatedTime = field("CreatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficDistributionGroupUsersRequest:
    boto3_raw_data: "type_defs.ListTrafficDistributionGroupUsersRequestTypeDef" = (
        dataclasses.field()
    )

    TrafficDistributionGroupId = field("TrafficDistributionGroupId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficDistributionGroupUsersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficDistributionGroupUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficDistributionGroupUserSummary:
    boto3_raw_data: "type_defs.TrafficDistributionGroupUserSummaryTypeDef" = (
        dataclasses.field()
    )

    UserId = field("UserId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrafficDistributionGroupUserSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficDistributionGroupUserSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficDistributionGroupsRequest:
    boto3_raw_data: "type_defs.ListTrafficDistributionGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficDistributionGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficDistributionGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficDistributionGroupSummary:
    boto3_raw_data: "type_defs.TrafficDistributionGroupSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    InstanceArn = field("InstanceArn")
    Status = field("Status")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrafficDistributionGroupSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficDistributionGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUseCasesRequest:
    boto3_raw_data: "type_defs.ListUseCasesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    IntegrationAssociationId = field("IntegrationAssociationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUseCasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUseCasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UseCase:
    boto3_raw_data: "type_defs.UseCaseTypeDef" = dataclasses.field()

    UseCaseId = field("UseCaseId")
    UseCaseArn = field("UseCaseArn")
    UseCaseType = field("UseCaseType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UseCaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UseCaseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserHierarchyGroupsRequest:
    boto3_raw_data: "type_defs.ListUserHierarchyGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUserHierarchyGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserHierarchyGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserProficienciesRequest:
    boto3_raw_data: "type_defs.ListUserProficienciesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    UserId = field("UserId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserProficienciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserProficienciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSummary:
    boto3_raw_data: "type_defs.UserSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Username = field("Username")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViewVersionsRequest:
    boto3_raw_data: "type_defs.ListViewVersionsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListViewVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViewVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewVersionSummary:
    boto3_raw_data: "type_defs.ViewVersionSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Description = field("Description")
    Name = field("Name")
    Type = field("Type")
    Version = field("Version")
    VersionDescription = field("VersionDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViewVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViewsRequest:
    boto3_raw_data: "type_defs.ListViewsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Type = field("Type")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListViewsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViewsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewSummary:
    boto3_raw_data: "type_defs.ViewSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Type = field("Type")
    Status = field("Status")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPlacement:
    boto3_raw_data: "type_defs.MediaPlacementTypeDef" = dataclasses.field()

    AudioHostUrl = field("AudioHostUrl")
    AudioFallbackUrl = field("AudioFallbackUrl")
    SignalingUrl = field("SignalingUrl")
    TurnControlUrl = field("TurnControlUrl")
    EventIngestionUrl = field("EventIngestionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaPlacementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaPlacementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricFilterV2Output:
    boto3_raw_data: "type_defs.MetricFilterV2OutputTypeDef" = dataclasses.field()

    MetricFilterKey = field("MetricFilterKey")
    MetricFilterValues = field("MetricFilterValues")
    Negate = field("Negate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricFilterV2OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricFilterV2OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricFilterV2:
    boto3_raw_data: "type_defs.MetricFilterV2TypeDef" = dataclasses.field()

    MetricFilterKey = field("MetricFilterKey")
    MetricFilterValues = field("MetricFilterValues")
    Negate = field("Negate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricFilterV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricFilterV2TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricInterval:
    boto3_raw_data: "type_defs.MetricIntervalTypeDef" = dataclasses.field()

    Interval = field("Interval")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricIntervalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThresholdV2:
    boto3_raw_data: "type_defs.ThresholdV2TypeDef" = dataclasses.field()

    Comparison = field("Comparison")
    ThresholdValue = field("ThresholdValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThresholdV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThresholdV2TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorContactRequest:
    boto3_raw_data: "type_defs.MonitorContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    UserId = field("UserId")
    AllowedMonitorCapabilities = field("AllowedMonitorCapabilities")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitorContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantDetails:
    boto3_raw_data: "type_defs.ParticipantDetailsTypeDef" = dataclasses.field()

    DisplayName = field("DisplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationRecipientTypeOutput:
    boto3_raw_data: "type_defs.NotificationRecipientTypeOutputTypeDef" = (
        dataclasses.field()
    )

    UserTags = field("UserTags")
    UserIds = field("UserIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NotificationRecipientTypeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationRecipientTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationRecipientType:
    boto3_raw_data: "type_defs.NotificationRecipientTypeTypeDef" = dataclasses.field()

    UserTags = field("UserTags")
    UserIds = field("UserIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationRecipientTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationRecipientTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberReference:
    boto3_raw_data: "type_defs.NumberReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NumberReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NumberReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundRawMessage:
    boto3_raw_data: "type_defs.OutboundRawMessageTypeDef" = dataclasses.field()

    Subject = field("Subject")
    Body = field("Body")
    ContentType = field("ContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundRawMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundRawMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantTimerValue:
    boto3_raw_data: "type_defs.ParticipantTimerValueTypeDef" = dataclasses.field()

    ParticipantTimerAction = field("ParticipantTimerAction")
    ParticipantTimerDurationInMinutes = field("ParticipantTimerDurationInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantTimerValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantTimerValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseContactRequest:
    boto3_raw_data: "type_defs.PauseContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersistentChat:
    boto3_raw_data: "type_defs.PersistentChatTypeDef" = dataclasses.field()

    RehydrationType = field("RehydrationType")
    SourceContactId = field("SourceContactId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PersistentChatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PersistentChatTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberQuickConnectConfig:
    boto3_raw_data: "type_defs.PhoneNumberQuickConnectConfigTypeDef" = (
        dataclasses.field()
    )

    PhoneNumber = field("PhoneNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PhoneNumberQuickConnectConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberQuickConnectConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttributeConfiguration:
    boto3_raw_data: "type_defs.PredefinedAttributeConfigurationTypeDef" = (
        dataclasses.field()
    )

    EnableValueValidationOnAssociation = field("EnableValueValidationOnAssociation")
    IsReadOnly = field("IsReadOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredefinedAttributeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttributeValuesOutput:
    boto3_raw_data: "type_defs.PredefinedAttributeValuesOutputTypeDef" = (
        dataclasses.field()
    )

    StringList = field("StringList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PredefinedAttributeValuesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttributeValues:
    boto3_raw_data: "type_defs.PredefinedAttributeValuesTypeDef" = dataclasses.field()

    StringList = field("StringList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredefinedAttributeValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutUserStatusRequest:
    boto3_raw_data: "type_defs.PutUserStatusRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    InstanceId = field("InstanceId")
    AgentStatusId = field("AgentStatusId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutUserStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutUserStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueInfoInput:
    boto3_raw_data: "type_defs.QueueInfoInputTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueInfoInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueInfoInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueQuickConnectConfig:
    boto3_raw_data: "type_defs.QueueQuickConnectConfigTypeDef" = dataclasses.field()

    QueueId = field("QueueId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueQuickConnectConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueQuickConnectConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserQuickConnectConfig:
    boto3_raw_data: "type_defs.UserQuickConnectConfigTypeDef" = dataclasses.field()

    UserId = field("UserId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserQuickConnectConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserQuickConnectConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisAttachment:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisAttachmentTypeDef" = (
        dataclasses.field()
    )

    AttachmentName = field("AttachmentName")
    AttachmentId = field("AttachmentId")
    ContentType = field("ContentType")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisAttachmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisCharacterInterval:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisCharacterIntervalTypeDef" = (
        dataclasses.field()
    )

    BeginOffsetChar = field("BeginOffsetChar")
    EndOffsetChar = field("EndOffsetChar")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisCharacterIntervalTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisCharacterIntervalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisTimeData:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisTimeDataTypeDef" = (
        dataclasses.field()
    )

    AbsoluteTime = field("AbsoluteTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RealTimeContactAnalysisTimeDataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisTimeDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisSegmentPostContactSummary:
    boto3_raw_data: (
        "type_defs.RealTimeContactAnalysisSegmentPostContactSummaryTypeDef"
    ) = dataclasses.field()

    Status = field("Status")
    Content = field("Content")
    FailureCode = field("FailureCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisSegmentPostContactSummaryTypeDef"
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
                "type_defs.RealTimeContactAnalysisSegmentPostContactSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringReference:
    boto3_raw_data: "type_defs.StringReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StringReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StringReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlReference:
    boto3_raw_data: "type_defs.UrlReferenceTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UrlReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleasePhoneNumberRequest:
    boto3_raw_data: "type_defs.ReleasePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleasePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleasePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicateInstanceRequest:
    boto3_raw_data: "type_defs.ReplicateInstanceRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ReplicaRegion = field("ReplicaRegion")
    ReplicaAlias = field("ReplicaAlias")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationStatusSummary:
    boto3_raw_data: "type_defs.ReplicationStatusSummaryTypeDef" = dataclasses.field()

    Region = field("Region")
    ReplicationStatus = field("ReplicationStatus")
    ReplicationStatusReason = field("ReplicationStatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationStatusSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationStatusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagSearchCondition:
    boto3_raw_data: "type_defs.TagSearchConditionTypeDef" = dataclasses.field()

    tagKey = field("tagKey")
    tagValue = field("tagValue")
    tagKeyComparisonType = field("tagKeyComparisonType")
    tagValueComparisonType = field("tagValueComparisonType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagSearchConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagSearchConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeContactRecordingRequest:
    boto3_raw_data: "type_defs.ResumeContactRecordingRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    InitialContactId = field("InitialContactId")
    ContactRecordingType = field("ContactRecordingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResumeContactRecordingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeContactRecordingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeContactRequest:
    boto3_raw_data: "type_defs.ResumeContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingCriteriaInputStepExpiry:
    boto3_raw_data: "type_defs.RoutingCriteriaInputStepExpiryTypeDef" = (
        dataclasses.field()
    )

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RoutingCriteriaInputStepExpiryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingCriteriaInputStepExpiryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitAutoEvaluationActionDefinition:
    boto3_raw_data: "type_defs.SubmitAutoEvaluationActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    EvaluationFormId = field("EvaluationFormId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubmitAutoEvaluationActionDefinitionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitAutoEvaluationActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersRequest:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersRequestTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberCountryCode = field("PhoneNumberCountryCode")
    PhoneNumberType = field("PhoneNumberType")
    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    PhoneNumberPrefix = field("PhoneNumberPrefix")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sort:
    boto3_raw_data: "type_defs.SortTypeDef" = dataclasses.field()

    FieldName = field("FieldName")
    Order = field("Order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagSet:
    boto3_raw_data: "type_defs.TagSetTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileSearchSummary:
    boto3_raw_data: "type_defs.SecurityProfileSearchSummaryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    OrganizationResourceId = field("OrganizationResourceId")
    Arn = field("Arn")
    SecurityProfileName = field("SecurityProfileName")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityProfileSearchSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVocabulariesRequest:
    boto3_raw_data: "type_defs.SearchVocabulariesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    State = field("State")
    NameStartsWith = field("NameStartsWith")
    LanguageCode = field("LanguageCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchVocabulariesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVocabulariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VocabularySummary:
    boto3_raw_data: "type_defs.VocabularySummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Arn = field("Arn")
    LanguageCode = field("LanguageCode")
    State = field("State")
    LastModifiedTime = field("LastModifiedTime")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VocabularySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VocabularySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchableContactAttributesCriteria:
    boto3_raw_data: "type_defs.SearchableContactAttributesCriteriaTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchableContactAttributesCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchableContactAttributesCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchableSegmentAttributesCriteria:
    boto3_raw_data: "type_defs.SearchableSegmentAttributesCriteriaTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchableSegmentAttributesCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchableSegmentAttributesCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentAttributeValue:
    boto3_raw_data: "type_defs.SegmentAttributeValueTypeDef" = dataclasses.field()

    ValueString = field("ValueString")
    ValueMap = field("ValueMap")
    ValueInteger = field("ValueInteger")
    ValueList = field("ValueList")
    ValueArn = field("ValueArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCampaign:
    boto3_raw_data: "type_defs.SourceCampaignTypeDef" = dataclasses.field()

    CampaignId = field("CampaignId")
    OutboundRequestId = field("OutboundRequestId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceCampaignTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceCampaignTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignInDistribution:
    boto3_raw_data: "type_defs.SignInDistributionTypeDef" = dataclasses.field()

    Region = field("Region")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignInDistributionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignInDistributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadUrlMetadata:
    boto3_raw_data: "type_defs.UploadUrlMetadataTypeDef" = dataclasses.field()

    Url = field("Url")
    UrlExpiry = field("UrlExpiry")
    HeadersToInclude = field("HeadersToInclude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadUrlMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadUrlMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContactEvaluationRequest:
    boto3_raw_data: "type_defs.StartContactEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    EvaluationFormId = field("EvaluationFormId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartContactEvaluationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContactEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceRecordingConfiguration:
    boto3_raw_data: "type_defs.VoiceRecordingConfigurationTypeDef" = dataclasses.field()

    VoiceRecordingTrack = field("VoiceRecordingTrack")
    IvrRecordingTrack = field("IvrRecordingTrack")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceRecordingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceRecordingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartScreenSharingRequest:
    boto3_raw_data: "type_defs.StartScreenSharingRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartScreenSharingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartScreenSharingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopContactRecordingRequest:
    boto3_raw_data: "type_defs.StopContactRecordingRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    InitialContactId = field("InitialContactId")
    ContactRecordingType = field("ContactRecordingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopContactRecordingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopContactRecordingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopContactStreamingRequest:
    boto3_raw_data: "type_defs.StopContactStreamingRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    StreamingId = field("StreamingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopContactStreamingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopContactStreamingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuspendContactRecordingRequest:
    boto3_raw_data: "type_defs.SuspendContactRecordingRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    InitialContactId = field("InitialContactId")
    ContactRecordingType = field("ContactRecordingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SuspendContactRecordingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuspendContactRecordingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagContactRequest:
    boto3_raw_data: "type_defs.TagContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    InstanceId = field("InstanceId")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagContactRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagContactRequestTypeDef"]
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
class TemplateAttributes:
    boto3_raw_data: "type_defs.TemplateAttributesTypeDef" = dataclasses.field()

    CustomAttributes = field("CustomAttributes")
    CustomerProfileAttributes = field("CustomerProfileAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptCriteria:
    boto3_raw_data: "type_defs.TranscriptCriteriaTypeDef" = dataclasses.field()

    ParticipantRole = field("ParticipantRole")
    SearchText = field("SearchText")
    MatchType = field("MatchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranscriptCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferContactRequest:
    boto3_raw_data: "type_defs.TransferContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    ContactFlowId = field("ContactFlowId")
    QueueId = field("QueueId")
    UserId = field("UserId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagContactRequest:
    boto3_raw_data: "type_defs.UntagContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    InstanceId = field("InstanceId")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagContactRequestTypeDef"]
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
class UpdateAgentStatusRequest:
    boto3_raw_data: "type_defs.UpdateAgentStatusRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    AgentStatusId = field("AgentStatusId")
    Name = field("Name")
    Description = field("Description")
    State = field("State")
    DisplayOrder = field("DisplayOrder")
    ResetOrderNumber = field("ResetOrderNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuthenticationProfileRequest:
    boto3_raw_data: "type_defs.UpdateAuthenticationProfileRequestTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileId = field("AuthenticationProfileId")
    InstanceId = field("InstanceId")
    Name = field("Name")
    Description = field("Description")
    AllowedIps = field("AllowedIps")
    BlockedIps = field("BlockedIps")
    PeriodicSessionDuration = field("PeriodicSessionDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAuthenticationProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthenticationProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactAttributesRequest:
    boto3_raw_data: "type_defs.UpdateContactAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    InitialContactId = field("InitialContactId")
    InstanceId = field("InstanceId")
    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContactAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactFlowContentRequest:
    boto3_raw_data: "type_defs.UpdateContactFlowContentRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")
    Content = field("Content")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContactFlowContentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactFlowContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactFlowMetadataRequest:
    boto3_raw_data: "type_defs.UpdateContactFlowMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")
    Name = field("Name")
    Description = field("Description")
    ContactFlowState = field("ContactFlowState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContactFlowMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactFlowMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactFlowModuleContentRequest:
    boto3_raw_data: "type_defs.UpdateContactFlowModuleContentRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowModuleId = field("ContactFlowModuleId")
    Content = field("Content")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContactFlowModuleContentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactFlowModuleContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactFlowModuleMetadataRequest:
    boto3_raw_data: "type_defs.UpdateContactFlowModuleMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowModuleId = field("ContactFlowModuleId")
    Name = field("Name")
    Description = field("Description")
    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContactFlowModuleMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactFlowModuleMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactFlowNameRequest:
    boto3_raw_data: "type_defs.UpdateContactFlowNameRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactFlowNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactFlowNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailAddressMetadataRequest:
    boto3_raw_data: "type_defs.UpdateEmailAddressMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EmailAddressId = field("EmailAddressId")
    Description = field("Description")
    DisplayName = field("DisplayName")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEmailAddressMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailAddressMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceAttributeRequest:
    boto3_raw_data: "type_defs.UpdateInstanceAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AttributeType = field("AttributeType")
    Value = field("Value")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateInstanceAttributeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParticipantAuthenticationRequest:
    boto3_raw_data: "type_defs.UpdateParticipantAuthenticationRequestTypeDef" = (
        dataclasses.field()
    )

    State = field("State")
    InstanceId = field("InstanceId")
    Code = field("Code")
    Error = field("Error")
    ErrorDescription = field("ErrorDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateParticipantAuthenticationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParticipantAuthenticationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberMetadataRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberId = field("PhoneNumberId")
    PhoneNumberDescription = field("PhoneNumberDescription")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePromptRequest:
    boto3_raw_data: "type_defs.UpdatePromptRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PromptId = field("PromptId")
    Name = field("Name")
    Description = field("Description")
    S3Uri = field("S3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueHoursOfOperationRequest:
    boto3_raw_data: "type_defs.UpdateQueueHoursOfOperationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    HoursOfOperationId = field("HoursOfOperationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQueueHoursOfOperationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueHoursOfOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueMaxContactsRequest:
    boto3_raw_data: "type_defs.UpdateQueueMaxContactsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    MaxContacts = field("MaxContacts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQueueMaxContactsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueMaxContactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueNameRequest:
    boto3_raw_data: "type_defs.UpdateQueueNameRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueStatusRequest:
    boto3_raw_data: "type_defs.UpdateQueueStatusRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateQueueStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQuickConnectNameRequest:
    boto3_raw_data: "type_defs.UpdateQuickConnectNameRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QuickConnectId = field("QuickConnectId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQuickConnectNameRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQuickConnectNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoutingProfileAgentAvailabilityTimerRequest:
    boto3_raw_data: (
        "type_defs.UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef"
    ) = dataclasses.field()

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")
    AgentAvailabilityTimer = field("AgentAvailabilityTimer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef"
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
                "type_defs.UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoutingProfileDefaultOutboundQueueRequest:
    boto3_raw_data: (
        "type_defs.UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef"
    ) = dataclasses.field()

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")
    DefaultOutboundQueueId = field("DefaultOutboundQueueId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef"
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
                "type_defs.UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoutingProfileNameRequest:
    boto3_raw_data: "type_defs.UpdateRoutingProfileNameRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRoutingProfileNameRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoutingProfileNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserHierarchyGroupNameRequest:
    boto3_raw_data: "type_defs.UpdateUserHierarchyGroupNameRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    HierarchyGroupId = field("HierarchyGroupId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateUserHierarchyGroupNameRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserHierarchyGroupNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserHierarchyRequest:
    boto3_raw_data: "type_defs.UpdateUserHierarchyRequestTypeDef" = dataclasses.field()

    UserId = field("UserId")
    InstanceId = field("InstanceId")
    HierarchyGroupId = field("HierarchyGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserHierarchyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserHierarchyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRoutingProfileRequest:
    boto3_raw_data: "type_defs.UpdateUserRoutingProfileRequestTypeDef" = (
        dataclasses.field()
    )

    RoutingProfileId = field("RoutingProfileId")
    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateUserRoutingProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRoutingProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserSecurityProfilesRequest:
    boto3_raw_data: "type_defs.UpdateUserSecurityProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileIds = field("SecurityProfileIds")
    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateUserSecurityProfilesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserSecurityProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateViewMetadataRequest:
    boto3_raw_data: "type_defs.UpdateViewMetadataRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateViewMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateViewMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserReference:
    boto3_raw_data: "type_defs.UserReferenceTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserIdentityInfoLite:
    boto3_raw_data: "type_defs.UserIdentityInfoLiteTypeDef" = dataclasses.field()

    FirstName = field("FirstName")
    LastName = field("LastName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserIdentityInfoLiteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserIdentityInfoLiteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewContent:
    boto3_raw_data: "type_defs.ViewContentTypeDef" = dataclasses.field()

    InputSchema = field("InputSchema")
    Template = field("Template")
    Actions = field("Actions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleSummary:
    boto3_raw_data: "type_defs.RuleSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    RuleId = field("RuleId")
    RuleArn = field("RuleArn")
    EventSourceName = field("EventSourceName")
    PublishStatus = field("PublishStatus")

    @cached_property
    def ActionSummaries(self):  # pragma: no cover
        return ActionSummary.make_many(self.boto3_raw_data["ActionSummaries"])

    CreatedTime = field("CreatedTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateEvaluationFormResponse:
    boto3_raw_data: "type_defs.ActivateEvaluationFormResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormArn = field("EvaluationFormArn")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateEvaluationFormResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateEvaluationFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAnalyticsDataSetResponse:
    boto3_raw_data: "type_defs.AssociateAnalyticsDataSetResponseTypeDef" = (
        dataclasses.field()
    )

    DataSetId = field("DataSetId")
    TargetAccountId = field("TargetAccountId")
    ResourceShareId = field("ResourceShareId")
    ResourceShareArn = field("ResourceShareArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAnalyticsDataSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAnalyticsDataSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateInstanceStorageConfigResponse:
    boto3_raw_data: "type_defs.AssociateInstanceStorageConfigResponseTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateInstanceStorageConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateInstanceStorageConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSecurityKeyResponse:
    boto3_raw_data: "type_defs.AssociateSecurityKeyResponseTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateSecurityKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSecurityKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimPhoneNumberResponse:
    boto3_raw_data: "type_defs.ClaimPhoneNumberResponseTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    PhoneNumberArn = field("PhoneNumberArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClaimPhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimPhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentStatusResponse:
    boto3_raw_data: "type_defs.CreateAgentStatusResponseTypeDef" = dataclasses.field()

    AgentStatusARN = field("AgentStatusARN")
    AgentStatusId = field("AgentStatusId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactFlowModuleResponse:
    boto3_raw_data: "type_defs.CreateContactFlowModuleResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContactFlowModuleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactFlowModuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactFlowResponse:
    boto3_raw_data: "type_defs.CreateContactFlowResponseTypeDef" = dataclasses.field()

    ContactFlowId = field("ContactFlowId")
    ContactFlowArn = field("ContactFlowArn")
    FlowContentSha256 = field("FlowContentSha256")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactFlowVersionResponse:
    boto3_raw_data: "type_defs.CreateContactFlowVersionResponseTypeDef" = (
        dataclasses.field()
    )

    ContactFlowArn = field("ContactFlowArn")
    Version = field("Version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContactFlowVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactFlowVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactResponse:
    boto3_raw_data: "type_defs.CreateContactResponseTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    ContactArn = field("ContactArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEmailAddressResponse:
    boto3_raw_data: "type_defs.CreateEmailAddressResponseTypeDef" = dataclasses.field()

    EmailAddressId = field("EmailAddressId")
    EmailAddressArn = field("EmailAddressArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEmailAddressResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEmailAddressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEvaluationFormResponse:
    boto3_raw_data: "type_defs.CreateEvaluationFormResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormArn = field("EvaluationFormArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEvaluationFormResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEvaluationFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHoursOfOperationOverrideResponse:
    boto3_raw_data: "type_defs.CreateHoursOfOperationOverrideResponseTypeDef" = (
        dataclasses.field()
    )

    HoursOfOperationOverrideId = field("HoursOfOperationOverrideId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateHoursOfOperationOverrideResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHoursOfOperationOverrideResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHoursOfOperationResponse:
    boto3_raw_data: "type_defs.CreateHoursOfOperationResponseTypeDef" = (
        dataclasses.field()
    )

    HoursOfOperationId = field("HoursOfOperationId")
    HoursOfOperationArn = field("HoursOfOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateHoursOfOperationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHoursOfOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceResponse:
    boto3_raw_data: "type_defs.CreateInstanceResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationAssociationResponse:
    boto3_raw_data: "type_defs.CreateIntegrationAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    IntegrationAssociationId = field("IntegrationAssociationId")
    IntegrationAssociationArn = field("IntegrationAssociationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIntegrationAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePersistentContactAssociationResponse:
    boto3_raw_data: "type_defs.CreatePersistentContactAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    ContinuedFromContactId = field("ContinuedFromContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePersistentContactAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePersistentContactAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptResponse:
    boto3_raw_data: "type_defs.CreatePromptResponseTypeDef" = dataclasses.field()

    PromptARN = field("PromptARN")
    PromptId = field("PromptId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePushNotificationRegistrationResponse:
    boto3_raw_data: "type_defs.CreatePushNotificationRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePushNotificationRegistrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePushNotificationRegistrationResponseTypeDef"]
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

    QueueArn = field("QueueArn")
    QueueId = field("QueueId")

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
class CreateQuickConnectResponse:
    boto3_raw_data: "type_defs.CreateQuickConnectResponseTypeDef" = dataclasses.field()

    QuickConnectARN = field("QuickConnectARN")
    QuickConnectId = field("QuickConnectId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQuickConnectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuickConnectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoutingProfileResponse:
    boto3_raw_data: "type_defs.CreateRoutingProfileResponseTypeDef" = (
        dataclasses.field()
    )

    RoutingProfileArn = field("RoutingProfileArn")
    RoutingProfileId = field("RoutingProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoutingProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoutingProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleResponse:
    boto3_raw_data: "type_defs.CreateRuleResponseTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")
    RuleId = field("RuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityProfileResponse:
    boto3_raw_data: "type_defs.CreateSecurityProfileResponseTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileId = field("SecurityProfileId")
    SecurityProfileArn = field("SecurityProfileArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSecurityProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTaskTemplateResponse:
    boto3_raw_data: "type_defs.CreateTaskTemplateResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTaskTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTaskTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficDistributionGroupResponse:
    boto3_raw_data: "type_defs.CreateTrafficDistributionGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTrafficDistributionGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficDistributionGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUseCaseResponse:
    boto3_raw_data: "type_defs.CreateUseCaseResponseTypeDef" = dataclasses.field()

    UseCaseId = field("UseCaseId")
    UseCaseArn = field("UseCaseArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUseCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUseCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserHierarchyGroupResponse:
    boto3_raw_data: "type_defs.CreateUserHierarchyGroupResponseTypeDef" = (
        dataclasses.field()
    )

    HierarchyGroupId = field("HierarchyGroupId")
    HierarchyGroupArn = field("HierarchyGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateUserHierarchyGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserHierarchyGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResponse:
    boto3_raw_data: "type_defs.CreateUserResponseTypeDef" = dataclasses.field()

    UserId = field("UserId")
    UserArn = field("UserArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVocabularyResponse:
    boto3_raw_data: "type_defs.CreateVocabularyResponseTypeDef" = dataclasses.field()

    VocabularyArn = field("VocabularyArn")
    VocabularyId = field("VocabularyId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateEvaluationFormResponse:
    boto3_raw_data: "type_defs.DeactivateEvaluationFormResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormArn = field("EvaluationFormArn")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateEvaluationFormResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateEvaluationFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVocabularyResponse:
    boto3_raw_data: "type_defs.DeleteVocabularyResponseTypeDef" = dataclasses.field()

    VocabularyArn = field("VocabularyArn")
    VocabularyId = field("VocabularyId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEmailAddressResponse:
    boto3_raw_data: "type_defs.DescribeEmailAddressResponseTypeDef" = (
        dataclasses.field()
    )

    EmailAddressId = field("EmailAddressId")
    EmailAddressArn = field("EmailAddressArn")
    EmailAddress = field("EmailAddress")
    DisplayName = field("DisplayName")
    Description = field("Description")
    CreateTimestamp = field("CreateTimestamp")
    ModifiedTimestamp = field("ModifiedTimestamp")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEmailAddressResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEmailAddressResponseTypeDef"]
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
class GetContactAttributesResponse:
    boto3_raw_data: "type_defs.GetContactAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    Attributes = field("Attributes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowAssociationResponse:
    boto3_raw_data: "type_defs.GetFlowAssociationResponseTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    FlowId = field("FlowId")
    ResourceType = field("ResourceType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowAssociationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPromptFileResponse:
    boto3_raw_data: "type_defs.GetPromptFileResponseTypeDef" = dataclasses.field()

    PromptPresignedUrl = field("PromptPresignedUrl")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPromptFileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPromptFileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportPhoneNumberResponse:
    boto3_raw_data: "type_defs.ImportPhoneNumberResponseTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    PhoneNumberArn = field("PhoneNumberArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportPhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportPhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovedOriginsResponse:
    boto3_raw_data: "type_defs.ListApprovedOriginsResponseTypeDef" = dataclasses.field()

    Origins = field("Origins")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApprovedOriginsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovedOriginsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLambdaFunctionsResponse:
    boto3_raw_data: "type_defs.ListLambdaFunctionsResponseTypeDef" = dataclasses.field()

    LambdaFunctions = field("LambdaFunctions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLambdaFunctionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLambdaFunctionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilePermissionsResponse:
    boto3_raw_data: "type_defs.ListSecurityProfilePermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    Permissions = field("Permissions")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilePermissionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilePermissionsResponseTypeDef"]
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
class MonitorContactResponse:
    boto3_raw_data: "type_defs.MonitorContactResponseTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    ContactArn = field("ContactArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitorContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicateInstanceResponse:
    boto3_raw_data: "type_defs.ReplicateInstanceResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicateInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicateInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendChatIntegrationEventResponse:
    boto3_raw_data: "type_defs.SendChatIntegrationEventResponseTypeDef" = (
        dataclasses.field()
    )

    InitialContactId = field("InitialContactId")
    NewChatCreated = field("NewChatCreated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendChatIntegrationEventResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendChatIntegrationEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChatContactResponse:
    boto3_raw_data: "type_defs.StartChatContactResponseTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    ParticipantId = field("ParticipantId")
    ParticipantToken = field("ParticipantToken")
    ContinuedFromContactId = field("ContinuedFromContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChatContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChatContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContactEvaluationResponse:
    boto3_raw_data: "type_defs.StartContactEvaluationResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationId = field("EvaluationId")
    EvaluationArn = field("EvaluationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartContactEvaluationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContactEvaluationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContactStreamingResponse:
    boto3_raw_data: "type_defs.StartContactStreamingResponseTypeDef" = (
        dataclasses.field()
    )

    StreamingId = field("StreamingId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartContactStreamingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContactStreamingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEmailContactResponse:
    boto3_raw_data: "type_defs.StartEmailContactResponseTypeDef" = dataclasses.field()

    ContactId = field("ContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartEmailContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEmailContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOutboundChatContactResponse:
    boto3_raw_data: "type_defs.StartOutboundChatContactResponseTypeDef" = (
        dataclasses.field()
    )

    ContactId = field("ContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartOutboundChatContactResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOutboundChatContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOutboundEmailContactResponse:
    boto3_raw_data: "type_defs.StartOutboundEmailContactResponseTypeDef" = (
        dataclasses.field()
    )

    ContactId = field("ContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOutboundEmailContactResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOutboundEmailContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOutboundVoiceContactResponse:
    boto3_raw_data: "type_defs.StartOutboundVoiceContactResponseTypeDef" = (
        dataclasses.field()
    )

    ContactId = field("ContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartOutboundVoiceContactResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOutboundVoiceContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTaskContactResponse:
    boto3_raw_data: "type_defs.StartTaskContactResponseTypeDef" = dataclasses.field()

    ContactId = field("ContactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTaskContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTaskContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitContactEvaluationResponse:
    boto3_raw_data: "type_defs.SubmitContactEvaluationResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationId = field("EvaluationId")
    EvaluationArn = field("EvaluationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubmitContactEvaluationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitContactEvaluationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferContactResponse:
    boto3_raw_data: "type_defs.TransferContactResponseTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    ContactArn = field("ContactArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactEvaluationResponse:
    boto3_raw_data: "type_defs.UpdateContactEvaluationResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationId = field("EvaluationId")
    EvaluationArn = field("EvaluationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContactEvaluationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactEvaluationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEmailAddressMetadataResponse:
    boto3_raw_data: "type_defs.UpdateEmailAddressMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    EmailAddressId = field("EmailAddressId")
    EmailAddressArn = field("EmailAddressArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEmailAddressMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEmailAddressMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEvaluationFormResponse:
    boto3_raw_data: "type_defs.UpdateEvaluationFormResponseTypeDef" = (
        dataclasses.field()
    )

    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormArn = field("EvaluationFormArn")
    EvaluationFormVersion = field("EvaluationFormVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEvaluationFormResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEvaluationFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberResponse:
    boto3_raw_data: "type_defs.UpdatePhoneNumberResponseTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    PhoneNumberArn = field("PhoneNumberArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePromptResponse:
    boto3_raw_data: "type_defs.UpdatePromptResponseTypeDef" = dataclasses.field()

    PromptARN = field("PromptARN")
    PromptId = field("PromptId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalEmailRecipients:
    boto3_raw_data: "type_defs.AdditionalEmailRecipientsTypeDef" = dataclasses.field()

    @cached_property
    def ToList(self):  # pragma: no cover
        return EmailRecipient.make_many(self.boto3_raw_data["ToList"])

    @cached_property
    def CcList(self):  # pragma: no cover
        return EmailRecipient.make_many(self.boto3_raw_data["CcList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalEmailRecipientsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalEmailRecipientsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentConfigOutput:
    boto3_raw_data: "type_defs.AgentConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def Distributions(self):  # pragma: no cover
        return Distribution.make_many(self.boto3_raw_data["Distributions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentConfig:
    boto3_raw_data: "type_defs.AgentConfigTypeDef" = dataclasses.field()

    @cached_property
    def Distributions(self):  # pragma: no cover
        return Distribution.make_many(self.boto3_raw_data["Distributions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyConfigOutput:
    boto3_raw_data: "type_defs.TelephonyConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def Distributions(self):  # pragma: no cover
        return Distribution.make_many(self.boto3_raw_data["Distributions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TelephonyConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TelephonyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TelephonyConfig:
    boto3_raw_data: "type_defs.TelephonyConfigTypeDef" = dataclasses.field()

    @cached_property
    def Distributions(self):  # pragma: no cover
        return Distribution.make_many(self.boto3_raw_data["Distributions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TelephonyConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TelephonyConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentContactReference:
    boto3_raw_data: "type_defs.AgentContactReferenceTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    Channel = field("Channel")
    InitiationMethod = field("InitiationMethod")
    AgentContactState = field("AgentContactState")
    StateStartTimestamp = field("StateStartTimestamp")
    ConnectedToAgentTimestamp = field("ConnectedToAgentTimestamp")

    @cached_property
    def Queue(self):  # pragma: no cover
        return QueueReference.make_one(self.boto3_raw_data["Queue"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentContactReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentContactReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyGroups:
    boto3_raw_data: "type_defs.HierarchyGroupsTypeDef" = dataclasses.field()

    @cached_property
    def Level1(self):  # pragma: no cover
        return AgentHierarchyGroup.make_one(self.boto3_raw_data["Level1"])

    @cached_property
    def Level2(self):  # pragma: no cover
        return AgentHierarchyGroup.make_one(self.boto3_raw_data["Level2"])

    @cached_property
    def Level3(self):  # pragma: no cover
        return AgentHierarchyGroup.make_one(self.boto3_raw_data["Level3"])

    @cached_property
    def Level4(self):  # pragma: no cover
        return AgentHierarchyGroup.make_one(self.boto3_raw_data["Level4"])

    @cached_property
    def Level5(self):  # pragma: no cover
        return AgentHierarchyGroup.make_one(self.boto3_raw_data["Level5"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HierarchyGroupsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HierarchyGroupsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedCapabilities:
    boto3_raw_data: "type_defs.AllowedCapabilitiesTypeDef" = dataclasses.field()

    @cached_property
    def Customer(self):  # pragma: no cover
        return ParticipantCapabilities.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Agent(self):  # pragma: no cover
        return ParticipantCapabilities.make_one(self.boto3_raw_data["Agent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllowedCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Customer:
    boto3_raw_data: "type_defs.CustomerTypeDef" = dataclasses.field()

    @cached_property
    def DeviceInfo(self):  # pragma: no cover
        return DeviceInfo.make_one(self.boto3_raw_data["DeviceInfo"])

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return ParticipantCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantDetailsToAdd:
    boto3_raw_data: "type_defs.ParticipantDetailsToAddTypeDef" = dataclasses.field()

    ParticipantRole = field("ParticipantRole")
    DisplayName = field("DisplayName")

    @cached_property
    def ParticipantCapabilities(self):  # pragma: no cover
        return ParticipantCapabilities.make_one(
            self.boto3_raw_data["ParticipantCapabilities"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipantDetailsToAddTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantDetailsToAddTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentQualityMetrics:
    boto3_raw_data: "type_defs.AgentQualityMetricsTypeDef" = dataclasses.field()

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioQualityMetricsInfo.make_one(self.boto3_raw_data["Audio"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentQualityMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentQualityMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerQualityMetrics:
    boto3_raw_data: "type_defs.CustomerQualityMetricsTypeDef" = dataclasses.field()

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioQualityMetricsInfo.make_one(self.boto3_raw_data["Audio"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerQualityMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerQualityMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatusSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.AgentStatusSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AgentStatusSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentStatusSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatusSearchCriteria:
    boto3_raw_data: "type_defs.AgentStatusSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentStatusSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentStatusSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowModuleSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.ContactFlowModuleSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    StateCondition = field("StateCondition")
    StatusCondition = field("StatusCondition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContactFlowModuleSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowModuleSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowModuleSearchCriteria:
    boto3_raw_data: "type_defs.ContactFlowModuleSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    StateCondition = field("StateCondition")
    StatusCondition = field("StatusCondition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContactFlowModuleSearchCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowModuleSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.ContactFlowSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    TypeCondition = field("TypeCondition")
    StateCondition = field("StateCondition")
    StatusCondition = field("StatusCondition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContactFlowSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowSearchCriteria:
    boto3_raw_data: "type_defs.ContactFlowSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    TypeCondition = field("TypeCondition")
    StateCondition = field("StateCondition")
    StatusCondition = field("StatusCondition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactFlowSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailAddressSearchCriteria:
    boto3_raw_data: "type_defs.EmailAddressSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailAddressSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailAddressSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.HoursOfOperationSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HoursOfOperationSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationSearchCriteria:
    boto3_raw_data: "type_defs.HoursOfOperationSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HoursOfOperationSearchCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttributeSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.PredefinedAttributeSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredefinedAttributeSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttributeSearchCriteria:
    boto3_raw_data: "type_defs.PredefinedAttributeSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PredefinedAttributeSearchCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.PromptSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PromptSearchCriteriaPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSearchCriteria:
    boto3_raw_data: "type_defs.PromptSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.QueueSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    QueueTypeCondition = field("QueueTypeCondition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueSearchCriteriaPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueSearchCriteria:
    boto3_raw_data: "type_defs.QueueSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    QueueTypeCondition = field("QueueTypeCondition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickConnectSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.QuickConnectSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.QuickConnectSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickConnectSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickConnectSearchCriteria:
    boto3_raw_data: "type_defs.QuickConnectSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickConnectSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickConnectSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.RoutingProfileSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RoutingProfileSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileSearchCriteria:
    boto3_raw_data: "type_defs.RoutingProfileSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.SecurityProfileSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecurityProfileSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileSearchCriteria:
    boto3_raw_data: "type_defs.SecurityProfileSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SecurityProfileSearchCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserHierarchyGroupSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.UserHierarchyGroupSearchCriteriaPaginatorTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserHierarchyGroupSearchCriteriaPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserHierarchyGroupSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserHierarchyGroupSearchCriteria:
    boto3_raw_data: "type_defs.UserHierarchyGroupSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserHierarchyGroupSearchCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserHierarchyGroupSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentStatusResponse:
    boto3_raw_data: "type_defs.ListAgentStatusResponseTypeDef" = dataclasses.field()

    @cached_property
    def AgentStatusSummaryList(self):  # pragma: no cover
        return AgentStatusSummary.make_many(
            self.boto3_raw_data["AgentStatusSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgentStatusResponse:
    boto3_raw_data: "type_defs.DescribeAgentStatusResponseTypeDef" = dataclasses.field()

    @cached_property
    def AgentStatus(self):  # pragma: no cover
        return AgentStatus.make_one(self.boto3_raw_data["AgentStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgentStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAgentStatusesResponse:
    boto3_raw_data: "type_defs.SearchAgentStatusesResponseTypeDef" = dataclasses.field()

    @cached_property
    def AgentStatuses(self):  # pragma: no cover
        return AgentStatus.make_many(self.boto3_raw_data["AgentStatuses"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchAgentStatusesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAgentStatusesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchCriteriaOutput:
    boto3_raw_data: "type_defs.MatchCriteriaOutputTypeDef" = dataclasses.field()

    @cached_property
    def AgentsCriteria(self):  # pragma: no cover
        return AgentsCriteriaOutput.make_one(self.boto3_raw_data["AgentsCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyticsDataAssociationsResponse:
    boto3_raw_data: "type_defs.ListAnalyticsDataAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Results(self):  # pragma: no cover
        return AnalyticsDataAssociationResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalyticsDataAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyticsDataAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyticsDataLakeDataSetsResponse:
    boto3_raw_data: "type_defs.ListAnalyticsDataLakeDataSetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Results(self):  # pragma: no cover
        return AnalyticsDataSetsResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalyticsDataLakeDataSetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyticsDataLakeDataSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfileApplicationsResponse:
    boto3_raw_data: "type_defs.ListSecurityProfileApplicationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Applications(self):  # pragma: no cover
        return ApplicationOutput.make_many(self.boto3_raw_data["Applications"])

    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfileApplicationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfileApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateLexBotRequest:
    boto3_raw_data: "type_defs.AssociateLexBotRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def LexBot(self):  # pragma: no cover
        return LexBot.make_one(self.boto3_raw_data["LexBot"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateLexBotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateLexBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLexBotsResponse:
    boto3_raw_data: "type_defs.ListLexBotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LexBots(self):  # pragma: no cover
        return LexBot.make_many(self.boto3_raw_data["LexBots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLexBotsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLexBotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateBotRequest:
    boto3_raw_data: "type_defs.AssociateBotRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def LexBot(self):  # pragma: no cover
        return LexBot.make_one(self.boto3_raw_data["LexBot"])

    @cached_property
    def LexV2Bot(self):  # pragma: no cover
        return LexV2Bot.make_one(self.boto3_raw_data["LexV2Bot"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateBotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateBotRequest:
    boto3_raw_data: "type_defs.DisassociateBotRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def LexBot(self):  # pragma: no cover
        return LexBot.make_one(self.boto3_raw_data["LexBot"])

    @cached_property
    def LexV2Bot(self):  # pragma: no cover
        return LexV2Bot.make_one(self.boto3_raw_data["LexV2Bot"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateBotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexBotConfig:
    boto3_raw_data: "type_defs.LexBotConfigTypeDef" = dataclasses.field()

    @cached_property
    def LexBot(self):  # pragma: no cover
        return LexBot.make_one(self.boto3_raw_data["LexBot"])

    @cached_property
    def LexV2Bot(self):  # pragma: no cover
        return LexV2Bot.make_one(self.boto3_raw_data["LexV2Bot"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LexBotConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LexBotConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserProficienciesRequest:
    boto3_raw_data: "type_defs.AssociateUserProficienciesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    UserId = field("UserId")

    @cached_property
    def UserProficiencies(self):  # pragma: no cover
        return UserProficiency.make_many(self.boto3_raw_data["UserProficiencies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateUserProficienciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserProficienciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserProficienciesResponse:
    boto3_raw_data: "type_defs.ListUserProficienciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserProficiencyList(self):  # pragma: no cover
        return UserProficiency.make_many(self.boto3_raw_data["UserProficiencyList"])

    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUserProficienciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserProficienciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserProficienciesRequest:
    boto3_raw_data: "type_defs.UpdateUserProficienciesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    UserId = field("UserId")

    @cached_property
    def UserProficiencies(self):  # pragma: no cover
        return UserProficiency.make_many(self.boto3_raw_data["UserProficiencies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateUserProficienciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserProficienciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedContactsResponse:
    boto3_raw_data: "type_defs.ListAssociatedContactsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContactSummaryList(self):  # pragma: no cover
        return AssociatedContactSummary.make_many(
            self.boto3_raw_data["ContactSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssociatedContactsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedContactsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachedFile:
    boto3_raw_data: "type_defs.AttachedFileTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    FileArn = field("FileArn")
    FileId = field("FileId")
    FileName = field("FileName")
    FileSizeInBytes = field("FileSizeInBytes")
    FileStatus = field("FileStatus")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return CreatedByInfo.make_one(self.boto3_raw_data["CreatedBy"])

    FileUseCaseType = field("FileUseCaseType")
    AssociatedResourceArn = field("AssociatedResourceArn")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachedFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachedFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAttachedFileUploadRequest:
    boto3_raw_data: "type_defs.StartAttachedFileUploadRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    FileName = field("FileName")
    FileSizeInBytes = field("FileSizeInBytes")
    FileUseCaseType = field("FileUseCaseType")
    AssociatedResourceArn = field("AssociatedResourceArn")
    ClientToken = field("ClientToken")
    UrlExpiryInSeconds = field("UrlExpiryInSeconds")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return CreatedByInfo.make_one(self.boto3_raw_data["CreatedBy"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAttachedFileUploadRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAttachedFileUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeAndCondition:
    boto3_raw_data: "type_defs.AttributeAndConditionTypeDef" = dataclasses.field()

    @cached_property
    def TagConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["TagConditions"])

    @cached_property
    def HierarchyGroupCondition(self):  # pragma: no cover
        return HierarchyGroupCondition.make_one(
            self.boto3_raw_data["HierarchyGroupCondition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeAndConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeAndConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommonAttributeAndCondition:
    boto3_raw_data: "type_defs.CommonAttributeAndConditionTypeDef" = dataclasses.field()

    @cached_property
    def TagConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["TagConditions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommonAttributeAndConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommonAttributeAndConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlPlaneTagFilter:
    boto3_raw_data: "type_defs.ControlPlaneTagFilterTypeDef" = dataclasses.field()

    @cached_property
    def OrConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["OrConditions"])

    @cached_property
    def AndConditions(self):  # pragma: no cover
        return TagCondition.make_many(self.boto3_raw_data["AndConditions"])

    @cached_property
    def TagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["TagCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlPlaneTagFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlPlaneTagFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAttributeResponse:
    boto3_raw_data: "type_defs.DescribeInstanceAttributeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attribute(self):  # pragma: no cover
        return Attribute.make_one(self.boto3_raw_data["Attribute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceAttributeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceAttributeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceAttributesResponse:
    boto3_raw_data: "type_defs.ListInstanceAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceAttributesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeetingFeaturesConfiguration:
    boto3_raw_data: "type_defs.MeetingFeaturesConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioFeatures.make_one(self.boto3_raw_data["Audio"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MeetingFeaturesConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MeetingFeaturesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuthenticationProfilesResponse:
    boto3_raw_data: "type_defs.ListAuthenticationProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthenticationProfileSummaryList(self):  # pragma: no cover
        return AuthenticationProfileSummary.make_many(
            self.boto3_raw_data["AuthenticationProfileSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuthenticationProfilesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuthenticationProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuthenticationProfileResponse:
    boto3_raw_data: "type_defs.DescribeAuthenticationProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthenticationProfile(self):  # pragma: no cover
        return AuthenticationProfile.make_one(
            self.boto3_raw_data["AuthenticationProfile"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAuthenticationProfileResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuthenticationProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersResponse:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AvailableNumbersList(self):  # pragma: no cover
        return AvailableNumberSummary.make_many(
            self.boto3_raw_data["AvailableNumbersList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateAnalyticsDataSetResponse:
    boto3_raw_data: "type_defs.BatchAssociateAnalyticsDataSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Created(self):  # pragma: no cover
        return AnalyticsDataAssociationResult.make_many(self.boto3_raw_data["Created"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return ErrorResult.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateAnalyticsDataSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateAnalyticsDataSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateAnalyticsDataSetResponse:
    boto3_raw_data: "type_defs.BatchDisassociateAnalyticsDataSetResponseTypeDef" = (
        dataclasses.field()
    )

    Deleted = field("Deleted")

    @cached_property
    def Errors(self):  # pragma: no cover
        return ErrorResult.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateAnalyticsDataSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateAnalyticsDataSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFlowAssociationResponse:
    boto3_raw_data: "type_defs.BatchGetFlowAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FlowAssociationSummaryList(self):  # pragma: no cover
        return FlowAssociationSummary.make_many(
            self.boto3_raw_data["FlowAssociationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFlowAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFlowAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowAssociationsResponse:
    boto3_raw_data: "type_defs.ListFlowAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FlowAssociationSummaryList(self):  # pragma: no cover
        return FlowAssociationSummary.make_many(
            self.boto3_raw_data["FlowAssociationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowAssociationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutContactResponse:
    boto3_raw_data: "type_defs.BatchPutContactResponseTypeDef" = dataclasses.field()

    @cached_property
    def SuccessfulRequestList(self):  # pragma: no cover
        return SuccessfulRequest.make_many(self.boto3_raw_data["SuccessfulRequestList"])

    @cached_property
    def FailedRequestList(self):  # pragma: no cover
        return FailedRequest.make_many(self.boto3_raw_data["FailedRequestList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseSlaConfigurationOutput:
    boto3_raw_data: "type_defs.CaseSlaConfigurationOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    TargetSlaMinutes = field("TargetSlaMinutes")
    FieldId = field("FieldId")

    @cached_property
    def TargetFieldValues(self):  # pragma: no cover
        return FieldValueUnionOutput.make_many(self.boto3_raw_data["TargetFieldValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseSlaConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseSlaConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValueOutput:
    boto3_raw_data: "type_defs.FieldValueOutputTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Value(self):  # pragma: no cover
        return FieldValueUnionOutput.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatMetrics:
    boto3_raw_data: "type_defs.ChatMetricsTypeDef" = dataclasses.field()

    @cached_property
    def ChatContactMetrics(self):  # pragma: no cover
        return ChatContactMetrics.make_one(self.boto3_raw_data["ChatContactMetrics"])

    @cached_property
    def AgentMetrics(self):  # pragma: no cover
        return ParticipantMetrics.make_one(self.boto3_raw_data["AgentMetrics"])

    @cached_property
    def CustomerMetrics(self):  # pragma: no cover
        return ParticipantMetrics.make_one(self.boto3_raw_data["CustomerMetrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChatMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChatMetricsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContactStreamingRequest:
    boto3_raw_data: "type_defs.StartContactStreamingRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @cached_property
    def ChatStreamingConfiguration(self):  # pragma: no cover
        return ChatStreamingConfiguration.make_one(
            self.boto3_raw_data["ChatStreamingConfiguration"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartContactStreamingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContactStreamingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClaimedPhoneNumberSummary:
    boto3_raw_data: "type_defs.ClaimedPhoneNumberSummaryTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    PhoneNumberArn = field("PhoneNumberArn")
    PhoneNumber = field("PhoneNumber")
    PhoneNumberCountryCode = field("PhoneNumberCountryCode")
    PhoneNumberType = field("PhoneNumberType")
    PhoneNumberDescription = field("PhoneNumberDescription")
    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    Tags = field("Tags")

    @cached_property
    def PhoneNumberStatus(self):  # pragma: no cover
        return PhoneNumberStatus.make_one(self.boto3_raw_data["PhoneNumberStatus"])

    SourcePhoneNumberArn = field("SourcePhoneNumberArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClaimedPhoneNumberSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClaimedPhoneNumberSummaryTypeDef"]
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

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @cached_property
    def NumberCondition(self):  # pragma: no cover
        return NumberCondition.make_one(self.boto3_raw_data["NumberCondition"])

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
class CreatePushNotificationRegistrationRequest:
    boto3_raw_data: "type_defs.CreatePushNotificationRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    PinpointAppArn = field("PinpointAppArn")
    DeviceToken = field("DeviceToken")
    DeviceType = field("DeviceType")

    @cached_property
    def ContactConfiguration(self):  # pragma: no cover
        return ContactConfiguration.make_one(
            self.boto3_raw_data["ContactConfiguration"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePushNotificationRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePushNotificationRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactDataRequest:
    boto3_raw_data: "type_defs.ContactDataRequestTypeDef" = dataclasses.field()

    @cached_property
    def SystemEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["SystemEndpoint"])

    @cached_property
    def CustomerEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["CustomerEndpoint"])

    RequestIdentifier = field("RequestIdentifier")
    QueueId = field("QueueId")
    Attributes = field("Attributes")

    @cached_property
    def Campaign(self):  # pragma: no cover
        return Campaign.make_one(self.boto3_raw_data["Campaign"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserDataFilters:
    boto3_raw_data: "type_defs.UserDataFiltersTypeDef" = dataclasses.field()

    Queues = field("Queues")

    @cached_property
    def ContactFilter(self):  # pragma: no cover
        return ContactFilter.make_one(self.boto3_raw_data["ContactFilter"])

    RoutingProfiles = field("RoutingProfiles")
    Agents = field("Agents")
    UserHierarchyGroups = field("UserHierarchyGroups")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDataFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDataFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowModulesResponse:
    boto3_raw_data: "type_defs.ListContactFlowModulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContactFlowModulesSummaryList(self):  # pragma: no cover
        return ContactFlowModuleSummary.make_many(
            self.boto3_raw_data["ContactFlowModulesSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactFlowModulesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowModulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactFlowModuleResponse:
    boto3_raw_data: "type_defs.DescribeContactFlowModuleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContactFlowModule(self):  # pragma: no cover
        return ContactFlowModule.make_one(self.boto3_raw_data["ContactFlowModule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContactFlowModuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactFlowModuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactFlowModulesResponse:
    boto3_raw_data: "type_defs.SearchContactFlowModulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContactFlowModules(self):  # pragma: no cover
        return ContactFlowModule.make_many(self.boto3_raw_data["ContactFlowModules"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchContactFlowModulesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactFlowModulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowsResponse:
    boto3_raw_data: "type_defs.ListContactFlowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ContactFlowSummaryList(self):  # pragma: no cover
        return ContactFlowSummary.make_many(
            self.boto3_raw_data["ContactFlowSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactFlowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactFlowResponse:
    boto3_raw_data: "type_defs.DescribeContactFlowResponseTypeDef" = dataclasses.field()

    @cached_property
    def ContactFlow(self):  # pragma: no cover
        return ContactFlow.make_one(self.boto3_raw_data["ContactFlow"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactFlowsResponse:
    boto3_raw_data: "type_defs.SearchContactFlowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ContactFlows(self):  # pragma: no cover
        return ContactFlow.make_many(self.boto3_raw_data["ContactFlows"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContactFlowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowVersionsResponse:
    boto3_raw_data: "type_defs.ListContactFlowVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ContactFlowVersionSummaryList(self):  # pragma: no cover
        return ContactFlowVersionSummary.make_many(
            self.boto3_raw_data["ContactFlowVersionSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactFlowVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactMetricsRequest:
    boto3_raw_data: "type_defs.GetContactMetricsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @cached_property
    def Metrics(self):  # pragma: no cover
        return ContactMetricInfo.make_many(self.boto3_raw_data["Metrics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactMetricResult:
    boto3_raw_data: "type_defs.ContactMetricResultTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Value(self):  # pragma: no cover
        return ContactMetricValue.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactMetricResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactSearchSummary:
    boto3_raw_data: "type_defs.ContactSearchSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    InitialContactId = field("InitialContactId")
    PreviousContactId = field("PreviousContactId")
    InitiationMethod = field("InitiationMethod")
    Channel = field("Channel")

    @cached_property
    def QueueInfo(self):  # pragma: no cover
        return ContactSearchSummaryQueueInfo.make_one(self.boto3_raw_data["QueueInfo"])

    @cached_property
    def AgentInfo(self):  # pragma: no cover
        return ContactSearchSummaryAgentInfo.make_one(self.boto3_raw_data["AgentInfo"])

    InitiationTimestamp = field("InitiationTimestamp")
    DisconnectTimestamp = field("DisconnectTimestamp")
    ScheduledTimestamp = field("ScheduledTimestamp")
    SegmentAttributes = field("SegmentAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactSearchSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactFlowVersionRequest:
    boto3_raw_data: "type_defs.CreateContactFlowVersionRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")
    Description = field("Description")
    FlowContentSha256 = field("FlowContentSha256")
    ContactFlowVersion = field("ContactFlowVersion")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateContactFlowVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactFlowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactsTimeRange:
    boto3_raw_data: "type_defs.SearchContactsTimeRangeTypeDef" = dataclasses.field()

    Type = field("Type")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContactsTimeRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactsTimeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactScheduleRequest:
    boto3_raw_data: "type_defs.UpdateContactScheduleRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    ScheduledTime = field("ScheduledTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactScheduleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOutboundVoiceContactRequest:
    boto3_raw_data: "type_defs.StartOutboundVoiceContactRequestTypeDef" = (
        dataclasses.field()
    )

    DestinationPhoneNumber = field("DestinationPhoneNumber")
    ContactFlowId = field("ContactFlowId")
    InstanceId = field("InstanceId")
    Name = field("Name")
    Description = field("Description")
    References = field("References")
    RelatedContactId = field("RelatedContactId")
    ClientToken = field("ClientToken")
    SourcePhoneNumber = field("SourcePhoneNumber")
    QueueId = field("QueueId")
    Attributes = field("Attributes")

    @cached_property
    def AnswerMachineDetectionConfig(self):  # pragma: no cover
        return AnswerMachineDetectionConfig.make_one(
            self.boto3_raw_data["AnswerMachineDetectionConfig"]
        )

    CampaignId = field("CampaignId")
    TrafficType = field("TrafficType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartOutboundVoiceContactRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOutboundVoiceContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskActionDefinitionOutput:
    boto3_raw_data: "type_defs.TaskActionDefinitionOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    ContactFlowId = field("ContactFlowId")
    Description = field("Description")
    References = field("References")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskActionDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskActionDefinition:
    boto3_raw_data: "type_defs.TaskActionDefinitionTypeDef" = dataclasses.field()

    Name = field("Name")
    ContactFlowId = field("ContactFlowId")
    Description = field("Description")
    References = field("References")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParticipantResponse:
    boto3_raw_data: "type_defs.CreateParticipantResponseTypeDef" = dataclasses.field()

    @cached_property
    def ParticipantCredentials(self):  # pragma: no cover
        return ParticipantTokenCredentials.make_one(
            self.boto3_raw_data["ParticipantCredentials"]
        )

    ParticipantId = field("ParticipantId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateParticipantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParticipantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueOutboundCallerConfigRequest:
    boto3_raw_data: "type_defs.UpdateQueueOutboundCallerConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")

    @cached_property
    def OutboundCallerConfig(self):  # pragma: no cover
        return OutboundCallerConfig.make_one(
            self.boto3_raw_data["OutboundCallerConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQueueOutboundCallerConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueOutboundCallerConfigRequestTypeDef"]
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

    InstanceId = field("InstanceId")
    Name = field("Name")
    HoursOfOperationId = field("HoursOfOperationId")
    Description = field("Description")

    @cached_property
    def OutboundCallerConfig(self):  # pragma: no cover
        return OutboundCallerConfig.make_one(
            self.boto3_raw_data["OutboundCallerConfig"]
        )

    @cached_property
    def OutboundEmailConfig(self):  # pragma: no cover
        return OutboundEmailConfig.make_one(self.boto3_raw_data["OutboundEmailConfig"])

    MaxContacts = field("MaxContacts")
    QuickConnectIds = field("QuickConnectIds")
    Tags = field("Tags")

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
class Queue:
    boto3_raw_data: "type_defs.QueueTypeDef" = dataclasses.field()

    Name = field("Name")
    QueueArn = field("QueueArn")
    QueueId = field("QueueId")
    Description = field("Description")

    @cached_property
    def OutboundCallerConfig(self):  # pragma: no cover
        return OutboundCallerConfig.make_one(
            self.boto3_raw_data["OutboundCallerConfig"]
        )

    @cached_property
    def OutboundEmailConfig(self):  # pragma: no cover
        return OutboundEmailConfig.make_one(self.boto3_raw_data["OutboundEmailConfig"])

    HoursOfOperationId = field("HoursOfOperationId")
    MaxContacts = field("MaxContacts")
    Status = field("Status")
    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQueueOutboundEmailConfigRequest:
    boto3_raw_data: "type_defs.UpdateQueueOutboundEmailConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")

    @cached_property
    def OutboundEmailConfig(self):  # pragma: no cover
        return OutboundEmailConfig.make_one(self.boto3_raw_data["OutboundEmailConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateQueueOutboundEmailConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQueueOutboundEmailConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserIdentityInfoRequest:
    boto3_raw_data: "type_defs.UpdateUserIdentityInfoRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityInfo(self):  # pragma: no cover
        return UserIdentityInfo.make_one(self.boto3_raw_data["IdentityInfo"])

    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateUserIdentityInfoRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserIdentityInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    Username = field("Username")

    @cached_property
    def PhoneConfig(self):  # pragma: no cover
        return UserPhoneConfig.make_one(self.boto3_raw_data["PhoneConfig"])

    SecurityProfileIds = field("SecurityProfileIds")
    RoutingProfileId = field("RoutingProfileId")
    InstanceId = field("InstanceId")
    Password = field("Password")

    @cached_property
    def IdentityInfo(self):  # pragma: no cover
        return UserIdentityInfo.make_one(self.boto3_raw_data["IdentityInfo"])

    DirectoryUserId = field("DirectoryUserId")
    HierarchyGroupId = field("HierarchyGroupId")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserPhoneConfigRequest:
    boto3_raw_data: "type_defs.UpdateUserPhoneConfigRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneConfig(self):  # pragma: no cover
        return UserPhoneConfig.make_one(self.boto3_raw_data["PhoneConfig"])

    UserId = field("UserId")
    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserPhoneConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserPhoneConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Username = field("Username")

    @cached_property
    def IdentityInfo(self):  # pragma: no cover
        return UserIdentityInfo.make_one(self.boto3_raw_data["IdentityInfo"])

    @cached_property
    def PhoneConfig(self):  # pragma: no cover
        return UserPhoneConfig.make_one(self.boto3_raw_data["PhoneConfig"])

    DirectoryUserId = field("DirectoryUserId")
    SecurityProfileIds = field("SecurityProfileIds")
    RoutingProfileId = field("RoutingProfileId")
    HierarchyGroupId = field("HierarchyGroupId")
    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

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
class CreateViewRequest:
    boto3_raw_data: "type_defs.CreateViewRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Status = field("Status")

    @cached_property
    def Content(self):  # pragma: no cover
        return ViewInputContent.make_one(self.boto3_raw_data["Content"])

    Name = field("Name")
    ClientToken = field("ClientToken")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateViewRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateViewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateViewContentRequest:
    boto3_raw_data: "type_defs.UpdateViewContentRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")
    Status = field("Status")

    @cached_property
    def Content(self):  # pragma: no cover
        return ViewInputContent.make_one(self.boto3_raw_data["Content"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateViewContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateViewContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFederationTokenResponse:
    boto3_raw_data: "type_defs.GetFederationTokenResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    SignInUrl = field("SignInUrl")
    UserArn = field("UserArn")
    UserId = field("UserId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFederationTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFederationTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaConcurrency:
    boto3_raw_data: "type_defs.MediaConcurrencyTypeDef" = dataclasses.field()

    Channel = field("Channel")
    Concurrency = field("Concurrency")

    @cached_property
    def CrossChannelBehavior(self):  # pragma: no cover
        return CrossChannelBehavior.make_one(
            self.boto3_raw_data["CrossChannelBehavior"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaConcurrencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaConcurrencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentMetricData:
    boto3_raw_data: "type_defs.CurrentMetricDataTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return CurrentMetric.make_one(self.boto3_raw_data["Metric"])

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CurrentMetricDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrentMetricDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationOverrideSearchCriteriaPaginator:
    boto3_raw_data: (
        "type_defs.HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef"
    ) = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @cached_property
    def DateCondition(self):  # pragma: no cover
        return DateCondition.make_one(self.boto3_raw_data["DateCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef"
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
                "type_defs.HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationOverrideSearchCriteria:
    boto3_raw_data: "type_defs.HoursOfOperationOverrideSearchCriteriaTypeDef" = (
        dataclasses.field()
    )

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @cached_property
    def DateCondition(self):  # pragma: no cover
        return DateCondition.make_one(self.boto3_raw_data["DateCondition"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HoursOfOperationOverrideSearchCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationOverrideSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDefaultVocabulariesResponse:
    boto3_raw_data: "type_defs.ListDefaultVocabulariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DefaultVocabularyList(self):  # pragma: no cover
        return DefaultVocabulary.make_many(self.boto3_raw_data["DefaultVocabularyList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDefaultVocabulariesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDefaultVocabulariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePromptResponse:
    boto3_raw_data: "type_defs.DescribePromptResponseTypeDef" = dataclasses.field()

    @cached_property
    def Prompt(self):  # pragma: no cover
        return Prompt.make_one(self.boto3_raw_data["Prompt"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPromptsResponse:
    boto3_raw_data: "type_defs.SearchPromptsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Prompts(self):  # pragma: no cover
        return Prompt.make_many(self.boto3_raw_data["Prompts"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchPromptsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPromptsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityProfileResponse:
    boto3_raw_data: "type_defs.DescribeSecurityProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityProfile(self):  # pragma: no cover
        return SecurityProfile.make_one(self.boto3_raw_data["SecurityProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSecurityProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrafficDistributionGroupResponse:
    boto3_raw_data: "type_defs.DescribeTrafficDistributionGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficDistributionGroup(self):  # pragma: no cover
        return TrafficDistributionGroup.make_one(
            self.boto3_raw_data["TrafficDistributionGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrafficDistributionGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrafficDistributionGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVocabularyResponse:
    boto3_raw_data: "type_defs.DescribeVocabularyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Vocabulary(self):  # pragma: no cover
        return Vocabulary.make_one(self.boto3_raw_data["Vocabulary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVocabularyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimensions:
    boto3_raw_data: "type_defs.DimensionsTypeDef" = dataclasses.field()

    @cached_property
    def Queue(self):  # pragma: no cover
        return QueueReference.make_one(self.boto3_raw_data["Queue"])

    Channel = field("Channel")

    @cached_property
    def RoutingProfile(self):  # pragma: no cover
        return RoutingProfileReference.make_one(self.boto3_raw_data["RoutingProfile"])

    RoutingStepExpression = field("RoutingStepExpression")

    @cached_property
    def AgentStatus(self):  # pragma: no cover
        return AgentStatusIdentifier.make_one(self.boto3_raw_data["AgentStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateRoutingProfileQueuesRequest:
    boto3_raw_data: "type_defs.DisassociateRoutingProfileQueuesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @cached_property
    def QueueReferences(self):  # pragma: no cover
        return RoutingProfileQueueReference.make_many(
            self.boto3_raw_data["QueueReferences"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateRoutingProfileQueuesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateRoutingProfileQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileQueueConfig:
    boto3_raw_data: "type_defs.RoutingProfileQueueConfigTypeDef" = dataclasses.field()

    @cached_property
    def QueueReference(self):  # pragma: no cover
        return RoutingProfileQueueReference.make_one(
            self.boto3_raw_data["QueueReference"]
        )

    Priority = field("Priority")
    Delay = field("Delay")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileQueueConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileQueueConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateUserProficienciesRequest:
    boto3_raw_data: "type_defs.DisassociateUserProficienciesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    UserId = field("UserId")

    @cached_property
    def UserProficiencies(self):  # pragma: no cover
        return UserProficiencyDisassociate.make_many(
            self.boto3_raw_data["UserProficiencies"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateUserProficienciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateUserProficienciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopContactRequest:
    boto3_raw_data: "type_defs.StopContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    InstanceId = field("InstanceId")

    @cached_property
    def DisconnectReason(self):  # pragma: no cover
        return DisconnectReason.make_one(self.boto3_raw_data["DisconnectReason"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAttachedFileResponse:
    boto3_raw_data: "type_defs.GetAttachedFileResponseTypeDef" = dataclasses.field()

    FileArn = field("FileArn")
    FileId = field("FileId")
    CreationTime = field("CreationTime")
    FileStatus = field("FileStatus")
    FileName = field("FileName")
    FileSizeInBytes = field("FileSizeInBytes")
    AssociatedResourceArn = field("AssociatedResourceArn")
    FileUseCaseType = field("FileUseCaseType")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return CreatedByInfo.make_one(self.boto3_raw_data["CreatedBy"])

    @cached_property
    def DownloadUrlMetadata(self):  # pragma: no cover
        return DownloadUrlMetadata.make_one(self.boto3_raw_data["DownloadUrlMetadata"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAttachedFileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAttachedFileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundAdditionalRecipients:
    boto3_raw_data: "type_defs.InboundAdditionalRecipientsTypeDef" = dataclasses.field()

    @cached_property
    def ToAddresses(self):  # pragma: no cover
        return EmailAddressInfo.make_many(self.boto3_raw_data["ToAddresses"])

    @cached_property
    def CcAddresses(self):  # pragma: no cover
        return EmailAddressInfo.make_many(self.boto3_raw_data["CcAddresses"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InboundAdditionalRecipientsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundAdditionalRecipientsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundAdditionalRecipients:
    boto3_raw_data: "type_defs.OutboundAdditionalRecipientsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CcEmailAddresses(self):  # pragma: no cover
        return EmailAddressInfo.make_many(self.boto3_raw_data["CcEmailAddresses"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundAdditionalRecipientsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundAdditionalRecipientsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchEmailAddressesResponse:
    boto3_raw_data: "type_defs.SearchEmailAddressesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EmailAddresses(self):  # pragma: no cover
        return EmailAddressMetadata.make_many(self.boto3_raw_data["EmailAddresses"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchEmailAddressesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchEmailAddressesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamConfig:
    boto3_raw_data: "type_defs.KinesisVideoStreamConfigTypeDef" = dataclasses.field()

    Prefix = field("Prefix")
    RetentionPeriodHours = field("RetentionPeriodHours")

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisVideoStreamConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Config:
    boto3_raw_data: "type_defs.S3ConfigTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    BucketPrefix = field("BucketPrefix")

    @cached_property
    def EncryptionConfig(self):  # pragma: no cover
        return EncryptionConfig.make_one(self.boto3_raw_data["EncryptionConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationAnswerInput:
    boto3_raw_data: "type_defs.EvaluationAnswerInputTypeDef" = dataclasses.field()

    @cached_property
    def Value(self):  # pragma: no cover
        return EvaluationAnswerData.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationAnswerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationAnswerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationAnswerOutput:
    boto3_raw_data: "type_defs.EvaluationAnswerOutputTypeDef" = dataclasses.field()

    @cached_property
    def Value(self):  # pragma: no cover
        return EvaluationAnswerData.make_one(self.boto3_raw_data["Value"])

    @cached_property
    def SystemSuggestedValue(self):  # pragma: no cover
        return EvaluationAnswerData.make_one(
            self.boto3_raw_data["SystemSuggestedValue"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationAnswerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationAnswerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormNumericQuestionAutomation:
    boto3_raw_data: "type_defs.EvaluationFormNumericQuestionAutomationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PropertyValue(self):  # pragma: no cover
        return NumericQuestionPropertyValueAutomation.make_one(
            self.boto3_raw_data["PropertyValue"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormNumericQuestionAutomationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormNumericQuestionAutomationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSingleSelectQuestionAutomationOption:
    boto3_raw_data: (
        "type_defs.EvaluationFormSingleSelectQuestionAutomationOptionTypeDef"
    ) = dataclasses.field()

    @cached_property
    def RuleCategory(self):  # pragma: no cover
        return SingleSelectQuestionRuleCategoryAutomation.make_one(
            self.boto3_raw_data["RuleCategory"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormSingleSelectQuestionAutomationOptionTypeDef"
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
                "type_defs.EvaluationFormSingleSelectQuestionAutomationOptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationFormsResponse:
    boto3_raw_data: "type_defs.ListEvaluationFormsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EvaluationFormSummaryList(self):  # pragma: no cover
        return EvaluationFormSummary.make_many(
            self.boto3_raw_data["EvaluationFormSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEvaluationFormsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationFormsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationFormVersionsResponse:
    boto3_raw_data: "type_defs.ListEvaluationFormVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EvaluationFormVersionSummaryList(self):  # pragma: no cover
        return EvaluationFormVersionSummary.make_many(
            self.boto3_raw_data["EvaluationFormVersionSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEvaluationFormVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationFormVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationMetadata:
    boto3_raw_data: "type_defs.EvaluationMetadataTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    EvaluatorArn = field("EvaluatorArn")
    ContactAgentId = field("ContactAgentId")

    @cached_property
    def Score(self):  # pragma: no cover
        return EvaluationScore.make_one(self.boto3_raw_data["Score"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationSummary:
    boto3_raw_data: "type_defs.EvaluationSummaryTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")
    EvaluationArn = field("EvaluationArn")
    EvaluationFormTitle = field("EvaluationFormTitle")
    EvaluationFormId = field("EvaluationFormId")
    Status = field("Status")
    EvaluatorArn = field("EvaluatorArn")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def Score(self):  # pragma: no cover
        return EvaluationScore.make_one(self.boto3_raw_data["Score"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCurrentMetricDataRequest:
    boto3_raw_data: "type_defs.GetCurrentMetricDataRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def CurrentMetrics(self):  # pragma: no cover
        return CurrentMetric.make_many(self.boto3_raw_data["CurrentMetrics"])

    Groupings = field("Groupings")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return CurrentMetricSortCriteria.make_many(self.boto3_raw_data["SortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCurrentMetricDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCurrentMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentStatusRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentStatusRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AgentStatusTypes = field("AgentStatusTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentStatusRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentStatusRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApprovedOriginsRequestPaginate:
    boto3_raw_data: "type_defs.ListApprovedOriginsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApprovedOriginsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApprovedOriginsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuthenticationProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListAuthenticationProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuthenticationProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuthenticationProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsRequestPaginate:
    boto3_raw_data: "type_defs.ListBotsRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    LexVersion = field("LexVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactEvaluationsRequestPaginate:
    boto3_raw_data: "type_defs.ListContactEvaluationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContactEvaluationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactEvaluationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowModulesRequestPaginate:
    boto3_raw_data: "type_defs.ListContactFlowModulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowModuleState = field("ContactFlowModuleState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContactFlowModulesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowModulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListContactFlowVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContactFlowVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactFlowsRequestPaginate:
    boto3_raw_data: "type_defs.ListContactFlowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactFlowTypes = field("ContactFlowTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactFlowsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactFlowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactReferencesRequestPaginate:
    boto3_raw_data: "type_defs.ListContactReferencesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    ReferenceTypes = field("ReferenceTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContactReferencesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactReferencesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDefaultVocabulariesRequestPaginate:
    boto3_raw_data: "type_defs.ListDefaultVocabulariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    LanguageCode = field("LanguageCode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDefaultVocabulariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDefaultVocabulariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationFormVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListEvaluationFormVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEvaluationFormVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationFormVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationFormsRequestPaginate:
    boto3_raw_data: "type_defs.ListEvaluationFormsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEvaluationFormsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationFormsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ResourceType = field("ResourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlowAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHoursOfOperationOverridesRequestPaginate:
    boto3_raw_data: "type_defs.ListHoursOfOperationOverridesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHoursOfOperationOverridesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHoursOfOperationOverridesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHoursOfOperationsRequestPaginate:
    boto3_raw_data: "type_defs.ListHoursOfOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHoursOfOperationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHoursOfOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstanceAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceStorageConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListInstanceStorageConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ResourceType = field("ResourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceStorageConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceStorageConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListIntegrationAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    IntegrationType = field("IntegrationType")
    IntegrationArn = field("IntegrationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIntegrationAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLambdaFunctionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLambdaFunctionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLambdaFunctionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLambdaFunctionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLexBotsRequestPaginate:
    boto3_raw_data: "type_defs.ListLexBotsRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLexBotsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLexBotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersRequestPaginate:
    boto3_raw_data: "type_defs.ListPhoneNumbersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    PhoneNumberTypes = field("PhoneNumberTypes")
    PhoneNumberCountryCodes = field("PhoneNumberCountryCodes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersV2RequestPaginate:
    boto3_raw_data: "type_defs.ListPhoneNumbersV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    PhoneNumberCountryCodes = field("PhoneNumberCountryCodes")
    PhoneNumberTypes = field("PhoneNumberTypes")
    PhoneNumberPrefix = field("PhoneNumberPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPhoneNumbersV2RequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredefinedAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListPredefinedAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPredefinedAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredefinedAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptsRequestPaginate:
    boto3_raw_data: "type_defs.ListPromptsRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueQuickConnectsRequestPaginate:
    boto3_raw_data: "type_defs.ListQueueQuickConnectsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QueueId = field("QueueId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueueQuickConnectsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueQuickConnectsRequestPaginateTypeDef"]
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

    InstanceId = field("InstanceId")
    QueueTypes = field("QueueTypes")

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
class ListQuickConnectsRequestPaginate:
    boto3_raw_data: "type_defs.ListQuickConnectsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QuickConnectTypes = field("QuickConnectTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQuickConnectsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuickConnectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingProfileQueuesRequestPaginate:
    boto3_raw_data: "type_defs.ListRoutingProfileQueuesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRoutingProfileQueuesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingProfileQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListRoutingProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRoutingProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListRulesRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PublishStatus = field("PublishStatus")
    EventSourceName = field("EventSourceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSecurityKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfileApplicationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListSecurityProfileApplicationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    SecurityProfileId = field("SecurityProfileId")
    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfileApplicationsRequestPaginateTypeDef"
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
                "type_defs.ListSecurityProfileApplicationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilePermissionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityProfilePermissionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileId = field("SecurityProfileId")
    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilePermissionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilePermissionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListTaskTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Status = field("Status")
    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTaskTemplatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficDistributionGroupUsersRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListTrafficDistributionGroupUsersRequestPaginateTypeDef"
    ) = dataclasses.field()

    TrafficDistributionGroupId = field("TrafficDistributionGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficDistributionGroupUsersRequestPaginateTypeDef"
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
                "type_defs.ListTrafficDistributionGroupUsersRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficDistributionGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrafficDistributionGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficDistributionGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficDistributionGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUseCasesRequestPaginate:
    boto3_raw_data: "type_defs.ListUseCasesRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    IntegrationAssociationId = field("IntegrationAssociationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUseCasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUseCasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserHierarchyGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListUserHierarchyGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUserHierarchyGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserHierarchyGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserProficienciesRequestPaginate:
    boto3_raw_data: "type_defs.ListUserProficienciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    UserId = field("UserId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUserProficienciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserProficienciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViewVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListViewVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ViewId = field("ViewId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListViewVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViewVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViewsRequestPaginate:
    boto3_raw_data: "type_defs.ListViewsRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListViewsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViewsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersRequestPaginate:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberCountryCode = field("PhoneNumberCountryCode")
    PhoneNumberType = field("PhoneNumberType")
    TargetArn = field("TargetArn")
    InstanceId = field("InstanceId")
    PhoneNumberPrefix = field("PhoneNumberPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVocabulariesRequestPaginate:
    boto3_raw_data: "type_defs.SearchVocabulariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    State = field("State")
    NameStartsWith = field("NameStartsWith")
    LanguageCode = field("LanguageCode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchVocabulariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVocabulariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyPathReference:
    boto3_raw_data: "type_defs.HierarchyPathReferenceTypeDef" = dataclasses.field()

    @cached_property
    def LevelOne(self):  # pragma: no cover
        return HierarchyGroupSummaryReference.make_one(self.boto3_raw_data["LevelOne"])

    @cached_property
    def LevelTwo(self):  # pragma: no cover
        return HierarchyGroupSummaryReference.make_one(self.boto3_raw_data["LevelTwo"])

    @cached_property
    def LevelThree(self):  # pragma: no cover
        return HierarchyGroupSummaryReference.make_one(
            self.boto3_raw_data["LevelThree"]
        )

    @cached_property
    def LevelFour(self):  # pragma: no cover
        return HierarchyGroupSummaryReference.make_one(self.boto3_raw_data["LevelFour"])

    @cached_property
    def LevelFive(self):  # pragma: no cover
        return HierarchyGroupSummaryReference.make_one(self.boto3_raw_data["LevelFive"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchyPathReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyPathReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyPath:
    boto3_raw_data: "type_defs.HierarchyPathTypeDef" = dataclasses.field()

    @cached_property
    def LevelOne(self):  # pragma: no cover
        return HierarchyGroupSummary.make_one(self.boto3_raw_data["LevelOne"])

    @cached_property
    def LevelTwo(self):  # pragma: no cover
        return HierarchyGroupSummary.make_one(self.boto3_raw_data["LevelTwo"])

    @cached_property
    def LevelThree(self):  # pragma: no cover
        return HierarchyGroupSummary.make_one(self.boto3_raw_data["LevelThree"])

    @cached_property
    def LevelFour(self):  # pragma: no cover
        return HierarchyGroupSummary.make_one(self.boto3_raw_data["LevelFour"])

    @cached_property
    def LevelFive(self):  # pragma: no cover
        return HierarchyGroupSummary.make_one(self.boto3_raw_data["LevelFive"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HierarchyPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HierarchyPathTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserHierarchyGroupsResponse:
    boto3_raw_data: "type_defs.ListUserHierarchyGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserHierarchyGroupSummaryList(self):  # pragma: no cover
        return HierarchyGroupSummary.make_many(
            self.boto3_raw_data["UserHierarchyGroupSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUserHierarchyGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserHierarchyGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyStructure:
    boto3_raw_data: "type_defs.HierarchyStructureTypeDef" = dataclasses.field()

    @cached_property
    def LevelOne(self):  # pragma: no cover
        return HierarchyLevel.make_one(self.boto3_raw_data["LevelOne"])

    @cached_property
    def LevelTwo(self):  # pragma: no cover
        return HierarchyLevel.make_one(self.boto3_raw_data["LevelTwo"])

    @cached_property
    def LevelThree(self):  # pragma: no cover
        return HierarchyLevel.make_one(self.boto3_raw_data["LevelThree"])

    @cached_property
    def LevelFour(self):  # pragma: no cover
        return HierarchyLevel.make_one(self.boto3_raw_data["LevelFour"])

    @cached_property
    def LevelFive(self):  # pragma: no cover
        return HierarchyLevel.make_one(self.boto3_raw_data["LevelFive"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchyStructureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyStructureUpdate:
    boto3_raw_data: "type_defs.HierarchyStructureUpdateTypeDef" = dataclasses.field()

    @cached_property
    def LevelOne(self):  # pragma: no cover
        return HierarchyLevelUpdate.make_one(self.boto3_raw_data["LevelOne"])

    @cached_property
    def LevelTwo(self):  # pragma: no cover
        return HierarchyLevelUpdate.make_one(self.boto3_raw_data["LevelTwo"])

    @cached_property
    def LevelThree(self):  # pragma: no cover
        return HierarchyLevelUpdate.make_one(self.boto3_raw_data["LevelThree"])

    @cached_property
    def LevelFour(self):  # pragma: no cover
        return HierarchyLevelUpdate.make_one(self.boto3_raw_data["LevelFour"])

    @cached_property
    def LevelFive(self):  # pragma: no cover
        return HierarchyLevelUpdate.make_one(self.boto3_raw_data["LevelFive"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HierarchyStructureUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchyStructureUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoricalMetric:
    boto3_raw_data: "type_defs.HistoricalMetricTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Threshold(self):  # pragma: no cover
        return Threshold.make_one(self.boto3_raw_data["Threshold"])

    Statistic = field("Statistic")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HistoricalMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationConfig:
    boto3_raw_data: "type_defs.HoursOfOperationConfigTypeDef" = dataclasses.field()

    Day = field("Day")

    @cached_property
    def StartTime(self):  # pragma: no cover
        return HoursOfOperationTimeSlice.make_one(self.boto3_raw_data["StartTime"])

    @cached_property
    def EndTime(self):  # pragma: no cover
        return HoursOfOperationTimeSlice.make_one(self.boto3_raw_data["EndTime"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HoursOfOperationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationOverrideConfig:
    boto3_raw_data: "type_defs.HoursOfOperationOverrideConfigTypeDef" = (
        dataclasses.field()
    )

    Day = field("Day")

    @cached_property
    def StartTime(self):  # pragma: no cover
        return OverrideTimeSlice.make_one(self.boto3_raw_data["StartTime"])

    @cached_property
    def EndTime(self):  # pragma: no cover
        return OverrideTimeSlice.make_one(self.boto3_raw_data["EndTime"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HoursOfOperationOverrideConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationOverrideConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperationalHour:
    boto3_raw_data: "type_defs.OperationalHourTypeDef" = dataclasses.field()

    @cached_property
    def Start(self):  # pragma: no cover
        return OverrideTimeSlice.make_one(self.boto3_raw_data["Start"])

    @cached_property
    def End(self):  # pragma: no cover
        return OverrideTimeSlice.make_one(self.boto3_raw_data["End"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperationalHourTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperationalHourTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHoursOfOperationsResponse:
    boto3_raw_data: "type_defs.ListHoursOfOperationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HoursOfOperationSummaryList(self):  # pragma: no cover
        return HoursOfOperationSummary.make_many(
            self.boto3_raw_data["HoursOfOperationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHoursOfOperationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHoursOfOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundEmailContent:
    boto3_raw_data: "type_defs.InboundEmailContentTypeDef" = dataclasses.field()

    MessageSourceType = field("MessageSourceType")

    @cached_property
    def RawMessage(self):  # pragma: no cover
        return InboundRawMessage.make_one(self.boto3_raw_data["RawMessage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InboundEmailContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundEmailContentTypeDef"]
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

    Id = field("Id")
    Arn = field("Arn")
    IdentityManagementType = field("IdentityManagementType")
    InstanceAlias = field("InstanceAlias")
    CreatedTime = field("CreatedTime")
    ServiceRole = field("ServiceRole")
    InstanceStatus = field("InstanceStatus")

    @cached_property
    def StatusReason(self):  # pragma: no cover
        return InstanceStatusReason.make_one(self.boto3_raw_data["StatusReason"])

    InboundCallsEnabled = field("InboundCallsEnabled")
    OutboundCallsEnabled = field("OutboundCallsEnabled")
    InstanceAccessUrl = field("InstanceAccessUrl")
    Tags = field("Tags")

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
class ListInstancesResponse:
    boto3_raw_data: "type_defs.ListInstancesResponseTypeDef" = dataclasses.field()

    @cached_property
    def InstanceSummaryList(self):  # pragma: no cover
        return InstanceSummary.make_many(self.boto3_raw_data["InstanceSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationAssociationsResponse:
    boto3_raw_data: "type_defs.ListIntegrationAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IntegrationAssociationSummaryList(self):  # pragma: no cover
        return IntegrationAssociationSummary.make_many(
            self.boto3_raw_data["IntegrationAssociationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIntegrationAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvisibleFieldInfo:
    boto3_raw_data: "type_defs.InvisibleFieldInfoTypeDef" = dataclasses.field()

    @cached_property
    def Id(self):  # pragma: no cover
        return TaskTemplateFieldIdentifier.make_one(self.boto3_raw_data["Id"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvisibleFieldInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvisibleFieldInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadOnlyFieldInfo:
    boto3_raw_data: "type_defs.ReadOnlyFieldInfoTypeDef" = dataclasses.field()

    @cached_property
    def Id(self):  # pragma: no cover
        return TaskTemplateFieldIdentifier.make_one(self.boto3_raw_data["Id"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadOnlyFieldInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadOnlyFieldInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequiredFieldInfo:
    boto3_raw_data: "type_defs.RequiredFieldInfoTypeDef" = dataclasses.field()

    @cached_property
    def Id(self):  # pragma: no cover
        return TaskTemplateFieldIdentifier.make_one(self.boto3_raw_data["Id"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequiredFieldInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequiredFieldInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateDefaultFieldValue:
    boto3_raw_data: "type_defs.TaskTemplateDefaultFieldValueTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Id(self):  # pragma: no cover
        return TaskTemplateFieldIdentifier.make_one(self.boto3_raw_data["Id"])

    DefaultValue = field("DefaultValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskTemplateDefaultFieldValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateDefaultFieldValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateFieldOutput:
    boto3_raw_data: "type_defs.TaskTemplateFieldOutputTypeDef" = dataclasses.field()

    @cached_property
    def Id(self):  # pragma: no cover
        return TaskTemplateFieldIdentifier.make_one(self.boto3_raw_data["Id"])

    Description = field("Description")
    Type = field("Type")
    SingleSelectOptions = field("SingleSelectOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateFieldOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateField:
    boto3_raw_data: "type_defs.TaskTemplateFieldTypeDef" = dataclasses.field()

    @cached_property
    def Id(self):  # pragma: no cover
        return TaskTemplateFieldIdentifier.make_one(self.boto3_raw_data["Id"])

    Description = field("Description")
    Type = field("Type")
    SingleSelectOptions = field("SingleSelectOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersResponse:
    boto3_raw_data: "type_defs.ListPhoneNumbersResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumberSummaryList(self):  # pragma: no cover
        return PhoneNumberSummary.make_many(
            self.boto3_raw_data["PhoneNumberSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersV2Response:
    boto3_raw_data: "type_defs.ListPhoneNumbersV2ResponseTypeDef" = dataclasses.field()

    @cached_property
    def ListPhoneNumbersSummaryList(self):  # pragma: no cover
        return ListPhoneNumbersSummary.make_many(
            self.boto3_raw_data["ListPhoneNumbersSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPredefinedAttributesResponse:
    boto3_raw_data: "type_defs.ListPredefinedAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PredefinedAttributeSummaryList(self):  # pragma: no cover
        return PredefinedAttributeSummary.make_many(
            self.boto3_raw_data["PredefinedAttributeSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPredefinedAttributesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPredefinedAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptsResponse:
    boto3_raw_data: "type_defs.ListPromptsResponseTypeDef" = dataclasses.field()

    @cached_property
    def PromptSummaryList(self):  # pragma: no cover
        return PromptSummary.make_many(self.boto3_raw_data["PromptSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueueQuickConnectsResponse:
    boto3_raw_data: "type_defs.ListQueueQuickConnectsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QuickConnectSummaryList(self):  # pragma: no cover
        return QuickConnectSummary.make_many(
            self.boto3_raw_data["QuickConnectSummaryList"]
        )

    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueueQuickConnectsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueueQuickConnectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQuickConnectsResponse:
    boto3_raw_data: "type_defs.ListQuickConnectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def QuickConnectSummaryList(self):  # pragma: no cover
        return QuickConnectSummary.make_many(
            self.boto3_raw_data["QuickConnectSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQuickConnectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQuickConnectsResponseTypeDef"]
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
    def QueueSummaryList(self):  # pragma: no cover
        return QueueSummary.make_many(self.boto3_raw_data["QueueSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class ListRoutingProfileQueuesResponse:
    boto3_raw_data: "type_defs.ListRoutingProfileQueuesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RoutingProfileQueueConfigSummaryList(self):  # pragma: no cover
        return RoutingProfileQueueConfigSummary.make_many(
            self.boto3_raw_data["RoutingProfileQueueConfigSummaryList"]
        )

    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRoutingProfileQueuesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingProfileQueuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingProfilesResponse:
    boto3_raw_data: "type_defs.ListRoutingProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def RoutingProfileSummaryList(self):  # pragma: no cover
        return RoutingProfileSummary.make_many(
            self.boto3_raw_data["RoutingProfileSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutingProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityKeysResponse:
    boto3_raw_data: "type_defs.ListSecurityKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def SecurityKeys(self):  # pragma: no cover
        return SecurityKey.make_many(self.boto3_raw_data["SecurityKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesResponse:
    boto3_raw_data: "type_defs.ListSecurityProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityProfileSummaryList(self):  # pragma: no cover
        return SecurityProfileSummary.make_many(
            self.boto3_raw_data["SecurityProfileSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskTemplatesResponse:
    boto3_raw_data: "type_defs.ListTaskTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TaskTemplates(self):  # pragma: no cover
        return TaskTemplateMetadata.make_many(self.boto3_raw_data["TaskTemplates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaskTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficDistributionGroupUsersResponse:
    boto3_raw_data: "type_defs.ListTrafficDistributionGroupUsersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficDistributionGroupUserSummaryList(self):  # pragma: no cover
        return TrafficDistributionGroupUserSummary.make_many(
            self.boto3_raw_data["TrafficDistributionGroupUserSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficDistributionGroupUsersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficDistributionGroupUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficDistributionGroupsResponse:
    boto3_raw_data: "type_defs.ListTrafficDistributionGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficDistributionGroupSummaryList(self):  # pragma: no cover
        return TrafficDistributionGroupSummary.make_many(
            self.boto3_raw_data["TrafficDistributionGroupSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficDistributionGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficDistributionGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUseCasesResponse:
    boto3_raw_data: "type_defs.ListUseCasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def UseCaseSummaryList(self):  # pragma: no cover
        return UseCase.make_many(self.boto3_raw_data["UseCaseSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUseCasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUseCasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserSummaryList(self):  # pragma: no cover
        return UserSummary.make_many(self.boto3_raw_data["UserSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViewVersionsResponse:
    boto3_raw_data: "type_defs.ListViewVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ViewVersionSummaryList(self):  # pragma: no cover
        return ViewVersionSummary.make_many(
            self.boto3_raw_data["ViewVersionSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListViewVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViewVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViewsResponse:
    boto3_raw_data: "type_defs.ListViewsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ViewsSummaryList(self):  # pragma: no cover
        return ViewSummary.make_many(self.boto3_raw_data["ViewsSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListViewsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViewsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricV2Output:
    boto3_raw_data: "type_defs.MetricV2OutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Threshold(self):  # pragma: no cover
        return ThresholdV2.make_many(self.boto3_raw_data["Threshold"])

    @cached_property
    def MetricFilters(self):  # pragma: no cover
        return MetricFilterV2Output.make_many(self.boto3_raw_data["MetricFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricV2OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricV2OutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewSessionDetails:
    boto3_raw_data: "type_defs.NewSessionDetailsTypeDef" = dataclasses.field()

    SupportedMessagingContentTypes = field("SupportedMessagingContentTypes")

    @cached_property
    def ParticipantDetails(self):  # pragma: no cover
        return ParticipantDetails.make_one(self.boto3_raw_data["ParticipantDetails"])

    Attributes = field("Attributes")

    @cached_property
    def StreamingConfiguration(self):  # pragma: no cover
        return ChatStreamingConfiguration.make_one(
            self.boto3_raw_data["StreamingConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NewSessionDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewSessionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendNotificationActionDefinitionOutput:
    boto3_raw_data: "type_defs.SendNotificationActionDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    DeliveryMethod = field("DeliveryMethod")
    Content = field("Content")
    ContentType = field("ContentType")

    @cached_property
    def Recipient(self):  # pragma: no cover
        return NotificationRecipientTypeOutput.make_one(
            self.boto3_raw_data["Recipient"]
        )

    Subject = field("Subject")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendNotificationActionDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendNotificationActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipantTimerConfiguration:
    boto3_raw_data: "type_defs.ParticipantTimerConfigurationTypeDef" = (
        dataclasses.field()
    )

    ParticipantRole = field("ParticipantRole")
    TimerType = field("TimerType")

    @cached_property
    def TimerValue(self):  # pragma: no cover
        return ParticipantTimerValue.make_one(self.boto3_raw_data["TimerValue"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ParticipantTimerConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipantTimerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredefinedAttribute:
    boto3_raw_data: "type_defs.PredefinedAttributeTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Values(self):  # pragma: no cover
        return PredefinedAttributeValuesOutput.make_one(self.boto3_raw_data["Values"])

    Purposes = field("Purposes")

    @cached_property
    def AttributeConfiguration(self):  # pragma: no cover
        return PredefinedAttributeConfiguration.make_one(
            self.boto3_raw_data["AttributeConfiguration"]
        )

    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredefinedAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredefinedAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickConnectConfig:
    boto3_raw_data: "type_defs.QuickConnectConfigTypeDef" = dataclasses.field()

    QuickConnectType = field("QuickConnectType")

    @cached_property
    def UserConfig(self):  # pragma: no cover
        return UserQuickConnectConfig.make_one(self.boto3_raw_data["UserConfig"])

    @cached_property
    def QueueConfig(self):  # pragma: no cover
        return QueueQuickConnectConfig.make_one(self.boto3_raw_data["QueueConfig"])

    @cached_property
    def PhoneConfig(self):  # pragma: no cover
        return PhoneNumberQuickConnectConfig.make_one(
            self.boto3_raw_data["PhoneConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickConnectConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickConnectConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisTranscriptItemRedaction:
    boto3_raw_data: (
        "type_defs.RealTimeContactAnalysisTranscriptItemRedactionTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CharacterOffsets(self):  # pragma: no cover
        return RealTimeContactAnalysisCharacterInterval.make_many(
            self.boto3_raw_data["CharacterOffsets"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisTranscriptItemRedactionTypeDef"
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
                "type_defs.RealTimeContactAnalysisTranscriptItemRedactionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisTranscriptItemWithCharacterOffsets:
    boto3_raw_data: (
        "type_defs.RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef"
    ) = dataclasses.field()

    Id = field("Id")

    @cached_property
    def CharacterOffsets(self):  # pragma: no cover
        return RealTimeContactAnalysisCharacterInterval.make_one(
            self.boto3_raw_data["CharacterOffsets"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef"
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
                "type_defs.RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisTranscriptItemWithContent:
    boto3_raw_data: (
        "type_defs.RealTimeContactAnalysisTranscriptItemWithContentTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    Content = field("Content")

    @cached_property
    def CharacterOffsets(self):  # pragma: no cover
        return RealTimeContactAnalysisCharacterInterval.make_one(
            self.boto3_raw_data["CharacterOffsets"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisTranscriptItemWithContentTypeDef"
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
                "type_defs.RealTimeContactAnalysisTranscriptItemWithContentTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisSegmentAttachments:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisSegmentAttachmentsTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ParticipantId = field("ParticipantId")
    ParticipantRole = field("ParticipantRole")

    @cached_property
    def Attachments(self):  # pragma: no cover
        return RealTimeContactAnalysisAttachment.make_many(
            self.boto3_raw_data["Attachments"]
        )

    @cached_property
    def Time(self):  # pragma: no cover
        return RealTimeContactAnalysisTimeData.make_one(self.boto3_raw_data["Time"])

    DisplayName = field("DisplayName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisSegmentAttachmentsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisSegmentAttachmentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisSegmentEvent:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisSegmentEventTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    EventType = field("EventType")

    @cached_property
    def Time(self):  # pragma: no cover
        return RealTimeContactAnalysisTimeData.make_one(self.boto3_raw_data["Time"])

    ParticipantId = field("ParticipantId")
    ParticipantRole = field("ParticipantRole")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisSegmentEventTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisSegmentEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceSummary:
    boto3_raw_data: "type_defs.ReferenceSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Url(self):  # pragma: no cover
        return UrlReference.make_one(self.boto3_raw_data["Url"])

    @cached_property
    def Attachment(self):  # pragma: no cover
        return AttachmentReference.make_one(self.boto3_raw_data["Attachment"])

    @cached_property
    def EmailMessage(self):  # pragma: no cover
        return EmailMessageReference.make_one(self.boto3_raw_data["EmailMessage"])

    @cached_property
    def String(self):  # pragma: no cover
        return StringReference.make_one(self.boto3_raw_data["String"])

    @cached_property
    def Number(self):  # pragma: no cover
        return NumberReference.make_one(self.boto3_raw_data["Number"])

    @cached_property
    def Date(self):  # pragma: no cover
        return DateReference.make_one(self.boto3_raw_data["Date"])

    @cached_property
    def Email(self):  # pragma: no cover
        return EmailReference.make_one(self.boto3_raw_data["Email"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfiguration:
    boto3_raw_data: "type_defs.ReplicationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationStatusSummaryList(self):  # pragma: no cover
        return ReplicationStatusSummary.make_many(
            self.boto3_raw_data["ReplicationStatusSummaryList"]
        )

    SourceRegion = field("SourceRegion")
    GlobalSignInEndpoint = field("GlobalSignInEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTagsSearchCriteria:
    boto3_raw_data: "type_defs.ResourceTagsSearchCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def TagSearchCondition(self):  # pragma: no cover
        return TagSearchCondition.make_one(self.boto3_raw_data["TagSearchCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceTagsSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTagsSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourceTagsResponse:
    boto3_raw_data: "type_defs.SearchResourceTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagSet.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourceTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourceTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSecurityProfilesResponse:
    boto3_raw_data: "type_defs.SearchSecurityProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecurityProfiles(self):  # pragma: no cover
        return SecurityProfileSearchSummary.make_many(
            self.boto3_raw_data["SecurityProfiles"]
        )

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchSecurityProfilesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSecurityProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVocabulariesResponse:
    boto3_raw_data: "type_defs.SearchVocabulariesResponseTypeDef" = dataclasses.field()

    @cached_property
    def VocabularySummaryList(self):  # pragma: no cover
        return VocabularySummary.make_many(self.boto3_raw_data["VocabularySummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchVocabulariesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVocabulariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchableContactAttributes:
    boto3_raw_data: "type_defs.SearchableContactAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Criteria(self):  # pragma: no cover
        return SearchableContactAttributesCriteria.make_many(
            self.boto3_raw_data["Criteria"]
        )

    MatchType = field("MatchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchableContactAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchableContactAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchableSegmentAttributes:
    boto3_raw_data: "type_defs.SearchableSegmentAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Criteria(self):  # pragma: no cover
        return SearchableSegmentAttributesCriteria.make_many(
            self.boto3_raw_data["Criteria"]
        )

    MatchType = field("MatchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchableSegmentAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchableSegmentAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignInConfigOutput:
    boto3_raw_data: "type_defs.SignInConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def Distributions(self):  # pragma: no cover
        return SignInDistribution.make_many(self.boto3_raw_data["Distributions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignInConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignInConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignInConfig:
    boto3_raw_data: "type_defs.SignInConfigTypeDef" = dataclasses.field()

    @cached_property
    def Distributions(self):  # pragma: no cover
        return SignInDistribution.make_many(self.boto3_raw_data["Distributions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignInConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignInConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAttachedFileUploadResponse:
    boto3_raw_data: "type_defs.StartAttachedFileUploadResponseTypeDef" = (
        dataclasses.field()
    )

    FileArn = field("FileArn")
    FileId = field("FileId")
    CreationTime = field("CreationTime")
    FileStatus = field("FileStatus")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return CreatedByInfo.make_one(self.boto3_raw_data["CreatedBy"])

    @cached_property
    def UploadUrlMetadata(self):  # pragma: no cover
        return UploadUrlMetadata.make_one(self.boto3_raw_data["UploadUrlMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAttachedFileUploadResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAttachedFileUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartContactRecordingRequest:
    boto3_raw_data: "type_defs.StartContactRecordingRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    InitialContactId = field("InitialContactId")

    @cached_property
    def VoiceRecordingConfiguration(self):  # pragma: no cover
        return VoiceRecordingConfiguration.make_one(
            self.boto3_raw_data["VoiceRecordingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartContactRecordingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartContactRecordingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplatedMessageConfig:
    boto3_raw_data: "type_defs.TemplatedMessageConfigTypeDef" = dataclasses.field()

    KnowledgeBaseId = field("KnowledgeBaseId")
    MessageTemplateId = field("MessageTemplateId")

    @cached_property
    def TemplateAttributes(self):  # pragma: no cover
        return TemplateAttributes.make_one(self.boto3_raw_data["TemplateAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplatedMessageConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplatedMessageConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transcript:
    boto3_raw_data: "type_defs.TranscriptTypeDef" = dataclasses.field()

    @cached_property
    def Criteria(self):  # pragma: no cover
        return TranscriptCriteria.make_many(self.boto3_raw_data["Criteria"])

    MatchType = field("MatchType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TranscriptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSearchSummary:
    boto3_raw_data: "type_defs.UserSearchSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    DirectoryUserId = field("DirectoryUserId")
    HierarchyGroupId = field("HierarchyGroupId")
    Id = field("Id")

    @cached_property
    def IdentityInfo(self):  # pragma: no cover
        return UserIdentityInfoLite.make_one(self.boto3_raw_data["IdentityInfo"])

    @cached_property
    def PhoneConfig(self):  # pragma: no cover
        return UserPhoneConfig.make_one(self.boto3_raw_data["PhoneConfig"])

    RoutingProfileId = field("RoutingProfileId")
    SecurityProfileIds = field("SecurityProfileIds")
    Tags = field("Tags")
    Username = field("Username")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSearchSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserSearchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class View:
    boto3_raw_data: "type_defs.ViewTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Status = field("Status")
    Type = field("Type")
    Description = field("Description")
    Version = field("Version")
    VersionDescription = field("VersionDescription")

    @cached_property
    def Content(self):  # pragma: no cover
        return ViewContent.make_one(self.boto3_raw_data["Content"])

    Tags = field("Tags")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    ViewContentSha256 = field("ViewContentSha256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesResponse:
    boto3_raw_data: "type_defs.ListRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def RuleSummaryList(self):  # pragma: no cover
        return RuleSummary.make_many(self.boto3_raw_data["RuleSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentInfo:
    boto3_raw_data: "type_defs.AgentInfoTypeDef" = dataclasses.field()

    Id = field("Id")
    ConnectedToAgentTimestamp = field("ConnectedToAgentTimestamp")
    AgentPauseDurationInSeconds = field("AgentPauseDurationInSeconds")

    @cached_property
    def HierarchyGroups(self):  # pragma: no cover
        return HierarchyGroups.make_one(self.boto3_raw_data["HierarchyGroups"])

    @cached_property
    def DeviceInfo(self):  # pragma: no cover
        return DeviceInfo.make_one(self.boto3_raw_data["DeviceInfo"])

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return ParticipantCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    AfterContactWorkDuration = field("AfterContactWorkDuration")
    AfterContactWorkStartTimestamp = field("AfterContactWorkStartTimestamp")
    AfterContactWorkEndTimestamp = field("AfterContactWorkEndTimestamp")
    AgentInitiatedHoldDuration = field("AgentInitiatedHoldDuration")

    @cached_property
    def StateTransitions(self):  # pragma: no cover
        return StateTransition.make_many(self.boto3_raw_data["StateTransitions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWebRTCContactRequest:
    boto3_raw_data: "type_defs.StartWebRTCContactRequestTypeDef" = dataclasses.field()

    ContactFlowId = field("ContactFlowId")
    InstanceId = field("InstanceId")

    @cached_property
    def ParticipantDetails(self):  # pragma: no cover
        return ParticipantDetails.make_one(self.boto3_raw_data["ParticipantDetails"])

    Attributes = field("Attributes")
    ClientToken = field("ClientToken")

    @cached_property
    def AllowedCapabilities(self):  # pragma: no cover
        return AllowedCapabilities.make_one(self.boto3_raw_data["AllowedCapabilities"])

    RelatedContactId = field("RelatedContactId")
    References = field("References")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartWebRTCContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWebRTCContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParticipantRequest:
    boto3_raw_data: "type_defs.CreateParticipantRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @cached_property
    def ParticipantDetails(self):  # pragma: no cover
        return ParticipantDetailsToAdd.make_one(
            self.boto3_raw_data["ParticipantDetails"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateParticipantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParticipantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QualityMetrics:
    boto3_raw_data: "type_defs.QualityMetricsTypeDef" = dataclasses.field()

    @cached_property
    def Agent(self):  # pragma: no cover
        return AgentQualityMetrics.make_one(self.boto3_raw_data["Agent"])

    @cached_property
    def Customer(self):  # pragma: no cover
        return CustomerQualityMetrics.make_one(self.boto3_raw_data["Customer"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QualityMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QualityMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPredefinedAttributesRequestPaginate:
    boto3_raw_data: "type_defs.SearchPredefinedAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return PredefinedAttributeSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPredefinedAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPredefinedAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPredefinedAttributesRequest:
    boto3_raw_data: "type_defs.SearchPredefinedAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return PredefinedAttributeSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPredefinedAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPredefinedAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeConditionOutput:
    boto3_raw_data: "type_defs.AttributeConditionOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    ProficiencyLevel = field("ProficiencyLevel")

    @cached_property
    def Range(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["Range"])

    @cached_property
    def MatchCriteria(self):  # pragma: no cover
        return MatchCriteriaOutput.make_one(self.boto3_raw_data["MatchCriteria"])

    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchCriteria:
    boto3_raw_data: "type_defs.MatchCriteriaTypeDef" = dataclasses.field()

    AgentsCriteria = field("AgentsCriteria")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityProfileRequest:
    boto3_raw_data: "type_defs.CreateSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileName = field("SecurityProfileName")
    InstanceId = field("InstanceId")
    Description = field("Description")
    Permissions = field("Permissions")
    Tags = field("Tags")
    AllowedAccessControlTags = field("AllowedAccessControlTags")
    TagRestrictedResources = field("TagRestrictedResources")
    Applications = field("Applications")
    HierarchyRestrictedResources = field("HierarchyRestrictedResources")
    AllowedAccessControlHierarchyGroupId = field("AllowedAccessControlHierarchyGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityProfileRequest:
    boto3_raw_data: "type_defs.UpdateSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    SecurityProfileId = field("SecurityProfileId")
    InstanceId = field("InstanceId")
    Description = field("Description")
    Permissions = field("Permissions")
    AllowedAccessControlTags = field("AllowedAccessControlTags")
    TagRestrictedResources = field("TagRestrictedResources")
    Applications = field("Applications")
    HierarchyRestrictedResources = field("HierarchyRestrictedResources")
    AllowedAccessControlHierarchyGroupId = field("AllowedAccessControlHierarchyGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsResponse:
    boto3_raw_data: "type_defs.ListBotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def LexBots(self):  # pragma: no cover
        return LexBotConfig.make_many(self.boto3_raw_data["LexBots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBotsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAttachedFileMetadataResponse:
    boto3_raw_data: "type_defs.BatchGetAttachedFileMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Files(self):  # pragma: no cover
        return AttachedFile.make_many(self.boto3_raw_data["Files"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return AttachedFileError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAttachedFileMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAttachedFileMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlPlaneUserAttributeFilter:
    boto3_raw_data: "type_defs.ControlPlaneUserAttributeFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrConditions(self):  # pragma: no cover
        return AttributeAndCondition.make_many(self.boto3_raw_data["OrConditions"])

    @cached_property
    def AndCondition(self):  # pragma: no cover
        return AttributeAndCondition.make_one(self.boto3_raw_data["AndCondition"])

    @cached_property
    def TagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["TagCondition"])

    @cached_property
    def HierarchyGroupCondition(self):  # pragma: no cover
        return HierarchyGroupCondition.make_one(
            self.boto3_raw_data["HierarchyGroupCondition"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ControlPlaneUserAttributeFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlPlaneUserAttributeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlPlaneAttributeFilter:
    boto3_raw_data: "type_defs.ControlPlaneAttributeFilterTypeDef" = dataclasses.field()

    @cached_property
    def OrConditions(self):  # pragma: no cover
        return CommonAttributeAndCondition.make_many(
            self.boto3_raw_data["OrConditions"]
        )

    @cached_property
    def AndCondition(self):  # pragma: no cover
        return CommonAttributeAndCondition.make_one(self.boto3_raw_data["AndCondition"])

    @cached_property
    def TagCondition(self):  # pragma: no cover
        return TagCondition.make_one(self.boto3_raw_data["TagCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlPlaneAttributeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlPlaneAttributeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowModuleSearchFilter:
    boto3_raw_data: "type_defs.ContactFlowModuleSearchFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContactFlowModuleSearchFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowModuleSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFlowSearchFilter:
    boto3_raw_data: "type_defs.ContactFlowSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactFlowSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactFlowSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmailAddressSearchFilter:
    boto3_raw_data: "type_defs.EmailAddressSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmailAddressSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmailAddressSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationSearchFilter:
    boto3_raw_data: "type_defs.HoursOfOperationSearchFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HoursOfOperationSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSearchFilter:
    boto3_raw_data: "type_defs.PromptSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueSearchFilter:
    boto3_raw_data: "type_defs.QueueSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueSearchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickConnectSearchFilter:
    boto3_raw_data: "type_defs.QuickConnectSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QuickConnectSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QuickConnectSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfileSearchFilter:
    boto3_raw_data: "type_defs.RoutingProfileSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingProfileSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfilesSearchFilter:
    boto3_raw_data: "type_defs.SecurityProfilesSearchFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityProfilesSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfilesSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Meeting:
    boto3_raw_data: "type_defs.MeetingTypeDef" = dataclasses.field()

    MediaRegion = field("MediaRegion")

    @cached_property
    def MediaPlacement(self):  # pragma: no cover
        return MediaPlacement.make_one(self.boto3_raw_data["MediaPlacement"])

    @cached_property
    def MeetingFeatures(self):  # pragma: no cover
        return MeetingFeaturesConfiguration.make_one(
            self.boto3_raw_data["MeetingFeatures"]
        )

    MeetingId = field("MeetingId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeetingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeetingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignSlaActionDefinitionOutput:
    boto3_raw_data: "type_defs.AssignSlaActionDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    SlaAssignmentType = field("SlaAssignmentType")

    @cached_property
    def CaseSlaConfiguration(self):  # pragma: no cover
        return CaseSlaConfigurationOutput.make_one(
            self.boto3_raw_data["CaseSlaConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssignSlaActionDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignSlaActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseActionDefinitionOutput:
    boto3_raw_data: "type_defs.CreateCaseActionDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fields(self):  # pragma: no cover
        return FieldValueOutput.make_many(self.boto3_raw_data["Fields"])

    TemplateId = field("TemplateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCaseActionDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCaseActionDefinitionOutput:
    boto3_raw_data: "type_defs.UpdateCaseActionDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fields(self):  # pragma: no cover
        return FieldValueOutput.make_many(self.boto3_raw_data["Fields"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCaseActionDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCaseActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePhoneNumberResponse:
    boto3_raw_data: "type_defs.DescribePhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def ClaimedPhoneNumberSummary(self):  # pragma: no cover
        return ClaimedPhoneNumberSummary.make_one(
            self.boto3_raw_data["ClaimedPhoneNumberSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCondition:
    boto3_raw_data: "type_defs.ListConditionTypeDef" = dataclasses.field()

    TargetListType = field("TargetListType")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Condition.make_many(self.boto3_raw_data["Conditions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutContactRequest:
    boto3_raw_data: "type_defs.BatchPutContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def ContactDataRequestList(self):  # pragma: no cover
        return ContactDataRequest.make_many(
            self.boto3_raw_data["ContactDataRequestList"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCurrentUserDataRequest:
    boto3_raw_data: "type_defs.GetCurrentUserDataRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return UserDataFilters.make_one(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCurrentUserDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCurrentUserDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactMetricsResponse:
    boto3_raw_data: "type_defs.GetContactMetricsResponseTypeDef" = dataclasses.field()

    @cached_property
    def MetricResults(self):  # pragma: no cover
        return ContactMetricResult.make_many(self.boto3_raw_data["MetricResults"])

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactsResponse:
    boto3_raw_data: "type_defs.SearchContactsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Contacts(self):  # pragma: no cover
        return ContactSearchSummary.make_many(self.boto3_raw_data["Contacts"])

    TotalCount = field("TotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContactsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueueResponse:
    boto3_raw_data: "type_defs.DescribeQueueResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queue(self):  # pragma: no cover
        return Queue.make_one(self.boto3_raw_data["Queue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQueuesResponse:
    boto3_raw_data: "type_defs.SearchQueuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queues(self):  # pragma: no cover
        return Queue.make_many(self.boto3_raw_data["Queues"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQueuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQueuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserResponse:
    boto3_raw_data: "type_defs.DescribeUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingProfile:
    boto3_raw_data: "type_defs.RoutingProfileTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    RoutingProfileArn = field("RoutingProfileArn")
    RoutingProfileId = field("RoutingProfileId")
    Description = field("Description")

    @cached_property
    def MediaConcurrencies(self):  # pragma: no cover
        return MediaConcurrency.make_many(self.boto3_raw_data["MediaConcurrencies"])

    DefaultOutboundQueueId = field("DefaultOutboundQueueId")
    Tags = field("Tags")
    NumberOfAssociatedQueues = field("NumberOfAssociatedQueues")
    NumberOfAssociatedUsers = field("NumberOfAssociatedUsers")
    AgentAvailabilityTimer = field("AgentAvailabilityTimer")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")
    IsDefault = field("IsDefault")
    AssociatedQueueIds = field("AssociatedQueueIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoutingProfileConcurrencyRequest:
    boto3_raw_data: "type_defs.UpdateRoutingProfileConcurrencyRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @cached_property
    def MediaConcurrencies(self):  # pragma: no cover
        return MediaConcurrency.make_many(self.boto3_raw_data["MediaConcurrencies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRoutingProfileConcurrencyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoutingProfileConcurrencyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CurrentMetricResult:
    boto3_raw_data: "type_defs.CurrentMetricResultTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimensions.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Collections(self):  # pragma: no cover
        return CurrentMetricData.make_many(self.boto3_raw_data["Collections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CurrentMetricResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrentMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateRoutingProfileQueuesRequest:
    boto3_raw_data: "type_defs.AssociateRoutingProfileQueuesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @cached_property
    def QueueConfigs(self):  # pragma: no cover
        return RoutingProfileQueueConfig.make_many(self.boto3_raw_data["QueueConfigs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateRoutingProfileQueuesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateRoutingProfileQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoutingProfileRequest:
    boto3_raw_data: "type_defs.CreateRoutingProfileRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    Description = field("Description")
    DefaultOutboundQueueId = field("DefaultOutboundQueueId")

    @cached_property
    def MediaConcurrencies(self):  # pragma: no cover
        return MediaConcurrency.make_many(self.boto3_raw_data["MediaConcurrencies"])

    @cached_property
    def QueueConfigs(self):  # pragma: no cover
        return RoutingProfileQueueConfig.make_many(self.boto3_raw_data["QueueConfigs"])

    Tags = field("Tags")
    AgentAvailabilityTimer = field("AgentAvailabilityTimer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoutingProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoutingProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoutingProfileQueuesRequest:
    boto3_raw_data: "type_defs.UpdateRoutingProfileQueuesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    RoutingProfileId = field("RoutingProfileId")

    @cached_property
    def QueueConfigs(self):  # pragma: no cover
        return RoutingProfileQueueConfig.make_many(self.boto3_raw_data["QueueConfigs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRoutingProfileQueuesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoutingProfileQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceStorageConfig:
    boto3_raw_data: "type_defs.InstanceStorageConfigTypeDef" = dataclasses.field()

    StorageType = field("StorageType")
    AssociationId = field("AssociationId")

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @cached_property
    def KinesisVideoStreamConfig(self):  # pragma: no cover
        return KinesisVideoStreamConfig.make_one(
            self.boto3_raw_data["KinesisVideoStreamConfig"]
        )

    @cached_property
    def KinesisStreamConfig(self):  # pragma: no cover
        return KinesisStreamConfig.make_one(self.boto3_raw_data["KinesisStreamConfig"])

    @cached_property
    def KinesisFirehoseConfig(self):  # pragma: no cover
        return KinesisFirehoseConfig.make_one(
            self.boto3_raw_data["KinesisFirehoseConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceStorageConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceStorageConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitContactEvaluationRequest:
    boto3_raw_data: "type_defs.SubmitContactEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationId = field("EvaluationId")
    Answers = field("Answers")
    Notes = field("Notes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubmitContactEvaluationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitContactEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactEvaluationRequest:
    boto3_raw_data: "type_defs.UpdateContactEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    EvaluationId = field("EvaluationId")
    Answers = field("Answers")
    Notes = field("Notes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContactEvaluationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormNumericQuestionPropertiesOutput:
    boto3_raw_data: "type_defs.EvaluationFormNumericQuestionPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    MinValue = field("MinValue")
    MaxValue = field("MaxValue")

    @cached_property
    def Options(self):  # pragma: no cover
        return EvaluationFormNumericQuestionOption.make_many(
            self.boto3_raw_data["Options"]
        )

    @cached_property
    def Automation(self):  # pragma: no cover
        return EvaluationFormNumericQuestionAutomation.make_one(
            self.boto3_raw_data["Automation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormNumericQuestionPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormNumericQuestionPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormNumericQuestionProperties:
    boto3_raw_data: "type_defs.EvaluationFormNumericQuestionPropertiesTypeDef" = (
        dataclasses.field()
    )

    MinValue = field("MinValue")
    MaxValue = field("MaxValue")

    @cached_property
    def Options(self):  # pragma: no cover
        return EvaluationFormNumericQuestionOption.make_many(
            self.boto3_raw_data["Options"]
        )

    @cached_property
    def Automation(self):  # pragma: no cover
        return EvaluationFormNumericQuestionAutomation.make_one(
            self.boto3_raw_data["Automation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormNumericQuestionPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormNumericQuestionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSingleSelectQuestionAutomationOutput:
    boto3_raw_data: (
        "type_defs.EvaluationFormSingleSelectQuestionAutomationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return EvaluationFormSingleSelectQuestionAutomationOption.make_many(
            self.boto3_raw_data["Options"]
        )

    DefaultOptionRefId = field("DefaultOptionRefId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormSingleSelectQuestionAutomationOutputTypeDef"
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
                "type_defs.EvaluationFormSingleSelectQuestionAutomationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSingleSelectQuestionAutomation:
    boto3_raw_data: "type_defs.EvaluationFormSingleSelectQuestionAutomationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Options(self):  # pragma: no cover
        return EvaluationFormSingleSelectQuestionAutomationOption.make_many(
            self.boto3_raw_data["Options"]
        )

    DefaultOptionRefId = field("DefaultOptionRefId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormSingleSelectQuestionAutomationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormSingleSelectQuestionAutomationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evaluation:
    boto3_raw_data: "type_defs.EvaluationTypeDef" = dataclasses.field()

    EvaluationId = field("EvaluationId")
    EvaluationArn = field("EvaluationArn")

    @cached_property
    def Metadata(self):  # pragma: no cover
        return EvaluationMetadata.make_one(self.boto3_raw_data["Metadata"])

    Answers = field("Answers")
    Notes = field("Notes")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")
    Scores = field("Scores")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactEvaluationsResponse:
    boto3_raw_data: "type_defs.ListContactEvaluationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EvaluationSummaryList(self):  # pragma: no cover
        return EvaluationSummary.make_many(self.boto3_raw_data["EvaluationSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactEvaluationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactEvaluationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseSlaConfiguration:
    boto3_raw_data: "type_defs.CaseSlaConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    TargetSlaMinutes = field("TargetSlaMinutes")
    FieldId = field("FieldId")
    TargetFieldValues = field("TargetFieldValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseSlaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseSlaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValue:
    boto3_raw_data: "type_defs.FieldValueTypeDef" = dataclasses.field()

    Id = field("Id")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserData:
    boto3_raw_data: "type_defs.UserDataTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return UserReference.make_one(self.boto3_raw_data["User"])

    @cached_property
    def RoutingProfile(self):  # pragma: no cover
        return RoutingProfileReference.make_one(self.boto3_raw_data["RoutingProfile"])

    @cached_property
    def HierarchyPath(self):  # pragma: no cover
        return HierarchyPathReference.make_one(self.boto3_raw_data["HierarchyPath"])

    @cached_property
    def Status(self):  # pragma: no cover
        return AgentStatusReference.make_one(self.boto3_raw_data["Status"])

    AvailableSlotsByChannel = field("AvailableSlotsByChannel")
    MaxSlotsByChannel = field("MaxSlotsByChannel")
    ActiveSlotsByChannel = field("ActiveSlotsByChannel")

    @cached_property
    def Contacts(self):  # pragma: no cover
        return AgentContactReference.make_many(self.boto3_raw_data["Contacts"])

    NextStatus = field("NextStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchyGroup:
    boto3_raw_data: "type_defs.HierarchyGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    LevelId = field("LevelId")

    @cached_property
    def HierarchyPath(self):  # pragma: no cover
        return HierarchyPath.make_one(self.boto3_raw_data["HierarchyPath"])

    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HierarchyGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HierarchyGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserHierarchyStructureResponse:
    boto3_raw_data: "type_defs.DescribeUserHierarchyStructureResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HierarchyStructure(self):  # pragma: no cover
        return HierarchyStructure.make_one(self.boto3_raw_data["HierarchyStructure"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserHierarchyStructureResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserHierarchyStructureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserHierarchyStructureRequest:
    boto3_raw_data: "type_defs.UpdateUserHierarchyStructureRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HierarchyStructure(self):  # pragma: no cover
        return HierarchyStructureUpdate.make_one(
            self.boto3_raw_data["HierarchyStructure"]
        )

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateUserHierarchyStructureRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserHierarchyStructureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataRequestPaginate:
    boto3_raw_data: "type_defs.GetMetricDataRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def HistoricalMetrics(self):  # pragma: no cover
        return HistoricalMetric.make_many(self.boto3_raw_data["HistoricalMetrics"])

    Groupings = field("Groupings")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataRequest:
    boto3_raw_data: "type_defs.GetMetricDataRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def HistoricalMetrics(self):  # pragma: no cover
        return HistoricalMetric.make_many(self.boto3_raw_data["HistoricalMetrics"])

    Groupings = field("Groupings")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoricalMetricData:
    boto3_raw_data: "type_defs.HistoricalMetricDataTypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return HistoricalMetric.make_one(self.boto3_raw_data["Metric"])

    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HistoricalMetricDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalMetricDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHoursOfOperationRequest:
    boto3_raw_data: "type_defs.CreateHoursOfOperationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Name = field("Name")
    TimeZone = field("TimeZone")

    @cached_property
    def Config(self):  # pragma: no cover
        return HoursOfOperationConfig.make_many(self.boto3_raw_data["Config"])

    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateHoursOfOperationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHoursOfOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperation:
    boto3_raw_data: "type_defs.HoursOfOperationTypeDef" = dataclasses.field()

    HoursOfOperationId = field("HoursOfOperationId")
    HoursOfOperationArn = field("HoursOfOperationArn")
    Name = field("Name")
    Description = field("Description")
    TimeZone = field("TimeZone")

    @cached_property
    def Config(self):  # pragma: no cover
        return HoursOfOperationConfig.make_many(self.boto3_raw_data["Config"])

    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HoursOfOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHoursOfOperationRequest:
    boto3_raw_data: "type_defs.UpdateHoursOfOperationRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    Name = field("Name")
    Description = field("Description")
    TimeZone = field("TimeZone")

    @cached_property
    def Config(self):  # pragma: no cover
        return HoursOfOperationConfig.make_many(self.boto3_raw_data["Config"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateHoursOfOperationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHoursOfOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHoursOfOperationOverrideRequest:
    boto3_raw_data: "type_defs.CreateHoursOfOperationOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    Name = field("Name")

    @cached_property
    def Config(self):  # pragma: no cover
        return HoursOfOperationOverrideConfig.make_many(self.boto3_raw_data["Config"])

    EffectiveFrom = field("EffectiveFrom")
    EffectiveTill = field("EffectiveTill")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateHoursOfOperationOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHoursOfOperationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoursOfOperationOverride:
    boto3_raw_data: "type_defs.HoursOfOperationOverrideTypeDef" = dataclasses.field()

    HoursOfOperationOverrideId = field("HoursOfOperationOverrideId")
    HoursOfOperationId = field("HoursOfOperationId")
    HoursOfOperationArn = field("HoursOfOperationArn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Config(self):  # pragma: no cover
        return HoursOfOperationOverrideConfig.make_many(self.boto3_raw_data["Config"])

    EffectiveFrom = field("EffectiveFrom")
    EffectiveTill = field("EffectiveTill")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HoursOfOperationOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoursOfOperationOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHoursOfOperationOverrideRequest:
    boto3_raw_data: "type_defs.UpdateHoursOfOperationOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    HoursOfOperationId = field("HoursOfOperationId")
    HoursOfOperationOverrideId = field("HoursOfOperationOverrideId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Config(self):  # pragma: no cover
        return HoursOfOperationOverrideConfig.make_many(self.boto3_raw_data["Config"])

    EffectiveFrom = field("EffectiveFrom")
    EffectiveTill = field("EffectiveTill")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateHoursOfOperationOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHoursOfOperationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectiveHoursOfOperations:
    boto3_raw_data: "type_defs.EffectiveHoursOfOperationsTypeDef" = dataclasses.field()

    Date = field("Date")

    @cached_property
    def OperationalHours(self):  # pragma: no cover
        return OperationalHour.make_many(self.boto3_raw_data["OperationalHours"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EffectiveHoursOfOperationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectiveHoursOfOperationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateConstraintsOutput:
    boto3_raw_data: "type_defs.TaskTemplateConstraintsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RequiredFields(self):  # pragma: no cover
        return RequiredFieldInfo.make_many(self.boto3_raw_data["RequiredFields"])

    @cached_property
    def ReadOnlyFields(self):  # pragma: no cover
        return ReadOnlyFieldInfo.make_many(self.boto3_raw_data["ReadOnlyFields"])

    @cached_property
    def InvisibleFields(self):  # pragma: no cover
        return InvisibleFieldInfo.make_many(self.boto3_raw_data["InvisibleFields"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskTemplateConstraintsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateConstraintsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateConstraints:
    boto3_raw_data: "type_defs.TaskTemplateConstraintsTypeDef" = dataclasses.field()

    @cached_property
    def RequiredFields(self):  # pragma: no cover
        return RequiredFieldInfo.make_many(self.boto3_raw_data["RequiredFields"])

    @cached_property
    def ReadOnlyFields(self):  # pragma: no cover
        return ReadOnlyFieldInfo.make_many(self.boto3_raw_data["ReadOnlyFields"])

    @cached_property
    def InvisibleFields(self):  # pragma: no cover
        return InvisibleFieldInfo.make_many(self.boto3_raw_data["InvisibleFields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateDefaultsOutput:
    boto3_raw_data: "type_defs.TaskTemplateDefaultsOutputTypeDef" = dataclasses.field()

    @cached_property
    def DefaultFieldValues(self):  # pragma: no cover
        return TaskTemplateDefaultFieldValue.make_many(
            self.boto3_raw_data["DefaultFieldValues"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateDefaultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateDefaultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskTemplateDefaults:
    boto3_raw_data: "type_defs.TaskTemplateDefaultsTypeDef" = dataclasses.field()

    @cached_property
    def DefaultFieldValues(self):  # pragma: no cover
        return TaskTemplateDefaultFieldValue.make_many(
            self.boto3_raw_data["DefaultFieldValues"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskTemplateDefaultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskTemplateDefaultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricV2:
    boto3_raw_data: "type_defs.MetricV2TypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Threshold(self):  # pragma: no cover
        return ThresholdV2.make_many(self.boto3_raw_data["Threshold"])

    MetricFilters = field("MetricFilters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricV2TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDataV2:
    boto3_raw_data: "type_defs.MetricDataV2TypeDef" = dataclasses.field()

    @cached_property
    def Metric(self):  # pragma: no cover
        return MetricV2Output.make_one(self.boto3_raw_data["Metric"])

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDataV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDataV2TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendChatIntegrationEventRequest:
    boto3_raw_data: "type_defs.SendChatIntegrationEventRequestTypeDef" = (
        dataclasses.field()
    )

    SourceId = field("SourceId")
    DestinationId = field("DestinationId")

    @cached_property
    def Event(self):  # pragma: no cover
        return ChatEvent.make_one(self.boto3_raw_data["Event"])

    Subtype = field("Subtype")

    @cached_property
    def NewSessionDetails(self):  # pragma: no cover
        return NewSessionDetails.make_one(self.boto3_raw_data["NewSessionDetails"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendChatIntegrationEventRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendChatIntegrationEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendNotificationActionDefinition:
    boto3_raw_data: "type_defs.SendNotificationActionDefinitionTypeDef" = (
        dataclasses.field()
    )

    DeliveryMethod = field("DeliveryMethod")
    Content = field("Content")
    ContentType = field("ContentType")
    Recipient = field("Recipient")
    Subject = field("Subject")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendNotificationActionDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendNotificationActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatParticipantRoleConfig:
    boto3_raw_data: "type_defs.ChatParticipantRoleConfigTypeDef" = dataclasses.field()

    @cached_property
    def ParticipantTimerConfigList(self):  # pragma: no cover
        return ParticipantTimerConfiguration.make_many(
            self.boto3_raw_data["ParticipantTimerConfigList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChatParticipantRoleConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatParticipantRoleConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePredefinedAttributeResponse:
    boto3_raw_data: "type_defs.DescribePredefinedAttributeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PredefinedAttribute(self):  # pragma: no cover
        return PredefinedAttribute.make_one(self.boto3_raw_data["PredefinedAttribute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePredefinedAttributeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePredefinedAttributeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPredefinedAttributesResponse:
    boto3_raw_data: "type_defs.SearchPredefinedAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PredefinedAttributes(self):  # pragma: no cover
        return PredefinedAttribute.make_many(
            self.boto3_raw_data["PredefinedAttributes"]
        )

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchPredefinedAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPredefinedAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePredefinedAttributeRequest:
    boto3_raw_data: "type_defs.CreatePredefinedAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Name = field("Name")
    Values = field("Values")
    Purposes = field("Purposes")

    @cached_property
    def AttributeConfiguration(self):  # pragma: no cover
        return InputPredefinedAttributeConfiguration.make_one(
            self.boto3_raw_data["AttributeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePredefinedAttributeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePredefinedAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePredefinedAttributeRequest:
    boto3_raw_data: "type_defs.UpdatePredefinedAttributeRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    Name = field("Name")
    Values = field("Values")
    Purposes = field("Purposes")

    @cached_property
    def AttributeConfiguration(self):  # pragma: no cover
        return InputPredefinedAttributeConfiguration.make_one(
            self.boto3_raw_data["AttributeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePredefinedAttributeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePredefinedAttributeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQuickConnectRequest:
    boto3_raw_data: "type_defs.CreateQuickConnectRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")

    @cached_property
    def QuickConnectConfig(self):  # pragma: no cover
        return QuickConnectConfig.make_one(self.boto3_raw_data["QuickConnectConfig"])

    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateQuickConnectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQuickConnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuickConnect:
    boto3_raw_data: "type_defs.QuickConnectTypeDef" = dataclasses.field()

    QuickConnectARN = field("QuickConnectARN")
    QuickConnectId = field("QuickConnectId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def QuickConnectConfig(self):  # pragma: no cover
        return QuickConnectConfig.make_one(self.boto3_raw_data["QuickConnectConfig"])

    Tags = field("Tags")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedRegion = field("LastModifiedRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuickConnectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QuickConnectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQuickConnectConfigRequest:
    boto3_raw_data: "type_defs.UpdateQuickConnectConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    QuickConnectId = field("QuickConnectId")

    @cached_property
    def QuickConnectConfig(self):  # pragma: no cover
        return QuickConnectConfig.make_one(self.boto3_raw_data["QuickConnectConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQuickConnectConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQuickConnectConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisSegmentTranscript:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisSegmentTranscriptTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ParticipantId = field("ParticipantId")
    ParticipantRole = field("ParticipantRole")
    Content = field("Content")

    @cached_property
    def Time(self):  # pragma: no cover
        return RealTimeContactAnalysisTimeData.make_one(self.boto3_raw_data["Time"])

    DisplayName = field("DisplayName")
    ContentType = field("ContentType")

    @cached_property
    def Redaction(self):  # pragma: no cover
        return RealTimeContactAnalysisTranscriptItemRedaction.make_one(
            self.boto3_raw_data["Redaction"]
        )

    Sentiment = field("Sentiment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisSegmentTranscriptTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisSegmentTranscriptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisPointOfInterest:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisPointOfInterestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TranscriptItems(self):  # pragma: no cover
        return RealTimeContactAnalysisTranscriptItemWithCharacterOffsets.make_many(
            self.boto3_raw_data["TranscriptItems"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisPointOfInterestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisPointOfInterestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisIssueDetected:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisIssueDetectedTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TranscriptItems(self):  # pragma: no cover
        return RealTimeContactAnalysisTranscriptItemWithContent.make_many(
            self.boto3_raw_data["TranscriptItems"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisIssueDetectedTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisIssueDetectedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactReferencesResponse:
    boto3_raw_data: "type_defs.ListContactReferencesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReferenceSummaryList(self):  # pragma: no cover
        return ReferenceSummary.make_many(self.boto3_raw_data["ReferenceSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContactReferencesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactReferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceResponse:
    boto3_raw_data: "type_defs.DescribeInstanceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Instance(self):  # pragma: no cover
        return Instance.make_one(self.boto3_raw_data["Instance"])

    @cached_property
    def ReplicationConfiguration(self):  # pragma: no cover
        return ReplicationConfiguration.make_one(
            self.boto3_raw_data["ReplicationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourceTagsRequestPaginate:
    boto3_raw_data: "type_defs.SearchResourceTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ResourceTypes = field("ResourceTypes")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return ResourceTagsSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchResourceTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourceTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourceTagsRequest:
    boto3_raw_data: "type_defs.SearchResourceTagsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ResourceTypes = field("ResourceTypes")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return ResourceTagsSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourceTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourceTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactRequest:
    boto3_raw_data: "type_defs.CreateContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Channel = field("Channel")
    InitiationMethod = field("InitiationMethod")
    ClientToken = field("ClientToken")
    RelatedContactId = field("RelatedContactId")
    Attributes = field("Attributes")
    References = field("References")
    ExpiryDurationInMinutes = field("ExpiryDurationInMinutes")

    @cached_property
    def UserInfo(self):  # pragma: no cover
        return UserInfo.make_one(self.boto3_raw_data["UserInfo"])

    InitiateAs = field("InitiateAs")
    Name = field("Name")
    Description = field("Description")
    SegmentAttributes = field("SegmentAttributes")
    PreviousContactId = field("PreviousContactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChatContactRequest:
    boto3_raw_data: "type_defs.StartChatContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactFlowId = field("ContactFlowId")

    @cached_property
    def ParticipantDetails(self):  # pragma: no cover
        return ParticipantDetails.make_one(self.boto3_raw_data["ParticipantDetails"])

    Attributes = field("Attributes")

    @cached_property
    def InitialMessage(self):  # pragma: no cover
        return ChatMessage.make_one(self.boto3_raw_data["InitialMessage"])

    ClientToken = field("ClientToken")
    ChatDurationInMinutes = field("ChatDurationInMinutes")
    SupportedMessagingContentTypes = field("SupportedMessagingContentTypes")

    @cached_property
    def PersistentChat(self):  # pragma: no cover
        return PersistentChat.make_one(self.boto3_raw_data["PersistentChat"])

    RelatedContactId = field("RelatedContactId")
    SegmentAttributes = field("SegmentAttributes")
    CustomerId = field("CustomerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChatContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChatContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEmailContactRequest:
    boto3_raw_data: "type_defs.StartEmailContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def FromEmailAddress(self):  # pragma: no cover
        return EmailAddressInfo.make_one(self.boto3_raw_data["FromEmailAddress"])

    DestinationEmailAddress = field("DestinationEmailAddress")

    @cached_property
    def EmailMessage(self):  # pragma: no cover
        return InboundEmailContent.make_one(self.boto3_raw_data["EmailMessage"])

    Description = field("Description")
    References = field("References")
    Name = field("Name")

    @cached_property
    def AdditionalRecipients(self):  # pragma: no cover
        return InboundAdditionalRecipients.make_one(
            self.boto3_raw_data["AdditionalRecipients"]
        )

    @cached_property
    def Attachments(self):  # pragma: no cover
        return EmailAttachment.make_many(self.boto3_raw_data["Attachments"])

    ContactFlowId = field("ContactFlowId")
    RelatedContactId = field("RelatedContactId")
    Attributes = field("Attributes")
    SegmentAttributes = field("SegmentAttributes")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartEmailContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEmailContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOutboundChatContactRequest:
    boto3_raw_data: "type_defs.StartOutboundChatContactRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["SourceEndpoint"])

    @cached_property
    def DestinationEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["DestinationEndpoint"])

    InstanceId = field("InstanceId")
    SegmentAttributes = field("SegmentAttributes")
    ContactFlowId = field("ContactFlowId")
    Attributes = field("Attributes")
    ChatDurationInMinutes = field("ChatDurationInMinutes")

    @cached_property
    def ParticipantDetails(self):  # pragma: no cover
        return ParticipantDetails.make_one(self.boto3_raw_data["ParticipantDetails"])

    @cached_property
    def InitialSystemMessage(self):  # pragma: no cover
        return ChatMessage.make_one(self.boto3_raw_data["InitialSystemMessage"])

    RelatedContactId = field("RelatedContactId")
    SupportedMessagingContentTypes = field("SupportedMessagingContentTypes")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartOutboundChatContactRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOutboundChatContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTaskContactRequest:
    boto3_raw_data: "type_defs.StartTaskContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    PreviousContactId = field("PreviousContactId")
    ContactFlowId = field("ContactFlowId")
    Attributes = field("Attributes")
    References = field("References")
    Description = field("Description")
    ClientToken = field("ClientToken")
    ScheduledTime = field("ScheduledTime")
    TaskTemplateId = field("TaskTemplateId")
    QuickConnectId = field("QuickConnectId")
    RelatedContactId = field("RelatedContactId")
    SegmentAttributes = field("SegmentAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTaskContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTaskContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactRequest:
    boto3_raw_data: "type_defs.UpdateContactRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    Name = field("Name")
    Description = field("Description")
    References = field("References")
    SegmentAttributes = field("SegmentAttributes")

    @cached_property
    def QueueInfo(self):  # pragma: no cover
        return QueueInfoInput.make_one(self.boto3_raw_data["QueueInfo"])

    @cached_property
    def UserInfo(self):  # pragma: no cover
        return UserInfo.make_one(self.boto3_raw_data["UserInfo"])

    @cached_property
    def CustomerEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["CustomerEndpoint"])

    @cached_property
    def SystemEndpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["SystemEndpoint"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficDistributionResponse:
    boto3_raw_data: "type_defs.GetTrafficDistributionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TelephonyConfig(self):  # pragma: no cover
        return TelephonyConfigOutput.make_one(self.boto3_raw_data["TelephonyConfig"])

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def SignInConfig(self):  # pragma: no cover
        return SignInConfigOutput.make_one(self.boto3_raw_data["SignInConfig"])

    @cached_property
    def AgentConfig(self):  # pragma: no cover
        return AgentConfigOutput.make_one(self.boto3_raw_data["AgentConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTrafficDistributionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficDistributionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundEmailContent:
    boto3_raw_data: "type_defs.OutboundEmailContentTypeDef" = dataclasses.field()

    MessageSourceType = field("MessageSourceType")

    @cached_property
    def TemplatedMessageConfig(self):  # pragma: no cover
        return TemplatedMessageConfig.make_one(
            self.boto3_raw_data["TemplatedMessageConfig"]
        )

    @cached_property
    def RawMessage(self):  # pragma: no cover
        return OutboundRawMessage.make_one(self.boto3_raw_data["RawMessage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundEmailContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundEmailContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactAnalysis:
    boto3_raw_data: "type_defs.ContactAnalysisTypeDef" = dataclasses.field()

    @cached_property
    def Transcript(self):  # pragma: no cover
        return Transcript.make_one(self.boto3_raw_data["Transcript"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactAnalysisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactAnalysisTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersResponse:
    boto3_raw_data: "type_defs.SearchUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return UserSearchSummary.make_many(self.boto3_raw_data["Users"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateViewResponse:
    boto3_raw_data: "type_defs.CreateViewResponseTypeDef" = dataclasses.field()

    @cached_property
    def View(self):  # pragma: no cover
        return View.make_one(self.boto3_raw_data["View"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateViewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateViewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateViewVersionResponse:
    boto3_raw_data: "type_defs.CreateViewVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def View(self):  # pragma: no cover
        return View.make_one(self.boto3_raw_data["View"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateViewVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateViewVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeViewResponse:
    boto3_raw_data: "type_defs.DescribeViewResponseTypeDef" = dataclasses.field()

    @cached_property
    def View(self):  # pragma: no cover
        return View.make_one(self.boto3_raw_data["View"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeViewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeViewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateViewContentResponse:
    boto3_raw_data: "type_defs.UpdateViewContentResponseTypeDef" = dataclasses.field()

    @cached_property
    def View(self):  # pragma: no cover
        return View.make_one(self.boto3_raw_data["View"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateViewContentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateViewContentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionOutput:
    boto3_raw_data: "type_defs.ExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def AttributeCondition(self):  # pragma: no cover
        return AttributeConditionOutput.make_one(
            self.boto3_raw_data["AttributeCondition"]
        )

    AndExpression = field("AndExpression")
    OrExpression = field("OrExpression")

    @cached_property
    def NotAttributeCondition(self):  # pragma: no cover
        return AttributeConditionOutput.make_one(
            self.boto3_raw_data["NotAttributeCondition"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSearchFilter:
    boto3_raw_data: "type_defs.UserSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def TagFilter(self):  # pragma: no cover
        return ControlPlaneTagFilter.make_one(self.boto3_raw_data["TagFilter"])

    @cached_property
    def UserAttributeFilter(self):  # pragma: no cover
        return ControlPlaneUserAttributeFilter.make_one(
            self.boto3_raw_data["UserAttributeFilter"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSearchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentStatusSearchFilter:
    boto3_raw_data: "type_defs.AgentStatusSearchFilterTypeDef" = dataclasses.field()

    @cached_property
    def AttributeFilter(self):  # pragma: no cover
        return ControlPlaneAttributeFilter.make_one(
            self.boto3_raw_data["AttributeFilter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentStatusSearchFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentStatusSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserHierarchyGroupSearchFilter:
    boto3_raw_data: "type_defs.UserHierarchyGroupSearchFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AttributeFilter(self):  # pragma: no cover
        return ControlPlaneAttributeFilter.make_one(
            self.boto3_raw_data["AttributeFilter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserHierarchyGroupSearchFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserHierarchyGroupSearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactFlowModulesRequestPaginate:
    boto3_raw_data: "type_defs.SearchContactFlowModulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return ContactFlowModuleSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return ContactFlowModuleSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchContactFlowModulesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactFlowModulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactFlowModulesRequest:
    boto3_raw_data: "type_defs.SearchContactFlowModulesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return ContactFlowModuleSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return ContactFlowModuleSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchContactFlowModulesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactFlowModulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactFlowsRequestPaginate:
    boto3_raw_data: "type_defs.SearchContactFlowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return ContactFlowSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return ContactFlowSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchContactFlowsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactFlowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactFlowsRequest:
    boto3_raw_data: "type_defs.SearchContactFlowsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return ContactFlowSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return ContactFlowSearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContactFlowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactFlowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchEmailAddressesRequest:
    boto3_raw_data: "type_defs.SearchEmailAddressesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return EmailAddressSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return EmailAddressSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchEmailAddressesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchEmailAddressesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchHoursOfOperationOverridesRequestPaginate:
    boto3_raw_data: (
        "type_defs.SearchHoursOfOperationOverridesRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return HoursOfOperationSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return HoursOfOperationOverrideSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchHoursOfOperationOverridesRequestPaginateTypeDef"
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
                "type_defs.SearchHoursOfOperationOverridesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchHoursOfOperationOverridesRequest:
    boto3_raw_data: "type_defs.SearchHoursOfOperationOverridesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return HoursOfOperationSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return HoursOfOperationOverrideSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchHoursOfOperationOverridesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchHoursOfOperationOverridesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchHoursOfOperationsRequestPaginate:
    boto3_raw_data: "type_defs.SearchHoursOfOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return HoursOfOperationSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return HoursOfOperationSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchHoursOfOperationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchHoursOfOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchHoursOfOperationsRequest:
    boto3_raw_data: "type_defs.SearchHoursOfOperationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return HoursOfOperationSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return HoursOfOperationSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchHoursOfOperationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchHoursOfOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPromptsRequestPaginate:
    boto3_raw_data: "type_defs.SearchPromptsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return PromptSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return PromptSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchPromptsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPromptsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchPromptsRequest:
    boto3_raw_data: "type_defs.SearchPromptsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return PromptSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return PromptSearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchPromptsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchPromptsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQueuesRequestPaginate:
    boto3_raw_data: "type_defs.SearchQueuesRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return QueueSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return QueueSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQueuesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQueuesRequest:
    boto3_raw_data: "type_defs.SearchQueuesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return QueueSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return QueueSearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQueuesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuickConnectsRequestPaginate:
    boto3_raw_data: "type_defs.SearchQuickConnectsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return QuickConnectSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return QuickConnectSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchQuickConnectsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuickConnectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuickConnectsRequest:
    boto3_raw_data: "type_defs.SearchQuickConnectsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return QuickConnectSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return QuickConnectSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuickConnectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuickConnectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRoutingProfilesRequestPaginate:
    boto3_raw_data: "type_defs.SearchRoutingProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return RoutingProfileSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return RoutingProfileSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchRoutingProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRoutingProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRoutingProfilesRequest:
    boto3_raw_data: "type_defs.SearchRoutingProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return RoutingProfileSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return RoutingProfileSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchRoutingProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRoutingProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSecurityProfilesRequestPaginate:
    boto3_raw_data: "type_defs.SearchSecurityProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return SecurityProfileSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return SecurityProfilesSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchSecurityProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSecurityProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSecurityProfilesRequest:
    boto3_raw_data: "type_defs.SearchSecurityProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return SecurityProfileSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return SecurityProfilesSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchSecurityProfilesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSecurityProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionData:
    boto3_raw_data: "type_defs.ConnectionDataTypeDef" = dataclasses.field()

    @cached_property
    def Attendee(self):  # pragma: no cover
        return Attendee.make_one(self.boto3_raw_data["Attendee"])

    @cached_property
    def Meeting(self):  # pragma: no cover
        return Meeting.make_one(self.boto3_raw_data["Meeting"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleActionOutput:
    boto3_raw_data: "type_defs.RuleActionOutputTypeDef" = dataclasses.field()

    ActionType = field("ActionType")

    @cached_property
    def TaskAction(self):  # pragma: no cover
        return TaskActionDefinitionOutput.make_one(self.boto3_raw_data["TaskAction"])

    @cached_property
    def EventBridgeAction(self):  # pragma: no cover
        return EventBridgeActionDefinition.make_one(
            self.boto3_raw_data["EventBridgeAction"]
        )

    AssignContactCategoryAction = field("AssignContactCategoryAction")

    @cached_property
    def SendNotificationAction(self):  # pragma: no cover
        return SendNotificationActionDefinitionOutput.make_one(
            self.boto3_raw_data["SendNotificationAction"]
        )

    @cached_property
    def CreateCaseAction(self):  # pragma: no cover
        return CreateCaseActionDefinitionOutput.make_one(
            self.boto3_raw_data["CreateCaseAction"]
        )

    @cached_property
    def UpdateCaseAction(self):  # pragma: no cover
        return UpdateCaseActionDefinitionOutput.make_one(
            self.boto3_raw_data["UpdateCaseAction"]
        )

    @cached_property
    def AssignSlaAction(self):  # pragma: no cover
        return AssignSlaActionDefinitionOutput.make_one(
            self.boto3_raw_data["AssignSlaAction"]
        )

    EndAssociatedTasksAction = field("EndAssociatedTasksAction")

    @cached_property
    def SubmitAutoEvaluationAction(self):  # pragma: no cover
        return SubmitAutoEvaluationActionDefinition.make_one(
            self.boto3_raw_data["SubmitAutoEvaluationAction"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSearchCriteriaPaginator:
    boto3_raw_data: "type_defs.UserSearchCriteriaPaginatorTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @cached_property
    def ListCondition(self):  # pragma: no cover
        return ListCondition.make_one(self.boto3_raw_data["ListCondition"])

    @cached_property
    def HierarchyGroupCondition(self):  # pragma: no cover
        return HierarchyGroupCondition.make_one(
            self.boto3_raw_data["HierarchyGroupCondition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserSearchCriteriaPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserSearchCriteriaPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSearchCriteria:
    boto3_raw_data: "type_defs.UserSearchCriteriaTypeDef" = dataclasses.field()

    OrConditions = field("OrConditions")
    AndConditions = field("AndConditions")

    @cached_property
    def StringCondition(self):  # pragma: no cover
        return StringCondition.make_one(self.boto3_raw_data["StringCondition"])

    @cached_property
    def ListCondition(self):  # pragma: no cover
        return ListCondition.make_one(self.boto3_raw_data["ListCondition"])

    @cached_property
    def HierarchyGroupCondition(self):  # pragma: no cover
        return HierarchyGroupCondition.make_one(
            self.boto3_raw_data["HierarchyGroupCondition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserSearchCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserSearchCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRoutingProfileResponse:
    boto3_raw_data: "type_defs.DescribeRoutingProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RoutingProfile(self):  # pragma: no cover
        return RoutingProfile.make_one(self.boto3_raw_data["RoutingProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRoutingProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRoutingProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRoutingProfilesResponse:
    boto3_raw_data: "type_defs.SearchRoutingProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RoutingProfiles(self):  # pragma: no cover
        return RoutingProfile.make_many(self.boto3_raw_data["RoutingProfiles"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchRoutingProfilesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRoutingProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCurrentMetricDataResponse:
    boto3_raw_data: "type_defs.GetCurrentMetricDataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricResults(self):  # pragma: no cover
        return CurrentMetricResult.make_many(self.boto3_raw_data["MetricResults"])

    DataSnapshotTime = field("DataSnapshotTime")
    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCurrentMetricDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCurrentMetricDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateInstanceStorageConfigRequest:
    boto3_raw_data: "type_defs.AssociateInstanceStorageConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ResourceType = field("ResourceType")

    @cached_property
    def StorageConfig(self):  # pragma: no cover
        return InstanceStorageConfig.make_one(self.boto3_raw_data["StorageConfig"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateInstanceStorageConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateInstanceStorageConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceStorageConfigResponse:
    boto3_raw_data: "type_defs.DescribeInstanceStorageConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageConfig(self):  # pragma: no cover
        return InstanceStorageConfig.make_one(self.boto3_raw_data["StorageConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceStorageConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceStorageConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceStorageConfigsResponse:
    boto3_raw_data: "type_defs.ListInstanceStorageConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageConfigs(self):  # pragma: no cover
        return InstanceStorageConfig.make_many(self.boto3_raw_data["StorageConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceStorageConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceStorageConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceStorageConfigRequest:
    boto3_raw_data: "type_defs.UpdateInstanceStorageConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")
    ResourceType = field("ResourceType")

    @cached_property
    def StorageConfig(self):  # pragma: no cover
        return InstanceStorageConfig.make_one(self.boto3_raw_data["StorageConfig"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateInstanceStorageConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceStorageConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSingleSelectQuestionPropertiesOutput:
    boto3_raw_data: (
        "type_defs.EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return EvaluationFormSingleSelectQuestionOption.make_many(
            self.boto3_raw_data["Options"]
        )

    DisplayAs = field("DisplayAs")

    @cached_property
    def Automation(self):  # pragma: no cover
        return EvaluationFormSingleSelectQuestionAutomationOutput.make_one(
            self.boto3_raw_data["Automation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef"
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
                "type_defs.EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCurrentUserDataResponse:
    boto3_raw_data: "type_defs.GetCurrentUserDataResponseTypeDef" = dataclasses.field()

    @cached_property
    def UserDataList(self):  # pragma: no cover
        return UserData.make_many(self.boto3_raw_data["UserDataList"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCurrentUserDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCurrentUserDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserHierarchyGroupResponse:
    boto3_raw_data: "type_defs.DescribeUserHierarchyGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HierarchyGroup(self):  # pragma: no cover
        return HierarchyGroup.make_one(self.boto3_raw_data["HierarchyGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserHierarchyGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserHierarchyGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUserHierarchyGroupsResponse:
    boto3_raw_data: "type_defs.SearchUserHierarchyGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserHierarchyGroups(self):  # pragma: no cover
        return HierarchyGroup.make_many(self.boto3_raw_data["UserHierarchyGroups"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchUserHierarchyGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUserHierarchyGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoricalMetricResult:
    boto3_raw_data: "type_defs.HistoricalMetricResultTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimensions.make_one(self.boto3_raw_data["Dimensions"])

    @cached_property
    def Collections(self):  # pragma: no cover
        return HistoricalMetricData.make_many(self.boto3_raw_data["Collections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HistoricalMetricResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHoursOfOperationResponse:
    boto3_raw_data: "type_defs.DescribeHoursOfOperationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HoursOfOperation(self):  # pragma: no cover
        return HoursOfOperation.make_one(self.boto3_raw_data["HoursOfOperation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeHoursOfOperationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHoursOfOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchHoursOfOperationsResponse:
    boto3_raw_data: "type_defs.SearchHoursOfOperationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HoursOfOperations(self):  # pragma: no cover
        return HoursOfOperation.make_many(self.boto3_raw_data["HoursOfOperations"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchHoursOfOperationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchHoursOfOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHoursOfOperationOverrideResponse:
    boto3_raw_data: "type_defs.DescribeHoursOfOperationOverrideResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HoursOfOperationOverride(self):  # pragma: no cover
        return HoursOfOperationOverride.make_one(
            self.boto3_raw_data["HoursOfOperationOverride"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHoursOfOperationOverrideResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHoursOfOperationOverrideResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHoursOfOperationOverridesResponse:
    boto3_raw_data: "type_defs.ListHoursOfOperationOverridesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HoursOfOperationOverrideList(self):  # pragma: no cover
        return HoursOfOperationOverride.make_many(
            self.boto3_raw_data["HoursOfOperationOverrideList"]
        )

    LastModifiedRegion = field("LastModifiedRegion")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHoursOfOperationOverridesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHoursOfOperationOverridesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchHoursOfOperationOverridesResponse:
    boto3_raw_data: "type_defs.SearchHoursOfOperationOverridesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HoursOfOperationOverrides(self):  # pragma: no cover
        return HoursOfOperationOverride.make_many(
            self.boto3_raw_data["HoursOfOperationOverrides"]
        )

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchHoursOfOperationOverridesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchHoursOfOperationOverridesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectiveHoursOfOperationsResponse:
    boto3_raw_data: "type_defs.GetEffectiveHoursOfOperationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EffectiveHoursOfOperationList(self):  # pragma: no cover
        return EffectiveHoursOfOperations.make_many(
            self.boto3_raw_data["EffectiveHoursOfOperationList"]
        )

    TimeZone = field("TimeZone")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEffectiveHoursOfOperationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectiveHoursOfOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaskTemplateResponse:
    boto3_raw_data: "type_defs.GetTaskTemplateResponseTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    ContactFlowId = field("ContactFlowId")
    SelfAssignFlowId = field("SelfAssignFlowId")

    @cached_property
    def Constraints(self):  # pragma: no cover
        return TaskTemplateConstraintsOutput.make_one(
            self.boto3_raw_data["Constraints"]
        )

    @cached_property
    def Defaults(self):  # pragma: no cover
        return TaskTemplateDefaultsOutput.make_one(self.boto3_raw_data["Defaults"])

    @cached_property
    def Fields(self):  # pragma: no cover
        return TaskTemplateFieldOutput.make_many(self.boto3_raw_data["Fields"])

    Status = field("Status")
    LastModifiedTime = field("LastModifiedTime")
    CreatedTime = field("CreatedTime")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaskTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaskTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskTemplateResponse:
    boto3_raw_data: "type_defs.UpdateTaskTemplateResponseTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    ContactFlowId = field("ContactFlowId")
    SelfAssignFlowId = field("SelfAssignFlowId")

    @cached_property
    def Constraints(self):  # pragma: no cover
        return TaskTemplateConstraintsOutput.make_one(
            self.boto3_raw_data["Constraints"]
        )

    @cached_property
    def Defaults(self):  # pragma: no cover
        return TaskTemplateDefaultsOutput.make_one(self.boto3_raw_data["Defaults"])

    @cached_property
    def Fields(self):  # pragma: no cover
        return TaskTemplateFieldOutput.make_many(self.boto3_raw_data["Fields"])

    Status = field("Status")
    LastModifiedTime = field("LastModifiedTime")
    CreatedTime = field("CreatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricResultV2:
    boto3_raw_data: "type_defs.MetricResultV2TypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")

    @cached_property
    def MetricInterval(self):  # pragma: no cover
        return MetricInterval.make_one(self.boto3_raw_data["MetricInterval"])

    @cached_property
    def Collections(self):  # pragma: no cover
        return MetricDataV2.make_many(self.boto3_raw_data["Collections"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricResultV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricResultV2TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParticipantRoleConfigChannelInfo:
    boto3_raw_data: "type_defs.UpdateParticipantRoleConfigChannelInfoTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Chat(self):  # pragma: no cover
        return ChatParticipantRoleConfig.make_one(self.boto3_raw_data["Chat"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateParticipantRoleConfigChannelInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParticipantRoleConfigChannelInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQuickConnectResponse:
    boto3_raw_data: "type_defs.DescribeQuickConnectResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QuickConnect(self):  # pragma: no cover
        return QuickConnect.make_one(self.boto3_raw_data["QuickConnect"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQuickConnectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQuickConnectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchQuickConnectsResponse:
    boto3_raw_data: "type_defs.SearchQuickConnectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def QuickConnects(self):  # pragma: no cover
        return QuickConnect.make_many(self.boto3_raw_data["QuickConnects"])

    ApproximateTotalCount = field("ApproximateTotalCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchQuickConnectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchQuickConnectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisCategoryDetails:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisCategoryDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PointsOfInterest(self):  # pragma: no cover
        return RealTimeContactAnalysisPointOfInterest.make_many(
            self.boto3_raw_data["PointsOfInterest"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisCategoryDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisCategoryDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisSegmentIssues:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisSegmentIssuesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IssuesDetected(self):  # pragma: no cover
        return RealTimeContactAnalysisIssueDetected.make_many(
            self.boto3_raw_data["IssuesDetected"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisSegmentIssuesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisSegmentIssuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrafficDistributionRequest:
    boto3_raw_data: "type_defs.UpdateTrafficDistributionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    TelephonyConfig = field("TelephonyConfig")
    SignInConfig = field("SignInConfig")
    AgentConfig = field("AgentConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTrafficDistributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrafficDistributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendOutboundEmailRequest:
    boto3_raw_data: "type_defs.SendOutboundEmailRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def FromEmailAddress(self):  # pragma: no cover
        return EmailAddressInfo.make_one(self.boto3_raw_data["FromEmailAddress"])

    @cached_property
    def DestinationEmailAddress(self):  # pragma: no cover
        return EmailAddressInfo.make_one(self.boto3_raw_data["DestinationEmailAddress"])

    @cached_property
    def EmailMessage(self):  # pragma: no cover
        return OutboundEmailContent.make_one(self.boto3_raw_data["EmailMessage"])

    TrafficType = field("TrafficType")

    @cached_property
    def AdditionalRecipients(self):  # pragma: no cover
        return OutboundAdditionalRecipients.make_one(
            self.boto3_raw_data["AdditionalRecipients"]
        )

    @cached_property
    def SourceCampaign(self):  # pragma: no cover
        return SourceCampaign.make_one(self.boto3_raw_data["SourceCampaign"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendOutboundEmailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendOutboundEmailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOutboundEmailContactRequest:
    boto3_raw_data: "type_defs.StartOutboundEmailContactRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @cached_property
    def DestinationEmailAddress(self):  # pragma: no cover
        return EmailAddressInfo.make_one(self.boto3_raw_data["DestinationEmailAddress"])

    @cached_property
    def EmailMessage(self):  # pragma: no cover
        return OutboundEmailContent.make_one(self.boto3_raw_data["EmailMessage"])

    @cached_property
    def FromEmailAddress(self):  # pragma: no cover
        return EmailAddressInfo.make_one(self.boto3_raw_data["FromEmailAddress"])

    @cached_property
    def AdditionalRecipients(self):  # pragma: no cover
        return OutboundAdditionalRecipients.make_one(
            self.boto3_raw_data["AdditionalRecipients"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartOutboundEmailContactRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOutboundEmailContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCriteria:
    boto3_raw_data: "type_defs.SearchCriteriaTypeDef" = dataclasses.field()

    AgentIds = field("AgentIds")

    @cached_property
    def AgentHierarchyGroups(self):  # pragma: no cover
        return AgentHierarchyGroups.make_one(
            self.boto3_raw_data["AgentHierarchyGroups"]
        )

    Channels = field("Channels")

    @cached_property
    def ContactAnalysis(self):  # pragma: no cover
        return ContactAnalysis.make_one(self.boto3_raw_data["ContactAnalysis"])

    InitiationMethods = field("InitiationMethods")
    QueueIds = field("QueueIds")

    @cached_property
    def SearchableContactAttributes(self):  # pragma: no cover
        return SearchableContactAttributes.make_one(
            self.boto3_raw_data["SearchableContactAttributes"]
        )

    @cached_property
    def SearchableSegmentAttributes(self):  # pragma: no cover
        return SearchableSegmentAttributes.make_one(
            self.boto3_raw_data["SearchableSegmentAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Step:
    boto3_raw_data: "type_defs.StepTypeDef" = dataclasses.field()

    @cached_property
    def Expiry(self):  # pragma: no cover
        return Expiry.make_one(self.boto3_raw_data["Expiry"])

    @cached_property
    def Expression(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["Expression"])

    Status = field("Status")

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
class AttributeCondition:
    boto3_raw_data: "type_defs.AttributeConditionTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    ProficiencyLevel = field("ProficiencyLevel")

    @cached_property
    def Range(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["Range"])

    MatchCriteria = field("MatchCriteria")
    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAgentStatusesRequestPaginate:
    boto3_raw_data: "type_defs.SearchAgentStatusesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return AgentStatusSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return AgentStatusSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAgentStatusesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAgentStatusesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAgentStatusesRequest:
    boto3_raw_data: "type_defs.SearchAgentStatusesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return AgentStatusSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return AgentStatusSearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchAgentStatusesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAgentStatusesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUserHierarchyGroupsRequestPaginate:
    boto3_raw_data: "type_defs.SearchUserHierarchyGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return UserHierarchyGroupSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return UserHierarchyGroupSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchUserHierarchyGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUserHierarchyGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUserHierarchyGroupsRequest:
    boto3_raw_data: "type_defs.SearchUserHierarchyGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return UserHierarchyGroupSearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return UserHierarchyGroupSearchCriteria.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchUserHierarchyGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUserHierarchyGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWebRTCContactResponse:
    boto3_raw_data: "type_defs.StartWebRTCContactResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConnectionData(self):  # pragma: no cover
        return ConnectionData.make_one(self.boto3_raw_data["ConnectionData"])

    ContactId = field("ContactId")
    ParticipantId = field("ParticipantId")
    ParticipantToken = field("ParticipantToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartWebRTCContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWebRTCContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    Name = field("Name")
    RuleId = field("RuleId")
    RuleArn = field("RuleArn")

    @cached_property
    def TriggerEventSource(self):  # pragma: no cover
        return RuleTriggerEventSource.make_one(
            self.boto3_raw_data["TriggerEventSource"]
        )

    Function = field("Function")

    @cached_property
    def Actions(self):  # pragma: no cover
        return RuleActionOutput.make_many(self.boto3_raw_data["Actions"])

    PublishStatus = field("PublishStatus")
    CreatedTime = field("CreatedTime")
    LastUpdatedTime = field("LastUpdatedTime")
    LastUpdatedBy = field("LastUpdatedBy")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersRequestPaginate:
    boto3_raw_data: "type_defs.SearchUsersRequestPaginateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return UserSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return UserSearchCriteriaPaginator.make_one(
            self.boto3_raw_data["SearchCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersRequest:
    boto3_raw_data: "type_defs.SearchUsersRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return UserSearchFilter.make_one(self.boto3_raw_data["SearchFilter"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return UserSearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormQuestionTypePropertiesOutput:
    boto3_raw_data: "type_defs.EvaluationFormQuestionTypePropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Numeric(self):  # pragma: no cover
        return EvaluationFormNumericQuestionPropertiesOutput.make_one(
            self.boto3_raw_data["Numeric"]
        )

    @cached_property
    def SingleSelect(self):  # pragma: no cover
        return EvaluationFormSingleSelectQuestionPropertiesOutput.make_one(
            self.boto3_raw_data["SingleSelect"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormQuestionTypePropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormQuestionTypePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormSingleSelectQuestionProperties:
    boto3_raw_data: "type_defs.EvaluationFormSingleSelectQuestionPropertiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Options(self):  # pragma: no cover
        return EvaluationFormSingleSelectQuestionOption.make_many(
            self.boto3_raw_data["Options"]
        )

    DisplayAs = field("DisplayAs")
    Automation = field("Automation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormSingleSelectQuestionPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormSingleSelectQuestionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssignSlaActionDefinition:
    boto3_raw_data: "type_defs.AssignSlaActionDefinitionTypeDef" = dataclasses.field()

    SlaAssignmentType = field("SlaAssignmentType")
    CaseSlaConfiguration = field("CaseSlaConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignSlaActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignSlaActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseActionDefinition:
    boto3_raw_data: "type_defs.CreateCaseActionDefinitionTypeDef" = dataclasses.field()

    Fields = field("Fields")
    TemplateId = field("TemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCaseActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCaseActionDefinition:
    boto3_raw_data: "type_defs.UpdateCaseActionDefinitionTypeDef" = dataclasses.field()

    Fields = field("Fields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCaseActionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCaseActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataResponse:
    boto3_raw_data: "type_defs.GetMetricDataResponseTypeDef" = dataclasses.field()

    @cached_property
    def MetricResults(self):  # pragma: no cover
        return HistoricalMetricResult.make_many(self.boto3_raw_data["MetricResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTaskTemplateRequest:
    boto3_raw_data: "type_defs.CreateTaskTemplateRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")
    Fields = field("Fields")
    Description = field("Description")
    ContactFlowId = field("ContactFlowId")
    SelfAssignFlowId = field("SelfAssignFlowId")
    Constraints = field("Constraints")
    Defaults = field("Defaults")
    Status = field("Status")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTaskTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTaskTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskTemplateRequest:
    boto3_raw_data: "type_defs.UpdateTaskTemplateRequestTypeDef" = dataclasses.field()

    TaskTemplateId = field("TaskTemplateId")
    InstanceId = field("InstanceId")
    Name = field("Name")
    Description = field("Description")
    ContactFlowId = field("ContactFlowId")
    SelfAssignFlowId = field("SelfAssignFlowId")
    Constraints = field("Constraints")
    Defaults = field("Defaults")
    Status = field("Status")
    Fields = field("Fields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataV2Request:
    boto3_raw_data: "type_defs.GetMetricDataV2RequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def Filters(self):  # pragma: no cover
        return FilterV2.make_many(self.boto3_raw_data["Filters"])

    Metrics = field("Metrics")

    @cached_property
    def Interval(self):  # pragma: no cover
        return IntervalDetails.make_one(self.boto3_raw_data["Interval"])

    Groupings = field("Groupings")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricDataV2Response:
    boto3_raw_data: "type_defs.GetMetricDataV2ResponseTypeDef" = dataclasses.field()

    @cached_property
    def MetricResults(self):  # pragma: no cover
        return MetricResultV2.make_many(self.boto3_raw_data["MetricResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricDataV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricDataV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParticipantRoleConfigRequest:
    boto3_raw_data: "type_defs.UpdateParticipantRoleConfigRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")

    @cached_property
    def ChannelConfiguration(self):  # pragma: no cover
        return UpdateParticipantRoleConfigChannelInfo.make_one(
            self.boto3_raw_data["ChannelConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateParticipantRoleConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateParticipantRoleConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeContactAnalysisSegmentCategories:
    boto3_raw_data: "type_defs.RealTimeContactAnalysisSegmentCategoriesTypeDef" = (
        dataclasses.field()
    )

    MatchedDetails = field("MatchedDetails")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RealTimeContactAnalysisSegmentCategoriesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeContactAnalysisSegmentCategoriesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactsRequestPaginate:
    boto3_raw_data: "type_defs.SearchContactsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def TimeRange(self):  # pragma: no cover
        return SearchContactsTimeRange.make_one(self.boto3_raw_data["TimeRange"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return SearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    @cached_property
    def Sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["Sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchContactsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchContactsRequest:
    boto3_raw_data: "type_defs.SearchContactsRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def TimeRange(self):  # pragma: no cover
        return SearchContactsTimeRange.make_one(self.boto3_raw_data["TimeRange"])

    @cached_property
    def SearchCriteria(self):  # pragma: no cover
        return SearchCriteria.make_one(self.boto3_raw_data["SearchCriteria"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["Sort"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchContactsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchContactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingCriteria:
    boto3_raw_data: "type_defs.RoutingCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def Steps(self):  # pragma: no cover
        return Step.make_many(self.boto3_raw_data["Steps"])

    ActivationTimestamp = field("ActivationTimestamp")
    Index = field("Index")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleResponse:
    boto3_raw_data: "type_defs.DescribeRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rule(self):  # pragma: no cover
        return Rule.make_one(self.boto3_raw_data["Rule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormQuestionOutput:
    boto3_raw_data: "type_defs.EvaluationFormQuestionOutputTypeDef" = (
        dataclasses.field()
    )

    Title = field("Title")
    RefId = field("RefId")
    QuestionType = field("QuestionType")
    Instructions = field("Instructions")
    NotApplicableEnabled = field("NotApplicableEnabled")

    @cached_property
    def QuestionTypeProperties(self):  # pragma: no cover
        return EvaluationFormQuestionTypePropertiesOutput.make_one(
            self.boto3_raw_data["QuestionTypeProperties"]
        )

    Weight = field("Weight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormQuestionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormQuestionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealtimeContactAnalysisSegment:
    boto3_raw_data: "type_defs.RealtimeContactAnalysisSegmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Transcript(self):  # pragma: no cover
        return RealTimeContactAnalysisSegmentTranscript.make_one(
            self.boto3_raw_data["Transcript"]
        )

    @cached_property
    def Categories(self):  # pragma: no cover
        return RealTimeContactAnalysisSegmentCategories.make_one(
            self.boto3_raw_data["Categories"]
        )

    @cached_property
    def Issues(self):  # pragma: no cover
        return RealTimeContactAnalysisSegmentIssues.make_one(
            self.boto3_raw_data["Issues"]
        )

    @cached_property
    def Event(self):  # pragma: no cover
        return RealTimeContactAnalysisSegmentEvent.make_one(
            self.boto3_raw_data["Event"]
        )

    @cached_property
    def Attachments(self):  # pragma: no cover
        return RealTimeContactAnalysisSegmentAttachments.make_one(
            self.boto3_raw_data["Attachments"]
        )

    @cached_property
    def PostContactSummary(self):  # pragma: no cover
        return RealTimeContactAnalysisSegmentPostContactSummary.make_one(
            self.boto3_raw_data["PostContactSummary"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RealtimeContactAnalysisSegmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealtimeContactAnalysisSegmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Contact:
    boto3_raw_data: "type_defs.ContactTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    InitialContactId = field("InitialContactId")
    PreviousContactId = field("PreviousContactId")
    ContactAssociationId = field("ContactAssociationId")
    InitiationMethod = field("InitiationMethod")
    Name = field("Name")
    Description = field("Description")
    Channel = field("Channel")

    @cached_property
    def QueueInfo(self):  # pragma: no cover
        return QueueInfo.make_one(self.boto3_raw_data["QueueInfo"])

    @cached_property
    def AgentInfo(self):  # pragma: no cover
        return AgentInfo.make_one(self.boto3_raw_data["AgentInfo"])

    InitiationTimestamp = field("InitiationTimestamp")
    DisconnectTimestamp = field("DisconnectTimestamp")
    LastUpdateTimestamp = field("LastUpdateTimestamp")
    LastPausedTimestamp = field("LastPausedTimestamp")
    LastResumedTimestamp = field("LastResumedTimestamp")
    TotalPauseCount = field("TotalPauseCount")
    TotalPauseDurationInSeconds = field("TotalPauseDurationInSeconds")
    ScheduledTimestamp = field("ScheduledTimestamp")
    RelatedContactId = field("RelatedContactId")

    @cached_property
    def WisdomInfo(self):  # pragma: no cover
        return WisdomInfo.make_one(self.boto3_raw_data["WisdomInfo"])

    CustomerId = field("CustomerId")

    @cached_property
    def CustomerEndpoint(self):  # pragma: no cover
        return EndpointInfo.make_one(self.boto3_raw_data["CustomerEndpoint"])

    @cached_property
    def SystemEndpoint(self):  # pragma: no cover
        return EndpointInfo.make_one(self.boto3_raw_data["SystemEndpoint"])

    QueueTimeAdjustmentSeconds = field("QueueTimeAdjustmentSeconds")
    QueuePriority = field("QueuePriority")
    Tags = field("Tags")
    ConnectedToSystemTimestamp = field("ConnectedToSystemTimestamp")

    @cached_property
    def RoutingCriteria(self):  # pragma: no cover
        return RoutingCriteria.make_one(self.boto3_raw_data["RoutingCriteria"])

    @cached_property
    def Customer(self):  # pragma: no cover
        return Customer.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Campaign(self):  # pragma: no cover
        return Campaign.make_one(self.boto3_raw_data["Campaign"])

    AnsweringMachineDetectionStatus = field("AnsweringMachineDetectionStatus")

    @cached_property
    def CustomerVoiceActivity(self):  # pragma: no cover
        return CustomerVoiceActivity.make_one(
            self.boto3_raw_data["CustomerVoiceActivity"]
        )

    @cached_property
    def QualityMetrics(self):  # pragma: no cover
        return QualityMetrics.make_one(self.boto3_raw_data["QualityMetrics"])

    @cached_property
    def ChatMetrics(self):  # pragma: no cover
        return ChatMetrics.make_one(self.boto3_raw_data["ChatMetrics"])

    @cached_property
    def DisconnectDetails(self):  # pragma: no cover
        return DisconnectDetails.make_one(self.boto3_raw_data["DisconnectDetails"])

    @cached_property
    def AdditionalEmailRecipients(self):  # pragma: no cover
        return AdditionalEmailRecipients.make_one(
            self.boto3_raw_data["AdditionalEmailRecipients"]
        )

    SegmentAttributes = field("SegmentAttributes")

    @cached_property
    def Recordings(self):  # pragma: no cover
        return RecordingInfo.make_many(self.boto3_raw_data["Recordings"])

    DisconnectReason = field("DisconnectReason")
    ContactEvaluations = field("ContactEvaluations")

    @cached_property
    def ContactDetails(self):  # pragma: no cover
        return ContactDetails.make_one(self.boto3_raw_data["ContactDetails"])

    Attributes = field("Attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Expression:
    boto3_raw_data: "type_defs.ExpressionTypeDef" = dataclasses.field()

    AttributeCondition = field("AttributeCondition")
    AndExpression = field("AndExpression")
    OrExpression = field("OrExpression")
    NotAttributeCondition = field("NotAttributeCondition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpressionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormItemOutput:
    boto3_raw_data: "type_defs.EvaluationFormItemOutputTypeDef" = dataclasses.field()

    @cached_property
    def Section(self):  # pragma: no cover
        return EvaluationFormSectionOutput.make_one(self.boto3_raw_data["Section"])

    @cached_property
    def Question(self):  # pragma: no cover
        return EvaluationFormQuestionOutput.make_one(self.boto3_raw_data["Question"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormQuestionTypeProperties:
    boto3_raw_data: "type_defs.EvaluationFormQuestionTypePropertiesTypeDef" = (
        dataclasses.field()
    )

    Numeric = field("Numeric")
    SingleSelect = field("SingleSelect")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationFormQuestionTypePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormQuestionTypePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleAction:
    boto3_raw_data: "type_defs.RuleActionTypeDef" = dataclasses.field()

    ActionType = field("ActionType")
    TaskAction = field("TaskAction")

    @cached_property
    def EventBridgeAction(self):  # pragma: no cover
        return EventBridgeActionDefinition.make_one(
            self.boto3_raw_data["EventBridgeAction"]
        )

    AssignContactCategoryAction = field("AssignContactCategoryAction")
    SendNotificationAction = field("SendNotificationAction")
    CreateCaseAction = field("CreateCaseAction")
    UpdateCaseAction = field("UpdateCaseAction")
    AssignSlaAction = field("AssignSlaAction")
    EndAssociatedTasksAction = field("EndAssociatedTasksAction")

    @cached_property
    def SubmitAutoEvaluationAction(self):  # pragma: no cover
        return SubmitAutoEvaluationActionDefinition.make_one(
            self.boto3_raw_data["SubmitAutoEvaluationAction"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRealtimeContactAnalysisSegmentsV2Response:
    boto3_raw_data: "type_defs.ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef" = (
        dataclasses.field()
    )

    Channel = field("Channel")
    Status = field("Status")

    @cached_property
    def Segments(self):  # pragma: no cover
        return RealtimeContactAnalysisSegment.make_many(self.boto3_raw_data["Segments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactResponse:
    boto3_raw_data: "type_defs.DescribeContactResponseTypeDef" = dataclasses.field()

    @cached_property
    def Contact(self):  # pragma: no cover
        return Contact.make_one(self.boto3_raw_data["Contact"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormContent:
    boto3_raw_data: "type_defs.EvaluationFormContentTypeDef" = dataclasses.field()

    EvaluationFormVersion = field("EvaluationFormVersion")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormArn = field("EvaluationFormArn")
    Title = field("Title")

    @cached_property
    def Items(self):  # pragma: no cover
        return EvaluationFormItemOutput.make_many(self.boto3_raw_data["Items"])

    Description = field("Description")

    @cached_property
    def ScoringStrategy(self):  # pragma: no cover
        return EvaluationFormScoringStrategy.make_one(
            self.boto3_raw_data["ScoringStrategy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationForm:
    boto3_raw_data: "type_defs.EvaluationFormTypeDef" = dataclasses.field()

    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")
    Locked = field("Locked")
    EvaluationFormArn = field("EvaluationFormArn")
    Title = field("Title")
    Status = field("Status")

    @cached_property
    def Items(self):  # pragma: no cover
        return EvaluationFormItemOutput.make_many(self.boto3_raw_data["Items"])

    CreatedTime = field("CreatedTime")
    CreatedBy = field("CreatedBy")
    LastModifiedTime = field("LastModifiedTime")
    LastModifiedBy = field("LastModifiedBy")
    Description = field("Description")

    @cached_property
    def ScoringStrategy(self):  # pragma: no cover
        return EvaluationFormScoringStrategy.make_one(
            self.boto3_raw_data["ScoringStrategy"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationFormTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingCriteriaInputStep:
    boto3_raw_data: "type_defs.RoutingCriteriaInputStepTypeDef" = dataclasses.field()

    @cached_property
    def Expiry(self):  # pragma: no cover
        return RoutingCriteriaInputStepExpiry.make_one(self.boto3_raw_data["Expiry"])

    Expression = field("Expression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingCriteriaInputStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingCriteriaInputStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContactEvaluationResponse:
    boto3_raw_data: "type_defs.DescribeContactEvaluationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Evaluation(self):  # pragma: no cover
        return Evaluation.make_one(self.boto3_raw_data["Evaluation"])

    @cached_property
    def EvaluationForm(self):  # pragma: no cover
        return EvaluationFormContent.make_one(self.boto3_raw_data["EvaluationForm"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContactEvaluationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContactEvaluationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEvaluationFormResponse:
    boto3_raw_data: "type_defs.DescribeEvaluationFormResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EvaluationForm(self):  # pragma: no cover
        return EvaluationForm.make_one(self.boto3_raw_data["EvaluationForm"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEvaluationFormResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEvaluationFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormQuestion:
    boto3_raw_data: "type_defs.EvaluationFormQuestionTypeDef" = dataclasses.field()

    Title = field("Title")
    RefId = field("RefId")
    QuestionType = field("QuestionType")
    Instructions = field("Instructions")
    NotApplicableEnabled = field("NotApplicableEnabled")
    QuestionTypeProperties = field("QuestionTypeProperties")
    Weight = field("Weight")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormQuestionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormQuestionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleRequest:
    boto3_raw_data: "type_defs.CreateRuleRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Name = field("Name")

    @cached_property
    def TriggerEventSource(self):  # pragma: no cover
        return RuleTriggerEventSource.make_one(
            self.boto3_raw_data["TriggerEventSource"]
        )

    Function = field("Function")
    Actions = field("Actions")
    PublishStatus = field("PublishStatus")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleRequest:
    boto3_raw_data: "type_defs.UpdateRuleRequestTypeDef" = dataclasses.field()

    RuleId = field("RuleId")
    InstanceId = field("InstanceId")
    Name = field("Name")
    Function = field("Function")
    Actions = field("Actions")
    PublishStatus = field("PublishStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingCriteriaInput:
    boto3_raw_data: "type_defs.RoutingCriteriaInputTypeDef" = dataclasses.field()

    @cached_property
    def Steps(self):  # pragma: no cover
        return RoutingCriteriaInputStep.make_many(self.boto3_raw_data["Steps"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingCriteriaInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingCriteriaInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactRoutingDataRequest:
    boto3_raw_data: "type_defs.UpdateContactRoutingDataRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    ContactId = field("ContactId")
    QueueTimeAdjustmentSeconds = field("QueueTimeAdjustmentSeconds")
    QueuePriority = field("QueuePriority")

    @cached_property
    def RoutingCriteria(self):  # pragma: no cover
        return RoutingCriteriaInput.make_one(self.boto3_raw_data["RoutingCriteria"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateContactRoutingDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactRoutingDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationFormItem:
    boto3_raw_data: "type_defs.EvaluationFormItemTypeDef" = dataclasses.field()

    Section = field("Section")
    Question = field("Question")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationFormItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationFormItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEvaluationFormRequest:
    boto3_raw_data: "type_defs.CreateEvaluationFormRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    Title = field("Title")
    Items = field("Items")
    Description = field("Description")

    @cached_property
    def ScoringStrategy(self):  # pragma: no cover
        return EvaluationFormScoringStrategy.make_one(
            self.boto3_raw_data["ScoringStrategy"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEvaluationFormRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEvaluationFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEvaluationFormRequest:
    boto3_raw_data: "type_defs.UpdateEvaluationFormRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    EvaluationFormId = field("EvaluationFormId")
    EvaluationFormVersion = field("EvaluationFormVersion")
    Title = field("Title")
    Items = field("Items")
    CreateNewVersion = field("CreateNewVersion")
    Description = field("Description")

    @cached_property
    def ScoringStrategy(self):  # pragma: no cover
        return EvaluationFormScoringStrategy.make_one(
            self.boto3_raw_data["ScoringStrategy"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEvaluationFormRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEvaluationFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
