# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opensearch import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class NaturalLanguageQueryGenerationOptionsInput:
    boto3_raw_data: "type_defs.NaturalLanguageQueryGenerationOptionsInputTypeDef" = (
        dataclasses.field()
    )

    DesiredState = field("DesiredState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NaturalLanguageQueryGenerationOptionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NaturalLanguageQueryGenerationOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3VectorsEngine:
    boto3_raw_data: "type_defs.S3VectorsEngineTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3VectorsEngineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3VectorsEngineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NaturalLanguageQueryGenerationOptionsOutput:
    boto3_raw_data: "type_defs.NaturalLanguageQueryGenerationOptionsOutputTypeDef" = (
        dataclasses.field()
    )

    DesiredState = field("DesiredState")
    CurrentState = field("CurrentState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NaturalLanguageQueryGenerationOptionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NaturalLanguageQueryGenerationOptionsOutputTypeDef"]
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
class AWSDomainInformation:
    boto3_raw_data: "type_defs.AWSDomainInformationTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    OwnerId = field("OwnerId")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AWSDomainInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AWSDomainInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptInboundConnectionRequest:
    boto3_raw_data: "type_defs.AcceptInboundConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionId = field("ConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceptInboundConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptInboundConnectionRequestTypeDef"]
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
class IAMFederationOptionsInput:
    boto3_raw_data: "type_defs.IAMFederationOptionsInputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IAMFederationOptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IAMFederationOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JWTOptionsInput:
    boto3_raw_data: "type_defs.JWTOptionsInputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")
    PublicKey = field("PublicKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JWTOptionsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JWTOptionsInputTypeDef"]],
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
class IAMFederationOptionsOutput:
    boto3_raw_data: "type_defs.IAMFederationOptionsOutputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IAMFederationOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IAMFederationOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JWTOptionsOutput:
    boto3_raw_data: "type_defs.JWTOptionsOutputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")
    PublicKey = field("PublicKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JWTOptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JWTOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppConfig:
    boto3_raw_data: "type_defs.AppConfigTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSummary:
    boto3_raw_data: "type_defs.ApplicationSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    endpoint = field("endpoint")
    status = field("status")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSummaryTypeDef"]
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
    Service = field("Service")

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
    UseOffPeakWindow = field("UseOffPeakWindow")

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
class AvailabilityZoneInfo:
    boto3_raw_data: "type_defs.AvailabilityZoneInfoTypeDef" = dataclasses.field()

    AvailabilityZoneName = field("AvailabilityZoneName")
    ZoneStatus = field("ZoneStatus")
    ConfiguredDataNodeCount = field("ConfiguredDataNodeCount")
    AvailableDataNodeCount = field("AvailableDataNodeCount")
    TotalShards = field("TotalShards")
    TotalUnAssignedShards = field("TotalUnAssignedShards")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneInfoTypeDef"]
        ],
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
class CancelServiceSoftwareUpdateRequest:
    boto3_raw_data: "type_defs.CancelServiceSoftwareUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelServiceSoftwareUpdateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelServiceSoftwareUpdateRequestTypeDef"]
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
    InitiatedBy = field("InitiatedBy")
    StartTime = field("StartTime")
    LastUpdatedTime = field("LastUpdatedTime")

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
class CloudWatchDirectQueryDataSource:
    boto3_raw_data: "type_defs.CloudWatchDirectQueryDataSourceTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchDirectQueryDataSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchDirectQueryDataSourceTypeDef"]
        ],
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
class CrossClusterSearchConnectionProperties:
    boto3_raw_data: "type_defs.CrossClusterSearchConnectionPropertiesTypeDef" = (
        dataclasses.field()
    )

    SkipUnavailable = field("SkipUnavailable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CrossClusterSearchConnectionPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossClusterSearchConnectionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    dataSourceArn = field("dataSourceArn")
    dataSourceDescription = field("dataSourceDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamIdentityCenterOptionsInput:
    boto3_raw_data: "type_defs.IamIdentityCenterOptionsInputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    iamIdentityCenterInstanceArn = field("iamIdentityCenterInstanceArn")
    iamRoleForIdentityCenterApplicationArn = field(
        "iamRoleForIdentityCenterApplicationArn"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IamIdentityCenterOptionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamIdentityCenterOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamIdentityCenterOptions:
    boto3_raw_data: "type_defs.IamIdentityCenterOptionsTypeDef" = dataclasses.field()

    enabled = field("enabled")
    iamIdentityCenterInstanceArn = field("iamIdentityCenterInstanceArn")
    iamRoleForIdentityCenterApplicationArn = field(
        "iamRoleForIdentityCenterApplicationArn"
    )
    iamIdentityCenterApplicationArn = field("iamIdentityCenterApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamIdentityCenterOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamIdentityCenterOptionsTypeDef"]
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
class IdentityCenterOptionsInput:
    boto3_raw_data: "type_defs.IdentityCenterOptionsInputTypeDef" = dataclasses.field()

    EnabledAPIAccess = field("EnabledAPIAccess")
    IdentityCenterInstanceARN = field("IdentityCenterInstanceARN")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterOptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterOptionsInputTypeDef"]
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
class SoftwareUpdateOptions:
    boto3_raw_data: "type_defs.SoftwareUpdateOptionsTypeDef" = dataclasses.field()

    AutoSoftwareUpdateEnabled = field("AutoSoftwareUpdateEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SoftwareUpdateOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SoftwareUpdateOptionsTypeDef"]
        ],
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
class OutboundConnectionStatus:
    boto3_raw_data: "type_defs.OutboundConnectionStatusTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundConnectionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundConnectionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageConfiguration:
    boto3_raw_data: "type_defs.PackageConfigurationTypeDef" = dataclasses.field()

    LicenseRequirement = field("LicenseRequirement")
    ConfigurationRequirement = field("ConfigurationRequirement")
    LicenseFilepath = field("LicenseFilepath")
    RequiresRestartForConfigurationUpdate = field(
        "RequiresRestartForConfigurationUpdate"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageEncryptionOptions:
    boto3_raw_data: "type_defs.PackageEncryptionOptionsTypeDef" = dataclasses.field()

    EncryptionEnabled = field("EncryptionEnabled")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageEncryptionOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageEncryptionOptionsTypeDef"]
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
class PackageVendingOptions:
    boto3_raw_data: "type_defs.PackageVendingOptionsTypeDef" = dataclasses.field()

    VendingEnabled = field("VendingEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVendingOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVendingOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3GlueDataCatalog:
    boto3_raw_data: "type_defs.S3GlueDataCatalogTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3GlueDataCatalogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3GlueDataCatalogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteDataSourceRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectQueryDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteDirectQueryDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    DataSourceName = field("DataSourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectQueryDataSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectQueryDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInboundConnectionRequest:
    boto3_raw_data: "type_defs.DeleteInboundConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionId = field("ConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInboundConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInboundConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutboundConnectionRequest:
    boto3_raw_data: "type_defs.DeleteOutboundConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionId = field("ConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteOutboundConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOutboundConnectionRequestTypeDef"]
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
class DescribeDomainConfigRequest:
    boto3_raw_data: "type_defs.DescribeDomainConfigRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainHealthRequest:
    boto3_raw_data: "type_defs.DescribeDomainHealthRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainHealthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainHealthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainNodesRequest:
    boto3_raw_data: "type_defs.DescribeDomainNodesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainNodesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNodesStatus:
    boto3_raw_data: "type_defs.DomainNodesStatusTypeDef" = dataclasses.field()

    NodeId = field("NodeId")
    NodeType = field("NodeType")
    AvailabilityZone = field("AvailabilityZone")
    InstanceType = field("InstanceType")
    NodeStatus = field("NodeStatus")
    StorageType = field("StorageType")
    StorageVolumeType = field("StorageVolumeType")
    StorageSize = field("StorageSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainNodesStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNodesStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainRequest:
    boto3_raw_data: "type_defs.DescribeDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainsRequest:
    boto3_raw_data: "type_defs.DescribeDomainsRequestTypeDef" = dataclasses.field()

    DomainNames = field("DomainNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDryRunProgressRequest:
    boto3_raw_data: "type_defs.DescribeDryRunProgressRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    DryRunId = field("DryRunId")
    LoadDryRunConfig = field("LoadDryRunConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDryRunProgressRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDryRunProgressRequestTypeDef"]
        ],
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
class DescribeInstanceTypeLimitsRequest:
    boto3_raw_data: "type_defs.DescribeInstanceTypeLimitsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceType = field("InstanceType")
    EngineVersion = field("EngineVersion")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceTypeLimitsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceTypeLimitsRequestTypeDef"]
        ],
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
class DescribeReservedInstanceOfferingsRequest:
    boto3_raw_data: "type_defs.DescribeReservedInstanceOfferingsRequestTypeDef" = (
        dataclasses.field()
    )

    ReservedInstanceOfferingId = field("ReservedInstanceOfferingId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedInstanceOfferingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedInstanceOfferingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedInstancesRequest:
    boto3_raw_data: "type_defs.DescribeReservedInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    ReservedInstanceId = field("ReservedInstanceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReservedInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedInstancesRequestTypeDef"]
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
class SecurityLakeDirectQueryDataSource:
    boto3_raw_data: "type_defs.SecurityLakeDirectQueryDataSourceTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecurityLakeDirectQueryDataSourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityLakeDirectQueryDataSourceTypeDef"]
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
class DissociatePackagesRequest:
    boto3_raw_data: "type_defs.DissociatePackagesRequestTypeDef" = dataclasses.field()

    PackageList = field("PackageList")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DissociatePackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DissociatePackagesRequestTypeDef"]
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
class DomainMaintenanceDetails:
    boto3_raw_data: "type_defs.DomainMaintenanceDetailsTypeDef" = dataclasses.field()

    MaintenanceId = field("MaintenanceId")
    DomainName = field("DomainName")
    Action = field("Action")
    NodeId = field("NodeId")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainMaintenanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainMaintenanceDetailsTypeDef"]
        ],
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
class IdentityCenterOptions:
    boto3_raw_data: "type_defs.IdentityCenterOptionsTypeDef" = dataclasses.field()

    EnabledAPIAccess = field("EnabledAPIAccess")
    IdentityCenterInstanceARN = field("IdentityCenterInstanceARN")
    SubjectKey = field("SubjectKey")
    RolesKey = field("RolesKey")
    IdentityCenterApplicationARN = field("IdentityCenterApplicationARN")
    IdentityStoreId = field("IdentityStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterOptionsTypeDef"]
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
class ValidationFailure:
    boto3_raw_data: "type_defs.ValidationFailureTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationFailureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRequest:
    boto3_raw_data: "type_defs.GetApplicationRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompatibleVersionsRequest:
    boto3_raw_data: "type_defs.GetCompatibleVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCompatibleVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompatibleVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceRequest:
    boto3_raw_data: "type_defs.GetDataSourceRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectQueryDataSourceRequest:
    boto3_raw_data: "type_defs.GetDirectQueryDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    DataSourceName = field("DataSourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDirectQueryDataSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectQueryDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainMaintenanceStatusRequest:
    boto3_raw_data: "type_defs.GetDomainMaintenanceStatusRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    MaintenanceId = field("MaintenanceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainMaintenanceStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainMaintenanceStatusRequestTypeDef"]
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
class InboundConnectionStatus:
    boto3_raw_data: "type_defs.InboundConnectionStatusTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InboundConnectionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundConnectionStatusTypeDef"]
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
class InstanceTypeDetails:
    boto3_raw_data: "type_defs.InstanceTypeDetailsTypeDef" = dataclasses.field()

    InstanceType = field("InstanceType")
    EncryptionEnabled = field("EncryptionEnabled")
    CognitoEnabled = field("CognitoEnabled")
    AppLogsEnabled = field("AppLogsEnabled")
    AdvancedSecurityEnabled = field("AdvancedSecurityEnabled")
    WarmEnabled = field("WarmEnabled")
    InstanceRole = field("InstanceRole")
    AvailabilityZones = field("AvailabilityZones")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceTypeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyStoreAccessOption:
    boto3_raw_data: "type_defs.KeyStoreAccessOptionTypeDef" = dataclasses.field()

    KeyStoreAccessEnabled = field("KeyStoreAccessEnabled")
    KeyAccessRoleArn = field("KeyAccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyStoreAccessOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyStoreAccessOptionTypeDef"]
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
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    statuses = field("statuses")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesRequest:
    boto3_raw_data: "type_defs.ListDataSourcesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectQueryDataSourcesRequest:
    boto3_raw_data: "type_defs.ListDirectQueryDataSourcesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDirectQueryDataSourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectQueryDataSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainMaintenancesRequest:
    boto3_raw_data: "type_defs.ListDomainMaintenancesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Action = field("Action")
    Status = field("Status")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainMaintenancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainMaintenancesRequestTypeDef"]
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
class ListInstanceTypeDetailsRequest:
    boto3_raw_data: "type_defs.ListInstanceTypeDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    EngineVersion = field("EngineVersion")
    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    RetrieveAZs = field("RetrieveAZs")
    InstanceType = field("InstanceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceTypeDetailsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceTypeDetailsRequestTypeDef"]
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
class ListScheduledActionsRequest:
    boto3_raw_data: "type_defs.ListScheduledActionsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduledActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledAction:
    boto3_raw_data: "type_defs.ScheduledActionTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    Severity = field("Severity")
    ScheduledTime = field("ScheduledTime")
    Description = field("Description")
    ScheduledBy = field("ScheduledBy")
    Status = field("Status")
    Mandatory = field("Mandatory")
    Cancellable = field("Cancellable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduledActionTypeDef"]],
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
class ListVersionsRequest:
    boto3_raw_data: "type_defs.ListVersionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsRequestTypeDef"]
        ],
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
class NodeConfig:
    boto3_raw_data: "type_defs.NodeConfigTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Type = field("Type")
    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WindowStartTime:
    boto3_raw_data: "type_defs.WindowStartTimeTypeDef" = dataclasses.field()

    Hours = field("Hours")
    Minutes = field("Minutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WindowStartTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WindowStartTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginProperties:
    boto3_raw_data: "type_defs.PluginPropertiesTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Version = field("Version")
    ClassName = field("ClassName")
    UncompressedSizeInBytes = field("UncompressedSizeInBytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PluginPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PluginPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedInstanceOfferingRequest:
    boto3_raw_data: "type_defs.PurchaseReservedInstanceOfferingRequestTypeDef" = (
        dataclasses.field()
    )

    ReservedInstanceOfferingId = field("ReservedInstanceOfferingId")
    ReservationName = field("ReservationName")
    InstanceCount = field("InstanceCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedInstanceOfferingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedInstanceOfferingRequestTypeDef"]
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
class RejectInboundConnectionRequest:
    boto3_raw_data: "type_defs.RejectInboundConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionId = field("ConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectInboundConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectInboundConnectionRequestTypeDef"]
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
    Service = field("Service")

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
class StartDomainMaintenanceRequest:
    boto3_raw_data: "type_defs.StartDomainMaintenanceRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Action = field("Action")
    NodeId = field("NodeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDomainMaintenanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDomainMaintenanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartServiceSoftwareUpdateRequest:
    boto3_raw_data: "type_defs.StartServiceSoftwareUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ScheduleAt = field("ScheduleAt")
    DesiredStartTime = field("DesiredStartTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartServiceSoftwareUpdateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartServiceSoftwareUpdateRequestTypeDef"]
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
class UpdatePackageScopeRequest:
    boto3_raw_data: "type_defs.UpdatePackageScopeRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    Operation = field("Operation")
    PackageUserList = field("PackageUserList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageScopeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScheduledActionRequest:
    boto3_raw_data: "type_defs.UpdateScheduledActionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ActionID = field("ActionID")
    ActionType = field("ActionType")
    ScheduleAt = field("ScheduleAt")
    DesiredStartTime = field("DesiredStartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduledActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduledActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeDomainRequest:
    boto3_raw_data: "type_defs.UpgradeDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    TargetVersion = field("TargetVersion")
    PerformCheckOnly = field("PerformCheckOnly")
    AdvancedOptions = field("AdvancedOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeDomainRequestTypeDef"]
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
class AIMLOptionsInput:
    boto3_raw_data: "type_defs.AIMLOptionsInputTypeDef" = dataclasses.field()

    @cached_property
    def NaturalLanguageQueryGenerationOptions(self):  # pragma: no cover
        return NaturalLanguageQueryGenerationOptionsInput.make_one(
            self.boto3_raw_data["NaturalLanguageQueryGenerationOptions"]
        )

    @cached_property
    def S3VectorsEngine(self):  # pragma: no cover
        return S3VectorsEngine.make_one(self.boto3_raw_data["S3VectorsEngine"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIMLOptionsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIMLOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AIMLOptionsOutput:
    boto3_raw_data: "type_defs.AIMLOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def NaturalLanguageQueryGenerationOptions(self):  # pragma: no cover
        return NaturalLanguageQueryGenerationOptionsOutput.make_one(
            self.boto3_raw_data["NaturalLanguageQueryGenerationOptions"]
        )

    @cached_property
    def S3VectorsEngine(self):  # pragma: no cover
        return S3VectorsEngine.make_one(self.boto3_raw_data["S3VectorsEngine"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIMLOptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIMLOptionsOutputTypeDef"]
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
class IPAddressTypeStatus:
    boto3_raw_data: "type_defs.IPAddressTypeStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IPAddressTypeStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IPAddressTypeStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionStatus:
    boto3_raw_data: "type_defs.VersionStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VersionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VersionStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainInformationContainer:
    boto3_raw_data: "type_defs.DomainInformationContainerTypeDef" = dataclasses.field()

    @cached_property
    def AWSDomainInformation(self):  # pragma: no cover
        return AWSDomainInformation.make_one(
            self.boto3_raw_data["AWSDomainInformation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainInformationContainerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainInformationContainerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddDataSourceResponse:
    boto3_raw_data: "type_defs.AddDataSourceResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddDirectQueryDataSourceResponse:
    boto3_raw_data: "type_defs.AddDirectQueryDataSourceResponseTypeDef" = (
        dataclasses.field()
    )

    DataSourceArn = field("DataSourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddDirectQueryDataSourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddDirectQueryDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceResponse:
    boto3_raw_data: "type_defs.DeleteDataSourceResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceResponseTypeDef"]
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
class GetDomainMaintenanceStatusResponse:
    boto3_raw_data: "type_defs.GetDomainMaintenanceStatusResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    StatusMessage = field("StatusMessage")
    NodeId = field("NodeId")
    Action = field("Action")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainMaintenanceStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainMaintenanceStatusResponseTypeDef"]
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
class ListVersionsResponse:
    boto3_raw_data: "type_defs.ListVersionsResponseTypeDef" = dataclasses.field()

    Versions = field("Versions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedInstanceOfferingResponse:
    boto3_raw_data: "type_defs.PurchaseReservedInstanceOfferingResponseTypeDef" = (
        dataclasses.field()
    )

    ReservedInstanceId = field("ReservedInstanceId")
    ReservationName = field("ReservationName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedInstanceOfferingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedInstanceOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDomainMaintenanceResponse:
    boto3_raw_data: "type_defs.StartDomainMaintenanceResponseTypeDef" = (
        dataclasses.field()
    )

    MaintenanceId = field("MaintenanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDomainMaintenanceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDomainMaintenanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceResponse:
    boto3_raw_data: "type_defs.UpdateDataSourceResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectQueryDataSourceResponse:
    boto3_raw_data: "type_defs.UpdateDirectQueryDataSourceResponseTypeDef" = (
        dataclasses.field()
    )

    DataSourceArn = field("DataSourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectQueryDataSourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectQueryDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageScopeResponse:
    boto3_raw_data: "type_defs.UpdatePackageScopeResponseTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    Operation = field("Operation")
    PackageUserList = field("PackageUserList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageScopeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageScopeResponseTypeDef"]
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
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationSummaries(self):  # pragma: no cover
        return ApplicationSummary.make_many(self.boto3_raw_data["ApplicationSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
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
class EnvironmentInfo:
    boto3_raw_data: "type_defs.EnvironmentInfoTypeDef" = dataclasses.field()

    @cached_property
    def AvailabilityZoneInformation(self):  # pragma: no cover
        return AvailabilityZoneInfo.make_many(
            self.boto3_raw_data["AvailabilityZoneInformation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentInfoTypeDef"]],
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

    CancelledChangeIds = field("CancelledChangeIds")

    @cached_property
    def CancelledChangeProperties(self):  # pragma: no cover
        return CancelledChangeProperty.make_many(
            self.boto3_raw_data["CancelledChangeProperties"]
        )

    DryRun = field("DryRun")

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
class CancelServiceSoftwareUpdateResponse:
    boto3_raw_data: "type_defs.CancelServiceSoftwareUpdateResponseTypeDef" = (
        dataclasses.field()
    )

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
            "type_defs.CancelServiceSoftwareUpdateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelServiceSoftwareUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartServiceSoftwareUpdateResponse:
    boto3_raw_data: "type_defs.StartServiceSoftwareUpdateResponseTypeDef" = (
        dataclasses.field()
    )

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
            "type_defs.StartServiceSoftwareUpdateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartServiceSoftwareUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeDomainResponse:
    boto3_raw_data: "type_defs.UpgradeDomainResponseTypeDef" = dataclasses.field()

    UpgradeId = field("UpgradeId")
    DomainName = field("DomainName")
    TargetVersion = field("TargetVersion")
    PerformCheckOnly = field("PerformCheckOnly")
    AdvancedOptions = field("AdvancedOptions")

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
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeDomainResponseTypeDef"]
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

    LastUpdatedTime = field("LastUpdatedTime")
    ConfigChangeStatus = field("ConfigChangeStatus")
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
class GetCompatibleVersionsResponse:
    boto3_raw_data: "type_defs.GetCompatibleVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CompatibleVersions(self):  # pragma: no cover
        return CompatibleVersionsMap.make_many(
            self.boto3_raw_data["CompatibleVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCompatibleVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompatibleVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionProperties:
    boto3_raw_data: "type_defs.ConnectionPropertiesTypeDef" = dataclasses.field()

    Endpoint = field("Endpoint")

    @cached_property
    def CrossClusterSearch(self):  # pragma: no cover
        return CrossClusterSearchConnectionProperties.make_one(
            self.boto3_raw_data["CrossClusterSearch"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def appConfigs(self):  # pragma: no cover
        return AppConfig.make_many(self.boto3_raw_data["appConfigs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    name = field("name")
    clientToken = field("clientToken")

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def iamIdentityCenterOptions(self):  # pragma: no cover
        return IamIdentityCenterOptionsInput.make_one(
            self.boto3_raw_data["iamIdentityCenterOptions"]
        )

    @cached_property
    def appConfigs(self):  # pragma: no cover
        return AppConfig.make_many(self.boto3_raw_data["appConfigs"])

    @cached_property
    def tagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def iamIdentityCenterOptions(self):  # pragma: no cover
        return IamIdentityCenterOptions.make_one(
            self.boto3_raw_data["iamIdentityCenterOptions"]
        )

    @cached_property
    def appConfigs(self):  # pragma: no cover
        return AppConfig.make_many(self.boto3_raw_data["appConfigs"])

    @cached_property
    def tagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tagList"])

    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationResponse:
    boto3_raw_data: "type_defs.GetApplicationResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    endpoint = field("endpoint")
    status = field("status")

    @cached_property
    def iamIdentityCenterOptions(self):  # pragma: no cover
        return IamIdentityCenterOptions.make_one(
            self.boto3_raw_data["iamIdentityCenterOptions"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def appConfigs(self):  # pragma: no cover
        return AppConfig.make_many(self.boto3_raw_data["appConfigs"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResponse:
    boto3_raw_data: "type_defs.UpdateApplicationResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

    @cached_property
    def iamIdentityCenterOptions(self):  # pragma: no cover
        return IamIdentityCenterOptions.make_one(
            self.boto3_raw_data["iamIdentityCenterOptions"]
        )

    @cached_property
    def appConfigs(self):  # pragma: no cover
        return AppConfig.make_many(self.boto3_raw_data["appConfigs"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResponseTypeDef"]
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
class SoftwareUpdateOptionsStatus:
    boto3_raw_data: "type_defs.SoftwareUpdateOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return SoftwareUpdateOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SoftwareUpdateOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SoftwareUpdateOptionsStatusTypeDef"]
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
class UpdatePackageRequest:
    boto3_raw_data: "type_defs.UpdatePackageRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")

    @cached_property
    def PackageSource(self):  # pragma: no cover
        return PackageSource.make_one(self.boto3_raw_data["PackageSource"])

    PackageDescription = field("PackageDescription")
    CommitMessage = field("CommitMessage")

    @cached_property
    def PackageConfiguration(self):  # pragma: no cover
        return PackageConfiguration.make_one(
            self.boto3_raw_data["PackageConfiguration"]
        )

    @cached_property
    def PackageEncryptionOptions(self):  # pragma: no cover
        return PackageEncryptionOptions.make_one(
            self.boto3_raw_data["PackageEncryptionOptions"]
        )

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
class CreatePackageRequest:
    boto3_raw_data: "type_defs.CreatePackageRequestTypeDef" = dataclasses.field()

    PackageName = field("PackageName")
    PackageType = field("PackageType")

    @cached_property
    def PackageSource(self):  # pragma: no cover
        return PackageSource.make_one(self.boto3_raw_data["PackageSource"])

    PackageDescription = field("PackageDescription")

    @cached_property
    def PackageConfiguration(self):  # pragma: no cover
        return PackageConfiguration.make_one(
            self.boto3_raw_data["PackageConfiguration"]
        )

    EngineVersion = field("EngineVersion")

    @cached_property
    def PackageVendingOptions(self):  # pragma: no cover
        return PackageVendingOptions.make_one(
            self.boto3_raw_data["PackageVendingOptions"]
        )

    @cached_property
    def PackageEncryptionOptions(self):  # pragma: no cover
        return PackageEncryptionOptions.make_one(
            self.boto3_raw_data["PackageEncryptionOptions"]
        )

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
class DataSourceType:
    boto3_raw_data: "type_defs.DataSourceTypeTypeDef" = dataclasses.field()

    @cached_property
    def S3GlueDataCatalog(self):  # pragma: no cover
        return S3GlueDataCatalog.make_one(self.boto3_raw_data["S3GlueDataCatalog"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeTypeDef"]],
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
class DescribeDomainNodesResponse:
    boto3_raw_data: "type_defs.DescribeDomainNodesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainNodesStatusList(self):  # pragma: no cover
        return DomainNodesStatus.make_many(self.boto3_raw_data["DomainNodesStatusList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainNodesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundConnectionsRequest:
    boto3_raw_data: "type_defs.DescribeInboundConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundConnectionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInboundConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOutboundConnectionsRequest:
    boto3_raw_data: "type_defs.DescribeOutboundConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOutboundConnectionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOutboundConnectionsRequestTypeDef"]
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
class DirectQueryDataSourceType:
    boto3_raw_data: "type_defs.DirectQueryDataSourceTypeTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchLog(self):  # pragma: no cover
        return CloudWatchDirectQueryDataSource.make_one(
            self.boto3_raw_data["CloudWatchLog"]
        )

    @cached_property
    def SecurityLake(self):  # pragma: no cover
        return SecurityLakeDirectQueryDataSource.make_one(
            self.boto3_raw_data["SecurityLake"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectQueryDataSourceTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectQueryDataSourceTypeTypeDef"]
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
class ListDomainMaintenancesResponse:
    boto3_raw_data: "type_defs.ListDomainMaintenancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainMaintenances(self):  # pragma: no cover
        return DomainMaintenanceDetails.make_many(
            self.boto3_raw_data["DomainMaintenances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainMaintenancesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainMaintenancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityCenterOptionsStatus:
    boto3_raw_data: "type_defs.IdentityCenterOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return IdentityCenterOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterOptionsStatusTypeDef"]
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
class DryRunProgressStatus:
    boto3_raw_data: "type_defs.DryRunProgressStatusTypeDef" = dataclasses.field()

    DryRunId = field("DryRunId")
    DryRunStatus = field("DryRunStatus")
    CreationDate = field("CreationDate")
    UpdateDate = field("UpdateDate")

    @cached_property
    def ValidationFailures(self):  # pragma: no cover
        return ValidationFailure.make_many(self.boto3_raw_data["ValidationFailures"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DryRunProgressStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DryRunProgressStatusTypeDef"]
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
class ListInstanceTypeDetailsResponse:
    boto3_raw_data: "type_defs.ListInstanceTypeDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceTypeDetails(self):  # pragma: no cover
        return InstanceTypeDetails.make_many(self.boto3_raw_data["InstanceTypeDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceTypeDetailsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceTypeDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageAssociationConfiguration:
    boto3_raw_data: "type_defs.PackageAssociationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def KeyStoreAccessOption(self):  # pragma: no cover
        return KeyStoreAccessOption.make_one(
            self.boto3_raw_data["KeyStoreAccessOption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PackageAssociationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageAssociationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    statuses = field("statuses")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledActionsResponse:
    boto3_raw_data: "type_defs.ListScheduledActionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduledActions(self):  # pragma: no cover
        return ScheduledAction.make_many(self.boto3_raw_data["ScheduledActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduledActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScheduledActionResponse:
    boto3_raw_data: "type_defs.UpdateScheduledActionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScheduledAction(self):  # pragma: no cover
        return ScheduledAction.make_one(self.boto3_raw_data["ScheduledAction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateScheduledActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduledActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOption:
    boto3_raw_data: "type_defs.NodeOptionTypeDef" = dataclasses.field()

    NodeType = field("NodeType")

    @cached_property
    def NodeConfig(self):  # pragma: no cover
        return NodeConfig.make_one(self.boto3_raw_data["NodeConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OffPeakWindow:
    boto3_raw_data: "type_defs.OffPeakWindowTypeDef" = dataclasses.field()

    @cached_property
    def WindowStartTime(self):  # pragma: no cover
        return WindowStartTime.make_one(self.boto3_raw_data["WindowStartTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OffPeakWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OffPeakWindowTypeDef"]],
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

    EngineVersion = field("EngineVersion")

    @cached_property
    def AvailablePluginProperties(self):  # pragma: no cover
        return PluginProperties.make_one(
            self.boto3_raw_data["AvailablePluginProperties"]
        )

    @cached_property
    def AvailablePackageConfiguration(self):  # pragma: no cover
        return PackageConfiguration.make_one(
            self.boto3_raw_data["AvailablePackageConfiguration"]
        )

    AllowListedUserList = field("AllowListedUserList")
    PackageOwner = field("PackageOwner")

    @cached_property
    def PackageVendingOptions(self):  # pragma: no cover
        return PackageVendingOptions.make_one(
            self.boto3_raw_data["PackageVendingOptions"]
        )

    @cached_property
    def PackageEncryptionOptions(self):  # pragma: no cover
        return PackageEncryptionOptions.make_one(
            self.boto3_raw_data["PackageEncryptionOptions"]
        )

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
class PackageVersionHistory:
    boto3_raw_data: "type_defs.PackageVersionHistoryTypeDef" = dataclasses.field()

    PackageVersion = field("PackageVersion")
    CommitMessage = field("CommitMessage")
    CreatedAt = field("CreatedAt")

    @cached_property
    def PluginProperties(self):  # pragma: no cover
        return PluginProperties.make_one(self.boto3_raw_data["PluginProperties"])

    @cached_property
    def PackageConfiguration(self):  # pragma: no cover
        return PackageConfiguration.make_one(
            self.boto3_raw_data["PackageConfiguration"]
        )

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
class ReservedInstanceOffering:
    boto3_raw_data: "type_defs.ReservedInstanceOfferingTypeDef" = dataclasses.field()

    ReservedInstanceOfferingId = field("ReservedInstanceOfferingId")
    InstanceType = field("InstanceType")
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
        cls, boto3_raw_data: T.Optional["type_defs.ReservedInstanceOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedInstanceOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedInstance:
    boto3_raw_data: "type_defs.ReservedInstanceTypeDef" = dataclasses.field()

    ReservationName = field("ReservationName")
    ReservedInstanceId = field("ReservedInstanceId")
    BillingSubscriptionId = field("BillingSubscriptionId")
    ReservedInstanceOfferingId = field("ReservedInstanceOfferingId")
    InstanceType = field("InstanceType")
    StartTime = field("StartTime")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    InstanceCount = field("InstanceCount")
    State = field("State")
    PaymentOption = field("PaymentOption")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservedInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedInstanceTypeDef"]
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
class AIMLOptionsStatus:
    boto3_raw_data: "type_defs.AIMLOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return AIMLOptionsOutput.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AIMLOptionsStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AIMLOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundConnection:
    boto3_raw_data: "type_defs.InboundConnectionTypeDef" = dataclasses.field()

    @cached_property
    def LocalDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["LocalDomainInfo"]
        )

    @cached_property
    def RemoteDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["RemoteDomainInfo"]
        )

    ConnectionId = field("ConnectionId")

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return InboundConnectionStatus.make_one(self.boto3_raw_data["ConnectionStatus"])

    ConnectionMode = field("ConnectionMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InboundConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundConnectionTypeDef"]
        ],
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

    UseOffPeakWindow = field("UseOffPeakWindow")

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

    UseOffPeakWindow = field("UseOffPeakWindow")

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
class DescribeDomainHealthResponse:
    boto3_raw_data: "type_defs.DescribeDomainHealthResponseTypeDef" = (
        dataclasses.field()
    )

    DomainState = field("DomainState")
    AvailabilityZoneCount = field("AvailabilityZoneCount")
    ActiveAvailabilityZoneCount = field("ActiveAvailabilityZoneCount")
    StandByAvailabilityZoneCount = field("StandByAvailabilityZoneCount")
    DataNodeCount = field("DataNodeCount")
    DedicatedMaster = field("DedicatedMaster")
    MasterEligibleNodeCount = field("MasterEligibleNodeCount")
    WarmNodeCount = field("WarmNodeCount")
    MasterNode = field("MasterNode")
    ClusterHealth = field("ClusterHealth")
    TotalShards = field("TotalShards")
    TotalUnAssignedShards = field("TotalUnAssignedShards")

    @cached_property
    def EnvironmentInformation(self):  # pragma: no cover
        return EnvironmentInfo.make_many(self.boto3_raw_data["EnvironmentInformation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainHealthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainHealthResponseTypeDef"]
        ],
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
class CreateOutboundConnectionRequest:
    boto3_raw_data: "type_defs.CreateOutboundConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LocalDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["LocalDomainInfo"]
        )

    @cached_property
    def RemoteDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["RemoteDomainInfo"]
        )

    ConnectionAlias = field("ConnectionAlias")
    ConnectionMode = field("ConnectionMode")

    @cached_property
    def ConnectionProperties(self):  # pragma: no cover
        return ConnectionProperties.make_one(
            self.boto3_raw_data["ConnectionProperties"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOutboundConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOutboundConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOutboundConnectionResponse:
    boto3_raw_data: "type_defs.CreateOutboundConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LocalDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["LocalDomainInfo"]
        )

    @cached_property
    def RemoteDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["RemoteDomainInfo"]
        )

    ConnectionAlias = field("ConnectionAlias")

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return OutboundConnectionStatus.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    ConnectionId = field("ConnectionId")
    ConnectionMode = field("ConnectionMode")

    @cached_property
    def ConnectionProperties(self):  # pragma: no cover
        return ConnectionProperties.make_one(
            self.boto3_raw_data["ConnectionProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOutboundConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOutboundConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundConnection:
    boto3_raw_data: "type_defs.OutboundConnectionTypeDef" = dataclasses.field()

    @cached_property
    def LocalDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["LocalDomainInfo"]
        )

    @cached_property
    def RemoteDomainInfo(self):  # pragma: no cover
        return DomainInformationContainer.make_one(
            self.boto3_raw_data["RemoteDomainInfo"]
        )

    ConnectionId = field("ConnectionId")
    ConnectionAlias = field("ConnectionAlias")

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return OutboundConnectionStatus.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    ConnectionMode = field("ConnectionMode")

    @cached_property
    def ConnectionProperties(self):  # pragma: no cover
        return ConnectionProperties.make_one(
            self.boto3_raw_data["ConnectionProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddDataSourceRequest:
    boto3_raw_data: "type_defs.AddDataSourceRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Name = field("Name")

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceDetails:
    boto3_raw_data: "type_defs.DataSourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    Name = field("Name")
    Description = field("Description")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceResponse:
    boto3_raw_data: "type_defs.GetDataSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    Name = field("Name")
    Description = field("Description")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceRequest:
    boto3_raw_data: "type_defs.UpdateDataSourceRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Name = field("Name")

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    Description = field("Description")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddDirectQueryDataSourceRequest:
    boto3_raw_data: "type_defs.AddDirectQueryDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    DataSourceName = field("DataSourceName")

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DirectQueryDataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    OpenSearchArns = field("OpenSearchArns")
    Description = field("Description")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddDirectQueryDataSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddDirectQueryDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectQueryDataSource:
    boto3_raw_data: "type_defs.DirectQueryDataSourceTypeDef" = dataclasses.field()

    DataSourceName = field("DataSourceName")

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DirectQueryDataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    Description = field("Description")
    OpenSearchArns = field("OpenSearchArns")
    DataSourceArn = field("DataSourceArn")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectQueryDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectQueryDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectQueryDataSourceResponse:
    boto3_raw_data: "type_defs.GetDirectQueryDataSourceResponseTypeDef" = (
        dataclasses.field()
    )

    DataSourceName = field("DataSourceName")

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DirectQueryDataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    Description = field("Description")
    OpenSearchArns = field("OpenSearchArns")
    DataSourceArn = field("DataSourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDirectQueryDataSourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectQueryDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectQueryDataSourceRequest:
    boto3_raw_data: "type_defs.UpdateDirectQueryDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    DataSourceName = field("DataSourceName")

    @cached_property
    def DataSourceType(self):  # pragma: no cover
        return DirectQueryDataSourceType.make_one(self.boto3_raw_data["DataSourceType"])

    OpenSearchArns = field("OpenSearchArns")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectQueryDataSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectQueryDataSourceRequestTypeDef"]
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
class AssociatePackageRequest:
    boto3_raw_data: "type_defs.AssociatePackageRequestTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    DomainName = field("DomainName")
    PrerequisitePackageIDList = field("PrerequisitePackageIDList")

    @cached_property
    def AssociationConfiguration(self):  # pragma: no cover
        return PackageAssociationConfiguration.make_one(
            self.boto3_raw_data["AssociationConfiguration"]
        )

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
class DomainPackageDetails:
    boto3_raw_data: "type_defs.DomainPackageDetailsTypeDef" = dataclasses.field()

    PackageID = field("PackageID")
    PackageName = field("PackageName")
    PackageType = field("PackageType")
    LastUpdated = field("LastUpdated")
    DomainName = field("DomainName")
    DomainPackageStatus = field("DomainPackageStatus")
    PackageVersion = field("PackageVersion")
    PrerequisitePackageIDList = field("PrerequisitePackageIDList")
    ReferencePath = field("ReferencePath")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["ErrorDetails"])

    @cached_property
    def AssociationConfiguration(self):  # pragma: no cover
        return PackageAssociationConfiguration.make_one(
            self.boto3_raw_data["AssociationConfiguration"]
        )

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
class PackageDetailsForAssociation:
    boto3_raw_data: "type_defs.PackageDetailsForAssociationTypeDef" = (
        dataclasses.field()
    )

    PackageID = field("PackageID")
    PrerequisitePackageIDList = field("PrerequisitePackageIDList")

    @cached_property
    def AssociationConfiguration(self):  # pragma: no cover
        return PackageAssociationConfiguration.make_one(
            self.boto3_raw_data["AssociationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageDetailsForAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageDetailsForAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterConfigOutput:
    boto3_raw_data: "type_defs.ClusterConfigOutputTypeDef" = dataclasses.field()

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

    MultiAZWithStandbyEnabled = field("MultiAZWithStandbyEnabled")

    @cached_property
    def NodeOptions(self):  # pragma: no cover
        return NodeOption.make_many(self.boto3_raw_data["NodeOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterConfig:
    boto3_raw_data: "type_defs.ClusterConfigTypeDef" = dataclasses.field()

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

    MultiAZWithStandbyEnabled = field("MultiAZWithStandbyEnabled")

    @cached_property
    def NodeOptions(self):  # pragma: no cover
        return NodeOption.make_many(self.boto3_raw_data["NodeOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OffPeakWindowOptions:
    boto3_raw_data: "type_defs.OffPeakWindowOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def OffPeakWindow(self):  # pragma: no cover
        return OffPeakWindow.make_one(self.boto3_raw_data["OffPeakWindow"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OffPeakWindowOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OffPeakWindowOptionsTypeDef"]
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
class DescribeReservedInstanceOfferingsResponse:
    boto3_raw_data: "type_defs.DescribeReservedInstanceOfferingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedInstanceOfferings(self):  # pragma: no cover
        return ReservedInstanceOffering.make_many(
            self.boto3_raw_data["ReservedInstanceOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedInstanceOfferingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedInstanceOfferingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedInstancesResponse:
    boto3_raw_data: "type_defs.DescribeReservedInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedInstances(self):  # pragma: no cover
        return ReservedInstance.make_many(self.boto3_raw_data["ReservedInstances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedInstancesResponseTypeDef"]
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

    @cached_property
    def JWTOptions(self):  # pragma: no cover
        return JWTOptionsInput.make_one(self.boto3_raw_data["JWTOptions"])

    @cached_property
    def IAMFederationOptions(self):  # pragma: no cover
        return IAMFederationOptionsInput.make_one(
            self.boto3_raw_data["IAMFederationOptions"]
        )

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

    @cached_property
    def JWTOptions(self):  # pragma: no cover
        return JWTOptionsOutput.make_one(self.boto3_raw_data["JWTOptions"])

    @cached_property
    def IAMFederationOptions(self):  # pragma: no cover
        return IAMFederationOptionsOutput.make_one(
            self.boto3_raw_data["IAMFederationOptions"]
        )

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
class AcceptInboundConnectionResponse:
    boto3_raw_data: "type_defs.AcceptInboundConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connection(self):  # pragma: no cover
        return InboundConnection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceptInboundConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptInboundConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInboundConnectionResponse:
    boto3_raw_data: "type_defs.DeleteInboundConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connection(self):  # pragma: no cover
        return InboundConnection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInboundConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInboundConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundConnectionsResponse:
    boto3_raw_data: "type_defs.DescribeInboundConnectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connections(self):  # pragma: no cover
        return InboundConnection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundConnectionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInboundConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectInboundConnectionResponse:
    boto3_raw_data: "type_defs.RejectInboundConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connection(self):  # pragma: no cover
        return InboundConnection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectInboundConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectInboundConnectionResponseTypeDef"]
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
    UseOffPeakWindow = field("UseOffPeakWindow")

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
class DeleteOutboundConnectionResponse:
    boto3_raw_data: "type_defs.DeleteOutboundConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connection(self):  # pragma: no cover
        return OutboundConnection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteOutboundConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOutboundConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOutboundConnectionsResponse:
    boto3_raw_data: "type_defs.DescribeOutboundConnectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Connections(self):  # pragma: no cover
        return OutboundConnection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOutboundConnectionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOutboundConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesResponse:
    boto3_raw_data: "type_defs.ListDataSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourceDetails.make_many(self.boto3_raw_data["DataSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectQueryDataSourcesResponse:
    boto3_raw_data: "type_defs.ListDirectQueryDataSourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectQueryDataSources(self):  # pragma: no cover
        return DirectQueryDataSource.make_many(
            self.boto3_raw_data["DirectQueryDataSources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDirectQueryDataSourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectQueryDataSourcesResponseTypeDef"]
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
class AssociatePackagesResponse:
    boto3_raw_data: "type_defs.AssociatePackagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainPackageDetailsList(self):  # pragma: no cover
        return DomainPackageDetails.make_many(
            self.boto3_raw_data["DomainPackageDetailsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePackagesResponseTypeDef"]
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
class DissociatePackagesResponse:
    boto3_raw_data: "type_defs.DissociatePackagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainPackageDetailsList(self):  # pragma: no cover
        return DomainPackageDetails.make_many(
            self.boto3_raw_data["DomainPackageDetailsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DissociatePackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DissociatePackagesResponseTypeDef"]
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
class AssociatePackagesRequest:
    boto3_raw_data: "type_defs.AssociatePackagesRequestTypeDef" = dataclasses.field()

    @cached_property
    def PackageList(self):  # pragma: no cover
        return PackageDetailsForAssociation.make_many(
            self.boto3_raw_data["PackageList"]
        )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterConfigStatus:
    boto3_raw_data: "type_defs.ClusterConfigStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return ClusterConfigOutput.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterConfigStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterConfigStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OffPeakWindowOptionsStatus:
    boto3_raw_data: "type_defs.OffPeakWindowOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return OffPeakWindowOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OffPeakWindowOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OffPeakWindowOptionsStatusTypeDef"]
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
class DomainStatus:
    boto3_raw_data: "type_defs.DomainStatusTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    DomainName = field("DomainName")
    ARN = field("ARN")

    @cached_property
    def ClusterConfig(self):  # pragma: no cover
        return ClusterConfigOutput.make_one(self.boto3_raw_data["ClusterConfig"])

    Created = field("Created")
    Deleted = field("Deleted")
    Endpoint = field("Endpoint")
    EndpointV2 = field("EndpointV2")
    Endpoints = field("Endpoints")
    DomainEndpointV2HostedZoneId = field("DomainEndpointV2HostedZoneId")
    Processing = field("Processing")
    UpgradeProcessing = field("UpgradeProcessing")
    EngineVersion = field("EngineVersion")

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptions.make_one(self.boto3_raw_data["EBSOptions"])

    AccessPolicies = field("AccessPolicies")
    IPAddressType = field("IPAddressType")

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
    def IdentityCenterOptions(self):  # pragma: no cover
        return IdentityCenterOptions.make_one(
            self.boto3_raw_data["IdentityCenterOptions"]
        )

    @cached_property
    def AutoTuneOptions(self):  # pragma: no cover
        return AutoTuneOptionsOutput.make_one(self.boto3_raw_data["AutoTuneOptions"])

    @cached_property
    def ChangeProgressDetails(self):  # pragma: no cover
        return ChangeProgressDetails.make_one(
            self.boto3_raw_data["ChangeProgressDetails"]
        )

    @cached_property
    def OffPeakWindowOptions(self):  # pragma: no cover
        return OffPeakWindowOptions.make_one(
            self.boto3_raw_data["OffPeakWindowOptions"]
        )

    @cached_property
    def SoftwareUpdateOptions(self):  # pragma: no cover
        return SoftwareUpdateOptions.make_one(
            self.boto3_raw_data["SoftwareUpdateOptions"]
        )

    DomainProcessingStatus = field("DomainProcessingStatus")

    @cached_property
    def ModifyingProperties(self):  # pragma: no cover
        return ModifyingProperties.make_many(self.boto3_raw_data["ModifyingProperties"])

    @cached_property
    def AIMLOptions(self):  # pragma: no cover
        return AIMLOptionsOutput.make_one(self.boto3_raw_data["AIMLOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceTypeLimitsResponse:
    boto3_raw_data: "type_defs.DescribeInstanceTypeLimitsResponseTypeDef" = (
        dataclasses.field()
    )

    LimitsByRole = field("LimitsByRole")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceTypeLimitsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceTypeLimitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EngineVersion = field("EngineVersion")
    ClusterConfig = field("ClusterConfig")

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptions.make_one(self.boto3_raw_data["EBSOptions"])

    AccessPolicies = field("AccessPolicies")
    IPAddressType = field("IPAddressType")

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
    def IdentityCenterOptions(self):  # pragma: no cover
        return IdentityCenterOptionsInput.make_one(
            self.boto3_raw_data["IdentityCenterOptions"]
        )

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def AutoTuneOptions(self):  # pragma: no cover
        return AutoTuneOptionsInput.make_one(self.boto3_raw_data["AutoTuneOptions"])

    @cached_property
    def OffPeakWindowOptions(self):  # pragma: no cover
        return OffPeakWindowOptions.make_one(
            self.boto3_raw_data["OffPeakWindowOptions"]
        )

    @cached_property
    def SoftwareUpdateOptions(self):  # pragma: no cover
        return SoftwareUpdateOptions.make_one(
            self.boto3_raw_data["SoftwareUpdateOptions"]
        )

    @cached_property
    def AIMLOptions(self):  # pragma: no cover
        return AIMLOptionsInput.make_one(self.boto3_raw_data["AIMLOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainConfigRequest:
    boto3_raw_data: "type_defs.UpdateDomainConfigRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ClusterConfig = field("ClusterConfig")

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
    IPAddressType = field("IPAddressType")
    LogPublishingOptions = field("LogPublishingOptions")

    @cached_property
    def EncryptionAtRestOptions(self):  # pragma: no cover
        return EncryptionAtRestOptions.make_one(
            self.boto3_raw_data["EncryptionAtRestOptions"]
        )

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def NodeToNodeEncryptionOptions(self):  # pragma: no cover
        return NodeToNodeEncryptionOptions.make_one(
            self.boto3_raw_data["NodeToNodeEncryptionOptions"]
        )

    @cached_property
    def AdvancedSecurityOptions(self):  # pragma: no cover
        return AdvancedSecurityOptionsInput.make_one(
            self.boto3_raw_data["AdvancedSecurityOptions"]
        )

    @cached_property
    def IdentityCenterOptions(self):  # pragma: no cover
        return IdentityCenterOptionsInput.make_one(
            self.boto3_raw_data["IdentityCenterOptions"]
        )

    AutoTuneOptions = field("AutoTuneOptions")
    DryRun = field("DryRun")
    DryRunMode = field("DryRunMode")

    @cached_property
    def OffPeakWindowOptions(self):  # pragma: no cover
        return OffPeakWindowOptions.make_one(
            self.boto3_raw_data["OffPeakWindowOptions"]
        )

    @cached_property
    def SoftwareUpdateOptions(self):  # pragma: no cover
        return SoftwareUpdateOptions.make_one(
            self.boto3_raw_data["SoftwareUpdateOptions"]
        )

    @cached_property
    def AIMLOptions(self):  # pragma: no cover
        return AIMLOptionsInput.make_one(self.boto3_raw_data["AIMLOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainConfig:
    boto3_raw_data: "type_defs.DomainConfigTypeDef" = dataclasses.field()

    @cached_property
    def EngineVersion(self):  # pragma: no cover
        return VersionStatus.make_one(self.boto3_raw_data["EngineVersion"])

    @cached_property
    def ClusterConfig(self):  # pragma: no cover
        return ClusterConfigStatus.make_one(self.boto3_raw_data["ClusterConfig"])

    @cached_property
    def EBSOptions(self):  # pragma: no cover
        return EBSOptionsStatus.make_one(self.boto3_raw_data["EBSOptions"])

    @cached_property
    def AccessPolicies(self):  # pragma: no cover
        return AccessPoliciesStatus.make_one(self.boto3_raw_data["AccessPolicies"])

    @cached_property
    def IPAddressType(self):  # pragma: no cover
        return IPAddressTypeStatus.make_one(self.boto3_raw_data["IPAddressType"])

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
    def IdentityCenterOptions(self):  # pragma: no cover
        return IdentityCenterOptionsStatus.make_one(
            self.boto3_raw_data["IdentityCenterOptions"]
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
    def OffPeakWindowOptions(self):  # pragma: no cover
        return OffPeakWindowOptionsStatus.make_one(
            self.boto3_raw_data["OffPeakWindowOptions"]
        )

    @cached_property
    def SoftwareUpdateOptions(self):  # pragma: no cover
        return SoftwareUpdateOptionsStatus.make_one(
            self.boto3_raw_data["SoftwareUpdateOptions"]
        )

    @cached_property
    def ModifyingProperties(self):  # pragma: no cover
        return ModifyingProperties.make_many(self.boto3_raw_data["ModifyingProperties"])

    @cached_property
    def AIMLOptions(self):  # pragma: no cover
        return AIMLOptionsStatus.make_one(self.boto3_raw_data["AIMLOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainResponse:
    boto3_raw_data: "type_defs.CreateDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return DomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainResponse:
    boto3_raw_data: "type_defs.DeleteDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return DomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainResponse:
    boto3_raw_data: "type_defs.DescribeDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return DomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainsResponse:
    boto3_raw_data: "type_defs.DescribeDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainStatusList(self):  # pragma: no cover
        return DomainStatus.make_many(self.boto3_raw_data["DomainStatusList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDryRunProgressResponse:
    boto3_raw_data: "type_defs.DescribeDryRunProgressResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DryRunProgressStatus(self):  # pragma: no cover
        return DryRunProgressStatus.make_one(
            self.boto3_raw_data["DryRunProgressStatus"]
        )

    @cached_property
    def DryRunConfig(self):  # pragma: no cover
        return DomainStatus.make_one(self.boto3_raw_data["DryRunConfig"])

    @cached_property
    def DryRunResults(self):  # pragma: no cover
        return DryRunResults.make_one(self.boto3_raw_data["DryRunResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDryRunProgressResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDryRunProgressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainConfigResponse:
    boto3_raw_data: "type_defs.DescribeDomainConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainConfig(self):  # pragma: no cover
        return DomainConfig.make_one(self.boto3_raw_data["DomainConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainConfigResponse:
    boto3_raw_data: "type_defs.UpdateDomainConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainConfig(self):  # pragma: no cover
        return DomainConfig.make_one(self.boto3_raw_data["DomainConfig"])

    @cached_property
    def DryRunResults(self):  # pragma: no cover
        return DryRunResults.make_one(self.boto3_raw_data["DryRunResults"])

    @cached_property
    def DryRunProgressStatus(self):  # pragma: no cover
        return DryRunProgressStatus.make_one(
            self.boto3_raw_data["DryRunProgressStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
