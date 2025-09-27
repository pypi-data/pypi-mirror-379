# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptReservedNodeExchangeInputMessage:
    boto3_raw_data: "type_defs.AcceptReservedNodeExchangeInputMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeId = field("ReservedNodeId")
    TargetReservedNodeOfferingId = field("TargetReservedNodeOfferingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptReservedNodeExchangeInputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptReservedNodeExchangeInputMessageTypeDef"]
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
class AttributeValueTarget:
    boto3_raw_data: "type_defs.AttributeValueTargetTypeDef" = dataclasses.field()

    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountWithRestoreAccess:
    boto3_raw_data: "type_defs.AccountWithRestoreAccessTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    AccountAlias = field("AccountAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountWithRestoreAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountWithRestoreAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AquaConfiguration:
    boto3_raw_data: "type_defs.AquaConfigurationTypeDef" = dataclasses.field()

    AquaStatus = field("AquaStatus")
    AquaConfigurationStatus = field("AquaConfigurationStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AquaConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AquaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDataShareConsumerMessage:
    boto3_raw_data: "type_defs.AssociateDataShareConsumerMessageTypeDef" = (
        dataclasses.field()
    )

    DataShareArn = field("DataShareArn")
    AssociateEntireAccount = field("AssociateEntireAccount")
    ConsumerArn = field("ConsumerArn")
    ConsumerRegion = field("ConsumerRegion")
    AllowWrites = field("AllowWrites")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDataShareConsumerMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDataShareConsumerMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateAssociation:
    boto3_raw_data: "type_defs.CertificateAssociationTypeDef" = dataclasses.field()

    CustomDomainName = field("CustomDomainName")
    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateAssociationTypeDef"]
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

    AuthenticationProfileName = field("AuthenticationProfileName")
    AuthenticationProfileContent = field("AuthenticationProfileContent")

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
class AuthorizeClusterSecurityGroupIngressMessage:
    boto3_raw_data: "type_defs.AuthorizeClusterSecurityGroupIngressMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    CIDRIP = field("CIDRIP")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeClusterSecurityGroupIngressMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeClusterSecurityGroupIngressMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeDataShareMessage:
    boto3_raw_data: "type_defs.AuthorizeDataShareMessageTypeDef" = dataclasses.field()

    DataShareArn = field("DataShareArn")
    ConsumerIdentifier = field("ConsumerIdentifier")
    AllowWrites = field("AllowWrites")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizeDataShareMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeDataShareMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeEndpointAccessMessage:
    boto3_raw_data: "type_defs.AuthorizeEndpointAccessMessageTypeDef" = (
        dataclasses.field()
    )

    Account = field("Account")
    ClusterIdentifier = field("ClusterIdentifier")
    VpcIds = field("VpcIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthorizeEndpointAccessMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeEndpointAccessMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeSnapshotAccessMessage:
    boto3_raw_data: "type_defs.AuthorizeSnapshotAccessMessageTypeDef" = (
        dataclasses.field()
    )

    AccountWithRestoreAccess = field("AccountWithRestoreAccess")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    SnapshotClusterIdentifier = field("SnapshotClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthorizeSnapshotAccessMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeSnapshotAccessMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizedTokenIssuerOutput:
    boto3_raw_data: "type_defs.AuthorizedTokenIssuerOutputTypeDef" = dataclasses.field()

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    AuthorizedAudiencesList = field("AuthorizedAudiencesList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizedTokenIssuerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizedTokenIssuerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizedTokenIssuer:
    boto3_raw_data: "type_defs.AuthorizedTokenIssuerTypeDef" = dataclasses.field()

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    AuthorizedAudiencesList = field("AuthorizedAudiencesList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizedTokenIssuerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizedTokenIssuerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedPlatform:
    boto3_raw_data: "type_defs.SupportedPlatformTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SupportedPlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedPlatformTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterSnapshotMessage:
    boto3_raw_data: "type_defs.DeleteClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotClusterIdentifier = field("SnapshotClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotErrorMessage:
    boto3_raw_data: "type_defs.SnapshotErrorMessageTypeDef" = dataclasses.field()

    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotClusterIdentifier = field("SnapshotClusterIdentifier")
    FailureCode = field("FailureCode")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapshotErrorMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotErrorMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchModifyClusterSnapshotsMessage:
    boto3_raw_data: "type_defs.BatchModifyClusterSnapshotsMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotIdentifierList = field("SnapshotIdentifierList")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    Force = field("Force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchModifyClusterSnapshotsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchModifyClusterSnapshotsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelResizeMessage:
    boto3_raw_data: "type_defs.CancelResizeMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelResizeMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelResizeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterAssociatedToSchedule:
    boto3_raw_data: "type_defs.ClusterAssociatedToScheduleTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    ScheduleAssociationState = field("ScheduleAssociationState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterAssociatedToScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterAssociatedToScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevisionTarget:
    boto3_raw_data: "type_defs.RevisionTargetTypeDef" = dataclasses.field()

    DatabaseRevision = field("DatabaseRevision")
    Description = field("Description")
    DatabaseRevisionReleaseDate = field("DatabaseRevisionReleaseDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RevisionTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterIamRole:
    boto3_raw_data: "type_defs.ClusterIamRoleTypeDef" = dataclasses.field()

    IamRoleArn = field("IamRoleArn")
    ApplyStatus = field("ApplyStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterIamRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterIamRoleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterNode:
    boto3_raw_data: "type_defs.ClusterNodeTypeDef" = dataclasses.field()

    NodeRole = field("NodeRole")
    PrivateIPAddress = field("PrivateIPAddress")
    PublicIPAddress = field("PublicIPAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterNodeTypeDef"]]
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
    ApplyType = field("ApplyType")
    IsModifiable = field("IsModifiable")
    MinimumEngineVersion = field("MinimumEngineVersion")

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
class ClusterParameterStatus:
    boto3_raw_data: "type_defs.ClusterParameterStatusTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterApplyStatus = field("ParameterApplyStatus")
    ParameterApplyErrorDescription = field("ParameterApplyErrorDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterParameterStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterParameterStatusTypeDef"]
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
class ClusterSecurityGroupMembership:
    boto3_raw_data: "type_defs.ClusterSecurityGroupMembershipTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterSecurityGroupMembershipTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSnapshotCopyStatus:
    boto3_raw_data: "type_defs.ClusterSnapshotCopyStatusTypeDef" = dataclasses.field()

    DestinationRegion = field("DestinationRegion")
    RetentionPeriod = field("RetentionPeriod")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    SnapshotCopyGrantName = field("SnapshotCopyGrantName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterSnapshotCopyStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSnapshotCopyStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataTransferProgress:
    boto3_raw_data: "type_defs.DataTransferProgressTypeDef" = dataclasses.field()

    Status = field("Status")
    CurrentRateInMegaBytesPerSecond = field("CurrentRateInMegaBytesPerSecond")
    TotalDataInMegaBytes = field("TotalDataInMegaBytes")
    DataTransferredInMegaBytes = field("DataTransferredInMegaBytes")
    EstimatedTimeToCompletionInSeconds = field("EstimatedTimeToCompletionInSeconds")
    ElapsedTimeInSeconds = field("ElapsedTimeInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataTransferProgressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataTransferProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeferredMaintenanceWindow:
    boto3_raw_data: "type_defs.DeferredMaintenanceWindowTypeDef" = dataclasses.field()

    DeferMaintenanceIdentifier = field("DeferMaintenanceIdentifier")
    DeferMaintenanceStartTime = field("DeferMaintenanceStartTime")
    DeferMaintenanceEndTime = field("DeferMaintenanceEndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeferredMaintenanceWindowTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeferredMaintenanceWindowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticIpStatus:
    boto3_raw_data: "type_defs.ElasticIpStatusTypeDef" = dataclasses.field()

    ElasticIp = field("ElasticIp")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ElasticIpStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ElasticIpStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HsmStatus:
    boto3_raw_data: "type_defs.HsmStatusTypeDef" = dataclasses.field()

    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HsmStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HsmStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingModifiedValues:
    boto3_raw_data: "type_defs.PendingModifiedValuesTypeDef" = dataclasses.field()

    MasterUserPassword = field("MasterUserPassword")
    NodeType = field("NodeType")
    NumberOfNodes = field("NumberOfNodes")
    ClusterType = field("ClusterType")
    ClusterVersion = field("ClusterVersion")
    AutomatedSnapshotRetentionPeriod = field("AutomatedSnapshotRetentionPeriod")
    ClusterIdentifier = field("ClusterIdentifier")
    PubliclyAccessible = field("PubliclyAccessible")
    EnhancedVpcRouting = field("EnhancedVpcRouting")
    MaintenanceTrackName = field("MaintenanceTrackName")
    EncryptionType = field("EncryptionType")

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
class ReservedNodeExchangeStatus:
    boto3_raw_data: "type_defs.ReservedNodeExchangeStatusTypeDef" = dataclasses.field()

    ReservedNodeExchangeRequestId = field("ReservedNodeExchangeRequestId")
    Status = field("Status")
    RequestTime = field("RequestTime")
    SourceReservedNodeId = field("SourceReservedNodeId")
    SourceReservedNodeType = field("SourceReservedNodeType")
    SourceReservedNodeCount = field("SourceReservedNodeCount")
    TargetReservedNodeOfferingId = field("TargetReservedNodeOfferingId")
    TargetReservedNodeType = field("TargetReservedNodeType")
    TargetReservedNodeCount = field("TargetReservedNodeCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedNodeExchangeStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedNodeExchangeStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResizeInfo:
    boto3_raw_data: "type_defs.ResizeInfoTypeDef" = dataclasses.field()

    ResizeType = field("ResizeType")
    AllowCancelResize = field("AllowCancelResize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResizeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResizeInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreStatus:
    boto3_raw_data: "type_defs.RestoreStatusTypeDef" = dataclasses.field()

    Status = field("Status")
    CurrentRestoreRateInMegaBytesPerSecond = field(
        "CurrentRestoreRateInMegaBytesPerSecond"
    )
    SnapshotSizeInMegaBytes = field("SnapshotSizeInMegaBytes")
    ProgressInMegaBytes = field("ProgressInMegaBytes")
    ElapsedTimeInSeconds = field("ElapsedTimeInSeconds")
    EstimatedTimeToCompletionInSeconds = field("EstimatedTimeToCompletionInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestoreStatusTypeDef"]],
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
class ClusterVersion:
    boto3_raw_data: "type_defs.ClusterVersionTypeDef" = dataclasses.field()

    ClusterVersion = field("ClusterVersion")
    ClusterParameterGroupFamily = field("ClusterParameterGroupFamily")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyClusterSnapshotMessage:
    boto3_raw_data: "type_defs.CopyClusterSnapshotMessageTypeDef" = dataclasses.field()

    SourceSnapshotIdentifier = field("SourceSnapshotIdentifier")
    TargetSnapshotIdentifier = field("TargetSnapshotIdentifier")
    SourceSnapshotClusterIdentifier = field("SourceSnapshotClusterIdentifier")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthenticationProfileMessage:
    boto3_raw_data: "type_defs.CreateAuthenticationProfileMessageTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")
    AuthenticationProfileContent = field("AuthenticationProfileContent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAuthenticationProfileMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthenticationProfileMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomDomainAssociationMessage:
    boto3_raw_data: "type_defs.CreateCustomDomainAssociationMessageTypeDef" = (
        dataclasses.field()
    )

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDomainAssociationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDomainAssociationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointAccessMessage:
    boto3_raw_data: "type_defs.CreateEndpointAccessMessageTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")
    SubnetGroupName = field("SubnetGroupName")
    ClusterIdentifier = field("ClusterIdentifier")
    ResourceOwner = field("ResourceOwner")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointAccessMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointAccessMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataShareAssociation:
    boto3_raw_data: "type_defs.DataShareAssociationTypeDef" = dataclasses.field()

    ConsumerIdentifier = field("ConsumerIdentifier")
    Status = field("Status")
    ConsumerRegion = field("ConsumerRegion")
    CreatedDate = field("CreatedDate")
    StatusChangeDate = field("StatusChangeDate")
    ProducerAllowedWrites = field("ProducerAllowedWrites")
    ConsumerAcceptedWrites = field("ConsumerAcceptedWrites")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataShareAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataShareAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeauthorizeDataShareMessage:
    boto3_raw_data: "type_defs.DeauthorizeDataShareMessageTypeDef" = dataclasses.field()

    DataShareArn = field("DataShareArn")
    ConsumerIdentifier = field("ConsumerIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeauthorizeDataShareMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeauthorizeDataShareMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuthenticationProfileMessage:
    boto3_raw_data: "type_defs.DeleteAuthenticationProfileMessageTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAuthenticationProfileMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuthenticationProfileMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterMessage:
    boto3_raw_data: "type_defs.DeleteClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    SkipFinalClusterSnapshot = field("SkipFinalClusterSnapshot")
    FinalClusterSnapshotIdentifier = field("FinalClusterSnapshotIdentifier")
    FinalClusterSnapshotRetentionPeriod = field("FinalClusterSnapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.DeleteClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterSecurityGroupMessage:
    boto3_raw_data: "type_defs.DeleteClusterSecurityGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteClusterSecurityGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterSnapshotMessageRequest:
    boto3_raw_data: "type_defs.DeleteClusterSnapshotMessageRequestTypeDef" = (
        dataclasses.field()
    )

    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotClusterIdentifier = field("SnapshotClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteClusterSnapshotMessageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterSnapshotMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterSubnetGroupMessage:
    boto3_raw_data: "type_defs.DeleteClusterSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteClusterSubnetGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomDomainAssociationMessage:
    boto3_raw_data: "type_defs.DeleteCustomDomainAssociationMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    CustomDomainName = field("CustomDomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomDomainAssociationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomDomainAssociationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointAccessMessage:
    boto3_raw_data: "type_defs.DeleteEndpointAccessMessageTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointAccessMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointAccessMessageTypeDef"]
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
class DeleteHsmClientCertificateMessage:
    boto3_raw_data: "type_defs.DeleteHsmClientCertificateMessageTypeDef" = (
        dataclasses.field()
    )

    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteHsmClientCertificateMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHsmClientCertificateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHsmConfigurationMessage:
    boto3_raw_data: "type_defs.DeleteHsmConfigurationMessageTypeDef" = (
        dataclasses.field()
    )

    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteHsmConfigurationMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHsmConfigurationMessageTypeDef"]
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

    IntegrationArn = field("IntegrationArn")

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
class DeleteRedshiftIdcApplicationMessage:
    boto3_raw_data: "type_defs.DeleteRedshiftIdcApplicationMessageTypeDef" = (
        dataclasses.field()
    )

    RedshiftIdcApplicationArn = field("RedshiftIdcApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRedshiftIdcApplicationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRedshiftIdcApplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyMessage:
    boto3_raw_data: "type_defs.DeleteResourcePolicyMessageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduledActionMessage:
    boto3_raw_data: "type_defs.DeleteScheduledActionMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduledActionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotCopyGrantMessage:
    boto3_raw_data: "type_defs.DeleteSnapshotCopyGrantMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotCopyGrantName = field("SnapshotCopyGrantName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSnapshotCopyGrantMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotCopyGrantMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotScheduleMessage:
    boto3_raw_data: "type_defs.DeleteSnapshotScheduleMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduleIdentifier = field("ScheduleIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSnapshotScheduleMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotScheduleMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsMessage:
    boto3_raw_data: "type_defs.DeleteTagsMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUsageLimitMessage:
    boto3_raw_data: "type_defs.DeleteUsageLimitMessageTypeDef" = dataclasses.field()

    UsageLimitId = field("UsageLimitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUsageLimitMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUsageLimitMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAttributesMessage:
    boto3_raw_data: "type_defs.DescribeAccountAttributesMessageTypeDef" = (
        dataclasses.field()
    )

    AttributeNames = field("AttributeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountAttributesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAttributesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuthenticationProfilesMessage:
    boto3_raw_data: "type_defs.DescribeAuthenticationProfilesMessageTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAuthenticationProfilesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuthenticationProfilesMessageTypeDef"]
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
class DescribeClusterDbRevisionsMessage:
    boto3_raw_data: "type_defs.DescribeClusterDbRevisionsMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterDbRevisionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterDbRevisionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterParameterGroupsMessage:
    boto3_raw_data: "type_defs.DescribeClusterParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterParameterGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterParametersMessage:
    boto3_raw_data: "type_defs.DescribeClusterParametersMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    Source = field("Source")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterParametersMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSecurityGroupsMessage:
    boto3_raw_data: "type_defs.DescribeClusterSecurityGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterSecurityGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSecurityGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotSortingEntity:
    boto3_raw_data: "type_defs.SnapshotSortingEntityTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapshotSortingEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotSortingEntityTypeDef"]
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
class DescribeClusterSubnetGroupsMessage:
    boto3_raw_data: "type_defs.DescribeClusterSubnetGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterSubnetGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSubnetGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterTracksMessage:
    boto3_raw_data: "type_defs.DescribeClusterTracksMessageTypeDef" = (
        dataclasses.field()
    )

    MaintenanceTrackName = field("MaintenanceTrackName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterTracksMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterTracksMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterVersionsMessage:
    boto3_raw_data: "type_defs.DescribeClusterVersionsMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterVersion = field("ClusterVersion")
    ClusterParameterGroupFamily = field("ClusterParameterGroupFamily")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterVersionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterVersionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersMessage:
    boto3_raw_data: "type_defs.DescribeClustersMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClustersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomDomainAssociationsMessage:
    boto3_raw_data: "type_defs.DescribeCustomDomainAssociationsMessageTypeDef" = (
        dataclasses.field()
    )

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomDomainAssociationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomDomainAssociationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesForConsumerMessage:
    boto3_raw_data: "type_defs.DescribeDataSharesForConsumerMessageTypeDef" = (
        dataclasses.field()
    )

    ConsumerArn = field("ConsumerArn")
    Status = field("Status")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesForConsumerMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesForConsumerMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesForProducerMessage:
    boto3_raw_data: "type_defs.DescribeDataSharesForProducerMessageTypeDef" = (
        dataclasses.field()
    )

    ProducerArn = field("ProducerArn")
    Status = field("Status")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesForProducerMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesForProducerMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesMessage:
    boto3_raw_data: "type_defs.DescribeDataSharesMessageTypeDef" = dataclasses.field()

    DataShareArn = field("DataShareArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSharesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDefaultClusterParametersMessage:
    boto3_raw_data: "type_defs.DescribeDefaultClusterParametersMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupFamily = field("ParameterGroupFamily")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDefaultClusterParametersMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDefaultClusterParametersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointAccessMessage:
    boto3_raw_data: "type_defs.DescribeEndpointAccessMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    ResourceOwner = field("ResourceOwner")
    EndpointName = field("EndpointName")
    VpcId = field("VpcId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointAccessMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointAccessMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointAuthorizationMessage:
    boto3_raw_data: "type_defs.DescribeEndpointAuthorizationMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    Account = field("Account")
    Grantee = field("Grantee")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEndpointAuthorizationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointAuthorizationMessageTypeDef"]
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
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

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
class DescribeHsmClientCertificatesMessage:
    boto3_raw_data: "type_defs.DescribeHsmClientCertificatesMessageTypeDef" = (
        dataclasses.field()
    )

    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHsmClientCertificatesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHsmClientCertificatesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHsmConfigurationsMessage:
    boto3_raw_data: "type_defs.DescribeHsmConfigurationsMessageTypeDef" = (
        dataclasses.field()
    )

    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeHsmConfigurationsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHsmConfigurationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundIntegrationsMessage:
    boto3_raw_data: "type_defs.DescribeInboundIntegrationsMessageTypeDef" = (
        dataclasses.field()
    )

    IntegrationArn = field("IntegrationArn")
    TargetArn = field("TargetArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundIntegrationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInboundIntegrationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIntegrationsFilter:
    boto3_raw_data: "type_defs.DescribeIntegrationsFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIntegrationsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIntegrationsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoggingStatusMessage:
    boto3_raw_data: "type_defs.DescribeLoggingStatusMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLoggingStatusMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoggingStatusMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeConfigurationOptionsFilter:
    boto3_raw_data: "type_defs.NodeConfigurationOptionsFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NodeConfigurationOptionsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeConfigurationOptionsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableClusterOptionsMessage:
    boto3_raw_data: "type_defs.DescribeOrderableClusterOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterVersion = field("ClusterVersion")
    NodeType = field("NodeType")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableClusterOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrderableClusterOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePartnersInputMessage:
    boto3_raw_data: "type_defs.DescribePartnersInputMessageTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClusterIdentifier = field("ClusterIdentifier")
    DatabaseName = field("DatabaseName")
    PartnerName = field("PartnerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePartnersInputMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePartnersInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerIntegrationInfo:
    boto3_raw_data: "type_defs.PartnerIntegrationInfoTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    PartnerName = field("PartnerName")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartnerIntegrationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerIntegrationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRedshiftIdcApplicationsMessage:
    boto3_raw_data: "type_defs.DescribeRedshiftIdcApplicationsMessageTypeDef" = (
        dataclasses.field()
    )

    RedshiftIdcApplicationArn = field("RedshiftIdcApplicationArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRedshiftIdcApplicationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRedshiftIdcApplicationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodeExchangeStatusInputMessage:
    boto3_raw_data: (
        "type_defs.DescribeReservedNodeExchangeStatusInputMessageTypeDef"
    ) = dataclasses.field()

    ReservedNodeId = field("ReservedNodeId")
    ReservedNodeExchangeRequestId = field("ReservedNodeExchangeRequestId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodeExchangeStatusInputMessageTypeDef"
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
                "type_defs.DescribeReservedNodeExchangeStatusInputMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodeOfferingsMessage:
    boto3_raw_data: "type_defs.DescribeReservedNodeOfferingsMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeOfferingId = field("ReservedNodeOfferingId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodeOfferingsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodeOfferingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesMessage:
    boto3_raw_data: "type_defs.DescribeReservedNodesMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeId = field("ReservedNodeId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReservedNodesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResizeMessage:
    boto3_raw_data: "type_defs.DescribeResizeMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResizeMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResizeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledActionFilter:
    boto3_raw_data: "type_defs.ScheduledActionFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledActionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotCopyGrantsMessage:
    boto3_raw_data: "type_defs.DescribeSnapshotCopyGrantsMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotCopyGrantName = field("SnapshotCopyGrantName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSnapshotCopyGrantsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotCopyGrantsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotSchedulesMessage:
    boto3_raw_data: "type_defs.DescribeSnapshotSchedulesMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    ScheduleIdentifier = field("ScheduleIdentifier")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")
    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSnapshotSchedulesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotSchedulesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableRestoreStatusMessage:
    boto3_raw_data: "type_defs.DescribeTableRestoreStatusMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    TableRestoreRequestId = field("TableRestoreRequestId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTableRestoreStatusMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableRestoreStatusMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsMessage:
    boto3_raw_data: "type_defs.DescribeTagsMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    ResourceType = field("ResourceType")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsageLimitsMessage:
    boto3_raw_data: "type_defs.DescribeUsageLimitsMessageTypeDef" = dataclasses.field()

    UsageLimitId = field("UsageLimitId")
    ClusterIdentifier = field("ClusterIdentifier")
    FeatureType = field("FeatureType")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUsageLimitsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsageLimitsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableLoggingMessage:
    boto3_raw_data: "type_defs.DisableLoggingMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableLoggingMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableLoggingMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableSnapshotCopyMessage:
    boto3_raw_data: "type_defs.DisableSnapshotCopyMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableSnapshotCopyMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableSnapshotCopyMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDataShareConsumerMessage:
    boto3_raw_data: "type_defs.DisassociateDataShareConsumerMessageTypeDef" = (
        dataclasses.field()
    )

    DataShareArn = field("DataShareArn")
    DisassociateEntireAccount = field("DisassociateEntireAccount")
    ConsumerArn = field("ConsumerArn")
    ConsumerRegion = field("ConsumerRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDataShareConsumerMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDataShareConsumerMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableLoggingMessage:
    boto3_raw_data: "type_defs.EnableLoggingMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    BucketName = field("BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    LogDestinationType = field("LogDestinationType")
    LogExports = field("LogExports")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableLoggingMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableLoggingMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableSnapshotCopyMessage:
    boto3_raw_data: "type_defs.EnableSnapshotCopyMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    DestinationRegion = field("DestinationRegion")
    RetentionPeriod = field("RetentionPeriod")
    SnapshotCopyGrantName = field("SnapshotCopyGrantName")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableSnapshotCopyMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableSnapshotCopyMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointAuthorization:
    boto3_raw_data: "type_defs.EndpointAuthorizationTypeDef" = dataclasses.field()

    Grantor = field("Grantor")
    Grantee = field("Grantee")
    ClusterIdentifier = field("ClusterIdentifier")
    AuthorizeTime = field("AuthorizeTime")
    ClusterStatus = field("ClusterStatus")
    Status = field("Status")
    AllowedAllVPCs = field("AllowedAllVPCs")
    AllowedVPCs = field("AllowedVPCs")
    EndpointCount = field("EndpointCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointAuthorizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointAuthorizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventInfoMap:
    boto3_raw_data: "type_defs.EventInfoMapTypeDef" = dataclasses.field()

    EventId = field("EventId")
    EventCategories = field("EventCategories")
    EventDescription = field("EventDescription")
    Severity = field("Severity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventInfoMapTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventInfoMapTypeDef"]],
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
    Severity = field("Severity")
    Date = field("Date")
    EventId = field("EventId")

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
class FailoverPrimaryComputeInputMessage:
    boto3_raw_data: "type_defs.FailoverPrimaryComputeInputMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailoverPrimaryComputeInputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverPrimaryComputeInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterCredentialsMessage:
    boto3_raw_data: "type_defs.GetClusterCredentialsMessageTypeDef" = (
        dataclasses.field()
    )

    DbUser = field("DbUser")
    DbName = field("DbName")
    ClusterIdentifier = field("ClusterIdentifier")
    DurationSeconds = field("DurationSeconds")
    AutoCreate = field("AutoCreate")
    DbGroups = field("DbGroups")
    CustomDomainName = field("CustomDomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClusterCredentialsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterCredentialsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterCredentialsWithIAMMessage:
    boto3_raw_data: "type_defs.GetClusterCredentialsWithIAMMessageTypeDef" = (
        dataclasses.field()
    )

    DbName = field("DbName")
    ClusterIdentifier = field("ClusterIdentifier")
    DurationSeconds = field("DurationSeconds")
    CustomDomainName = field("CustomDomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetClusterCredentialsWithIAMMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterCredentialsWithIAMMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservedNodeExchangeConfigurationOptionsInputMessage:
    boto3_raw_data: (
        "type_defs.GetReservedNodeExchangeConfigurationOptionsInputMessageTypeDef"
    ) = dataclasses.field()

    ActionType = field("ActionType")
    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservedNodeExchangeConfigurationOptionsInputMessageTypeDef"
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
                "type_defs.GetReservedNodeExchangeConfigurationOptionsInputMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservedNodeExchangeOfferingsInputMessage:
    boto3_raw_data: "type_defs.GetReservedNodeExchangeOfferingsInputMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeId = field("ReservedNodeId")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservedNodeExchangeOfferingsInputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservedNodeExchangeOfferingsInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyMessage:
    boto3_raw_data: "type_defs.GetResourcePolicyMessageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePolicy:
    boto3_raw_data: "type_defs.ResourcePolicyTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcePolicyTypeDef"]],
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
class LakeFormationQuery:
    boto3_raw_data: "type_defs.LakeFormationQueryTypeDef" = dataclasses.field()

    Authorization = field("Authorization")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LakeFormationQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsMessage:
    boto3_raw_data: "type_defs.ListRecommendationsMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    NamespaceArn = field("NamespaceArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyAquaInputMessage:
    boto3_raw_data: "type_defs.ModifyAquaInputMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    AquaConfigurationStatus = field("AquaConfigurationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyAquaInputMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyAquaInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyAuthenticationProfileMessage:
    boto3_raw_data: "type_defs.ModifyAuthenticationProfileMessageTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")
    AuthenticationProfileContent = field("AuthenticationProfileContent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyAuthenticationProfileMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyAuthenticationProfileMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterDbRevisionMessage:
    boto3_raw_data: "type_defs.ModifyClusterDbRevisionMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    RevisionTarget = field("RevisionTarget")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClusterDbRevisionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterDbRevisionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterIamRolesMessage:
    boto3_raw_data: "type_defs.ModifyClusterIamRolesMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    AddIamRoles = field("AddIamRoles")
    RemoveIamRoles = field("RemoveIamRoles")
    DefaultIamRoleArn = field("DefaultIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterIamRolesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterIamRolesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterMessage:
    boto3_raw_data: "type_defs.ModifyClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    ClusterType = field("ClusterType")
    NodeType = field("NodeType")
    NumberOfNodes = field("NumberOfNodes")
    ClusterSecurityGroups = field("ClusterSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    MasterUserPassword = field("MasterUserPassword")
    ClusterParameterGroupName = field("ClusterParameterGroupName")
    AutomatedSnapshotRetentionPeriod = field("AutomatedSnapshotRetentionPeriod")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ClusterVersion = field("ClusterVersion")
    AllowVersionUpgrade = field("AllowVersionUpgrade")
    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    NewClusterIdentifier = field("NewClusterIdentifier")
    PubliclyAccessible = field("PubliclyAccessible")
    ElasticIp = field("ElasticIp")
    EnhancedVpcRouting = field("EnhancedVpcRouting")
    MaintenanceTrackName = field("MaintenanceTrackName")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    AvailabilityZoneRelocation = field("AvailabilityZoneRelocation")
    AvailabilityZone = field("AvailabilityZone")
    Port = field("Port")
    ManageMasterPassword = field("ManageMasterPassword")
    MasterPasswordSecretKmsKeyId = field("MasterPasswordSecretKmsKeyId")
    IpAddressType = field("IpAddressType")
    MultiAZ = field("MultiAZ")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterSnapshotMessage:
    boto3_raw_data: "type_defs.ModifyClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotIdentifier = field("SnapshotIdentifier")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterSnapshotScheduleMessage:
    boto3_raw_data: "type_defs.ModifyClusterSnapshotScheduleMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    ScheduleIdentifier = field("ScheduleIdentifier")
    DisassociateSchedule = field("DisassociateSchedule")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyClusterSnapshotScheduleMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterSnapshotScheduleMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterSubnetGroupMessage:
    boto3_raw_data: "type_defs.ModifyClusterSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    SubnetIds = field("SubnetIds")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClusterSubnetGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCustomDomainAssociationMessage:
    boto3_raw_data: "type_defs.ModifyCustomDomainAssociationMessageTypeDef" = (
        dataclasses.field()
    )

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyCustomDomainAssociationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCustomDomainAssociationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEndpointAccessMessage:
    boto3_raw_data: "type_defs.ModifyEndpointAccessMessageTypeDef" = dataclasses.field()

    EndpointName = field("EndpointName")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyEndpointAccessMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEndpointAccessMessageTypeDef"]
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
    SourceIds = field("SourceIds")
    EventCategories = field("EventCategories")
    Severity = field("Severity")
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
class ModifyIntegrationMessage:
    boto3_raw_data: "type_defs.ModifyIntegrationMessageTypeDef" = dataclasses.field()

    IntegrationArn = field("IntegrationArn")
    Description = field("Description")
    IntegrationName = field("IntegrationName")

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
class ModifySnapshotCopyRetentionPeriodMessage:
    boto3_raw_data: "type_defs.ModifySnapshotCopyRetentionPeriodMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    RetentionPeriod = field("RetentionPeriod")
    Manual = field("Manual")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifySnapshotCopyRetentionPeriodMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifySnapshotCopyRetentionPeriodMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifySnapshotScheduleMessage:
    boto3_raw_data: "type_defs.ModifySnapshotScheduleMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduleIdentifier = field("ScheduleIdentifier")
    ScheduleDefinitions = field("ScheduleDefinitions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifySnapshotScheduleMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifySnapshotScheduleMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyUsageLimitMessage:
    boto3_raw_data: "type_defs.ModifyUsageLimitMessageTypeDef" = dataclasses.field()

    UsageLimitId = field("UsageLimitId")
    Amount = field("Amount")
    BreachAction = field("BreachAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyUsageLimitMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyUsageLimitMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedIdentifier:
    boto3_raw_data: "type_defs.ProvisionedIdentifierTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessIdentifier:
    boto3_raw_data: "type_defs.ServerlessIdentifierTypeDef" = dataclasses.field()

    NamespaceIdentifier = field("NamespaceIdentifier")
    WorkgroupIdentifier = field("WorkgroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerlessIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    NetworkInterfaceId = field("NetworkInterfaceId")
    SubnetId = field("SubnetId")
    PrivateIpAddress = field("PrivateIpAddress")
    AvailabilityZone = field("AvailabilityZone")
    Ipv6Address = field("Ipv6Address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeConfigurationOption:
    boto3_raw_data: "type_defs.NodeConfigurationOptionTypeDef" = dataclasses.field()

    NodeType = field("NodeType")
    NumberOfNodes = field("NumberOfNodes")
    EstimatedDiskUtilizationPercent = field("EstimatedDiskUtilizationPercent")
    Mode = field("Mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeConfigurationOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeConfigurationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerIntegrationInputMessageRequest:
    boto3_raw_data: "type_defs.PartnerIntegrationInputMessageRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClusterIdentifier = field("ClusterIdentifier")
    DatabaseName = field("DatabaseName")
    PartnerName = field("PartnerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PartnerIntegrationInputMessageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerIntegrationInputMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerIntegrationInputMessage:
    boto3_raw_data: "type_defs.PartnerIntegrationInputMessageTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClusterIdentifier = field("ClusterIdentifier")
    DatabaseName = field("DatabaseName")
    PartnerName = field("PartnerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PartnerIntegrationInputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerIntegrationInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseClusterMessageRequest:
    boto3_raw_data: "type_defs.PauseClusterMessageRequestTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseClusterMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseClusterMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseClusterMessage:
    boto3_raw_data: "type_defs.PauseClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedNodeOfferingMessage:
    boto3_raw_data: "type_defs.PurchaseReservedNodeOfferingMessageTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeOfferingId = field("ReservedNodeOfferingId")
    NodeCount = field("NodeCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedNodeOfferingMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedNodeOfferingMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyMessage:
    boto3_raw_data: "type_defs.PutResourcePolicyMessageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadWriteAccess:
    boto3_raw_data: "type_defs.ReadWriteAccessTypeDef" = dataclasses.field()

    Authorization = field("Authorization")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadWriteAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadWriteAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootClusterMessage:
    boto3_raw_data: "type_defs.RebootClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedAction:
    boto3_raw_data: "type_defs.RecommendedActionTypeDef" = dataclasses.field()

    Text = field("Text")
    Database = field("Database")
    Command = field("Command")
    Type = field("Type")

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
class ReferenceLink:
    boto3_raw_data: "type_defs.ReferenceLinkTypeDef" = dataclasses.field()

    Text = field("Text")
    Link = field("Link")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceLinkTypeDef"]],
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
class RejectDataShareMessage:
    boto3_raw_data: "type_defs.RejectDataShareMessageTypeDef" = dataclasses.field()

    DataShareArn = field("DataShareArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectDataShareMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectDataShareMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResizeClusterMessageRequest:
    boto3_raw_data: "type_defs.ResizeClusterMessageRequestTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    ClusterType = field("ClusterType")
    NodeType = field("NodeType")
    NumberOfNodes = field("NumberOfNodes")
    Classic = field("Classic")
    ReservedNodeId = field("ReservedNodeId")
    TargetReservedNodeOfferingId = field("TargetReservedNodeOfferingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResizeClusterMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResizeClusterMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResizeClusterMessage:
    boto3_raw_data: "type_defs.ResizeClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    ClusterType = field("ClusterType")
    NodeType = field("NodeType")
    NumberOfNodes = field("NumberOfNodes")
    Classic = field("Classic")
    ReservedNodeId = field("ReservedNodeId")
    TargetReservedNodeOfferingId = field("TargetReservedNodeOfferingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResizeClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResizeClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreFromClusterSnapshotMessage:
    boto3_raw_data: "type_defs.RestoreFromClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    SnapshotClusterIdentifier = field("SnapshotClusterIdentifier")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")
    AllowVersionUpgrade = field("AllowVersionUpgrade")
    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    PubliclyAccessible = field("PubliclyAccessible")
    OwnerAccount = field("OwnerAccount")
    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    ElasticIp = field("ElasticIp")
    ClusterParameterGroupName = field("ClusterParameterGroupName")
    ClusterSecurityGroups = field("ClusterSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    AutomatedSnapshotRetentionPeriod = field("AutomatedSnapshotRetentionPeriod")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    KmsKeyId = field("KmsKeyId")
    NodeType = field("NodeType")
    EnhancedVpcRouting = field("EnhancedVpcRouting")
    AdditionalInfo = field("AdditionalInfo")
    IamRoles = field("IamRoles")
    MaintenanceTrackName = field("MaintenanceTrackName")
    SnapshotScheduleIdentifier = field("SnapshotScheduleIdentifier")
    NumberOfNodes = field("NumberOfNodes")
    AvailabilityZoneRelocation = field("AvailabilityZoneRelocation")
    AquaConfigurationStatus = field("AquaConfigurationStatus")
    DefaultIamRoleArn = field("DefaultIamRoleArn")
    ReservedNodeId = field("ReservedNodeId")
    TargetReservedNodeOfferingId = field("TargetReservedNodeOfferingId")
    Encrypted = field("Encrypted")
    ManageMasterPassword = field("ManageMasterPassword")
    MasterPasswordSecretKmsKeyId = field("MasterPasswordSecretKmsKeyId")
    IpAddressType = field("IpAddressType")
    MultiAZ = field("MultiAZ")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreFromClusterSnapshotMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreFromClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromClusterSnapshotMessage:
    boto3_raw_data: "type_defs.RestoreTableFromClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SourceDatabaseName = field("SourceDatabaseName")
    SourceTableName = field("SourceTableName")
    NewTableName = field("NewTableName")
    SourceSchemaName = field("SourceSchemaName")
    TargetDatabaseName = field("TargetDatabaseName")
    TargetSchemaName = field("TargetSchemaName")
    EnableCaseSensitiveIdentifier = field("EnableCaseSensitiveIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreTableFromClusterSnapshotMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableRestoreStatus:
    boto3_raw_data: "type_defs.TableRestoreStatusTypeDef" = dataclasses.field()

    TableRestoreRequestId = field("TableRestoreRequestId")
    Status = field("Status")
    Message = field("Message")
    RequestTime = field("RequestTime")
    ProgressInMegaBytes = field("ProgressInMegaBytes")
    TotalDataInMegaBytes = field("TotalDataInMegaBytes")
    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SourceDatabaseName = field("SourceDatabaseName")
    SourceSchemaName = field("SourceSchemaName")
    SourceTableName = field("SourceTableName")
    TargetDatabaseName = field("TargetDatabaseName")
    TargetSchemaName = field("TargetSchemaName")
    NewTableName = field("NewTableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableRestoreStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableRestoreStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeClusterMessageRequest:
    boto3_raw_data: "type_defs.ResumeClusterMessageRequestTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeClusterMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeClusterMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeClusterMessage:
    boto3_raw_data: "type_defs.ResumeClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeClusterSecurityGroupIngressMessage:
    boto3_raw_data: "type_defs.RevokeClusterSecurityGroupIngressMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    CIDRIP = field("CIDRIP")
    EC2SecurityGroupName = field("EC2SecurityGroupName")
    EC2SecurityGroupOwnerId = field("EC2SecurityGroupOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeClusterSecurityGroupIngressMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeClusterSecurityGroupIngressMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeEndpointAccessMessage:
    boto3_raw_data: "type_defs.RevokeEndpointAccessMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    Account = field("Account")
    VpcIds = field("VpcIds")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeEndpointAccessMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeEndpointAccessMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeSnapshotAccessMessage:
    boto3_raw_data: "type_defs.RevokeSnapshotAccessMessageTypeDef" = dataclasses.field()

    AccountWithRestoreAccess = field("AccountWithRestoreAccess")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    SnapshotClusterIdentifier = field("SnapshotClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeSnapshotAccessMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeSnapshotAccessMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateEncryptionKeyMessage:
    boto3_raw_data: "type_defs.RotateEncryptionKeyMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RotateEncryptionKeyMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateEncryptionKeyMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedOperation:
    boto3_raw_data: "type_defs.SupportedOperationTypeDef" = dataclasses.field()

    OperationName = field("OperationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePartnerStatusInputMessage:
    boto3_raw_data: "type_defs.UpdatePartnerStatusInputMessageTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClusterIdentifier = field("ClusterIdentifier")
    DatabaseName = field("DatabaseName")
    PartnerName = field("PartnerName")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePartnerStatusInputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePartnerStatusInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterCredentials:
    boto3_raw_data: "type_defs.ClusterCredentialsTypeDef" = dataclasses.field()

    DbUser = field("DbUser")
    DbPassword = field("DbPassword")
    Expiration = field("Expiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterExtendedCredentials:
    boto3_raw_data: "type_defs.ClusterExtendedCredentialsTypeDef" = dataclasses.field()

    DbUser = field("DbUser")
    DbPassword = field("DbPassword")
    Expiration = field("Expiration")
    NextRefreshTime = field("NextRefreshTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterExtendedCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterExtendedCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterParameterGroupNameMessage:
    boto3_raw_data: "type_defs.ClusterParameterGroupNameMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    ParameterGroupStatus = field("ParameterGroupStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterParameterGroupNameMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterParameterGroupNameMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthenticationProfileResult:
    boto3_raw_data: "type_defs.CreateAuthenticationProfileResultTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")
    AuthenticationProfileContent = field("AuthenticationProfileContent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAuthenticationProfileResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthenticationProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomDomainAssociationResult:
    boto3_raw_data: "type_defs.CreateCustomDomainAssociationResultTypeDef" = (
        dataclasses.field()
    )

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    ClusterIdentifier = field("ClusterIdentifier")
    CustomDomainCertExpiryTime = field("CustomDomainCertExpiryTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDomainAssociationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerStorageMessage:
    boto3_raw_data: "type_defs.CustomerStorageMessageTypeDef" = dataclasses.field()

    TotalBackupSizeInMegaBytes = field("TotalBackupSizeInMegaBytes")
    TotalProvisionedStorageInMegaBytes = field("TotalProvisionedStorageInMegaBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerStorageMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerStorageMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuthenticationProfileResult:
    boto3_raw_data: "type_defs.DeleteAuthenticationProfileResultTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAuthenticationProfileResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuthenticationProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterNamespaceOutputMessage:
    boto3_raw_data: "type_defs.DeregisterNamespaceOutputMessageTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterNamespaceOutputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterNamespaceOutputMessageTypeDef"]
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
class EndpointAuthorizationResponse:
    boto3_raw_data: "type_defs.EndpointAuthorizationResponseTypeDef" = (
        dataclasses.field()
    )

    Grantor = field("Grantor")
    Grantee = field("Grantee")
    ClusterIdentifier = field("ClusterIdentifier")
    AuthorizeTime = field("AuthorizeTime")
    ClusterStatus = field("ClusterStatus")
    Status = field("Status")
    AllowedAllVPCs = field("AllowedAllVPCs")
    AllowedVPCs = field("AllowedVPCs")
    EndpointCount = field("EndpointCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EndpointAuthorizationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointAuthorizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingStatus:
    boto3_raw_data: "type_defs.LoggingStatusTypeDef" = dataclasses.field()

    LoggingEnabled = field("LoggingEnabled")
    BucketName = field("BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    LastSuccessfulDeliveryTime = field("LastSuccessfulDeliveryTime")
    LastFailureTime = field("LastFailureTime")
    LastFailureMessage = field("LastFailureMessage")
    LogDestinationType = field("LogDestinationType")
    LogExports = field("LogExports")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyAuthenticationProfileResult:
    boto3_raw_data: "type_defs.ModifyAuthenticationProfileResultTypeDef" = (
        dataclasses.field()
    )

    AuthenticationProfileName = field("AuthenticationProfileName")
    AuthenticationProfileContent = field("AuthenticationProfileContent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyAuthenticationProfileResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyAuthenticationProfileResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCustomDomainAssociationResult:
    boto3_raw_data: "type_defs.ModifyCustomDomainAssociationResultTypeDef" = (
        dataclasses.field()
    )

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    ClusterIdentifier = field("ClusterIdentifier")
    CustomDomainCertExpiryTime = field("CustomDomainCertExpiryTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyCustomDomainAssociationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCustomDomainAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerIntegrationOutputMessage:
    boto3_raw_data: "type_defs.PartnerIntegrationOutputMessageTypeDef" = (
        dataclasses.field()
    )

    DatabaseName = field("DatabaseName")
    PartnerName = field("PartnerName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PartnerIntegrationOutputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerIntegrationOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterNamespaceOutputMessage:
    boto3_raw_data: "type_defs.RegisterNamespaceOutputMessageTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterNamespaceOutputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterNamespaceOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResizeProgressMessage:
    boto3_raw_data: "type_defs.ResizeProgressMessageTypeDef" = dataclasses.field()

    TargetNodeType = field("TargetNodeType")
    TargetNumberOfNodes = field("TargetNumberOfNodes")
    TargetClusterType = field("TargetClusterType")
    Status = field("Status")
    ImportTablesCompleted = field("ImportTablesCompleted")
    ImportTablesInProgress = field("ImportTablesInProgress")
    ImportTablesNotStarted = field("ImportTablesNotStarted")
    AvgResizeRateInMegaBytesPerSecond = field("AvgResizeRateInMegaBytesPerSecond")
    TotalResizeDataInMegaBytes = field("TotalResizeDataInMegaBytes")
    ProgressInMegaBytes = field("ProgressInMegaBytes")
    ElapsedTimeInSeconds = field("ElapsedTimeInSeconds")
    EstimatedTimeToCompletionInSeconds = field("EstimatedTimeToCompletionInSeconds")
    ResizeType = field("ResizeType")
    Message = field("Message")
    TargetEncryptionType = field("TargetEncryptionType")
    DataTransferProgressPercent = field("DataTransferProgressPercent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResizeProgressMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResizeProgressMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAttribute:
    boto3_raw_data: "type_defs.AccountAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")

    @cached_property
    def AttributeValues(self):  # pragma: no cover
        return AttributeValueTarget.make_many(self.boto3_raw_data["AttributeValues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyAquaOutputMessage:
    boto3_raw_data: "type_defs.ModifyAquaOutputMessageTypeDef" = dataclasses.field()

    @cached_property
    def AquaConfiguration(self):  # pragma: no cover
        return AquaConfiguration.make_one(self.boto3_raw_data["AquaConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyAquaOutputMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyAquaOutputMessageTypeDef"]
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

    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    CustomDomainCertificateExpiryDate = field("CustomDomainCertificateExpiryDate")

    @cached_property
    def CertificateAssociations(self):  # pragma: no cover
        return CertificateAssociation.make_many(
            self.boto3_raw_data["CertificateAssociations"]
        )

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
class DescribeAuthenticationProfilesResult:
    boto3_raw_data: "type_defs.DescribeAuthenticationProfilesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthenticationProfiles(self):  # pragma: no cover
        return AuthenticationProfile.make_many(
            self.boto3_raw_data["AuthenticationProfiles"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAuthenticationProfilesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuthenticationProfilesResultTypeDef"]
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

    @cached_property
    def SupportedPlatforms(self):  # pragma: no cover
        return SupportedPlatform.make_many(self.boto3_raw_data["SupportedPlatforms"])

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
class BatchDeleteClusterSnapshotsRequest:
    boto3_raw_data: "type_defs.BatchDeleteClusterSnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Identifiers(self):  # pragma: no cover
        return DeleteClusterSnapshotMessage.make_many(
            self.boto3_raw_data["Identifiers"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteClusterSnapshotsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteClusterSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteClusterSnapshotsResult:
    boto3_raw_data: "type_defs.BatchDeleteClusterSnapshotsResultTypeDef" = (
        dataclasses.field()
    )

    Resources = field("Resources")

    @cached_property
    def Errors(self):  # pragma: no cover
        return SnapshotErrorMessage.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteClusterSnapshotsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteClusterSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchModifyClusterSnapshotsOutputMessage:
    boto3_raw_data: "type_defs.BatchModifyClusterSnapshotsOutputMessageTypeDef" = (
        dataclasses.field()
    )

    Resources = field("Resources")

    @cached_property
    def Errors(self):  # pragma: no cover
        return SnapshotErrorMessage.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchModifyClusterSnapshotsOutputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchModifyClusterSnapshotsOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterDbRevision:
    boto3_raw_data: "type_defs.ClusterDbRevisionTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    CurrentDatabaseRevision = field("CurrentDatabaseRevision")
    DatabaseRevisionReleaseDate = field("DatabaseRevisionReleaseDate")

    @cached_property
    def RevisionTargets(self):  # pragma: no cover
        return RevisionTarget.make_many(self.boto3_raw_data["RevisionTargets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterDbRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterDbRevisionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecondaryClusterInfo:
    boto3_raw_data: "type_defs.SecondaryClusterInfoTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def ClusterNodes(self):  # pragma: no cover
        return ClusterNode.make_many(self.boto3_raw_data["ClusterNodes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecondaryClusterInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecondaryClusterInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterParameterGroupDetails:
    boto3_raw_data: "type_defs.ClusterParameterGroupDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterParameterGroupDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterParameterGroupDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultClusterParameters:
    boto3_raw_data: "type_defs.DefaultClusterParametersTypeDef" = dataclasses.field()

    ParameterGroupFamily = field("ParameterGroupFamily")
    Marker = field("Marker")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultClusterParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultClusterParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.ModifyClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.ResetClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    ResetAllParameters = field("ResetAllParameters")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterParameterGroupStatus:
    boto3_raw_data: "type_defs.ClusterParameterGroupStatusTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")
    ParameterApplyStatus = field("ParameterApplyStatus")

    @cached_property
    def ClusterParameterStatusList(self):  # pragma: no cover
        return ClusterParameterStatus.make_many(
            self.boto3_raw_data["ClusterParameterStatusList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterParameterGroupStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterParameterGroupStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterParameterGroup:
    boto3_raw_data: "type_defs.ClusterParameterGroupTypeDef" = dataclasses.field()

    ParameterGroupName = field("ParameterGroupName")
    ParameterGroupFamily = field("ParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterParameterGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterParameterGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterMessage:
    boto3_raw_data: "type_defs.CreateClusterMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    NodeType = field("NodeType")
    MasterUsername = field("MasterUsername")
    DBName = field("DBName")
    ClusterType = field("ClusterType")
    MasterUserPassword = field("MasterUserPassword")
    ClusterSecurityGroups = field("ClusterSecurityGroups")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    AvailabilityZone = field("AvailabilityZone")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ClusterParameterGroupName = field("ClusterParameterGroupName")
    AutomatedSnapshotRetentionPeriod = field("AutomatedSnapshotRetentionPeriod")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    Port = field("Port")
    ClusterVersion = field("ClusterVersion")
    AllowVersionUpgrade = field("AllowVersionUpgrade")
    NumberOfNodes = field("NumberOfNodes")
    PubliclyAccessible = field("PubliclyAccessible")
    Encrypted = field("Encrypted")
    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    ElasticIp = field("ElasticIp")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    EnhancedVpcRouting = field("EnhancedVpcRouting")
    AdditionalInfo = field("AdditionalInfo")
    IamRoles = field("IamRoles")
    MaintenanceTrackName = field("MaintenanceTrackName")
    SnapshotScheduleIdentifier = field("SnapshotScheduleIdentifier")
    AvailabilityZoneRelocation = field("AvailabilityZoneRelocation")
    AquaConfigurationStatus = field("AquaConfigurationStatus")
    DefaultIamRoleArn = field("DefaultIamRoleArn")
    LoadSampleData = field("LoadSampleData")
    ManageMasterPassword = field("ManageMasterPassword")
    MasterPasswordSecretKmsKeyId = field("MasterPasswordSecretKmsKeyId")
    IpAddressType = field("IpAddressType")
    MultiAZ = field("MultiAZ")
    RedshiftIdcApplicationArn = field("RedshiftIdcApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterParameterGroupMessage:
    boto3_raw_data: "type_defs.CreateClusterParameterGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    ParameterGroupFamily = field("ParameterGroupFamily")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateClusterParameterGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterParameterGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterSecurityGroupMessage:
    boto3_raw_data: "type_defs.CreateClusterSecurityGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateClusterSecurityGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterSnapshotMessage:
    boto3_raw_data: "type_defs.CreateClusterSnapshotMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotIdentifier = field("SnapshotIdentifier")
    ClusterIdentifier = field("ClusterIdentifier")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterSnapshotMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterSnapshotMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterSubnetGroupMessage:
    boto3_raw_data: "type_defs.CreateClusterSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    Description = field("Description")
    SubnetIds = field("SubnetIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateClusterSubnetGroupMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterSubnetGroupMessageTypeDef"]
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
    SourceIds = field("SourceIds")
    EventCategories = field("EventCategories")
    Severity = field("Severity")
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
class CreateHsmClientCertificateMessage:
    boto3_raw_data: "type_defs.CreateHsmClientCertificateMessageTypeDef" = (
        dataclasses.field()
    )

    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateHsmClientCertificateMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHsmClientCertificateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHsmConfigurationMessage:
    boto3_raw_data: "type_defs.CreateHsmConfigurationMessageTypeDef" = (
        dataclasses.field()
    )

    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    Description = field("Description")
    HsmIpAddress = field("HsmIpAddress")
    HsmPartitionName = field("HsmPartitionName")
    HsmPartitionPassword = field("HsmPartitionPassword")
    HsmServerPublicCertificate = field("HsmServerPublicCertificate")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateHsmConfigurationMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHsmConfigurationMessageTypeDef"]
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

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    AdditionalEncryptionContext = field("AdditionalEncryptionContext")
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
class CreateSnapshotCopyGrantMessage:
    boto3_raw_data: "type_defs.CreateSnapshotCopyGrantMessageTypeDef" = (
        dataclasses.field()
    )

    SnapshotCopyGrantName = field("SnapshotCopyGrantName")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSnapshotCopyGrantMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotCopyGrantMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotScheduleMessage:
    boto3_raw_data: "type_defs.CreateSnapshotScheduleMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduleDefinitions = field("ScheduleDefinitions")
    ScheduleIdentifier = field("ScheduleIdentifier")
    ScheduleDescription = field("ScheduleDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DryRun = field("DryRun")
    NextInvocations = field("NextInvocations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSnapshotScheduleMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotScheduleMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagsMessage:
    boto3_raw_data: "type_defs.CreateTagsMessageTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTagsMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUsageLimitMessage:
    boto3_raw_data: "type_defs.CreateUsageLimitMessageTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    FeatureType = field("FeatureType")
    LimitType = field("LimitType")
    Amount = field("Amount")
    Period = field("Period")
    BreachAction = field("BreachAction")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUsageLimitMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUsageLimitMessageTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
    Severity = field("Severity")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class HsmClientCertificate:
    boto3_raw_data: "type_defs.HsmClientCertificateTypeDef" = dataclasses.field()

    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    HsmClientCertificatePublicKey = field("HsmClientCertificatePublicKey")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HsmClientCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HsmClientCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HsmConfiguration:
    boto3_raw_data: "type_defs.HsmConfigurationTypeDef" = dataclasses.field()

    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    Description = field("Description")
    HsmIpAddress = field("HsmIpAddress")
    HsmPartitionName = field("HsmPartitionName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HsmConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HsmConfigurationTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class SnapshotCopyGrant:
    boto3_raw_data: "type_defs.SnapshotCopyGrantTypeDef" = dataclasses.field()

    SnapshotCopyGrantName = field("SnapshotCopyGrantName")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotCopyGrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotCopyGrantTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotScheduleResponse:
    boto3_raw_data: "type_defs.SnapshotScheduleResponseTypeDef" = dataclasses.field()

    ScheduleDefinitions = field("ScheduleDefinitions")
    ScheduleIdentifier = field("ScheduleIdentifier")
    ScheduleDescription = field("ScheduleDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    NextInvocations = field("NextInvocations")
    AssociatedClusterCount = field("AssociatedClusterCount")

    @cached_property
    def AssociatedClusters(self):  # pragma: no cover
        return ClusterAssociatedToSchedule.make_many(
            self.boto3_raw_data["AssociatedClusters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapshotScheduleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotScheduleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotSchedule:
    boto3_raw_data: "type_defs.SnapshotScheduleTypeDef" = dataclasses.field()

    ScheduleDefinitions = field("ScheduleDefinitions")
    ScheduleIdentifier = field("ScheduleIdentifier")
    ScheduleDescription = field("ScheduleDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    NextInvocations = field("NextInvocations")
    AssociatedClusterCount = field("AssociatedClusterCount")

    @cached_property
    def AssociatedClusters(self):  # pragma: no cover
        return ClusterAssociatedToSchedule.make_many(
            self.boto3_raw_data["AssociatedClusters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotScheduleTypeDef"]
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

    SnapshotIdentifier = field("SnapshotIdentifier")
    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotCreateTime = field("SnapshotCreateTime")
    Status = field("Status")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")
    ClusterCreateTime = field("ClusterCreateTime")
    MasterUsername = field("MasterUsername")
    ClusterVersion = field("ClusterVersion")
    EngineFullVersion = field("EngineFullVersion")
    SnapshotType = field("SnapshotType")
    NodeType = field("NodeType")
    NumberOfNodes = field("NumberOfNodes")
    DBName = field("DBName")
    VpcId = field("VpcId")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    EncryptedWithHSM = field("EncryptedWithHSM")

    @cached_property
    def AccountsWithRestoreAccess(self):  # pragma: no cover
        return AccountWithRestoreAccess.make_many(
            self.boto3_raw_data["AccountsWithRestoreAccess"]
        )

    OwnerAccount = field("OwnerAccount")
    TotalBackupSizeInMegaBytes = field("TotalBackupSizeInMegaBytes")
    ActualIncrementalBackupSizeInMegaBytes = field(
        "ActualIncrementalBackupSizeInMegaBytes"
    )
    BackupProgressInMegaBytes = field("BackupProgressInMegaBytes")
    CurrentBackupRateInMegaBytesPerSecond = field(
        "CurrentBackupRateInMegaBytesPerSecond"
    )
    EstimatedSecondsToCompletion = field("EstimatedSecondsToCompletion")
    ElapsedTimeInSeconds = field("ElapsedTimeInSeconds")
    SourceRegion = field("SourceRegion")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    RestorableNodeTypes = field("RestorableNodeTypes")
    EnhancedVpcRouting = field("EnhancedVpcRouting")
    MaintenanceTrackName = field("MaintenanceTrackName")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")
    ManualSnapshotRemainingDays = field("ManualSnapshotRemainingDays")
    SnapshotRetentionStartTime = field("SnapshotRetentionStartTime")
    MasterPasswordSecretArn = field("MasterPasswordSecretArn")
    MasterPasswordSecretKmsKeyId = field("MasterPasswordSecretKmsKeyId")
    SnapshotArn = field("SnapshotArn")

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
class TaggedResource:
    boto3_raw_data: "type_defs.TaggedResourceTypeDef" = dataclasses.field()

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    ResourceName = field("ResourceName")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaggedResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaggedResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageLimitResponse:
    boto3_raw_data: "type_defs.UsageLimitResponseTypeDef" = dataclasses.field()

    UsageLimitId = field("UsageLimitId")
    ClusterIdentifier = field("ClusterIdentifier")
    FeatureType = field("FeatureType")
    LimitType = field("LimitType")
    Amount = field("Amount")
    Period = field("Period")
    BreachAction = field("BreachAction")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageLimit:
    boto3_raw_data: "type_defs.UsageLimitTypeDef" = dataclasses.field()

    UsageLimitId = field("UsageLimitId")
    ClusterIdentifier = field("ClusterIdentifier")
    FeatureType = field("FeatureType")
    LimitType = field("LimitType")
    Amount = field("Amount")
    Period = field("Period")
    BreachAction = field("BreachAction")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageLimitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodeExchangeStatusOutputMessage:
    boto3_raw_data: (
        "type_defs.DescribeReservedNodeExchangeStatusOutputMessageTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ReservedNodeExchangeStatusDetails(self):  # pragma: no cover
        return ReservedNodeExchangeStatus.make_many(
            self.boto3_raw_data["ReservedNodeExchangeStatusDetails"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodeExchangeStatusOutputMessageTypeDef"
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
                "type_defs.DescribeReservedNodeExchangeStatusOutputMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterVersionsMessage:
    boto3_raw_data: "type_defs.ClusterVersionsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ClusterVersions(self):  # pragma: no cover
        return ClusterVersion.make_many(self.boto3_raw_data["ClusterVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterVersionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterVersionsMessageTypeDef"]
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
class ModifyClusterMaintenanceMessage:
    boto3_raw_data: "type_defs.ModifyClusterMaintenanceMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    DeferMaintenance = field("DeferMaintenance")
    DeferMaintenanceIdentifier = field("DeferMaintenanceIdentifier")
    DeferMaintenanceStartTime = field("DeferMaintenanceStartTime")
    DeferMaintenanceEndTime = field("DeferMaintenanceEndTime")
    DeferMaintenanceDuration = field("DeferMaintenanceDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClusterMaintenanceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterMaintenanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataShareResponse:
    boto3_raw_data: "type_defs.DataShareResponseTypeDef" = dataclasses.field()

    DataShareArn = field("DataShareArn")
    ProducerArn = field("ProducerArn")
    AllowPubliclyAccessibleConsumers = field("AllowPubliclyAccessibleConsumers")

    @cached_property
    def DataShareAssociations(self):  # pragma: no cover
        return DataShareAssociation.make_many(
            self.boto3_raw_data["DataShareAssociations"]
        )

    ManagedBy = field("ManagedBy")
    DataShareType = field("DataShareType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataShareResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataShare:
    boto3_raw_data: "type_defs.DataShareTypeDef" = dataclasses.field()

    DataShareArn = field("DataShareArn")
    ProducerArn = field("ProducerArn")
    AllowPubliclyAccessibleConsumers = field("AllowPubliclyAccessibleConsumers")

    @cached_property
    def DataShareAssociations(self):  # pragma: no cover
        return DataShareAssociation.make_many(
            self.boto3_raw_data["DataShareAssociations"]
        )

    ManagedBy = field("ManagedBy")
    DataShareType = field("DataShareType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataShareTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataShareTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterDbRevisionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterDbRevisionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterDbRevisionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterDbRevisionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterParameterGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterParameterGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterParameterGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterParameterGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterParametersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterParametersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ParameterGroupName = field("ParameterGroupName")
    Source = field("Source")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterParametersMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterParametersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSecurityGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterSecurityGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterSecurityGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSecurityGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSubnetGroupsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterSubnetGroupsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterSubnetGroupsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSubnetGroupsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterTracksMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterTracksMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    MaintenanceTrackName = field("MaintenanceTrackName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterTracksMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterTracksMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterVersionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterVersionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterVersion = field("ClusterVersion")
    ClusterParameterGroupFamily = field("ClusterParameterGroupFamily")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterVersionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterVersionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClustersMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClustersMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomDomainAssociationsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeCustomDomainAssociationsMessagePaginateTypeDef"
    ) = dataclasses.field()

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomDomainAssociationsMessagePaginateTypeDef"
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
                "type_defs.DescribeCustomDomainAssociationsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesForConsumerMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDataSharesForConsumerMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ConsumerArn = field("ConsumerArn")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesForConsumerMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesForConsumerMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesForProducerMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDataSharesForProducerMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ProducerArn = field("ProducerArn")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesForProducerMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesForProducerMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDataSharesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    DataShareArn = field("DataShareArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDefaultClusterParametersMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeDefaultClusterParametersMessagePaginateTypeDef"
    ) = dataclasses.field()

    ParameterGroupFamily = field("ParameterGroupFamily")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDefaultClusterParametersMessagePaginateTypeDef"
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
                "type_defs.DescribeDefaultClusterParametersMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointAccessMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEndpointAccessMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    ResourceOwner = field("ResourceOwner")
    EndpointName = field("EndpointName")
    VpcId = field("VpcId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEndpointAccessMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointAccessMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointAuthorizationMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEndpointAuthorizationMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    Account = field("Account")
    Grantee = field("Grantee")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEndpointAuthorizationMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointAuthorizationMessagePaginateTypeDef"]
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
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

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
class DescribeHsmClientCertificatesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeHsmClientCertificatesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    HsmClientCertificateIdentifier = field("HsmClientCertificateIdentifier")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHsmClientCertificatesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHsmClientCertificatesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHsmConfigurationsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeHsmConfigurationsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    HsmConfigurationIdentifier = field("HsmConfigurationIdentifier")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeHsmConfigurationsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHsmConfigurationsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundIntegrationsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeInboundIntegrationsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    IntegrationArn = field("IntegrationArn")
    TargetArn = field("TargetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundIntegrationsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInboundIntegrationsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableClusterOptionsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrderableClusterOptionsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ClusterVersion = field("ClusterVersion")
    NodeType = field("NodeType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableClusterOptionsMessagePaginateTypeDef"
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
                "type_defs.DescribeOrderableClusterOptionsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRedshiftIdcApplicationsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeRedshiftIdcApplicationsMessagePaginateTypeDef"
    ) = dataclasses.field()

    RedshiftIdcApplicationArn = field("RedshiftIdcApplicationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRedshiftIdcApplicationsMessagePaginateTypeDef"
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
                "type_defs.DescribeRedshiftIdcApplicationsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodeExchangeStatusInputMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef"
    ) = dataclasses.field()

    ReservedNodeId = field("ReservedNodeId")
    ReservedNodeExchangeRequestId = field("ReservedNodeExchangeRequestId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef"
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
                "type_defs.DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodeOfferingsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReservedNodeOfferingsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeOfferingId = field("ReservedNodeOfferingId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodeOfferingsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodeOfferingsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReservedNodesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReservedNodesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReservedNodeId = field("ReservedNodeId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReservedNodesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReservedNodesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotCopyGrantsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeSnapshotCopyGrantsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SnapshotCopyGrantName = field("SnapshotCopyGrantName")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSnapshotCopyGrantsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotCopyGrantsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotSchedulesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeSnapshotSchedulesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    ScheduleIdentifier = field("ScheduleIdentifier")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSnapshotSchedulesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotSchedulesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableRestoreStatusMessagePaginate:
    boto3_raw_data: "type_defs.DescribeTableRestoreStatusMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    TableRestoreRequestId = field("TableRestoreRequestId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTableRestoreStatusMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableRestoreStatusMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeTagsMessagePaginateTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    ResourceType = field("ResourceType")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsMessagePaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUsageLimitsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeUsageLimitsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    UsageLimitId = field("UsageLimitId")
    ClusterIdentifier = field("ClusterIdentifier")
    FeatureType = field("FeatureType")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeUsageLimitsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUsageLimitsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservedNodeExchangeConfigurationOptionsInputMessagePaginate:
    boto3_raw_data: "type_defs.GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef" = (dataclasses.field())

    ActionType = field("ActionType")
    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef"
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
                "type_defs.GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservedNodeExchangeOfferingsInputMessagePaginate:
    boto3_raw_data: (
        "type_defs.GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef"
    ) = dataclasses.field()

    ReservedNodeId = field("ReservedNodeId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef"
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
                "type_defs.GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsMessagePaginate:
    boto3_raw_data: "type_defs.ListRecommendationsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    NamespaceArn = field("NamespaceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecommendationsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSnapshotsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeClusterSnapshotsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    SnapshotType = field("SnapshotType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OwnerAccount = field("OwnerAccount")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")
    ClusterExists = field("ClusterExists")

    @cached_property
    def SortingEntities(self):  # pragma: no cover
        return SnapshotSortingEntity.make_many(self.boto3_raw_data["SortingEntities"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterSnapshotsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSnapshotsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSnapshotsMessage:
    boto3_raw_data: "type_defs.DescribeClusterSnapshotsMessageTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    SnapshotType = field("SnapshotType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    OwnerAccount = field("OwnerAccount")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")
    ClusterExists = field("ClusterExists")

    @cached_property
    def SortingEntities(self):  # pragma: no cover
        return SnapshotSortingEntity.make_many(self.boto3_raw_data["SortingEntities"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterSnapshotsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSnapshotsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterSnapshotsMessageWait:
    boto3_raw_data: "type_defs.DescribeClusterSnapshotsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    SnapshotType = field("SnapshotType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    OwnerAccount = field("OwnerAccount")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")
    ClusterExists = field("ClusterExists")

    @cached_property
    def SortingEntities(self):  # pragma: no cover
        return SnapshotSortingEntity.make_many(self.boto3_raw_data["SortingEntities"])

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterSnapshotsMessageWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterSnapshotsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersMessageWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeClustersMessageWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClustersMessageWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersMessageWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeClustersMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ClusterIdentifier = field("ClusterIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClustersMessageWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersMessageWait:
    boto3_raw_data: "type_defs.DescribeClustersMessageWaitTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    TagKeys = field("TagKeys")
    TagValues = field("TagValues")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClustersMessageWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersMessageWaitTypeDef"]
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

    IntegrationArn = field("IntegrationArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeIntegrationsFilter.make_many(self.boto3_raw_data["Filters"])

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
class DescribeIntegrationsMessage:
    boto3_raw_data: "type_defs.DescribeIntegrationsMessageTypeDef" = dataclasses.field()

    IntegrationArn = field("IntegrationArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeIntegrationsFilter.make_many(self.boto3_raw_data["Filters"])

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
class DescribeNodeConfigurationOptionsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeNodeConfigurationOptionsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ActionType = field("ActionType")
    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    OwnerAccount = field("OwnerAccount")

    @cached_property
    def Filters(self):  # pragma: no cover
        return NodeConfigurationOptionsFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNodeConfigurationOptionsMessagePaginateTypeDef"
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
                "type_defs.DescribeNodeConfigurationOptionsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodeConfigurationOptionsMessage:
    boto3_raw_data: "type_defs.DescribeNodeConfigurationOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    ActionType = field("ActionType")
    ClusterIdentifier = field("ClusterIdentifier")
    SnapshotIdentifier = field("SnapshotIdentifier")
    SnapshotArn = field("SnapshotArn")
    OwnerAccount = field("OwnerAccount")

    @cached_property
    def Filters(self):  # pragma: no cover
        return NodeConfigurationOptionsFilter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNodeConfigurationOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodeConfigurationOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePartnersOutputMessage:
    boto3_raw_data: "type_defs.DescribePartnersOutputMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PartnerIntegrationInfoList(self):  # pragma: no cover
        return PartnerIntegrationInfo.make_many(
            self.boto3_raw_data["PartnerIntegrationInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePartnersOutputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePartnersOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeScheduledActionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")
    TargetActionType = field("TargetActionType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Active = field("Active")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ScheduledActionFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScheduledActionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledActionsMessage:
    boto3_raw_data: "type_defs.DescribeScheduledActionsMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")
    TargetActionType = field("TargetActionType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Active = field("Active")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ScheduledActionFilter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledActionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointAuthorizationList:
    boto3_raw_data: "type_defs.EndpointAuthorizationListTypeDef" = dataclasses.field()

    @cached_property
    def EndpointAuthorizationList(self):  # pragma: no cover
        return EndpointAuthorization.make_many(
            self.boto3_raw_data["EndpointAuthorizationList"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointAuthorizationListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointAuthorizationListTypeDef"]
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

    @cached_property
    def Events(self):  # pragma: no cover
        return EventInfoMap.make_many(self.boto3_raw_data["Events"])

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
class GetResourcePolicyResult:
    boto3_raw_data: "type_defs.GetResourcePolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def ResourcePolicy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["ResourcePolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResult:
    boto3_raw_data: "type_defs.PutResourcePolicyResultTypeDef" = dataclasses.field()

    @cached_property
    def ResourcePolicy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["ResourcePolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundIntegration:
    boto3_raw_data: "type_defs.InboundIntegrationTypeDef" = dataclasses.field()

    IntegrationArn = field("IntegrationArn")
    SourceArn = field("SourceArn")
    TargetArn = field("TargetArn")
    Status = field("Status")

    @cached_property
    def Errors(self):  # pragma: no cover
        return IntegrationError.make_many(self.boto3_raw_data["Errors"])

    CreateTime = field("CreateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InboundIntegrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundIntegrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationResponse:
    boto3_raw_data: "type_defs.IntegrationResponseTypeDef" = dataclasses.field()

    IntegrationArn = field("IntegrationArn")
    IntegrationName = field("IntegrationName")
    SourceArn = field("SourceArn")
    TargetArn = field("TargetArn")
    Status = field("Status")

    @cached_property
    def Errors(self):  # pragma: no cover
        return IntegrationError.make_many(self.boto3_raw_data["Errors"])

    CreateTime = field("CreateTime")
    Description = field("Description")
    KMSKeyId = field("KMSKeyId")
    AdditionalEncryptionContext = field("AdditionalEncryptionContext")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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

    IntegrationArn = field("IntegrationArn")
    IntegrationName = field("IntegrationName")
    SourceArn = field("SourceArn")
    TargetArn = field("TargetArn")
    Status = field("Status")

    @cached_property
    def Errors(self):  # pragma: no cover
        return IntegrationError.make_many(self.boto3_raw_data["Errors"])

    CreateTime = field("CreateTime")
    Description = field("Description")
    KMSKeyId = field("KMSKeyId")
    AdditionalEncryptionContext = field("AdditionalEncryptionContext")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class LakeFormationScopeUnion:
    boto3_raw_data: "type_defs.LakeFormationScopeUnionTypeDef" = dataclasses.field()

    @cached_property
    def LakeFormationQuery(self):  # pragma: no cover
        return LakeFormationQuery.make_one(self.boto3_raw_data["LakeFormationQuery"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LakeFormationScopeUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationScopeUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NamespaceIdentifierUnion:
    boto3_raw_data: "type_defs.NamespaceIdentifierUnionTypeDef" = dataclasses.field()

    @cached_property
    def ServerlessIdentifier(self):  # pragma: no cover
        return ServerlessIdentifier.make_one(
            self.boto3_raw_data["ServerlessIdentifier"]
        )

    @cached_property
    def ProvisionedIdentifier(self):  # pragma: no cover
        return ProvisionedIdentifier.make_one(
            self.boto3_raw_data["ProvisionedIdentifier"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NamespaceIdentifierUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NamespaceIdentifierUnionTypeDef"]
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
    VpcId = field("VpcId")

    @cached_property
    def NetworkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["NetworkInterfaces"])

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
class NodeConfigurationOptionsMessage:
    boto3_raw_data: "type_defs.NodeConfigurationOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NodeConfigurationOptionList(self):  # pragma: no cover
        return NodeConfigurationOption.make_many(
            self.boto3_raw_data["NodeConfigurationOptionList"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NodeConfigurationOptionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeConfigurationOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessGrantsScopeUnion:
    boto3_raw_data: "type_defs.S3AccessGrantsScopeUnionTypeDef" = dataclasses.field()

    @cached_property
    def ReadWriteAccess(self):  # pragma: no cover
        return ReadWriteAccess.make_one(self.boto3_raw_data["ReadWriteAccess"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessGrantsScopeUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessGrantsScopeUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    Id = field("Id")
    ClusterIdentifier = field("ClusterIdentifier")
    NamespaceArn = field("NamespaceArn")
    CreatedAt = field("CreatedAt")
    RecommendationType = field("RecommendationType")
    Title = field("Title")
    Description = field("Description")
    Observation = field("Observation")
    ImpactRanking = field("ImpactRanking")
    RecommendationText = field("RecommendationText")

    @cached_property
    def RecommendedActions(self):  # pragma: no cover
        return RecommendedAction.make_many(self.boto3_raw_data["RecommendedActions"])

    @cached_property
    def ReferenceLinks(self):  # pragma: no cover
        return ReferenceLink.make_many(self.boto3_raw_data["ReferenceLinks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNodeOffering:
    boto3_raw_data: "type_defs.ReservedNodeOfferingTypeDef" = dataclasses.field()

    ReservedNodeOfferingId = field("ReservedNodeOfferingId")
    NodeType = field("NodeType")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    OfferingType = field("OfferingType")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    ReservedNodeOfferingType = field("ReservedNodeOfferingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedNodeOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedNodeOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNode:
    boto3_raw_data: "type_defs.ReservedNodeTypeDef" = dataclasses.field()

    ReservedNodeId = field("ReservedNodeId")
    ReservedNodeOfferingId = field("ReservedNodeOfferingId")
    NodeType = field("NodeType")
    StartTime = field("StartTime")
    Duration = field("Duration")
    FixedPrice = field("FixedPrice")
    UsagePrice = field("UsagePrice")
    CurrencyCode = field("CurrencyCode")
    NodeCount = field("NodeCount")
    State = field("State")
    OfferingType = field("OfferingType")

    @cached_property
    def RecurringCharges(self):  # pragma: no cover
        return RecurringCharge.make_many(self.boto3_raw_data["RecurringCharges"])

    ReservedNodeOfferingType = field("ReservedNodeOfferingType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservedNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReservedNodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromClusterSnapshotResult:
    boto3_raw_data: "type_defs.RestoreTableFromClusterSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TableRestoreStatus(self):  # pragma: no cover
        return TableRestoreStatus.make_one(self.boto3_raw_data["TableRestoreStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreTableFromClusterSnapshotResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableRestoreStatusMessage:
    boto3_raw_data: "type_defs.TableRestoreStatusMessageTypeDef" = dataclasses.field()

    @cached_property
    def TableRestoreStatusDetails(self):  # pragma: no cover
        return TableRestoreStatus.make_many(
            self.boto3_raw_data["TableRestoreStatusDetails"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableRestoreStatusMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableRestoreStatusMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledActionType:
    boto3_raw_data: "type_defs.ScheduledActionTypeTypeDef" = dataclasses.field()

    @cached_property
    def ResizeCluster(self):  # pragma: no cover
        return ResizeClusterMessage.make_one(self.boto3_raw_data["ResizeCluster"])

    @cached_property
    def PauseCluster(self):  # pragma: no cover
        return PauseClusterMessage.make_one(self.boto3_raw_data["PauseCluster"])

    @cached_property
    def ResumeCluster(self):  # pragma: no cover
        return ResumeClusterMessage.make_one(self.boto3_raw_data["ResumeCluster"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTarget:
    boto3_raw_data: "type_defs.UpdateTargetTypeDef" = dataclasses.field()

    MaintenanceTrackName = field("MaintenanceTrackName")
    DatabaseVersion = field("DatabaseVersion")

    @cached_property
    def SupportedOperations(self):  # pragma: no cover
        return SupportedOperation.make_many(self.boto3_raw_data["SupportedOperations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAttributeList:
    boto3_raw_data: "type_defs.AccountAttributeListTypeDef" = dataclasses.field()

    @cached_property
    def AccountAttributes(self):  # pragma: no cover
        return AccountAttribute.make_many(self.boto3_raw_data["AccountAttributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountAttributeListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAttributeListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDomainAssociationsMessage:
    boto3_raw_data: "type_defs.CustomDomainAssociationsMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["Associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomDomainAssociationsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDomainAssociationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderableClusterOption:
    boto3_raw_data: "type_defs.OrderableClusterOptionTypeDef" = dataclasses.field()

    ClusterVersion = field("ClusterVersion")
    ClusterType = field("ClusterType")
    NodeType = field("NodeType")

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["AvailabilityZones"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrderableClusterOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableClusterOptionTypeDef"]
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
class ClusterDbRevisionsMessage:
    boto3_raw_data: "type_defs.ClusterDbRevisionsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ClusterDbRevisions(self):  # pragma: no cover
        return ClusterDbRevision.make_many(self.boto3_raw_data["ClusterDbRevisions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterDbRevisionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterDbRevisionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDefaultClusterParametersResult:
    boto3_raw_data: "type_defs.DescribeDefaultClusterParametersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DefaultClusterParameters(self):  # pragma: no cover
        return DefaultClusterParameters.make_one(
            self.boto3_raw_data["DefaultClusterParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDefaultClusterParametersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDefaultClusterParametersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterParameterGroupsMessage:
    boto3_raw_data: "type_defs.ClusterParameterGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ParameterGroups(self):  # pragma: no cover
        return ClusterParameterGroup.make_many(self.boto3_raw_data["ParameterGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterParameterGroupsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterParameterGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterParameterGroupResult:
    boto3_raw_data: "type_defs.CreateClusterParameterGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterParameterGroup(self):  # pragma: no cover
        return ClusterParameterGroup.make_one(
            self.boto3_raw_data["ClusterParameterGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateClusterParameterGroupResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterParameterGroupResultTypeDef"]
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
class CreateHsmClientCertificateResult:
    boto3_raw_data: "type_defs.CreateHsmClientCertificateResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HsmClientCertificate(self):  # pragma: no cover
        return HsmClientCertificate.make_one(
            self.boto3_raw_data["HsmClientCertificate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateHsmClientCertificateResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHsmClientCertificateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HsmClientCertificateMessage:
    boto3_raw_data: "type_defs.HsmClientCertificateMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def HsmClientCertificates(self):  # pragma: no cover
        return HsmClientCertificate.make_many(
            self.boto3_raw_data["HsmClientCertificates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HsmClientCertificateMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HsmClientCertificateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHsmConfigurationResult:
    boto3_raw_data: "type_defs.CreateHsmConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HsmConfiguration(self):  # pragma: no cover
        return HsmConfiguration.make_one(self.boto3_raw_data["HsmConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHsmConfigurationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHsmConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HsmConfigurationMessage:
    boto3_raw_data: "type_defs.HsmConfigurationMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def HsmConfigurations(self):  # pragma: no cover
        return HsmConfiguration.make_many(self.boto3_raw_data["HsmConfigurations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HsmConfigurationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HsmConfigurationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSecurityGroup:
    boto3_raw_data: "type_defs.ClusterSecurityGroupTypeDef" = dataclasses.field()

    ClusterSecurityGroupName = field("ClusterSecurityGroupName")
    Description = field("Description")

    @cached_property
    def EC2SecurityGroups(self):  # pragma: no cover
        return EC2SecurityGroup.make_many(self.boto3_raw_data["EC2SecurityGroups"])

    @cached_property
    def IPRanges(self):  # pragma: no cover
        return IPRange.make_many(self.boto3_raw_data["IPRanges"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterSecurityGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSecurityGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotCopyGrantResult:
    boto3_raw_data: "type_defs.CreateSnapshotCopyGrantResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SnapshotCopyGrant(self):  # pragma: no cover
        return SnapshotCopyGrant.make_one(self.boto3_raw_data["SnapshotCopyGrant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSnapshotCopyGrantResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotCopyGrantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotCopyGrantMessage:
    boto3_raw_data: "type_defs.SnapshotCopyGrantMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def SnapshotCopyGrants(self):  # pragma: no cover
        return SnapshotCopyGrant.make_many(self.boto3_raw_data["SnapshotCopyGrants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapshotCopyGrantMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotCopyGrantMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSnapshotSchedulesOutputMessage:
    boto3_raw_data: "type_defs.DescribeSnapshotSchedulesOutputMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SnapshotSchedules(self):  # pragma: no cover
        return SnapshotSchedule.make_many(self.boto3_raw_data["SnapshotSchedules"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSnapshotSchedulesOutputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSnapshotSchedulesOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeSnapshotAccessResult:
    boto3_raw_data: "type_defs.AuthorizeSnapshotAccessResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthorizeSnapshotAccessResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeSnapshotAccessResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyClusterSnapshotResult:
    boto3_raw_data: "type_defs.CopyClusterSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyClusterSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterSnapshotResult:
    boto3_raw_data: "type_defs.CreateClusterSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterSnapshotResult:
    boto3_raw_data: "type_defs.DeleteClusterSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterSnapshotResult:
    boto3_raw_data: "type_defs.ModifyClusterSnapshotResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterSnapshotResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeSnapshotAccessResult:
    boto3_raw_data: "type_defs.RevokeSnapshotAccessResultTypeDef" = dataclasses.field()

    @cached_property
    def Snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["Snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeSnapshotAccessResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeSnapshotAccessResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotMessage:
    boto3_raw_data: "type_defs.SnapshotMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Snapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["Snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaggedResourceListMessage:
    boto3_raw_data: "type_defs.TaggedResourceListMessageTypeDef" = dataclasses.field()

    @cached_property
    def TaggedResources(self):  # pragma: no cover
        return TaggedResource.make_many(self.boto3_raw_data["TaggedResources"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaggedResourceListMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaggedResourceListMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageLimitList:
    boto3_raw_data: "type_defs.UsageLimitListTypeDef" = dataclasses.field()

    @cached_property
    def UsageLimits(self):  # pragma: no cover
        return UsageLimit.make_many(self.boto3_raw_data["UsageLimits"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageLimitListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageLimitListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesForConsumerResult:
    boto3_raw_data: "type_defs.DescribeDataSharesForConsumerResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataShares(self):  # pragma: no cover
        return DataShare.make_many(self.boto3_raw_data["DataShares"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesForConsumerResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesForConsumerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesForProducerResult:
    boto3_raw_data: "type_defs.DescribeDataSharesForProducerResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataShares(self):  # pragma: no cover
        return DataShare.make_many(self.boto3_raw_data["DataShares"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataSharesForProducerResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesForProducerResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataSharesResult:
    boto3_raw_data: "type_defs.DescribeDataSharesResultTypeDef" = dataclasses.field()

    @cached_property
    def DataShares(self):  # pragma: no cover
        return DataShare.make_many(self.boto3_raw_data["DataShares"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataSharesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataSharesResultTypeDef"]
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
class InboundIntegrationsMessage:
    boto3_raw_data: "type_defs.InboundIntegrationsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def InboundIntegrations(self):  # pragma: no cover
        return InboundIntegration.make_many(self.boto3_raw_data["InboundIntegrations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InboundIntegrationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundIntegrationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationsMessage:
    boto3_raw_data: "type_defs.IntegrationsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Integrations(self):  # pragma: no cover
        return Integration.make_many(self.boto3_raw_data["Integrations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterNamespaceInputMessage:
    boto3_raw_data: "type_defs.DeregisterNamespaceInputMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NamespaceIdentifier(self):  # pragma: no cover
        return NamespaceIdentifierUnion.make_one(
            self.boto3_raw_data["NamespaceIdentifier"]
        )

    ConsumerIdentifiers = field("ConsumerIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterNamespaceInputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterNamespaceInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterNamespaceInputMessage:
    boto3_raw_data: "type_defs.RegisterNamespaceInputMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NamespaceIdentifier(self):  # pragma: no cover
        return NamespaceIdentifierUnion.make_one(
            self.boto3_raw_data["NamespaceIdentifier"]
        )

    ConsumerIdentifiers = field("ConsumerIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterNamespaceInputMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterNamespaceInputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointAccessResponse:
    boto3_raw_data: "type_defs.EndpointAccessResponseTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    ResourceOwner = field("ResourceOwner")
    SubnetGroupName = field("SubnetGroupName")
    EndpointStatus = field("EndpointStatus")
    EndpointName = field("EndpointName")
    EndpointCreateTime = field("EndpointCreateTime")
    Port = field("Port")
    Address = field("Address")

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    @cached_property
    def VpcEndpoint(self):  # pragma: no cover
        return VpcEndpoint.make_one(self.boto3_raw_data["VpcEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointAccess:
    boto3_raw_data: "type_defs.EndpointAccessTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    ResourceOwner = field("ResourceOwner")
    SubnetGroupName = field("SubnetGroupName")
    EndpointStatus = field("EndpointStatus")
    EndpointName = field("EndpointName")
    EndpointCreateTime = field("EndpointCreateTime")
    Port = field("Port")
    Address = field("Address")

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    @cached_property
    def VpcEndpoint(self):  # pragma: no cover
        return VpcEndpoint.make_one(self.boto3_raw_data["VpcEndpoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointAccessTypeDef"]],
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

    @cached_property
    def VpcEndpoints(self):  # pragma: no cover
        return VpcEndpoint.make_many(self.boto3_raw_data["VpcEndpoints"])

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
class ServiceIntegrationsUnionOutput:
    boto3_raw_data: "type_defs.ServiceIntegrationsUnionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LakeFormation(self):  # pragma: no cover
        return LakeFormationScopeUnion.make_many(self.boto3_raw_data["LakeFormation"])

    @cached_property
    def S3AccessGrants(self):  # pragma: no cover
        return S3AccessGrantsScopeUnion.make_many(self.boto3_raw_data["S3AccessGrants"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceIntegrationsUnionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceIntegrationsUnionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceIntegrationsUnion:
    boto3_raw_data: "type_defs.ServiceIntegrationsUnionTypeDef" = dataclasses.field()

    @cached_property
    def LakeFormation(self):  # pragma: no cover
        return LakeFormationScopeUnion.make_many(self.boto3_raw_data["LakeFormation"])

    @cached_property
    def S3AccessGrants(self):  # pragma: no cover
        return S3AccessGrantsScopeUnion.make_many(self.boto3_raw_data["S3AccessGrants"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceIntegrationsUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceIntegrationsUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendationsResult:
    boto3_raw_data: "type_defs.ListRecommendationsResultTypeDef" = dataclasses.field()

    @cached_property
    def Recommendations(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["Recommendations"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservedNodeExchangeOfferingsOutputMessage:
    boto3_raw_data: "type_defs.GetReservedNodeExchangeOfferingsOutputMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReservedNodeOfferings(self):  # pragma: no cover
        return ReservedNodeOffering.make_many(
            self.boto3_raw_data["ReservedNodeOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservedNodeExchangeOfferingsOutputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservedNodeExchangeOfferingsOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNodeOfferingsMessage:
    boto3_raw_data: "type_defs.ReservedNodeOfferingsMessageTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReservedNodeOfferings(self):  # pragma: no cover
        return ReservedNodeOffering.make_many(
            self.boto3_raw_data["ReservedNodeOfferings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedNodeOfferingsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedNodeOfferingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptReservedNodeExchangeOutputMessage:
    boto3_raw_data: "type_defs.AcceptReservedNodeExchangeOutputMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ExchangedReservedNode(self):  # pragma: no cover
        return ReservedNode.make_one(self.boto3_raw_data["ExchangedReservedNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptReservedNodeExchangeOutputMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptReservedNodeExchangeOutputMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PurchaseReservedNodeOfferingResult:
    boto3_raw_data: "type_defs.PurchaseReservedNodeOfferingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReservedNode(self):  # pragma: no cover
        return ReservedNode.make_one(self.boto3_raw_data["ReservedNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PurchaseReservedNodeOfferingResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PurchaseReservedNodeOfferingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNodeConfigurationOption:
    boto3_raw_data: "type_defs.ReservedNodeConfigurationOptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceReservedNode(self):  # pragma: no cover
        return ReservedNode.make_one(self.boto3_raw_data["SourceReservedNode"])

    TargetReservedNodeCount = field("TargetReservedNodeCount")

    @cached_property
    def TargetReservedNodeOffering(self):  # pragma: no cover
        return ReservedNodeOffering.make_one(
            self.boto3_raw_data["TargetReservedNodeOffering"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReservedNodeConfigurationOptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedNodeConfigurationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservedNodesMessage:
    boto3_raw_data: "type_defs.ReservedNodesMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ReservedNodes(self):  # pragma: no cover
        return ReservedNode.make_many(self.boto3_raw_data["ReservedNodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservedNodesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservedNodesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduledActionMessage:
    boto3_raw_data: "type_defs.CreateScheduledActionMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")

    @cached_property
    def TargetAction(self):  # pragma: no cover
        return ScheduledActionType.make_one(self.boto3_raw_data["TargetAction"])

    Schedule = field("Schedule")
    IamRole = field("IamRole")
    ScheduledActionDescription = field("ScheduledActionDescription")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Enable = field("Enable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduledActionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyScheduledActionMessage:
    boto3_raw_data: "type_defs.ModifyScheduledActionMessageTypeDef" = (
        dataclasses.field()
    )

    ScheduledActionName = field("ScheduledActionName")

    @cached_property
    def TargetAction(self):  # pragma: no cover
        return ScheduledActionType.make_one(self.boto3_raw_data["TargetAction"])

    Schedule = field("Schedule")
    IamRole = field("IamRole")
    ScheduledActionDescription = field("ScheduledActionDescription")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Enable = field("Enable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyScheduledActionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyScheduledActionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledActionResponse:
    boto3_raw_data: "type_defs.ScheduledActionResponseTypeDef" = dataclasses.field()

    ScheduledActionName = field("ScheduledActionName")

    @cached_property
    def TargetAction(self):  # pragma: no cover
        return ScheduledActionType.make_one(self.boto3_raw_data["TargetAction"])

    Schedule = field("Schedule")
    IamRole = field("IamRole")
    ScheduledActionDescription = field("ScheduledActionDescription")
    State = field("State")
    NextInvocations = field("NextInvocations")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledActionResponseTypeDef"]
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

    ScheduledActionName = field("ScheduledActionName")

    @cached_property
    def TargetAction(self):  # pragma: no cover
        return ScheduledActionType.make_one(self.boto3_raw_data["TargetAction"])

    Schedule = field("Schedule")
    IamRole = field("IamRole")
    ScheduledActionDescription = field("ScheduledActionDescription")
    State = field("State")
    NextInvocations = field("NextInvocations")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

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
class MaintenanceTrack:
    boto3_raw_data: "type_defs.MaintenanceTrackTypeDef" = dataclasses.field()

    MaintenanceTrackName = field("MaintenanceTrackName")
    DatabaseVersion = field("DatabaseVersion")

    @cached_property
    def UpdateTargets(self):  # pragma: no cover
        return UpdateTarget.make_many(self.boto3_raw_data["UpdateTargets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaintenanceTrackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceTrackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderableClusterOptionsMessage:
    boto3_raw_data: "type_defs.OrderableClusterOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrderableClusterOptions(self):  # pragma: no cover
        return OrderableClusterOption.make_many(
            self.boto3_raw_data["OrderableClusterOptions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrderableClusterOptionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableClusterOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSubnetGroup:
    boto3_raw_data: "type_defs.ClusterSubnetGroupTypeDef" = dataclasses.field()

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    Description = field("Description")
    VpcId = field("VpcId")
    SubnetGroupStatus = field("SubnetGroupStatus")

    @cached_property
    def Subnets(self):  # pragma: no cover
        return Subnet.make_many(self.boto3_raw_data["Subnets"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SupportedClusterIpAddressTypes = field("SupportedClusterIpAddressTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterSubnetGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSubnetGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeClusterSecurityGroupIngressResult:
    boto3_raw_data: "type_defs.AuthorizeClusterSecurityGroupIngressResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterSecurityGroup(self):  # pragma: no cover
        return ClusterSecurityGroup.make_one(
            self.boto3_raw_data["ClusterSecurityGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthorizeClusterSecurityGroupIngressResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeClusterSecurityGroupIngressResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSecurityGroupMessage:
    boto3_raw_data: "type_defs.ClusterSecurityGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ClusterSecurityGroups(self):  # pragma: no cover
        return ClusterSecurityGroup.make_many(
            self.boto3_raw_data["ClusterSecurityGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterSecurityGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSecurityGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterSecurityGroupResult:
    boto3_raw_data: "type_defs.CreateClusterSecurityGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterSecurityGroup(self):  # pragma: no cover
        return ClusterSecurityGroup.make_one(
            self.boto3_raw_data["ClusterSecurityGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateClusterSecurityGroupResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterSecurityGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeClusterSecurityGroupIngressResult:
    boto3_raw_data: "type_defs.RevokeClusterSecurityGroupIngressResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterSecurityGroup(self):  # pragma: no cover
        return ClusterSecurityGroup.make_one(
            self.boto3_raw_data["ClusterSecurityGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RevokeClusterSecurityGroupIngressResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeClusterSecurityGroupIngressResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointAccessList:
    boto3_raw_data: "type_defs.EndpointAccessListTypeDef" = dataclasses.field()

    @cached_property
    def EndpointAccessList(self):  # pragma: no cover
        return EndpointAccess.make_many(self.boto3_raw_data["EndpointAccessList"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointAccessListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointAccessListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cluster:
    boto3_raw_data: "type_defs.ClusterTypeDef" = dataclasses.field()

    ClusterIdentifier = field("ClusterIdentifier")
    NodeType = field("NodeType")
    ClusterStatus = field("ClusterStatus")
    ClusterAvailabilityStatus = field("ClusterAvailabilityStatus")
    ModifyStatus = field("ModifyStatus")
    MasterUsername = field("MasterUsername")
    DBName = field("DBName")

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    ClusterCreateTime = field("ClusterCreateTime")
    AutomatedSnapshotRetentionPeriod = field("AutomatedSnapshotRetentionPeriod")
    ManualSnapshotRetentionPeriod = field("ManualSnapshotRetentionPeriod")

    @cached_property
    def ClusterSecurityGroups(self):  # pragma: no cover
        return ClusterSecurityGroupMembership.make_many(
            self.boto3_raw_data["ClusterSecurityGroups"]
        )

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    @cached_property
    def ClusterParameterGroups(self):  # pragma: no cover
        return ClusterParameterGroupStatus.make_many(
            self.boto3_raw_data["ClusterParameterGroups"]
        )

    ClusterSubnetGroupName = field("ClusterSubnetGroupName")
    VpcId = field("VpcId")
    AvailabilityZone = field("AvailabilityZone")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return PendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    ClusterVersion = field("ClusterVersion")
    AllowVersionUpgrade = field("AllowVersionUpgrade")
    NumberOfNodes = field("NumberOfNodes")
    PubliclyAccessible = field("PubliclyAccessible")
    Encrypted = field("Encrypted")

    @cached_property
    def RestoreStatus(self):  # pragma: no cover
        return RestoreStatus.make_one(self.boto3_raw_data["RestoreStatus"])

    @cached_property
    def DataTransferProgress(self):  # pragma: no cover
        return DataTransferProgress.make_one(
            self.boto3_raw_data["DataTransferProgress"]
        )

    @cached_property
    def HsmStatus(self):  # pragma: no cover
        return HsmStatus.make_one(self.boto3_raw_data["HsmStatus"])

    @cached_property
    def ClusterSnapshotCopyStatus(self):  # pragma: no cover
        return ClusterSnapshotCopyStatus.make_one(
            self.boto3_raw_data["ClusterSnapshotCopyStatus"]
        )

    ClusterPublicKey = field("ClusterPublicKey")

    @cached_property
    def ClusterNodes(self):  # pragma: no cover
        return ClusterNode.make_many(self.boto3_raw_data["ClusterNodes"])

    @cached_property
    def ElasticIpStatus(self):  # pragma: no cover
        return ElasticIpStatus.make_one(self.boto3_raw_data["ElasticIpStatus"])

    ClusterRevisionNumber = field("ClusterRevisionNumber")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    EnhancedVpcRouting = field("EnhancedVpcRouting")

    @cached_property
    def IamRoles(self):  # pragma: no cover
        return ClusterIamRole.make_many(self.boto3_raw_data["IamRoles"])

    PendingActions = field("PendingActions")
    MaintenanceTrackName = field("MaintenanceTrackName")
    ElasticResizeNumberOfNodeOptions = field("ElasticResizeNumberOfNodeOptions")

    @cached_property
    def DeferredMaintenanceWindows(self):  # pragma: no cover
        return DeferredMaintenanceWindow.make_many(
            self.boto3_raw_data["DeferredMaintenanceWindows"]
        )

    SnapshotScheduleIdentifier = field("SnapshotScheduleIdentifier")
    SnapshotScheduleState = field("SnapshotScheduleState")
    ExpectedNextSnapshotScheduleTime = field("ExpectedNextSnapshotScheduleTime")
    ExpectedNextSnapshotScheduleTimeStatus = field(
        "ExpectedNextSnapshotScheduleTimeStatus"
    )
    NextMaintenanceWindowStartTime = field("NextMaintenanceWindowStartTime")

    @cached_property
    def ResizeInfo(self):  # pragma: no cover
        return ResizeInfo.make_one(self.boto3_raw_data["ResizeInfo"])

    AvailabilityZoneRelocationStatus = field("AvailabilityZoneRelocationStatus")
    ClusterNamespaceArn = field("ClusterNamespaceArn")
    TotalStorageCapacityInMegaBytes = field("TotalStorageCapacityInMegaBytes")

    @cached_property
    def AquaConfiguration(self):  # pragma: no cover
        return AquaConfiguration.make_one(self.boto3_raw_data["AquaConfiguration"])

    DefaultIamRoleArn = field("DefaultIamRoleArn")

    @cached_property
    def ReservedNodeExchangeStatus(self):  # pragma: no cover
        return ReservedNodeExchangeStatus.make_one(
            self.boto3_raw_data["ReservedNodeExchangeStatus"]
        )

    CustomDomainName = field("CustomDomainName")
    CustomDomainCertificateArn = field("CustomDomainCertificateArn")
    CustomDomainCertificateExpiryDate = field("CustomDomainCertificateExpiryDate")
    MasterPasswordSecretArn = field("MasterPasswordSecretArn")
    MasterPasswordSecretKmsKeyId = field("MasterPasswordSecretKmsKeyId")
    IpAddressType = field("IpAddressType")
    MultiAZ = field("MultiAZ")

    @cached_property
    def MultiAZSecondary(self):  # pragma: no cover
        return SecondaryClusterInfo.make_one(self.boto3_raw_data["MultiAZSecondary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftIdcApplication:
    boto3_raw_data: "type_defs.RedshiftIdcApplicationTypeDef" = dataclasses.field()

    IdcInstanceArn = field("IdcInstanceArn")
    RedshiftIdcApplicationName = field("RedshiftIdcApplicationName")
    RedshiftIdcApplicationArn = field("RedshiftIdcApplicationArn")
    IdentityNamespace = field("IdentityNamespace")
    IdcDisplayName = field("IdcDisplayName")
    IamRoleArn = field("IamRoleArn")
    IdcManagedApplicationArn = field("IdcManagedApplicationArn")
    IdcOnboardStatus = field("IdcOnboardStatus")

    @cached_property
    def AuthorizedTokenIssuerList(self):  # pragma: no cover
        return AuthorizedTokenIssuerOutput.make_many(
            self.boto3_raw_data["AuthorizedTokenIssuerList"]
        )

    @cached_property
    def ServiceIntegrations(self):  # pragma: no cover
        return ServiceIntegrationsUnionOutput.make_many(
            self.boto3_raw_data["ServiceIntegrations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftIdcApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftIdcApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservedNodeExchangeConfigurationOptionsOutputMessage:
    boto3_raw_data: (
        "type_defs.GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef"
    ) = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ReservedNodeConfigurationOptionList(self):  # pragma: no cover
        return ReservedNodeConfigurationOption.make_many(
            self.boto3_raw_data["ReservedNodeConfigurationOptionList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef"
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
                "type_defs.GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledActionsMessage:
    boto3_raw_data: "type_defs.ScheduledActionsMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ScheduledActions(self):  # pragma: no cover
        return ScheduledAction.make_many(self.boto3_raw_data["ScheduledActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackListMessage:
    boto3_raw_data: "type_defs.TrackListMessageTypeDef" = dataclasses.field()

    @cached_property
    def MaintenanceTracks(self):  # pragma: no cover
        return MaintenanceTrack.make_many(self.boto3_raw_data["MaintenanceTracks"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrackListMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrackListMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSubnetGroupMessage:
    boto3_raw_data: "type_defs.ClusterSubnetGroupMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ClusterSubnetGroups(self):  # pragma: no cover
        return ClusterSubnetGroup.make_many(self.boto3_raw_data["ClusterSubnetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterSubnetGroupMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterSubnetGroupResult:
    boto3_raw_data: "type_defs.CreateClusterSubnetGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterSubnetGroup(self):  # pragma: no cover
        return ClusterSubnetGroup.make_one(self.boto3_raw_data["ClusterSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateClusterSubnetGroupResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterSubnetGroupResult:
    boto3_raw_data: "type_defs.ModifyClusterSubnetGroupResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterSubnetGroup(self):  # pragma: no cover
        return ClusterSubnetGroup.make_one(self.boto3_raw_data["ClusterSubnetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClusterSubnetGroupResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterSubnetGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClustersMessage:
    boto3_raw_data: "type_defs.ClustersMessageTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Clusters(self):  # pragma: no cover
        return Cluster.make_many(self.boto3_raw_data["Clusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClustersMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClustersMessageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterResult:
    boto3_raw_data: "type_defs.CreateClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterResult:
    boto3_raw_data: "type_defs.DeleteClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableSnapshotCopyResult:
    boto3_raw_data: "type_defs.DisableSnapshotCopyResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableSnapshotCopyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableSnapshotCopyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableSnapshotCopyResult:
    boto3_raw_data: "type_defs.EnableSnapshotCopyResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableSnapshotCopyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableSnapshotCopyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverPrimaryComputeResult:
    boto3_raw_data: "type_defs.FailoverPrimaryComputeResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailoverPrimaryComputeResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailoverPrimaryComputeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterDbRevisionResult:
    boto3_raw_data: "type_defs.ModifyClusterDbRevisionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClusterDbRevisionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterDbRevisionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterIamRolesResult:
    boto3_raw_data: "type_defs.ModifyClusterIamRolesResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterIamRolesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterIamRolesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterMaintenanceResult:
    boto3_raw_data: "type_defs.ModifyClusterMaintenanceResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClusterMaintenanceResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterMaintenanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClusterResult:
    boto3_raw_data: "type_defs.ModifyClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifySnapshotCopyRetentionPeriodResult:
    boto3_raw_data: "type_defs.ModifySnapshotCopyRetentionPeriodResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifySnapshotCopyRetentionPeriodResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifySnapshotCopyRetentionPeriodResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseClusterResult:
    boto3_raw_data: "type_defs.PauseClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootClusterResult:
    boto3_raw_data: "type_defs.RebootClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResizeClusterResult:
    boto3_raw_data: "type_defs.ResizeClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResizeClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResizeClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreFromClusterSnapshotResult:
    boto3_raw_data: "type_defs.RestoreFromClusterSnapshotResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreFromClusterSnapshotResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreFromClusterSnapshotResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeClusterResult:
    boto3_raw_data: "type_defs.ResumeClusterResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeClusterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeClusterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateEncryptionKeyResult:
    boto3_raw_data: "type_defs.RotateEncryptionKeyResultTypeDef" = dataclasses.field()

    @cached_property
    def Cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["Cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RotateEncryptionKeyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateEncryptionKeyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRedshiftIdcApplicationResult:
    boto3_raw_data: "type_defs.CreateRedshiftIdcApplicationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RedshiftIdcApplication(self):  # pragma: no cover
        return RedshiftIdcApplication.make_one(
            self.boto3_raw_data["RedshiftIdcApplication"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRedshiftIdcApplicationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRedshiftIdcApplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRedshiftIdcApplicationsResult:
    boto3_raw_data: "type_defs.DescribeRedshiftIdcApplicationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RedshiftIdcApplications(self):  # pragma: no cover
        return RedshiftIdcApplication.make_many(
            self.boto3_raw_data["RedshiftIdcApplications"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRedshiftIdcApplicationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRedshiftIdcApplicationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyRedshiftIdcApplicationResult:
    boto3_raw_data: "type_defs.ModifyRedshiftIdcApplicationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RedshiftIdcApplication(self):  # pragma: no cover
        return RedshiftIdcApplication.make_one(
            self.boto3_raw_data["RedshiftIdcApplication"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyRedshiftIdcApplicationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyRedshiftIdcApplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRedshiftIdcApplicationMessage:
    boto3_raw_data: "type_defs.CreateRedshiftIdcApplicationMessageTypeDef" = (
        dataclasses.field()
    )

    IdcInstanceArn = field("IdcInstanceArn")
    RedshiftIdcApplicationName = field("RedshiftIdcApplicationName")
    IdcDisplayName = field("IdcDisplayName")
    IamRoleArn = field("IamRoleArn")
    IdentityNamespace = field("IdentityNamespace")
    AuthorizedTokenIssuerList = field("AuthorizedTokenIssuerList")
    ServiceIntegrations = field("ServiceIntegrations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRedshiftIdcApplicationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRedshiftIdcApplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyRedshiftIdcApplicationMessage:
    boto3_raw_data: "type_defs.ModifyRedshiftIdcApplicationMessageTypeDef" = (
        dataclasses.field()
    )

    RedshiftIdcApplicationArn = field("RedshiftIdcApplicationArn")
    IdentityNamespace = field("IdentityNamespace")
    IamRoleArn = field("IamRoleArn")
    IdcDisplayName = field("IdcDisplayName")
    AuthorizedTokenIssuerList = field("AuthorizedTokenIssuerList")
    ServiceIntegrations = field("ServiceIntegrations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyRedshiftIdcApplicationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyRedshiftIdcApplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
