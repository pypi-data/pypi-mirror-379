# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_serverless import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Association:
    boto3_raw_data: "type_defs.AssociationTypeDef" = dataclasses.field()

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainCertificateExpiryTime = field("customDomainCertificateExpiryTime")
    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

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
class ConfigParameter:
    boto3_raw_data: "type_defs.ConfigParameterTypeDef" = dataclasses.field()

    parameterKey = field("parameterKey")
    parameterValue = field("parameterValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

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
class Snapshot:
    boto3_raw_data: "type_defs.SnapshotTypeDef" = dataclasses.field()

    accountsWithProvisionedRestoreAccess = field("accountsWithProvisionedRestoreAccess")
    accountsWithRestoreAccess = field("accountsWithRestoreAccess")
    actualIncrementalBackupSizeInMegaBytes = field(
        "actualIncrementalBackupSizeInMegaBytes"
    )
    adminPasswordSecretArn = field("adminPasswordSecretArn")
    adminPasswordSecretKmsKeyId = field("adminPasswordSecretKmsKeyId")
    adminUsername = field("adminUsername")
    backupProgressInMegaBytes = field("backupProgressInMegaBytes")
    currentBackupRateInMegaBytesPerSecond = field(
        "currentBackupRateInMegaBytesPerSecond"
    )
    elapsedTimeInSeconds = field("elapsedTimeInSeconds")
    estimatedSecondsToCompletion = field("estimatedSecondsToCompletion")
    kmsKeyId = field("kmsKeyId")
    namespaceArn = field("namespaceArn")
    namespaceName = field("namespaceName")
    ownerAccount = field("ownerAccount")
    snapshotArn = field("snapshotArn")
    snapshotCreateTime = field("snapshotCreateTime")
    snapshotName = field("snapshotName")
    snapshotRemainingDays = field("snapshotRemainingDays")
    snapshotRetentionPeriod = field("snapshotRetentionPeriod")
    snapshotRetentionStartTime = field("snapshotRetentionStartTime")
    status = field("status")
    totalBackupSizeInMegaBytes = field("totalBackupSizeInMegaBytes")

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
class CreateCustomDomainAssociationRequest:
    boto3_raw_data: "type_defs.CreateCustomDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDomainAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointAccessRequest:
    boto3_raw_data: "type_defs.CreateEndpointAccessRequestTypeDef" = dataclasses.field()

    endpointName = field("endpointName")
    subnetIds = field("subnetIds")
    workgroupName = field("workgroupName")
    ownerAccount = field("ownerAccount")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Namespace:
    boto3_raw_data: "type_defs.NamespaceTypeDef" = dataclasses.field()

    adminPasswordSecretArn = field("adminPasswordSecretArn")
    adminPasswordSecretKmsKeyId = field("adminPasswordSecretKmsKeyId")
    adminUsername = field("adminUsername")
    creationDate = field("creationDate")
    dbName = field("dbName")
    defaultIamRoleArn = field("defaultIamRoleArn")
    iamRoles = field("iamRoles")
    kmsKeyId = field("kmsKeyId")
    logExports = field("logExports")
    namespaceArn = field("namespaceArn")
    namespaceId = field("namespaceId")
    namespaceName = field("namespaceName")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NamespaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NamespaceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReservationRequest:
    boto3_raw_data: "type_defs.CreateReservationRequestTypeDef" = dataclasses.field()

    capacity = field("capacity")
    offeringId = field("offeringId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReservationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotCopyConfigurationRequest:
    boto3_raw_data: "type_defs.CreateSnapshotCopyConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    destinationRegion = field("destinationRegion")
    namespaceName = field("namespaceName")
    destinationKmsKeyId = field("destinationKmsKeyId")
    snapshotRetentionPeriod = field("snapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSnapshotCopyConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotCopyConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapshotCopyConfiguration:
    boto3_raw_data: "type_defs.SnapshotCopyConfigurationTypeDef" = dataclasses.field()

    destinationKmsKeyId = field("destinationKmsKeyId")
    destinationRegion = field("destinationRegion")
    namespaceName = field("namespaceName")
    snapshotCopyConfigurationArn = field("snapshotCopyConfigurationArn")
    snapshotCopyConfigurationId = field("snapshotCopyConfigurationId")
    snapshotRetentionPeriod = field("snapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnapshotCopyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapshotCopyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUsageLimitRequest:
    boto3_raw_data: "type_defs.CreateUsageLimitRequestTypeDef" = dataclasses.field()

    amount = field("amount")
    resourceArn = field("resourceArn")
    usageType = field("usageType")
    breachAction = field("breachAction")
    period = field("period")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUsageLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUsageLimitRequestTypeDef"]
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

    amount = field("amount")
    breachAction = field("breachAction")
    period = field("period")
    resourceArn = field("resourceArn")
    usageLimitArn = field("usageLimitArn")
    usageLimitId = field("usageLimitId")
    usageType = field("usageType")

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
class PerformanceTarget:
    boto3_raw_data: "type_defs.PerformanceTargetTypeDef" = dataclasses.field()

    level = field("level")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PerformanceTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomDomainAssociationRequest:
    boto3_raw_data: "type_defs.DeleteCustomDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomDomainAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointAccessRequest:
    boto3_raw_data: "type_defs.DeleteEndpointAccessRequestTypeDef" = dataclasses.field()

    endpointName = field("endpointName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNamespaceRequest:
    boto3_raw_data: "type_defs.DeleteNamespaceRequestTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")
    finalSnapshotName = field("finalSnapshotName")
    finalSnapshotRetentionPeriod = field("finalSnapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNamespaceRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class DeleteScheduledActionRequest:
    boto3_raw_data: "type_defs.DeleteScheduledActionRequestTypeDef" = (
        dataclasses.field()
    )

    scheduledActionName = field("scheduledActionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduledActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotCopyConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteSnapshotCopyConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    snapshotCopyConfigurationId = field("snapshotCopyConfigurationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSnapshotCopyConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotCopyConfigurationRequestTypeDef"]
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

    snapshotName = field("snapshotName")

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
class DeleteUsageLimitRequest:
    boto3_raw_data: "type_defs.DeleteUsageLimitRequestTypeDef" = dataclasses.field()

    usageLimitId = field("usageLimitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUsageLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUsageLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkgroupRequest:
    boto3_raw_data: "type_defs.DeleteWorkgroupRequestTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkgroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkgroupRequestTypeDef"]
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

    status = field("status")
    vpcSecurityGroupId = field("vpcSecurityGroupId")

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
class GetCredentialsRequest:
    boto3_raw_data: "type_defs.GetCredentialsRequestTypeDef" = dataclasses.field()

    customDomainName = field("customDomainName")
    dbName = field("dbName")
    durationSeconds = field("durationSeconds")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCredentialsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomDomainAssociationRequest:
    boto3_raw_data: "type_defs.GetCustomDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomDomainAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEndpointAccessRequest:
    boto3_raw_data: "type_defs.GetEndpointAccessRequestTypeDef" = dataclasses.field()

    endpointName = field("endpointName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEndpointAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNamespaceRequest:
    boto3_raw_data: "type_defs.GetNamespaceRequestTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecoveryPointRequest:
    boto3_raw_data: "type_defs.GetRecoveryPointRequestTypeDef" = dataclasses.field()

    recoveryPointId = field("recoveryPointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecoveryPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecoveryPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryPoint:
    boto3_raw_data: "type_defs.RecoveryPointTypeDef" = dataclasses.field()

    namespaceArn = field("namespaceArn")
    namespaceName = field("namespaceName")
    recoveryPointCreateTime = field("recoveryPointCreateTime")
    recoveryPointId = field("recoveryPointId")
    totalSizeInMegaBytes = field("totalSizeInMegaBytes")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecoveryPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecoveryPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationOfferingRequest:
    boto3_raw_data: "type_defs.GetReservationOfferingRequestTypeDef" = (
        dataclasses.field()
    )

    offeringId = field("offeringId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReservationOfferingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationOfferingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReservationOffering:
    boto3_raw_data: "type_defs.ReservationOfferingTypeDef" = dataclasses.field()

    currencyCode = field("currencyCode")
    duration = field("duration")
    hourlyCharge = field("hourlyCharge")
    offeringId = field("offeringId")
    offeringType = field("offeringType")
    upfrontCharge = field("upfrontCharge")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReservationOfferingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReservationOfferingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationRequest:
    boto3_raw_data: "type_defs.GetReservationRequestTypeDef" = dataclasses.field()

    reservationId = field("reservationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
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

    policy = field("policy")
    resourceArn = field("resourceArn")

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
class GetScheduledActionRequest:
    boto3_raw_data: "type_defs.GetScheduledActionRequestTypeDef" = dataclasses.field()

    scheduledActionName = field("scheduledActionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetScheduledActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScheduledActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotRequest:
    boto3_raw_data: "type_defs.GetSnapshotRequestTypeDef" = dataclasses.field()

    ownerAccount = field("ownerAccount")
    snapshotArn = field("snapshotArn")
    snapshotName = field("snapshotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTableRestoreStatusRequest:
    boto3_raw_data: "type_defs.GetTableRestoreStatusRequestTypeDef" = (
        dataclasses.field()
    )

    tableRestoreRequestId = field("tableRestoreRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTableRestoreStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableRestoreStatusRequestTypeDef"]
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

    message = field("message")
    namespaceName = field("namespaceName")
    newTableName = field("newTableName")
    progressInMegaBytes = field("progressInMegaBytes")
    recoveryPointId = field("recoveryPointId")
    requestTime = field("requestTime")
    snapshotName = field("snapshotName")
    sourceDatabaseName = field("sourceDatabaseName")
    sourceSchemaName = field("sourceSchemaName")
    sourceTableName = field("sourceTableName")
    status = field("status")
    tableRestoreRequestId = field("tableRestoreRequestId")
    targetDatabaseName = field("targetDatabaseName")
    targetSchemaName = field("targetSchemaName")
    totalDataInMegaBytes = field("totalDataInMegaBytes")
    workgroupName = field("workgroupName")

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
class GetTrackRequest:
    boto3_raw_data: "type_defs.GetTrackRequestTypeDef" = dataclasses.field()

    trackName = field("trackName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTrackRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTrackRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageLimitRequest:
    boto3_raw_data: "type_defs.GetUsageLimitRequestTypeDef" = dataclasses.field()

    usageLimitId = field("usageLimitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkgroupRequest:
    boto3_raw_data: "type_defs.GetWorkgroupRequestTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkgroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkgroupRequestTypeDef"]
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
class ListCustomDomainAssociationsRequest:
    boto3_raw_data: "type_defs.ListCustomDomainAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainName = field("customDomainName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomDomainAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomDomainAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointAccessRequest:
    boto3_raw_data: "type_defs.ListEndpointAccessRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    ownerAccount = field("ownerAccount")
    vpcId = field("vpcId")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedWorkgroupsRequest:
    boto3_raw_data: "type_defs.ListManagedWorkgroupsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sourceArn = field("sourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedWorkgroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedWorkgroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedWorkgroupListItem:
    boto3_raw_data: "type_defs.ManagedWorkgroupListItemTypeDef" = dataclasses.field()

    creationDate = field("creationDate")
    managedWorkgroupId = field("managedWorkgroupId")
    managedWorkgroupName = field("managedWorkgroupName")
    sourceArn = field("sourceArn")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedWorkgroupListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedWorkgroupListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamespacesRequest:
    boto3_raw_data: "type_defs.ListNamespacesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNamespacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamespacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationOfferingsRequest:
    boto3_raw_data: "type_defs.ListReservationOfferingsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReservationOfferingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationOfferingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsRequest:
    boto3_raw_data: "type_defs.ListReservationsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReservationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsRequestTypeDef"]
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

    maxResults = field("maxResults")
    namespaceName = field("namespaceName")
    nextToken = field("nextToken")

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
class ScheduledActionAssociation:
    boto3_raw_data: "type_defs.ScheduledActionAssociationTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")
    scheduledActionName = field("scheduledActionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledActionAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledActionAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotCopyConfigurationsRequest:
    boto3_raw_data: "type_defs.ListSnapshotCopyConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    namespaceName = field("namespaceName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSnapshotCopyConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotCopyConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableRestoreStatusRequest:
    boto3_raw_data: "type_defs.ListTableRestoreStatusRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    namespaceName = field("namespaceName")
    nextToken = field("nextToken")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTableRestoreStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableRestoreStatusRequestTypeDef"]
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
class ListTracksRequest:
    boto3_raw_data: "type_defs.ListTracksRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTracksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTracksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageLimitsRequest:
    boto3_raw_data: "type_defs.ListUsageLimitsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    resourceArn = field("resourceArn")
    usageType = field("usageType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsageLimitsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkgroupsRequest:
    boto3_raw_data: "type_defs.ListWorkgroupsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    ownerAccount = field("ownerAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkgroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkgroupsRequestTypeDef"]
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

    availabilityZone = field("availabilityZone")
    ipv6Address = field("ipv6Address")
    networkInterfaceId = field("networkInterfaceId")
    privateIpAddress = field("privateIpAddress")
    subnetId = field("subnetId")

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
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    policy = field("policy")
    resourceArn = field("resourceArn")

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
class RestoreFromRecoveryPointRequest:
    boto3_raw_data: "type_defs.RestoreFromRecoveryPointRequestTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    recoveryPointId = field("recoveryPointId")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreFromRecoveryPointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreFromRecoveryPointRequestTypeDef"]
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

    namespaceName = field("namespaceName")
    workgroupName = field("workgroupName")
    adminPasswordSecretKmsKeyId = field("adminPasswordSecretKmsKeyId")
    manageAdminPassword = field("manageAdminPassword")
    ownerAccount = field("ownerAccount")
    snapshotArn = field("snapshotArn")
    snapshotName = field("snapshotName")

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
class RestoreTableFromRecoveryPointRequest:
    boto3_raw_data: "type_defs.RestoreTableFromRecoveryPointRequestTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    newTableName = field("newTableName")
    recoveryPointId = field("recoveryPointId")
    sourceDatabaseName = field("sourceDatabaseName")
    sourceTableName = field("sourceTableName")
    workgroupName = field("workgroupName")
    activateCaseSensitiveIdentifier = field("activateCaseSensitiveIdentifier")
    sourceSchemaName = field("sourceSchemaName")
    targetDatabaseName = field("targetDatabaseName")
    targetSchemaName = field("targetSchemaName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreTableFromRecoveryPointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromRecoveryPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromSnapshotRequest:
    boto3_raw_data: "type_defs.RestoreTableFromSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    newTableName = field("newTableName")
    snapshotName = field("snapshotName")
    sourceDatabaseName = field("sourceDatabaseName")
    sourceTableName = field("sourceTableName")
    workgroupName = field("workgroupName")
    activateCaseSensitiveIdentifier = field("activateCaseSensitiveIdentifier")
    sourceSchemaName = field("sourceSchemaName")
    targetDatabaseName = field("targetDatabaseName")
    targetSchemaName = field("targetSchemaName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTableFromSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleOutput:
    boto3_raw_data: "type_defs.ScheduleOutputTypeDef" = dataclasses.field()

    at = field("at")
    cron = field("cron")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTarget:
    boto3_raw_data: "type_defs.UpdateTargetTypeDef" = dataclasses.field()

    trackName = field("trackName")
    workgroupVersion = field("workgroupVersion")

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
class UpdateCustomDomainAssociationRequest:
    boto3_raw_data: "type_defs.UpdateCustomDomainAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomDomainAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomDomainAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointAccessRequest:
    boto3_raw_data: "type_defs.UpdateEndpointAccessRequestTypeDef" = dataclasses.field()

    endpointName = field("endpointName")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNamespaceRequest:
    boto3_raw_data: "type_defs.UpdateNamespaceRequestTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")
    adminPasswordSecretKmsKeyId = field("adminPasswordSecretKmsKeyId")
    adminUserPassword = field("adminUserPassword")
    adminUsername = field("adminUsername")
    defaultIamRoleArn = field("defaultIamRoleArn")
    iamRoles = field("iamRoles")
    kmsKeyId = field("kmsKeyId")
    logExports = field("logExports")
    manageAdminPassword = field("manageAdminPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotCopyConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateSnapshotCopyConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    snapshotCopyConfigurationId = field("snapshotCopyConfigurationId")
    snapshotRetentionPeriod = field("snapshotRetentionPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSnapshotCopyConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotCopyConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotRequest:
    boto3_raw_data: "type_defs.UpdateSnapshotRequestTypeDef" = dataclasses.field()

    snapshotName = field("snapshotName")
    retentionPeriod = field("retentionPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUsageLimitRequest:
    boto3_raw_data: "type_defs.UpdateUsageLimitRequestTypeDef" = dataclasses.field()

    usageLimitId = field("usageLimitId")
    amount = field("amount")
    breachAction = field("breachAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUsageLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUsageLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConvertRecoveryPointToSnapshotRequest:
    boto3_raw_data: "type_defs.ConvertRecoveryPointToSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    recoveryPointId = field("recoveryPointId")
    snapshotName = field("snapshotName")
    retentionPeriod = field("retentionPeriod")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConvertRecoveryPointToSnapshotRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConvertRecoveryPointToSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNamespaceRequest:
    boto3_raw_data: "type_defs.CreateNamespaceRequestTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")
    adminPasswordSecretKmsKeyId = field("adminPasswordSecretKmsKeyId")
    adminUserPassword = field("adminUserPassword")
    adminUsername = field("adminUsername")
    dbName = field("dbName")
    defaultIamRoleArn = field("defaultIamRoleArn")
    iamRoles = field("iamRoles")
    kmsKeyId = field("kmsKeyId")
    logExports = field("logExports")
    manageAdminPassword = field("manageAdminPassword")
    redshiftIdcApplicationArn = field("redshiftIdcApplicationArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNamespaceRequestTypeDef"]
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

    namespaceName = field("namespaceName")
    snapshotName = field("snapshotName")
    retentionPeriod = field("retentionPeriod")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateSnapshotScheduleActionParametersOutput:
    boto3_raw_data: "type_defs.CreateSnapshotScheduleActionParametersOutputTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    snapshotNamePrefix = field("snapshotNamePrefix")
    retentionPeriod = field("retentionPeriod")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSnapshotScheduleActionParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotScheduleActionParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotScheduleActionParameters:
    boto3_raw_data: "type_defs.CreateSnapshotScheduleActionParametersTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    snapshotNamePrefix = field("snapshotNamePrefix")
    retentionPeriod = field("retentionPeriod")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSnapshotScheduleActionParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotScheduleActionParametersTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateCustomDomainAssociationResponse:
    boto3_raw_data: "type_defs.CreateCustomDomainAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainCertificateExpiryTime = field("customDomainCertificateExpiryTime")
    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDomainAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDomainAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCredentialsResponse:
    boto3_raw_data: "type_defs.GetCredentialsResponseTypeDef" = dataclasses.field()

    dbPassword = field("dbPassword")
    dbUser = field("dbUser")
    expiration = field("expiration")
    nextRefreshTime = field("nextRefreshTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCredentialsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomDomainAssociationResponse:
    boto3_raw_data: "type_defs.GetCustomDomainAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainCertificateExpiryTime = field("customDomainCertificateExpiryTime")
    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCustomDomainAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomDomainAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomDomainAssociationsResponse:
    boto3_raw_data: "type_defs.ListCustomDomainAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def associations(self):  # pragma: no cover
        return Association.make_many(self.boto3_raw_data["associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomDomainAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomDomainAssociationsResponseTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class UpdateCustomDomainAssociationResponse:
    boto3_raw_data: "type_defs.UpdateCustomDomainAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainCertificateExpiryTime = field("customDomainCertificateExpiryTime")
    customDomainName = field("customDomainName")
    workgroupName = field("workgroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomDomainAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomDomainAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConvertRecoveryPointToSnapshotResponse:
    boto3_raw_data: "type_defs.ConvertRecoveryPointToSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConvertRecoveryPointToSnapshotResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConvertRecoveryPointToSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotResponse:
    boto3_raw_data: "type_defs.CreateSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotResponse:
    boto3_raw_data: "type_defs.DeleteSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSnapshotResponse:
    boto3_raw_data: "type_defs.GetSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotsResponse:
    boto3_raw_data: "type_defs.ListSnapshotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def snapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["snapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSnapshotsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotResponse:
    boto3_raw_data: "type_defs.UpdateSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def snapshot(self):  # pragma: no cover
        return Snapshot.make_one(self.boto3_raw_data["snapshot"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNamespaceResponse:
    boto3_raw_data: "type_defs.CreateNamespaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespace(self):  # pragma: no cover
        return Namespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNamespaceResponse:
    boto3_raw_data: "type_defs.DeleteNamespaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespace(self):  # pragma: no cover
        return Namespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNamespaceResponse:
    boto3_raw_data: "type_defs.GetNamespaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespace(self):  # pragma: no cover
        return Namespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamespacesResponse:
    boto3_raw_data: "type_defs.ListNamespacesResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespaces(self):  # pragma: no cover
        return Namespace.make_many(self.boto3_raw_data["namespaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNamespacesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamespacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreFromRecoveryPointResponse:
    boto3_raw_data: "type_defs.RestoreFromRecoveryPointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def namespace(self):  # pragma: no cover
        return Namespace.make_one(self.boto3_raw_data["namespace"])

    recoveryPointId = field("recoveryPointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreFromRecoveryPointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreFromRecoveryPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreFromSnapshotResponse:
    boto3_raw_data: "type_defs.RestoreFromSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespace(self):  # pragma: no cover
        return Namespace.make_one(self.boto3_raw_data["namespace"])

    ownerAccount = field("ownerAccount")
    snapshotName = field("snapshotName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreFromSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreFromSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNamespaceResponse:
    boto3_raw_data: "type_defs.UpdateNamespaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def namespace(self):  # pragma: no cover
        return Namespace.make_one(self.boto3_raw_data["namespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsRequest:
    boto3_raw_data: "type_defs.ListRecoveryPointsRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    maxResults = field("maxResults")
    namespaceArn = field("namespaceArn")
    namespaceName = field("namespaceName")
    nextToken = field("nextToken")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecoveryPointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotsRequest:
    boto3_raw_data: "type_defs.ListSnapshotsRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    maxResults = field("maxResults")
    namespaceArn = field("namespaceArn")
    namespaceName = field("namespaceName")
    nextToken = field("nextToken")
    ownerAccount = field("ownerAccount")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    at = field("at")
    cron = field("cron")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSnapshotCopyConfigurationResponse:
    boto3_raw_data: "type_defs.CreateSnapshotCopyConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def snapshotCopyConfiguration(self):  # pragma: no cover
        return SnapshotCopyConfiguration.make_one(
            self.boto3_raw_data["snapshotCopyConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSnapshotCopyConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSnapshotCopyConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSnapshotCopyConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteSnapshotCopyConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def snapshotCopyConfiguration(self):  # pragma: no cover
        return SnapshotCopyConfiguration.make_one(
            self.boto3_raw_data["snapshotCopyConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSnapshotCopyConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSnapshotCopyConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotCopyConfigurationsResponse:
    boto3_raw_data: "type_defs.ListSnapshotCopyConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def snapshotCopyConfigurations(self):  # pragma: no cover
        return SnapshotCopyConfiguration.make_many(
            self.boto3_raw_data["snapshotCopyConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSnapshotCopyConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotCopyConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSnapshotCopyConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateSnapshotCopyConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def snapshotCopyConfiguration(self):  # pragma: no cover
        return SnapshotCopyConfiguration.make_one(
            self.boto3_raw_data["snapshotCopyConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSnapshotCopyConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSnapshotCopyConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUsageLimitResponse:
    boto3_raw_data: "type_defs.CreateUsageLimitResponseTypeDef" = dataclasses.field()

    @cached_property
    def usageLimit(self):  # pragma: no cover
        return UsageLimit.make_one(self.boto3_raw_data["usageLimit"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUsageLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUsageLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUsageLimitResponse:
    boto3_raw_data: "type_defs.DeleteUsageLimitResponseTypeDef" = dataclasses.field()

    @cached_property
    def usageLimit(self):  # pragma: no cover
        return UsageLimit.make_one(self.boto3_raw_data["usageLimit"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUsageLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUsageLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageLimitResponse:
    boto3_raw_data: "type_defs.GetUsageLimitResponseTypeDef" = dataclasses.field()

    @cached_property
    def usageLimit(self):  # pragma: no cover
        return UsageLimit.make_one(self.boto3_raw_data["usageLimit"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageLimitsResponse:
    boto3_raw_data: "type_defs.ListUsageLimitsResponseTypeDef" = dataclasses.field()

    @cached_property
    def usageLimits(self):  # pragma: no cover
        return UsageLimit.make_many(self.boto3_raw_data["usageLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsageLimitsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageLimitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUsageLimitResponse:
    boto3_raw_data: "type_defs.UpdateUsageLimitResponseTypeDef" = dataclasses.field()

    @cached_property
    def usageLimit(self):  # pragma: no cover
        return UsageLimit.make_one(self.boto3_raw_data["usageLimit"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUsageLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUsageLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkgroupRequest:
    boto3_raw_data: "type_defs.CreateWorkgroupRequestTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")
    workgroupName = field("workgroupName")
    baseCapacity = field("baseCapacity")

    @cached_property
    def configParameters(self):  # pragma: no cover
        return ConfigParameter.make_many(self.boto3_raw_data["configParameters"])

    enhancedVpcRouting = field("enhancedVpcRouting")
    ipAddressType = field("ipAddressType")
    maxCapacity = field("maxCapacity")
    port = field("port")

    @cached_property
    def pricePerformanceTarget(self):  # pragma: no cover
        return PerformanceTarget.make_one(self.boto3_raw_data["pricePerformanceTarget"])

    publiclyAccessible = field("publiclyAccessible")
    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    trackName = field("trackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkgroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkgroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkgroupRequest:
    boto3_raw_data: "type_defs.UpdateWorkgroupRequestTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")
    baseCapacity = field("baseCapacity")

    @cached_property
    def configParameters(self):  # pragma: no cover
        return ConfigParameter.make_many(self.boto3_raw_data["configParameters"])

    enhancedVpcRouting = field("enhancedVpcRouting")
    ipAddressType = field("ipAddressType")
    maxCapacity = field("maxCapacity")
    port = field("port")

    @cached_property
    def pricePerformanceTarget(self):  # pragma: no cover
        return PerformanceTarget.make_one(self.boto3_raw_data["pricePerformanceTarget"])

    publiclyAccessible = field("publiclyAccessible")
    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")
    trackName = field("trackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkgroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkgroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecoveryPointResponse:
    boto3_raw_data: "type_defs.GetRecoveryPointResponseTypeDef" = dataclasses.field()

    @cached_property
    def recoveryPoint(self):  # pragma: no cover
        return RecoveryPoint.make_one(self.boto3_raw_data["recoveryPoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecoveryPointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecoveryPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsResponse:
    boto3_raw_data: "type_defs.ListRecoveryPointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def recoveryPoints(self):  # pragma: no cover
        return RecoveryPoint.make_many(self.boto3_raw_data["recoveryPoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecoveryPointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationOfferingResponse:
    boto3_raw_data: "type_defs.GetReservationOfferingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def reservationOffering(self):  # pragma: no cover
        return ReservationOffering.make_one(self.boto3_raw_data["reservationOffering"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReservationOfferingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationOfferingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationOfferingsResponse:
    boto3_raw_data: "type_defs.ListReservationOfferingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def reservationOfferingsList(self):  # pragma: no cover
        return ReservationOffering.make_many(
            self.boto3_raw_data["reservationOfferingsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReservationOfferingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationOfferingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Reservation:
    boto3_raw_data: "type_defs.ReservationTypeDef" = dataclasses.field()

    capacity = field("capacity")
    endDate = field("endDate")

    @cached_property
    def offering(self):  # pragma: no cover
        return ReservationOffering.make_one(self.boto3_raw_data["offering"])

    reservationArn = field("reservationArn")
    reservationId = field("reservationId")
    startDate = field("startDate")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReservationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReservationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def resourcePolicy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["resourcePolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
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

    @cached_property
    def resourcePolicy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["resourcePolicy"])

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
class GetTableRestoreStatusResponse:
    boto3_raw_data: "type_defs.GetTableRestoreStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tableRestoreStatus(self):  # pragma: no cover
        return TableRestoreStatus.make_one(self.boto3_raw_data["tableRestoreStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTableRestoreStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTableRestoreStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableRestoreStatusResponse:
    boto3_raw_data: "type_defs.ListTableRestoreStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tableRestoreStatuses(self):  # pragma: no cover
        return TableRestoreStatus.make_many(self.boto3_raw_data["tableRestoreStatuses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTableRestoreStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableRestoreStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromRecoveryPointResponse:
    boto3_raw_data: "type_defs.RestoreTableFromRecoveryPointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tableRestoreStatus(self):  # pragma: no cover
        return TableRestoreStatus.make_one(self.boto3_raw_data["tableRestoreStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreTableFromRecoveryPointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromRecoveryPointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreTableFromSnapshotResponse:
    boto3_raw_data: "type_defs.RestoreTableFromSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tableRestoreStatus(self):  # pragma: no cover
        return TableRestoreStatus.make_one(self.boto3_raw_data["tableRestoreStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreTableFromSnapshotResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreTableFromSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomDomainAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomDomainAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainName = field("customDomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomDomainAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomDomainAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointAccessRequestPaginate:
    boto3_raw_data: "type_defs.ListEndpointAccessRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ownerAccount = field("ownerAccount")
    vpcId = field("vpcId")
    workgroupName = field("workgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEndpointAccessRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointAccessRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedWorkgroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedWorkgroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sourceArn = field("sourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedWorkgroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedWorkgroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNamespacesRequestPaginate:
    boto3_raw_data: "type_defs.ListNamespacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNamespacesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNamespacesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecoveryPointsRequestPaginate:
    boto3_raw_data: "type_defs.ListRecoveryPointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    endTime = field("endTime")
    namespaceArn = field("namespaceArn")
    namespaceName = field("namespaceName")
    startTime = field("startTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRecoveryPointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecoveryPointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationOfferingsRequestPaginate:
    boto3_raw_data: "type_defs.ListReservationOfferingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReservationOfferingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationOfferingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsRequestPaginate:
    boto3_raw_data: "type_defs.ListReservationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReservationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListScheduledActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListScheduledActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotCopyConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListSnapshotCopyConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSnapshotCopyConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotCopyConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.ListSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    endTime = field("endTime")
    namespaceArn = field("namespaceArn")
    namespaceName = field("namespaceName")
    ownerAccount = field("ownerAccount")
    startTime = field("startTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSnapshotsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTableRestoreStatusRequestPaginate:
    boto3_raw_data: "type_defs.ListTableRestoreStatusRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    workgroupName = field("workgroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTableRestoreStatusRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTableRestoreStatusRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTracksRequestPaginate:
    boto3_raw_data: "type_defs.ListTracksRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTracksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTracksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageLimitsRequestPaginate:
    boto3_raw_data: "type_defs.ListUsageLimitsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    usageType = field("usageType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUsageLimitsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageLimitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkgroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkgroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ownerAccount = field("ownerAccount")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkgroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkgroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedWorkgroupsResponse:
    boto3_raw_data: "type_defs.ListManagedWorkgroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managedWorkgroups(self):  # pragma: no cover
        return ManagedWorkgroupListItem.make_many(
            self.boto3_raw_data["managedWorkgroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListManagedWorkgroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedWorkgroupsResponseTypeDef"]
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
    def scheduledActions(self):  # pragma: no cover
        return ScheduledActionAssociation.make_many(
            self.boto3_raw_data["scheduledActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class VpcEndpoint:
    boto3_raw_data: "type_defs.VpcEndpointTypeDef" = dataclasses.field()

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    vpcEndpointId = field("vpcEndpointId")
    vpcId = field("vpcId")

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
class ServerlessTrack:
    boto3_raw_data: "type_defs.ServerlessTrackTypeDef" = dataclasses.field()

    trackName = field("trackName")

    @cached_property
    def updateTargets(self):  # pragma: no cover
        return UpdateTarget.make_many(self.boto3_raw_data["updateTargets"])

    workgroupVersion = field("workgroupVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerlessTrackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerlessTrackTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetActionOutput:
    boto3_raw_data: "type_defs.TargetActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def createSnapshot(self):  # pragma: no cover
        return CreateSnapshotScheduleActionParametersOutput.make_one(
            self.boto3_raw_data["createSnapshot"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetAction:
    boto3_raw_data: "type_defs.TargetActionTypeDef" = dataclasses.field()

    @cached_property
    def createSnapshot(self):  # pragma: no cover
        return CreateSnapshotScheduleActionParameters.make_one(
            self.boto3_raw_data["createSnapshot"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReservationResponse:
    boto3_raw_data: "type_defs.CreateReservationResponseTypeDef" = dataclasses.field()

    @cached_property
    def reservation(self):  # pragma: no cover
        return Reservation.make_one(self.boto3_raw_data["reservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReservationResponse:
    boto3_raw_data: "type_defs.GetReservationResponseTypeDef" = dataclasses.field()

    @cached_property
    def reservation(self):  # pragma: no cover
        return Reservation.make_one(self.boto3_raw_data["reservation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetReservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReservationsResponse:
    boto3_raw_data: "type_defs.ListReservationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def reservationsList(self):  # pragma: no cover
        return Reservation.make_many(self.boto3_raw_data["reservationsList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReservationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReservationsResponseTypeDef"]
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

    address = field("address")
    endpointArn = field("endpointArn")
    endpointCreateTime = field("endpointCreateTime")
    endpointName = field("endpointName")
    endpointStatus = field("endpointStatus")
    port = field("port")
    subnetIds = field("subnetIds")

    @cached_property
    def vpcEndpoint(self):  # pragma: no cover
        return VpcEndpoint.make_one(self.boto3_raw_data["vpcEndpoint"])

    @cached_property
    def vpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["vpcSecurityGroups"]
        )

    workgroupName = field("workgroupName")

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

    address = field("address")
    port = field("port")

    @cached_property
    def vpcEndpoints(self):  # pragma: no cover
        return VpcEndpoint.make_many(self.boto3_raw_data["vpcEndpoints"])

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
class GetTrackResponse:
    boto3_raw_data: "type_defs.GetTrackResponseTypeDef" = dataclasses.field()

    @cached_property
    def track(self):  # pragma: no cover
        return ServerlessTrack.make_one(self.boto3_raw_data["track"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTrackResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTracksResponse:
    boto3_raw_data: "type_defs.ListTracksResponseTypeDef" = dataclasses.field()

    @cached_property
    def tracks(self):  # pragma: no cover
        return ServerlessTrack.make_many(self.boto3_raw_data["tracks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTracksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTracksResponseTypeDef"]
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

    endTime = field("endTime")
    namespaceName = field("namespaceName")
    nextInvocations = field("nextInvocations")
    roleArn = field("roleArn")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleOutput.make_one(self.boto3_raw_data["schedule"])

    scheduledActionDescription = field("scheduledActionDescription")
    scheduledActionName = field("scheduledActionName")
    scheduledActionUuid = field("scheduledActionUuid")
    startTime = field("startTime")
    state = field("state")

    @cached_property
    def targetAction(self):  # pragma: no cover
        return TargetActionOutput.make_one(self.boto3_raw_data["targetAction"])

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
class CreateEndpointAccessResponse:
    boto3_raw_data: "type_defs.CreateEndpointAccessResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def endpoint(self):  # pragma: no cover
        return EndpointAccess.make_one(self.boto3_raw_data["endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointAccessResponse:
    boto3_raw_data: "type_defs.DeleteEndpointAccessResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def endpoint(self):  # pragma: no cover
        return EndpointAccess.make_one(self.boto3_raw_data["endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEndpointAccessResponse:
    boto3_raw_data: "type_defs.GetEndpointAccessResponseTypeDef" = dataclasses.field()

    @cached_property
    def endpoint(self):  # pragma: no cover
        return EndpointAccess.make_one(self.boto3_raw_data["endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEndpointAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointAccessResponse:
    boto3_raw_data: "type_defs.ListEndpointAccessResponseTypeDef" = dataclasses.field()

    @cached_property
    def endpoints(self):  # pragma: no cover
        return EndpointAccess.make_many(self.boto3_raw_data["endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointAccessResponse:
    boto3_raw_data: "type_defs.UpdateEndpointAccessResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def endpoint(self):  # pragma: no cover
        return EndpointAccess.make_one(self.boto3_raw_data["endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointAccessResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Workgroup:
    boto3_raw_data: "type_defs.WorkgroupTypeDef" = dataclasses.field()

    baseCapacity = field("baseCapacity")

    @cached_property
    def configParameters(self):  # pragma: no cover
        return ConfigParameter.make_many(self.boto3_raw_data["configParameters"])

    creationDate = field("creationDate")
    crossAccountVpcs = field("crossAccountVpcs")
    customDomainCertificateArn = field("customDomainCertificateArn")
    customDomainCertificateExpiryTime = field("customDomainCertificateExpiryTime")
    customDomainName = field("customDomainName")

    @cached_property
    def endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["endpoint"])

    enhancedVpcRouting = field("enhancedVpcRouting")
    ipAddressType = field("ipAddressType")
    maxCapacity = field("maxCapacity")
    namespaceName = field("namespaceName")
    patchVersion = field("patchVersion")
    pendingTrackName = field("pendingTrackName")
    port = field("port")

    @cached_property
    def pricePerformanceTarget(self):  # pragma: no cover
        return PerformanceTarget.make_one(self.boto3_raw_data["pricePerformanceTarget"])

    publiclyAccessible = field("publiclyAccessible")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    subnetIds = field("subnetIds")
    trackName = field("trackName")
    workgroupArn = field("workgroupArn")
    workgroupId = field("workgroupId")
    workgroupName = field("workgroupName")
    workgroupVersion = field("workgroupVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkgroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkgroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduledActionResponse:
    boto3_raw_data: "type_defs.CreateScheduledActionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def scheduledAction(self):  # pragma: no cover
        return ScheduledActionResponse.make_one(self.boto3_raw_data["scheduledAction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateScheduledActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduledActionResponse:
    boto3_raw_data: "type_defs.DeleteScheduledActionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def scheduledAction(self):  # pragma: no cover
        return ScheduledActionResponse.make_one(self.boto3_raw_data["scheduledAction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteScheduledActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScheduledActionResponse:
    boto3_raw_data: "type_defs.GetScheduledActionResponseTypeDef" = dataclasses.field()

    @cached_property
    def scheduledAction(self):  # pragma: no cover
        return ScheduledActionResponse.make_one(self.boto3_raw_data["scheduledAction"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetScheduledActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetScheduledActionResponseTypeDef"]
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
    def scheduledAction(self):  # pragma: no cover
        return ScheduledActionResponse.make_one(self.boto3_raw_data["scheduledAction"])

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
class CreateScheduledActionRequest:
    boto3_raw_data: "type_defs.CreateScheduledActionRequestTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    roleArn = field("roleArn")
    schedule = field("schedule")
    scheduledActionName = field("scheduledActionName")
    targetAction = field("targetAction")
    enabled = field("enabled")
    endTime = field("endTime")
    scheduledActionDescription = field("scheduledActionDescription")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduledActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledActionRequestTypeDef"]
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

    scheduledActionName = field("scheduledActionName")
    enabled = field("enabled")
    endTime = field("endTime")
    roleArn = field("roleArn")
    schedule = field("schedule")
    scheduledActionDescription = field("scheduledActionDescription")
    startTime = field("startTime")
    targetAction = field("targetAction")

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
class CreateWorkgroupResponse:
    boto3_raw_data: "type_defs.CreateWorkgroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def workgroup(self):  # pragma: no cover
        return Workgroup.make_one(self.boto3_raw_data["workgroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkgroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkgroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkgroupResponse:
    boto3_raw_data: "type_defs.DeleteWorkgroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def workgroup(self):  # pragma: no cover
        return Workgroup.make_one(self.boto3_raw_data["workgroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkgroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkgroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkgroupResponse:
    boto3_raw_data: "type_defs.GetWorkgroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def workgroup(self):  # pragma: no cover
        return Workgroup.make_one(self.boto3_raw_data["workgroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkgroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkgroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkgroupsResponse:
    boto3_raw_data: "type_defs.ListWorkgroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def workgroups(self):  # pragma: no cover
        return Workgroup.make_many(self.boto3_raw_data["workgroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkgroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkgroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkgroupResponse:
    boto3_raw_data: "type_defs.UpdateWorkgroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def workgroup(self):  # pragma: no cover
        return Workgroup.make_one(self.boto3_raw_data["workgroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkgroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkgroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
