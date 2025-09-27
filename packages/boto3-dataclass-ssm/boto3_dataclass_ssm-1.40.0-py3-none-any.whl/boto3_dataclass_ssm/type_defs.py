# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountSharingInfo:
    boto3_raw_data: "type_defs.AccountSharingInfoTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    SharedDocumentVersion = field("SharedDocumentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountSharingInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountSharingInfoTypeDef"]
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
class Alarm:
    boto3_raw_data: "type_defs.AlarmTypeDef" = dataclasses.field()

    Name = field("Name")

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
class AlarmStateInformation:
    boto3_raw_data: "type_defs.AlarmStateInformationTypeDef" = dataclasses.field()

    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlarmStateInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlarmStateInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateOpsItemRelatedItemRequest:
    boto3_raw_data: "type_defs.AssociateOpsItemRelatedItemRequestTypeDef" = (
        dataclasses.field()
    )

    OpsItemId = field("OpsItemId")
    AssociationType = field("AssociationType")
    ResourceType = field("ResourceType")
    ResourceUri = field("ResourceUri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateOpsItemRelatedItemRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateOpsItemRelatedItemRequestTypeDef"]
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
class AssociationOverview:
    boto3_raw_data: "type_defs.AssociationOverviewTypeDef" = dataclasses.field()

    Status = field("Status")
    DetailedStatus = field("DetailedStatus")
    AssociationStatusAggregatedCount = field("AssociationStatusAggregatedCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationOverviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationStatusOutput:
    boto3_raw_data: "type_defs.AssociationStatusOutputTypeDef" = dataclasses.field()

    Date = field("Date")
    Name = field("Name")
    Message = field("Message")
    AdditionalInfo = field("AdditionalInfo")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetOutput:
    boto3_raw_data: "type_defs.TargetOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationExecutionFilter:
    boto3_raw_data: "type_defs.AssociationExecutionFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSource:
    boto3_raw_data: "type_defs.OutputSourceTypeDef" = dataclasses.field()

    OutputSourceId = field("OutputSourceId")
    OutputSourceType = field("OutputSourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationExecutionTargetsFilter:
    boto3_raw_data: "type_defs.AssociationExecutionTargetsFilterTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociationExecutionTargetsFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationExecutionTargetsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationFilter:
    boto3_raw_data: "type_defs.AssociationFilterTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociationFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentContent:
    boto3_raw_data: "type_defs.AttachmentContentTypeDef" = dataclasses.field()

    Name = field("Name")
    Size = field("Size")
    Hash = field("Hash")
    HashType = field("HashType")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentInformation:
    boto3_raw_data: "type_defs.AttachmentInformationTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachmentInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentsSource:
    boto3_raw_data: "type_defs.AttachmentsSourceTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentsSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentsSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationExecutionFilter:
    boto3_raw_data: "type_defs.AutomationExecutionFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomationExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolvedTargets:
    boto3_raw_data: "type_defs.ResolvedTargetsTypeDef" = dataclasses.field()

    ParameterValues = field("ParameterValues")
    Truncated = field("Truncated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolvedTargetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResolvedTargetsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetPreview:
    boto3_raw_data: "type_defs.TargetPreviewTypeDef" = dataclasses.field()

    Count = field("Count")
    TargetType = field("TargetType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetPreviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetPreviewTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProgressCounters:
    boto3_raw_data: "type_defs.ProgressCountersTypeDef" = dataclasses.field()

    TotalSteps = field("TotalSteps")
    SuccessSteps = field("SuccessSteps")
    FailedSteps = field("FailedSteps")
    CancelledSteps = field("CancelledSteps")
    TimedOutSteps = field("TimedOutSteps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProgressCountersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProgressCountersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelCommandRequest:
    boto3_raw_data: "type_defs.CancelCommandRequestTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMaintenanceWindowExecutionRequest:
    boto3_raw_data: "type_defs.CancelMaintenanceWindowExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelMaintenanceWindowExecutionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMaintenanceWindowExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchOutputConfig:
    boto3_raw_data: "type_defs.CloudWatchOutputConfigTypeDef" = dataclasses.field()

    CloudWatchLogGroupName = field("CloudWatchLogGroupName")
    CloudWatchOutputEnabled = field("CloudWatchOutputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchOutputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandFilter:
    boto3_raw_data: "type_defs.CommandFilterTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommandFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandPlugin:
    boto3_raw_data: "type_defs.CommandPluginTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    ResponseCode = field("ResponseCode")
    ResponseStartDateTime = field("ResponseStartDateTime")
    ResponseFinishDateTime = field("ResponseFinishDateTime")
    Output = field("Output")
    StandardOutputUrl = field("StandardOutputUrl")
    StandardErrorUrl = field("StandardErrorUrl")
    OutputS3Region = field("OutputS3Region")
    OutputS3BucketName = field("OutputS3BucketName")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandPluginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommandPluginTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigOutput:
    boto3_raw_data: "type_defs.NotificationConfigOutputTypeDef" = dataclasses.field()

    NotificationArn = field("NotificationArn")
    NotificationEvents = field("NotificationEvents")
    NotificationType = field("NotificationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceExecutionSummaryOutput:
    boto3_raw_data: "type_defs.ComplianceExecutionSummaryOutputTypeDef" = (
        dataclasses.field()
    )

    ExecutionTime = field("ExecutionTime")
    ExecutionId = field("ExecutionId")
    ExecutionType = field("ExecutionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComplianceExecutionSummaryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceExecutionSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceItemEntry:
    boto3_raw_data: "type_defs.ComplianceItemEntryTypeDef" = dataclasses.field()

    Severity = field("Severity")
    Status = field("Status")
    Id = field("Id")
    Title = field("Title")
    Details = field("Details")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceItemEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceItemEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceStringFilter:
    boto3_raw_data: "type_defs.ComplianceStringFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceStringFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceStringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeveritySummary:
    boto3_raw_data: "type_defs.SeveritySummaryTypeDef" = dataclasses.field()

    CriticalCount = field("CriticalCount")
    HighCount = field("HighCount")
    MediumCount = field("MediumCount")
    LowCount = field("LowCount")
    InformationalCount = field("InformationalCount")
    UnspecifiedCount = field("UnspecifiedCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeveritySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeveritySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationMetadataItem:
    boto3_raw_data: "type_defs.RegistrationMetadataItemTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationMetadataItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationMetadataItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentRequires:
    boto3_raw_data: "type_defs.DocumentRequiresTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")
    RequireType = field("RequireType")
    VersionName = field("VersionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentRequiresTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentRequiresTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemDataValue:
    boto3_raw_data: "type_defs.OpsItemDataValueTypeDef" = dataclasses.field()

    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsItemDataValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsItemDataValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemNotification:
    boto3_raw_data: "type_defs.OpsItemNotificationTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsItemNotificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsItemNotificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedOpsItem:
    boto3_raw_data: "type_defs.RelatedOpsItemTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelatedOpsItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelatedOpsItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataValue:
    boto3_raw_data: "type_defs.MetadataValueTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    ExpirationTime = field("ExpirationTime")

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
class DeleteActivationRequest:
    boto3_raw_data: "type_defs.DeleteActivationRequestTypeDef" = dataclasses.field()

    ActivationId = field("ActivationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteActivationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteActivationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssociationRequest:
    boto3_raw_data: "type_defs.DeleteAssociationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocumentRequest:
    boto3_raw_data: "type_defs.DeleteDocumentRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DocumentVersion = field("DocumentVersion")
    VersionName = field("VersionName")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInventoryRequest:
    boto3_raw_data: "type_defs.DeleteInventoryRequestTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    SchemaDeleteOption = field("SchemaDeleteOption")
    DryRun = field("DryRun")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInventoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInventoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.DeleteMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMaintenanceWindowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOpsItemRequest:
    boto3_raw_data: "type_defs.DeleteOpsItemRequestTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOpsItemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOpsItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOpsMetadataRequest:
    boto3_raw_data: "type_defs.DeleteOpsMetadataRequestTypeDef" = dataclasses.field()

    OpsMetadataArn = field("OpsMetadataArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOpsMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOpsMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteParameterRequest:
    boto3_raw_data: "type_defs.DeleteParameterRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParameterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParameterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteParametersRequest:
    boto3_raw_data: "type_defs.DeleteParametersRequestTypeDef" = dataclasses.field()

    Names = field("Names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParametersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePatchBaselineRequest:
    boto3_raw_data: "type_defs.DeletePatchBaselineRequestTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePatchBaselineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePatchBaselineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceDataSyncRequest:
    boto3_raw_data: "type_defs.DeleteResourceDataSyncRequestTypeDef" = (
        dataclasses.field()
    )

    SyncName = field("SyncName")
    SyncType = field("SyncType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResourceDataSyncRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceDataSyncRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    PolicyId = field("PolicyId")
    PolicyHash = field("PolicyHash")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterManagedInstanceRequest:
    boto3_raw_data: "type_defs.DeregisterManagedInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterManagedInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterManagedInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterPatchBaselineForPatchGroupRequest:
    boto3_raw_data: "type_defs.DeregisterPatchBaselineForPatchGroupRequestTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")
    PatchGroup = field("PatchGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterPatchBaselineForPatchGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterPatchBaselineForPatchGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTargetFromMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.DeregisterTargetFromMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTargetId = field("WindowTargetId")
    Safe = field("Safe")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterTargetFromMaintenanceWindowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTargetFromMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTaskFromMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.DeregisterTaskFromMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterTaskFromMaintenanceWindowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTaskFromMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivationsFilter:
    boto3_raw_data: "type_defs.DescribeActivationsFilterTypeDef" = dataclasses.field()

    FilterKey = field("FilterKey")
    FilterValues = field("FilterValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivationsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivationsFilterTypeDef"]
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
class DescribeAssociationRequest:
    boto3_raw_data: "type_defs.DescribeAssociationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")
    AssociationVersion = field("AssociationVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepExecutionFilter:
    boto3_raw_data: "type_defs.StepExecutionFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchOrchestratorFilter:
    boto3_raw_data: "type_defs.PatchOrchestratorFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatchOrchestratorFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchOrchestratorFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Patch:
    boto3_raw_data: "type_defs.PatchTypeDef" = dataclasses.field()

    Id = field("Id")
    ReleaseDate = field("ReleaseDate")
    Title = field("Title")
    Description = field("Description")
    ContentUrl = field("ContentUrl")
    Vendor = field("Vendor")
    ProductFamily = field("ProductFamily")
    Product = field("Product")
    Classification = field("Classification")
    MsrcSeverity = field("MsrcSeverity")
    KbNumber = field("KbNumber")
    MsrcNumber = field("MsrcNumber")
    Language = field("Language")
    AdvisoryIds = field("AdvisoryIds")
    BugzillaIds = field("BugzillaIds")
    CVEIds = field("CVEIds")
    Name = field("Name")
    Epoch = field("Epoch")
    Version = field("Version")
    Release = field("Release")
    Arch = field("Arch")
    Severity = field("Severity")
    Repository = field("Repository")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentPermissionRequest:
    boto3_raw_data: "type_defs.DescribeDocumentPermissionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    PermissionType = field("PermissionType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentPermissionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentRequest:
    boto3_raw_data: "type_defs.DescribeDocumentRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DocumentVersion = field("DocumentVersion")
    VersionName = field("VersionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEffectiveInstanceAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeEffectiveInstanceAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEffectiveInstanceAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEffectiveInstanceAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAssociation:
    boto3_raw_data: "type_defs.InstanceAssociationTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    InstanceId = field("InstanceId")
    Content = field("Content")
    AssociationVersion = field("AssociationVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEffectivePatchesForPatchBaselineRequest:
    boto3_raw_data: (
        "type_defs.DescribeEffectivePatchesForPatchBaselineRequestTypeDef"
    ) = dataclasses.field()

    BaselineId = field("BaselineId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEffectivePatchesForPatchBaselineRequestTypeDef"
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
                "type_defs.DescribeEffectivePatchesForPatchBaselineRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAssociationsStatusRequest:
    boto3_raw_data: "type_defs.DescribeInstanceAssociationsStatusRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceAssociationsStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceAssociationsStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceInformationFilter:
    boto3_raw_data: "type_defs.InstanceInformationFilterTypeDef" = dataclasses.field()

    key = field("key")
    valueSet = field("valueSet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceInformationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceInformationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceInformationStringFilter:
    boto3_raw_data: "type_defs.InstanceInformationStringFilterTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceInformationStringFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceInformationStringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancePatchStateFilter:
    boto3_raw_data: "type_defs.InstancePatchStateFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancePatchStateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePatchStateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancePatchState:
    boto3_raw_data: "type_defs.InstancePatchStateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PatchGroup = field("PatchGroup")
    BaselineId = field("BaselineId")
    OperationStartTime = field("OperationStartTime")
    OperationEndTime = field("OperationEndTime")
    Operation = field("Operation")
    SnapshotId = field("SnapshotId")
    InstallOverrideList = field("InstallOverrideList")
    OwnerInformation = field("OwnerInformation")
    InstalledCount = field("InstalledCount")
    InstalledOtherCount = field("InstalledOtherCount")
    InstalledPendingRebootCount = field("InstalledPendingRebootCount")
    InstalledRejectedCount = field("InstalledRejectedCount")
    MissingCount = field("MissingCount")
    FailedCount = field("FailedCount")
    UnreportedNotApplicableCount = field("UnreportedNotApplicableCount")
    NotApplicableCount = field("NotApplicableCount")
    AvailableSecurityUpdateCount = field("AvailableSecurityUpdateCount")
    LastNoRebootInstallOperationTime = field("LastNoRebootInstallOperationTime")
    RebootOption = field("RebootOption")
    CriticalNonCompliantCount = field("CriticalNonCompliantCount")
    SecurityNonCompliantCount = field("SecurityNonCompliantCount")
    OtherNonCompliantCount = field("OtherNonCompliantCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancePatchStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePatchStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchStatesRequest:
    boto3_raw_data: "type_defs.DescribeInstancePatchStatesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceIds = field("InstanceIds")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePatchStatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePatchStatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchComplianceData:
    boto3_raw_data: "type_defs.PatchComplianceDataTypeDef" = dataclasses.field()

    Title = field("Title")
    KBId = field("KBId")
    Classification = field("Classification")
    Severity = field("Severity")
    State = field("State")
    InstalledTime = field("InstalledTime")
    CVEIds = field("CVEIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatchComplianceDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchComplianceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancePropertyFilter:
    boto3_raw_data: "type_defs.InstancePropertyFilterTypeDef" = dataclasses.field()

    key = field("key")
    valueSet = field("valueSet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancePropertyFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePropertyFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstancePropertyStringFilter:
    boto3_raw_data: "type_defs.InstancePropertyStringFilterTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstancePropertyStringFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePropertyStringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInventoryDeletionsRequest:
    boto3_raw_data: "type_defs.DescribeInventoryDeletionsRequestTypeDef" = (
        dataclasses.field()
    )

    DeletionId = field("DeletionId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInventoryDeletionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInventoryDeletionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowFilter:
    boto3_raw_data: "type_defs.MaintenanceWindowFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowExecutionTaskInvocationIdentity:
    boto3_raw_data: (
        "type_defs.MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
    ) = dataclasses.field()

    WindowExecutionId = field("WindowExecutionId")
    TaskExecutionId = field("TaskExecutionId")
    InvocationId = field("InvocationId")
    ExecutionId = field("ExecutionId")
    TaskType = field("TaskType")
    Parameters = field("Parameters")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OwnerInformation = field("OwnerInformation")
    WindowTargetId = field("WindowTargetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
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
                "type_defs.MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowExecution:
    boto3_raw_data: "type_defs.MaintenanceWindowExecutionTypeDef" = dataclasses.field()

    WindowId = field("WindowId")
    WindowExecutionId = field("WindowExecutionId")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledWindowExecution:
    boto3_raw_data: "type_defs.ScheduledWindowExecutionTypeDef" = dataclasses.field()

    WindowId = field("WindowId")
    Name = field("Name")
    ExecutionTime = field("ExecutionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledWindowExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledWindowExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowIdentityForTarget:
    boto3_raw_data: "type_defs.MaintenanceWindowIdentityForTargetTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowIdentityForTargetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowIdentityForTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowIdentity:
    boto3_raw_data: "type_defs.MaintenanceWindowIdentityTypeDef" = dataclasses.field()

    WindowId = field("WindowId")
    Name = field("Name")
    Description = field("Description")
    Enabled = field("Enabled")
    Duration = field("Duration")
    Cutoff = field("Cutoff")
    Schedule = field("Schedule")
    ScheduleTimezone = field("ScheduleTimezone")
    ScheduleOffset = field("ScheduleOffset")
    EndDate = field("EndDate")
    StartDate = field("StartDate")
    NextExecutionTime = field("NextExecutionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowIdentityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemFilter:
    boto3_raw_data: "type_defs.OpsItemFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsItemFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsItemFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterStringFilter:
    boto3_raw_data: "type_defs.ParameterStringFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Option = field("Option")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterStringFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterStringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametersFilter:
    boto3_raw_data: "type_defs.ParametersFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParametersFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametersFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchBaselineIdentity:
    boto3_raw_data: "type_defs.PatchBaselineIdentityTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")
    BaselineName = field("BaselineName")
    OperatingSystem = field("OperatingSystem")
    BaselineDescription = field("BaselineDescription")
    DefaultBaseline = field("DefaultBaseline")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatchBaselineIdentityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchBaselineIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchGroupStateRequest:
    boto3_raw_data: "type_defs.DescribePatchGroupStateRequestTypeDef" = (
        dataclasses.field()
    )

    PatchGroup = field("PatchGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePatchGroupStateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchGroupStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchPropertiesRequest:
    boto3_raw_data: "type_defs.DescribePatchPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    OperatingSystem = field("OperatingSystem")
    Property = field("Property")
    PatchSet = field("PatchSet")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePatchPropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionFilter:
    boto3_raw_data: "type_defs.SessionFilterTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateOpsItemRelatedItemRequest:
    boto3_raw_data: "type_defs.DisassociateOpsItemRelatedItemRequestTypeDef" = (
        dataclasses.field()
    )

    OpsItemId = field("OpsItemId")
    AssociationId = field("AssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateOpsItemRelatedItemRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateOpsItemRelatedItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentDefaultVersionDescription:
    boto3_raw_data: "type_defs.DocumentDefaultVersionDescriptionTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DefaultVersion = field("DefaultVersion")
    DefaultVersionName = field("DefaultVersionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DocumentDefaultVersionDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentDefaultVersionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentParameter:
    boto3_raw_data: "type_defs.DocumentParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Description = field("Description")
    DefaultValue = field("DefaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewInformation:
    boto3_raw_data: "type_defs.ReviewInformationTypeDef" = dataclasses.field()

    ReviewedTime = field("ReviewedTime")
    Status = field("Status")
    Reviewer = field("Reviewer")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReviewInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentFilter:
    boto3_raw_data: "type_defs.DocumentFilterTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentKeyValuesFilter:
    boto3_raw_data: "type_defs.DocumentKeyValuesFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentKeyValuesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentKeyValuesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentReviewCommentSource:
    boto3_raw_data: "type_defs.DocumentReviewCommentSourceTypeDef" = dataclasses.field()

    Type = field("Type")
    Content = field("Content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentReviewCommentSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentReviewCommentSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentVersionInfo:
    boto3_raw_data: "type_defs.DocumentVersionInfoTypeDef" = dataclasses.field()

    Name = field("Name")
    DisplayName = field("DisplayName")
    DocumentVersion = field("DocumentVersion")
    VersionName = field("VersionName")
    CreatedDate = field("CreatedDate")
    IsDefaultVersion = field("IsDefaultVersion")
    DocumentFormat = field("DocumentFormat")
    Status = field("Status")
    StatusInformation = field("StatusInformation")
    ReviewStatus = field("ReviewStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentVersionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentVersionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchStatus:
    boto3_raw_data: "type_defs.PatchStatusTypeDef" = dataclasses.field()

    DeploymentStatus = field("DeploymentStatus")
    ComplianceLevel = field("ComplianceLevel")
    ApprovalDate = field("ApprovalDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureDetails:
    boto3_raw_data: "type_defs.FailureDetailsTypeDef" = dataclasses.field()

    FailureStage = field("FailureStage")
    FailureType = field("FailureType")
    Details = field("Details")

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
class GetAccessTokenRequest:
    boto3_raw_data: "type_defs.GetAccessTokenRequestTypeDef" = dataclasses.field()

    AccessRequestId = field("AccessRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomationExecutionRequest:
    boto3_raw_data: "type_defs.GetAutomationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    AutomationExecutionId = field("AutomationExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAutomationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalendarStateRequest:
    boto3_raw_data: "type_defs.GetCalendarStateRequestTypeDef" = dataclasses.field()

    CalendarNames = field("CalendarNames")
    AtTime = field("AtTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCalendarStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalendarStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandInvocationRequest:
    boto3_raw_data: "type_defs.GetCommandInvocationRequestTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    PluginName = field("PluginName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommandInvocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandInvocationRequestTypeDef"]
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
class GetConnectionStatusRequest:
    boto3_raw_data: "type_defs.GetConnectionStatusRequestTypeDef" = dataclasses.field()

    Target = field("Target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDefaultPatchBaselineRequest:
    boto3_raw_data: "type_defs.GetDefaultPatchBaselineRequestTypeDef" = (
        dataclasses.field()
    )

    OperatingSystem = field("OperatingSystem")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDefaultPatchBaselineRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDefaultPatchBaselineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentRequest:
    boto3_raw_data: "type_defs.GetDocumentRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    VersionName = field("VersionName")
    DocumentVersion = field("DocumentVersion")
    DocumentFormat = field("DocumentFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionPreviewRequest:
    boto3_raw_data: "type_defs.GetExecutionPreviewRequestTypeDef" = dataclasses.field()

    ExecutionPreviewId = field("ExecutionPreviewId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExecutionPreviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryFilter:
    boto3_raw_data: "type_defs.InventoryFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InventoryFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultAttribute:
    boto3_raw_data: "type_defs.ResultAttributeTypeDef" = dataclasses.field()

    TypeName = field("TypeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInventorySchemaRequest:
    boto3_raw_data: "type_defs.GetInventorySchemaRequestTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Aggregator = field("Aggregator")
    SubType = field("SubType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInventorySchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInventorySchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowExecutionRequest:
    boto3_raw_data: "type_defs.GetMaintenanceWindowExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMaintenanceWindowExecutionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowExecutionTaskInvocationRequest:
    boto3_raw_data: (
        "type_defs.GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef"
    ) = dataclasses.field()

    WindowExecutionId = field("WindowExecutionId")
    TaskId = field("TaskId")
    InvocationId = field("InvocationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef"
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
                "type_defs.GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowExecutionTaskRequest:
    boto3_raw_data: "type_defs.GetMaintenanceWindowExecutionTaskRequestTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")
    TaskId = field("TaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMaintenanceWindowExecutionTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowExecutionTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowTaskParameterValueExpressionOutput:
    boto3_raw_data: (
        "type_defs.MaintenanceWindowTaskParameterValueExpressionOutputTypeDef"
    ) = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowTaskParameterValueExpressionOutputTypeDef"
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
                "type_defs.MaintenanceWindowTaskParameterValueExpressionOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.GetMaintenanceWindowRequestTypeDef" = dataclasses.field()

    WindowId = field("WindowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMaintenanceWindowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowTaskRequest:
    boto3_raw_data: "type_defs.GetMaintenanceWindowTaskRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMaintenanceWindowTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingInfo:
    boto3_raw_data: "type_defs.LoggingInfoTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3Region = field("S3Region")
    S3KeyPrefix = field("S3KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsItemRequest:
    boto3_raw_data: "type_defs.GetOpsItemRequestTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")
    OpsItemArn = field("OpsItemArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetOpsItemRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsMetadataRequest:
    boto3_raw_data: "type_defs.GetOpsMetadataRequestTypeDef" = dataclasses.field()

    OpsMetadataArn = field("OpsMetadataArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpsMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsFilter:
    boto3_raw_data: "type_defs.OpsFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsResultAttribute:
    boto3_raw_data: "type_defs.OpsResultAttributeTypeDef" = dataclasses.field()

    TypeName = field("TypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsResultAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsResultAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParameterHistoryRequest:
    boto3_raw_data: "type_defs.GetParameterHistoryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    WithDecryption = field("WithDecryption")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParameterHistoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParameterHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParameterRequest:
    boto3_raw_data: "type_defs.GetParameterRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    WithDecryption = field("WithDecryption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParameterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParameterRequestTypeDef"]
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

    Name = field("Name")
    Type = field("Type")
    Value = field("Value")
    Version = field("Version")
    Selector = field("Selector")
    SourceResult = field("SourceResult")
    LastModifiedDate = field("LastModifiedDate")
    ARN = field("ARN")
    DataType = field("DataType")

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
class GetParametersRequest:
    boto3_raw_data: "type_defs.GetParametersRequestTypeDef" = dataclasses.field()

    Names = field("Names")
    WithDecryption = field("WithDecryption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPatchBaselineForPatchGroupRequest:
    boto3_raw_data: "type_defs.GetPatchBaselineForPatchGroupRequestTypeDef" = (
        dataclasses.field()
    )

    PatchGroup = field("PatchGroup")
    OperatingSystem = field("OperatingSystem")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPatchBaselineForPatchGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPatchBaselineForPatchGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPatchBaselineRequest:
    boto3_raw_data: "type_defs.GetPatchBaselineRequestTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPatchBaselineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPatchBaselineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchSourceOutput:
    boto3_raw_data: "type_defs.PatchSourceOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Products = field("Products")
    Configuration = field("Configuration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchSourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePoliciesRequest:
    boto3_raw_data: "type_defs.GetResourcePoliciesRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePoliciesResponseEntry:
    boto3_raw_data: "type_defs.GetResourcePoliciesResponseEntryTypeDef" = (
        dataclasses.field()
    )

    PolicyId = field("PolicyId")
    PolicyHash = field("PolicyHash")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourcePoliciesResponseEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePoliciesResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSettingRequest:
    boto3_raw_data: "type_defs.GetServiceSettingRequestTypeDef" = dataclasses.field()

    SettingId = field("SettingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSetting:
    boto3_raw_data: "type_defs.ServiceSettingTypeDef" = dataclasses.field()

    SettingId = field("SettingId")
    SettingValue = field("SettingValue")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedUser = field("LastModifiedUser")
    ARN = field("ARN")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAggregatedAssociationOverview:
    boto3_raw_data: "type_defs.InstanceAggregatedAssociationOverviewTypeDef" = (
        dataclasses.field()
    )

    DetailedStatus = field("DetailedStatus")
    InstanceAssociationStatusAggregatedCount = field(
        "InstanceAssociationStatusAggregatedCount"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceAggregatedAssociationOverviewTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAggregatedAssociationOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3OutputLocation:
    boto3_raw_data: "type_defs.S3OutputLocationTypeDef" = dataclasses.field()

    OutputS3Region = field("OutputS3Region")
    OutputS3BucketName = field("OutputS3BucketName")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3OutputLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3OutputLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3OutputUrl:
    boto3_raw_data: "type_defs.S3OutputUrlTypeDef" = dataclasses.field()

    OutputUrl = field("OutputUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3OutputUrlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3OutputUrlTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceInfo:
    boto3_raw_data: "type_defs.InstanceInfoTypeDef" = dataclasses.field()

    AgentType = field("AgentType")
    AgentVersion = field("AgentVersion")
    ComputerName = field("ComputerName")
    InstanceStatus = field("InstanceStatus")
    IpAddress = field("IpAddress")
    ManagedStatus = field("ManagedStatus")
    PlatformType = field("PlatformType")
    PlatformName = field("PlatformName")
    PlatformVersion = field("PlatformVersion")
    ResourceType = field("ResourceType")

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
class InventoryDeletionSummaryItem:
    boto3_raw_data: "type_defs.InventoryDeletionSummaryItemTypeDef" = (
        dataclasses.field()
    )

    Version = field("Version")
    Count = field("Count")
    RemainingCount = field("RemainingCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryDeletionSummaryItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryDeletionSummaryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryItemAttribute:
    boto3_raw_data: "type_defs.InventoryItemAttributeTypeDef" = dataclasses.field()

    Name = field("Name")
    DataType = field("DataType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryItemAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryItemAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryItem:
    boto3_raw_data: "type_defs.InventoryItemTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    SchemaVersion = field("SchemaVersion")
    CaptureTime = field("CaptureTime")
    ContentHash = field("ContentHash")
    Content = field("Content")
    Context = field("Context")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InventoryItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryResultItem:
    boto3_raw_data: "type_defs.InventoryResultItemTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    SchemaVersion = field("SchemaVersion")
    Content = field("Content")
    CaptureTime = field("CaptureTime")
    ContentHash = field("ContentHash")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelParameterVersionRequest:
    boto3_raw_data: "type_defs.LabelParameterVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Labels = field("Labels")
    ParameterVersion = field("ParameterVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelParameterVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelParameterVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationVersionsRequest:
    boto3_raw_data: "type_defs.ListAssociationVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssociationVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociationVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentMetadataHistoryRequest:
    boto3_raw_data: "type_defs.ListDocumentMetadataHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Metadata = field("Metadata")
    DocumentVersion = field("DocumentVersion")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentMetadataHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentMetadataHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentVersionsRequest:
    boto3_raw_data: "type_defs.ListDocumentVersionsRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeFilter:
    boto3_raw_data: "type_defs.NodeFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeAggregatorPaginator:
    boto3_raw_data: "type_defs.NodeAggregatorPaginatorTypeDef" = dataclasses.field()

    AggregatorType = field("AggregatorType")
    TypeName = field("TypeName")
    AttributeName = field("AttributeName")
    Aggregators = field("Aggregators")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeAggregatorPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeAggregatorPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeAggregator:
    boto3_raw_data: "type_defs.NodeAggregatorTypeDef" = dataclasses.field()

    AggregatorType = field("AggregatorType")
    TypeName = field("TypeName")
    AttributeName = field("AttributeName")
    Aggregators = field("Aggregators")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeAggregatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeAggregatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemEventFilter:
    boto3_raw_data: "type_defs.OpsItemEventFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsItemEventFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsItemEventFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemRelatedItemsFilter:
    boto3_raw_data: "type_defs.OpsItemRelatedItemsFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsItemRelatedItemsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsItemRelatedItemsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsMetadataFilter:
    boto3_raw_data: "type_defs.OpsMetadataFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsMetadataFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsMetadataFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsMetadata:
    boto3_raw_data: "type_defs.OpsMetadataTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    OpsMetadataArn = field("OpsMetadataArn")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedUser = field("LastModifiedUser")
    CreationDate = field("CreationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsMetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDataSyncRequest:
    boto3_raw_data: "type_defs.ListResourceDataSyncRequestTypeDef" = dataclasses.field()

    SyncType = field("SyncType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceDataSyncRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDataSyncRequestTypeDef"]
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

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

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
class MaintenanceWindowAutomationParametersOutput:
    boto3_raw_data: "type_defs.MaintenanceWindowAutomationParametersOutputTypeDef" = (
        dataclasses.field()
    )

    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowAutomationParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowAutomationParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowAutomationParameters:
    boto3_raw_data: "type_defs.MaintenanceWindowAutomationParametersTypeDef" = (
        dataclasses.field()
    )

    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowAutomationParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowAutomationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowLambdaParametersOutput:
    boto3_raw_data: "type_defs.MaintenanceWindowLambdaParametersOutputTypeDef" = (
        dataclasses.field()
    )

    ClientContext = field("ClientContext")
    Qualifier = field("Qualifier")
    Payload = field("Payload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowLambdaParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowLambdaParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfig:
    boto3_raw_data: "type_defs.NotificationConfigTypeDef" = dataclasses.field()

    NotificationArn = field("NotificationArn")
    NotificationEvents = field("NotificationEvents")
    NotificationType = field("NotificationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowStepFunctionsParameters:
    boto3_raw_data: "type_defs.MaintenanceWindowStepFunctionsParametersTypeDef" = (
        dataclasses.field()
    )

    Input = field("Input")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowStepFunctionsParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowStepFunctionsParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowTaskParameterValueExpression:
    boto3_raw_data: "type_defs.MaintenanceWindowTaskParameterValueExpressionTypeDef" = (
        dataclasses.field()
    )

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowTaskParameterValueExpressionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowTaskParameterValueExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDocumentPermissionRequest:
    boto3_raw_data: "type_defs.ModifyDocumentPermissionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    PermissionType = field("PermissionType")
    AccountIdsToAdd = field("AccountIdsToAdd")
    AccountIdsToRemove = field("AccountIdsToRemove")
    SharedDocumentVersion = field("SharedDocumentVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyDocumentPermissionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDocumentPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOwnerInfo:
    boto3_raw_data: "type_defs.NodeOwnerInfoTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    OrganizationalUnitId = field("OrganizationalUnitId")
    OrganizationalUnitPath = field("OrganizationalUnitPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOwnerInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOwnerInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsEntityItem:
    boto3_raw_data: "type_defs.OpsEntityItemTypeDef" = dataclasses.field()

    CaptureTime = field("CaptureTime")
    Content = field("Content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsEntityItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsEntityItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemIdentity:
    boto3_raw_data: "type_defs.OpsItemIdentityTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsItemIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsItemIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterInlinePolicy:
    boto3_raw_data: "type_defs.ParameterInlinePolicyTypeDef" = dataclasses.field()

    PolicyText = field("PolicyText")
    PolicyType = field("PolicyType")
    PolicyStatus = field("PolicyStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterInlinePolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterInlinePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParentStepDetails:
    boto3_raw_data: "type_defs.ParentStepDetailsTypeDef" = dataclasses.field()

    StepExecutionId = field("StepExecutionId")
    StepName = field("StepName")
    Action = field("Action")
    Iteration = field("Iteration")
    IteratorValue = field("IteratorValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParentStepDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParentStepDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchFilterOutput:
    boto3_raw_data: "type_defs.PatchFilterOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchFilter:
    boto3_raw_data: "type_defs.PatchFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchSource:
    boto3_raw_data: "type_defs.PatchSourceTypeDef" = dataclasses.field()

    Name = field("Name")
    Products = field("Products")
    Configuration = field("Configuration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")
    PolicyId = field("PolicyId")
    PolicyHash = field("PolicyHash")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDefaultPatchBaselineRequest:
    boto3_raw_data: "type_defs.RegisterDefaultPatchBaselineRequestTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterDefaultPatchBaselineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDefaultPatchBaselineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterPatchBaselineForPatchGroupRequest:
    boto3_raw_data: "type_defs.RegisterPatchBaselineForPatchGroupRequestTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")
    PatchGroup = field("PatchGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterPatchBaselineForPatchGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterPatchBaselineForPatchGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromResourceRequest:
    boto3_raw_data: "type_defs.RemoveTagsFromResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveTagsFromResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetServiceSettingRequest:
    boto3_raw_data: "type_defs.ResetServiceSettingRequestTypeDef" = dataclasses.field()

    SettingId = field("SettingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetServiceSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetServiceSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncOrganizationalUnit:
    boto3_raw_data: "type_defs.ResourceDataSyncOrganizationalUnitTypeDef" = (
        dataclasses.field()
    )

    OrganizationalUnitId = field("OrganizationalUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceDataSyncOrganizationalUnitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncOrganizationalUnitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncDestinationDataSharing:
    boto3_raw_data: "type_defs.ResourceDataSyncDestinationDataSharingTypeDef" = (
        dataclasses.field()
    )

    DestinationDataSharingType = field("DestinationDataSharingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceDataSyncDestinationDataSharingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncDestinationDataSharingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeSessionRequest:
    boto3_raw_data: "type_defs.ResumeSessionRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendAutomationSignalRequest:
    boto3_raw_data: "type_defs.SendAutomationSignalRequestTypeDef" = dataclasses.field()

    AutomationExecutionId = field("AutomationExecutionId")
    SignalType = field("SignalType")
    Payload = field("Payload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendAutomationSignalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendAutomationSignalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionManagerOutputUrl:
    boto3_raw_data: "type_defs.SessionManagerOutputUrlTypeDef" = dataclasses.field()

    S3OutputUrl = field("S3OutputUrl")
    CloudWatchOutputUrl = field("CloudWatchOutputUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionManagerOutputUrlTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionManagerOutputUrlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssociationsOnceRequest:
    boto3_raw_data: "type_defs.StartAssociationsOnceRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationIds = field("AssociationIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAssociationsOnceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssociationsOnceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSessionRequest:
    boto3_raw_data: "type_defs.StartSessionRequestTypeDef" = dataclasses.field()

    Target = field("Target")
    DocumentName = field("DocumentName")
    Reason = field("Reason")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAutomationExecutionRequest:
    boto3_raw_data: "type_defs.StopAutomationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    AutomationExecutionId = field("AutomationExecutionId")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopAutomationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAutomationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateSessionRequest:
    boto3_raw_data: "type_defs.TerminateSessionRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnlabelParameterVersionRequest:
    boto3_raw_data: "type_defs.UnlabelParameterVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    ParameterVersion = field("ParameterVersion")
    Labels = field("Labels")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnlabelParameterVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnlabelParameterVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentDefaultVersionRequest:
    boto3_raw_data: "type_defs.UpdateDocumentDefaultVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DocumentVersion = field("DocumentVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDocumentDefaultVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentDefaultVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.UpdateMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    Name = field("Name")
    Description = field("Description")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    Schedule = field("Schedule")
    ScheduleTimezone = field("ScheduleTimezone")
    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    Cutoff = field("Cutoff")
    AllowUnassociatedTargets = field("AllowUnassociatedTargets")
    Enabled = field("Enabled")
    Replace = field("Replace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMaintenanceWindowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateManagedInstanceRoleRequest:
    boto3_raw_data: "type_defs.UpdateManagedInstanceRoleRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    IamRole = field("IamRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateManagedInstanceRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateManagedInstanceRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSettingRequest:
    boto3_raw_data: "type_defs.UpdateServiceSettingRequestTypeDef" = dataclasses.field()

    SettingId = field("SettingId")
    SettingValue = field("SettingValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Activation:
    boto3_raw_data: "type_defs.ActivationTypeDef" = dataclasses.field()

    ActivationId = field("ActivationId")
    Description = field("Description")
    DefaultInstanceName = field("DefaultInstanceName")
    IamRole = field("IamRole")
    RegistrationLimit = field("RegistrationLimit")
    RegistrationsCount = field("RegistrationsCount")
    ExpirationDate = field("ExpirationDate")
    Expired = field("Expired")
    CreatedDate = field("CreatedDate")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceRequest:
    boto3_raw_data: "type_defs.AddTagsToResourceRequestTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.CreateMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Schedule = field("Schedule")
    Duration = field("Duration")
    Cutoff = field("Cutoff")
    AllowUnassociatedTargets = field("AllowUnassociatedTargets")
    Description = field("Description")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    ScheduleTimezone = field("ScheduleTimezone")
    ScheduleOffset = field("ScheduleOffset")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMaintenanceWindowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutParameterRequest:
    boto3_raw_data: "type_defs.PutParameterRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")
    Description = field("Description")
    Type = field("Type")
    KeyId = field("KeyId")
    Overwrite = field("Overwrite")
    AllowedPattern = field("AllowedPattern")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Tier = field("Tier")
    Policies = field("Policies")
    DataType = field("DataType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutParameterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutParameterRequestTypeDef"]
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

    @cached_property
    def Alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["Alarms"])

    IgnorePollAlarmFailure = field("IgnorePollAlarmFailure")

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

    @cached_property
    def Alarms(self):  # pragma: no cover
        return Alarm.make_many(self.boto3_raw_data["Alarms"])

    IgnorePollAlarmFailure = field("IgnorePollAlarmFailure")

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
class AssociateOpsItemRelatedItemResponse:
    boto3_raw_data: "type_defs.AssociateOpsItemRelatedItemResponseTypeDef" = (
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
            "type_defs.AssociateOpsItemRelatedItemResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateOpsItemRelatedItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMaintenanceWindowExecutionResult:
    boto3_raw_data: "type_defs.CancelMaintenanceWindowExecutionResultTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelMaintenanceWindowExecutionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMaintenanceWindowExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateActivationResult:
    boto3_raw_data: "type_defs.CreateActivationResultTypeDef" = dataclasses.field()

    ActivationId = field("ActivationId")
    ActivationCode = field("ActivationCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateActivationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateActivationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMaintenanceWindowResult:
    boto3_raw_data: "type_defs.CreateMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMaintenanceWindowResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpsItemResponse:
    boto3_raw_data: "type_defs.CreateOpsItemResponseTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")
    OpsItemArn = field("OpsItemArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOpsItemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpsItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpsMetadataResult:
    boto3_raw_data: "type_defs.CreateOpsMetadataResultTypeDef" = dataclasses.field()

    OpsMetadataArn = field("OpsMetadataArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOpsMetadataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpsMetadataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePatchBaselineResult:
    boto3_raw_data: "type_defs.CreatePatchBaselineResultTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePatchBaselineResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePatchBaselineResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMaintenanceWindowResult:
    boto3_raw_data: "type_defs.DeleteMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMaintenanceWindowResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteParametersResult:
    boto3_raw_data: "type_defs.DeleteParametersResultTypeDef" = dataclasses.field()

    DeletedParameters = field("DeletedParameters")
    InvalidParameters = field("InvalidParameters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteParametersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePatchBaselineResult:
    boto3_raw_data: "type_defs.DeletePatchBaselineResultTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePatchBaselineResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePatchBaselineResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterPatchBaselineForPatchGroupResult:
    boto3_raw_data: "type_defs.DeregisterPatchBaselineForPatchGroupResultTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")
    PatchGroup = field("PatchGroup")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterPatchBaselineForPatchGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterPatchBaselineForPatchGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTargetFromMaintenanceWindowResult:
    boto3_raw_data: "type_defs.DeregisterTargetFromMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTargetId = field("WindowTargetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterTargetFromMaintenanceWindowResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTargetFromMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTaskFromMaintenanceWindowResult:
    boto3_raw_data: "type_defs.DeregisterTaskFromMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterTaskFromMaintenanceWindowResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTaskFromMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentPermissionResponse:
    boto3_raw_data: "type_defs.DescribeDocumentPermissionResponseTypeDef" = (
        dataclasses.field()
    )

    AccountIds = field("AccountIds")

    @cached_property
    def AccountSharingInfoList(self):  # pragma: no cover
        return AccountSharingInfo.make_many(
            self.boto3_raw_data["AccountSharingInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDocumentPermissionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentPermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchGroupStateResult:
    boto3_raw_data: "type_defs.DescribePatchGroupStateResultTypeDef" = (
        dataclasses.field()
    )

    Instances = field("Instances")
    InstancesWithInstalledPatches = field("InstancesWithInstalledPatches")
    InstancesWithInstalledOtherPatches = field("InstancesWithInstalledOtherPatches")
    InstancesWithInstalledPendingRebootPatches = field(
        "InstancesWithInstalledPendingRebootPatches"
    )
    InstancesWithInstalledRejectedPatches = field(
        "InstancesWithInstalledRejectedPatches"
    )
    InstancesWithMissingPatches = field("InstancesWithMissingPatches")
    InstancesWithFailedPatches = field("InstancesWithFailedPatches")
    InstancesWithNotApplicablePatches = field("InstancesWithNotApplicablePatches")
    InstancesWithUnreportedNotApplicablePatches = field(
        "InstancesWithUnreportedNotApplicablePatches"
    )
    InstancesWithCriticalNonCompliantPatches = field(
        "InstancesWithCriticalNonCompliantPatches"
    )
    InstancesWithSecurityNonCompliantPatches = field(
        "InstancesWithSecurityNonCompliantPatches"
    )
    InstancesWithOtherNonCompliantPatches = field(
        "InstancesWithOtherNonCompliantPatches"
    )
    InstancesWithAvailableSecurityUpdates = field(
        "InstancesWithAvailableSecurityUpdates"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePatchGroupStateResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchGroupStateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchPropertiesResult:
    boto3_raw_data: "type_defs.DescribePatchPropertiesResultTypeDef" = (
        dataclasses.field()
    )

    Properties = field("Properties")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePatchPropertiesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchPropertiesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalendarStateResponse:
    boto3_raw_data: "type_defs.GetCalendarStateResponseTypeDef" = dataclasses.field()

    State = field("State")
    AtTime = field("AtTime")
    NextTransitionTime = field("NextTransitionTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCalendarStateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalendarStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionStatusResponse:
    boto3_raw_data: "type_defs.GetConnectionStatusResponseTypeDef" = dataclasses.field()

    Target = field("Target")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDefaultPatchBaselineResult:
    boto3_raw_data: "type_defs.GetDefaultPatchBaselineResultTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")
    OperatingSystem = field("OperatingSystem")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDefaultPatchBaselineResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDefaultPatchBaselineResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeployablePatchSnapshotForInstanceResult:
    boto3_raw_data: "type_defs.GetDeployablePatchSnapshotForInstanceResultTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    SnapshotId = field("SnapshotId")
    SnapshotDownloadUrl = field("SnapshotDownloadUrl")
    Product = field("Product")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeployablePatchSnapshotForInstanceResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeployablePatchSnapshotForInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowExecutionResult:
    boto3_raw_data: "type_defs.GetMaintenanceWindowExecutionResultTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")
    TaskIds = field("TaskIds")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMaintenanceWindowExecutionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowExecutionTaskInvocationResult:
    boto3_raw_data: (
        "type_defs.GetMaintenanceWindowExecutionTaskInvocationResultTypeDef"
    ) = dataclasses.field()

    WindowExecutionId = field("WindowExecutionId")
    TaskExecutionId = field("TaskExecutionId")
    InvocationId = field("InvocationId")
    ExecutionId = field("ExecutionId")
    TaskType = field("TaskType")
    Parameters = field("Parameters")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OwnerInformation = field("OwnerInformation")
    WindowTargetId = field("WindowTargetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMaintenanceWindowExecutionTaskInvocationResultTypeDef"
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
                "type_defs.GetMaintenanceWindowExecutionTaskInvocationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowResult:
    boto3_raw_data: "type_defs.GetMaintenanceWindowResultTypeDef" = dataclasses.field()

    WindowId = field("WindowId")
    Name = field("Name")
    Description = field("Description")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    Schedule = field("Schedule")
    ScheduleTimezone = field("ScheduleTimezone")
    ScheduleOffset = field("ScheduleOffset")
    NextExecutionTime = field("NextExecutionTime")
    Duration = field("Duration")
    Cutoff = field("Cutoff")
    AllowUnassociatedTargets = field("AllowUnassociatedTargets")
    Enabled = field("Enabled")
    CreatedDate = field("CreatedDate")
    ModifiedDate = field("ModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMaintenanceWindowResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPatchBaselineForPatchGroupResult:
    boto3_raw_data: "type_defs.GetPatchBaselineForPatchGroupResultTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")
    PatchGroup = field("PatchGroup")
    OperatingSystem = field("OperatingSystem")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPatchBaselineForPatchGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPatchBaselineForPatchGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LabelParameterVersionResult:
    boto3_raw_data: "type_defs.LabelParameterVersionResultTypeDef" = dataclasses.field()

    InvalidLabels = field("InvalidLabels")
    ParameterVersion = field("ParameterVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LabelParameterVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LabelParameterVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInventoryEntriesResult:
    boto3_raw_data: "type_defs.ListInventoryEntriesResultTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    InstanceId = field("InstanceId")
    SchemaVersion = field("SchemaVersion")
    CaptureTime = field("CaptureTime")
    Entries = field("Entries")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInventoryEntriesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInventoryEntriesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesSummaryResult:
    boto3_raw_data: "type_defs.ListNodesSummaryResultTypeDef" = dataclasses.field()

    Summary = field("Summary")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodesSummaryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesSummaryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResult:
    boto3_raw_data: "type_defs.ListTagsForResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInventoryResult:
    boto3_raw_data: "type_defs.PutInventoryResultTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInventoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInventoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutParameterResult:
    boto3_raw_data: "type_defs.PutParameterResultTypeDef" = dataclasses.field()

    Version = field("Version")
    Tier = field("Tier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutParameterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutParameterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    PolicyHash = field("PolicyHash")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDefaultPatchBaselineResult:
    boto3_raw_data: "type_defs.RegisterDefaultPatchBaselineResultTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterDefaultPatchBaselineResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDefaultPatchBaselineResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterPatchBaselineForPatchGroupResult:
    boto3_raw_data: "type_defs.RegisterPatchBaselineForPatchGroupResultTypeDef" = (
        dataclasses.field()
    )

    BaselineId = field("BaselineId")
    PatchGroup = field("PatchGroup")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterPatchBaselineForPatchGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterPatchBaselineForPatchGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTargetWithMaintenanceWindowResult:
    boto3_raw_data: "type_defs.RegisterTargetWithMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowTargetId = field("WindowTargetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterTargetWithMaintenanceWindowResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTargetWithMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTaskWithMaintenanceWindowResult:
    boto3_raw_data: "type_defs.RegisterTaskWithMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowTaskId = field("WindowTaskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterTaskWithMaintenanceWindowResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTaskWithMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeSessionResponse:
    boto3_raw_data: "type_defs.ResumeSessionResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    TokenValue = field("TokenValue")
    StreamUrl = field("StreamUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAccessRequestResponse:
    boto3_raw_data: "type_defs.StartAccessRequestResponseTypeDef" = dataclasses.field()

    AccessRequestId = field("AccessRequestId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAccessRequestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAccessRequestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAutomationExecutionResult:
    boto3_raw_data: "type_defs.StartAutomationExecutionResultTypeDef" = (
        dataclasses.field()
    )

    AutomationExecutionId = field("AutomationExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAutomationExecutionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAutomationExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChangeRequestExecutionResult:
    boto3_raw_data: "type_defs.StartChangeRequestExecutionResultTypeDef" = (
        dataclasses.field()
    )

    AutomationExecutionId = field("AutomationExecutionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartChangeRequestExecutionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChangeRequestExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExecutionPreviewResponse:
    boto3_raw_data: "type_defs.StartExecutionPreviewResponseTypeDef" = (
        dataclasses.field()
    )

    ExecutionPreviewId = field("ExecutionPreviewId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartExecutionPreviewResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExecutionPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSessionResponse:
    boto3_raw_data: "type_defs.StartSessionResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    TokenValue = field("TokenValue")
    StreamUrl = field("StreamUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateSessionResponse:
    boto3_raw_data: "type_defs.TerminateSessionResponseTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnlabelParameterVersionResult:
    boto3_raw_data: "type_defs.UnlabelParameterVersionResultTypeDef" = (
        dataclasses.field()
    )

    RemovedLabels = field("RemovedLabels")
    InvalidLabels = field("InvalidLabels")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnlabelParameterVersionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnlabelParameterVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceWindowResult:
    boto3_raw_data: "type_defs.UpdateMaintenanceWindowResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    Name = field("Name")
    Description = field("Description")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    Schedule = field("Schedule")
    ScheduleTimezone = field("ScheduleTimezone")
    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    Cutoff = field("Cutoff")
    AllowUnassociatedTargets = field("AllowUnassociatedTargets")
    Enabled = field("Enabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMaintenanceWindowResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceWindowResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpsMetadataResult:
    boto3_raw_data: "type_defs.UpdateOpsMetadataResultTypeDef" = dataclasses.field()

    OpsMetadataArn = field("OpsMetadataArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOpsMetadataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpsMetadataResultTypeDef"]
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

    Name = field("Name")
    InstanceId = field("InstanceId")
    AssociationId = field("AssociationId")
    AssociationVersion = field("AssociationVersion")
    DocumentVersion = field("DocumentVersion")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    LastExecutionDate = field("LastExecutionDate")

    @cached_property
    def Overview(self):  # pragma: no cover
        return AssociationOverview.make_one(self.boto3_raw_data["Overview"])

    ScheduleExpression = field("ScheduleExpression")
    AssociationName = field("AssociationName")
    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")

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
class MaintenanceWindowTarget:
    boto3_raw_data: "type_defs.MaintenanceWindowTargetTypeDef" = dataclasses.field()

    WindowId = field("WindowId")
    WindowTargetId = field("WindowTargetId")
    ResourceType = field("ResourceType")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    OwnerInformation = field("OwnerInformation")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceWindowTargetResult:
    boto3_raw_data: "type_defs.UpdateMaintenanceWindowTargetResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTargetId = field("WindowTargetId")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    OwnerInformation = field("OwnerInformation")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMaintenanceWindowTargetResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceWindowTargetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationExecutionsRequest:
    boto3_raw_data: "type_defs.DescribeAssociationExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AssociationExecutionFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssociationExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationExecutionTarget:
    boto3_raw_data: "type_defs.AssociationExecutionTargetTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    AssociationVersion = field("AssociationVersion")
    ExecutionId = field("ExecutionId")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    Status = field("Status")
    DetailedStatus = field("DetailedStatus")
    LastExecutionDate = field("LastExecutionDate")

    @cached_property
    def OutputSource(self):  # pragma: no cover
        return OutputSource.make_one(self.boto3_raw_data["OutputSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationExecutionTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationExecutionTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationExecutionTargetsRequest:
    boto3_raw_data: "type_defs.DescribeAssociationExecutionTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")
    ExecutionId = field("ExecutionId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AssociationExecutionTargetsFilter.make_many(
            self.boto3_raw_data["Filters"]
        )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssociationExecutionTargetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationExecutionTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationsRequest:
    boto3_raw_data: "type_defs.ListAssociationsRequestTypeDef" = dataclasses.field()

    @cached_property
    def AssociationFilterList(self):  # pragma: no cover
        return AssociationFilter.make_many(self.boto3_raw_data["AssociationFilterList"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationStatus:
    boto3_raw_data: "type_defs.AssociationStatusTypeDef" = dataclasses.field()

    Date = field("Date")
    Name = field("Name")
    Message = field("Message")
    AdditionalInfo = field("AdditionalInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociationStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceExecutionSummary:
    boto3_raw_data: "type_defs.ComplianceExecutionSummaryTypeDef" = dataclasses.field()

    ExecutionTime = field("ExecutionTime")
    ExecutionId = field("ExecutionId")
    ExecutionType = field("ExecutionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentRequest:
    boto3_raw_data: "type_defs.UpdateDocumentRequestTypeDef" = dataclasses.field()

    Content = field("Content")
    Name = field("Name")

    @cached_property
    def Attachments(self):  # pragma: no cover
        return AttachmentsSource.make_many(self.boto3_raw_data["Attachments"])

    DisplayName = field("DisplayName")
    VersionName = field("VersionName")
    DocumentVersion = field("DocumentVersion")
    DocumentFormat = field("DocumentFormat")
    TargetType = field("TargetType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutomationExecutionsRequest:
    boto3_raw_data: "type_defs.DescribeAutomationExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return AutomationExecutionFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutomationExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutomationExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationExecutionPreview:
    boto3_raw_data: "type_defs.AutomationExecutionPreviewTypeDef" = dataclasses.field()

    StepPreviews = field("StepPreviews")
    Regions = field("Regions")

    @cached_property
    def TargetPreviews(self):  # pragma: no cover
        return TargetPreview.make_many(self.boto3_raw_data["TargetPreviews"])

    TotalAccounts = field("TotalAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomationExecutionPreviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationExecutionPreviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowLambdaParameters:
    boto3_raw_data: "type_defs.MaintenanceWindowLambdaParametersTypeDef" = (
        dataclasses.field()
    )

    ClientContext = field("ClientContext")
    Qualifier = field("Qualifier")
    Payload = field("Payload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowLambdaParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowLambdaParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandInvocationResult:
    boto3_raw_data: "type_defs.GetCommandInvocationResultTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    Comment = field("Comment")
    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    PluginName = field("PluginName")
    ResponseCode = field("ResponseCode")
    ExecutionStartDateTime = field("ExecutionStartDateTime")
    ExecutionElapsedTime = field("ExecutionElapsedTime")
    ExecutionEndDateTime = field("ExecutionEndDateTime")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StandardOutputContent = field("StandardOutputContent")
    StandardOutputUrl = field("StandardOutputUrl")
    StandardErrorContent = field("StandardErrorContent")
    StandardErrorUrl = field("StandardErrorUrl")

    @cached_property
    def CloudWatchOutputConfig(self):  # pragma: no cover
        return CloudWatchOutputConfig.make_one(
            self.boto3_raw_data["CloudWatchOutputConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommandInvocationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandInvocationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandInvocationsRequest:
    boto3_raw_data: "type_defs.ListCommandInvocationsRequestTypeDef" = (
        dataclasses.field()
    )

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return CommandFilter.make_many(self.boto3_raw_data["Filters"])

    Details = field("Details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCommandInvocationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandInvocationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandsRequest:
    boto3_raw_data: "type_defs.ListCommandsRequestTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return CommandFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandInvocation:
    boto3_raw_data: "type_defs.CommandInvocationTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    InstanceName = field("InstanceName")
    Comment = field("Comment")
    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    RequestedDateTime = field("RequestedDateTime")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    TraceOutput = field("TraceOutput")
    StandardOutputUrl = field("StandardOutputUrl")
    StandardErrorUrl = field("StandardErrorUrl")

    @cached_property
    def CommandPlugins(self):  # pragma: no cover
        return CommandPlugin.make_many(self.boto3_raw_data["CommandPlugins"])

    ServiceRole = field("ServiceRole")

    @cached_property
    def NotificationConfig(self):  # pragma: no cover
        return NotificationConfigOutput.make_one(
            self.boto3_raw_data["NotificationConfig"]
        )

    @cached_property
    def CloudWatchOutputConfig(self):  # pragma: no cover
        return CloudWatchOutputConfig.make_one(
            self.boto3_raw_data["CloudWatchOutputConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandInvocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandInvocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowRunCommandParametersOutput:
    boto3_raw_data: "type_defs.MaintenanceWindowRunCommandParametersOutputTypeDef" = (
        dataclasses.field()
    )

    Comment = field("Comment")

    @cached_property
    def CloudWatchOutputConfig(self):  # pragma: no cover
        return CloudWatchOutputConfig.make_one(
            self.boto3_raw_data["CloudWatchOutputConfig"]
        )

    DocumentHash = field("DocumentHash")
    DocumentHashType = field("DocumentHashType")
    DocumentVersion = field("DocumentVersion")

    @cached_property
    def NotificationConfig(self):  # pragma: no cover
        return NotificationConfigOutput.make_one(
            self.boto3_raw_data["NotificationConfig"]
        )

    OutputS3BucketName = field("OutputS3BucketName")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")
    Parameters = field("Parameters")
    ServiceRoleArn = field("ServiceRoleArn")
    TimeoutSeconds = field("TimeoutSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowRunCommandParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowRunCommandParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceItem:
    boto3_raw_data: "type_defs.ComplianceItemTypeDef" = dataclasses.field()

    ComplianceType = field("ComplianceType")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    Id = field("Id")
    Title = field("Title")
    Status = field("Status")
    Severity = field("Severity")

    @cached_property
    def ExecutionSummary(self):  # pragma: no cover
        return ComplianceExecutionSummaryOutput.make_one(
            self.boto3_raw_data["ExecutionSummary"]
        )

    Details = field("Details")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComplianceItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComplianceItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceItemsRequest:
    boto3_raw_data: "type_defs.ListComplianceItemsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ComplianceStringFilter.make_many(self.boto3_raw_data["Filters"])

    ResourceIds = field("ResourceIds")
    ResourceTypes = field("ResourceTypes")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComplianceItemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceSummariesRequest:
    boto3_raw_data: "type_defs.ListComplianceSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ComplianceStringFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComplianceSummariesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceComplianceSummariesRequest:
    boto3_raw_data: "type_defs.ListResourceComplianceSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ComplianceStringFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceComplianceSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceComplianceSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompliantSummary:
    boto3_raw_data: "type_defs.CompliantSummaryTypeDef" = dataclasses.field()

    CompliantCount = field("CompliantCount")

    @cached_property
    def SeveritySummary(self):  # pragma: no cover
        return SeveritySummary.make_one(self.boto3_raw_data["SeveritySummary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompliantSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompliantSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NonCompliantSummary:
    boto3_raw_data: "type_defs.NonCompliantSummaryTypeDef" = dataclasses.field()

    NonCompliantCount = field("NonCompliantCount")

    @cached_property
    def SeveritySummary(self):  # pragma: no cover
        return SeveritySummary.make_one(self.boto3_raw_data["SeveritySummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NonCompliantSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NonCompliantSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateActivationRequest:
    boto3_raw_data: "type_defs.CreateActivationRequestTypeDef" = dataclasses.field()

    IamRole = field("IamRole")
    Description = field("Description")
    DefaultInstanceName = field("DefaultInstanceName")
    RegistrationLimit = field("RegistrationLimit")
    ExpirationDate = field("ExpirationDate")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def RegistrationMetadata(self):  # pragma: no cover
        return RegistrationMetadataItem.make_many(
            self.boto3_raw_data["RegistrationMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateActivationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateActivationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDocumentRequest:
    boto3_raw_data: "type_defs.CreateDocumentRequestTypeDef" = dataclasses.field()

    Content = field("Content")
    Name = field("Name")

    @cached_property
    def Requires(self):  # pragma: no cover
        return DocumentRequires.make_many(self.boto3_raw_data["Requires"])

    @cached_property
    def Attachments(self):  # pragma: no cover
        return AttachmentsSource.make_many(self.boto3_raw_data["Attachments"])

    DisplayName = field("DisplayName")
    VersionName = field("VersionName")
    DocumentType = field("DocumentType")
    DocumentFormat = field("DocumentFormat")
    TargetType = field("TargetType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentIdentifier:
    boto3_raw_data: "type_defs.DocumentIdentifierTypeDef" = dataclasses.field()

    Name = field("Name")
    CreatedDate = field("CreatedDate")
    DisplayName = field("DisplayName")
    Owner = field("Owner")
    VersionName = field("VersionName")
    PlatformTypes = field("PlatformTypes")
    DocumentVersion = field("DocumentVersion")
    DocumentType = field("DocumentType")
    SchemaVersion = field("SchemaVersion")
    DocumentFormat = field("DocumentFormat")
    TargetType = field("TargetType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def Requires(self):  # pragma: no cover
        return DocumentRequires.make_many(self.boto3_raw_data["Requires"])

    ReviewStatus = field("ReviewStatus")
    Author = field("Author")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentResult:
    boto3_raw_data: "type_defs.GetDocumentResultTypeDef" = dataclasses.field()

    Name = field("Name")
    CreatedDate = field("CreatedDate")
    DisplayName = field("DisplayName")
    VersionName = field("VersionName")
    DocumentVersion = field("DocumentVersion")
    Status = field("Status")
    StatusInformation = field("StatusInformation")
    Content = field("Content")
    DocumentType = field("DocumentType")
    DocumentFormat = field("DocumentFormat")

    @cached_property
    def Requires(self):  # pragma: no cover
        return DocumentRequires.make_many(self.boto3_raw_data["Requires"])

    @cached_property
    def AttachmentsContent(self):  # pragma: no cover
        return AttachmentContent.make_many(self.boto3_raw_data["AttachmentsContent"])

    ReviewStatus = field("ReviewStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDocumentResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemSummary:
    boto3_raw_data: "type_defs.OpsItemSummaryTypeDef" = dataclasses.field()

    CreatedBy = field("CreatedBy")
    CreatedTime = field("CreatedTime")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedTime = field("LastModifiedTime")
    Priority = field("Priority")
    Source = field("Source")
    Status = field("Status")
    OpsItemId = field("OpsItemId")
    Title = field("Title")
    OperationalData = field("OperationalData")
    Category = field("Category")
    Severity = field("Severity")
    OpsItemType = field("OpsItemType")
    ActualStartTime = field("ActualStartTime")
    ActualEndTime = field("ActualEndTime")
    PlannedStartTime = field("PlannedStartTime")
    PlannedEndTime = field("PlannedEndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsItemSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsItemSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpsItemRequest:
    boto3_raw_data: "type_defs.CreateOpsItemRequestTypeDef" = dataclasses.field()

    Description = field("Description")
    Source = field("Source")
    Title = field("Title")
    OpsItemType = field("OpsItemType")
    OperationalData = field("OperationalData")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return OpsItemNotification.make_many(self.boto3_raw_data["Notifications"])

    Priority = field("Priority")

    @cached_property
    def RelatedOpsItems(self):  # pragma: no cover
        return RelatedOpsItem.make_many(self.boto3_raw_data["RelatedOpsItems"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Category = field("Category")
    Severity = field("Severity")
    ActualStartTime = field("ActualStartTime")
    ActualEndTime = field("ActualEndTime")
    PlannedStartTime = field("PlannedStartTime")
    PlannedEndTime = field("PlannedEndTime")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOpsItemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpsItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItem:
    boto3_raw_data: "type_defs.OpsItemTypeDef" = dataclasses.field()

    CreatedBy = field("CreatedBy")
    OpsItemType = field("OpsItemType")
    CreatedTime = field("CreatedTime")
    Description = field("Description")
    LastModifiedBy = field("LastModifiedBy")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return OpsItemNotification.make_many(self.boto3_raw_data["Notifications"])

    Priority = field("Priority")

    @cached_property
    def RelatedOpsItems(self):  # pragma: no cover
        return RelatedOpsItem.make_many(self.boto3_raw_data["RelatedOpsItems"])

    Status = field("Status")
    OpsItemId = field("OpsItemId")
    Version = field("Version")
    Title = field("Title")
    Source = field("Source")
    OperationalData = field("OperationalData")
    Category = field("Category")
    Severity = field("Severity")
    ActualStartTime = field("ActualStartTime")
    ActualEndTime = field("ActualEndTime")
    PlannedStartTime = field("PlannedStartTime")
    PlannedEndTime = field("PlannedEndTime")
    OpsItemArn = field("OpsItemArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpsItemRequest:
    boto3_raw_data: "type_defs.UpdateOpsItemRequestTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")
    Description = field("Description")
    OperationalData = field("OperationalData")
    OperationalDataToDelete = field("OperationalDataToDelete")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return OpsItemNotification.make_many(self.boto3_raw_data["Notifications"])

    Priority = field("Priority")

    @cached_property
    def RelatedOpsItems(self):  # pragma: no cover
        return RelatedOpsItem.make_many(self.boto3_raw_data["RelatedOpsItems"])

    Status = field("Status")
    Title = field("Title")
    Category = field("Category")
    Severity = field("Severity")
    ActualStartTime = field("ActualStartTime")
    ActualEndTime = field("ActualEndTime")
    PlannedStartTime = field("PlannedStartTime")
    PlannedEndTime = field("PlannedEndTime")
    OpsItemArn = field("OpsItemArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOpsItemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpsItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpsMetadataRequest:
    boto3_raw_data: "type_defs.CreateOpsMetadataRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Metadata = field("Metadata")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOpsMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpsMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsMetadataResult:
    boto3_raw_data: "type_defs.GetOpsMetadataResultTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Metadata = field("Metadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpsMetadataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsMetadataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpsMetadataRequest:
    boto3_raw_data: "type_defs.UpdateOpsMetadataRequestTypeDef" = dataclasses.field()

    OpsMetadataArn = field("OpsMetadataArn")
    MetadataToUpdate = field("MetadataToUpdate")
    KeysToDelete = field("KeysToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOpsMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpsMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessTokenResponse:
    boto3_raw_data: "type_defs.GetAccessTokenResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    AccessRequestStatus = field("AccessRequestStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivationsRequest:
    boto3_raw_data: "type_defs.DescribeActivationsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeActivationsFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeActivationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeActivationsFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeActivationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationExecutionTargetsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAssociationExecutionTargetsRequestPaginateTypeDef"
    ) = dataclasses.field()

    AssociationId = field("AssociationId")
    ExecutionId = field("ExecutionId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AssociationExecutionTargetsFilter.make_many(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssociationExecutionTargetsRequestPaginateTypeDef"
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
                "type_defs.DescribeAssociationExecutionTargetsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAssociationExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AssociationExecutionFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssociationExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutomationExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAutomationExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return AutomationExecutionFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutomationExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutomationExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEffectiveInstanceAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef"
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
                "type_defs.DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEffectivePatchesForPatchBaselineRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef"
    ) = dataclasses.field()

    BaselineId = field("BaselineId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef"
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
                "type_defs.DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAssociationsStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeInstanceAssociationsStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceAssociationsStatusRequestPaginateTypeDef"
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
                "type_defs.DescribeInstanceAssociationsStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchStatesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeInstancePatchStatesRequestPaginateTypeDef" = (
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
            "type_defs.DescribeInstancePatchStatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePatchStatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInventoryDeletionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeInventoryDeletionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DeletionId = field("DeletionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInventoryDeletionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInventoryDeletionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchPropertiesRequestPaginate:
    boto3_raw_data: "type_defs.DescribePatchPropertiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OperatingSystem = field("OperatingSystem")
    Property = field("Property")
    PatchSet = field("PatchSet")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePatchPropertiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchPropertiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInventorySchemaRequestPaginate:
    boto3_raw_data: "type_defs.GetInventorySchemaRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TypeName = field("TypeName")
    Aggregator = field("Aggregator")
    SubType = field("SubType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInventorySchemaRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInventorySchemaRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParameterHistoryRequestPaginate:
    boto3_raw_data: "type_defs.GetParameterHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    WithDecryption = field("WithDecryption")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetParameterHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParameterHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.GetResourcePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourcePoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociationVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociationVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociationVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationFilterList(self):  # pragma: no cover
        return AssociationFilter.make_many(self.boto3_raw_data["AssociationFilterList"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssociationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandInvocationsRequestPaginate:
    boto3_raw_data: "type_defs.ListCommandInvocationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return CommandFilter.make_many(self.boto3_raw_data["Filters"])

    Details = field("Details")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommandInvocationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandInvocationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandsRequestPaginate:
    boto3_raw_data: "type_defs.ListCommandsRequestPaginateTypeDef" = dataclasses.field()

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return CommandFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceItemsRequestPaginate:
    boto3_raw_data: "type_defs.ListComplianceItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ComplianceStringFilter.make_many(self.boto3_raw_data["Filters"])

    ResourceIds = field("ResourceIds")
    ResourceTypes = field("ResourceTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComplianceItemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceSummariesRequestPaginate:
    boto3_raw_data: "type_defs.ListComplianceSummariesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ComplianceStringFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComplianceSummariesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceSummariesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDocumentVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceComplianceSummariesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListResourceComplianceSummariesRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ComplianceStringFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceComplianceSummariesRequestPaginateTypeDef"
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
                "type_defs.ListResourceComplianceSummariesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDataSyncRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceDataSyncRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SyncType = field("SyncType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceDataSyncRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDataSyncRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutomationStepExecutionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAutomationStepExecutionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    AutomationExecutionId = field("AutomationExecutionId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StepExecutionFilter.make_many(self.boto3_raw_data["Filters"])

    ReverseOrder = field("ReverseOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutomationStepExecutionsRequestPaginateTypeDef"
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
                "type_defs.DescribeAutomationStepExecutionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutomationStepExecutionsRequest:
    boto3_raw_data: "type_defs.DescribeAutomationStepExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    AutomationExecutionId = field("AutomationExecutionId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StepExecutionFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ReverseOrder = field("ReverseOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutomationStepExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutomationStepExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailablePatchesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAvailablePatchesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAvailablePatchesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailablePatchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailablePatchesRequest:
    boto3_raw_data: "type_defs.DescribeAvailablePatchesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAvailablePatchesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailablePatchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeInstancePatchesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePatchesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePatchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchesRequest:
    boto3_raw_data: "type_defs.DescribeInstancePatchesRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstancePatchesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePatchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchBaselinesRequestPaginate:
    boto3_raw_data: "type_defs.DescribePatchBaselinesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePatchBaselinesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchBaselinesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchBaselinesRequest:
    boto3_raw_data: "type_defs.DescribePatchBaselinesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePatchBaselinesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchBaselinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribePatchGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePatchGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchGroupsRequest:
    boto3_raw_data: "type_defs.DescribePatchGroupsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePatchGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailablePatchesResult:
    boto3_raw_data: "type_defs.DescribeAvailablePatchesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Patches(self):  # pragma: no cover
        return Patch.make_many(self.boto3_raw_data["Patches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAvailablePatchesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailablePatchesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEffectiveInstanceAssociationsResult:
    boto3_raw_data: "type_defs.DescribeEffectiveInstanceAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return InstanceAssociation.make_many(self.boto3_raw_data["Associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEffectiveInstanceAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEffectiveInstanceAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceInformationRequestPaginate:
    boto3_raw_data: "type_defs.DescribeInstanceInformationRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceInformationFilterList(self):  # pragma: no cover
        return InstanceInformationFilter.make_many(
            self.boto3_raw_data["InstanceInformationFilterList"]
        )

    @cached_property
    def Filters(self):  # pragma: no cover
        return InstanceInformationStringFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceInformationRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceInformationRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceInformationRequest:
    boto3_raw_data: "type_defs.DescribeInstanceInformationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceInformationFilterList(self):  # pragma: no cover
        return InstanceInformationFilter.make_many(
            self.boto3_raw_data["InstanceInformationFilterList"]
        )

    @cached_property
    def Filters(self):  # pragma: no cover
        return InstanceInformationStringFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceInformationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceInformationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchStatesForPatchGroupRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef"
    ) = dataclasses.field()

    PatchGroup = field("PatchGroup")

    @cached_property
    def Filters(self):  # pragma: no cover
        return InstancePatchStateFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef"
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
                "type_defs.DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchStatesForPatchGroupRequest:
    boto3_raw_data: (
        "type_defs.DescribeInstancePatchStatesForPatchGroupRequestTypeDef"
    ) = dataclasses.field()

    PatchGroup = field("PatchGroup")

    @cached_property
    def Filters(self):  # pragma: no cover
        return InstancePatchStateFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePatchStatesForPatchGroupRequestTypeDef"
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
                "type_defs.DescribeInstancePatchStatesForPatchGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchStatesForPatchGroupResult:
    boto3_raw_data: (
        "type_defs.DescribeInstancePatchStatesForPatchGroupResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def InstancePatchStates(self):  # pragma: no cover
        return InstancePatchState.make_many(self.boto3_raw_data["InstancePatchStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePatchStatesForPatchGroupResultTypeDef"
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
                "type_defs.DescribeInstancePatchStatesForPatchGroupResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchStatesResult:
    boto3_raw_data: "type_defs.DescribeInstancePatchStatesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstancePatchStates(self):  # pragma: no cover
        return InstancePatchState.make_many(self.boto3_raw_data["InstancePatchStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePatchStatesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePatchStatesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePatchesResult:
    boto3_raw_data: "type_defs.DescribeInstancePatchesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Patches(self):  # pragma: no cover
        return PatchComplianceData.make_many(self.boto3_raw_data["Patches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstancePatchesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePatchesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePropertiesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeInstancePropertiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstancePropertyFilterList(self):  # pragma: no cover
        return InstancePropertyFilter.make_many(
            self.boto3_raw_data["InstancePropertyFilterList"]
        )

    @cached_property
    def FiltersWithOperator(self):  # pragma: no cover
        return InstancePropertyStringFilter.make_many(
            self.boto3_raw_data["FiltersWithOperator"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePropertiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePropertiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePropertiesRequest:
    boto3_raw_data: "type_defs.DescribeInstancePropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstancePropertyFilterList(self):  # pragma: no cover
        return InstancePropertyFilter.make_many(
            self.boto3_raw_data["InstancePropertyFilterList"]
        )

    @cached_property
    def FiltersWithOperator(self):  # pragma: no cover
        return InstancePropertyStringFilter.make_many(
            self.boto3_raw_data["FiltersWithOperator"]
        )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstancePropertiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef" = (dataclasses.field())

    WindowExecutionId = field("WindowExecutionId")
    TaskId = field("TaskId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef"
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
                "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionTaskInvocationsRequest:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef"
    ) = dataclasses.field()

    WindowExecutionId = field("WindowExecutionId")
    TaskId = field("TaskId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef"
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
                "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionTasksRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef"
    ) = dataclasses.field()

    WindowExecutionId = field("WindowExecutionId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef"
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
                "type_defs.DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionTasksRequest:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowExecutionTasksRequestTypeDef"
    ) = dataclasses.field()

    WindowExecutionId = field("WindowExecutionId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionTasksRequestTypeDef"
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
                "type_defs.DescribeMaintenanceWindowExecutionTasksRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    WindowId = field("WindowId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef"
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
                "type_defs.DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionsRequest:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowTargetsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowTargetsRequestPaginateTypeDef"
    ) = dataclasses.field()

    WindowId = field("WindowId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowTargetsRequestPaginateTypeDef"
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
                "type_defs.DescribeMaintenanceWindowTargetsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowTargetsRequest:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowTargetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowTasksRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowTasksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowTasksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowTasksRequest:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowTasksRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowsRequest:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return MaintenanceWindowFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionTaskInvocationsResult:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def WindowExecutionTaskInvocationIdentities(self):  # pragma: no cover
        return MaintenanceWindowExecutionTaskInvocationIdentity.make_many(
            self.boto3_raw_data["WindowExecutionTaskInvocationIdentities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef"
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
                "type_defs.DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionsResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowExecutionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WindowExecutions(self):  # pragma: no cover
        return MaintenanceWindowExecution.make_many(
            self.boto3_raw_data["WindowExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowExecutionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowScheduleResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowScheduleResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduledWindowExecutions(self):  # pragma: no cover
        return ScheduledWindowExecution.make_many(
            self.boto3_raw_data["ScheduledWindowExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowScheduleResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowScheduleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowsForTargetResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowsForTargetResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WindowIdentities(self):  # pragma: no cover
        return MaintenanceWindowIdentityForTarget.make_many(
            self.boto3_raw_data["WindowIdentities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowsForTargetResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowsForTargetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowsResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WindowIdentities(self):  # pragma: no cover
        return MaintenanceWindowIdentity.make_many(
            self.boto3_raw_data["WindowIdentities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMaintenanceWindowsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOpsItemsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeOpsItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OpsItemFilters(self):  # pragma: no cover
        return OpsItemFilter.make_many(self.boto3_raw_data["OpsItemFilters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOpsItemsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOpsItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOpsItemsRequest:
    boto3_raw_data: "type_defs.DescribeOpsItemsRequestTypeDef" = dataclasses.field()

    @cached_property
    def OpsItemFilters(self):  # pragma: no cover
        return OpsItemFilter.make_many(self.boto3_raw_data["OpsItemFilters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOpsItemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOpsItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersByPathRequestPaginate:
    boto3_raw_data: "type_defs.GetParametersByPathRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Path = field("Path")
    Recursive = field("Recursive")

    @cached_property
    def ParameterFilters(self):  # pragma: no cover
        return ParameterStringFilter.make_many(self.boto3_raw_data["ParameterFilters"])

    WithDecryption = field("WithDecryption")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetParametersByPathRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersByPathRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersByPathRequest:
    boto3_raw_data: "type_defs.GetParametersByPathRequestTypeDef" = dataclasses.field()

    Path = field("Path")
    Recursive = field("Recursive")

    @cached_property
    def ParameterFilters(self):  # pragma: no cover
        return ParameterStringFilter.make_many(self.boto3_raw_data["ParameterFilters"])

    WithDecryption = field("WithDecryption")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersByPathRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersByPathRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParametersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeParametersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ParametersFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def ParameterFilters(self):  # pragma: no cover
        return ParameterStringFilter.make_many(self.boto3_raw_data["ParameterFilters"])

    Shared = field("Shared")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeParametersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParametersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParametersRequest:
    boto3_raw_data: "type_defs.DescribeParametersRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ParametersFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def ParameterFilters(self):  # pragma: no cover
        return ParameterStringFilter.make_many(self.boto3_raw_data["ParameterFilters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Shared = field("Shared")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeParametersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchBaselinesResult:
    boto3_raw_data: "type_defs.DescribePatchBaselinesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BaselineIdentities(self):  # pragma: no cover
        return PatchBaselineIdentity.make_many(
            self.boto3_raw_data["BaselineIdentities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePatchBaselinesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchBaselinesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchGroupPatchBaselineMapping:
    boto3_raw_data: "type_defs.PatchGroupPatchBaselineMappingTypeDef" = (
        dataclasses.field()
    )

    PatchGroup = field("PatchGroup")

    @cached_property
    def BaselineIdentity(self):  # pragma: no cover
        return PatchBaselineIdentity.make_one(self.boto3_raw_data["BaselineIdentity"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PatchGroupPatchBaselineMappingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchGroupPatchBaselineMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSessionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSessionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SessionFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSessionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSessionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSessionsRequest:
    boto3_raw_data: "type_defs.DescribeSessionsRequestTypeDef" = dataclasses.field()

    State = field("State")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return SessionFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentDefaultVersionResult:
    boto3_raw_data: "type_defs.UpdateDocumentDefaultVersionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Description(self):  # pragma: no cover
        return DocumentDefaultVersionDescription.make_one(
            self.boto3_raw_data["Description"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDocumentDefaultVersionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentDefaultVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentDescription:
    boto3_raw_data: "type_defs.DocumentDescriptionTypeDef" = dataclasses.field()

    Sha1 = field("Sha1")
    Hash = field("Hash")
    HashType = field("HashType")
    Name = field("Name")
    DisplayName = field("DisplayName")
    VersionName = field("VersionName")
    Owner = field("Owner")
    CreatedDate = field("CreatedDate")
    Status = field("Status")
    StatusInformation = field("StatusInformation")
    DocumentVersion = field("DocumentVersion")
    Description = field("Description")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return DocumentParameter.make_many(self.boto3_raw_data["Parameters"])

    PlatformTypes = field("PlatformTypes")
    DocumentType = field("DocumentType")
    SchemaVersion = field("SchemaVersion")
    LatestVersion = field("LatestVersion")
    DefaultVersion = field("DefaultVersion")
    DocumentFormat = field("DocumentFormat")
    TargetType = field("TargetType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def AttachmentsInformation(self):  # pragma: no cover
        return AttachmentInformation.make_many(
            self.boto3_raw_data["AttachmentsInformation"]
        )

    @cached_property
    def Requires(self):  # pragma: no cover
        return DocumentRequires.make_many(self.boto3_raw_data["Requires"])

    Author = field("Author")

    @cached_property
    def ReviewInformation(self):  # pragma: no cover
        return ReviewInformation.make_many(self.boto3_raw_data["ReviewInformation"])

    ApprovedVersion = field("ApprovedVersion")
    PendingReviewVersion = field("PendingReviewVersion")
    ReviewStatus = field("ReviewStatus")
    Category = field("Category")
    CategoryEnum = field("CategoryEnum")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentsRequestPaginate:
    boto3_raw_data: "type_defs.ListDocumentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentFilterList(self):  # pragma: no cover
        return DocumentFilter.make_many(self.boto3_raw_data["DocumentFilterList"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return DocumentKeyValuesFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentsRequest:
    boto3_raw_data: "type_defs.ListDocumentsRequestTypeDef" = dataclasses.field()

    @cached_property
    def DocumentFilterList(self):  # pragma: no cover
        return DocumentFilter.make_many(self.boto3_raw_data["DocumentFilterList"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return DocumentKeyValuesFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentReviewerResponseSource:
    boto3_raw_data: "type_defs.DocumentReviewerResponseSourceTypeDef" = (
        dataclasses.field()
    )

    CreateTime = field("CreateTime")
    UpdatedTime = field("UpdatedTime")
    ReviewStatus = field("ReviewStatus")

    @cached_property
    def Comment(self):  # pragma: no cover
        return DocumentReviewCommentSource.make_many(self.boto3_raw_data["Comment"])

    Reviewer = field("Reviewer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DocumentReviewerResponseSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentReviewerResponseSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentReviews:
    boto3_raw_data: "type_defs.DocumentReviewsTypeDef" = dataclasses.field()

    Action = field("Action")

    @cached_property
    def Comment(self):  # pragma: no cover
        return DocumentReviewCommentSource.make_many(self.boto3_raw_data["Comment"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentReviewsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentReviewsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentVersionsResult:
    boto3_raw_data: "type_defs.ListDocumentVersionsResultTypeDef" = dataclasses.field()

    @cached_property
    def DocumentVersions(self):  # pragma: no cover
        return DocumentVersionInfo.make_many(self.boto3_raw_data["DocumentVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectivePatch:
    boto3_raw_data: "type_defs.EffectivePatchTypeDef" = dataclasses.field()

    @cached_property
    def Patch(self):  # pragma: no cover
        return Patch.make_one(self.boto3_raw_data["Patch"])

    @cached_property
    def PatchStatus(self):  # pragma: no cover
        return PatchStatus.make_one(self.boto3_raw_data["PatchStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EffectivePatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EffectivePatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandInvocationRequestWait:
    boto3_raw_data: "type_defs.GetCommandInvocationRequestWaitTypeDef" = (
        dataclasses.field()
    )

    CommandId = field("CommandId")
    InstanceId = field("InstanceId")
    PluginName = field("PluginName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCommandInvocationRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandInvocationRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryGroup:
    boto3_raw_data: "type_defs.InventoryGroupTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Filters(self):  # pragma: no cover
        return InventoryFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InventoryGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInventoryEntriesRequest:
    boto3_raw_data: "type_defs.ListInventoryEntriesRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    TypeName = field("TypeName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return InventoryFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInventoryEntriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInventoryEntriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsAggregatorPaginator:
    boto3_raw_data: "type_defs.OpsAggregatorPaginatorTypeDef" = dataclasses.field()

    AggregatorType = field("AggregatorType")
    TypeName = field("TypeName")
    AttributeName = field("AttributeName")
    Values = field("Values")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsFilter.make_many(self.boto3_raw_data["Filters"])

    Aggregators = field("Aggregators")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsAggregatorPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsAggregatorPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsAggregator:
    boto3_raw_data: "type_defs.OpsAggregatorTypeDef" = dataclasses.field()

    AggregatorType = field("AggregatorType")
    TypeName = field("TypeName")
    AttributeName = field("AttributeName")
    Values = field("Values")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsFilter.make_many(self.boto3_raw_data["Filters"])

    Aggregators = field("Aggregators")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsAggregatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsAggregatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParameterResult:
    boto3_raw_data: "type_defs.GetParameterResultTypeDef" = dataclasses.field()

    @cached_property
    def Parameter(self):  # pragma: no cover
        return Parameter.make_one(self.boto3_raw_data["Parameter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParameterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParameterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersByPathResult:
    boto3_raw_data: "type_defs.GetParametersByPathResultTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersByPathResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersByPathResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersResult:
    boto3_raw_data: "type_defs.GetParametersResultTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    InvalidParameters = field("InvalidParameters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParametersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePoliciesResponse:
    boto3_raw_data: "type_defs.GetResourcePoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policies(self):  # pragma: no cover
        return GetResourcePoliciesResponseEntry.make_many(
            self.boto3_raw_data["Policies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceSettingResult:
    boto3_raw_data: "type_defs.GetServiceSettingResultTypeDef" = dataclasses.field()

    @cached_property
    def ServiceSetting(self):  # pragma: no cover
        return ServiceSetting.make_one(self.boto3_raw_data["ServiceSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceSettingResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceSettingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetServiceSettingResult:
    boto3_raw_data: "type_defs.ResetServiceSettingResultTypeDef" = dataclasses.field()

    @cached_property
    def ServiceSetting(self):  # pragma: no cover
        return ServiceSetting.make_one(self.boto3_raw_data["ServiceSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetServiceSettingResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetServiceSettingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceInformation:
    boto3_raw_data: "type_defs.InstanceInformationTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    PingStatus = field("PingStatus")
    LastPingDateTime = field("LastPingDateTime")
    AgentVersion = field("AgentVersion")
    IsLatestVersion = field("IsLatestVersion")
    PlatformType = field("PlatformType")
    PlatformName = field("PlatformName")
    PlatformVersion = field("PlatformVersion")
    ActivationId = field("ActivationId")
    IamRole = field("IamRole")
    RegistrationDate = field("RegistrationDate")
    ResourceType = field("ResourceType")
    Name = field("Name")
    IPAddress = field("IPAddress")
    ComputerName = field("ComputerName")
    AssociationStatus = field("AssociationStatus")
    LastAssociationExecutionDate = field("LastAssociationExecutionDate")
    LastSuccessfulAssociationExecutionDate = field(
        "LastSuccessfulAssociationExecutionDate"
    )

    @cached_property
    def AssociationOverview(self):  # pragma: no cover
        return InstanceAggregatedAssociationOverview.make_one(
            self.boto3_raw_data["AssociationOverview"]
        )

    SourceId = field("SourceId")
    SourceType = field("SourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceProperty:
    boto3_raw_data: "type_defs.InstancePropertyTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceId = field("InstanceId")
    InstanceType = field("InstanceType")
    InstanceRole = field("InstanceRole")
    KeyName = field("KeyName")
    InstanceState = field("InstanceState")
    Architecture = field("Architecture")
    IPAddress = field("IPAddress")
    LaunchTime = field("LaunchTime")
    PingStatus = field("PingStatus")
    LastPingDateTime = field("LastPingDateTime")
    AgentVersion = field("AgentVersion")
    PlatformType = field("PlatformType")
    PlatformName = field("PlatformName")
    PlatformVersion = field("PlatformVersion")
    ActivationId = field("ActivationId")
    IamRole = field("IamRole")
    RegistrationDate = field("RegistrationDate")
    ResourceType = field("ResourceType")
    ComputerName = field("ComputerName")
    AssociationStatus = field("AssociationStatus")
    LastAssociationExecutionDate = field("LastAssociationExecutionDate")
    LastSuccessfulAssociationExecutionDate = field(
        "LastSuccessfulAssociationExecutionDate"
    )

    @cached_property
    def AssociationOverview(self):  # pragma: no cover
        return InstanceAggregatedAssociationOverview.make_one(
            self.boto3_raw_data["AssociationOverview"]
        )

    SourceId = field("SourceId")
    SourceType = field("SourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstancePropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAssociationOutputLocation:
    boto3_raw_data: "type_defs.InstanceAssociationOutputLocationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Location(self):  # pragma: no cover
        return S3OutputLocation.make_one(self.boto3_raw_data["S3Location"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceAssociationOutputLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAssociationOutputLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAssociationOutputUrl:
    boto3_raw_data: "type_defs.InstanceAssociationOutputUrlTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3OutputUrl(self):  # pragma: no cover
        return S3OutputUrl.make_one(self.boto3_raw_data["S3OutputUrl"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceAssociationOutputUrlTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAssociationOutputUrlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeType:
    boto3_raw_data: "type_defs.NodeTypeTypeDef" = dataclasses.field()

    @cached_property
    def Instance(self):  # pragma: no cover
        return InstanceInfo.make_one(self.boto3_raw_data["Instance"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryDeletionSummary:
    boto3_raw_data: "type_defs.InventoryDeletionSummaryTypeDef" = dataclasses.field()

    TotalCount = field("TotalCount")
    RemainingCount = field("RemainingCount")

    @cached_property
    def SummaryItems(self):  # pragma: no cover
        return InventoryDeletionSummaryItem.make_many(
            self.boto3_raw_data["SummaryItems"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryDeletionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryDeletionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryItemSchema:
    boto3_raw_data: "type_defs.InventoryItemSchemaTypeDef" = dataclasses.field()

    TypeName = field("TypeName")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return InventoryItemAttribute.make_many(self.boto3_raw_data["Attributes"])

    Version = field("Version")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryItemSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryItemSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInventoryRequest:
    boto3_raw_data: "type_defs.PutInventoryRequestTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @cached_property
    def Items(self):  # pragma: no cover
        return InventoryItem.make_many(self.boto3_raw_data["Items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInventoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInventoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryResultEntity:
    boto3_raw_data: "type_defs.InventoryResultEntityTypeDef" = dataclasses.field()

    Id = field("Id")
    Data = field("Data")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryResultEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryResultEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesRequestPaginate:
    boto3_raw_data: "type_defs.ListNodesRequestPaginateTypeDef" = dataclasses.field()

    SyncName = field("SyncName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return NodeFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesRequest:
    boto3_raw_data: "type_defs.ListNodesRequestTypeDef" = dataclasses.field()

    SyncName = field("SyncName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return NodeFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesSummaryRequestPaginate:
    boto3_raw_data: "type_defs.ListNodesSummaryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Aggregators(self):  # pragma: no cover
        return NodeAggregatorPaginator.make_many(self.boto3_raw_data["Aggregators"])

    SyncName = field("SyncName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return NodeFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNodesSummaryRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesSummaryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesSummaryRequest:
    boto3_raw_data: "type_defs.ListNodesSummaryRequestTypeDef" = dataclasses.field()

    @cached_property
    def Aggregators(self):  # pragma: no cover
        return NodeAggregator.make_many(self.boto3_raw_data["Aggregators"])

    SyncName = field("SyncName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return NodeFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodesSummaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsItemEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListOpsItemEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsItemEventFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOpsItemEventsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsItemEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsItemEventsRequest:
    boto3_raw_data: "type_defs.ListOpsItemEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsItemEventFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpsItemEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsItemEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsItemRelatedItemsRequestPaginate:
    boto3_raw_data: "type_defs.ListOpsItemRelatedItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OpsItemId = field("OpsItemId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsItemRelatedItemsFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOpsItemRelatedItemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsItemRelatedItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsItemRelatedItemsRequest:
    boto3_raw_data: "type_defs.ListOpsItemRelatedItemsRequestTypeDef" = (
        dataclasses.field()
    )

    OpsItemId = field("OpsItemId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsItemRelatedItemsFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOpsItemRelatedItemsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsItemRelatedItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsMetadataRequestPaginate:
    boto3_raw_data: "type_defs.ListOpsMetadataRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsMetadataFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOpsMetadataRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsMetadataRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsMetadataRequest:
    boto3_raw_data: "type_defs.ListOpsMetadataRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsMetadataFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpsMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsMetadataResult:
    boto3_raw_data: "type_defs.ListOpsMetadataResultTypeDef" = dataclasses.field()

    @cached_property
    def OpsMetadataList(self):  # pragma: no cover
        return OpsMetadata.make_many(self.boto3_raw_data["OpsMetadataList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpsMetadataResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsMetadataResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowRunCommandParameters:
    boto3_raw_data: "type_defs.MaintenanceWindowRunCommandParametersTypeDef" = (
        dataclasses.field()
    )

    Comment = field("Comment")

    @cached_property
    def CloudWatchOutputConfig(self):  # pragma: no cover
        return CloudWatchOutputConfig.make_one(
            self.boto3_raw_data["CloudWatchOutputConfig"]
        )

    DocumentHash = field("DocumentHash")
    DocumentHashType = field("DocumentHashType")
    DocumentVersion = field("DocumentVersion")

    @cached_property
    def NotificationConfig(self):  # pragma: no cover
        return NotificationConfig.make_one(self.boto3_raw_data["NotificationConfig"])

    OutputS3BucketName = field("OutputS3BucketName")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")
    Parameters = field("Parameters")
    ServiceRoleArn = field("ServiceRoleArn")
    TimeoutSeconds = field("TimeoutSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowRunCommandParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowRunCommandParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsEntity:
    boto3_raw_data: "type_defs.OpsEntityTypeDef" = dataclasses.field()

    Id = field("Id")
    Data = field("Data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpsEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpsEntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemEventSummary:
    boto3_raw_data: "type_defs.OpsItemEventSummaryTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")
    EventId = field("EventId")
    Source = field("Source")
    DetailType = field("DetailType")
    Detail = field("Detail")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return OpsItemIdentity.make_one(self.boto3_raw_data["CreatedBy"])

    CreatedTime = field("CreatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsItemEventSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsItemEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpsItemRelatedItemSummary:
    boto3_raw_data: "type_defs.OpsItemRelatedItemSummaryTypeDef" = dataclasses.field()

    OpsItemId = field("OpsItemId")
    AssociationId = field("AssociationId")
    ResourceType = field("ResourceType")
    AssociationType = field("AssociationType")
    ResourceUri = field("ResourceUri")

    @cached_property
    def CreatedBy(self):  # pragma: no cover
        return OpsItemIdentity.make_one(self.boto3_raw_data["CreatedBy"])

    CreatedTime = field("CreatedTime")

    @cached_property
    def LastModifiedBy(self):  # pragma: no cover
        return OpsItemIdentity.make_one(self.boto3_raw_data["LastModifiedBy"])

    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpsItemRelatedItemSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpsItemRelatedItemSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterHistory:
    boto3_raw_data: "type_defs.ParameterHistoryTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    KeyId = field("KeyId")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedUser = field("LastModifiedUser")
    Description = field("Description")
    Value = field("Value")
    AllowedPattern = field("AllowedPattern")
    Version = field("Version")
    Labels = field("Labels")
    Tier = field("Tier")

    @cached_property
    def Policies(self):  # pragma: no cover
        return ParameterInlinePolicy.make_many(self.boto3_raw_data["Policies"])

    DataType = field("DataType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterHistoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterMetadata:
    boto3_raw_data: "type_defs.ParameterMetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    ARN = field("ARN")
    Type = field("Type")
    KeyId = field("KeyId")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedUser = field("LastModifiedUser")
    Description = field("Description")
    AllowedPattern = field("AllowedPattern")
    Version = field("Version")
    Tier = field("Tier")

    @cached_property
    def Policies(self):  # pragma: no cover
        return ParameterInlinePolicy.make_many(self.boto3_raw_data["Policies"])

    DataType = field("DataType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchFilterGroupOutput:
    boto3_raw_data: "type_defs.PatchFilterGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def PatchFilters(self):  # pragma: no cover
        return PatchFilterOutput.make_many(self.boto3_raw_data["PatchFilters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatchFilterGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchFilterGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncAwsOrganizationsSourceOutput:
    boto3_raw_data: "type_defs.ResourceDataSyncAwsOrganizationsSourceOutputTypeDef" = (
        dataclasses.field()
    )

    OrganizationSourceType = field("OrganizationSourceType")

    @cached_property
    def OrganizationalUnits(self):  # pragma: no cover
        return ResourceDataSyncOrganizationalUnit.make_many(
            self.boto3_raw_data["OrganizationalUnits"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceDataSyncAwsOrganizationsSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncAwsOrganizationsSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncAwsOrganizationsSource:
    boto3_raw_data: "type_defs.ResourceDataSyncAwsOrganizationsSourceTypeDef" = (
        dataclasses.field()
    )

    OrganizationSourceType = field("OrganizationSourceType")

    @cached_property
    def OrganizationalUnits(self):  # pragma: no cover
        return ResourceDataSyncOrganizationalUnit.make_many(
            self.boto3_raw_data["OrganizationalUnits"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourceDataSyncAwsOrganizationsSourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncAwsOrganizationsSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncS3Destination:
    boto3_raw_data: "type_defs.ResourceDataSyncS3DestinationTypeDef" = (
        dataclasses.field()
    )

    BucketName = field("BucketName")
    SyncFormat = field("SyncFormat")
    Region = field("Region")
    Prefix = field("Prefix")
    AWSKMSKeyARN = field("AWSKMSKeyARN")

    @cached_property
    def DestinationDataSharing(self):  # pragma: no cover
        return ResourceDataSyncDestinationDataSharing.make_one(
            self.boto3_raw_data["DestinationDataSharing"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResourceDataSyncS3DestinationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncS3DestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    Target = field("Target")
    Status = field("Status")
    StartDate = field("StartDate")
    EndDate = field("EndDate")
    DocumentName = field("DocumentName")
    Owner = field("Owner")
    Reason = field("Reason")
    Details = field("Details")

    @cached_property
    def OutputUrl(self):  # pragma: no cover
        return SessionManagerOutputUrl.make_one(self.boto3_raw_data["OutputUrl"])

    MaxSessionDuration = field("MaxSessionDuration")
    AccessType = field("AccessType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivationsResult:
    boto3_raw_data: "type_defs.DescribeActivationsResultTypeDef" = dataclasses.field()

    @cached_property
    def ActivationList(self):  # pragma: no cover
        return Activation.make_many(self.boto3_raw_data["ActivationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationExecution:
    boto3_raw_data: "type_defs.AssociationExecutionTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    AssociationVersion = field("AssociationVersion")
    ExecutionId = field("ExecutionId")
    Status = field("Status")
    DetailedStatus = field("DetailedStatus")
    CreatedTime = field("CreatedTime")
    LastExecutionDate = field("LastExecutionDate")
    ResourceCountByStatus = field("ResourceCountByStatus")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationExecutionTypeDef"]
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

    CommandId = field("CommandId")
    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    Comment = field("Comment")
    ExpiresAfter = field("ExpiresAfter")
    Parameters = field("Parameters")
    InstanceIds = field("InstanceIds")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    RequestedDateTime = field("RequestedDateTime")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    OutputS3Region = field("OutputS3Region")
    OutputS3BucketName = field("OutputS3BucketName")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    TargetCount = field("TargetCount")
    CompletedCount = field("CompletedCount")
    ErrorCount = field("ErrorCount")
    DeliveryTimedOutCount = field("DeliveryTimedOutCount")
    ServiceRole = field("ServiceRole")

    @cached_property
    def NotificationConfig(self):  # pragma: no cover
        return NotificationConfigOutput.make_one(
            self.boto3_raw_data["NotificationConfig"]
        )

    @cached_property
    def CloudWatchOutputConfig(self):  # pragma: no cover
        return CloudWatchOutputConfig.make_one(
            self.boto3_raw_data["CloudWatchOutputConfig"]
        )

    TimeoutSeconds = field("TimeoutSeconds")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

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
class GetMaintenanceWindowExecutionTaskResult:
    boto3_raw_data: "type_defs.GetMaintenanceWindowExecutionTaskResultTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")
    TaskExecutionId = field("TaskExecutionId")
    TaskArn = field("TaskArn")
    ServiceRole = field("ServiceRole")
    Type = field("Type")
    TaskParameters = field("TaskParameters")
    Priority = field("Priority")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMaintenanceWindowExecutionTaskResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowExecutionTaskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowExecutionTaskIdentity:
    boto3_raw_data: "type_defs.MaintenanceWindowExecutionTaskIdentityTypeDef" = (
        dataclasses.field()
    )

    WindowExecutionId = field("WindowExecutionId")
    TaskExecutionId = field("TaskExecutionId")
    Status = field("Status")
    StatusDetails = field("StatusDetails")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    TaskArn = field("TaskArn")
    TaskType = field("TaskType")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowExecutionTaskIdentityTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowExecutionTaskIdentityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowTask:
    boto3_raw_data: "type_defs.MaintenanceWindowTaskTypeDef" = dataclasses.field()

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")
    TaskArn = field("TaskArn")
    Type = field("Type")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TaskParameters = field("TaskParameters")
    Priority = field("Priority")

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    ServiceRoleArn = field("ServiceRoleArn")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    Name = field("Name")
    Description = field("Description")
    CutoffBehavior = field("CutoffBehavior")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetLocationOutput:
    boto3_raw_data: "type_defs.TargetLocationOutputTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    Regions = field("Regions")
    TargetLocationMaxConcurrency = field("TargetLocationMaxConcurrency")
    TargetLocationMaxErrors = field("TargetLocationMaxErrors")
    ExecutionRoleName = field("ExecutionRoleName")

    @cached_property
    def TargetLocationAlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["TargetLocationAlarmConfiguration"]
        )

    IncludeChildOrganizationUnits = field("IncludeChildOrganizationUnits")
    ExcludeAccounts = field("ExcludeAccounts")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TargetsMaxConcurrency = field("TargetsMaxConcurrency")
    TargetsMaxErrors = field("TargetsMaxErrors")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetLocationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetLocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationsResult:
    boto3_raw_data: "type_defs.ListAssociationsResultTypeDef" = dataclasses.field()

    @cached_property
    def Associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["Associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowTargetsResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowTargetsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Targets(self):  # pragma: no cover
        return MaintenanceWindowTarget.make_many(self.boto3_raw_data["Targets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowTargetsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowTargetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationExecutionTargetsResult:
    boto3_raw_data: "type_defs.DescribeAssociationExecutionTargetsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationExecutionTargets(self):  # pragma: no cover
        return AssociationExecutionTarget.make_many(
            self.boto3_raw_data["AssociationExecutionTargets"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssociationExecutionTargetsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationExecutionTargetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionPreview:
    boto3_raw_data: "type_defs.ExecutionPreviewTypeDef" = dataclasses.field()

    @cached_property
    def Automation(self):  # pragma: no cover
        return AutomationExecutionPreview.make_one(self.boto3_raw_data["Automation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionPreviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionPreviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandInvocationsResult:
    boto3_raw_data: "type_defs.ListCommandInvocationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CommandInvocations(self):  # pragma: no cover
        return CommandInvocation.make_many(self.boto3_raw_data["CommandInvocations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandInvocationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandInvocationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowTaskInvocationParametersOutput:
    boto3_raw_data: (
        "type_defs.MaintenanceWindowTaskInvocationParametersOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def RunCommand(self):  # pragma: no cover
        return MaintenanceWindowRunCommandParametersOutput.make_one(
            self.boto3_raw_data["RunCommand"]
        )

    @cached_property
    def Automation(self):  # pragma: no cover
        return MaintenanceWindowAutomationParametersOutput.make_one(
            self.boto3_raw_data["Automation"]
        )

    @cached_property
    def StepFunctions(self):  # pragma: no cover
        return MaintenanceWindowStepFunctionsParameters.make_one(
            self.boto3_raw_data["StepFunctions"]
        )

    @cached_property
    def Lambda(self):  # pragma: no cover
        return MaintenanceWindowLambdaParametersOutput.make_one(
            self.boto3_raw_data["Lambda"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowTaskInvocationParametersOutputTypeDef"
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
                "type_defs.MaintenanceWindowTaskInvocationParametersOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceItemsResult:
    boto3_raw_data: "type_defs.ListComplianceItemsResultTypeDef" = dataclasses.field()

    @cached_property
    def ComplianceItems(self):  # pragma: no cover
        return ComplianceItem.make_many(self.boto3_raw_data["ComplianceItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComplianceItemsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceItemsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceSummaryItem:
    boto3_raw_data: "type_defs.ComplianceSummaryItemTypeDef" = dataclasses.field()

    ComplianceType = field("ComplianceType")

    @cached_property
    def CompliantSummary(self):  # pragma: no cover
        return CompliantSummary.make_one(self.boto3_raw_data["CompliantSummary"])

    @cached_property
    def NonCompliantSummary(self):  # pragma: no cover
        return NonCompliantSummary.make_one(self.boto3_raw_data["NonCompliantSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceSummaryItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceSummaryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceComplianceSummaryItem:
    boto3_raw_data: "type_defs.ResourceComplianceSummaryItemTypeDef" = (
        dataclasses.field()
    )

    ComplianceType = field("ComplianceType")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    Status = field("Status")
    OverallSeverity = field("OverallSeverity")

    @cached_property
    def ExecutionSummary(self):  # pragma: no cover
        return ComplianceExecutionSummaryOutput.make_one(
            self.boto3_raw_data["ExecutionSummary"]
        )

    @cached_property
    def CompliantSummary(self):  # pragma: no cover
        return CompliantSummary.make_one(self.boto3_raw_data["CompliantSummary"])

    @cached_property
    def NonCompliantSummary(self):  # pragma: no cover
        return NonCompliantSummary.make_one(self.boto3_raw_data["NonCompliantSummary"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResourceComplianceSummaryItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceComplianceSummaryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentsResult:
    boto3_raw_data: "type_defs.ListDocumentsResultTypeDef" = dataclasses.field()

    @cached_property
    def DocumentIdentifiers(self):  # pragma: no cover
        return DocumentIdentifier.make_many(self.boto3_raw_data["DocumentIdentifiers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDocumentsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOpsItemsResponse:
    boto3_raw_data: "type_defs.DescribeOpsItemsResponseTypeDef" = dataclasses.field()

    @cached_property
    def OpsItemSummaries(self):  # pragma: no cover
        return OpsItemSummary.make_many(self.boto3_raw_data["OpsItemSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOpsItemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOpsItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsItemResponse:
    boto3_raw_data: "type_defs.GetOpsItemResponseTypeDef" = dataclasses.field()

    @cached_property
    def OpsItem(self):  # pragma: no cover
        return OpsItem.make_one(self.boto3_raw_data["OpsItem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpsItemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePatchGroupsResult:
    boto3_raw_data: "type_defs.DescribePatchGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def Mappings(self):  # pragma: no cover
        return PatchGroupPatchBaselineMapping.make_many(self.boto3_raw_data["Mappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePatchGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePatchGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDocumentResult:
    boto3_raw_data: "type_defs.CreateDocumentResultTypeDef" = dataclasses.field()

    @cached_property
    def DocumentDescription(self):  # pragma: no cover
        return DocumentDescription.make_one(self.boto3_raw_data["DocumentDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDocumentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDocumentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDocumentResult:
    boto3_raw_data: "type_defs.DescribeDocumentResultTypeDef" = dataclasses.field()

    @cached_property
    def Document(self):  # pragma: no cover
        return DocumentDescription.make_one(self.boto3_raw_data["Document"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDocumentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDocumentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentResult:
    boto3_raw_data: "type_defs.UpdateDocumentResultTypeDef" = dataclasses.field()

    @cached_property
    def DocumentDescription(self):  # pragma: no cover
        return DocumentDescription.make_one(self.boto3_raw_data["DocumentDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDocumentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadataResponseInfo:
    boto3_raw_data: "type_defs.DocumentMetadataResponseInfoTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReviewerResponse(self):  # pragma: no cover
        return DocumentReviewerResponseSource.make_many(
            self.boto3_raw_data["ReviewerResponse"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentMetadataResponseInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataResponseInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentMetadataRequest:
    boto3_raw_data: "type_defs.UpdateDocumentMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def DocumentReviews(self):  # pragma: no cover
        return DocumentReviews.make_one(self.boto3_raw_data["DocumentReviews"])

    DocumentVersion = field("DocumentVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDocumentMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEffectivePatchesForPatchBaselineResult:
    boto3_raw_data: (
        "type_defs.DescribeEffectivePatchesForPatchBaselineResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def EffectivePatches(self):  # pragma: no cover
        return EffectivePatch.make_many(self.boto3_raw_data["EffectivePatches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEffectivePatchesForPatchBaselineResultTypeDef"
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
                "type_defs.DescribeEffectivePatchesForPatchBaselineResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryAggregatorPaginator:
    boto3_raw_data: "type_defs.InventoryAggregatorPaginatorTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    Aggregators = field("Aggregators")

    @cached_property
    def Groups(self):  # pragma: no cover
        return InventoryGroup.make_many(self.boto3_raw_data["Groups"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryAggregatorPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryAggregatorPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryAggregator:
    boto3_raw_data: "type_defs.InventoryAggregatorTypeDef" = dataclasses.field()

    Expression = field("Expression")
    Aggregators = field("Aggregators")

    @cached_property
    def Groups(self):  # pragma: no cover
        return InventoryGroup.make_many(self.boto3_raw_data["Groups"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryAggregatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryAggregatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsSummaryRequestPaginate:
    boto3_raw_data: "type_defs.GetOpsSummaryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SyncName = field("SyncName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def Aggregators(self):  # pragma: no cover
        return OpsAggregatorPaginator.make_many(self.boto3_raw_data["Aggregators"])

    @cached_property
    def ResultAttributes(self):  # pragma: no cover
        return OpsResultAttribute.make_many(self.boto3_raw_data["ResultAttributes"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpsSummaryRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsSummaryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsSummaryRequest:
    boto3_raw_data: "type_defs.GetOpsSummaryRequestTypeDef" = dataclasses.field()

    SyncName = field("SyncName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OpsFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def Aggregators(self):  # pragma: no cover
        return OpsAggregator.make_many(self.boto3_raw_data["Aggregators"])

    @cached_property
    def ResultAttributes(self):  # pragma: no cover
        return OpsResultAttribute.make_many(self.boto3_raw_data["ResultAttributes"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpsSummaryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceInformationResult:
    boto3_raw_data: "type_defs.DescribeInstanceInformationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceInformationList(self):  # pragma: no cover
        return InstanceInformation.make_many(
            self.boto3_raw_data["InstanceInformationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceInformationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceInformationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancePropertiesResult:
    boto3_raw_data: "type_defs.DescribeInstancePropertiesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProperties(self):  # pragma: no cover
        return InstanceProperty.make_many(self.boto3_raw_data["InstanceProperties"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstancePropertiesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancePropertiesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAssociationStatusInfo:
    boto3_raw_data: "type_defs.InstanceAssociationStatusInfoTypeDef" = (
        dataclasses.field()
    )

    AssociationId = field("AssociationId")
    Name = field("Name")
    DocumentVersion = field("DocumentVersion")
    AssociationVersion = field("AssociationVersion")
    InstanceId = field("InstanceId")
    ExecutionDate = field("ExecutionDate")
    Status = field("Status")
    DetailedStatus = field("DetailedStatus")
    ExecutionSummary = field("ExecutionSummary")
    ErrorCode = field("ErrorCode")

    @cached_property
    def OutputUrl(self):  # pragma: no cover
        return InstanceAssociationOutputUrl.make_one(self.boto3_raw_data["OutputUrl"])

    AssociationName = field("AssociationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InstanceAssociationStatusInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAssociationStatusInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Node:
    boto3_raw_data: "type_defs.NodeTypeDef" = dataclasses.field()

    CaptureTime = field("CaptureTime")
    Id = field("Id")

    @cached_property
    def Owner(self):  # pragma: no cover
        return NodeOwnerInfo.make_one(self.boto3_raw_data["Owner"])

    Region = field("Region")

    @cached_property
    def NodeType(self):  # pragma: no cover
        return NodeType.make_one(self.boto3_raw_data["NodeType"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInventoryResult:
    boto3_raw_data: "type_defs.DeleteInventoryResultTypeDef" = dataclasses.field()

    DeletionId = field("DeletionId")
    TypeName = field("TypeName")

    @cached_property
    def DeletionSummary(self):  # pragma: no cover
        return InventoryDeletionSummary.make_one(self.boto3_raw_data["DeletionSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInventoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInventoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryDeletionStatusItem:
    boto3_raw_data: "type_defs.InventoryDeletionStatusItemTypeDef" = dataclasses.field()

    DeletionId = field("DeletionId")
    TypeName = field("TypeName")
    DeletionStartTime = field("DeletionStartTime")
    LastStatus = field("LastStatus")
    LastStatusMessage = field("LastStatusMessage")

    @cached_property
    def DeletionSummary(self):  # pragma: no cover
        return InventoryDeletionSummary.make_one(self.boto3_raw_data["DeletionSummary"])

    LastStatusUpdateTime = field("LastStatusUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryDeletionStatusItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryDeletionStatusItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInventorySchemaResult:
    boto3_raw_data: "type_defs.GetInventorySchemaResultTypeDef" = dataclasses.field()

    @cached_property
    def Schemas(self):  # pragma: no cover
        return InventoryItemSchema.make_many(self.boto3_raw_data["Schemas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInventorySchemaResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInventorySchemaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInventoryResult:
    boto3_raw_data: "type_defs.GetInventoryResultTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return InventoryResultEntity.make_many(self.boto3_raw_data["Entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInventoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInventoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindowTaskInvocationParameters:
    boto3_raw_data: "type_defs.MaintenanceWindowTaskInvocationParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RunCommand(self):  # pragma: no cover
        return MaintenanceWindowRunCommandParameters.make_one(
            self.boto3_raw_data["RunCommand"]
        )

    @cached_property
    def Automation(self):  # pragma: no cover
        return MaintenanceWindowAutomationParameters.make_one(
            self.boto3_raw_data["Automation"]
        )

    @cached_property
    def StepFunctions(self):  # pragma: no cover
        return MaintenanceWindowStepFunctionsParameters.make_one(
            self.boto3_raw_data["StepFunctions"]
        )

    @cached_property
    def Lambda(self):  # pragma: no cover
        return MaintenanceWindowLambdaParameters.make_one(self.boto3_raw_data["Lambda"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MaintenanceWindowTaskInvocationParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowTaskInvocationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpsSummaryResult:
    boto3_raw_data: "type_defs.GetOpsSummaryResultTypeDef" = dataclasses.field()

    @cached_property
    def Entities(self):  # pragma: no cover
        return OpsEntity.make_many(self.boto3_raw_data["Entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpsSummaryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpsSummaryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsItemEventsResponse:
    boto3_raw_data: "type_defs.ListOpsItemEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Summaries(self):  # pragma: no cover
        return OpsItemEventSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpsItemEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsItemEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpsItemRelatedItemsResponse:
    boto3_raw_data: "type_defs.ListOpsItemRelatedItemsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summaries(self):  # pragma: no cover
        return OpsItemRelatedItemSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOpsItemRelatedItemsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpsItemRelatedItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParameterHistoryResult:
    boto3_raw_data: "type_defs.GetParameterHistoryResultTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterHistory.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetParameterHistoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParameterHistoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeParametersResult:
    boto3_raw_data: "type_defs.DescribeParametersResultTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterMetadata.make_many(self.boto3_raw_data["Parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeParametersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchRuleOutput:
    boto3_raw_data: "type_defs.PatchRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def PatchFilterGroup(self):  # pragma: no cover
        return PatchFilterGroupOutput.make_one(self.boto3_raw_data["PatchFilterGroup"])

    ComplianceLevel = field("ComplianceLevel")
    ApproveAfterDays = field("ApproveAfterDays")
    ApproveUntilDate = field("ApproveUntilDate")
    EnableNonSecurity = field("EnableNonSecurity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchRuleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchFilterGroup:
    boto3_raw_data: "type_defs.PatchFilterGroupTypeDef" = dataclasses.field()

    PatchFilters = field("PatchFilters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchFilterGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchFilterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncSourceWithState:
    boto3_raw_data: "type_defs.ResourceDataSyncSourceWithStateTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")

    @cached_property
    def AwsOrganizationsSource(self):  # pragma: no cover
        return ResourceDataSyncAwsOrganizationsSourceOutput.make_one(
            self.boto3_raw_data["AwsOrganizationsSource"]
        )

    SourceRegions = field("SourceRegions")
    IncludeFutureRegions = field("IncludeFutureRegions")
    State = field("State")
    EnableAllOpsDataSources = field("EnableAllOpsDataSources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResourceDataSyncSourceWithStateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncSourceWithStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSessionsResponse:
    boto3_raw_data: "type_defs.DescribeSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Sessions(self):  # pragma: no cover
        return Session.make_many(self.boto3_raw_data["Sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowScheduleRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowScheduleRequestPaginateTypeDef"
    ) = dataclasses.field()

    WindowId = field("WindowId")
    Targets = field("Targets")
    ResourceType = field("ResourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowScheduleRequestPaginateTypeDef"
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
                "type_defs.DescribeMaintenanceWindowScheduleRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowScheduleRequest:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowScheduleRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    Targets = field("Targets")
    ResourceType = field("ResourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PatchOrchestratorFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowScheduleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowScheduleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowsForTargetRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef"
    ) = dataclasses.field()

    Targets = field("Targets")
    ResourceType = field("ResourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef"
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
                "type_defs.DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowsForTargetRequest:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowsForTargetRequestTypeDef" = (
        dataclasses.field()
    )

    Targets = field("Targets")
    ResourceType = field("ResourceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowsForTargetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowsForTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTargetWithMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.RegisterTargetWithMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    ResourceType = field("ResourceType")
    Targets = field("Targets")
    OwnerInformation = field("OwnerInformation")
    Name = field("Name")
    Description = field("Description")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterTargetWithMaintenanceWindowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTargetWithMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAccessRequestRequest:
    boto3_raw_data: "type_defs.StartAccessRequestRequestTypeDef" = dataclasses.field()

    Reason = field("Reason")
    Targets = field("Targets")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAccessRequestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAccessRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceWindowTargetRequest:
    boto3_raw_data: "type_defs.UpdateMaintenanceWindowTargetRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTargetId = field("WindowTargetId")
    Targets = field("Targets")
    OwnerInformation = field("OwnerInformation")
    Name = field("Name")
    Description = field("Description")
    Replace = field("Replace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMaintenanceWindowTargetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceWindowTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationExecutionsResult:
    boto3_raw_data: "type_defs.DescribeAssociationExecutionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationExecutions(self):  # pragma: no cover
        return AssociationExecution.make_many(
            self.boto3_raw_data["AssociationExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAssociationExecutionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationExecutionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandsResult:
    boto3_raw_data: "type_defs.ListCommandsResultTypeDef" = dataclasses.field()

    @cached_property
    def Commands(self):  # pragma: no cover
        return Command.make_many(self.boto3_raw_data["Commands"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCommandResult:
    boto3_raw_data: "type_defs.SendCommandResultTypeDef" = dataclasses.field()

    @cached_property
    def Command(self):  # pragma: no cover
        return Command.make_one(self.boto3_raw_data["Command"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendCommandResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCommandResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowExecutionTasksResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowExecutionTasksResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WindowExecutionTaskIdentities(self):  # pragma: no cover
        return MaintenanceWindowExecutionTaskIdentity.make_many(
            self.boto3_raw_data["WindowExecutionTaskIdentities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowExecutionTasksResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowExecutionTasksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMaintenanceWindowTasksResult:
    boto3_raw_data: "type_defs.DescribeMaintenanceWindowTasksResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tasks(self):  # pragma: no cover
        return MaintenanceWindowTask.make_many(self.boto3_raw_data["Tasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMaintenanceWindowTasksResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMaintenanceWindowTasksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationDescription:
    boto3_raw_data: "type_defs.AssociationDescriptionTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceId = field("InstanceId")
    AssociationVersion = field("AssociationVersion")
    Date = field("Date")
    LastUpdateAssociationDate = field("LastUpdateAssociationDate")

    @cached_property
    def Status(self):  # pragma: no cover
        return AssociationStatusOutput.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def Overview(self):  # pragma: no cover
        return AssociationOverview.make_one(self.boto3_raw_data["Overview"])

    DocumentVersion = field("DocumentVersion")
    AutomationTargetParameterName = field("AutomationTargetParameterName")
    Parameters = field("Parameters")
    AssociationId = field("AssociationId")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    ScheduleExpression = field("ScheduleExpression")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return InstanceAssociationOutputLocation.make_one(
            self.boto3_raw_data["OutputLocation"]
        )

    LastExecutionDate = field("LastExecutionDate")
    LastSuccessfulExecutionDate = field("LastSuccessfulExecutionDate")
    AssociationName = field("AssociationName")
    MaxErrors = field("MaxErrors")
    MaxConcurrency = field("MaxConcurrency")
    ComplianceSeverity = field("ComplianceSeverity")
    SyncCompliance = field("SyncCompliance")
    ApplyOnlyAtCronInterval = field("ApplyOnlyAtCronInterval")
    CalendarNames = field("CalendarNames")

    @cached_property
    def TargetLocations(self):  # pragma: no cover
        return TargetLocationOutput.make_many(self.boto3_raw_data["TargetLocations"])

    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationVersionInfo:
    boto3_raw_data: "type_defs.AssociationVersionInfoTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    AssociationVersion = field("AssociationVersion")
    CreatedDate = field("CreatedDate")
    Name = field("Name")
    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    ScheduleExpression = field("ScheduleExpression")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return InstanceAssociationOutputLocation.make_one(
            self.boto3_raw_data["OutputLocation"]
        )

    AssociationName = field("AssociationName")
    MaxErrors = field("MaxErrors")
    MaxConcurrency = field("MaxConcurrency")
    ComplianceSeverity = field("ComplianceSeverity")
    SyncCompliance = field("SyncCompliance")
    ApplyOnlyAtCronInterval = field("ApplyOnlyAtCronInterval")
    CalendarNames = field("CalendarNames")

    @cached_property
    def TargetLocations(self):  # pragma: no cover
        return TargetLocationOutput.make_many(self.boto3_raw_data["TargetLocations"])

    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationVersionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationVersionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssociationBatchRequestEntryOutput:
    boto3_raw_data: "type_defs.CreateAssociationBatchRequestEntryOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    InstanceId = field("InstanceId")
    Parameters = field("Parameters")
    AutomationTargetParameterName = field("AutomationTargetParameterName")
    DocumentVersion = field("DocumentVersion")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    ScheduleExpression = field("ScheduleExpression")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return InstanceAssociationOutputLocation.make_one(
            self.boto3_raw_data["OutputLocation"]
        )

    AssociationName = field("AssociationName")
    MaxErrors = field("MaxErrors")
    MaxConcurrency = field("MaxConcurrency")
    ComplianceSeverity = field("ComplianceSeverity")
    SyncCompliance = field("SyncCompliance")
    ApplyOnlyAtCronInterval = field("ApplyOnlyAtCronInterval")
    CalendarNames = field("CalendarNames")

    @cached_property
    def TargetLocations(self):  # pragma: no cover
        return TargetLocationOutput.make_many(self.boto3_raw_data["TargetLocations"])

    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssociationBatchRequestEntryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssociationBatchRequestEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunbookOutput:
    boto3_raw_data: "type_defs.RunbookOutputTypeDef" = dataclasses.field()

    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")
    TargetParameterName = field("TargetParameterName")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TargetMaps = field("TargetMaps")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")

    @cached_property
    def TargetLocations(self):  # pragma: no cover
        return TargetLocationOutput.make_many(self.boto3_raw_data["TargetLocations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunbookOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunbookOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepExecution:
    boto3_raw_data: "type_defs.StepExecutionTypeDef" = dataclasses.field()

    StepName = field("StepName")
    Action = field("Action")
    TimeoutSeconds = field("TimeoutSeconds")
    OnFailure = field("OnFailure")
    MaxAttempts = field("MaxAttempts")
    ExecutionStartTime = field("ExecutionStartTime")
    ExecutionEndTime = field("ExecutionEndTime")
    StepStatus = field("StepStatus")
    ResponseCode = field("ResponseCode")
    Inputs = field("Inputs")
    Outputs = field("Outputs")
    Response = field("Response")
    FailureMessage = field("FailureMessage")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    StepExecutionId = field("StepExecutionId")
    OverriddenParameters = field("OverriddenParameters")
    IsEnd = field("IsEnd")
    NextStep = field("NextStep")
    IsCritical = field("IsCritical")
    ValidNextSteps = field("ValidNextSteps")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    @cached_property
    def TargetLocation(self):  # pragma: no cover
        return TargetLocationOutput.make_one(self.boto3_raw_data["TargetLocation"])

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    @cached_property
    def ParentStepDetails(self):  # pragma: no cover
        return ParentStepDetails.make_one(self.boto3_raw_data["ParentStepDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCommandRequest:
    boto3_raw_data: "type_defs.SendCommandRequestTypeDef" = dataclasses.field()

    DocumentName = field("DocumentName")
    InstanceIds = field("InstanceIds")
    Targets = field("Targets")
    DocumentVersion = field("DocumentVersion")
    DocumentHash = field("DocumentHash")
    DocumentHashType = field("DocumentHashType")
    TimeoutSeconds = field("TimeoutSeconds")
    Comment = field("Comment")
    Parameters = field("Parameters")
    OutputS3Region = field("OutputS3Region")
    OutputS3BucketName = field("OutputS3BucketName")
    OutputS3KeyPrefix = field("OutputS3KeyPrefix")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    ServiceRoleArn = field("ServiceRoleArn")
    NotificationConfig = field("NotificationConfig")

    @cached_property
    def CloudWatchOutputConfig(self):  # pragma: no cover
        return CloudWatchOutputConfig.make_one(
            self.boto3_raw_data["CloudWatchOutputConfig"]
        )

    AlarmConfiguration = field("AlarmConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetLocation:
    boto3_raw_data: "type_defs.TargetLocationTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    Regions = field("Regions")
    TargetLocationMaxConcurrency = field("TargetLocationMaxConcurrency")
    TargetLocationMaxErrors = field("TargetLocationMaxErrors")
    ExecutionRoleName = field("ExecutionRoleName")
    TargetLocationAlarmConfiguration = field("TargetLocationAlarmConfiguration")
    IncludeChildOrganizationUnits = field("IncludeChildOrganizationUnits")
    ExcludeAccounts = field("ExcludeAccounts")
    Targets = field("Targets")
    TargetsMaxConcurrency = field("TargetsMaxConcurrency")
    TargetsMaxErrors = field("TargetsMaxErrors")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssociationStatusRequest:
    boto3_raw_data: "type_defs.UpdateAssociationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    InstanceId = field("InstanceId")
    AssociationStatus = field("AssociationStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssociationStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssociationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutComplianceItemsRequest:
    boto3_raw_data: "type_defs.PutComplianceItemsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    ComplianceType = field("ComplianceType")
    ExecutionSummary = field("ExecutionSummary")

    @cached_property
    def Items(self):  # pragma: no cover
        return ComplianceItemEntry.make_many(self.boto3_raw_data["Items"])

    ItemContentHash = field("ItemContentHash")
    UploadType = field("UploadType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutComplianceItemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutComplianceItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionPreviewResponse:
    boto3_raw_data: "type_defs.GetExecutionPreviewResponseTypeDef" = dataclasses.field()

    ExecutionPreviewId = field("ExecutionPreviewId")
    EndedAt = field("EndedAt")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ExecutionPreview(self):  # pragma: no cover
        return ExecutionPreview.make_one(self.boto3_raw_data["ExecutionPreview"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExecutionPreviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMaintenanceWindowTaskResult:
    boto3_raw_data: "type_defs.GetMaintenanceWindowTaskResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TaskArn = field("TaskArn")
    ServiceRoleArn = field("ServiceRoleArn")
    TaskType = field("TaskType")
    TaskParameters = field("TaskParameters")

    @cached_property
    def TaskInvocationParameters(self):  # pragma: no cover
        return MaintenanceWindowTaskInvocationParametersOutput.make_one(
            self.boto3_raw_data["TaskInvocationParameters"]
        )

    Priority = field("Priority")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    Name = field("Name")
    Description = field("Description")
    CutoffBehavior = field("CutoffBehavior")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMaintenanceWindowTaskResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMaintenanceWindowTaskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceWindowTaskResult:
    boto3_raw_data: "type_defs.UpdateMaintenanceWindowTaskResultTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TaskArn = field("TaskArn")
    ServiceRoleArn = field("ServiceRoleArn")
    TaskParameters = field("TaskParameters")

    @cached_property
    def TaskInvocationParameters(self):  # pragma: no cover
        return MaintenanceWindowTaskInvocationParametersOutput.make_one(
            self.boto3_raw_data["TaskInvocationParameters"]
        )

    Priority = field("Priority")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    Name = field("Name")
    Description = field("Description")
    CutoffBehavior = field("CutoffBehavior")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMaintenanceWindowTaskResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceWindowTaskResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceSummariesResult:
    boto3_raw_data: "type_defs.ListComplianceSummariesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComplianceSummaryItems(self):  # pragma: no cover
        return ComplianceSummaryItem.make_many(
            self.boto3_raw_data["ComplianceSummaryItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComplianceSummariesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceSummariesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceComplianceSummariesResult:
    boto3_raw_data: "type_defs.ListResourceComplianceSummariesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceComplianceSummaryItems(self):  # pragma: no cover
        return ResourceComplianceSummaryItem.make_many(
            self.boto3_raw_data["ResourceComplianceSummaryItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceComplianceSummariesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceComplianceSummariesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDocumentMetadataHistoryResponse:
    boto3_raw_data: "type_defs.ListDocumentMetadataHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DocumentVersion = field("DocumentVersion")
    Author = field("Author")

    @cached_property
    def Metadata(self):  # pragma: no cover
        return DocumentMetadataResponseInfo.make_one(self.boto3_raw_data["Metadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDocumentMetadataHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDocumentMetadataHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInventoryRequestPaginate:
    boto3_raw_data: "type_defs.GetInventoryRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return InventoryFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def Aggregators(self):  # pragma: no cover
        return InventoryAggregatorPaginator.make_many(
            self.boto3_raw_data["Aggregators"]
        )

    @cached_property
    def ResultAttributes(self):  # pragma: no cover
        return ResultAttribute.make_many(self.boto3_raw_data["ResultAttributes"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInventoryRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInventoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInventoryRequest:
    boto3_raw_data: "type_defs.GetInventoryRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return InventoryFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def Aggregators(self):  # pragma: no cover
        return InventoryAggregator.make_many(self.boto3_raw_data["Aggregators"])

    @cached_property
    def ResultAttributes(self):  # pragma: no cover
        return ResultAttribute.make_many(self.boto3_raw_data["ResultAttributes"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInventoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInventoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAssociationsStatusResult:
    boto3_raw_data: "type_defs.DescribeInstanceAssociationsStatusResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceAssociationStatusInfos(self):  # pragma: no cover
        return InstanceAssociationStatusInfo.make_many(
            self.boto3_raw_data["InstanceAssociationStatusInfos"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceAssociationsStatusResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceAssociationsStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesResult:
    boto3_raw_data: "type_defs.ListNodesResultTypeDef" = dataclasses.field()

    @cached_property
    def Nodes(self):  # pragma: no cover
        return Node.make_many(self.boto3_raw_data["Nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListNodesResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInventoryDeletionsResult:
    boto3_raw_data: "type_defs.DescribeInventoryDeletionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InventoryDeletions(self):  # pragma: no cover
        return InventoryDeletionStatusItem.make_many(
            self.boto3_raw_data["InventoryDeletions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInventoryDeletionsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInventoryDeletionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchRuleGroupOutput:
    boto3_raw_data: "type_defs.PatchRuleGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def PatchRules(self):  # pragma: no cover
        return PatchRuleOutput.make_many(self.boto3_raw_data["PatchRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatchRuleGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatchRuleGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncItem:
    boto3_raw_data: "type_defs.ResourceDataSyncItemTypeDef" = dataclasses.field()

    SyncName = field("SyncName")
    SyncType = field("SyncType")

    @cached_property
    def SyncSource(self):  # pragma: no cover
        return ResourceDataSyncSourceWithState.make_one(
            self.boto3_raw_data["SyncSource"]
        )

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return ResourceDataSyncS3Destination.make_one(
            self.boto3_raw_data["S3Destination"]
        )

    LastSyncTime = field("LastSyncTime")
    LastSuccessfulSyncTime = field("LastSuccessfulSyncTime")
    SyncLastModifiedTime = field("SyncLastModifiedTime")
    LastStatus = field("LastStatus")
    SyncCreatedTime = field("SyncCreatedTime")
    LastSyncStatusMessage = field("LastSyncStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDataSyncItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDataSyncSource:
    boto3_raw_data: "type_defs.ResourceDataSyncSourceTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    SourceRegions = field("SourceRegions")
    AwsOrganizationsSource = field("AwsOrganizationsSource")
    IncludeFutureRegions = field("IncludeFutureRegions")
    EnableAllOpsDataSources = field("EnableAllOpsDataSources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDataSyncSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDataSyncSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssociationResult:
    boto3_raw_data: "type_defs.CreateAssociationResultTypeDef" = dataclasses.field()

    @cached_property
    def AssociationDescription(self):  # pragma: no cover
        return AssociationDescription.make_one(
            self.boto3_raw_data["AssociationDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssociationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssociationResult:
    boto3_raw_data: "type_defs.DescribeAssociationResultTypeDef" = dataclasses.field()

    @cached_property
    def AssociationDescription(self):  # pragma: no cover
        return AssociationDescription.make_one(
            self.boto3_raw_data["AssociationDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssociationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssociationResult:
    boto3_raw_data: "type_defs.UpdateAssociationResultTypeDef" = dataclasses.field()

    @cached_property
    def AssociationDescription(self):  # pragma: no cover
        return AssociationDescription.make_one(
            self.boto3_raw_data["AssociationDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssociationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssociationStatusResult:
    boto3_raw_data: "type_defs.UpdateAssociationStatusResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationDescription(self):  # pragma: no cover
        return AssociationDescription.make_one(
            self.boto3_raw_data["AssociationDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssociationStatusResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssociationStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociationVersionsResult:
    boto3_raw_data: "type_defs.ListAssociationVersionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationVersions(self):  # pragma: no cover
        return AssociationVersionInfo.make_many(
            self.boto3_raw_data["AssociationVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssociationVersionsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociationVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedCreateAssociation:
    boto3_raw_data: "type_defs.FailedCreateAssociationTypeDef" = dataclasses.field()

    @cached_property
    def Entry(self):  # pragma: no cover
        return CreateAssociationBatchRequestEntryOutput.make_one(
            self.boto3_raw_data["Entry"]
        )

    Message = field("Message")
    Fault = field("Fault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedCreateAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedCreateAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationExecutionMetadata:
    boto3_raw_data: "type_defs.AutomationExecutionMetadataTypeDef" = dataclasses.field()

    AutomationExecutionId = field("AutomationExecutionId")
    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    AutomationExecutionStatus = field("AutomationExecutionStatus")
    ExecutionStartTime = field("ExecutionStartTime")
    ExecutionEndTime = field("ExecutionEndTime")
    ExecutedBy = field("ExecutedBy")
    LogFile = field("LogFile")
    Outputs = field("Outputs")
    Mode = field("Mode")
    ParentAutomationExecutionId = field("ParentAutomationExecutionId")
    CurrentStepName = field("CurrentStepName")
    CurrentAction = field("CurrentAction")
    FailureMessage = field("FailureMessage")
    TargetParameterName = field("TargetParameterName")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TargetMaps = field("TargetMaps")

    @cached_property
    def ResolvedTargets(self):  # pragma: no cover
        return ResolvedTargets.make_one(self.boto3_raw_data["ResolvedTargets"])

    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    Target = field("Target")
    AutomationType = field("AutomationType")

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    TargetLocationsURL = field("TargetLocationsURL")
    AutomationSubtype = field("AutomationSubtype")
    ScheduledTime = field("ScheduledTime")

    @cached_property
    def Runbooks(self):  # pragma: no cover
        return RunbookOutput.make_many(self.boto3_raw_data["Runbooks"])

    OpsItemId = field("OpsItemId")
    AssociationId = field("AssociationId")
    ChangeRequestName = field("ChangeRequestName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomationExecutionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationExecutionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationExecution:
    boto3_raw_data: "type_defs.AutomationExecutionTypeDef" = dataclasses.field()

    AutomationExecutionId = field("AutomationExecutionId")
    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    ExecutionStartTime = field("ExecutionStartTime")
    ExecutionEndTime = field("ExecutionEndTime")
    AutomationExecutionStatus = field("AutomationExecutionStatus")

    @cached_property
    def StepExecutions(self):  # pragma: no cover
        return StepExecution.make_many(self.boto3_raw_data["StepExecutions"])

    StepExecutionsTruncated = field("StepExecutionsTruncated")
    Parameters = field("Parameters")
    Outputs = field("Outputs")
    FailureMessage = field("FailureMessage")
    Mode = field("Mode")
    ParentAutomationExecutionId = field("ParentAutomationExecutionId")
    ExecutedBy = field("ExecutedBy")
    CurrentStepName = field("CurrentStepName")
    CurrentAction = field("CurrentAction")
    TargetParameterName = field("TargetParameterName")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    TargetMaps = field("TargetMaps")

    @cached_property
    def ResolvedTargets(self):  # pragma: no cover
        return ResolvedTargets.make_one(self.boto3_raw_data["ResolvedTargets"])

    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    Target = field("Target")

    @cached_property
    def TargetLocations(self):  # pragma: no cover
        return TargetLocationOutput.make_many(self.boto3_raw_data["TargetLocations"])

    @cached_property
    def ProgressCounters(self):  # pragma: no cover
        return ProgressCounters.make_one(self.boto3_raw_data["ProgressCounters"])

    @cached_property
    def AlarmConfiguration(self):  # pragma: no cover
        return AlarmConfigurationOutput.make_one(
            self.boto3_raw_data["AlarmConfiguration"]
        )

    @cached_property
    def TriggeredAlarms(self):  # pragma: no cover
        return AlarmStateInformation.make_many(self.boto3_raw_data["TriggeredAlarms"])

    TargetLocationsURL = field("TargetLocationsURL")
    AutomationSubtype = field("AutomationSubtype")
    ScheduledTime = field("ScheduledTime")

    @cached_property
    def Runbooks(self):  # pragma: no cover
        return RunbookOutput.make_many(self.boto3_raw_data["Runbooks"])

    OpsItemId = field("OpsItemId")
    AssociationId = field("AssociationId")
    ChangeRequestName = field("ChangeRequestName")
    Variables = field("Variables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomationExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutomationStepExecutionsResult:
    boto3_raw_data: "type_defs.DescribeAutomationStepExecutionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StepExecutions(self):  # pragma: no cover
        return StepExecution.make_many(self.boto3_raw_data["StepExecutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutomationStepExecutionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutomationStepExecutionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTaskWithMaintenanceWindowRequest:
    boto3_raw_data: "type_defs.RegisterTaskWithMaintenanceWindowRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    TaskArn = field("TaskArn")
    TaskType = field("TaskType")
    Targets = field("Targets")
    ServiceRoleArn = field("ServiceRoleArn")
    TaskParameters = field("TaskParameters")
    TaskInvocationParameters = field("TaskInvocationParameters")
    Priority = field("Priority")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    Name = field("Name")
    Description = field("Description")
    ClientToken = field("ClientToken")
    CutoffBehavior = field("CutoffBehavior")
    AlarmConfiguration = field("AlarmConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterTaskWithMaintenanceWindowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTaskWithMaintenanceWindowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMaintenanceWindowTaskRequest:
    boto3_raw_data: "type_defs.UpdateMaintenanceWindowTaskRequestTypeDef" = (
        dataclasses.field()
    )

    WindowId = field("WindowId")
    WindowTaskId = field("WindowTaskId")
    Targets = field("Targets")
    TaskArn = field("TaskArn")
    ServiceRoleArn = field("ServiceRoleArn")
    TaskParameters = field("TaskParameters")
    TaskInvocationParameters = field("TaskInvocationParameters")
    Priority = field("Priority")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    Name = field("Name")
    Description = field("Description")
    Replace = field("Replace")
    CutoffBehavior = field("CutoffBehavior")
    AlarmConfiguration = field("AlarmConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMaintenanceWindowTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMaintenanceWindowTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPatchBaselineResult:
    boto3_raw_data: "type_defs.GetPatchBaselineResultTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")
    Name = field("Name")
    OperatingSystem = field("OperatingSystem")

    @cached_property
    def GlobalFilters(self):  # pragma: no cover
        return PatchFilterGroupOutput.make_one(self.boto3_raw_data["GlobalFilters"])

    @cached_property
    def ApprovalRules(self):  # pragma: no cover
        return PatchRuleGroupOutput.make_one(self.boto3_raw_data["ApprovalRules"])

    ApprovedPatches = field("ApprovedPatches")
    ApprovedPatchesComplianceLevel = field("ApprovedPatchesComplianceLevel")
    ApprovedPatchesEnableNonSecurity = field("ApprovedPatchesEnableNonSecurity")
    RejectedPatches = field("RejectedPatches")
    RejectedPatchesAction = field("RejectedPatchesAction")
    PatchGroups = field("PatchGroups")
    CreatedDate = field("CreatedDate")
    ModifiedDate = field("ModifiedDate")
    Description = field("Description")

    @cached_property
    def Sources(self):  # pragma: no cover
        return PatchSourceOutput.make_many(self.boto3_raw_data["Sources"])

    AvailableSecurityUpdatesComplianceStatus = field(
        "AvailableSecurityUpdatesComplianceStatus"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPatchBaselineResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPatchBaselineResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePatchBaselineResult:
    boto3_raw_data: "type_defs.UpdatePatchBaselineResultTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")
    Name = field("Name")
    OperatingSystem = field("OperatingSystem")

    @cached_property
    def GlobalFilters(self):  # pragma: no cover
        return PatchFilterGroupOutput.make_one(self.boto3_raw_data["GlobalFilters"])

    @cached_property
    def ApprovalRules(self):  # pragma: no cover
        return PatchRuleGroupOutput.make_one(self.boto3_raw_data["ApprovalRules"])

    ApprovedPatches = field("ApprovedPatches")
    ApprovedPatchesComplianceLevel = field("ApprovedPatchesComplianceLevel")
    ApprovedPatchesEnableNonSecurity = field("ApprovedPatchesEnableNonSecurity")
    RejectedPatches = field("RejectedPatches")
    RejectedPatchesAction = field("RejectedPatchesAction")
    CreatedDate = field("CreatedDate")
    ModifiedDate = field("ModifiedDate")
    Description = field("Description")

    @cached_property
    def Sources(self):  # pragma: no cover
        return PatchSourceOutput.make_many(self.boto3_raw_data["Sources"])

    AvailableSecurityUpdatesComplianceStatus = field(
        "AvailableSecurityUpdatesComplianceStatus"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePatchBaselineResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePatchBaselineResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchRule:
    boto3_raw_data: "type_defs.PatchRuleTypeDef" = dataclasses.field()

    PatchFilterGroup = field("PatchFilterGroup")
    ComplianceLevel = field("ComplianceLevel")
    ApproveAfterDays = field("ApproveAfterDays")
    ApproveUntilDate = field("ApproveUntilDate")
    EnableNonSecurity = field("EnableNonSecurity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDataSyncResult:
    boto3_raw_data: "type_defs.ListResourceDataSyncResultTypeDef" = dataclasses.field()

    @cached_property
    def ResourceDataSyncItems(self):  # pragma: no cover
        return ResourceDataSyncItem.make_many(
            self.boto3_raw_data["ResourceDataSyncItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceDataSyncResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDataSyncResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceDataSyncRequest:
    boto3_raw_data: "type_defs.CreateResourceDataSyncRequestTypeDef" = (
        dataclasses.field()
    )

    SyncName = field("SyncName")

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return ResourceDataSyncS3Destination.make_one(
            self.boto3_raw_data["S3Destination"]
        )

    SyncType = field("SyncType")

    @cached_property
    def SyncSource(self):  # pragma: no cover
        return ResourceDataSyncSource.make_one(self.boto3_raw_data["SyncSource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceDataSyncRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceDataSyncRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceDataSyncRequest:
    boto3_raw_data: "type_defs.UpdateResourceDataSyncRequestTypeDef" = (
        dataclasses.field()
    )

    SyncName = field("SyncName")
    SyncType = field("SyncType")

    @cached_property
    def SyncSource(self):  # pragma: no cover
        return ResourceDataSyncSource.make_one(self.boto3_raw_data["SyncSource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResourceDataSyncRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceDataSyncRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssociationBatchResult:
    boto3_raw_data: "type_defs.CreateAssociationBatchResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Successful(self):  # pragma: no cover
        return AssociationDescription.make_many(self.boto3_raw_data["Successful"])

    @cached_property
    def Failed(self):  # pragma: no cover
        return FailedCreateAssociation.make_many(self.boto3_raw_data["Failed"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssociationBatchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssociationBatchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutomationExecutionsResult:
    boto3_raw_data: "type_defs.DescribeAutomationExecutionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutomationExecutionMetadataList(self):  # pragma: no cover
        return AutomationExecutionMetadata.make_many(
            self.boto3_raw_data["AutomationExecutionMetadataList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutomationExecutionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutomationExecutionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomationExecutionResult:
    boto3_raw_data: "type_defs.GetAutomationExecutionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutomationExecution(self):  # pragma: no cover
        return AutomationExecution.make_one(self.boto3_raw_data["AutomationExecution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAutomationExecutionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomationExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationExecutionInputs:
    boto3_raw_data: "type_defs.AutomationExecutionInputsTypeDef" = dataclasses.field()

    Parameters = field("Parameters")
    TargetParameterName = field("TargetParameterName")
    Targets = field("Targets")
    TargetMaps = field("TargetMaps")
    TargetLocations = field("TargetLocations")
    TargetLocationsURL = field("TargetLocationsURL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomationExecutionInputsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationExecutionInputsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssociationBatchRequestEntry:
    boto3_raw_data: "type_defs.CreateAssociationBatchRequestEntryTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    InstanceId = field("InstanceId")
    Parameters = field("Parameters")
    AutomationTargetParameterName = field("AutomationTargetParameterName")
    DocumentVersion = field("DocumentVersion")
    Targets = field("Targets")
    ScheduleExpression = field("ScheduleExpression")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return InstanceAssociationOutputLocation.make_one(
            self.boto3_raw_data["OutputLocation"]
        )

    AssociationName = field("AssociationName")
    MaxErrors = field("MaxErrors")
    MaxConcurrency = field("MaxConcurrency")
    ComplianceSeverity = field("ComplianceSeverity")
    SyncCompliance = field("SyncCompliance")
    ApplyOnlyAtCronInterval = field("ApplyOnlyAtCronInterval")
    CalendarNames = field("CalendarNames")
    TargetLocations = field("TargetLocations")
    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")
    AlarmConfiguration = field("AlarmConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssociationBatchRequestEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssociationBatchRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssociationRequest:
    boto3_raw_data: "type_defs.CreateAssociationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DocumentVersion = field("DocumentVersion")
    InstanceId = field("InstanceId")
    Parameters = field("Parameters")
    Targets = field("Targets")
    ScheduleExpression = field("ScheduleExpression")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return InstanceAssociationOutputLocation.make_one(
            self.boto3_raw_data["OutputLocation"]
        )

    AssociationName = field("AssociationName")
    AutomationTargetParameterName = field("AutomationTargetParameterName")
    MaxErrors = field("MaxErrors")
    MaxConcurrency = field("MaxConcurrency")
    ComplianceSeverity = field("ComplianceSeverity")
    SyncCompliance = field("SyncCompliance")
    ApplyOnlyAtCronInterval = field("ApplyOnlyAtCronInterval")
    CalendarNames = field("CalendarNames")
    TargetLocations = field("TargetLocations")
    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AlarmConfiguration = field("AlarmConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Runbook:
    boto3_raw_data: "type_defs.RunbookTypeDef" = dataclasses.field()

    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")
    TargetParameterName = field("TargetParameterName")
    Targets = field("Targets")
    TargetMaps = field("TargetMaps")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    TargetLocations = field("TargetLocations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunbookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunbookTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAutomationExecutionRequest:
    boto3_raw_data: "type_defs.StartAutomationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")
    ClientToken = field("ClientToken")
    Mode = field("Mode")
    TargetParameterName = field("TargetParameterName")
    Targets = field("Targets")
    TargetMaps = field("TargetMaps")
    MaxConcurrency = field("MaxConcurrency")
    MaxErrors = field("MaxErrors")
    TargetLocations = field("TargetLocations")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AlarmConfiguration = field("AlarmConfiguration")
    TargetLocationsURL = field("TargetLocationsURL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAutomationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAutomationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssociationRequest:
    boto3_raw_data: "type_defs.UpdateAssociationRequestTypeDef" = dataclasses.field()

    AssociationId = field("AssociationId")
    Parameters = field("Parameters")
    DocumentVersion = field("DocumentVersion")
    ScheduleExpression = field("ScheduleExpression")

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return InstanceAssociationOutputLocation.make_one(
            self.boto3_raw_data["OutputLocation"]
        )

    Name = field("Name")
    Targets = field("Targets")
    AssociationName = field("AssociationName")
    AssociationVersion = field("AssociationVersion")
    AutomationTargetParameterName = field("AutomationTargetParameterName")
    MaxErrors = field("MaxErrors")
    MaxConcurrency = field("MaxConcurrency")
    ComplianceSeverity = field("ComplianceSeverity")
    SyncCompliance = field("SyncCompliance")
    ApplyOnlyAtCronInterval = field("ApplyOnlyAtCronInterval")
    CalendarNames = field("CalendarNames")
    TargetLocations = field("TargetLocations")
    ScheduleOffset = field("ScheduleOffset")
    Duration = field("Duration")
    TargetMaps = field("TargetMaps")
    AlarmConfiguration = field("AlarmConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionInputs:
    boto3_raw_data: "type_defs.ExecutionInputsTypeDef" = dataclasses.field()

    @cached_property
    def Automation(self):  # pragma: no cover
        return AutomationExecutionInputs.make_one(self.boto3_raw_data["Automation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionInputsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionInputsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchRuleGroup:
    boto3_raw_data: "type_defs.PatchRuleGroupTypeDef" = dataclasses.field()

    PatchRules = field("PatchRules")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchRuleGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchRuleGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExecutionPreviewRequest:
    boto3_raw_data: "type_defs.StartExecutionPreviewRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")

    @cached_property
    def ExecutionInputs(self):  # pragma: no cover
        return ExecutionInputs.make_one(self.boto3_raw_data["ExecutionInputs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExecutionPreviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExecutionPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssociationBatchRequest:
    boto3_raw_data: "type_defs.CreateAssociationBatchRequestTypeDef" = (
        dataclasses.field()
    )

    Entries = field("Entries")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssociationBatchRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssociationBatchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChangeRequestExecutionRequest:
    boto3_raw_data: "type_defs.StartChangeRequestExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    DocumentName = field("DocumentName")
    Runbooks = field("Runbooks")
    ScheduledTime = field("ScheduledTime")
    DocumentVersion = field("DocumentVersion")
    Parameters = field("Parameters")
    ChangeRequestName = field("ChangeRequestName")
    ClientToken = field("ClientToken")
    AutoApprove = field("AutoApprove")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ScheduledEndTime = field("ScheduledEndTime")
    ChangeDetails = field("ChangeDetails")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartChangeRequestExecutionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChangeRequestExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BaselineOverride:
    boto3_raw_data: "type_defs.BaselineOverrideTypeDef" = dataclasses.field()

    OperatingSystem = field("OperatingSystem")
    GlobalFilters = field("GlobalFilters")
    ApprovalRules = field("ApprovalRules")
    ApprovedPatches = field("ApprovedPatches")
    ApprovedPatchesComplianceLevel = field("ApprovedPatchesComplianceLevel")
    RejectedPatches = field("RejectedPatches")
    RejectedPatchesAction = field("RejectedPatchesAction")
    ApprovedPatchesEnableNonSecurity = field("ApprovedPatchesEnableNonSecurity")
    Sources = field("Sources")
    AvailableSecurityUpdatesComplianceStatus = field(
        "AvailableSecurityUpdatesComplianceStatus"
    )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BaselineOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaselineOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePatchBaselineRequest:
    boto3_raw_data: "type_defs.CreatePatchBaselineRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    OperatingSystem = field("OperatingSystem")
    GlobalFilters = field("GlobalFilters")
    ApprovalRules = field("ApprovalRules")
    ApprovedPatches = field("ApprovedPatches")
    ApprovedPatchesComplianceLevel = field("ApprovedPatchesComplianceLevel")
    ApprovedPatchesEnableNonSecurity = field("ApprovedPatchesEnableNonSecurity")
    RejectedPatches = field("RejectedPatches")
    RejectedPatchesAction = field("RejectedPatchesAction")
    Description = field("Description")
    Sources = field("Sources")
    AvailableSecurityUpdatesComplianceStatus = field(
        "AvailableSecurityUpdatesComplianceStatus"
    )
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePatchBaselineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePatchBaselineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePatchBaselineRequest:
    boto3_raw_data: "type_defs.UpdatePatchBaselineRequestTypeDef" = dataclasses.field()

    BaselineId = field("BaselineId")
    Name = field("Name")
    GlobalFilters = field("GlobalFilters")
    ApprovalRules = field("ApprovalRules")
    ApprovedPatches = field("ApprovedPatches")
    ApprovedPatchesComplianceLevel = field("ApprovedPatchesComplianceLevel")
    ApprovedPatchesEnableNonSecurity = field("ApprovedPatchesEnableNonSecurity")
    RejectedPatches = field("RejectedPatches")
    RejectedPatchesAction = field("RejectedPatchesAction")
    Description = field("Description")
    Sources = field("Sources")
    AvailableSecurityUpdatesComplianceStatus = field(
        "AvailableSecurityUpdatesComplianceStatus"
    )
    Replace = field("Replace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePatchBaselineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePatchBaselineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeployablePatchSnapshotForInstanceRequest:
    boto3_raw_data: "type_defs.GetDeployablePatchSnapshotForInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceId = field("InstanceId")
    SnapshotId = field("SnapshotId")

    @cached_property
    def BaselineOverride(self):  # pragma: no cover
        return BaselineOverride.make_one(self.boto3_raw_data["BaselineOverride"])

    UseS3DualStackEndpoint = field("UseS3DualStackEndpoint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeployablePatchSnapshotForInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeployablePatchSnapshotForInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
