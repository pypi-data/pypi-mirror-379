# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ds import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptSharedDirectoryRequest:
    boto3_raw_data: "type_defs.AcceptSharedDirectoryRequestTypeDef" = (
        dataclasses.field()
    )

    SharedDirectoryId = field("SharedDirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptSharedDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptSharedDirectoryRequestTypeDef"]
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
class SharedDirectory:
    boto3_raw_data: "type_defs.SharedDirectoryTypeDef" = dataclasses.field()

    OwnerAccountId = field("OwnerAccountId")
    OwnerDirectoryId = field("OwnerDirectoryId")
    ShareMethod = field("ShareMethod")
    SharedAccountId = field("SharedAccountId")
    SharedDirectoryId = field("SharedDirectoryId")
    ShareStatus = field("ShareStatus")
    ShareNotes = field("ShareNotes")
    CreatedDateTime = field("CreatedDateTime")
    LastUpdatedDateTime = field("LastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SharedDirectoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SharedDirectoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpRoute:
    boto3_raw_data: "type_defs.IpRouteTypeDef" = dataclasses.field()

    CidrIp = field("CidrIp")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpRouteTypeDef"]]
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
class AssessmentValidation:
    boto3_raw_data: "type_defs.AssessmentValidationTypeDef" = dataclasses.field()

    Category = field("Category")
    Name = field("Name")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusReason = field("StatusReason")
    StartTime = field("StartTime")
    LastUpdateDateTime = field("LastUpdateDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentValidationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentValidationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentSummary:
    boto3_raw_data: "type_defs.AssessmentSummaryTypeDef" = dataclasses.field()

    AssessmentId = field("AssessmentId")
    DirectoryId = field("DirectoryId")
    DnsName = field("DnsName")
    StartTime = field("StartTime")
    LastUpdateDateTime = field("LastUpdateDateTime")
    Status = field("Status")
    CustomerDnsIps = field("CustomerDnsIps")
    ReportType = field("ReportType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Assessment:
    boto3_raw_data: "type_defs.AssessmentTypeDef" = dataclasses.field()

    AssessmentId = field("AssessmentId")
    DirectoryId = field("DirectoryId")
    DnsName = field("DnsName")
    StartTime = field("StartTime")
    LastUpdateDateTime = field("LastUpdateDateTime")
    Status = field("Status")
    StatusCode = field("StatusCode")
    StatusReason = field("StatusReason")
    CustomerDnsIps = field("CustomerDnsIps")
    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    SelfManagedInstanceIds = field("SelfManagedInstanceIds")
    ReportType = field("ReportType")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssessmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    Name = field("Name")
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
class CancelSchemaExtensionRequest:
    boto3_raw_data: "type_defs.CancelSchemaExtensionRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    SchemaExtensionId = field("SchemaExtensionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSchemaExtensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSchemaExtensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateInfo:
    boto3_raw_data: "type_defs.CertificateInfoTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")
    CommonName = field("CommonName")
    State = field("State")
    ExpiryDateTime = field("ExpiryDateTime")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientCertAuthSettings:
    boto3_raw_data: "type_defs.ClientCertAuthSettingsTypeDef" = dataclasses.field()

    OCSPUrl = field("OCSPUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientCertAuthSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientCertAuthSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientAuthenticationSettingInfo:
    boto3_raw_data: "type_defs.ClientAuthenticationSettingInfoTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Status = field("Status")
    LastUpdatedDateTime = field("LastUpdatedDateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClientAuthenticationSettingInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientAuthenticationSettingInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalForwarder:
    boto3_raw_data: "type_defs.ConditionalForwarderTypeDef" = dataclasses.field()

    RemoteDomainName = field("RemoteDomainName")
    DnsIpAddrs = field("DnsIpAddrs")
    ReplicationScope = field("ReplicationScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionalForwarderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalForwarderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryConnectSettings:
    boto3_raw_data: "type_defs.DirectoryConnectSettingsTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    CustomerDnsIps = field("CustomerDnsIps")
    CustomerUserName = field("CustomerUserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectoryConnectSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryConnectSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasRequest:
    boto3_raw_data: "type_defs.CreateAliasRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Alias = field("Alias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConditionalForwarderRequest:
    boto3_raw_data: "type_defs.CreateConditionalForwarderRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    RemoteDomainName = field("RemoteDomainName")
    DnsIpAddrs = field("DnsIpAddrs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConditionalForwarderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConditionalForwarderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateLogSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    LogGroupName = field("LogGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLogSubscriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotRequest:
    boto3_raw_data: "type_defs.CreateSnapshotRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustRequest:
    boto3_raw_data: "type_defs.CreateTrustRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    RemoteDomainName = field("RemoteDomainName")
    TrustPassword = field("TrustPassword")
    TrustDirection = field("TrustDirection")
    TrustType = field("TrustType")
    ConditionalForwarderIpAddrs = field("ConditionalForwarderIpAddrs")
    SelectiveAuth = field("SelectiveAuth")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrustRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteADAssessmentRequest:
    boto3_raw_data: "type_defs.DeleteADAssessmentRequestTypeDef" = dataclasses.field()

    AssessmentId = field("AssessmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteADAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteADAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConditionalForwarderRequest:
    boto3_raw_data: "type_defs.DeleteConditionalForwarderRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    RemoteDomainName = field("RemoteDomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConditionalForwarderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConditionalForwarderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectoryRequest:
    boto3_raw_data: "type_defs.DeleteDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLogSubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteLogSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLogSubscriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLogSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotRequest:
    boto3_raw_data: "type_defs.DeleteSnapshotRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrustRequest:
    boto3_raw_data: "type_defs.DeleteTrustRequestTypeDef" = dataclasses.field()

    TrustId = field("TrustId")
    DeleteAssociatedConditionalForwarder = field("DeleteAssociatedConditionalForwarder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrustRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrustRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterCertificateRequest:
    boto3_raw_data: "type_defs.DeregisterCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    CertificateId = field("CertificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterEventTopicRequest:
    boto3_raw_data: "type_defs.DeregisterEventTopicRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    TopicName = field("TopicName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterEventTopicRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterEventTopicRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeADAssessmentRequest:
    boto3_raw_data: "type_defs.DescribeADAssessmentRequestTypeDef" = dataclasses.field()

    AssessmentId = field("AssessmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeADAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeADAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCAEnrollmentPolicyRequest:
    boto3_raw_data: "type_defs.DescribeCAEnrollmentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCAEnrollmentPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCAEnrollmentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateRequest:
    boto3_raw_data: "type_defs.DescribeCertificateRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    CertificateId = field("CertificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateRequestTypeDef"]
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
class DescribeClientAuthenticationSettingsRequest:
    boto3_raw_data: "type_defs.DescribeClientAuthenticationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    Type = field("Type")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClientAuthenticationSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClientAuthenticationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConditionalForwardersRequest:
    boto3_raw_data: "type_defs.DescribeConditionalForwardersRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    RemoteDomainNames = field("RemoteDomainNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConditionalForwardersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConditionalForwardersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoriesRequest:
    boto3_raw_data: "type_defs.DescribeDirectoriesRequestTypeDef" = dataclasses.field()

    DirectoryIds = field("DirectoryIds")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDirectoriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoryDataAccessRequest:
    boto3_raw_data: "type_defs.DescribeDirectoryDataAccessRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectoryDataAccessRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoryDataAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainControllersRequest:
    boto3_raw_data: "type_defs.DescribeDomainControllersRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    DomainControllerIds = field("DomainControllerIds")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDomainControllersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainControllersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainController:
    boto3_raw_data: "type_defs.DomainControllerTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    DomainControllerId = field("DomainControllerId")
    DnsIpAddr = field("DnsIpAddr")
    VpcId = field("VpcId")
    SubnetId = field("SubnetId")
    AvailabilityZone = field("AvailabilityZone")
    Status = field("Status")
    StatusReason = field("StatusReason")
    LaunchTime = field("LaunchTime")
    StatusLastUpdatedDateTime = field("StatusLastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainControllerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainControllerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTopicsRequest:
    boto3_raw_data: "type_defs.DescribeEventTopicsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    TopicNames = field("TopicNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventTopicsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTopicsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTopic:
    boto3_raw_data: "type_defs.EventTopicTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    TopicName = field("TopicName")
    TopicArn = field("TopicArn")
    CreatedDateTime = field("CreatedDateTime")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTopicTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTopicTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHybridADUpdateRequest:
    boto3_raw_data: "type_defs.DescribeHybridADUpdateRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    UpdateType = field("UpdateType")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeHybridADUpdateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHybridADUpdateRequestTypeDef"]
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
class DescribeLDAPSSettingsRequest:
    boto3_raw_data: "type_defs.DescribeLDAPSSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    Type = field("Type")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLDAPSSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLDAPSSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LDAPSSettingInfo:
    boto3_raw_data: "type_defs.LDAPSSettingInfoTypeDef" = dataclasses.field()

    LDAPSStatus = field("LDAPSStatus")
    LDAPSStatusReason = field("LDAPSStatusReason")
    LastUpdatedDateTime = field("LastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LDAPSSettingInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LDAPSSettingInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegionsRequest:
    boto3_raw_data: "type_defs.DescribeRegionsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    RegionName = field("RegionName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRegionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSettingsRequest:
    boto3_raw_data: "type_defs.DescribeSettingsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Status = field("Status")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SettingEntry:
    boto3_raw_data: "type_defs.SettingEntryTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")
    AllowedValues = field("AllowedValues")
    AppliedValue = field("AppliedValue")
    RequestedValue = field("RequestedValue")
    RequestStatus = field("RequestStatus")
    RequestDetailedStatus = field("RequestDetailedStatus")
    RequestStatusMessage = field("RequestStatusMessage")
    LastUpdatedDateTime = field("LastUpdatedDateTime")
    LastRequestedDateTime = field("LastRequestedDateTime")
    DataType = field("DataType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSharedDirectoriesRequest:
    boto3_raw_data: "type_defs.DescribeSharedDirectoriesRequestTypeDef" = (
        dataclasses.field()
    )

    OwnerDirectoryId = field("OwnerDirectoryId")
    SharedDirectoryIds = field("SharedDirectoryIds")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSharedDirectoriesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSharedDirectoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsRequest:
    boto3_raw_data: "type_defs.DescribeSnapshotsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SnapshotIds = field("SnapshotIds")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsRequestTypeDef"]
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

    DirectoryId = field("DirectoryId")
    SnapshotId = field("SnapshotId")
    Type = field("Type")
    Name = field("Name")
    Status = field("Status")
    StartTime = field("StartTime")

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
class DescribeTrustsRequest:
    boto3_raw_data: "type_defs.DescribeTrustsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    TrustIds = field("TrustIds")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrustsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trust:
    boto3_raw_data: "type_defs.TrustTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    TrustId = field("TrustId")
    RemoteDomainName = field("RemoteDomainName")
    TrustType = field("TrustType")
    TrustDirection = field("TrustDirection")
    TrustState = field("TrustState")
    CreatedDateTime = field("CreatedDateTime")
    LastUpdatedDateTime = field("LastUpdatedDateTime")
    StateLastUpdatedDateTime = field("StateLastUpdatedDateTime")
    TrustStateReason = field("TrustStateReason")
    SelectiveAuth = field("SelectiveAuth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrustTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateDirectoryRequest:
    boto3_raw_data: "type_defs.DescribeUpdateDirectoryRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    UpdateType = field("UpdateType")
    RegionName = field("RegionName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUpdateDirectoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryConnectSettingsDescription:
    boto3_raw_data: "type_defs.DirectoryConnectSettingsDescriptionTypeDef" = (
        dataclasses.field()
    )

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    CustomerUserName = field("CustomerUserName")
    SecurityGroupId = field("SecurityGroupId")
    AvailabilityZones = field("AvailabilityZones")
    ConnectIps = field("ConnectIps")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DirectoryConnectSettingsDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryConnectSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryVpcSettingsDescription:
    boto3_raw_data: "type_defs.DirectoryVpcSettingsDescriptionTypeDef" = (
        dataclasses.field()
    )

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    SecurityGroupId = field("SecurityGroupId")
    AvailabilityZones = field("AvailabilityZones")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DirectoryVpcSettingsDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryVpcSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridSettingsDescription:
    boto3_raw_data: "type_defs.HybridSettingsDescriptionTypeDef" = dataclasses.field()

    SelfManagedDnsIpAddrs = field("SelfManagedDnsIpAddrs")
    SelfManagedInstanceIds = field("SelfManagedInstanceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HybridSettingsDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RadiusSettingsOutput:
    boto3_raw_data: "type_defs.RadiusSettingsOutputTypeDef" = dataclasses.field()

    RadiusServers = field("RadiusServers")
    RadiusPort = field("RadiusPort")
    RadiusTimeout = field("RadiusTimeout")
    RadiusRetries = field("RadiusRetries")
    SharedSecret = field("SharedSecret")
    AuthenticationProtocol = field("AuthenticationProtocol")
    DisplayLabel = field("DisplayLabel")
    UseSameUsername = field("UseSameUsername")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RadiusSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RadiusSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionsInfo:
    boto3_raw_data: "type_defs.RegionsInfoTypeDef" = dataclasses.field()

    PrimaryRegion = field("PrimaryRegion")
    AdditionalRegions = field("AdditionalRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionsInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionsInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryLimits:
    boto3_raw_data: "type_defs.DirectoryLimitsTypeDef" = dataclasses.field()

    CloudOnlyDirectoriesLimit = field("CloudOnlyDirectoriesLimit")
    CloudOnlyDirectoriesCurrentCount = field("CloudOnlyDirectoriesCurrentCount")
    CloudOnlyDirectoriesLimitReached = field("CloudOnlyDirectoriesLimitReached")
    CloudOnlyMicrosoftADLimit = field("CloudOnlyMicrosoftADLimit")
    CloudOnlyMicrosoftADCurrentCount = field("CloudOnlyMicrosoftADCurrentCount")
    CloudOnlyMicrosoftADLimitReached = field("CloudOnlyMicrosoftADLimitReached")
    ConnectedDirectoriesLimit = field("ConnectedDirectoriesLimit")
    ConnectedDirectoriesCurrentCount = field("ConnectedDirectoriesCurrentCount")
    ConnectedDirectoriesLimitReached = field("ConnectedDirectoriesLimitReached")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DirectoryLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DirectoryLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryVpcSettingsOutput:
    boto3_raw_data: "type_defs.DirectoryVpcSettingsOutputTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectoryVpcSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryVpcSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryVpcSettings:
    boto3_raw_data: "type_defs.DirectoryVpcSettingsTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectoryVpcSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryVpcSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableCAEnrollmentPolicyRequest:
    boto3_raw_data: "type_defs.DisableCAEnrollmentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableCAEnrollmentPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableCAEnrollmentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableClientAuthenticationRequest:
    boto3_raw_data: "type_defs.DisableClientAuthenticationRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableClientAuthenticationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableClientAuthenticationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDirectoryDataAccessRequest:
    boto3_raw_data: "type_defs.DisableDirectoryDataAccessRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableDirectoryDataAccessRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDirectoryDataAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableLDAPSRequest:
    boto3_raw_data: "type_defs.DisableLDAPSRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableLDAPSRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableLDAPSRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableRadiusRequest:
    boto3_raw_data: "type_defs.DisableRadiusRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableRadiusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableRadiusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableSsoRequest:
    boto3_raw_data: "type_defs.DisableSsoRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    Password = field("Password")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisableSsoRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableSsoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableCAEnrollmentPolicyRequest:
    boto3_raw_data: "type_defs.EnableCAEnrollmentPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    PcaConnectorArn = field("PcaConnectorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableCAEnrollmentPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableCAEnrollmentPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableClientAuthenticationRequest:
    boto3_raw_data: "type_defs.EnableClientAuthenticationRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableClientAuthenticationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableClientAuthenticationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDirectoryDataAccessRequest:
    boto3_raw_data: "type_defs.EnableDirectoryDataAccessRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableDirectoryDataAccessRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDirectoryDataAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableLDAPSRequest:
    boto3_raw_data: "type_defs.EnableLDAPSRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableLDAPSRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableLDAPSRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableSsoRequest:
    boto3_raw_data: "type_defs.EnableSsoRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    Password = field("Password")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableSsoRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableSsoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotLimitsRequest:
    boto3_raw_data: "type_defs.GetSnapshotLimitsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotLimitsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotLimits:
    boto3_raw_data: "type_defs.SnapshotLimitsTypeDef" = dataclasses.field()

    ManualSnapshotsLimit = field("ManualSnapshotsLimit")
    ManualSnapshotsCurrentCount = field("ManualSnapshotsCurrentCount")
    ManualSnapshotsLimitReached = field("ManualSnapshotsLimitReached")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridAdministratorAccountUpdate:
    boto3_raw_data: "type_defs.HybridAdministratorAccountUpdateTypeDef" = (
        dataclasses.field()
    )

    SecretArn = field("SecretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HybridAdministratorAccountUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridAdministratorAccountUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridCustomerInstancesSettings:
    boto3_raw_data: "type_defs.HybridCustomerInstancesSettingsTypeDef" = (
        dataclasses.field()
    )

    CustomerDnsIps = field("CustomerDnsIps")
    InstanceIds = field("InstanceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HybridCustomerInstancesSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridCustomerInstancesSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridUpdateValue:
    boto3_raw_data: "type_defs.HybridUpdateValueTypeDef" = dataclasses.field()

    InstanceIds = field("InstanceIds")
    DnsIps = field("DnsIps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HybridUpdateValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridUpdateValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpRouteInfo:
    boto3_raw_data: "type_defs.IpRouteInfoTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    CidrIp = field("CidrIp")
    IpRouteStatusMsg = field("IpRouteStatusMsg")
    AddedDateTime = field("AddedDateTime")
    IpRouteStatusReason = field("IpRouteStatusReason")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpRouteInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpRouteInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListADAssessmentsRequest:
    boto3_raw_data: "type_defs.ListADAssessmentsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListADAssessmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListADAssessmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequest:
    boto3_raw_data: "type_defs.ListCertificatesRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIpRoutesRequest:
    boto3_raw_data: "type_defs.ListIpRoutesRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIpRoutesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIpRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListLogSubscriptionsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogSubscriptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSubscription:
    boto3_raw_data: "type_defs.LogSubscriptionTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    LogGroupName = field("LogGroupName")
    SubscriptionCreatedDateTime = field("SubscriptionCreatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogSubscriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemaExtensionsRequest:
    boto3_raw_data: "type_defs.ListSchemaExtensionsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemaExtensionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemaExtensionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaExtensionInfo:
    boto3_raw_data: "type_defs.SchemaExtensionInfoTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SchemaExtensionId = field("SchemaExtensionId")
    Description = field("Description")
    SchemaExtensionStatus = field("SchemaExtensionStatus")
    SchemaExtensionStatusReason = field("SchemaExtensionStatusReason")
    StartDateTime = field("StartDateTime")
    EndDateTime = field("EndDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaExtensionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaExtensionInfoTypeDef"]
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

    ResourceId = field("ResourceId")
    NextToken = field("NextToken")
    Limit = field("Limit")

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
class OSUpdateSettings:
    boto3_raw_data: "type_defs.OSUpdateSettingsTypeDef" = dataclasses.field()

    OSVersion = field("OSVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OSUpdateSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OSUpdateSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RadiusSettings:
    boto3_raw_data: "type_defs.RadiusSettingsTypeDef" = dataclasses.field()

    RadiusServers = field("RadiusServers")
    RadiusPort = field("RadiusPort")
    RadiusTimeout = field("RadiusTimeout")
    RadiusRetries = field("RadiusRetries")
    SharedSecret = field("SharedSecret")
    AuthenticationProtocol = field("AuthenticationProtocol")
    DisplayLabel = field("DisplayLabel")
    UseSameUsername = field("UseSameUsername")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RadiusSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RadiusSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterEventTopicRequest:
    boto3_raw_data: "type_defs.RegisterEventTopicRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    TopicName = field("TopicName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterEventTopicRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterEventTopicRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectSharedDirectoryRequest:
    boto3_raw_data: "type_defs.RejectSharedDirectoryRequestTypeDef" = (
        dataclasses.field()
    )

    SharedDirectoryId = field("SharedDirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectSharedDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectSharedDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveIpRoutesRequest:
    boto3_raw_data: "type_defs.RemoveIpRoutesRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    CidrIps = field("CidrIps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveIpRoutesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveIpRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveRegionRequest:
    boto3_raw_data: "type_defs.RemoveRegionRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveRegionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveRegionRequestTypeDef"]
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
class ResetUserPasswordRequest:
    boto3_raw_data: "type_defs.ResetUserPasswordRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    NewPassword = field("NewPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetUserPasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetUserPasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreFromSnapshotRequest:
    boto3_raw_data: "type_defs.RestoreFromSnapshotRequestTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreFromSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreFromSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Setting:
    boto3_raw_data: "type_defs.SettingTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareTarget:
    boto3_raw_data: "type_defs.ShareTargetTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareTargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSchemaExtensionRequest:
    boto3_raw_data: "type_defs.StartSchemaExtensionRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    CreateSnapshotBeforeSchemaExtension = field("CreateSnapshotBeforeSchemaExtension")
    LdifContent = field("LdifContent")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSchemaExtensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSchemaExtensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnshareTarget:
    boto3_raw_data: "type_defs.UnshareTargetTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnshareTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnshareTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConditionalForwarderRequest:
    boto3_raw_data: "type_defs.UpdateConditionalForwarderRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    RemoteDomainName = field("RemoteDomainName")
    DnsIpAddrs = field("DnsIpAddrs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConditionalForwarderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConditionalForwarderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNumberOfDomainControllersRequest:
    boto3_raw_data: "type_defs.UpdateNumberOfDomainControllersRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    DesiredNumber = field("DesiredNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNumberOfDomainControllersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNumberOfDomainControllersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustRequest:
    boto3_raw_data: "type_defs.UpdateTrustRequestTypeDef" = dataclasses.field()

    TrustId = field("TrustId")
    SelectiveAuth = field("SelectiveAuth")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrustRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyTrustRequest:
    boto3_raw_data: "type_defs.VerifyTrustRequestTypeDef" = dataclasses.field()

    TrustId = field("TrustId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyTrustRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyTrustRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectDirectoryResult:
    boto3_raw_data: "type_defs.ConnectDirectoryResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasResult:
    boto3_raw_data: "type_defs.CreateAliasResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Alias = field("Alias")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAliasResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryResult:
    boto3_raw_data: "type_defs.CreateDirectoryResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHybridADResult:
    boto3_raw_data: "type_defs.CreateHybridADResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHybridADResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHybridADResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMicrosoftADResult:
    boto3_raw_data: "type_defs.CreateMicrosoftADResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMicrosoftADResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMicrosoftADResultTypeDef"]
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

    SnapshotId = field("SnapshotId")

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
class CreateTrustResult:
    boto3_raw_data: "type_defs.CreateTrustResultTypeDef" = dataclasses.field()

    TrustId = field("TrustId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTrustResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteADAssessmentResult:
    boto3_raw_data: "type_defs.DeleteADAssessmentResultTypeDef" = dataclasses.field()

    AssessmentId = field("AssessmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteADAssessmentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteADAssessmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectoryResult:
    boto3_raw_data: "type_defs.DeleteDirectoryResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectoryResultTypeDef"]
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

    SnapshotId = field("SnapshotId")

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
class DeleteTrustResult:
    boto3_raw_data: "type_defs.DeleteTrustResultTypeDef" = dataclasses.field()

    TrustId = field("TrustId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTrustResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrustResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCAEnrollmentPolicyResult:
    boto3_raw_data: "type_defs.DescribeCAEnrollmentPolicyResultTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    PcaConnectorArn = field("PcaConnectorArn")
    CaEnrollmentPolicyStatus = field("CaEnrollmentPolicyStatus")
    LastUpdatedDateTime = field("LastUpdatedDateTime")
    CaEnrollmentPolicyStatusReason = field("CaEnrollmentPolicyStatusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCAEnrollmentPolicyResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCAEnrollmentPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoryDataAccessResult:
    boto3_raw_data: "type_defs.DescribeDirectoryDataAccessResultTypeDef" = (
        dataclasses.field()
    )

    DataAccessStatus = field("DataAccessStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectoryDataAccessResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoryDataAccessResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCertificateResult:
    boto3_raw_data: "type_defs.RegisterCertificateResultTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterCertificateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectSharedDirectoryResult:
    boto3_raw_data: "type_defs.RejectSharedDirectoryResultTypeDef" = dataclasses.field()

    SharedDirectoryId = field("SharedDirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectSharedDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectSharedDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareDirectoryResult:
    boto3_raw_data: "type_defs.ShareDirectoryResultTypeDef" = dataclasses.field()

    SharedDirectoryId = field("SharedDirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShareDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShareDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartADAssessmentResult:
    boto3_raw_data: "type_defs.StartADAssessmentResultTypeDef" = dataclasses.field()

    AssessmentId = field("AssessmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartADAssessmentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartADAssessmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSchemaExtensionResult:
    boto3_raw_data: "type_defs.StartSchemaExtensionResultTypeDef" = dataclasses.field()

    SchemaExtensionId = field("SchemaExtensionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSchemaExtensionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSchemaExtensionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnshareDirectoryResult:
    boto3_raw_data: "type_defs.UnshareDirectoryResultTypeDef" = dataclasses.field()

    SharedDirectoryId = field("SharedDirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnshareDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnshareDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHybridADResult:
    boto3_raw_data: "type_defs.UpdateHybridADResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    AssessmentId = field("AssessmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHybridADResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHybridADResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSettingsResult:
    boto3_raw_data: "type_defs.UpdateSettingsResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSettingsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSettingsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustResult:
    boto3_raw_data: "type_defs.UpdateTrustResultTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    TrustId = field("TrustId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTrustResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyTrustResult:
    boto3_raw_data: "type_defs.VerifyTrustResultTypeDef" = dataclasses.field()

    TrustId = field("TrustId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyTrustResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyTrustResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptSharedDirectoryResult:
    boto3_raw_data: "type_defs.AcceptSharedDirectoryResultTypeDef" = dataclasses.field()

    @cached_property
    def SharedDirectory(self):  # pragma: no cover
        return SharedDirectory.make_one(self.boto3_raw_data["SharedDirectory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptSharedDirectoryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptSharedDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSharedDirectoriesResult:
    boto3_raw_data: "type_defs.DescribeSharedDirectoriesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SharedDirectories(self):  # pragma: no cover
        return SharedDirectory.make_many(self.boto3_raw_data["SharedDirectories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSharedDirectoriesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSharedDirectoriesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddIpRoutesRequest:
    boto3_raw_data: "type_defs.AddIpRoutesRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def IpRoutes(self):  # pragma: no cover
        return IpRoute.make_many(self.boto3_raw_data["IpRoutes"])

    UpdateSecurityGroupForDirectoryControllers = field(
        "UpdateSecurityGroupForDirectoryControllers"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddIpRoutesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddIpRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceRequest:
    boto3_raw_data: "type_defs.AddTagsToResourceRequestTypeDef" = dataclasses.field()

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
class CreateHybridADRequest:
    boto3_raw_data: "type_defs.CreateHybridADRequestTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    AssessmentId = field("AssessmentId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHybridADRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHybridADRequestTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class AssessmentReport:
    boto3_raw_data: "type_defs.AssessmentReportTypeDef" = dataclasses.field()

    DomainControllerIp = field("DomainControllerIp")

    @cached_property
    def Validations(self):  # pragma: no cover
        return AssessmentValidation.make_many(self.boto3_raw_data["Validations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListADAssessmentsResult:
    boto3_raw_data: "type_defs.ListADAssessmentsResultTypeDef" = dataclasses.field()

    @cached_property
    def Assessments(self):  # pragma: no cover
        return AssessmentSummary.make_many(self.boto3_raw_data["Assessments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListADAssessmentsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListADAssessmentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Computer:
    boto3_raw_data: "type_defs.ComputerTypeDef" = dataclasses.field()

    ComputerId = field("ComputerId")
    ComputerName = field("ComputerName")

    @cached_property
    def ComputerAttributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["ComputerAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputerRequest:
    boto3_raw_data: "type_defs.CreateComputerRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    ComputerName = field("ComputerName")
    Password = field("Password")
    OrganizationalUnitDistinguishedName = field("OrganizationalUnitDistinguishedName")

    @cached_property
    def ComputerAttributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["ComputerAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComputerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesResult:
    boto3_raw_data: "type_defs.ListCertificatesResultTypeDef" = dataclasses.field()

    @cached_property
    def CertificatesInfo(self):  # pragma: no cover
        return CertificateInfo.make_many(self.boto3_raw_data["CertificatesInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesResultTypeDef"]
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

    CertificateId = field("CertificateId")
    State = field("State")
    StateReason = field("StateReason")
    CommonName = field("CommonName")
    RegisteredDateTime = field("RegisteredDateTime")
    ExpiryDateTime = field("ExpiryDateTime")
    Type = field("Type")

    @cached_property
    def ClientCertAuthSettings(self):  # pragma: no cover
        return ClientCertAuthSettings.make_one(
            self.boto3_raw_data["ClientCertAuthSettings"]
        )

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
class RegisterCertificateRequest:
    boto3_raw_data: "type_defs.RegisterCertificateRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    CertificateData = field("CertificateData")
    Type = field("Type")

    @cached_property
    def ClientCertAuthSettings(self):  # pragma: no cover
        return ClientCertAuthSettings.make_one(
            self.boto3_raw_data["ClientCertAuthSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClientAuthenticationSettingsResult:
    boto3_raw_data: "type_defs.DescribeClientAuthenticationSettingsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientAuthenticationSettingsInfo(self):  # pragma: no cover
        return ClientAuthenticationSettingInfo.make_many(
            self.boto3_raw_data["ClientAuthenticationSettingsInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClientAuthenticationSettingsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClientAuthenticationSettingsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConditionalForwardersResult:
    boto3_raw_data: "type_defs.DescribeConditionalForwardersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConditionalForwarders(self):  # pragma: no cover
        return ConditionalForwarder.make_many(
            self.boto3_raw_data["ConditionalForwarders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConditionalForwardersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConditionalForwardersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectDirectoryRequest:
    boto3_raw_data: "type_defs.ConnectDirectoryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Password = field("Password")
    Size = field("Size")

    @cached_property
    def ConnectSettings(self):  # pragma: no cover
        return DirectoryConnectSettings.make_one(self.boto3_raw_data["ConnectSettings"])

    ShortName = field("ShortName")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClientAuthenticationSettingsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeClientAuthenticationSettingsRequestPaginateTypeDef"
    ) = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClientAuthenticationSettingsRequestPaginateTypeDef"
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
                "type_defs.DescribeClientAuthenticationSettingsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDirectoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryIds = field("DirectoryIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectoriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainControllersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDomainControllersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    DomainControllerIds = field("DomainControllerIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainControllersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainControllersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLDAPSSettingsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeLDAPSSettingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLDAPSSettingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLDAPSSettingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRegionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    RegionName = field("RegionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRegionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSharedDirectoriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSharedDirectoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OwnerDirectoryId = field("OwnerDirectoryId")
    SharedDirectoryIds = field("SharedDirectoryIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSharedDirectoriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSharedDirectoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    SnapshotIds = field("SnapshotIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeTrustsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    TrustIds = field("TrustIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTrustsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateDirectoryRequestPaginate:
    boto3_raw_data: "type_defs.DescribeUpdateDirectoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    UpdateType = field("UpdateType")
    RegionName = field("RegionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUpdateDirectoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateDirectoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListADAssessmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListADAssessmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListADAssessmentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListADAssessmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIpRoutesRequestPaginate:
    boto3_raw_data: "type_defs.ListIpRoutesRequestPaginateTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIpRoutesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIpRoutesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLogSubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLogSubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemaExtensionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSchemaExtensionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSchemaExtensionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemaExtensionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainControllersResult:
    boto3_raw_data: "type_defs.DescribeDomainControllersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainControllers(self):  # pragma: no cover
        return DomainController.make_many(self.boto3_raw_data["DomainControllers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDomainControllersResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainControllersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTopicsResult:
    boto3_raw_data: "type_defs.DescribeEventTopicsResultTypeDef" = dataclasses.field()

    @cached_property
    def EventTopics(self):  # pragma: no cover
        return EventTopic.make_many(self.boto3_raw_data["EventTopics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventTopicsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTopicsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHybridADUpdateRequestWait:
    boto3_raw_data: "type_defs.DescribeHybridADUpdateRequestWaitTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    UpdateType = field("UpdateType")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHybridADUpdateRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHybridADUpdateRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLDAPSSettingsResult:
    boto3_raw_data: "type_defs.DescribeLDAPSSettingsResultTypeDef" = dataclasses.field()

    @cached_property
    def LDAPSSettingsInfo(self):  # pragma: no cover
        return LDAPSSettingInfo.make_many(self.boto3_raw_data["LDAPSSettingsInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLDAPSSettingsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLDAPSSettingsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSettingsResult:
    boto3_raw_data: "type_defs.DescribeSettingsResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def SettingEntries(self):  # pragma: no cover
        return SettingEntry.make_many(self.boto3_raw_data["SettingEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSettingsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSettingsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotsResult:
    boto3_raw_data: "type_defs.DescribeSnapshotsResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["Snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSnapshotsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustsResult:
    boto3_raw_data: "type_defs.DescribeTrustsResultTypeDef" = dataclasses.field()

    @cached_property
    def Trusts(self):  # pragma: no cover
        return Trust.make_many(self.boto3_raw_data["Trusts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrustsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerDirectoryDescription:
    boto3_raw_data: "type_defs.OwnerDirectoryDescriptionTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    AccountId = field("AccountId")
    DnsIpAddrs = field("DnsIpAddrs")

    @cached_property
    def VpcSettings(self):  # pragma: no cover
        return DirectoryVpcSettingsDescription.make_one(
            self.boto3_raw_data["VpcSettings"]
        )

    @cached_property
    def RadiusSettings(self):  # pragma: no cover
        return RadiusSettingsOutput.make_one(self.boto3_raw_data["RadiusSettings"])

    RadiusStatus = field("RadiusStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnerDirectoryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnerDirectoryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectoryLimitsResult:
    boto3_raw_data: "type_defs.GetDirectoryLimitsResultTypeDef" = dataclasses.field()

    @cached_property
    def DirectoryLimits(self):  # pragma: no cover
        return DirectoryLimits.make_one(self.boto3_raw_data["DirectoryLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDirectoryLimitsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectoryLimitsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionDescription:
    boto3_raw_data: "type_defs.RegionDescriptionTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    RegionName = field("RegionName")
    RegionType = field("RegionType")
    Status = field("Status")

    @cached_property
    def VpcSettings(self):  # pragma: no cover
        return DirectoryVpcSettingsOutput.make_one(self.boto3_raw_data["VpcSettings"])

    DesiredNumberOfDomainControllers = field("DesiredNumberOfDomainControllers")
    LaunchTime = field("LaunchTime")
    StatusLastUpdatedDateTime = field("StatusLastUpdatedDateTime")
    LastUpdatedDateTime = field("LastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotLimitsResult:
    boto3_raw_data: "type_defs.GetSnapshotLimitsResultTypeDef" = dataclasses.field()

    @cached_property
    def SnapshotLimits(self):  # pragma: no cover
        return SnapshotLimits.make_one(self.boto3_raw_data["SnapshotLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotLimitsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotLimitsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHybridADRequest:
    boto3_raw_data: "type_defs.UpdateHybridADRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def HybridAdministratorAccountUpdate(self):  # pragma: no cover
        return HybridAdministratorAccountUpdate.make_one(
            self.boto3_raw_data["HybridAdministratorAccountUpdate"]
        )

    @cached_property
    def SelfManagedInstancesSettings(self):  # pragma: no cover
        return HybridCustomerInstancesSettings.make_one(
            self.boto3_raw_data["SelfManagedInstancesSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHybridADRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHybridADRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridUpdateInfoEntry:
    boto3_raw_data: "type_defs.HybridUpdateInfoEntryTypeDef" = dataclasses.field()

    Status = field("Status")
    StatusReason = field("StatusReason")
    InitiatedBy = field("InitiatedBy")

    @cached_property
    def NewValue(self):  # pragma: no cover
        return HybridUpdateValue.make_one(self.boto3_raw_data["NewValue"])

    @cached_property
    def PreviousValue(self):  # pragma: no cover
        return HybridUpdateValue.make_one(self.boto3_raw_data["PreviousValue"])

    StartTime = field("StartTime")
    LastUpdatedDateTime = field("LastUpdatedDateTime")
    AssessmentId = field("AssessmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HybridUpdateInfoEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridUpdateInfoEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIpRoutesResult:
    boto3_raw_data: "type_defs.ListIpRoutesResultTypeDef" = dataclasses.field()

    @cached_property
    def IpRoutesInfo(self):  # pragma: no cover
        return IpRouteInfo.make_many(self.boto3_raw_data["IpRoutesInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIpRoutesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIpRoutesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogSubscriptionsResult:
    boto3_raw_data: "type_defs.ListLogSubscriptionsResultTypeDef" = dataclasses.field()

    @cached_property
    def LogSubscriptions(self):  # pragma: no cover
        return LogSubscription.make_many(self.boto3_raw_data["LogSubscriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogSubscriptionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogSubscriptionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemaExtensionsResult:
    boto3_raw_data: "type_defs.ListSchemaExtensionsResultTypeDef" = dataclasses.field()

    @cached_property
    def SchemaExtensionsInfo(self):  # pragma: no cover
        return SchemaExtensionInfo.make_many(
            self.boto3_raw_data["SchemaExtensionsInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemaExtensionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemaExtensionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectorySetupRequest:
    boto3_raw_data: "type_defs.UpdateDirectorySetupRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    UpdateType = field("UpdateType")

    @cached_property
    def OSUpdateSettings(self):  # pragma: no cover
        return OSUpdateSettings.make_one(self.boto3_raw_data["OSUpdateSettings"])

    CreateSnapshotBeforeUpdate = field("CreateSnapshotBeforeUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDirectorySetupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectorySetupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateValue:
    boto3_raw_data: "type_defs.UpdateValueTypeDef" = dataclasses.field()

    @cached_property
    def OSUpdateSettings(self):  # pragma: no cover
        return OSUpdateSettings.make_one(self.boto3_raw_data["OSUpdateSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSettingsRequest:
    boto3_raw_data: "type_defs.UpdateSettingsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def Settings(self):  # pragma: no cover
        return Setting.make_many(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareDirectoryRequest:
    boto3_raw_data: "type_defs.ShareDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def ShareTarget(self):  # pragma: no cover
        return ShareTarget.make_one(self.boto3_raw_data["ShareTarget"])

    ShareMethod = field("ShareMethod")
    ShareNotes = field("ShareNotes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ShareDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ShareDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnshareDirectoryRequest:
    boto3_raw_data: "type_defs.UnshareDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def UnshareTarget(self):  # pragma: no cover
        return UnshareTarget.make_one(self.boto3_raw_data["UnshareTarget"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnshareDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnshareDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeADAssessmentResult:
    boto3_raw_data: "type_defs.DescribeADAssessmentResultTypeDef" = dataclasses.field()

    @cached_property
    def Assessment(self):  # pragma: no cover
        return Assessment.make_one(self.boto3_raw_data["Assessment"])

    @cached_property
    def AssessmentReports(self):  # pragma: no cover
        return AssessmentReport.make_many(self.boto3_raw_data["AssessmentReports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeADAssessmentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeADAssessmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputerResult:
    boto3_raw_data: "type_defs.CreateComputerResultTypeDef" = dataclasses.field()

    @cached_property
    def Computer(self):  # pragma: no cover
        return Computer.make_one(self.boto3_raw_data["Computer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComputerResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateResult:
    boto3_raw_data: "type_defs.DescribeCertificateResultTypeDef" = dataclasses.field()

    @cached_property
    def Certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectoryDescription:
    boto3_raw_data: "type_defs.DirectoryDescriptionTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Name = field("Name")
    ShortName = field("ShortName")
    Size = field("Size")
    Edition = field("Edition")
    Alias = field("Alias")
    AccessUrl = field("AccessUrl")
    Description = field("Description")
    DnsIpAddrs = field("DnsIpAddrs")
    Stage = field("Stage")
    ShareStatus = field("ShareStatus")
    ShareMethod = field("ShareMethod")
    ShareNotes = field("ShareNotes")
    LaunchTime = field("LaunchTime")
    StageLastUpdatedDateTime = field("StageLastUpdatedDateTime")
    Type = field("Type")

    @cached_property
    def VpcSettings(self):  # pragma: no cover
        return DirectoryVpcSettingsDescription.make_one(
            self.boto3_raw_data["VpcSettings"]
        )

    @cached_property
    def ConnectSettings(self):  # pragma: no cover
        return DirectoryConnectSettingsDescription.make_one(
            self.boto3_raw_data["ConnectSettings"]
        )

    @cached_property
    def RadiusSettings(self):  # pragma: no cover
        return RadiusSettingsOutput.make_one(self.boto3_raw_data["RadiusSettings"])

    RadiusStatus = field("RadiusStatus")
    StageReason = field("StageReason")
    SsoEnabled = field("SsoEnabled")
    DesiredNumberOfDomainControllers = field("DesiredNumberOfDomainControllers")

    @cached_property
    def OwnerDirectoryDescription(self):  # pragma: no cover
        return OwnerDirectoryDescription.make_one(
            self.boto3_raw_data["OwnerDirectoryDescription"]
        )

    @cached_property
    def RegionsInfo(self):  # pragma: no cover
        return RegionsInfo.make_one(self.boto3_raw_data["RegionsInfo"])

    OsVersion = field("OsVersion")

    @cached_property
    def HybridSettings(self):  # pragma: no cover
        return HybridSettingsDescription.make_one(self.boto3_raw_data["HybridSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectoryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectoryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegionsResult:
    boto3_raw_data: "type_defs.DescribeRegionsResultTypeDef" = dataclasses.field()

    @cached_property
    def RegionsDescription(self):  # pragma: no cover
        return RegionDescription.make_many(self.boto3_raw_data["RegionsDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRegionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddRegionRequest:
    boto3_raw_data: "type_defs.AddRegionRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    RegionName = field("RegionName")
    VPCSettings = field("VPCSettings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddRegionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddRegionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentConfiguration:
    boto3_raw_data: "type_defs.AssessmentConfigurationTypeDef" = dataclasses.field()

    CustomerDnsIps = field("CustomerDnsIps")
    DnsName = field("DnsName")
    VpcSettings = field("VpcSettings")
    InstanceIds = field("InstanceIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryRequest:
    boto3_raw_data: "type_defs.CreateDirectoryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Password = field("Password")
    Size = field("Size")
    ShortName = field("ShortName")
    Description = field("Description")
    VpcSettings = field("VpcSettings")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMicrosoftADRequest:
    boto3_raw_data: "type_defs.CreateMicrosoftADRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Password = field("Password")
    VpcSettings = field("VpcSettings")
    ShortName = field("ShortName")
    Description = field("Description")
    Edition = field("Edition")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMicrosoftADRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMicrosoftADRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HybridUpdateActivities:
    boto3_raw_data: "type_defs.HybridUpdateActivitiesTypeDef" = dataclasses.field()

    @cached_property
    def SelfManagedInstances(self):  # pragma: no cover
        return HybridUpdateInfoEntry.make_many(
            self.boto3_raw_data["SelfManagedInstances"]
        )

    @cached_property
    def HybridAdministratorAccount(self):  # pragma: no cover
        return HybridUpdateInfoEntry.make_many(
            self.boto3_raw_data["HybridAdministratorAccount"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HybridUpdateActivitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HybridUpdateActivitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInfoEntry:
    boto3_raw_data: "type_defs.UpdateInfoEntryTypeDef" = dataclasses.field()

    Region = field("Region")
    Status = field("Status")
    StatusReason = field("StatusReason")
    InitiatedBy = field("InitiatedBy")

    @cached_property
    def NewValue(self):  # pragma: no cover
        return UpdateValue.make_one(self.boto3_raw_data["NewValue"])

    @cached_property
    def PreviousValue(self):  # pragma: no cover
        return UpdateValue.make_one(self.boto3_raw_data["PreviousValue"])

    StartTime = field("StartTime")
    LastUpdatedDateTime = field("LastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateInfoEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateInfoEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableRadiusRequest:
    boto3_raw_data: "type_defs.EnableRadiusRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    RadiusSettings = field("RadiusSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableRadiusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableRadiusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRadiusRequest:
    boto3_raw_data: "type_defs.UpdateRadiusRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    RadiusSettings = field("RadiusSettings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRadiusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRadiusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectoriesResult:
    boto3_raw_data: "type_defs.DescribeDirectoriesResultTypeDef" = dataclasses.field()

    @cached_property
    def DirectoryDescriptions(self):  # pragma: no cover
        return DirectoryDescription.make_many(
            self.boto3_raw_data["DirectoryDescriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDirectoriesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectoriesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartADAssessmentRequest:
    boto3_raw_data: "type_defs.StartADAssessmentRequestTypeDef" = dataclasses.field()

    @cached_property
    def AssessmentConfiguration(self):  # pragma: no cover
        return AssessmentConfiguration.make_one(
            self.boto3_raw_data["AssessmentConfiguration"]
        )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartADAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartADAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHybridADUpdateResult:
    boto3_raw_data: "type_defs.DescribeHybridADUpdateResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UpdateActivities(self):  # pragma: no cover
        return HybridUpdateActivities.make_one(self.boto3_raw_data["UpdateActivities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeHybridADUpdateResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHybridADUpdateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateDirectoryResult:
    boto3_raw_data: "type_defs.DescribeUpdateDirectoryResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UpdateActivities(self):  # pragma: no cover
        return UpdateInfoEntry.make_many(self.boto3_raw_data["UpdateActivities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeUpdateDirectoryResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
