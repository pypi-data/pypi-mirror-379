# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeconnections import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Connection:
    boto3_raw_data: "type_defs.ConnectionTypeDef" = dataclasses.field()

    ConnectionName = field("ConnectionName")
    ConnectionArn = field("ConnectionArn")
    ProviderType = field("ProviderType")
    OwnerAccountId = field("OwnerAccountId")
    ConnectionStatus = field("ConnectionStatus")
    HostArn = field("HostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionTypeDef"]]
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
class RepositoryLinkInfo:
    boto3_raw_data: "type_defs.RepositoryLinkInfoTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    OwnerId = field("OwnerId")
    ProviderType = field("ProviderType")
    RepositoryLinkArn = field("RepositoryLinkArn")
    RepositoryLinkId = field("RepositoryLinkId")
    RepositoryName = field("RepositoryName")
    EncryptionKeyArn = field("EncryptionKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryLinkInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryLinkInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSyncConfigurationInput:
    boto3_raw_data: "type_defs.CreateSyncConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    Branch = field("Branch")
    ConfigFile = field("ConfigFile")
    RepositoryLinkId = field("RepositoryLinkId")
    ResourceName = field("ResourceName")
    RoleArn = field("RoleArn")
    SyncType = field("SyncType")
    PublishDeploymentStatus = field("PublishDeploymentStatus")
    TriggerResourceUpdateOn = field("TriggerResourceUpdateOn")
    PullRequestComment = field("PullRequestComment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSyncConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSyncConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncConfiguration:
    boto3_raw_data: "type_defs.SyncConfigurationTypeDef" = dataclasses.field()

    Branch = field("Branch")
    OwnerId = field("OwnerId")
    ProviderType = field("ProviderType")
    RepositoryLinkId = field("RepositoryLinkId")
    RepositoryName = field("RepositoryName")
    ResourceName = field("ResourceName")
    RoleArn = field("RoleArn")
    SyncType = field("SyncType")
    ConfigFile = field("ConfigFile")
    PublishDeploymentStatus = field("PublishDeploymentStatus")
    TriggerResourceUpdateOn = field("TriggerResourceUpdateOn")
    PullRequestComment = field("PullRequestComment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionInput:
    boto3_raw_data: "type_defs.DeleteConnectionInputTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHostInput:
    boto3_raw_data: "type_defs.DeleteHostInputTypeDef" = dataclasses.field()

    HostArn = field("HostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteHostInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteHostInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRepositoryLinkInput:
    boto3_raw_data: "type_defs.DeleteRepositoryLinkInputTypeDef" = dataclasses.field()

    RepositoryLinkId = field("RepositoryLinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRepositoryLinkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRepositoryLinkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSyncConfigurationInput:
    boto3_raw_data: "type_defs.DeleteSyncConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    SyncType = field("SyncType")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSyncConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSyncConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionInput:
    boto3_raw_data: "type_defs.GetConnectionInputTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostInput:
    boto3_raw_data: "type_defs.GetHostInputTypeDef" = dataclasses.field()

    HostArn = field("HostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetHostInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetHostInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigurationOutput:
    boto3_raw_data: "type_defs.VpcConfigurationOutputTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    TlsCertificate = field("TlsCertificate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryLinkInput:
    boto3_raw_data: "type_defs.GetRepositoryLinkInputTypeDef" = dataclasses.field()

    RepositoryLinkId = field("RepositoryLinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryLinkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryLinkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositorySyncStatusInput:
    boto3_raw_data: "type_defs.GetRepositorySyncStatusInputTypeDef" = (
        dataclasses.field()
    )

    Branch = field("Branch")
    RepositoryLinkId = field("RepositoryLinkId")
    SyncType = field("SyncType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositorySyncStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositorySyncStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSyncStatusInput:
    boto3_raw_data: "type_defs.GetResourceSyncStatusInputTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    SyncType = field("SyncType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceSyncStatusInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSyncStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Revision:
    boto3_raw_data: "type_defs.RevisionTypeDef" = dataclasses.field()

    Branch = field("Branch")
    Directory = field("Directory")
    OwnerId = field("OwnerId")
    RepositoryName = field("RepositoryName")
    ProviderType = field("ProviderType")
    Sha = field("Sha")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RevisionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSyncBlockerSummaryInput:
    boto3_raw_data: "type_defs.GetSyncBlockerSummaryInputTypeDef" = dataclasses.field()

    SyncType = field("SyncType")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSyncBlockerSummaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSyncBlockerSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSyncConfigurationInput:
    boto3_raw_data: "type_defs.GetSyncConfigurationInputTypeDef" = dataclasses.field()

    SyncType = field("SyncType")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSyncConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSyncConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsInput:
    boto3_raw_data: "type_defs.ListConnectionsInputTypeDef" = dataclasses.field()

    ProviderTypeFilter = field("ProviderTypeFilter")
    HostArnFilter = field("HostArnFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostsInput:
    boto3_raw_data: "type_defs.ListHostsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListHostsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListHostsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoryLinksInput:
    boto3_raw_data: "type_defs.ListRepositoryLinksInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoryLinksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoryLinksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositorySyncDefinitionsInput:
    boto3_raw_data: "type_defs.ListRepositorySyncDefinitionsInputTypeDef" = (
        dataclasses.field()
    )

    RepositoryLinkId = field("RepositoryLinkId")
    SyncType = field("SyncType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositorySyncDefinitionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositorySyncDefinitionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySyncDefinition:
    boto3_raw_data: "type_defs.RepositorySyncDefinitionTypeDef" = dataclasses.field()

    Branch = field("Branch")
    Directory = field("Directory")
    Parent = field("Parent")
    Target = field("Target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositorySyncDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySyncDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSyncConfigurationsInput:
    boto3_raw_data: "type_defs.ListSyncConfigurationsInputTypeDef" = dataclasses.field()

    RepositoryLinkId = field("RepositoryLinkId")
    SyncType = field("SyncType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSyncConfigurationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSyncConfigurationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySyncEvent:
    boto3_raw_data: "type_defs.RepositorySyncEventTypeDef" = dataclasses.field()

    Event = field("Event")
    Time = field("Time")
    Type = field("Type")
    ExternalId = field("ExternalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositorySyncEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySyncEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSyncEvent:
    boto3_raw_data: "type_defs.ResourceSyncEventTypeDef" = dataclasses.field()

    Event = field("Event")
    Time = field("Time")
    Type = field("Type")
    ExternalId = field("ExternalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceSyncEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSyncEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncBlockerContext:
    boto3_raw_data: "type_defs.SyncBlockerContextTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncBlockerContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncBlockerContextTypeDef"]
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
    TagKeys = field("TagKeys")

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
class UpdateRepositoryLinkInput:
    boto3_raw_data: "type_defs.UpdateRepositoryLinkInputTypeDef" = dataclasses.field()

    RepositoryLinkId = field("RepositoryLinkId")
    ConnectionArn = field("ConnectionArn")
    EncryptionKeyArn = field("EncryptionKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRepositoryLinkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryLinkInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSyncBlockerInput:
    boto3_raw_data: "type_defs.UpdateSyncBlockerInputTypeDef" = dataclasses.field()

    Id = field("Id")
    SyncType = field("SyncType")
    ResourceName = field("ResourceName")
    ResolvedReason = field("ResolvedReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSyncBlockerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSyncBlockerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSyncConfigurationInput:
    boto3_raw_data: "type_defs.UpdateSyncConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    ResourceName = field("ResourceName")
    SyncType = field("SyncType")
    Branch = field("Branch")
    ConfigFile = field("ConfigFile")
    RepositoryLinkId = field("RepositoryLinkId")
    RoleArn = field("RoleArn")
    PublishDeploymentStatus = field("PublishDeploymentStatus")
    TriggerResourceUpdateOn = field("TriggerResourceUpdateOn")
    PullRequestComment = field("PullRequestComment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSyncConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSyncConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    TlsCertificate = field("TlsCertificate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionInput:
    boto3_raw_data: "type_defs.CreateConnectionInputTypeDef" = dataclasses.field()

    ConnectionName = field("ConnectionName")
    ProviderType = field("ProviderType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    HostArn = field("HostArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryLinkInput:
    boto3_raw_data: "type_defs.CreateRepositoryLinkInputTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    OwnerId = field("OwnerId")
    RepositoryName = field("RepositoryName")
    EncryptionKeyArn = field("EncryptionKeyArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryLinkInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryLinkInputTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateConnectionOutput:
    boto3_raw_data: "type_defs.CreateConnectionOutputTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHostOutput:
    boto3_raw_data: "type_defs.CreateHostOutputTypeDef" = dataclasses.field()

    HostArn = field("HostArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateHostOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHostOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionOutput:
    boto3_raw_data: "type_defs.GetConnectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsOutput:
    boto3_raw_data: "type_defs.ListConnectionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRepositoryLinkOutput:
    boto3_raw_data: "type_defs.CreateRepositoryLinkOutputTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryLinkInfo(self):  # pragma: no cover
        return RepositoryLinkInfo.make_one(self.boto3_raw_data["RepositoryLinkInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRepositoryLinkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRepositoryLinkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositoryLinkOutput:
    boto3_raw_data: "type_defs.GetRepositoryLinkOutputTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryLinkInfo(self):  # pragma: no cover
        return RepositoryLinkInfo.make_one(self.boto3_raw_data["RepositoryLinkInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRepositoryLinkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositoryLinkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositoryLinksOutput:
    boto3_raw_data: "type_defs.ListRepositoryLinksOutputTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryLinks(self):  # pragma: no cover
        return RepositoryLinkInfo.make_many(self.boto3_raw_data["RepositoryLinks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRepositoryLinksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositoryLinksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRepositoryLinkOutput:
    boto3_raw_data: "type_defs.UpdateRepositoryLinkOutputTypeDef" = dataclasses.field()

    @cached_property
    def RepositoryLinkInfo(self):  # pragma: no cover
        return RepositoryLinkInfo.make_one(self.boto3_raw_data["RepositoryLinkInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRepositoryLinkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRepositoryLinkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSyncConfigurationOutput:
    boto3_raw_data: "type_defs.CreateSyncConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SyncConfiguration(self):  # pragma: no cover
        return SyncConfiguration.make_one(self.boto3_raw_data["SyncConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSyncConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSyncConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSyncConfigurationOutput:
    boto3_raw_data: "type_defs.GetSyncConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def SyncConfiguration(self):  # pragma: no cover
        return SyncConfiguration.make_one(self.boto3_raw_data["SyncConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSyncConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSyncConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSyncConfigurationsOutput:
    boto3_raw_data: "type_defs.ListSyncConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SyncConfigurations(self):  # pragma: no cover
        return SyncConfiguration.make_many(self.boto3_raw_data["SyncConfigurations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSyncConfigurationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSyncConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSyncConfigurationOutput:
    boto3_raw_data: "type_defs.UpdateSyncConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SyncConfiguration(self):  # pragma: no cover
        return SyncConfiguration.make_one(self.boto3_raw_data["SyncConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSyncConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSyncConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostOutput:
    boto3_raw_data: "type_defs.GetHostOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")
    ProviderType = field("ProviderType")
    ProviderEndpoint = field("ProviderEndpoint")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["VpcConfiguration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetHostOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetHostOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Host:
    boto3_raw_data: "type_defs.HostTypeDef" = dataclasses.field()

    Name = field("Name")
    HostArn = field("HostArn")
    ProviderType = field("ProviderType")
    ProviderEndpoint = field("ProviderEndpoint")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["VpcConfiguration"])

    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRepositorySyncDefinitionsOutput:
    boto3_raw_data: "type_defs.ListRepositorySyncDefinitionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RepositorySyncDefinitions(self):  # pragma: no cover
        return RepositorySyncDefinition.make_many(
            self.boto3_raw_data["RepositorySyncDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRepositorySyncDefinitionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRepositorySyncDefinitionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositorySyncAttempt:
    boto3_raw_data: "type_defs.RepositorySyncAttemptTypeDef" = dataclasses.field()

    StartedAt = field("StartedAt")
    Status = field("Status")

    @cached_property
    def Events(self):  # pragma: no cover
        return RepositorySyncEvent.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositorySyncAttemptTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositorySyncAttemptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSyncAttempt:
    boto3_raw_data: "type_defs.ResourceSyncAttemptTypeDef" = dataclasses.field()

    @cached_property
    def Events(self):  # pragma: no cover
        return ResourceSyncEvent.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def InitialRevision(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["InitialRevision"])

    StartedAt = field("StartedAt")
    Status = field("Status")

    @cached_property
    def TargetRevision(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["TargetRevision"])

    Target = field("Target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSyncAttemptTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSyncAttemptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncBlocker:
    boto3_raw_data: "type_defs.SyncBlockerTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    Status = field("Status")
    CreatedReason = field("CreatedReason")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Contexts(self):  # pragma: no cover
        return SyncBlockerContext.make_many(self.boto3_raw_data["Contexts"])

    ResolvedReason = field("ResolvedReason")
    ResolvedAt = field("ResolvedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncBlockerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyncBlockerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostsOutput:
    boto3_raw_data: "type_defs.ListHostsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Hosts(self):  # pragma: no cover
        return Host.make_many(self.boto3_raw_data["Hosts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListHostsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListHostsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRepositorySyncStatusOutput:
    boto3_raw_data: "type_defs.GetRepositorySyncStatusOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LatestSync(self):  # pragma: no cover
        return RepositorySyncAttempt.make_one(self.boto3_raw_data["LatestSync"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRepositorySyncStatusOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRepositorySyncStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSyncStatusOutput:
    boto3_raw_data: "type_defs.GetResourceSyncStatusOutputTypeDef" = dataclasses.field()

    @cached_property
    def DesiredState(self):  # pragma: no cover
        return Revision.make_one(self.boto3_raw_data["DesiredState"])

    @cached_property
    def LatestSuccessfulSync(self):  # pragma: no cover
        return ResourceSyncAttempt.make_one(self.boto3_raw_data["LatestSuccessfulSync"])

    @cached_property
    def LatestSync(self):  # pragma: no cover
        return ResourceSyncAttempt.make_one(self.boto3_raw_data["LatestSync"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceSyncStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSyncStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncBlockerSummary:
    boto3_raw_data: "type_defs.SyncBlockerSummaryTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    ParentResourceName = field("ParentResourceName")

    @cached_property
    def LatestBlockers(self):  # pragma: no cover
        return SyncBlocker.make_many(self.boto3_raw_data["LatestBlockers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SyncBlockerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SyncBlockerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSyncBlockerOutput:
    boto3_raw_data: "type_defs.UpdateSyncBlockerOutputTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    ParentResourceName = field("ParentResourceName")

    @cached_property
    def SyncBlocker(self):  # pragma: no cover
        return SyncBlocker.make_one(self.boto3_raw_data["SyncBlocker"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSyncBlockerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSyncBlockerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHostInput:
    boto3_raw_data: "type_defs.CreateHostInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ProviderType = field("ProviderType")
    ProviderEndpoint = field("ProviderEndpoint")
    VpcConfiguration = field("VpcConfiguration")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateHostInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateHostInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHostInput:
    boto3_raw_data: "type_defs.UpdateHostInputTypeDef" = dataclasses.field()

    HostArn = field("HostArn")
    ProviderEndpoint = field("ProviderEndpoint")
    VpcConfiguration = field("VpcConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateHostInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateHostInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSyncBlockerSummaryOutput:
    boto3_raw_data: "type_defs.GetSyncBlockerSummaryOutputTypeDef" = dataclasses.field()

    @cached_property
    def SyncBlockerSummary(self):  # pragma: no cover
        return SyncBlockerSummary.make_one(self.boto3_raw_data["SyncBlockerSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSyncBlockerSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSyncBlockerSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
