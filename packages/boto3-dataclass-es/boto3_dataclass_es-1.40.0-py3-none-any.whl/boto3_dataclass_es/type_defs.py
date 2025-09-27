# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_es import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptInboundCrossClusterSearchConnectionRequest:
    boto3_raw_data: (
        "type_defs.AcceptInboundCrossClusterSearchConnectionRequestTypeDef"
    ) = dataclasses.field()

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptInboundCrossClusterSearchConnectionRequestTypeDef"
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
                "type_defs.AcceptInboundCrossClusterSearchConnectionRequestTypeDef"
            ]
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
class OptionStatus:
    boto3_raw_data: "type_defs.OptionStatusTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    UpdateDate = field("UpdateDate")
    State = field("State")
    UpdateVersion = field("UpdateVersion")
    PendingDeletion = field("PendingDeletion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionStatusTypeDef"]],
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
class AdditionalLimit:
    boto3_raw_data: "type_defs.AdditionalLimitTypeDef" = dataclasses.field()

    LimitName = field("LimitName")
    LimitValues = field("LimitValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdditionalLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdditionalLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MasterUserOptions:
    boto3_raw_data: "type_defs.MasterUserOptionsTypeDef" = dataclasses.field()

    MasterUserARN = field("MasterUserARN")
    MasterUserName = field("MasterUserName")
    MasterUserPassword = field("MasterUserPassword")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MasterUserOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MasterUserOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePackageRequest:
    boto3_raw_data: "type_defs.AssociatePackageRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeVpcEndpointAccessRequest:
    boto3_raw_data: "type_defs.AuthorizeVpcEndpointAccessRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Account = field("Account")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeVpcEndpointAccessRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeVpcEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizedPrincipal:
    boto3_raw_data: "type_defs.AuthorizedPrincipalTypeDef" = dataclasses.field()

    PrincipalType = field("PrincipalType")
    Principal = field("Principal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizedPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizedPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledAutoTuneDetails:
    boto3_raw_data: "type_defs.ScheduledAutoTuneDetailsTypeDef" = dataclasses.field()

    Date = field("Date")
    ActionType = field("ActionType")
    Action = field("Action")
    Severity = field("Severity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledAutoTuneDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledAutoTuneDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Duration:
    boto3_raw_data: "type_defs.DurationTypeDef" = dataclasses.field()

    Value = field("Value")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DurationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneOptionsOutput:
    boto3_raw_data: "type_defs.AutoTuneOptionsOutputTypeDef" = dataclasses.field()

    State = field("State")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTuneOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTuneOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneStatus:
    boto3_raw_data: "type_defs.AutoTuneStatusTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    UpdateDate = field("UpdateDate")
    State = field("State")
    UpdateVersion = field("UpdateVersion")
    ErrorMessage = field("ErrorMessage")
    PendingDeletion = field("PendingDeletion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoTuneStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoTuneStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDomainConfigChangeRequest:
    boto3_raw_data: "type_defs.CancelDomainConfigChangeRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelDomainConfigChangeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDomainConfigChangeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelledChangeProperty:
    boto3_raw_data: "type_defs.CancelledChangePropertyTypeDef" = dataclasses.field()

    PropertyName = field("PropertyName")
    CancelledValue = field("CancelledValue")
    ActiveValue = field("ActiveValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelledChangePropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelledChangePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelElasticsearchServiceSoftwareUpdateRequest:
    boto3_raw_data: (
        "type_defs.CancelElasticsearchServiceSoftwareUpdateRequestTypeDef"
    ) = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelElasticsearchServiceSoftwareUpdateRequestTypeDef"
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
                "type_defs.CancelElasticsearchServiceSoftwareUpdateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSoftwareOptions:
    boto3_raw_data: "type_defs.ServiceSoftwareOptionsTypeDef" = dataclasses.field()

    CurrentVersion = field("CurrentVersion")
    NewVersion = field("NewVersion")
    UpdateAvailable = field("UpdateAvailable")
    Cancellable = field("Cancellable")
    UpdateStatus = field("UpdateStatus")
    Description = field("Description")
    AutomatedUpdateDate = field("AutomatedUpdateDate")
    OptionalDeployment = field("OptionalDeployment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceSoftwareOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceSoftwareOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeProgressDetails:
    boto3_raw_data: "type_defs.ChangeProgressDetailsTypeDef" = dataclasses.field()

    ChangeId = field("ChangeId")
    Message = field("Message")
    ConfigChangeStatus = field("ConfigChangeStatus")
    StartTime = field("StartTime")
    LastUpdatedTime = field("LastUpdatedTime")
    InitiatedBy = field("InitiatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeProgressDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeProgressDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeProgressStage:
    boto3_raw_data: "type_defs.ChangeProgressStageTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    Description = field("Description")
    LastUpdated = field("LastUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeProgressStageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeProgressStageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoOptions:
    boto3_raw_data: "type_defs.CognitoOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    UserPoolId = field("UserPoolId")
    IdentityPoolId = field("IdentityPoolId")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CognitoOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CognitoOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColdStorageOptions:
    boto3_raw_data: "type_defs.ColdStorageOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColdStorageOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColdStorageOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompatibleVersionsMap:
    boto3_raw_data: "type_defs.CompatibleVersionsMapTypeDef" = dataclasses.field()

    SourceVersion = field("SourceVersion")
    TargetVersions = field("TargetVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompatibleVersionsMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompatibleVersionsMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEndpointOptions:
    boto3_raw_data: "type_defs.DomainEndpointOptionsTypeDef" = dataclasses.field()

    EnforceHTTPS = field("EnforceHTTPS")
    TLSSecurityPolicy = field("TLSSecurityPolicy")
    CustomEndpointEnabled = field("CustomEndpointEnabled")
    CustomEndpoint = field("CustomEndpoint")
    CustomEndpointCertificateArn = field("CustomEndpointCertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainEndpointOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainEndpointOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSOptions:
    boto3_raw_data: "type_defs.EBSOptionsTypeDef" = dataclasses.field()

    EBSEnabled = field("EBSEnabled")
    VolumeType = field("VolumeType")
    VolumeSize = field("VolumeSize")
    Iops = field("Iops")
    Throughput = field("Throughput")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EBSOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EBSOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionAtRestOptions:
    boto3_raw_data: "type_defs.EncryptionAtRestOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionAtRestOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionAtRestOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogPublishingOption:
    boto3_raw_data: "type_defs.LogPublishingOptionTypeDef" = dataclasses.field()

    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogPublishingOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogPublishingOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeToNodeEncryptionOptions:
    boto3_raw_data: "type_defs.NodeToNodeEncryptionOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeToNodeEncryptionOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeToNodeEncryptionOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotOptions:
    boto3_raw_data: "type_defs.SnapshotOptionsTypeDef" = dataclasses.field()

    AutomatedSnapshotStartHour = field("AutomatedSnapshotStartHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VPCOptions:
    boto3_raw_data: "type_defs.VPCOptionsTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VPCOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VPCOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainInformation:
    boto3_raw_data: "type_defs.DomainInformationTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    OwnerId = field("OwnerId")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundCrossClusterSearchConnectionStatus:
    boto3_raw_data: "type_defs.OutboundCrossClusterSearchConnectionStatusTypeDef" = (
        dataclasses.field()
    )

    StatusCode = field("StatusCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OutboundCrossClusterSearchConnectionStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundCrossClusterSearchConnectionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageSource:
    boto3_raw_data: "type_defs.PackageSourceTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3Key = field("S3Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteElasticsearchDomainRequest:
    boto3_raw_data: "type_defs.DeleteElasticsearchDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteElasticsearchDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteElasticsearchDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInboundCrossClusterSearchConnectionRequest:
    boto3_raw_data: (
        "type_defs.DeleteInboundCrossClusterSearchConnectionRequestTypeDef"
    ) = dataclasses.field()

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInboundCrossClusterSearchConnectionRequestTypeDef"
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
                "type_defs.DeleteInboundCrossClusterSearchConnectionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutboundCrossClusterSearchConnectionRequest:
    boto3_raw_data: (
        "type_defs.DeleteOutboundCrossClusterSearchConnectionRequestTypeDef"
    ) = dataclasses.field()

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOutboundCrossClusterSearchConnectionRequestTypeDef"
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
                "type_defs.DeleteOutboundCrossClusterSearchConnectionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageRequest:
    boto3_raw_data: "type_defs.DeletePackageRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointRequest:
    boto3_raw_data: "type_defs.DeleteVpcEndpointRequestTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointSummary:
    boto3_raw_data: "type_defs.VpcEndpointSummaryTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")
    VpcEndpointOwner = field("VpcEndpointOwner")
    DomainArn = field("DomainArn")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainAutoTunesRequest:
    boto3_raw_data: "type_defs.DescribeDomainAutoTunesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDomainAutoTunesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainAutoTunesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainChangeProgressRequest:
    boto3_raw_data: "type_defs.DescribeDomainChangeProgressRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ChangeId = field("ChangeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainChangeProgressRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainChangeProgressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchDomainConfigRequest:
    boto3_raw_data: "type_defs.DescribeElasticsearchDomainConfigRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchDomainConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticsearchDomainConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchDomainRequest:
    boto3_raw_data: "type_defs.DescribeElasticsearchDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchDomainRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticsearchDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchDomainsRequest:
    boto3_raw_data: "type_defs.DescribeElasticsearchDomainsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainNames = field("DomainNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchDomainsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticsearchDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchInstanceTypeLimitsRequest:
    boto3_raw_data: (
        "type_defs.DescribeElasticsearchInstanceTypeLimitsRequestTypeDef"
    ) = dataclasses.field()

    InstanceType = field("InstanceType")
    ElasticsearchVersion = field("ElasticsearchVersion")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchInstanceTypeLimitsRequestTypeDef"
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
                "type_defs.DescribeElasticsearchInstanceTypeLimitsRequestTypeDef"
            ]
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
class DescribePackagesFilter:
    boto3_raw_data: "type_defs.DescribePackagesFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackagesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagesFilterTypeDef"]
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
class DescribeReservedElasticsearchInstanceOfferingsRequest:
    boto3_raw_data: (
        "type_defs.DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef"
    ) = dataclasses.field()

    ReservedElasticsearchInstanceOfferingId = field(
        "ReservedElasticsearchInstanceOfferingId"
    )
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef"
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
                "type_defs.DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedElasticsearchInstancesRequest:
    boto3_raw_data: "type_defs.DescribeReservedElasticsearchInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    ReservedElasticsearchInstanceId = field("ReservedElasticsearchInstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedElasticsearchInstancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedElasticsearchInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcEndpointsRequest:
    boto3_raw_data: "type_defs.DescribeVpcEndpointsRequestTypeDef" = dataclasses.field()

    VpcEndpointIds = field("VpcEndpointIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVpcEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointError:
    boto3_raw_data: "type_defs.VpcEndpointErrorTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DissociatePackageRequest:
    boto3_raw_data: "type_defs.DissociatePackageRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DissociatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DissociatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainInfo:
    boto3_raw_data: "type_defs.DomainInfoTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EngineType = field("EngineType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    ErrorType = field("ErrorType")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DryRunResults:
    boto3_raw_data: "type_defs.DryRunResultsTypeDef" = dataclasses.field()

    DeploymentType = field("DeploymentType")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DryRunResultsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DryRunResultsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZoneAwarenessConfig:
    boto3_raw_data: "type_defs.ZoneAwarenessConfigTypeDef" = dataclasses.field()

    AvailabilityZoneCount = field("AvailabilityZoneCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZoneAwarenessConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZoneAwarenessConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyingProperties:
    boto3_raw_data: "type_defs.ModifyingPropertiesTypeDef" = dataclasses.field()

    Name = field("Name")
    ActiveValue = field("ActiveValue")
    PendingValue = field("PendingValue")
    ValueType = field("ValueType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyingPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyingPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VPCDerivedInfo:
    boto3_raw_data: "type_defs.VPCDerivedInfoTypeDef" = dataclasses.field()

    VPCId = field("VPCId")
    SubnetIds = field("SubnetIds")
    AvailabilityZones = field("AvailabilityZones")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VPCDerivedInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VPCDerivedInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompatibleElasticsearchVersionsRequest:
    boto3_raw_data: "type_defs.GetCompatibleElasticsearchVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCompatibleElasticsearchVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompatibleElasticsearchVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionHistoryRequest:
    boto3_raw_data: "type_defs.GetPackageVersionHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    PackageID = field("PackageID")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPackageVersionHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionHistory:
    boto3_raw_data: "type_defs.PackageVersionHistoryTypeDef" = dataclasses.field()

    PackageVersion = field("PackageVersion")
    CommitMessage = field("CommitMessage")
    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionHistoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUpgradeHistoryRequest:
    boto3_raw_data: "type_defs.GetUpgradeHistoryRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUpgradeHistoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUpgradeHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUpgradeStatusRequest:
    boto3_raw_data: "type_defs.GetUpgradeStatusRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUpgradeStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUpgradeStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundCrossClusterSearchConnectionStatus:
    boto3_raw_data: "type_defs.InboundCrossClusterSearchConnectionStatusTypeDef" = (
        dataclasses.field()
    )

    StatusCode = field("StatusCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InboundCrossClusterSearchConnectionStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundCrossClusterSearchConnectionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceCountLimits:
    boto3_raw_data: "type_defs.InstanceCountLimitsTypeDef" = dataclasses.field()

    MinimumInstanceCount = field("MinimumInstanceCount")
    MaximumInstanceCount = field("MaximumInstanceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceCountLimitsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceCountLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainNamesRequest:
    boto3_raw_data: "type_defs.ListDomainNamesRequestTypeDef" = dataclasses.field()

    EngineType = field("EngineType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainNamesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsForPackageRequest:
    boto3_raw_data: "type_defs.ListDomainsForPackageRequestTypeDef" = (
        dataclasses.field()
    )

    PackageID = field("PackageID")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsForPackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsForPackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListElasticsearchInstanceTypesRequest:
    boto3_raw_data: "type_defs.ListElasticsearchInstanceTypesRequestTypeDef" = (
        dataclasses.field()
    )

    ElasticsearchVersion = field("ElasticsearchVersion")
    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListElasticsearchInstanceTypesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListElasticsearchInstanceTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListElasticsearchVersionsRequest:
    boto3_raw_data: "type_defs.ListElasticsearchVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListElasticsearchVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListElasticsearchVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesForDomainRequest:
    boto3_raw_data: "type_defs.ListPackagesForDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesForDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesForDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequest:
    boto3_raw_data: "type_defs.ListTagsRequestTypeDef" = dataclasses.field()

    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointAccessRequest:
    boto3_raw_data: "type_defs.ListVpcEndpointAccessRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcEndpointAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointsForDomainRequest:
    boto3_raw_data: "type_defs.ListVpcEndpointsForDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVpcEndpointsForDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointsForDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointsRequest:
    boto3_raw_data: "type_defs.ListVpcEndpointsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedElasticsearchInstanceOfferingRequest:
    boto3_raw_data: (
        "type_defs.PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef"
    ) = dataclasses.field()

    ReservedElasticsearchInstanceOfferingId = field(
        "ReservedElasticsearchInstanceOfferingId"
    )
    ReservationName = field("ReservationName")
    InstanceCount = field("InstanceCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef"
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
                "type_defs.PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef"
            ]
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
class RejectInboundCrossClusterSearchConnectionRequest:
    boto3_raw_data: (
        "type_defs.RejectInboundCrossClusterSearchConnectionRequestTypeDef"
    ) = dataclasses.field()

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectInboundCrossClusterSearchConnectionRequestTypeDef"
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
                "type_defs.RejectInboundCrossClusterSearchConnectionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsRequest:
    boto3_raw_data: "type_defs.RemoveTagsRequestTypeDef" = dataclasses.field()

    ARN = field("ARN")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeVpcEndpointAccessRequest:
    boto3_raw_data: "type_defs.RevokeVpcEndpointAccessRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Account = field("Account")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RevokeVpcEndpointAccessRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeVpcEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAMLIdp:
    boto3_raw_data: "type_defs.SAMLIdpTypeDef" = dataclasses.field()

    MetadataContent = field("MetadataContent")
    EntityId = field("EntityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SAMLIdpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SAMLIdpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartElasticsearchServiceSoftwareUpdateRequest:
    boto3_raw_data: (
        "type_defs.StartElasticsearchServiceSoftwareUpdateRequestTypeDef"
    ) = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartElasticsearchServiceSoftwareUpdateRequestTypeDef"
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
                "type_defs.StartElasticsearchServiceSoftwareUpdateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageTypeLimit:
    boto3_raw_data: "type_defs.StorageTypeLimitTypeDef" = dataclasses.field()

    LimitName = field("LimitName")
    LimitValues = field("LimitValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageTypeLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageTypeLimitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeElasticsearchDomainRequest:
    boto3_raw_data: "type_defs.UpgradeElasticsearchDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    TargetVersion = field("TargetVersion")
    PerformCheckOnly = field("PerformCheckOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpgradeElasticsearchDomainRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeElasticsearchDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeStepItem:
    boto3_raw_data: "type_defs.UpgradeStepItemTypeDef" = dataclasses.field()

    UpgradeStep = field("UpgradeStep")
    UpgradeStepStatus = field("UpgradeStepStatus")
    Issues = field("Issues")
    ProgressPercent = field("ProgressPercent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpgradeStepItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpgradeStepItemTypeDef"]],
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
class GetUpgradeStatusResponse:
    boto3_raw_data: "type_defs.GetUpgradeStatusResponseTypeDef" = dataclasses.field()

    UpgradeStep = field("UpgradeStep")
    StepStatus = field("StepStatus")
    UpgradeName = field("UpgradeName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUpgradeStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUpgradeStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListElasticsearchInstanceTypesResponse:
    boto3_raw_data: "type_defs.ListElasticsearchInstanceTypesResponseTypeDef" = (
        dataclasses.field()
    )

    ElasticsearchInstanceTypes = field("ElasticsearchInstanceTypes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListElasticsearchInstanceTypesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListElasticsearchInstanceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListElasticsearchVersionsResponse:
    boto3_raw_data: "type_defs.ListElasticsearchVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    ElasticsearchVersions = field("ElasticsearchVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListElasticsearchVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListElasticsearchVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedElasticsearchInstanceOfferingResponse:
    boto3_raw_data: (
        "type_defs.PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef"
    ) = dataclasses.field()

    ReservedElasticsearchInstanceId = field("ReservedElasticsearchInstanceId")
    ReservationName = field("ReservationName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef"
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
                "type_defs.PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPoliciesStatus:
    boto3_raw_data: "type_defs.AccessPoliciesStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPoliciesStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPoliciesStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedOptionsStatus:
    boto3_raw_data: "type_defs.AdvancedOptionsStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchVersionStatus:
    boto3_raw_data: "type_defs.ElasticsearchVersionStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchVersionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchVersionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsRequest:
    boto3_raw_data: "type_defs.AddTagsRequestTypeDef" = dataclasses.field()

    ARN = field("ARN")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResponse:
    boto3_raw_data: "type_defs.ListTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeVpcEndpointAccessResponse:
    boto3_raw_data: "type_defs.AuthorizeVpcEndpointAccessResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthorizedPrincipal(self):  # pragma: no cover
        return AuthorizedPrincipal.make_one(self.boto3_raw_data["AuthorizedPrincipal"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeVpcEndpointAccessResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeVpcEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointAccessResponse:
    boto3_raw_data: "type_defs.ListVpcEndpointAccessResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthorizedPrincipalList(self):  # pragma: no cover
        return AuthorizedPrincipal.make_many(
            self.boto3_raw_data["AuthorizedPrincipalList"]
        )

    NextToken = field("NextToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVpcEndpointAccessResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneDetails:
    boto3_raw_data: "type_defs.AutoTuneDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ScheduledAutoTuneDetails(self):  # pragma: no cover
        return ScheduledAutoTuneDetails.make_one(
            self.boto3_raw_data["ScheduledAutoTuneDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoTuneDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoTuneDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneMaintenanceScheduleOutput:
    boto3_raw_data: "type_defs.AutoTuneMaintenanceScheduleOutputTypeDef" = (
        dataclasses.field()
    )

    StartAt = field("StartAt")

    @cached_property
    def Duration(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["Duration"])

    CronExpressionForRecurrence = field("CronExpressionForRecurrence")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutoTuneMaintenanceScheduleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTuneMaintenanceScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneMaintenanceSchedule:
    boto3_raw_data: "type_defs.AutoTuneMaintenanceScheduleTypeDef" = dataclasses.field()

    StartAt = field("StartAt")

    @cached_property
    def Duration(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["Duration"])

    CronExpressionForRecurrence = field("CronExpressionForRecurrence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTuneMaintenanceScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTuneMaintenanceScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDomainConfigChangeResponse:
    boto3_raw_data: "type_defs.CancelDomainConfigChangeResponseTypeDef" = (
        dataclasses.field()
    )

    DryRun = field("DryRun")
    CancelledChangeIds = field("CancelledChangeIds")

    @cached_property
    def CancelledChangeProperties(self):  # pragma: no cover
        return CancelledChangeProperty.make_many(
            self.boto3_raw_data["CancelledChangeProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelDomainConfigChangeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDomainConfigChangeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelElasticsearchServiceSoftwareUpdateResponse:
    boto3_raw_data: (
        "type_defs.CancelElasticsearchServiceSoftwareUpdateResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceSoftwareOptions(self):  # pragma: no cover
        return ServiceSoftwareOptions.make_one(
            self.boto3_raw_data["ServiceSoftwareOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelElasticsearchServiceSoftwareUpdateResponseTypeDef"
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
                "type_defs.CancelElasticsearchServiceSoftwareUpdateResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartElasticsearchServiceSoftwareUpdateResponse:
    boto3_raw_data: (
        "type_defs.StartElasticsearchServiceSoftwareUpdateResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceSoftwareOptions(self):  # pragma: no cover
        return ServiceSoftwareOptions.make_one(
            self.boto3_raw_data["ServiceSoftwareOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartElasticsearchServiceSoftwareUpdateResponseTypeDef"
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
                "type_defs.StartElasticsearchServiceSoftwareUpdateResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeElasticsearchDomainResponse:
    boto3_raw_data: "type_defs.UpgradeElasticsearchDomainResponseTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    TargetVersion = field("TargetVersion")
    PerformCheckOnly = field("PerformCheckOnly")

    @cached_property
    def ChangeProgressDetails(self):  # pragma: no cover
        return ChangeProgressDetails.make_one(
            self.boto3_raw_data["ChangeProgressDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpgradeElasticsearchDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeElasticsearchDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeProgressStatusDetails:
    boto3_raw_data: "type_defs.ChangeProgressStatusDetailsTypeDef" = dataclasses.field()

    ChangeId = field("ChangeId")
    StartTime = field("StartTime")
    Status = field("Status")
    PendingProperties = field("PendingProperties")
    CompletedProperties = field("CompletedProperties")
    TotalNumberOfStages = field("TotalNumberOfStages")

    @cached_property
    def ChangeProgressStages(self):  # pragma: no cover
        return ChangeProgressStage.make_many(
            self.boto3_raw_data["ChangeProgressStages"]
        )

    ConfigChangeStatus = field("ConfigChangeStatus")
    LastUpdatedTime = field("LastUpdatedTime")
    InitiatedBy = field("InitiatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeProgressStatusDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeProgressStatusDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoOptionsStatus:
    boto3_raw_data: "type_defs.CognitoOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return CognitoOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CognitoOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompatibleElasticsearchVersionsResponse:
    boto3_raw_data: "type_defs.GetCompatibleElasticsearchVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CompatibleElasticsearchVersions(self):  # pragma: no cover
        return CompatibleVersionsMap.make_many(
            self.boto3_raw_data["CompatibleElasticsearchVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCompatibleElasticsearchVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompatibleElasticsearchVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEndpointOptionsStatus:
    boto3_raw_data: "type_defs.DomainEndpointOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainEndpointOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainEndpointOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSOptionsStatus:
    boto3_raw_data: "type_defs.EBSOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return EBSOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EBSOptionsStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionAtRestOptionsStatus:
    boto3_raw_data: "type_defs.EncryptionAtRestOptionsStatusTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Options(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EncryptionAtRestOptionsStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionAtRestOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogPublishingOptionsStatus:
    boto3_raw_data: "type_defs.LogPublishingOptionsStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogPublishingOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogPublishingOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeToNodeEncryptionOptionsStatus:
    boto3_raw_data: "type_defs.NodeToNodeEncryptionOptionsStatusTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Options(self):  # pragma: no cover
        return NodeToNodeEncryptionOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NodeToNodeEncryptionOptionsStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeToNodeEncryptionOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotOptionsStatus:
    boto3_raw_data: "type_defs.SnapshotOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return SnapshotOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapshotOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointRequest:
    boto3_raw_data: "type_defs.CreateVpcEndpointRequestTypeDef" = dataclasses.field()

    DomainArn = field("DomainArn")

    @cached_property
    def VpcOptions(self):  # pragma: no cover
        return VPCOptions.make_one(self.boto3_raw_data["VpcOptions"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcEndpointRequest:
    boto3_raw_data: "type_defs.UpdateVpcEndpointRequestTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")

    @cached_property
    def VpcOptions(self):  # pragma: no cover
        return VPCOptions.make_one(self.boto3_raw_data["VpcOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOutboundCrossClusterSearchConnectionRequest:
    boto3_raw_data: (
        "type_defs.CreateOutboundCrossClusterSearchConnectionRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SourceDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["SourceDomainInfo"])

    @cached_property
    def DestinationDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["DestinationDomainInfo"])

    ConnectionAlias = field("ConnectionAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOutboundCrossClusterSearchConnectionRequestTypeDef"
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
                "type_defs.CreateOutboundCrossClusterSearchConnectionRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOutboundCrossClusterSearchConnectionResponse:
    boto3_raw_data: (
        "type_defs.CreateOutboundCrossClusterSearchConnectionResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SourceDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["SourceDomainInfo"])

    @cached_property
    def DestinationDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["DestinationDomainInfo"])

    ConnectionAlias = field("ConnectionAlias")

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return OutboundCrossClusterSearchConnectionStatus.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOutboundCrossClusterSearchConnectionResponseTypeDef"
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
                "type_defs.CreateOutboundCrossClusterSearchConnectionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundCrossClusterSearchConnection:
    boto3_raw_data: "type_defs.OutboundCrossClusterSearchConnectionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["SourceDomainInfo"])

    @cached_property
    def DestinationDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["DestinationDomainInfo"])

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")
    ConnectionAlias = field("ConnectionAlias")

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return OutboundCrossClusterSearchConnectionStatus.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OutboundCrossClusterSearchConnectionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundCrossClusterSearchConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageRequest:
    boto3_raw_data: "type_defs.CreatePackageRequestTypeDef" = dataclasses.field()

    PackageName = field("PackageName")
    PackageType = field("PackageType")

    @cached_property
    def PackageSource(self):  # pragma: no cover
        return PackageSource.make_one(self.boto3_raw_data["PackageSource"])

    PackageDescription = field("PackageDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageRequest:
    boto3_raw_data: "type_defs.UpdatePackageRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")

    @cached_property
    def PackageSource(self):  # pragma: no cover
        return PackageSource.make_one(self.boto3_raw_data["PackageSource"])

    PackageDescription = field("PackageDescription")
    CommitMessage = field("CommitMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointResponse:
    boto3_raw_data: "type_defs.DeleteVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcEndpointSummary(self):  # pragma: no cover
        return VpcEndpointSummary.make_one(self.boto3_raw_data["VpcEndpointSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointsForDomainResponse:
    boto3_raw_data: "type_defs.ListVpcEndpointsForDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcEndpointSummaryList(self):  # pragma: no cover
        return VpcEndpointSummary.make_many(
            self.boto3_raw_data["VpcEndpointSummaryList"]
        )

    NextToken = field("NextToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVpcEndpointsForDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointsForDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointsResponse:
    boto3_raw_data: "type_defs.ListVpcEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcEndpointSummaryList(self):  # pragma: no cover
        return VpcEndpointSummary.make_many(
            self.boto3_raw_data["VpcEndpointSummaryList"]
        )

    NextToken = field("NextToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundCrossClusterSearchConnectionsRequest:
    boto3_raw_data: (
        "type_defs.DescribeInboundCrossClusterSearchConnectionsRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundCrossClusterSearchConnectionsRequestTypeDef"
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
                "type_defs.DescribeInboundCrossClusterSearchConnectionsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOutboundCrossClusterSearchConnectionsRequest:
    boto3_raw_data: (
        "type_defs.DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef"
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
                "type_defs.DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackagesRequest:
    boto3_raw_data: "type_defs.DescribePackagesRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribePackagesFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedElasticsearchInstanceOfferingsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeReservedElasticsearchInstanceOfferingsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ReservedElasticsearchInstanceOfferingId = field(
        "ReservedElasticsearchInstanceOfferingId"
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedElasticsearchInstanceOfferingsRequestPaginateTypeDef"
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
                "type_defs.DescribeReservedElasticsearchInstanceOfferingsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedElasticsearchInstancesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeReservedElasticsearchInstancesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ReservedElasticsearchInstanceId = field("ReservedElasticsearchInstanceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedElasticsearchInstancesRequestPaginateTypeDef"
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
                "type_defs.DescribeReservedElasticsearchInstancesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUpgradeHistoryRequestPaginate:
    boto3_raw_data: "type_defs.GetUpgradeHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetUpgradeHistoryRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUpgradeHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListElasticsearchInstanceTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListElasticsearchInstanceTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ElasticsearchVersion = field("ElasticsearchVersion")
    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListElasticsearchInstanceTypesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListElasticsearchInstanceTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListElasticsearchVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListElasticsearchVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListElasticsearchVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListElasticsearchVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainNamesResponse:
    boto3_raw_data: "type_defs.ListDomainNamesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainNames(self):  # pragma: no cover
        return DomainInfo.make_many(self.boto3_raw_data["DomainNames"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainNamesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainPackageDetails:
    boto3_raw_data: "type_defs.DomainPackageDetailsTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    PackageName = field("PackageName")
    PackageType = field("PackageType")
    LastUpdated = field("LastUpdated")
    DomainName = field("DomainName")
    DomainPackageStatus = field("DomainPackageStatus")
    PackageVersion = field("PackageVersion")
    ReferencePath = field("ReferencePath")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["ErrorDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainPackageDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainPackageDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageDetails:
    boto3_raw_data: "type_defs.PackageDetailsTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    PackageName = field("PackageName")
    PackageType = field("PackageType")
    PackageDescription = field("PackageDescription")
    PackageStatus = field("PackageStatus")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    AvailablePackageVersion = field("AvailablePackageVersion")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["ErrorDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchClusterConfig:
    boto3_raw_data: "type_defs.ElasticsearchClusterConfigTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    InstanceCount = field("InstanceCount")
    DedicatedMasterEnabled = field("DedicatedMasterEnabled")
    ZoneAwarenessEnabled = field("ZoneAwarenessEnabled")

    @cached_property
    def ZoneAwarenessConfig(self):  # pragma: no cover
        return ZoneAwarenessConfig.make_one(self.boto3_raw_data["ZoneAwarenessConfig"])

    DedicatedMasterType = field("DedicatedMasterType")
    DedicatedMasterCount = field("DedicatedMasterCount")
    WarmEnabled = field("WarmEnabled")
    WarmType = field("WarmType")
    WarmCount = field("WarmCount")

    @cached_property
    def ColdStorageOptions(self):  # pragma: no cover
        return ColdStorageOptions.make_one(self.boto3_raw_data["ColdStorageOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchClusterConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchClusterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VPCDerivedInfoStatus:
    boto3_raw_data: "type_defs.VPCDerivedInfoStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return VPCDerivedInfo.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VPCDerivedInfoStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VPCDerivedInfoStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpoint:
    boto3_raw_data: "type_defs.VpcEndpointTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")
    VpcEndpointOwner = field("VpcEndpointOwner")
    DomainArn = field("DomainArn")

    @cached_property
    def VpcOptions(self):  # pragma: no cover
        return VPCDerivedInfo.make_one(self.boto3_raw_data["VpcOptions"])

    Status = field("Status")
    Endpoint = field("Endpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcEndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionHistoryResponse:
    boto3_raw_data: "type_defs.GetPackageVersionHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    PackageID = field("PackageID")

    @cached_property
    def PackageVersionHistoryList(self):  # pragma: no cover
        return PackageVersionHistory.make_many(
            self.boto3_raw_data["PackageVersionHistoryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPackageVersionHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundCrossClusterSearchConnection:
    boto3_raw_data: "type_defs.InboundCrossClusterSearchConnectionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["SourceDomainInfo"])

    @cached_property
    def DestinationDomainInfo(self):  # pragma: no cover
        return DomainInformation.make_one(self.boto3_raw_data["DestinationDomainInfo"])

    CrossClusterSearchConnectionId = field("CrossClusterSearchConnectionId")

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return InboundCrossClusterSearchConnectionStatus.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InboundCrossClusterSearchConnectionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundCrossClusterSearchConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceLimits:
    boto3_raw_data: "type_defs.InstanceLimitsTypeDef" = dataclasses.field()

    @cached_property
    def InstanceCountLimits(self):  # pragma: no cover
        return InstanceCountLimits.make_one(self.boto3_raw_data["InstanceCountLimits"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedElasticsearchInstanceOffering:
    boto3_raw_data: "type_defs.ReservedElasticsearchInstanceOfferingTypeDef" = (
        dataclasses.field()
    )

    ReservedElasticsearchInstanceOfferingId = field(
        "ReservedElasticsearchInstanceOfferingId"
    )
    ElasticsearchInstanceType = field("ElasticsearchInstanceType")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    PaymentOption = field("PaymentOption")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReservedElasticsearchInstanceOfferingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedElasticsearchInstanceOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedElasticsearchInstance:
    boto3_raw_data: "type_defs.ReservedElasticsearchInstanceTypeDef" = (
        dataclasses.field()
    )

    ReservationName = field("ReservationName")
    ReservedElasticsearchInstanceId = field("ReservedElasticsearchInstanceId")
    ReservedElasticsearchInstanceOfferingId = field(
        "ReservedElasticsearchInstanceOfferingId"
    )
    ElasticsearchInstanceType = field("ElasticsearchInstanceType")
    StartTime = field("StartTime")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    ElasticsearchInstanceCount = field("ElasticsearchInstanceCount")
    State = field("State")
    PaymentOption = field("PaymentOption")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReservedElasticsearchInstanceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedElasticsearchInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAMLOptionsInput:
    boto3_raw_data: "type_defs.SAMLOptionsInputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def Idp(self):  # pragma: no cover
        return SAMLIdp.make_one(self.boto3_raw_data["Idp"])

    MasterUserName = field("MasterUserName")
    MasterBackendRole = field("MasterBackendRole")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")
    SessionTimeoutMinutes = field("SessionTimeoutMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SAMLOptionsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAMLOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAMLOptionsOutput:
    boto3_raw_data: "type_defs.SAMLOptionsOutputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def Idp(self):  # pragma: no cover
        return SAMLIdp.make_one(self.boto3_raw_data["Idp"])

    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")
    SessionTimeoutMinutes = field("SessionTimeoutMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SAMLOptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAMLOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageType:
    boto3_raw_data: "type_defs.StorageTypeTypeDef" = dataclasses.field()

    StorageTypeName = field("StorageTypeName")
    StorageSubTypeName = field("StorageSubTypeName")

    @cached_property
    def StorageTypeLimits(self):  # pragma: no cover
        return StorageTypeLimit.make_many(self.boto3_raw_data["StorageTypeLimits"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StorageTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeHistory:
    boto3_raw_data: "type_defs.UpgradeHistoryTypeDef" = dataclasses.field()

    UpgradeName = field("UpgradeName")
    StartTimestamp = field("StartTimestamp")
    UpgradeStatus = field("UpgradeStatus")

    @cached_property
    def StepsList(self):  # pragma: no cover
        return UpgradeStepItem.make_many(self.boto3_raw_data["StepsList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpgradeHistoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpgradeHistoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTune:
    boto3_raw_data: "type_defs.AutoTuneTypeDef" = dataclasses.field()

    AutoTuneType = field("AutoTuneType")

    @cached_property
    def AutoTuneDetails(self):  # pragma: no cover
        return AutoTuneDetails.make_one(self.boto3_raw_data["AutoTuneDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoTuneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoTuneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneOptionsExtra:
    boto3_raw_data: "type_defs.AutoTuneOptionsExtraTypeDef" = dataclasses.field()

    DesiredState = field("DesiredState")
    RollbackOnDisable = field("RollbackOnDisable")

    @cached_property
    def MaintenanceSchedules(self):  # pragma: no cover
        return AutoTuneMaintenanceScheduleOutput.make_many(
            self.boto3_raw_data["MaintenanceSchedules"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTuneOptionsExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTuneOptionsExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneOptions:
    boto3_raw_data: "type_defs.AutoTuneOptionsTypeDef" = dataclasses.field()

    DesiredState = field("DesiredState")
    RollbackOnDisable = field("RollbackOnDisable")

    @cached_property
    def MaintenanceSchedules(self):  # pragma: no cover
        return AutoTuneMaintenanceSchedule.make_many(
            self.boto3_raw_data["MaintenanceSchedules"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoTuneOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoTuneOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainChangeProgressResponse:
    boto3_raw_data: "type_defs.DescribeDomainChangeProgressResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeProgressStatus(self):  # pragma: no cover
        return ChangeProgressStatusDetails.make_one(
            self.boto3_raw_data["ChangeProgressStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainChangeProgressResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainChangeProgressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutboundCrossClusterSearchConnectionResponse:
    boto3_raw_data: (
        "type_defs.DeleteOutboundCrossClusterSearchConnectionResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CrossClusterSearchConnection(self):  # pragma: no cover
        return OutboundCrossClusterSearchConnection.make_one(
            self.boto3_raw_data["CrossClusterSearchConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOutboundCrossClusterSearchConnectionResponseTypeDef"
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
                "type_defs.DeleteOutboundCrossClusterSearchConnectionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOutboundCrossClusterSearchConnectionsResponse:
    boto3_raw_data: (
        "type_defs.DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CrossClusterSearchConnections(self):  # pragma: no cover
        return OutboundCrossClusterSearchConnection.make_many(
            self.boto3_raw_data["CrossClusterSearchConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef"
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
                "type_defs.DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePackageResponse:
    boto3_raw_data: "type_defs.AssociatePackageResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainPackageDetails(self):  # pragma: no cover
        return DomainPackageDetails.make_one(
            self.boto3_raw_data["DomainPackageDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DissociatePackageResponse:
    boto3_raw_data: "type_defs.DissociatePackageResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainPackageDetails(self):  # pragma: no cover
        return DomainPackageDetails.make_one(
            self.boto3_raw_data["DomainPackageDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DissociatePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DissociatePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsForPackageResponse:
    boto3_raw_data: "type_defs.ListDomainsForPackageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainPackageDetailsList(self):  # pragma: no cover
        return DomainPackageDetails.make_many(
            self.boto3_raw_data["DomainPackageDetailsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainsForPackageResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsForPackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesForDomainResponse:
    boto3_raw_data: "type_defs.ListPackagesForDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainPackageDetailsList(self):  # pragma: no cover
        return DomainPackageDetails.make_many(
            self.boto3_raw_data["DomainPackageDetailsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPackagesForDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesForDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageResponse:
    boto3_raw_data: "type_defs.CreatePackageResponseTypeDef" = dataclasses.field()

    @cached_property
    def PackageDetails(self):  # pragma: no cover
        return PackageDetails.make_one(self.boto3_raw_data["PackageDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageResponse:
    boto3_raw_data: "type_defs.DeletePackageResponseTypeDef" = dataclasses.field()

    @cached_property
    def PackageDetails(self):  # pragma: no cover
        return PackageDetails.make_one(self.boto3_raw_data["PackageDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackagesResponse:
    boto3_raw_data: "type_defs.DescribePackagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def PackageDetailsList(self):  # pragma: no cover
        return PackageDetails.make_many(self.boto3_raw_data["PackageDetailsList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageResponse:
    boto3_raw_data: "type_defs.UpdatePackageResponseTypeDef" = dataclasses.field()

    @cached_property
    def PackageDetails(self):  # pragma: no cover
        return PackageDetails.make_one(self.boto3_raw_data["PackageDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchClusterConfigStatus:
    boto3_raw_data: "type_defs.ElasticsearchClusterConfigStatusTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Options(self):  # pragma: no cover
        return ElasticsearchClusterConfig.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ElasticsearchClusterConfigStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchClusterConfigStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointResponse:
    boto3_raw_data: "type_defs.CreateVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcEndpoint(self):  # pragma: no cover
        return VpcEndpoint.make_one(self.boto3_raw_data["VpcEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeVpcEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcEndpoints(self):  # pragma: no cover
        return VpcEndpoint.make_many(self.boto3_raw_data["VpcEndpoints"])

    @cached_property
    def VpcEndpointErrors(self):  # pragma: no cover
        return VpcEndpointError.make_many(self.boto3_raw_data["VpcEndpointErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVpcEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcEndpointResponse:
    boto3_raw_data: "type_defs.UpdateVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcEndpoint(self):  # pragma: no cover
        return VpcEndpoint.make_one(self.boto3_raw_data["VpcEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptInboundCrossClusterSearchConnectionResponse:
    boto3_raw_data: (
        "type_defs.AcceptInboundCrossClusterSearchConnectionResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CrossClusterSearchConnection(self):  # pragma: no cover
        return InboundCrossClusterSearchConnection.make_one(
            self.boto3_raw_data["CrossClusterSearchConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptInboundCrossClusterSearchConnectionResponseTypeDef"
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
                "type_defs.AcceptInboundCrossClusterSearchConnectionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInboundCrossClusterSearchConnectionResponse:
    boto3_raw_data: (
        "type_defs.DeleteInboundCrossClusterSearchConnectionResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CrossClusterSearchConnection(self):  # pragma: no cover
        return InboundCrossClusterSearchConnection.make_one(
            self.boto3_raw_data["CrossClusterSearchConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInboundCrossClusterSearchConnectionResponseTypeDef"
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
                "type_defs.DeleteInboundCrossClusterSearchConnectionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundCrossClusterSearchConnectionsResponse:
    boto3_raw_data: (
        "type_defs.DescribeInboundCrossClusterSearchConnectionsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CrossClusterSearchConnections(self):  # pragma: no cover
        return InboundCrossClusterSearchConnection.make_many(
            self.boto3_raw_data["CrossClusterSearchConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundCrossClusterSearchConnectionsResponseTypeDef"
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
                "type_defs.DescribeInboundCrossClusterSearchConnectionsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectInboundCrossClusterSearchConnectionResponse:
    boto3_raw_data: (
        "type_defs.RejectInboundCrossClusterSearchConnectionResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CrossClusterSearchConnection(self):  # pragma: no cover
        return InboundCrossClusterSearchConnection.make_one(
            self.boto3_raw_data["CrossClusterSearchConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectInboundCrossClusterSearchConnectionResponseTypeDef"
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
                "type_defs.RejectInboundCrossClusterSearchConnectionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedElasticsearchInstanceOfferingsResponse:
    boto3_raw_data: (
        "type_defs.DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ReservedElasticsearchInstanceOfferings(self):  # pragma: no cover
        return ReservedElasticsearchInstanceOffering.make_many(
            self.boto3_raw_data["ReservedElasticsearchInstanceOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef"
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
                "type_defs.DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedElasticsearchInstancesResponse:
    boto3_raw_data: (
        "type_defs.DescribeReservedElasticsearchInstancesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ReservedElasticsearchInstances(self):  # pragma: no cover
        return ReservedElasticsearchInstance.make_many(
            self.boto3_raw_data["ReservedElasticsearchInstances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedElasticsearchInstancesResponseTypeDef"
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
                "type_defs.DescribeReservedElasticsearchInstancesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedSecurityOptionsInput:
    boto3_raw_data: "type_defs.AdvancedSecurityOptionsInputTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")
    InternalUserDatabaseEnabled = field("InternalUserDatabaseEnabled")

    @cached_property
    def MasterUserOptions(self):  # pragma: no cover
        return MasterUserOptions.make_one(self.boto3_raw_data["MasterUserOptions"])

    @cached_property
    def SAMLOptions(self):  # pragma: no cover
        return SAMLOptionsInput.make_one(self.boto3_raw_data["SAMLOptions"])

    AnonymousAuthEnabled = field("AnonymousAuthEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedSecurityOptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedSecurityOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedSecurityOptions:
    boto3_raw_data: "type_defs.AdvancedSecurityOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    InternalUserDatabaseEnabled = field("InternalUserDatabaseEnabled")

    @cached_property
    def SAMLOptions(self):  # pragma: no cover
        return SAMLOptionsOutput.make_one(self.boto3_raw_data["SAMLOptions"])

    AnonymousAuthDisableDate = field("AnonymousAuthDisableDate")
    AnonymousAuthEnabled = field("AnonymousAuthEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedSecurityOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedSecurityOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Limits:
    boto3_raw_data: "type_defs.LimitsTypeDef" = dataclasses.field()

    @cached_property
    def StorageTypes(self):  # pragma: no cover
        return StorageType.make_many(self.boto3_raw_data["StorageTypes"])

    @cached_property
    def InstanceLimits(self):  # pragma: no cover
        return InstanceLimits.make_one(self.boto3_raw_data["InstanceLimits"])

    @cached_property
    def AdditionalLimits(self):  # pragma: no cover
        return AdditionalLimit.make_many(self.boto3_raw_data["AdditionalLimits"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LimitsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUpgradeHistoryResponse:
    boto3_raw_data: "type_defs.GetUpgradeHistoryResponseTypeDef" = dataclasses.field()

    @cached_property
    def UpgradeHistories(self):  # pragma: no cover
        return UpgradeHistory.make_many(self.boto3_raw_data["UpgradeHistories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUpgradeHistoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUpgradeHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainAutoTunesResponse:
    boto3_raw_data: "type_defs.DescribeDomainAutoTunesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoTunes(self):  # pragma: no cover
        return AutoTune.make_many(self.boto3_raw_data["AutoTunes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDomainAutoTunesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainAutoTunesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneOptionsStatus:
    boto3_raw_data: "type_defs.AutoTuneOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return AutoTuneOptionsExtra.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return AutoTuneStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTuneOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTuneOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTuneOptionsInput:
    boto3_raw_data: "type_defs.AutoTuneOptionsInputTypeDef" = dataclasses.field()

    DesiredState = field("DesiredState")
    MaintenanceSchedules = field("MaintenanceSchedules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTuneOptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTuneOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedSecurityOptionsStatus:
    boto3_raw_data: "type_defs.AdvancedSecurityOptionsStatusTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Options(self):  # pragma: no cover
        return AdvancedSecurityOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdvancedSecurityOptionsStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedSecurityOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchDomainStatus:
    boto3_raw_data: "type_defs.ElasticsearchDomainStatusTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    DomainName = field("DomainName")
    ARN = field("ARN")

    @cached_property
    def ElasticsearchClusterConfig(self):  # pragma: no cover
        return ElasticsearchClusterConfig.make_one(
            self.boto3_raw_data["ElasticsearchClusterConfig"]
        )

    Created = field("Created")
    Deleted = field("Deleted")
    Endpoint = field("Endpoint")
    Endpoints = field("Endpoints")
    Processing = field("Processing")
    UpgradeProcessing = field("UpgradeProcessing")
    ElasticsearchVersion = field("ElasticsearchVersion")

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptions.make_one(self.boto3_raw_data["EBSOptions"])

    AccessPolicies = field("AccessPolicies")

    @cached_property
    def SnapshotOptions(self):  # pragma: no cover
        return SnapshotOptions.make_one(self.boto3_raw_data["SnapshotOptions"])

    @cached_property
    def VPCOptions(self):  # pragma: no cover
        return VPCDerivedInfo.make_one(self.boto3_raw_data["VPCOptions"])

    @cached_property
    def CognitoOptions(self):  # pragma: no cover
        return CognitoOptions.make_one(self.boto3_raw_data["CognitoOptions"])

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    @cached_property
    def NodeToNodeEncryptionOptions(self):  # pragma: no cover
        return NodeToNodeEncryptionOptions.make_one(
            self.boto3_raw_data["NodeToNodeEncryptionOptions"]
        )

    AdvancedOptions = field("AdvancedOptions")
    LogPublishingOptions = field("LogPublishingOptions")

    @cached_property
    def ServiceSoftwareOptions(self):  # pragma: no cover
        return ServiceSoftwareOptions.make_one(
            self.boto3_raw_data["ServiceSoftwareOptions"]
        )

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def AdvancedSecurityOptions(self):  # pragma: no cover
        return AdvancedSecurityOptions.make_one(
            self.boto3_raw_data["AdvancedSecurityOptions"]
        )

    @cached_property
    def AutoTuneOptions(self):  # pragma: no cover
        return AutoTuneOptionsOutput.make_one(self.boto3_raw_data["AutoTuneOptions"])

    @cached_property
    def ChangeProgressDetails(self):  # pragma: no cover
        return ChangeProgressDetails.make_one(
            self.boto3_raw_data["ChangeProgressDetails"]
        )

    DomainProcessingStatus = field("DomainProcessingStatus")

    @cached_property
    def ModifyingProperties(self):  # pragma: no cover
        return ModifyingProperties.make_many(self.boto3_raw_data["ModifyingProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchDomainStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchDomainStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchInstanceTypeLimitsResponse:
    boto3_raw_data: (
        "type_defs.DescribeElasticsearchInstanceTypeLimitsResponseTypeDef"
    ) = dataclasses.field()

    LimitsByRole = field("LimitsByRole")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchInstanceTypeLimitsResponseTypeDef"
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
                "type_defs.DescribeElasticsearchInstanceTypeLimitsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateElasticsearchDomainRequest:
    boto3_raw_data: "type_defs.CreateElasticsearchDomainRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ElasticsearchVersion = field("ElasticsearchVersion")

    @cached_property
    def ElasticsearchClusterConfig(self):  # pragma: no cover
        return ElasticsearchClusterConfig.make_one(
            self.boto3_raw_data["ElasticsearchClusterConfig"]
        )

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptions.make_one(self.boto3_raw_data["EBSOptions"])

    AccessPolicies = field("AccessPolicies")

    @cached_property
    def SnapshotOptions(self):  # pragma: no cover
        return SnapshotOptions.make_one(self.boto3_raw_data["SnapshotOptions"])

    @cached_property
    def VPCOptions(self):  # pragma: no cover
        return VPCOptions.make_one(self.boto3_raw_data["VPCOptions"])

    @cached_property
    def CognitoOptions(self):  # pragma: no cover
        return CognitoOptions.make_one(self.boto3_raw_data["CognitoOptions"])

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    @cached_property
    def NodeToNodeEncryptionOptions(self):  # pragma: no cover
        return NodeToNodeEncryptionOptions.make_one(
            self.boto3_raw_data["NodeToNodeEncryptionOptions"]
        )

    AdvancedOptions = field("AdvancedOptions")
    LogPublishingOptions = field("LogPublishingOptions")

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def AdvancedSecurityOptions(self):  # pragma: no cover
        return AdvancedSecurityOptionsInput.make_one(
            self.boto3_raw_data["AdvancedSecurityOptions"]
        )

    @cached_property
    def AutoTuneOptions(self):  # pragma: no cover
        return AutoTuneOptionsInput.make_one(self.boto3_raw_data["AutoTuneOptions"])

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateElasticsearchDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateElasticsearchDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateElasticsearchDomainConfigRequest:
    boto3_raw_data: "type_defs.UpdateElasticsearchDomainConfigRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def ElasticsearchClusterConfig(self):  # pragma: no cover
        return ElasticsearchClusterConfig.make_one(
            self.boto3_raw_data["ElasticsearchClusterConfig"]
        )

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptions.make_one(self.boto3_raw_data["EBSOptions"])

    @cached_property
    def SnapshotOptions(self):  # pragma: no cover
        return SnapshotOptions.make_one(self.boto3_raw_data["SnapshotOptions"])

    @cached_property
    def VPCOptions(self):  # pragma: no cover
        return VPCOptions.make_one(self.boto3_raw_data["VPCOptions"])

    @cached_property
    def CognitoOptions(self):  # pragma: no cover
        return CognitoOptions.make_one(self.boto3_raw_data["CognitoOptions"])

    AdvancedOptions = field("AdvancedOptions")
    AccessPolicies = field("AccessPolicies")
    LogPublishingOptions = field("LogPublishingOptions")

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def AdvancedSecurityOptions(self):  # pragma: no cover
        return AdvancedSecurityOptionsInput.make_one(
            self.boto3_raw_data["AdvancedSecurityOptions"]
        )

    @cached_property
    def NodeToNodeEncryptionOptions(self):  # pragma: no cover
        return NodeToNodeEncryptionOptions.make_one(
            self.boto3_raw_data["NodeToNodeEncryptionOptions"]
        )

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    AutoTuneOptions = field("AutoTuneOptions")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateElasticsearchDomainConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateElasticsearchDomainConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchDomainConfig:
    boto3_raw_data: "type_defs.ElasticsearchDomainConfigTypeDef" = dataclasses.field()

    @cached_property
    def ElasticsearchVersion(self):  # pragma: no cover
        return ElasticsearchVersionStatus.make_one(
            self.boto3_raw_data["ElasticsearchVersion"]
        )

    @cached_property
    def ElasticsearchClusterConfig(self):  # pragma: no cover
        return ElasticsearchClusterConfigStatus.make_one(
            self.boto3_raw_data["ElasticsearchClusterConfig"]
        )

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptionsStatus.make_one(self.boto3_raw_data["EBSOptions"])

    @cached_property
    def AccessPolicies(self):  # pragma: no cover
        return AccessPoliciesStatus.make_one(self.boto3_raw_data["AccessPolicies"])

    @cached_property
    def SnapshotOptions(self):  # pragma: no cover
        return SnapshotOptionsStatus.make_one(self.boto3_raw_data["SnapshotOptions"])

    @cached_property
    def VPCOptions(self):  # pragma: no cover
        return VPCDerivedInfoStatus.make_one(self.boto3_raw_data["VPCOptions"])

    @cached_property
    def CognitoOptions(self):  # pragma: no cover
        return CognitoOptionsStatus.make_one(self.boto3_raw_data["CognitoOptions"])

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptionsStatus.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    @cached_property
    def NodeToNodeEncryptionOptions(self):  # pragma: no cover
        return NodeToNodeEncryptionOptionsStatus.make_one(
            self.boto3_raw_data["NodeToNodeEncryptionOptions"]
        )

    @cached_property
    def AdvancedOptions(self):  # pragma: no cover
        return AdvancedOptionsStatus.make_one(self.boto3_raw_data["AdvancedOptions"])

    @cached_property
    def LogPublishingOptions(self):  # pragma: no cover
        return LogPublishingOptionsStatus.make_one(
            self.boto3_raw_data["LogPublishingOptions"]
        )

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptionsStatus.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def AdvancedSecurityOptions(self):  # pragma: no cover
        return AdvancedSecurityOptionsStatus.make_one(
            self.boto3_raw_data["AdvancedSecurityOptions"]
        )

    @cached_property
    def AutoTuneOptions(self):  # pragma: no cover
        return AutoTuneOptionsStatus.make_one(self.boto3_raw_data["AutoTuneOptions"])

    @cached_property
    def ChangeProgressDetails(self):  # pragma: no cover
        return ChangeProgressDetails.make_one(
            self.boto3_raw_data["ChangeProgressDetails"]
        )

    @cached_property
    def ModifyingProperties(self):  # pragma: no cover
        return ModifyingProperties.make_many(self.boto3_raw_data["ModifyingProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchDomainConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchDomainConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateElasticsearchDomainResponse:
    boto3_raw_data: "type_defs.CreateElasticsearchDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return ElasticsearchDomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateElasticsearchDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateElasticsearchDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteElasticsearchDomainResponse:
    boto3_raw_data: "type_defs.DeleteElasticsearchDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return ElasticsearchDomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteElasticsearchDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteElasticsearchDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchDomainResponse:
    boto3_raw_data: "type_defs.DescribeElasticsearchDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return ElasticsearchDomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticsearchDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchDomainsResponse:
    boto3_raw_data: "type_defs.DescribeElasticsearchDomainsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainStatusList(self):  # pragma: no cover
        return ElasticsearchDomainStatus.make_many(
            self.boto3_raw_data["DomainStatusList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchDomainsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticsearchDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeElasticsearchDomainConfigResponse:
    boto3_raw_data: "type_defs.DescribeElasticsearchDomainConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainConfig(self):  # pragma: no cover
        return ElasticsearchDomainConfig.make_one(self.boto3_raw_data["DomainConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeElasticsearchDomainConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeElasticsearchDomainConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateElasticsearchDomainConfigResponse:
    boto3_raw_data: "type_defs.UpdateElasticsearchDomainConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainConfig(self):  # pragma: no cover
        return ElasticsearchDomainConfig.make_one(self.boto3_raw_data["DomainConfig"])

    @cached_property
    def DryRunResults(self):  # pragma: no cover
        return DryRunResults.make_one(self.boto3_raw_data["DryRunResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateElasticsearchDomainConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateElasticsearchDomainConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
