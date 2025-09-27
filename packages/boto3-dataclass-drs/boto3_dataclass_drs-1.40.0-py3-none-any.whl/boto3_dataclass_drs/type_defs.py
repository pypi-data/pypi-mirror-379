# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_drs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    accountID = field("accountID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSourceNetworkStackRequest:
    boto3_raw_data: "type_defs.AssociateSourceNetworkStackRequestTypeDef" = (
        dataclasses.field()
    )

    cfnStackName = field("cfnStackName")
    sourceNetworkID = field("sourceNetworkID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateSourceNetworkStackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSourceNetworkStackRequestTypeDef"]
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
class CPU:
    boto3_raw_data: "type_defs.CPUTypeDef" = dataclasses.field()

    cores = field("cores")
    modelName = field("modelName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CPUTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CPUTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductCode:
    boto3_raw_data: "type_defs.ProductCodeTypeDef" = dataclasses.field()

    productCodeId = field("productCodeId")
    productCodeMode = field("productCodeMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProductCodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProductCodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExtendedSourceServerRequest:
    boto3_raw_data: "type_defs.CreateExtendedSourceServerRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerArn = field("sourceServerArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExtendedSourceServerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExtendedSourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Licensing:
    boto3_raw_data: "type_defs.LicensingTypeDef" = dataclasses.field()

    osByol = field("osByol")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicensingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicensingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PITPolicyRule:
    boto3_raw_data: "type_defs.PITPolicyRuleTypeDef" = dataclasses.field()

    interval = field("interval")
    retentionDuration = field("retentionDuration")
    units = field("units")
    enabled = field("enabled")
    ruleID = field("ruleID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PITPolicyRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PITPolicyRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSourceNetworkRequest:
    boto3_raw_data: "type_defs.CreateSourceNetworkRequestTypeDef" = dataclasses.field()

    originAccountID = field("originAccountID")
    originRegion = field("originRegion")
    vpcID = field("vpcID")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSourceNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSourceNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationError:
    boto3_raw_data: "type_defs.DataReplicationErrorTypeDef" = dataclasses.field()

    error = field("error")
    rawError = field("rawError")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInfoReplicatedDisk:
    boto3_raw_data: "type_defs.DataReplicationInfoReplicatedDiskTypeDef" = (
        dataclasses.field()
    )

    backloggedStorageBytes = field("backloggedStorageBytes")
    deviceName = field("deviceName")
    replicatedStorageBytes = field("replicatedStorageBytes")
    rescannedStorageBytes = field("rescannedStorageBytes")
    totalStorageBytes = field("totalStorageBytes")
    volumeStatus = field("volumeStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataReplicationInfoReplicatedDiskTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInfoReplicatedDiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInitiationStep:
    boto3_raw_data: "type_defs.DataReplicationInitiationStepTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataReplicationInitiationStepTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInitiationStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobRequest:
    boto3_raw_data: "type_defs.DeleteJobRequestTypeDef" = dataclasses.field()

    jobID = field("jobID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLaunchActionRequest:
    boto3_raw_data: "type_defs.DeleteLaunchActionRequestTypeDef" = dataclasses.field()

    actionId = field("actionId")
    resourceId = field("resourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLaunchActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLaunchActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLaunchConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.DeleteLaunchConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteLaunchConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLaunchConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecoveryInstanceRequest:
    boto3_raw_data: "type_defs.DeleteRecoveryInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    recoveryInstanceID = field("recoveryInstanceID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRecoveryInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecoveryInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.DeleteReplicationConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSourceNetworkRequest:
    boto3_raw_data: "type_defs.DeleteSourceNetworkRequestTypeDef" = dataclasses.field()

    sourceNetworkID = field("sourceNetworkID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSourceNetworkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSourceNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSourceServerRequest:
    boto3_raw_data: "type_defs.DeleteSourceServerRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSourceServerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSourceServerRequestTypeDef"]
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
class DescribeJobLogItemsRequest:
    boto3_raw_data: "type_defs.DescribeJobLogItemsRequestTypeDef" = dataclasses.field()

    jobID = field("jobID")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobLogItemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobLogItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequestFilters:
    boto3_raw_data: "type_defs.DescribeJobsRequestFiltersTypeDef" = dataclasses.field()

    fromDate = field("fromDate")
    jobIDs = field("jobIDs")
    toDate = field("toDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLaunchConfigurationTemplatesRequest:
    boto3_raw_data: "type_defs.DescribeLaunchConfigurationTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateIDs = field("launchConfigurationTemplateIDs")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLaunchConfigurationTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLaunchConfigurationTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoveryInstancesRequestFilters:
    boto3_raw_data: "type_defs.DescribeRecoveryInstancesRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    recoveryInstanceIDs = field("recoveryInstanceIDs")
    sourceServerIDs = field("sourceServerIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecoveryInstancesRequestFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoveryInstancesRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoverySnapshotsRequestFilters:
    boto3_raw_data: "type_defs.DescribeRecoverySnapshotsRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    fromDateTime = field("fromDateTime")
    toDateTime = field("toDateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecoverySnapshotsRequestFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoverySnapshotsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoverySnapshot:
    boto3_raw_data: "type_defs.RecoverySnapshotTypeDef" = dataclasses.field()

    expectedTimestamp = field("expectedTimestamp")
    snapshotID = field("snapshotID")
    sourceServerID = field("sourceServerID")
    ebsSnapshots = field("ebsSnapshots")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecoverySnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoverySnapshotTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationTemplatesRequest:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationTemplatesRequestTypeDef"
    ) = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    replicationConfigurationTemplateIDs = field("replicationConfigurationTemplateIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationTemplatesRequestTypeDef"
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
                "type_defs.DescribeReplicationConfigurationTemplatesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceNetworksRequestFilters:
    boto3_raw_data: "type_defs.DescribeSourceNetworksRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    originAccountID = field("originAccountID")
    originRegion = field("originRegion")
    sourceNetworkIDs = field("sourceNetworkIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSourceNetworksRequestFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceNetworksRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersRequestFilters:
    boto3_raw_data: "type_defs.DescribeSourceServersRequestFiltersTypeDef" = (
        dataclasses.field()
    )

    hardwareId = field("hardwareId")
    sourceServerIDs = field("sourceServerIDs")
    stagingAccountIDs = field("stagingAccountIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSourceServersRequestFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectRecoveryInstanceRequest:
    boto3_raw_data: "type_defs.DisconnectRecoveryInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    recoveryInstanceID = field("recoveryInstanceID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisconnectRecoveryInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectRecoveryInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectSourceServerRequest:
    boto3_raw_data: "type_defs.DisconnectSourceServerRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisconnectSourceServerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectSourceServerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Disk:
    boto3_raw_data: "type_defs.DiskTypeDef" = dataclasses.field()

    bytes = field("bytes")
    deviceName = field("deviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DiskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DiskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceNetworkData:
    boto3_raw_data: "type_defs.SourceNetworkDataTypeDef" = dataclasses.field()

    sourceNetworkID = field("sourceNetworkID")
    sourceVpc = field("sourceVpc")
    stackName = field("stackName")
    targetVpc = field("targetVpc")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceNetworkDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceNetworkDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSourceNetworkCfnTemplateRequest:
    boto3_raw_data: "type_defs.ExportSourceNetworkCfnTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    sourceNetworkID = field("sourceNetworkID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportSourceNetworkCfnTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSourceNetworkCfnTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFailbackReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.GetFailbackReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    recoveryInstanceID = field("recoveryInstanceID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFailbackReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFailbackReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.GetLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLaunchConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.GetReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentificationHints:
    boto3_raw_data: "type_defs.IdentificationHintsTypeDef" = dataclasses.field()

    awsInstanceID = field("awsInstanceID")
    fqdn = field("fqdn")
    hostname = field("hostname")
    vmWareUuid = field("vmWareUuid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentificationHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentificationHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchActionParameter:
    boto3_raw_data: "type_defs.LaunchActionParameterTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchActionParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchActionParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchActionsRequestFilters:
    boto3_raw_data: "type_defs.LaunchActionsRequestFiltersTypeDef" = dataclasses.field()

    actionIds = field("actionIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchActionsRequestFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchActionsRequestFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchIntoInstanceProperties:
    boto3_raw_data: "type_defs.LaunchIntoInstancePropertiesTypeDef" = (
        dataclasses.field()
    )

    launchIntoEC2InstanceID = field("launchIntoEC2InstanceID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchIntoInstancePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchIntoInstancePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastLaunchInitiated:
    boto3_raw_data: "type_defs.LifeCycleLastLaunchInitiatedTypeDef" = (
        dataclasses.field()
    )

    apiCallDateTime = field("apiCallDateTime")
    jobID = field("jobID")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastLaunchInitiatedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastLaunchInitiatedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExtensibleSourceServersRequest:
    boto3_raw_data: "type_defs.ListExtensibleSourceServersRequestTypeDef" = (
        dataclasses.field()
    )

    stagingAccountID = field("stagingAccountID")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExtensibleSourceServersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensibleSourceServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StagingSourceServer:
    boto3_raw_data: "type_defs.StagingSourceServerTypeDef" = dataclasses.field()

    arn = field("arn")
    hostname = field("hostname")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StagingSourceServerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StagingSourceServerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStagingAccountsRequest:
    boto3_raw_data: "type_defs.ListStagingAccountsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStagingAccountsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStagingAccountsRequestTypeDef"]
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
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    ips = field("ips")
    isPrimary = field("isPrimary")
    macAddress = field("macAddress")

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
class OS:
    boto3_raw_data: "type_defs.OSTypeDef" = dataclasses.field()

    fullString = field("fullString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OSTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OSTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingResourceID:
    boto3_raw_data: "type_defs.ParticipatingResourceIDTypeDef" = dataclasses.field()

    sourceNetworkID = field("sourceNetworkID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipatingResourceIDTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingResourceIDTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceDataReplicationError:
    boto3_raw_data: "type_defs.RecoveryInstanceDataReplicationErrorTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    rawError = field("rawError")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecoveryInstanceDataReplicationErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceDataReplicationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceDataReplicationInfoReplicatedDisk:
    boto3_raw_data: (
        "type_defs.RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef"
    ) = dataclasses.field()

    backloggedStorageBytes = field("backloggedStorageBytes")
    deviceName = field("deviceName")
    replicatedStorageBytes = field("replicatedStorageBytes")
    rescannedStorageBytes = field("rescannedStorageBytes")
    totalStorageBytes = field("totalStorageBytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef"
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
                "type_defs.RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceDataReplicationInitiationStep:
    boto3_raw_data: "type_defs.RecoveryInstanceDataReplicationInitiationStepTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecoveryInstanceDataReplicationInitiationStepTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceDataReplicationInitiationStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceDisk:
    boto3_raw_data: "type_defs.RecoveryInstanceDiskTypeDef" = dataclasses.field()

    bytes = field("bytes")
    ebsVolumeID = field("ebsVolumeID")
    internalDeviceName = field("internalDeviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryInstanceDiskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceDiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceFailback:
    boto3_raw_data: "type_defs.RecoveryInstanceFailbackTypeDef" = dataclasses.field()

    agentLastSeenByServiceDateTime = field("agentLastSeenByServiceDateTime")
    elapsedReplicationDuration = field("elapsedReplicationDuration")
    failbackClientID = field("failbackClientID")
    failbackClientLastSeenByServiceDateTime = field(
        "failbackClientLastSeenByServiceDateTime"
    )
    failbackInitiationTime = field("failbackInitiationTime")
    failbackJobID = field("failbackJobID")
    failbackLaunchType = field("failbackLaunchType")
    failbackToOriginalServer = field("failbackToOriginalServer")
    firstByteDateTime = field("firstByteDateTime")
    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryInstanceFailbackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceFailbackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryLifeCycle:
    boto3_raw_data: "type_defs.RecoveryLifeCycleTypeDef" = dataclasses.field()

    apiCallDateTime = field("apiCallDateTime")
    jobID = field("jobID")
    lastRecoveryResult = field("lastRecoveryResult")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecoveryLifeCycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryLifeCycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationReplicatedDisk:
    boto3_raw_data: "type_defs.ReplicationConfigurationReplicatedDiskTypeDef" = (
        dataclasses.field()
    )

    deviceName = field("deviceName")
    iops = field("iops")
    isBootDisk = field("isBootDisk")
    optimizedStagingDiskType = field("optimizedStagingDiskType")
    stagingDiskType = field("stagingDiskType")
    throughput = field("throughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationConfigurationReplicatedDiskTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationReplicatedDiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryDataReplicationRequest:
    boto3_raw_data: "type_defs.RetryDataReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryDataReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryDataReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReverseReplicationRequest:
    boto3_raw_data: "type_defs.ReverseReplicationRequestTypeDef" = dataclasses.field()

    recoveryInstanceID = field("recoveryInstanceID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCloudProperties:
    boto3_raw_data: "type_defs.SourceCloudPropertiesTypeDef" = dataclasses.field()

    originAccountID = field("originAccountID")
    originAvailabilityZone = field("originAvailabilityZone")
    originRegion = field("originRegion")
    sourceOutpostArn = field("sourceOutpostArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceCloudPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceCloudPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StagingArea:
    boto3_raw_data: "type_defs.StagingAreaTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")
    stagingAccountID = field("stagingAccountID")
    stagingSourceServerArn = field("stagingSourceServerArn")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StagingAreaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StagingAreaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFailbackLaunchRequest:
    boto3_raw_data: "type_defs.StartFailbackLaunchRequestTypeDef" = dataclasses.field()

    recoveryInstanceIDs = field("recoveryInstanceIDs")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFailbackLaunchRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFailbackLaunchRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecoveryRequestSourceServer:
    boto3_raw_data: "type_defs.StartRecoveryRequestSourceServerTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    recoverySnapshotID = field("recoverySnapshotID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRecoveryRequestSourceServerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecoveryRequestSourceServerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationRequest:
    boto3_raw_data: "type_defs.StartReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSourceNetworkRecoveryRequestNetworkEntry:
    boto3_raw_data: "type_defs.StartSourceNetworkRecoveryRequestNetworkEntryTypeDef" = (
        dataclasses.field()
    )

    sourceNetworkID = field("sourceNetworkID")
    cfnStackName = field("cfnStackName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSourceNetworkRecoveryRequestNetworkEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSourceNetworkRecoveryRequestNetworkEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSourceNetworkReplicationRequest:
    boto3_raw_data: "type_defs.StartSourceNetworkReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceNetworkID = field("sourceNetworkID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSourceNetworkReplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSourceNetworkReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFailbackRequest:
    boto3_raw_data: "type_defs.StopFailbackRequestTypeDef" = dataclasses.field()

    recoveryInstanceID = field("recoveryInstanceID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopFailbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFailbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationRequest:
    boto3_raw_data: "type_defs.StopReplicationRequestTypeDef" = dataclasses.field()

    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSourceNetworkReplicationRequest:
    boto3_raw_data: "type_defs.StopSourceNetworkReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceNetworkID = field("sourceNetworkID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopSourceNetworkReplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSourceNetworkReplicationRequestTypeDef"]
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
class TerminateRecoveryInstancesRequest:
    boto3_raw_data: "type_defs.TerminateRecoveryInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    recoveryInstanceIDs = field("recoveryInstanceIDs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TerminateRecoveryInstancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateRecoveryInstancesRequestTypeDef"]
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
class UpdateFailbackReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateFailbackReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    recoveryInstanceID = field("recoveryInstanceID")
    bandwidthThrottling = field("bandwidthThrottling")
    name = field("name")
    usePrivateIP = field("usePrivateIP")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFailbackReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFailbackReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSourceNetworkResponse:
    boto3_raw_data: "type_defs.CreateSourceNetworkResponseTypeDef" = dataclasses.field()

    sourceNetworkID = field("sourceNetworkID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSourceNetworkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSourceNetworkResponseTypeDef"]
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
class ExportSourceNetworkCfnTemplateResponse:
    boto3_raw_data: "type_defs.ExportSourceNetworkCfnTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    s3DestinationUrl = field("s3DestinationUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportSourceNetworkCfnTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSourceNetworkCfnTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFailbackReplicationConfigurationResponse:
    boto3_raw_data: "type_defs.GetFailbackReplicationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    bandwidthThrottling = field("bandwidthThrottling")
    name = field("name")
    recoveryInstanceID = field("recoveryInstanceID")
    usePrivateIP = field("usePrivateIP")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFailbackReplicationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFailbackReplicationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStagingAccountsResponse:
    boto3_raw_data: "type_defs.ListStagingAccountsResponseTypeDef" = dataclasses.field()

    @cached_property
    def accounts(self):  # pragma: no cover
        return Account.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStagingAccountsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStagingAccountsResponseTypeDef"]
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
class ReverseReplicationResponse:
    boto3_raw_data: "type_defs.ReverseReplicationResponseTypeDef" = dataclasses.field()

    reversedDirectionSourceServerArn = field("reversedDirectionSourceServerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseReplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversionProperties:
    boto3_raw_data: "type_defs.ConversionPropertiesTypeDef" = dataclasses.field()

    dataTimestamp = field("dataTimestamp")
    forceUefi = field("forceUefi")
    rootVolumeName = field("rootVolumeName")
    volumeToConversionMap = field("volumeToConversionMap")
    volumeToProductCodes = field("volumeToProductCodes")
    volumeToVolumeSize = field("volumeToVolumeSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversionPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLaunchConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.CreateLaunchConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    exportBucketArn = field("exportBucketArn")
    launchDisposition = field("launchDisposition")
    launchIntoSourceInstance = field("launchIntoSourceInstance")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    postLaunchEnabled = field("postLaunchEnabled")
    tags = field("tags")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLaunchConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLaunchConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfigurationTemplate:
    boto3_raw_data: "type_defs.LaunchConfigurationTemplateTypeDef" = dataclasses.field()

    arn = field("arn")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    exportBucketArn = field("exportBucketArn")
    launchConfigurationTemplateID = field("launchConfigurationTemplateID")
    launchDisposition = field("launchDisposition")
    launchIntoSourceInstance = field("launchIntoSourceInstance")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    postLaunchEnabled = field("postLaunchEnabled")
    tags = field("tags")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.UpdateLaunchConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    launchConfigurationTemplateID = field("launchConfigurationTemplateID")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    exportBucketArn = field("exportBucketArn")
    launchDisposition = field("launchDisposition")
    launchIntoSourceInstance = field("launchIntoSourceInstance")

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    postLaunchEnabled = field("postLaunchEnabled")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLaunchConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.CreateReplicationConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")

    @cached_property
    def pitPolicy(self):  # pragma: no cover
        return PITPolicyRule.make_many(self.boto3_raw_data["pitPolicy"])

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")
    autoReplicateNewDisks = field("autoReplicateNewDisks")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationTemplateResponse:
    boto3_raw_data: "type_defs.ReplicationConfigurationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    autoReplicateNewDisks = field("autoReplicateNewDisks")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")

    @cached_property
    def pitPolicy(self):  # pragma: no cover
        return PITPolicyRule.make_many(self.boto3_raw_data["pitPolicy"])

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")
    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    tags = field("tags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationConfigurationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationTemplate:
    boto3_raw_data: "type_defs.ReplicationConfigurationTemplateTypeDef" = (
        dataclasses.field()
    )

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")
    arn = field("arn")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    autoReplicateNewDisks = field("autoReplicateNewDisks")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")

    @cached_property
    def pitPolicy(self):  # pragma: no cover
        return PITPolicyRule.make_many(self.boto3_raw_data["pitPolicy"])

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    tags = field("tags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReplicationConfigurationTemplateRequest:
    boto3_raw_data: "type_defs.UpdateReplicationConfigurationTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    replicationConfigurationTemplateID = field("replicationConfigurationTemplateID")
    arn = field("arn")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    autoReplicateNewDisks = field("autoReplicateNewDisks")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")

    @cached_property
    def pitPolicy(self):  # pragma: no cover
        return PITPolicyRule.make_many(self.boto3_raw_data["pitPolicy"])

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReplicationConfigurationTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationConfigurationTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInitiation:
    boto3_raw_data: "type_defs.DataReplicationInitiationTypeDef" = dataclasses.field()

    nextAttemptDateTime = field("nextAttemptDateTime")
    startDateTime = field("startDateTime")

    @cached_property
    def steps(self):  # pragma: no cover
        return DataReplicationInitiationStep.make_many(self.boto3_raw_data["steps"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationInitiationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInitiationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobLogItemsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeJobLogItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    jobID = field("jobID")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeJobLogItemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobLogItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLaunchConfigurationTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    launchConfigurationTemplateIDs = field("launchConfigurationTemplateIDs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef"
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
                "type_defs.DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    replicationConfigurationTemplateIDs = field("replicationConfigurationTemplateIDs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef"
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
                "type_defs.DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExtensibleSourceServersRequestPaginate:
    boto3_raw_data: "type_defs.ListExtensibleSourceServersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    stagingAccountID = field("stagingAccountID")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExtensibleSourceServersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensibleSourceServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStagingAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListStagingAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStagingAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStagingAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeJobsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeJobsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequest:
    boto3_raw_data: "type_defs.DescribeJobsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeJobsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoveryInstancesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRecoveryInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeRecoveryInstancesRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecoveryInstancesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoveryInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoveryInstancesRequest:
    boto3_raw_data: "type_defs.DescribeRecoveryInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeRecoveryInstancesRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRecoveryInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoveryInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoverySnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRecoverySnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeRecoverySnapshotsRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    order = field("order")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecoverySnapshotsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoverySnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoverySnapshotsRequest:
    boto3_raw_data: "type_defs.DescribeRecoverySnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeRecoverySnapshotsRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    order = field("order")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRecoverySnapshotsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoverySnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoverySnapshotsResponse:
    boto3_raw_data: "type_defs.DescribeRecoverySnapshotsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return RecoverySnapshot.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecoverySnapshotsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoverySnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceNetworksRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSourceNetworksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeSourceNetworksRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSourceNetworksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceNetworksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceNetworksRequest:
    boto3_raw_data: "type_defs.DescribeSourceNetworksRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeSourceNetworksRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSourceNetworksRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceNetworksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSourceServersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeSourceServersRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSourceServersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersRequest:
    boto3_raw_data: "type_defs.DescribeSourceServersRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return DescribeSourceServersRequestFilters.make_one(
            self.boto3_raw_data["filters"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSourceServersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventResourceData:
    boto3_raw_data: "type_defs.EventResourceDataTypeDef" = dataclasses.field()

    @cached_property
    def sourceNetworkData(self):  # pragma: no cover
        return SourceNetworkData.make_one(self.boto3_raw_data["sourceNetworkData"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventResourceDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventResourceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchAction:
    boto3_raw_data: "type_defs.LaunchActionTypeDef" = dataclasses.field()

    actionCode = field("actionCode")
    actionId = field("actionId")
    actionVersion = field("actionVersion")
    active = field("active")
    category = field("category")
    description = field("description")
    name = field("name")
    optional = field("optional")
    order = field("order")
    parameters = field("parameters")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLaunchActionRequest:
    boto3_raw_data: "type_defs.PutLaunchActionRequestTypeDef" = dataclasses.field()

    actionCode = field("actionCode")
    actionId = field("actionId")
    actionVersion = field("actionVersion")
    active = field("active")
    category = field("category")
    description = field("description")
    name = field("name")
    optional = field("optional")
    order = field("order")
    resourceId = field("resourceId")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLaunchActionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLaunchActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLaunchActionResponse:
    boto3_raw_data: "type_defs.PutLaunchActionResponseTypeDef" = dataclasses.field()

    actionCode = field("actionCode")
    actionId = field("actionId")
    actionVersion = field("actionVersion")
    active = field("active")
    category = field("category")
    description = field("description")
    name = field("name")
    optional = field("optional")
    order = field("order")
    parameters = field("parameters")
    resourceId = field("resourceId")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLaunchActionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLaunchActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLaunchActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceId = field("resourceId")

    @cached_property
    def filters(self):  # pragma: no cover
        return LaunchActionsRequestFilters.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLaunchActionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchActionsRequest:
    boto3_raw_data: "type_defs.ListLaunchActionsRequestTypeDef" = dataclasses.field()

    resourceId = field("resourceId")

    @cached_property
    def filters(self):  # pragma: no cover
        return LaunchActionsRequestFilters.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchConfiguration:
    boto3_raw_data: "type_defs.LaunchConfigurationTypeDef" = dataclasses.field()

    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    ec2LaunchTemplateID = field("ec2LaunchTemplateID")
    launchDisposition = field("launchDisposition")

    @cached_property
    def launchIntoInstanceProperties(self):  # pragma: no cover
        return LaunchIntoInstanceProperties.make_one(
            self.boto3_raw_data["launchIntoInstanceProperties"]
        )

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    name = field("name")
    postLaunchEnabled = field("postLaunchEnabled")
    sourceServerID = field("sourceServerID")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateLaunchConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    copyPrivateIp = field("copyPrivateIp")
    copyTags = field("copyTags")
    launchDisposition = field("launchDisposition")

    @cached_property
    def launchIntoInstanceProperties(self):  # pragma: no cover
        return LaunchIntoInstanceProperties.make_one(
            self.boto3_raw_data["launchIntoInstanceProperties"]
        )

    @cached_property
    def licensing(self):  # pragma: no cover
        return Licensing.make_one(self.boto3_raw_data["licensing"])

    name = field("name")
    postLaunchEnabled = field("postLaunchEnabled")
    targetInstanceTypeRightSizingMethod = field("targetInstanceTypeRightSizingMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLaunchConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleLastLaunch:
    boto3_raw_data: "type_defs.LifeCycleLastLaunchTypeDef" = dataclasses.field()

    @cached_property
    def initiated(self):  # pragma: no cover
        return LifeCycleLastLaunchInitiated.make_one(self.boto3_raw_data["initiated"])

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifeCycleLastLaunchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleLastLaunchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExtensibleSourceServersResponse:
    boto3_raw_data: "type_defs.ListExtensibleSourceServersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return StagingSourceServer.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExtensibleSourceServersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensibleSourceServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceProperties:
    boto3_raw_data: "type_defs.SourcePropertiesTypeDef" = dataclasses.field()

    @cached_property
    def cpus(self):  # pragma: no cover
        return CPU.make_many(self.boto3_raw_data["cpus"])

    @cached_property
    def disks(self):  # pragma: no cover
        return Disk.make_many(self.boto3_raw_data["disks"])

    @cached_property
    def identificationHints(self):  # pragma: no cover
        return IdentificationHints.make_one(self.boto3_raw_data["identificationHints"])

    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @cached_property
    def os(self):  # pragma: no cover
        return OS.make_one(self.boto3_raw_data["os"])

    ramBytes = field("ramBytes")
    recommendedInstanceType = field("recommendedInstanceType")
    supportsNitroInstances = field("supportsNitroInstances")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourcePropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingResource:
    boto3_raw_data: "type_defs.ParticipatingResourceTypeDef" = dataclasses.field()

    launchStatus = field("launchStatus")

    @cached_property
    def participatingResourceID(self):  # pragma: no cover
        return ParticipatingResourceID.make_one(
            self.boto3_raw_data["participatingResourceID"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipatingResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceDataReplicationInitiation:
    boto3_raw_data: "type_defs.RecoveryInstanceDataReplicationInitiationTypeDef" = (
        dataclasses.field()
    )

    startDateTime = field("startDateTime")

    @cached_property
    def steps(self):  # pragma: no cover
        return RecoveryInstanceDataReplicationInitiationStep.make_many(
            self.boto3_raw_data["steps"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecoveryInstanceDataReplicationInitiationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceDataReplicationInitiationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceProperties:
    boto3_raw_data: "type_defs.RecoveryInstancePropertiesTypeDef" = dataclasses.field()

    @cached_property
    def cpus(self):  # pragma: no cover
        return CPU.make_many(self.boto3_raw_data["cpus"])

    @cached_property
    def disks(self):  # pragma: no cover
        return RecoveryInstanceDisk.make_many(self.boto3_raw_data["disks"])

    @cached_property
    def identificationHints(self):  # pragma: no cover
        return IdentificationHints.make_one(self.boto3_raw_data["identificationHints"])

    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @cached_property
    def os(self):  # pragma: no cover
        return OS.make_one(self.boto3_raw_data["os"])

    ramBytes = field("ramBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecoveryInstancePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstancePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceNetwork:
    boto3_raw_data: "type_defs.SourceNetworkTypeDef" = dataclasses.field()

    arn = field("arn")
    cfnStackName = field("cfnStackName")

    @cached_property
    def lastRecovery(self):  # pragma: no cover
        return RecoveryLifeCycle.make_one(self.boto3_raw_data["lastRecovery"])

    launchedVpcID = field("launchedVpcID")
    replicationStatus = field("replicationStatus")
    replicationStatusDetails = field("replicationStatusDetails")
    sourceAccountID = field("sourceAccountID")
    sourceNetworkID = field("sourceNetworkID")
    sourceRegion = field("sourceRegion")
    sourceVpcID = field("sourceVpcID")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceNetworkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfiguration:
    boto3_raw_data: "type_defs.ReplicationConfigurationTypeDef" = dataclasses.field()

    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    autoReplicateNewDisks = field("autoReplicateNewDisks")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    name = field("name")

    @cached_property
    def pitPolicy(self):  # pragma: no cover
        return PITPolicyRule.make_many(self.boto3_raw_data["pitPolicy"])

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return ReplicationConfigurationReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    sourceServerID = field("sourceServerID")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class UpdateReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    sourceServerID = field("sourceServerID")
    associateDefaultSecurityGroup = field("associateDefaultSecurityGroup")
    autoReplicateNewDisks = field("autoReplicateNewDisks")
    bandwidthThrottling = field("bandwidthThrottling")
    createPublicIP = field("createPublicIP")
    dataPlaneRouting = field("dataPlaneRouting")
    defaultLargeStagingDiskType = field("defaultLargeStagingDiskType")
    ebsEncryption = field("ebsEncryption")
    ebsEncryptionKeyArn = field("ebsEncryptionKeyArn")
    name = field("name")

    @cached_property
    def pitPolicy(self):  # pragma: no cover
        return PITPolicyRule.make_many(self.boto3_raw_data["pitPolicy"])

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return ReplicationConfigurationReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    replicationServerInstanceType = field("replicationServerInstanceType")
    replicationServersSecurityGroupsIDs = field("replicationServersSecurityGroupsIDs")
    stagingAreaSubnetId = field("stagingAreaSubnetId")
    stagingAreaTags = field("stagingAreaTags")
    useDedicatedReplicationServer = field("useDedicatedReplicationServer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecoveryRequest:
    boto3_raw_data: "type_defs.StartRecoveryRequestTypeDef" = dataclasses.field()

    @cached_property
    def sourceServers(self):  # pragma: no cover
        return StartRecoveryRequestSourceServer.make_many(
            self.boto3_raw_data["sourceServers"]
        )

    isDrill = field("isDrill")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRecoveryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecoveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSourceNetworkRecoveryRequest:
    boto3_raw_data: "type_defs.StartSourceNetworkRecoveryRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceNetworks(self):  # pragma: no cover
        return StartSourceNetworkRecoveryRequestNetworkEntry.make_many(
            self.boto3_raw_data["sourceNetworks"]
        )

    deployAsNew = field("deployAsNew")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSourceNetworkRecoveryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSourceNetworkRecoveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLaunchConfigurationTemplateResponse:
    boto3_raw_data: "type_defs.CreateLaunchConfigurationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def launchConfigurationTemplate(self):  # pragma: no cover
        return LaunchConfigurationTemplate.make_one(
            self.boto3_raw_data["launchConfigurationTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLaunchConfigurationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLaunchConfigurationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLaunchConfigurationTemplatesResponse:
    boto3_raw_data: "type_defs.DescribeLaunchConfigurationTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return LaunchConfigurationTemplate.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLaunchConfigurationTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLaunchConfigurationTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLaunchConfigurationTemplateResponse:
    boto3_raw_data: "type_defs.UpdateLaunchConfigurationTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def launchConfigurationTemplate(self):  # pragma: no cover
        return LaunchConfigurationTemplate.make_one(
            self.boto3_raw_data["launchConfigurationTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLaunchConfigurationTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLaunchConfigurationTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationTemplatesResponse:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationTemplatesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ReplicationConfigurationTemplate.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationTemplatesResponseTypeDef"
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
                "type_defs.DescribeReplicationConfigurationTemplatesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationInfo:
    boto3_raw_data: "type_defs.DataReplicationInfoTypeDef" = dataclasses.field()

    @cached_property
    def dataReplicationError(self):  # pragma: no cover
        return DataReplicationError.make_one(
            self.boto3_raw_data["dataReplicationError"]
        )

    @cached_property
    def dataReplicationInitiation(self):  # pragma: no cover
        return DataReplicationInitiation.make_one(
            self.boto3_raw_data["dataReplicationInitiation"]
        )

    dataReplicationState = field("dataReplicationState")
    etaDateTime = field("etaDateTime")
    lagDuration = field("lagDuration")

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return DataReplicationInfoReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    stagingAvailabilityZone = field("stagingAvailabilityZone")
    stagingOutpostArn = field("stagingOutpostArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobLogEventData:
    boto3_raw_data: "type_defs.JobLogEventDataTypeDef" = dataclasses.field()

    @cached_property
    def conversionProperties(self):  # pragma: no cover
        return ConversionProperties.make_one(
            self.boto3_raw_data["conversionProperties"]
        )

    conversionServerID = field("conversionServerID")

    @cached_property
    def eventResourceData(self):  # pragma: no cover
        return EventResourceData.make_one(self.boto3_raw_data["eventResourceData"])

    rawError = field("rawError")
    sourceServerID = field("sourceServerID")
    targetInstanceID = field("targetInstanceID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobLogEventDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobLogEventDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchActionRun:
    boto3_raw_data: "type_defs.LaunchActionRunTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return LaunchAction.make_one(self.boto3_raw_data["action"])

    failureReason = field("failureReason")
    runId = field("runId")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchActionRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchActionRunTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchActionsResponse:
    boto3_raw_data: "type_defs.ListLaunchActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return LaunchAction.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycle:
    boto3_raw_data: "type_defs.LifeCycleTypeDef" = dataclasses.field()

    addedToServiceDateTime = field("addedToServiceDateTime")
    elapsedReplicationDuration = field("elapsedReplicationDuration")
    firstByteDateTime = field("firstByteDateTime")

    @cached_property
    def lastLaunch(self):  # pragma: no cover
        return LifeCycleLastLaunch.make_one(self.boto3_raw_data["lastLaunch"])

    lastSeenByServiceDateTime = field("lastSeenByServiceDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifeCycleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstanceDataReplicationInfo:
    boto3_raw_data: "type_defs.RecoveryInstanceDataReplicationInfoTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataReplicationError(self):  # pragma: no cover
        return RecoveryInstanceDataReplicationError.make_one(
            self.boto3_raw_data["dataReplicationError"]
        )

    @cached_property
    def dataReplicationInitiation(self):  # pragma: no cover
        return RecoveryInstanceDataReplicationInitiation.make_one(
            self.boto3_raw_data["dataReplicationInitiation"]
        )

    dataReplicationState = field("dataReplicationState")
    etaDateTime = field("etaDateTime")
    lagDuration = field("lagDuration")

    @cached_property
    def replicatedDisks(self):  # pragma: no cover
        return RecoveryInstanceDataReplicationInfoReplicatedDisk.make_many(
            self.boto3_raw_data["replicatedDisks"]
        )

    stagingAvailabilityZone = field("stagingAvailabilityZone")
    stagingOutpostArn = field("stagingOutpostArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecoveryInstanceDataReplicationInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceDataReplicationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceNetworksResponse:
    boto3_raw_data: "type_defs.DescribeSourceNetworksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SourceNetwork.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSourceNetworksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceNetworksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSourceNetworkReplicationResponse:
    boto3_raw_data: "type_defs.StartSourceNetworkReplicationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceNetwork(self):  # pragma: no cover
        return SourceNetwork.make_one(self.boto3_raw_data["sourceNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSourceNetworkReplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSourceNetworkReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSourceNetworkReplicationResponse:
    boto3_raw_data: "type_defs.StopSourceNetworkReplicationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceNetwork(self):  # pragma: no cover
        return SourceNetwork.make_one(self.boto3_raw_data["sourceNetwork"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopSourceNetworkReplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSourceNetworkReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobLog:
    boto3_raw_data: "type_defs.JobLogTypeDef" = dataclasses.field()

    event = field("event")

    @cached_property
    def eventData(self):  # pragma: no cover
        return JobLogEventData.make_one(self.boto3_raw_data["eventData"])

    logDateTime = field("logDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobLogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchActionsStatus:
    boto3_raw_data: "type_defs.LaunchActionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def runs(self):  # pragma: no cover
        return LaunchActionRun.make_many(self.boto3_raw_data["runs"])

    ssmAgentDiscoveryDatetime = field("ssmAgentDiscoveryDatetime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchActionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchActionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServerResponse:
    boto3_raw_data: "type_defs.SourceServerResponseTypeDef" = dataclasses.field()

    agentVersion = field("agentVersion")
    arn = field("arn")

    @cached_property
    def dataReplicationInfo(self):  # pragma: no cover
        return DataReplicationInfo.make_one(self.boto3_raw_data["dataReplicationInfo"])

    lastLaunchResult = field("lastLaunchResult")

    @cached_property
    def lifeCycle(self):  # pragma: no cover
        return LifeCycle.make_one(self.boto3_raw_data["lifeCycle"])

    recoveryInstanceId = field("recoveryInstanceId")
    replicationDirection = field("replicationDirection")
    reversedDirectionSourceServerArn = field("reversedDirectionSourceServerArn")

    @cached_property
    def sourceCloudProperties(self):  # pragma: no cover
        return SourceCloudProperties.make_one(
            self.boto3_raw_data["sourceCloudProperties"]
        )

    sourceNetworkID = field("sourceNetworkID")

    @cached_property
    def sourceProperties(self):  # pragma: no cover
        return SourceProperties.make_one(self.boto3_raw_data["sourceProperties"])

    sourceServerID = field("sourceServerID")

    @cached_property
    def stagingArea(self):  # pragma: no cover
        return StagingArea.make_one(self.boto3_raw_data["stagingArea"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceServerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceServer:
    boto3_raw_data: "type_defs.SourceServerTypeDef" = dataclasses.field()

    agentVersion = field("agentVersion")
    arn = field("arn")

    @cached_property
    def dataReplicationInfo(self):  # pragma: no cover
        return DataReplicationInfo.make_one(self.boto3_raw_data["dataReplicationInfo"])

    lastLaunchResult = field("lastLaunchResult")

    @cached_property
    def lifeCycle(self):  # pragma: no cover
        return LifeCycle.make_one(self.boto3_raw_data["lifeCycle"])

    recoveryInstanceId = field("recoveryInstanceId")
    replicationDirection = field("replicationDirection")
    reversedDirectionSourceServerArn = field("reversedDirectionSourceServerArn")

    @cached_property
    def sourceCloudProperties(self):  # pragma: no cover
        return SourceCloudProperties.make_one(
            self.boto3_raw_data["sourceCloudProperties"]
        )

    sourceNetworkID = field("sourceNetworkID")

    @cached_property
    def sourceProperties(self):  # pragma: no cover
        return SourceProperties.make_one(self.boto3_raw_data["sourceProperties"])

    sourceServerID = field("sourceServerID")

    @cached_property
    def stagingArea(self):  # pragma: no cover
        return StagingArea.make_one(self.boto3_raw_data["stagingArea"])

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecoveryInstance:
    boto3_raw_data: "type_defs.RecoveryInstanceTypeDef" = dataclasses.field()

    agentVersion = field("agentVersion")
    arn = field("arn")

    @cached_property
    def dataReplicationInfo(self):  # pragma: no cover
        return RecoveryInstanceDataReplicationInfo.make_one(
            self.boto3_raw_data["dataReplicationInfo"]
        )

    ec2InstanceID = field("ec2InstanceID")
    ec2InstanceState = field("ec2InstanceState")

    @cached_property
    def failback(self):  # pragma: no cover
        return RecoveryInstanceFailback.make_one(self.boto3_raw_data["failback"])

    isDrill = field("isDrill")
    jobID = field("jobID")
    originAvailabilityZone = field("originAvailabilityZone")
    originEnvironment = field("originEnvironment")
    pointInTimeSnapshotDateTime = field("pointInTimeSnapshotDateTime")
    recoveryInstanceID = field("recoveryInstanceID")

    @cached_property
    def recoveryInstanceProperties(self):  # pragma: no cover
        return RecoveryInstanceProperties.make_one(
            self.boto3_raw_data["recoveryInstanceProperties"]
        )

    sourceOutpostArn = field("sourceOutpostArn")
    sourceServerID = field("sourceServerID")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecoveryInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecoveryInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobLogItemsResponse:
    boto3_raw_data: "type_defs.DescribeJobLogItemsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return JobLog.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobLogItemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobLogItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingServer:
    boto3_raw_data: "type_defs.ParticipatingServerTypeDef" = dataclasses.field()

    @cached_property
    def launchActionsStatus(self):  # pragma: no cover
        return LaunchActionsStatus.make_one(self.boto3_raw_data["launchActionsStatus"])

    launchStatus = field("launchStatus")
    recoveryInstanceID = field("recoveryInstanceID")
    sourceServerID = field("sourceServerID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipatingServerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingServerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExtendedSourceServerResponse:
    boto3_raw_data: "type_defs.CreateExtendedSourceServerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceServer(self):  # pragma: no cover
        return SourceServer.make_one(self.boto3_raw_data["sourceServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExtendedSourceServerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExtendedSourceServerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSourceServersResponse:
    boto3_raw_data: "type_defs.DescribeSourceServersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SourceServer.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSourceServersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSourceServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationResponse:
    boto3_raw_data: "type_defs.StartReplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def sourceServer(self):  # pragma: no cover
        return SourceServer.make_one(self.boto3_raw_data["sourceServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationResponse:
    boto3_raw_data: "type_defs.StopReplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def sourceServer(self):  # pragma: no cover
        return SourceServer.make_one(self.boto3_raw_data["sourceServer"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecoveryInstancesResponse:
    boto3_raw_data: "type_defs.DescribeRecoveryInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return RecoveryInstance.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecoveryInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecoveryInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    jobID = field("jobID")
    arn = field("arn")
    creationDateTime = field("creationDateTime")
    endDateTime = field("endDateTime")
    initiatedBy = field("initiatedBy")

    @cached_property
    def participatingResources(self):  # pragma: no cover
        return ParticipatingResource.make_many(
            self.boto3_raw_data["participatingResources"]
        )

    @cached_property
    def participatingServers(self):  # pragma: no cover
        return ParticipatingServer.make_many(
            self.boto3_raw_data["participatingServers"]
        )

    status = field("status")
    tags = field("tags")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSourceNetworkStackResponse:
    boto3_raw_data: "type_defs.AssociateSourceNetworkStackResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateSourceNetworkStackResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSourceNetworkStackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsResponse:
    boto3_raw_data: "type_defs.DescribeJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFailbackLaunchResponse:
    boto3_raw_data: "type_defs.StartFailbackLaunchResponseTypeDef" = dataclasses.field()

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFailbackLaunchResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFailbackLaunchResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecoveryResponse:
    boto3_raw_data: "type_defs.StartRecoveryResponseTypeDef" = dataclasses.field()

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRecoveryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecoveryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSourceNetworkRecoveryResponse:
    boto3_raw_data: "type_defs.StartSourceNetworkRecoveryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSourceNetworkRecoveryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSourceNetworkRecoveryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateRecoveryInstancesResponse:
    boto3_raw_data: "type_defs.TerminateRecoveryInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TerminateRecoveryInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateRecoveryInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
