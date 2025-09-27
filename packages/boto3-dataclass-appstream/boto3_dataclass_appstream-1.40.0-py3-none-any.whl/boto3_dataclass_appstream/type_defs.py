# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appstream import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessEndpoint:
    boto3_raw_data: "type_defs.AccessEndpointTypeDef" = dataclasses.field()

    EndpointType = field("EndpointType")
    VpceId = field("VpceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppBlockBuilderAppBlockAssociation:
    boto3_raw_data: "type_defs.AppBlockBuilderAppBlockAssociationTypeDef" = (
        dataclasses.field()
    )

    AppBlockArn = field("AppBlockArn")
    AppBlockBuilderName = field("AppBlockBuilderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AppBlockBuilderAppBlockAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppBlockBuilderAppBlockAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppBlockBuilderStateChangeReason:
    boto3_raw_data: "type_defs.AppBlockBuilderStateChangeReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AppBlockBuilderStateChangeReasonTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppBlockBuilderStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceError:
    boto3_raw_data: "type_defs.ResourceErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    ErrorTimestamp = field("ErrorTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigOutput:
    boto3_raw_data: "type_defs.VpcConfigOutputTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
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
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationFleetAssociation:
    boto3_raw_data: "type_defs.ApplicationFleetAssociationTypeDef" = dataclasses.field()

    FleetName = field("FleetName")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationFleetAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationFleetAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSettingsResponse:
    boto3_raw_data: "type_defs.ApplicationSettingsResponseTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SettingsGroup = field("SettingsGroup")
    S3BucketName = field("S3BucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSettings:
    boto3_raw_data: "type_defs.ApplicationSettingsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SettingsGroup = field("SettingsGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAppBlockBuilderAppBlockRequest:
    boto3_raw_data: "type_defs.AssociateAppBlockBuilderAppBlockRequestTypeDef" = (
        dataclasses.field()
    )

    AppBlockArn = field("AppBlockArn")
    AppBlockBuilderName = field("AppBlockBuilderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAppBlockBuilderAppBlockRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAppBlockBuilderAppBlockRequestTypeDef"]
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
class AssociateApplicationFleetRequest:
    boto3_raw_data: "type_defs.AssociateApplicationFleetRequestTypeDef" = (
        dataclasses.field()
    )

    FleetName = field("FleetName")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateApplicationFleetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApplicationFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApplicationToEntitlementRequest:
    boto3_raw_data: "type_defs.AssociateApplicationToEntitlementRequestTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    EntitlementName = field("EntitlementName")
    ApplicationIdentifier = field("ApplicationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateApplicationToEntitlementRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApplicationToEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFleetRequest:
    boto3_raw_data: "type_defs.AssociateFleetRequestTypeDef" = dataclasses.field()

    FleetName = field("FleetName")
    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserStackAssociation:
    boto3_raw_data: "type_defs.UserStackAssociationTypeDef" = dataclasses.field()

    StackName = field("StackName")
    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")
    SendEmailNotification = field("SendEmailNotification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserStackAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserStackAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateBasedAuthProperties:
    boto3_raw_data: "type_defs.CertificateBasedAuthPropertiesTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CertificateBasedAuthPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateBasedAuthPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeCapacityStatus:
    boto3_raw_data: "type_defs.ComputeCapacityStatusTypeDef" = dataclasses.field()

    Desired = field("Desired")
    Running = field("Running")
    InUse = field("InUse")
    Available = field("Available")
    DesiredUserSessions = field("DesiredUserSessions")
    AvailableUserSessions = field("AvailableUserSessions")
    ActiveUserSessions = field("ActiveUserSessions")
    ActualUserSessions = field("ActualUserSessions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeCapacityStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeCapacityStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeCapacity:
    boto3_raw_data: "type_defs.ComputeCapacityTypeDef" = dataclasses.field()

    DesiredInstances = field("DesiredInstances")
    DesiredSessions = field("DesiredSessions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeCapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeCapacityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyImageRequest:
    boto3_raw_data: "type_defs.CopyImageRequestTypeDef" = dataclasses.field()

    SourceImageName = field("SourceImageName")
    DestinationImageName = field("DestinationImageName")
    DestinationRegion = field("DestinationRegion")
    DestinationImageDescription = field("DestinationImageDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyImageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppBlockBuilderStreamingURLRequest:
    boto3_raw_data: "type_defs.CreateAppBlockBuilderStreamingURLRequestTypeDef" = (
        dataclasses.field()
    )

    AppBlockBuilderName = field("AppBlockBuilderName")
    Validity = field("Validity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAppBlockBuilderStreamingURLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppBlockBuilderStreamingURLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAccountCredentials:
    boto3_raw_data: "type_defs.ServiceAccountCredentialsTypeDef" = dataclasses.field()

    AccountName = field("AccountName")
    AccountPassword = field("AccountPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceAccountCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAccountCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitlementAttribute:
    boto3_raw_data: "type_defs.EntitlementAttributeTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntitlementAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntitlementAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainJoinInfo:
    boto3_raw_data: "type_defs.DomainJoinInfoTypeDef" = dataclasses.field()

    DirectoryName = field("DirectoryName")
    OrganizationalUnitDistinguishedName = field("OrganizationalUnitDistinguishedName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainJoinInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainJoinInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageBuilderStreamingURLRequest:
    boto3_raw_data: "type_defs.CreateImageBuilderStreamingURLRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Validity = field("Validity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateImageBuilderStreamingURLRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageBuilderStreamingURLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingExperienceSettings:
    boto3_raw_data: "type_defs.StreamingExperienceSettingsTypeDef" = dataclasses.field()

    PreferredProtocol = field("PreferredProtocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingExperienceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingExperienceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSetting:
    boto3_raw_data: "type_defs.UserSettingTypeDef" = dataclasses.field()

    Action = field("Action")
    Permission = field("Permission")
    MaximumLength = field("MaximumLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSettingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamingURLRequest:
    boto3_raw_data: "type_defs.CreateStreamingURLRequestTypeDef" = dataclasses.field()

    StackName = field("StackName")
    FleetName = field("FleetName")
    UserId = field("UserId")
    ApplicationId = field("ApplicationId")
    Validity = field("Validity")
    SessionContext = field("SessionContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStreamingURLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamingURLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeFooterLink:
    boto3_raw_data: "type_defs.ThemeFooterLinkTypeDef" = dataclasses.field()

    DisplayName = field("DisplayName")
    FooterLinkURL = field("FooterLinkURL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeFooterLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemeFooterLinkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUpdatedImageRequest:
    boto3_raw_data: "type_defs.CreateUpdatedImageRequestTypeDef" = dataclasses.field()

    existingImageName = field("existingImageName")
    newImageName = field("newImageName")
    newImageDescription = field("newImageDescription")
    newImageDisplayName = field("newImageDisplayName")
    newImageTags = field("newImageTags")
    dryRun = field("dryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUpdatedImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUpdatedImageRequestTypeDef"]
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

    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")
    MessageAction = field("MessageAction")
    FirstName = field("FirstName")
    LastName = field("LastName")

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
class DeleteAppBlockBuilderRequest:
    boto3_raw_data: "type_defs.DeleteAppBlockBuilderRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppBlockBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppBlockBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppBlockRequest:
    boto3_raw_data: "type_defs.DeleteAppBlockRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppBlockRequestTypeDef"]
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

    Name = field("Name")

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
class DeleteDirectoryConfigRequest:
    boto3_raw_data: "type_defs.DeleteDirectoryConfigRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryName = field("DirectoryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDirectoryConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectoryConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEntitlementRequest:
    boto3_raw_data: "type_defs.DeleteEntitlementRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEntitlementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetRequest:
    boto3_raw_data: "type_defs.DeleteFleetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageBuilderRequest:
    boto3_raw_data: "type_defs.DeleteImageBuilderRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImagePermissionsRequest:
    boto3_raw_data: "type_defs.DeleteImagePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SharedAccountId = field("SharedAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteImagePermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImagePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageRequest:
    boto3_raw_data: "type_defs.DeleteImageRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackRequest:
    boto3_raw_data: "type_defs.DeleteStackRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThemeForStackRequest:
    boto3_raw_data: "type_defs.DeleteThemeForStackRequestTypeDef" = dataclasses.field()

    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThemeForStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThemeForStackRequestTypeDef"]
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

    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")

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
class DescribeAppBlockBuilderAppBlockAssociationsRequest:
    boto3_raw_data: (
        "type_defs.DescribeAppBlockBuilderAppBlockAssociationsRequestTypeDef"
    ) = dataclasses.field()

    AppBlockArn = field("AppBlockArn")
    AppBlockBuilderName = field("AppBlockBuilderName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppBlockBuilderAppBlockAssociationsRequestTypeDef"
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
                "type_defs.DescribeAppBlockBuilderAppBlockAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppBlockBuildersRequest:
    boto3_raw_data: "type_defs.DescribeAppBlockBuildersRequestTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAppBlockBuildersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppBlockBuildersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppBlocksRequest:
    boto3_raw_data: "type_defs.DescribeAppBlocksRequestTypeDef" = dataclasses.field()

    Arns = field("Arns")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppBlocksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppBlocksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationFleetAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeApplicationFleetAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    FleetName = field("FleetName")
    ApplicationArn = field("ApplicationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationFleetAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationFleetAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationsRequest:
    boto3_raw_data: "type_defs.DescribeApplicationsRequestTypeDef" = dataclasses.field()

    Arns = field("Arns")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationsRequestTypeDef"]
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
class DescribeDirectoryConfigsRequest:
    boto3_raw_data: "type_defs.DescribeDirectoryConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryNames = field("DirectoryNames")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDirectoryConfigsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoryConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntitlementsRequest:
    boto3_raw_data: "type_defs.DescribeEntitlementsRequestTypeDef" = dataclasses.field()

    StackName = field("StackName")
    Name = field("Name")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEntitlementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntitlementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetsRequest:
    boto3_raw_data: "type_defs.DescribeFleetsRequestTypeDef" = dataclasses.field()

    Names = field("Names")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetsRequestTypeDef"]
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
class DescribeImageBuildersRequest:
    boto3_raw_data: "type_defs.DescribeImageBuildersRequestTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImageBuildersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageBuildersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagePermissionsRequest:
    boto3_raw_data: "type_defs.DescribeImagePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    MaxResults = field("MaxResults")
    SharedAwsAccountIds = field("SharedAwsAccountIds")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImagePermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesRequest:
    boto3_raw_data: "type_defs.DescribeImagesRequestTypeDef" = dataclasses.field()

    Names = field("Names")
    Arns = field("Arns")
    Type = field("Type")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesRequestTypeDef"]
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

    StackName = field("StackName")
    FleetName = field("FleetName")
    UserId = field("UserId")
    NextToken = field("NextToken")
    Limit = field("Limit")
    AuthenticationType = field("AuthenticationType")
    InstanceId = field("InstanceId")

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
class DescribeStacksRequest:
    boto3_raw_data: "type_defs.DescribeStacksRequestTypeDef" = dataclasses.field()

    Names = field("Names")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThemeForStackRequest:
    boto3_raw_data: "type_defs.DescribeThemeForStackRequestTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThemeForStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThemeForStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsageReportSubscriptionsRequest:
    boto3_raw_data: "type_defs.DescribeUsageReportSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUsageReportSubscriptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsageReportSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserStackAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeUserStackAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserStackAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserStackAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersRequest:
    boto3_raw_data: "type_defs.DescribeUsersRequestTypeDef" = dataclasses.field()

    AuthenticationType = field("AuthenticationType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersRequestTypeDef"]
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

    AuthenticationType = field("AuthenticationType")
    Arn = field("Arn")
    UserName = field("UserName")
    Enabled = field("Enabled")
    Status = field("Status")
    FirstName = field("FirstName")
    LastName = field("LastName")
    CreatedTime = field("CreatedTime")

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
class DisableUserRequest:
    boto3_raw_data: "type_defs.DisableUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAppBlockBuilderAppBlockRequest:
    boto3_raw_data: "type_defs.DisassociateAppBlockBuilderAppBlockRequestTypeDef" = (
        dataclasses.field()
    )

    AppBlockArn = field("AppBlockArn")
    AppBlockBuilderName = field("AppBlockBuilderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAppBlockBuilderAppBlockRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAppBlockBuilderAppBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateApplicationFleetRequest:
    boto3_raw_data: "type_defs.DisassociateApplicationFleetRequestTypeDef" = (
        dataclasses.field()
    )

    FleetName = field("FleetName")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateApplicationFleetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateApplicationFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateApplicationFromEntitlementRequest:
    boto3_raw_data: "type_defs.DisassociateApplicationFromEntitlementRequestTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    EntitlementName = field("EntitlementName")
    ApplicationIdentifier = field("ApplicationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateApplicationFromEntitlementRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateApplicationFromEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFleetRequest:
    boto3_raw_data: "type_defs.DisassociateFleetRequestTypeDef" = dataclasses.field()

    FleetName = field("FleetName")
    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableUserRequest:
    boto3_raw_data: "type_defs.EnableUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitledApplication:
    boto3_raw_data: "type_defs.EntitledApplicationTypeDef" = dataclasses.field()

    ApplicationIdentifier = field("ApplicationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntitledApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntitledApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpireSessionRequest:
    boto3_raw_data: "type_defs.ExpireSessionRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpireSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpireSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetError:
    boto3_raw_data: "type_defs.FleetErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageBuilderStateChangeReason:
    boto3_raw_data: "type_defs.ImageBuilderStateChangeReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageBuilderStateChangeReasonTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageBuilderStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAccessConfiguration:
    boto3_raw_data: "type_defs.NetworkAccessConfigurationTypeDef" = dataclasses.field()

    EniPrivateIpAddress = field("EniPrivateIpAddress")
    EniId = field("EniId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImagePermissions:
    boto3_raw_data: "type_defs.ImagePermissionsTypeDef" = dataclasses.field()

    allowFleet = field("allowFleet")
    allowImageBuilder = field("allowImageBuilder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImagePermissionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImagePermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageStateChangeReason:
    boto3_raw_data: "type_defs.ImageStateChangeReasonTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageStateChangeReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageStateChangeReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastReportGenerationExecutionError:
    boto3_raw_data: "type_defs.LastReportGenerationExecutionErrorTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LastReportGenerationExecutionErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LastReportGenerationExecutionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedFleetsRequest:
    boto3_raw_data: "type_defs.ListAssociatedFleetsRequestTypeDef" = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedFleetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedFleetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedStacksRequest:
    boto3_raw_data: "type_defs.ListAssociatedStacksRequestTypeDef" = dataclasses.field()

    FleetName = field("FleetName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedStacksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedStacksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitledApplicationsRequest:
    boto3_raw_data: "type_defs.ListEntitledApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    EntitlementName = field("EntitlementName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntitledApplicationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitledApplicationsRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class StackError:
    boto3_raw_data: "type_defs.StackErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConnectorOutput:
    boto3_raw_data: "type_defs.StorageConnectorOutputTypeDef" = dataclasses.field()

    ConnectorType = field("ConnectorType")
    ResourceIdentifier = field("ResourceIdentifier")
    Domains = field("Domains")
    DomainsRequireAdminConsent = field("DomainsRequireAdminConsent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConnectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConnectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAppBlockBuilderRequest:
    boto3_raw_data: "type_defs.StartAppBlockBuilderRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAppBlockBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAppBlockBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFleetRequest:
    boto3_raw_data: "type_defs.StartFleetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartFleetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImageBuilderRequest:
    boto3_raw_data: "type_defs.StartImageBuilderRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AppstreamAgentVersion = field("AppstreamAgentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImageBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImageBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAppBlockBuilderRequest:
    boto3_raw_data: "type_defs.StopAppBlockBuilderRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopAppBlockBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAppBlockBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFleetRequest:
    boto3_raw_data: "type_defs.StopFleetRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopFleetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopImageBuilderRequest:
    boto3_raw_data: "type_defs.StopImageBuilderRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopImageBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopImageBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConnector:
    boto3_raw_data: "type_defs.StorageConnectorTypeDef" = dataclasses.field()

    ConnectorType = field("ConnectorType")
    ResourceIdentifier = field("ResourceIdentifier")
    Domains = field("Domains")
    DomainsRequireAdminConsent = field("DomainsRequireAdminConsent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConnectorTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppBlockBuilder:
    boto3_raw_data: "type_defs.AppBlockBuilderTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Platform = field("Platform")
    InstanceType = field("InstanceType")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    State = field("State")
    DisplayName = field("DisplayName")
    Description = field("Description")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")
    IamRoleArn = field("IamRoleArn")
    CreatedTime = field("CreatedTime")

    @cached_property
    def AppBlockBuilderErrors(self):  # pragma: no cover
        return ResourceError.make_many(self.boto3_raw_data["AppBlockBuilderErrors"])

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return AppBlockBuilderStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppBlockBuilderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppBlockBuilderTypeDef"]],
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
    DisplayName = field("DisplayName")
    IconURL = field("IconURL")
    LaunchPath = field("LaunchPath")
    LaunchParameters = field("LaunchParameters")
    Enabled = field("Enabled")
    Metadata = field("Metadata")
    WorkingDirectory = field("WorkingDirectory")
    Description = field("Description")
    Arn = field("Arn")
    AppBlockArn = field("AppBlockArn")

    @cached_property
    def IconS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["IconS3Location"])

    Platforms = field("Platforms")
    InstanceFamilies = field("InstanceFamilies")
    CreatedTime = field("CreatedTime")

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
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def IconS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["IconS3Location"])

    LaunchPath = field("LaunchPath")
    Platforms = field("Platforms")
    InstanceFamilies = field("InstanceFamilies")
    AppBlockArn = field("AppBlockArn")
    DisplayName = field("DisplayName")
    Description = field("Description")
    WorkingDirectory = field("WorkingDirectory")
    LaunchParameters = field("LaunchParameters")
    Tags = field("Tags")

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
class ScriptDetails:
    boto3_raw_data: "type_defs.ScriptDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ScriptS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["ScriptS3Location"])

    ExecutablePath = field("ExecutablePath")
    TimeoutInSeconds = field("TimeoutInSeconds")
    ExecutableParameters = field("ExecutableParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScriptDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DisplayName = field("DisplayName")
    Description = field("Description")

    @cached_property
    def IconS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["IconS3Location"])

    LaunchPath = field("LaunchPath")
    WorkingDirectory = field("WorkingDirectory")
    LaunchParameters = field("LaunchParameters")
    AppBlockArn = field("AppBlockArn")
    AttributesToDelete = field("AttributesToDelete")

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
class AssociateAppBlockBuilderAppBlockResult:
    boto3_raw_data: "type_defs.AssociateAppBlockBuilderAppBlockResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AppBlockBuilderAppBlockAssociation(self):  # pragma: no cover
        return AppBlockBuilderAppBlockAssociation.make_one(
            self.boto3_raw_data["AppBlockBuilderAppBlockAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAppBlockBuilderAppBlockResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAppBlockBuilderAppBlockResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApplicationFleetResult:
    boto3_raw_data: "type_defs.AssociateApplicationFleetResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationFleetAssociation(self):  # pragma: no cover
        return ApplicationFleetAssociation.make_one(
            self.boto3_raw_data["ApplicationFleetAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateApplicationFleetResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApplicationFleetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyImageResponse:
    boto3_raw_data: "type_defs.CopyImageResponseTypeDef" = dataclasses.field()

    DestinationImageName = field("DestinationImageName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyImageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyImageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppBlockBuilderStreamingURLResult:
    boto3_raw_data: "type_defs.CreateAppBlockBuilderStreamingURLResultTypeDef" = (
        dataclasses.field()
    )

    StreamingURL = field("StreamingURL")
    Expires = field("Expires")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAppBlockBuilderStreamingURLResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppBlockBuilderStreamingURLResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageBuilderStreamingURLResult:
    boto3_raw_data: "type_defs.CreateImageBuilderStreamingURLResultTypeDef" = (
        dataclasses.field()
    )

    StreamingURL = field("StreamingURL")
    Expires = field("Expires")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateImageBuilderStreamingURLResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageBuilderStreamingURLResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamingURLResult:
    boto3_raw_data: "type_defs.CreateStreamingURLResultTypeDef" = dataclasses.field()

    StreamingURL = field("StreamingURL")
    Expires = field("Expires")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStreamingURLResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamingURLResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUsageReportSubscriptionResult:
    boto3_raw_data: "type_defs.CreateUsageReportSubscriptionResultTypeDef" = (
        dataclasses.field()
    )

    S3BucketName = field("S3BucketName")
    Schedule = field("Schedule")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUsageReportSubscriptionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUsageReportSubscriptionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppBlockBuilderAppBlockAssociationsResult:
    boto3_raw_data: (
        "type_defs.DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AppBlockBuilderAppBlockAssociations(self):  # pragma: no cover
        return AppBlockBuilderAppBlockAssociation.make_many(
            self.boto3_raw_data["AppBlockBuilderAppBlockAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef"
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
                "type_defs.DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationFleetAssociationsResult:
    boto3_raw_data: "type_defs.DescribeApplicationFleetAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationFleetAssociations(self):  # pragma: no cover
        return ApplicationFleetAssociation.make_many(
            self.boto3_raw_data["ApplicationFleetAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationFleetAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationFleetAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedFleetsResult:
    boto3_raw_data: "type_defs.ListAssociatedFleetsResultTypeDef" = dataclasses.field()

    Names = field("Names")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedFleetsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedFleetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedStacksResult:
    boto3_raw_data: "type_defs.ListAssociatedStacksResultTypeDef" = dataclasses.field()

    Names = field("Names")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssociatedStacksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedStacksResultTypeDef"]
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

    Tags = field("Tags")

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
class BatchAssociateUserStackRequest:
    boto3_raw_data: "type_defs.BatchAssociateUserStackRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserStackAssociations(self):  # pragma: no cover
        return UserStackAssociation.make_many(
            self.boto3_raw_data["UserStackAssociations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchAssociateUserStackRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateUserStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateUserStackRequest:
    boto3_raw_data: "type_defs.BatchDisassociateUserStackRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserStackAssociations(self):  # pragma: no cover
        return UserStackAssociation.make_many(
            self.boto3_raw_data["UserStackAssociations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateUserStackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateUserStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserStackAssociationsResult:
    boto3_raw_data: "type_defs.DescribeUserStackAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserStackAssociations(self):  # pragma: no cover
        return UserStackAssociation.make_many(
            self.boto3_raw_data["UserStackAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserStackAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserStackAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserStackAssociationError:
    boto3_raw_data: "type_defs.UserStackAssociationErrorTypeDef" = dataclasses.field()

    @cached_property
    def UserStackAssociation(self):  # pragma: no cover
        return UserStackAssociation.make_one(
            self.boto3_raw_data["UserStackAssociation"]
        )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserStackAssociationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserStackAssociationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryConfigRequest:
    boto3_raw_data: "type_defs.CreateDirectoryConfigRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryName = field("DirectoryName")
    OrganizationalUnitDistinguishedNames = field("OrganizationalUnitDistinguishedNames")

    @cached_property
    def ServiceAccountCredentials(self):  # pragma: no cover
        return ServiceAccountCredentials.make_one(
            self.boto3_raw_data["ServiceAccountCredentials"]
        )

    @cached_property
    def CertificateBasedAuthProperties(self):  # pragma: no cover
        return CertificateBasedAuthProperties.make_one(
            self.boto3_raw_data["CertificateBasedAuthProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDirectoryConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryConfig:
    boto3_raw_data: "type_defs.DirectoryConfigTypeDef" = dataclasses.field()

    DirectoryName = field("DirectoryName")
    OrganizationalUnitDistinguishedNames = field("OrganizationalUnitDistinguishedNames")

    @cached_property
    def ServiceAccountCredentials(self):  # pragma: no cover
        return ServiceAccountCredentials.make_one(
            self.boto3_raw_data["ServiceAccountCredentials"]
        )

    CreatedTime = field("CreatedTime")

    @cached_property
    def CertificateBasedAuthProperties(self):  # pragma: no cover
        return CertificateBasedAuthProperties.make_one(
            self.boto3_raw_data["CertificateBasedAuthProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DirectoryConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DirectoryConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectoryConfigRequest:
    boto3_raw_data: "type_defs.UpdateDirectoryConfigRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryName = field("DirectoryName")
    OrganizationalUnitDistinguishedNames = field("OrganizationalUnitDistinguishedNames")

    @cached_property
    def ServiceAccountCredentials(self):  # pragma: no cover
        return ServiceAccountCredentials.make_one(
            self.boto3_raw_data["ServiceAccountCredentials"]
        )

    @cached_property
    def CertificateBasedAuthProperties(self):  # pragma: no cover
        return CertificateBasedAuthProperties.make_one(
            self.boto3_raw_data["CertificateBasedAuthProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDirectoryConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectoryConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEntitlementRequest:
    boto3_raw_data: "type_defs.CreateEntitlementRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    StackName = field("StackName")
    AppVisibility = field("AppVisibility")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return EntitlementAttribute.make_many(self.boto3_raw_data["Attributes"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEntitlementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entitlement:
    boto3_raw_data: "type_defs.EntitlementTypeDef" = dataclasses.field()

    Name = field("Name")
    StackName = field("StackName")
    AppVisibility = field("AppVisibility")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return EntitlementAttribute.make_many(self.boto3_raw_data["Attributes"])

    Description = field("Description")
    CreatedTime = field("CreatedTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitlementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntitlementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEntitlementRequest:
    boto3_raw_data: "type_defs.UpdateEntitlementRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    StackName = field("StackName")
    Description = field("Description")
    AppVisibility = field("AppVisibility")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return EntitlementAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEntitlementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEntitlementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThemeForStackRequest:
    boto3_raw_data: "type_defs.CreateThemeForStackRequestTypeDef" = dataclasses.field()

    StackName = field("StackName")
    TitleText = field("TitleText")
    ThemeStyling = field("ThemeStyling")

    @cached_property
    def OrganizationLogoS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["OrganizationLogoS3Location"])

    @cached_property
    def FaviconS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["FaviconS3Location"])

    @cached_property
    def FooterLinks(self):  # pragma: no cover
        return ThemeFooterLink.make_many(self.boto3_raw_data["FooterLinks"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThemeForStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThemeForStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Theme:
    boto3_raw_data: "type_defs.ThemeTypeDef" = dataclasses.field()

    StackName = field("StackName")
    State = field("State")
    ThemeTitleText = field("ThemeTitleText")
    ThemeStyling = field("ThemeStyling")

    @cached_property
    def ThemeFooterLinks(self):  # pragma: no cover
        return ThemeFooterLink.make_many(self.boto3_raw_data["ThemeFooterLinks"])

    ThemeOrganizationLogoURL = field("ThemeOrganizationLogoURL")
    ThemeFaviconURL = field("ThemeFaviconURL")
    CreatedTime = field("CreatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThemeForStackRequest:
    boto3_raw_data: "type_defs.UpdateThemeForStackRequestTypeDef" = dataclasses.field()

    StackName = field("StackName")

    @cached_property
    def FooterLinks(self):  # pragma: no cover
        return ThemeFooterLink.make_many(self.boto3_raw_data["FooterLinks"])

    TitleText = field("TitleText")
    ThemeStyling = field("ThemeStyling")

    @cached_property
    def OrganizationLogoS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["OrganizationLogoS3Location"])

    @cached_property
    def FaviconS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["FaviconS3Location"])

    State = field("State")
    AttributesToDelete = field("AttributesToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThemeForStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThemeForStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoryConfigsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDirectoryConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryNames = field("DirectoryNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectoryConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoryConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeFleetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageBuildersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeImageBuildersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageBuildersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageBuildersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeImagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    Arns = field("Arns")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImagesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesRequestPaginateTypeDef"]
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

    StackName = field("StackName")
    FleetName = field("FleetName")
    UserId = field("UserId")
    AuthenticationType = field("AuthenticationType")
    InstanceId = field("InstanceId")

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
class DescribeStacksRequestPaginate:
    boto3_raw_data: "type_defs.DescribeStacksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStacksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserStackAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeUserStackAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    UserName = field("UserName")
    AuthenticationType = field("AuthenticationType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUserStackAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserStackAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeUsersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AuthenticationType = field("AuthenticationType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedFleetsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociatedFleetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedFleetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedFleetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedStacksRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociatedStacksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FleetName = field("FleetName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedStacksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedStacksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetsRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeFleetsRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFleetsRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetsRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetsRequestWait:
    boto3_raw_data: "type_defs.DescribeFleetsRequestWaitTypeDef" = dataclasses.field()

    Names = field("Names")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetsRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetsRequestWaitTypeDef"]
        ],
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

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class ListEntitledApplicationsResult:
    boto3_raw_data: "type_defs.ListEntitledApplicationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntitledApplications(self):  # pragma: no cover
        return EntitledApplication.make_many(
            self.boto3_raw_data["EntitledApplications"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntitledApplicationsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitledApplicationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Fleet:
    boto3_raw_data: "type_defs.FleetTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    InstanceType = field("InstanceType")

    @cached_property
    def ComputeCapacityStatus(self):  # pragma: no cover
        return ComputeCapacityStatus.make_one(
            self.boto3_raw_data["ComputeCapacityStatus"]
        )

    State = field("State")
    DisplayName = field("DisplayName")
    Description = field("Description")
    ImageName = field("ImageName")
    ImageArn = field("ImageArn")
    FleetType = field("FleetType")
    MaxUserDurationInSeconds = field("MaxUserDurationInSeconds")
    DisconnectTimeoutInSeconds = field("DisconnectTimeoutInSeconds")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    CreatedTime = field("CreatedTime")

    @cached_property
    def FleetErrors(self):  # pragma: no cover
        return FleetError.make_many(self.boto3_raw_data["FleetErrors"])

    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")

    @cached_property
    def DomainJoinInfo(self):  # pragma: no cover
        return DomainJoinInfo.make_one(self.boto3_raw_data["DomainJoinInfo"])

    IdleDisconnectTimeoutInSeconds = field("IdleDisconnectTimeoutInSeconds")
    IamRoleArn = field("IamRoleArn")
    StreamView = field("StreamView")
    Platform = field("Platform")
    MaxConcurrentSessions = field("MaxConcurrentSessions")
    UsbDeviceFilterStrings = field("UsbDeviceFilterStrings")

    @cached_property
    def SessionScriptS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SessionScriptS3Location"])

    MaxSessionsPerInstance = field("MaxSessionsPerInstance")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageBuilder:
    boto3_raw_data: "type_defs.ImageBuilderTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    ImageArn = field("ImageArn")
    Description = field("Description")
    DisplayName = field("DisplayName")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["VpcConfig"])

    InstanceType = field("InstanceType")
    Platform = field("Platform")
    IamRoleArn = field("IamRoleArn")
    State = field("State")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return ImageBuilderStateChangeReason.make_one(
            self.boto3_raw_data["StateChangeReason"]
        )

    CreatedTime = field("CreatedTime")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")

    @cached_property
    def DomainJoinInfo(self):  # pragma: no cover
        return DomainJoinInfo.make_one(self.boto3_raw_data["DomainJoinInfo"])

    @cached_property
    def NetworkAccessConfiguration(self):  # pragma: no cover
        return NetworkAccessConfiguration.make_one(
            self.boto3_raw_data["NetworkAccessConfiguration"]
        )

    @cached_property
    def ImageBuilderErrors(self):  # pragma: no cover
        return ResourceError.make_many(self.boto3_raw_data["ImageBuilderErrors"])

    AppstreamAgentVersion = field("AppstreamAgentVersion")

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    LatestAppstreamAgentVersion = field("LatestAppstreamAgentVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageBuilderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageBuilderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    Id = field("Id")
    UserId = field("UserId")
    StackName = field("StackName")
    FleetName = field("FleetName")
    State = field("State")
    ConnectionState = field("ConnectionState")
    StartTime = field("StartTime")
    MaxExpirationTime = field("MaxExpirationTime")
    AuthenticationType = field("AuthenticationType")

    @cached_property
    def NetworkAccessConfiguration(self):  # pragma: no cover
        return NetworkAccessConfiguration.make_one(
            self.boto3_raw_data["NetworkAccessConfiguration"]
        )

    InstanceId = field("InstanceId")

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
class SharedImagePermissions:
    boto3_raw_data: "type_defs.SharedImagePermissionsTypeDef" = dataclasses.field()

    sharedAccountId = field("sharedAccountId")

    @cached_property
    def imagePermissions(self):  # pragma: no cover
        return ImagePermissions.make_one(self.boto3_raw_data["imagePermissions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SharedImagePermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharedImagePermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImagePermissionsRequest:
    boto3_raw_data: "type_defs.UpdateImagePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    SharedAccountId = field("SharedAccountId")

    @cached_property
    def ImagePermissions(self):  # pragma: no cover
        return ImagePermissions.make_one(self.boto3_raw_data["ImagePermissions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateImagePermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImagePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageReportSubscription:
    boto3_raw_data: "type_defs.UsageReportSubscriptionTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    Schedule = field("Schedule")
    LastGeneratedReportDate = field("LastGeneratedReportDate")

    @cached_property
    def SubscriptionErrors(self):  # pragma: no cover
        return LastReportGenerationExecutionError.make_many(
            self.boto3_raw_data["SubscriptionErrors"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageReportSubscriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageReportSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stack:
    boto3_raw_data: "type_defs.StackTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    DisplayName = field("DisplayName")
    CreatedTime = field("CreatedTime")

    @cached_property
    def StorageConnectors(self):  # pragma: no cover
        return StorageConnectorOutput.make_many(
            self.boto3_raw_data["StorageConnectors"]
        )

    RedirectURL = field("RedirectURL")
    FeedbackURL = field("FeedbackURL")

    @cached_property
    def StackErrors(self):  # pragma: no cover
        return StackError.make_many(self.boto3_raw_data["StackErrors"])

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSetting.make_many(self.boto3_raw_data["UserSettings"])

    @cached_property
    def ApplicationSettings(self):  # pragma: no cover
        return ApplicationSettingsResponse.make_one(
            self.boto3_raw_data["ApplicationSettings"]
        )

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    EmbedHostDomains = field("EmbedHostDomains")

    @cached_property
    def StreamingExperienceSettings(self):  # pragma: no cover
        return StreamingExperienceSettings.make_one(
            self.boto3_raw_data["StreamingExperienceSettings"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppBlockBuilderResult:
    boto3_raw_data: "type_defs.CreateAppBlockBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def AppBlockBuilder(self):  # pragma: no cover
        return AppBlockBuilder.make_one(self.boto3_raw_data["AppBlockBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAppBlockBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppBlockBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppBlockBuildersResult:
    boto3_raw_data: "type_defs.DescribeAppBlockBuildersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AppBlockBuilders(self):  # pragma: no cover
        return AppBlockBuilder.make_many(self.boto3_raw_data["AppBlockBuilders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAppBlockBuildersResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppBlockBuildersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAppBlockBuilderResult:
    boto3_raw_data: "type_defs.StartAppBlockBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def AppBlockBuilder(self):  # pragma: no cover
        return AppBlockBuilder.make_one(self.boto3_raw_data["AppBlockBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAppBlockBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAppBlockBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAppBlockBuilderResult:
    boto3_raw_data: "type_defs.StopAppBlockBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def AppBlockBuilder(self):  # pragma: no cover
        return AppBlockBuilder.make_one(self.boto3_raw_data["AppBlockBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopAppBlockBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAppBlockBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppBlockBuilderResult:
    boto3_raw_data: "type_defs.UpdateAppBlockBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def AppBlockBuilder(self):  # pragma: no cover
        return AppBlockBuilder.make_one(self.boto3_raw_data["AppBlockBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAppBlockBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppBlockBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResult:
    boto3_raw_data: "type_defs.CreateApplicationResultTypeDef" = dataclasses.field()

    @cached_property
    def Application(self):  # pragma: no cover
        return Application.make_one(self.boto3_raw_data["Application"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationsResult:
    boto3_raw_data: "type_defs.DescribeApplicationsResultTypeDef" = dataclasses.field()

    @cached_property
    def Applications(self):  # pragma: no cover
        return Application.make_many(self.boto3_raw_data["Applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Image:
    boto3_raw_data: "type_defs.ImageTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    BaseImageArn = field("BaseImageArn")
    DisplayName = field("DisplayName")
    State = field("State")
    Visibility = field("Visibility")
    ImageBuilderSupported = field("ImageBuilderSupported")
    ImageBuilderName = field("ImageBuilderName")
    Platform = field("Platform")
    Description = field("Description")

    @cached_property
    def StateChangeReason(self):  # pragma: no cover
        return ImageStateChangeReason.make_one(self.boto3_raw_data["StateChangeReason"])

    @cached_property
    def Applications(self):  # pragma: no cover
        return Application.make_many(self.boto3_raw_data["Applications"])

    CreatedTime = field("CreatedTime")
    PublicBaseImageReleasedDate = field("PublicBaseImageReleasedDate")
    AppstreamAgentVersion = field("AppstreamAgentVersion")

    @cached_property
    def ImagePermissions(self):  # pragma: no cover
        return ImagePermissions.make_one(self.boto3_raw_data["ImagePermissions"])

    @cached_property
    def ImageErrors(self):  # pragma: no cover
        return ResourceError.make_many(self.boto3_raw_data["ImageErrors"])

    LatestAppstreamAgentVersion = field("LatestAppstreamAgentVersion")
    SupportedInstanceFamilies = field("SupportedInstanceFamilies")
    DynamicAppProvidersEnabled = field("DynamicAppProvidersEnabled")
    ImageSharedWithOthers = field("ImageSharedWithOthers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResult:
    boto3_raw_data: "type_defs.UpdateApplicationResultTypeDef" = dataclasses.field()

    @cached_property
    def Application(self):  # pragma: no cover
        return Application.make_one(self.boto3_raw_data["Application"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppBlock:
    boto3_raw_data: "type_defs.AppBlockTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    DisplayName = field("DisplayName")

    @cached_property
    def SourceS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SourceS3Location"])

    @cached_property
    def SetupScriptDetails(self):  # pragma: no cover
        return ScriptDetails.make_one(self.boto3_raw_data["SetupScriptDetails"])

    CreatedTime = field("CreatedTime")

    @cached_property
    def PostSetupScriptDetails(self):  # pragma: no cover
        return ScriptDetails.make_one(self.boto3_raw_data["PostSetupScriptDetails"])

    PackagingType = field("PackagingType")
    State = field("State")

    @cached_property
    def AppBlockErrors(self):  # pragma: no cover
        return ErrorDetails.make_many(self.boto3_raw_data["AppBlockErrors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppBlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppBlockRequest:
    boto3_raw_data: "type_defs.CreateAppBlockRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def SourceS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SourceS3Location"])

    Description = field("Description")
    DisplayName = field("DisplayName")

    @cached_property
    def SetupScriptDetails(self):  # pragma: no cover
        return ScriptDetails.make_one(self.boto3_raw_data["SetupScriptDetails"])

    Tags = field("Tags")

    @cached_property
    def PostSetupScriptDetails(self):  # pragma: no cover
        return ScriptDetails.make_one(self.boto3_raw_data["PostSetupScriptDetails"])

    PackagingType = field("PackagingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAppBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateUserStackResult:
    boto3_raw_data: "type_defs.BatchAssociateUserStackResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return UserStackAssociationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchAssociateUserStackResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateUserStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateUserStackResult:
    boto3_raw_data: "type_defs.BatchDisassociateUserStackResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return UserStackAssociationError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDisassociateUserStackResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateUserStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryConfigResult:
    boto3_raw_data: "type_defs.CreateDirectoryConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def DirectoryConfig(self):  # pragma: no cover
        return DirectoryConfig.make_one(self.boto3_raw_data["DirectoryConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDirectoryConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoryConfigsResult:
    boto3_raw_data: "type_defs.DescribeDirectoryConfigsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DirectoryConfigs(self):  # pragma: no cover
        return DirectoryConfig.make_many(self.boto3_raw_data["DirectoryConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDirectoryConfigsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoryConfigsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectoryConfigResult:
    boto3_raw_data: "type_defs.UpdateDirectoryConfigResultTypeDef" = dataclasses.field()

    @cached_property
    def DirectoryConfig(self):  # pragma: no cover
        return DirectoryConfig.make_one(self.boto3_raw_data["DirectoryConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDirectoryConfigResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectoryConfigResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEntitlementResult:
    boto3_raw_data: "type_defs.CreateEntitlementResultTypeDef" = dataclasses.field()

    @cached_property
    def Entitlement(self):  # pragma: no cover
        return Entitlement.make_one(self.boto3_raw_data["Entitlement"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEntitlementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEntitlementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntitlementsResult:
    boto3_raw_data: "type_defs.DescribeEntitlementsResultTypeDef" = dataclasses.field()

    @cached_property
    def Entitlements(self):  # pragma: no cover
        return Entitlement.make_many(self.boto3_raw_data["Entitlements"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEntitlementsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntitlementsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEntitlementResult:
    boto3_raw_data: "type_defs.UpdateEntitlementResultTypeDef" = dataclasses.field()

    @cached_property
    def Entitlement(self):  # pragma: no cover
        return Entitlement.make_one(self.boto3_raw_data["Entitlement"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEntitlementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEntitlementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThemeForStackResult:
    boto3_raw_data: "type_defs.CreateThemeForStackResultTypeDef" = dataclasses.field()

    @cached_property
    def Theme(self):  # pragma: no cover
        return Theme.make_one(self.boto3_raw_data["Theme"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThemeForStackResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThemeForStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThemeForStackResult:
    boto3_raw_data: "type_defs.DescribeThemeForStackResultTypeDef" = dataclasses.field()

    @cached_property
    def Theme(self):  # pragma: no cover
        return Theme.make_one(self.boto3_raw_data["Theme"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThemeForStackResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThemeForStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThemeForStackResult:
    boto3_raw_data: "type_defs.UpdateThemeForStackResultTypeDef" = dataclasses.field()

    @cached_property
    def Theme(self):  # pragma: no cover
        return Theme.make_one(self.boto3_raw_data["Theme"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThemeForStackResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThemeForStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetResult:
    boto3_raw_data: "type_defs.CreateFleetResultTypeDef" = dataclasses.field()

    @cached_property
    def Fleet(self):  # pragma: no cover
        return Fleet.make_one(self.boto3_raw_data["Fleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFleetResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetsResult:
    boto3_raw_data: "type_defs.DescribeFleetsResultTypeDef" = dataclasses.field()

    @cached_property
    def Fleets(self):  # pragma: no cover
        return Fleet.make_many(self.boto3_raw_data["Fleets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetResult:
    boto3_raw_data: "type_defs.UpdateFleetResultTypeDef" = dataclasses.field()

    @cached_property
    def Fleet(self):  # pragma: no cover
        return Fleet.make_one(self.boto3_raw_data["Fleet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageBuilderResult:
    boto3_raw_data: "type_defs.CreateImageBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def ImageBuilder(self):  # pragma: no cover
        return ImageBuilder.make_one(self.boto3_raw_data["ImageBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImageBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageBuilderResult:
    boto3_raw_data: "type_defs.DeleteImageBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def ImageBuilder(self):  # pragma: no cover
        return ImageBuilder.make_one(self.boto3_raw_data["ImageBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImageBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageBuildersResult:
    boto3_raw_data: "type_defs.DescribeImageBuildersResultTypeDef" = dataclasses.field()

    @cached_property
    def ImageBuilders(self):  # pragma: no cover
        return ImageBuilder.make_many(self.boto3_raw_data["ImageBuilders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImageBuildersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageBuildersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImageBuilderResult:
    boto3_raw_data: "type_defs.StartImageBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def ImageBuilder(self):  # pragma: no cover
        return ImageBuilder.make_one(self.boto3_raw_data["ImageBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImageBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImageBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopImageBuilderResult:
    boto3_raw_data: "type_defs.StopImageBuilderResultTypeDef" = dataclasses.field()

    @cached_property
    def ImageBuilder(self):  # pragma: no cover
        return ImageBuilder.make_one(self.boto3_raw_data["ImageBuilder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopImageBuilderResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopImageBuilderResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSessionsResult:
    boto3_raw_data: "type_defs.DescribeSessionsResultTypeDef" = dataclasses.field()

    @cached_property
    def Sessions(self):  # pragma: no cover
        return Session.make_many(self.boto3_raw_data["Sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSessionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSessionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagePermissionsResult:
    boto3_raw_data: "type_defs.DescribeImagePermissionsResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def SharedImagePermissionsList(self):  # pragma: no cover
        return SharedImagePermissions.make_many(
            self.boto3_raw_data["SharedImagePermissionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImagePermissionsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagePermissionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsageReportSubscriptionsResult:
    boto3_raw_data: "type_defs.DescribeUsageReportSubscriptionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UsageReportSubscriptions(self):  # pragma: no cover
        return UsageReportSubscription.make_many(
            self.boto3_raw_data["UsageReportSubscriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUsageReportSubscriptionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsageReportSubscriptionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackResult:
    boto3_raw_data: "type_defs.CreateStackResultTypeDef" = dataclasses.field()

    @cached_property
    def Stack(self):  # pragma: no cover
        return Stack.make_one(self.boto3_raw_data["Stack"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStackResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksResult:
    boto3_raw_data: "type_defs.DescribeStacksResultTypeDef" = dataclasses.field()

    @cached_property
    def Stacks(self):  # pragma: no cover
        return Stack.make_many(self.boto3_raw_data["Stacks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackResult:
    boto3_raw_data: "type_defs.UpdateStackResultTypeDef" = dataclasses.field()

    @cached_property
    def Stack(self):  # pragma: no cover
        return Stack.make_one(self.boto3_raw_data["Stack"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateStackResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackRequest:
    boto3_raw_data: "type_defs.CreateStackRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    DisplayName = field("DisplayName")
    StorageConnectors = field("StorageConnectors")
    RedirectURL = field("RedirectURL")
    FeedbackURL = field("FeedbackURL")

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSetting.make_many(self.boto3_raw_data["UserSettings"])

    @cached_property
    def ApplicationSettings(self):  # pragma: no cover
        return ApplicationSettings.make_one(self.boto3_raw_data["ApplicationSettings"])

    Tags = field("Tags")

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    EmbedHostDomains = field("EmbedHostDomains")

    @cached_property
    def StreamingExperienceSettings(self):  # pragma: no cover
        return StreamingExperienceSettings.make_one(
            self.boto3_raw_data["StreamingExperienceSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackRequest:
    boto3_raw_data: "type_defs.UpdateStackRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    DisplayName = field("DisplayName")
    Description = field("Description")
    StorageConnectors = field("StorageConnectors")
    DeleteStorageConnectors = field("DeleteStorageConnectors")
    RedirectURL = field("RedirectURL")
    FeedbackURL = field("FeedbackURL")
    AttributesToDelete = field("AttributesToDelete")

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSetting.make_many(self.boto3_raw_data["UserSettings"])

    @cached_property
    def ApplicationSettings(self):  # pragma: no cover
        return ApplicationSettings.make_one(self.boto3_raw_data["ApplicationSettings"])

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    EmbedHostDomains = field("EmbedHostDomains")

    @cached_property
    def StreamingExperienceSettings(self):  # pragma: no cover
        return StreamingExperienceSettings.make_one(
            self.boto3_raw_data["StreamingExperienceSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppBlockBuilderRequest:
    boto3_raw_data: "type_defs.CreateAppBlockBuilderRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Platform = field("Platform")
    InstanceType = field("InstanceType")
    VpcConfig = field("VpcConfig")
    Description = field("Description")
    DisplayName = field("DisplayName")
    Tags = field("Tags")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")
    IamRoleArn = field("IamRoleArn")

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAppBlockBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppBlockBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetRequest:
    boto3_raw_data: "type_defs.CreateFleetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceType = field("InstanceType")
    ImageName = field("ImageName")
    ImageArn = field("ImageArn")
    FleetType = field("FleetType")

    @cached_property
    def ComputeCapacity(self):  # pragma: no cover
        return ComputeCapacity.make_one(self.boto3_raw_data["ComputeCapacity"])

    VpcConfig = field("VpcConfig")
    MaxUserDurationInSeconds = field("MaxUserDurationInSeconds")
    DisconnectTimeoutInSeconds = field("DisconnectTimeoutInSeconds")
    Description = field("Description")
    DisplayName = field("DisplayName")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")

    @cached_property
    def DomainJoinInfo(self):  # pragma: no cover
        return DomainJoinInfo.make_one(self.boto3_raw_data["DomainJoinInfo"])

    Tags = field("Tags")
    IdleDisconnectTimeoutInSeconds = field("IdleDisconnectTimeoutInSeconds")
    IamRoleArn = field("IamRoleArn")
    StreamView = field("StreamView")
    Platform = field("Platform")
    MaxConcurrentSessions = field("MaxConcurrentSessions")
    UsbDeviceFilterStrings = field("UsbDeviceFilterStrings")

    @cached_property
    def SessionScriptS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SessionScriptS3Location"])

    MaxSessionsPerInstance = field("MaxSessionsPerInstance")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImageBuilderRequest:
    boto3_raw_data: "type_defs.CreateImageBuilderRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceType = field("InstanceType")
    ImageName = field("ImageName")
    ImageArn = field("ImageArn")
    Description = field("Description")
    DisplayName = field("DisplayName")
    VpcConfig = field("VpcConfig")
    IamRoleArn = field("IamRoleArn")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")

    @cached_property
    def DomainJoinInfo(self):  # pragma: no cover
        return DomainJoinInfo.make_one(self.boto3_raw_data["DomainJoinInfo"])

    AppstreamAgentVersion = field("AppstreamAgentVersion")
    Tags = field("Tags")

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateImageBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImageBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAppBlockBuilderRequest:
    boto3_raw_data: "type_defs.UpdateAppBlockBuilderRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    DisplayName = field("DisplayName")
    Platform = field("Platform")
    InstanceType = field("InstanceType")
    VpcConfig = field("VpcConfig")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")
    IamRoleArn = field("IamRoleArn")

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    AttributesToDelete = field("AttributesToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAppBlockBuilderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAppBlockBuilderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetRequest:
    boto3_raw_data: "type_defs.UpdateFleetRequestTypeDef" = dataclasses.field()

    ImageName = field("ImageName")
    ImageArn = field("ImageArn")
    Name = field("Name")
    InstanceType = field("InstanceType")

    @cached_property
    def ComputeCapacity(self):  # pragma: no cover
        return ComputeCapacity.make_one(self.boto3_raw_data["ComputeCapacity"])

    VpcConfig = field("VpcConfig")
    MaxUserDurationInSeconds = field("MaxUserDurationInSeconds")
    DisconnectTimeoutInSeconds = field("DisconnectTimeoutInSeconds")
    DeleteVpcConfig = field("DeleteVpcConfig")
    Description = field("Description")
    DisplayName = field("DisplayName")
    EnableDefaultInternetAccess = field("EnableDefaultInternetAccess")

    @cached_property
    def DomainJoinInfo(self):  # pragma: no cover
        return DomainJoinInfo.make_one(self.boto3_raw_data["DomainJoinInfo"])

    IdleDisconnectTimeoutInSeconds = field("IdleDisconnectTimeoutInSeconds")
    AttributesToDelete = field("AttributesToDelete")
    IamRoleArn = field("IamRoleArn")
    StreamView = field("StreamView")
    Platform = field("Platform")
    MaxConcurrentSessions = field("MaxConcurrentSessions")
    UsbDeviceFilterStrings = field("UsbDeviceFilterStrings")

    @cached_property
    def SessionScriptS3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SessionScriptS3Location"])

    MaxSessionsPerInstance = field("MaxSessionsPerInstance")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUpdatedImageResult:
    boto3_raw_data: "type_defs.CreateUpdatedImageResultTypeDef" = dataclasses.field()

    @cached_property
    def image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["image"])

    canUpdateImage = field("canUpdateImage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUpdatedImageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUpdatedImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImageResult:
    boto3_raw_data: "type_defs.DeleteImageResultTypeDef" = dataclasses.field()

    @cached_property
    def Image(self):  # pragma: no cover
        return Image.make_one(self.boto3_raw_data["Image"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteImageResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImagesResult:
    boto3_raw_data: "type_defs.DescribeImagesResultTypeDef" = dataclasses.field()

    @cached_property
    def Images(self):  # pragma: no cover
        return Image.make_many(self.boto3_raw_data["Images"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImagesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImagesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppBlockResult:
    boto3_raw_data: "type_defs.CreateAppBlockResultTypeDef" = dataclasses.field()

    @cached_property
    def AppBlock(self):  # pragma: no cover
        return AppBlock.make_one(self.boto3_raw_data["AppBlock"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAppBlockResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppBlockResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAppBlocksResult:
    boto3_raw_data: "type_defs.DescribeAppBlocksResultTypeDef" = dataclasses.field()

    @cached_property
    def AppBlocks(self):  # pragma: no cover
        return AppBlock.make_many(self.boto3_raw_data["AppBlocks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAppBlocksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAppBlocksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
