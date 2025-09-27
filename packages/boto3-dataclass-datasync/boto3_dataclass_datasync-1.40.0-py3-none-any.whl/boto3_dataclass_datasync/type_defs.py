# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_datasync import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Platform:
    boto3_raw_data: "type_defs.PlatformTypeDef" = dataclasses.field()

    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlatformTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AzureBlobSasConfiguration:
    boto3_raw_data: "type_defs.AzureBlobSasConfigurationTypeDef" = dataclasses.field()

    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AzureBlobSasConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AzureBlobSasConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelTaskExecutionRequest:
    boto3_raw_data: "type_defs.CancelTaskExecutionRequestTypeDef" = dataclasses.field()

    TaskExecutionArn = field("TaskExecutionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelTaskExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTaskExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmkSecretConfig:
    boto3_raw_data: "type_defs.CmkSecretConfigTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CmkSecretConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CmkSecretConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagListEntry:
    boto3_raw_data: "type_defs.TagListEntryTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagListEntryTypeDef"]],
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
class CustomSecretConfig:
    boto3_raw_data: "type_defs.CustomSecretConfigTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")
    SecretAccessRoleArn = field("SecretAccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomSecretConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomSecretConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HdfsNameNode:
    boto3_raw_data: "type_defs.HdfsNameNodeTypeDef" = dataclasses.field()

    Hostname = field("Hostname")
    Port = field("Port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HdfsNameNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HdfsNameNodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QopConfiguration:
    boto3_raw_data: "type_defs.QopConfigurationTypeDef" = dataclasses.field()

    RpcProtection = field("RpcProtection")
    DataTransferProtection = field("DataTransferProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QopConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QopConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NfsMountOptions:
    boto3_raw_data: "type_defs.NfsMountOptionsTypeDef" = dataclasses.field()

    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NfsMountOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NfsMountOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Config:
    boto3_raw_data: "type_defs.S3ConfigTypeDef" = dataclasses.field()

    BucketAccessRoleArn = field("BucketAccessRoleArn")

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
class SmbMountOptions:
    boto3_raw_data: "type_defs.SmbMountOptionsTypeDef" = dataclasses.field()

    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SmbMountOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SmbMountOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterRule:
    boto3_raw_data: "type_defs.FilterRuleTypeDef" = dataclasses.field()

    FilterType = field("FilterType")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Options:
    boto3_raw_data: "type_defs.OptionsTypeDef" = dataclasses.field()

    VerifyMode = field("VerifyMode")
    OverwriteMode = field("OverwriteMode")
    Atime = field("Atime")
    Mtime = field("Mtime")
    Uid = field("Uid")
    Gid = field("Gid")
    PreserveDeletedFiles = field("PreserveDeletedFiles")
    PreserveDevices = field("PreserveDevices")
    PosixPermissions = field("PosixPermissions")
    BytesPerSecond = field("BytesPerSecond")
    TaskQueueing = field("TaskQueueing")
    LogLevel = field("LogLevel")
    TransferMode = field("TransferMode")
    SecurityDescriptorCopyFlags = field("SecurityDescriptorCopyFlags")
    ObjectTags = field("ObjectTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSchedule:
    boto3_raw_data: "type_defs.TaskScheduleTypeDef" = dataclasses.field()

    ScheduleExpression = field("ScheduleExpression")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentRequest:
    boto3_raw_data: "type_defs.DeleteAgentRequestTypeDef" = dataclasses.field()

    AgentArn = field("AgentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLocationRequest:
    boto3_raw_data: "type_defs.DeleteLocationRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTaskRequest:
    boto3_raw_data: "type_defs.DeleteTaskRequestTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgentRequest:
    boto3_raw_data: "type_defs.DescribeAgentRequestTypeDef" = dataclasses.field()

    AgentArn = field("AgentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateLinkConfig:
    boto3_raw_data: "type_defs.PrivateLinkConfigTypeDef" = dataclasses.field()

    VpcEndpointId = field("VpcEndpointId")
    PrivateLinkEndpoint = field("PrivateLinkEndpoint")
    SubnetArns = field("SubnetArns")
    SecurityGroupArns = field("SecurityGroupArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivateLinkConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateLinkConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationAzureBlobRequest:
    boto3_raw_data: "type_defs.DescribeLocationAzureBlobRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLocationAzureBlobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationAzureBlobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedSecretConfig:
    boto3_raw_data: "type_defs.ManagedSecretConfigTypeDef" = dataclasses.field()

    SecretArn = field("SecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedSecretConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedSecretConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationEfsRequest:
    boto3_raw_data: "type_defs.DescribeLocationEfsRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationEfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationEfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2ConfigOutput:
    boto3_raw_data: "type_defs.Ec2ConfigOutputTypeDef" = dataclasses.field()

    SubnetArn = field("SubnetArn")
    SecurityGroupArns = field("SecurityGroupArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2ConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ec2ConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxLustreRequest:
    boto3_raw_data: "type_defs.DescribeLocationFsxLustreRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLocationFsxLustreRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxLustreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxOntapRequest:
    boto3_raw_data: "type_defs.DescribeLocationFsxOntapRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLocationFsxOntapRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxOntapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxOpenZfsRequest:
    boto3_raw_data: "type_defs.DescribeLocationFsxOpenZfsRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationFsxOpenZfsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxOpenZfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxWindowsRequest:
    boto3_raw_data: "type_defs.DescribeLocationFsxWindowsRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationFsxWindowsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxWindowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationHdfsRequest:
    boto3_raw_data: "type_defs.DescribeLocationHdfsRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationHdfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationHdfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationNfsRequest:
    boto3_raw_data: "type_defs.DescribeLocationNfsRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationNfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationNfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnPremConfigOutput:
    boto3_raw_data: "type_defs.OnPremConfigOutputTypeDef" = dataclasses.field()

    AgentArns = field("AgentArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OnPremConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OnPremConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationObjectStorageRequest:
    boto3_raw_data: "type_defs.DescribeLocationObjectStorageRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationObjectStorageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationObjectStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationS3Request:
    boto3_raw_data: "type_defs.DescribeLocationS3RequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationS3RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationS3RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationSmbRequest:
    boto3_raw_data: "type_defs.DescribeLocationSmbRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationSmbRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationSmbRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskExecutionRequest:
    boto3_raw_data: "type_defs.DescribeTaskExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    TaskExecutionArn = field("TaskExecutionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTaskExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportResult:
    boto3_raw_data: "type_defs.ReportResultTypeDef" = dataclasses.field()

    Status = field("Status")
    ErrorCode = field("ErrorCode")
    ErrorDetail = field("ErrorDetail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskExecutionFilesFailedDetail:
    boto3_raw_data: "type_defs.TaskExecutionFilesFailedDetailTypeDef" = (
        dataclasses.field()
    )

    Prepare = field("Prepare")
    Transfer = field("Transfer")
    Verify = field("Verify")
    Delete = field("Delete")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskExecutionFilesFailedDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskExecutionFilesFailedDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskExecutionFilesListedDetail:
    boto3_raw_data: "type_defs.TaskExecutionFilesListedDetailTypeDef" = (
        dataclasses.field()
    )

    AtSource = field("AtSource")
    AtDestinationForDelete = field("AtDestinationForDelete")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskExecutionFilesListedDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskExecutionFilesListedDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskExecutionResultDetail:
    boto3_raw_data: "type_defs.TaskExecutionResultDetailTypeDef" = dataclasses.field()

    PrepareDuration = field("PrepareDuration")
    PrepareStatus = field("PrepareStatus")
    TotalDuration = field("TotalDuration")
    TransferDuration = field("TransferDuration")
    TransferStatus = field("TransferStatus")
    VerifyDuration = field("VerifyDuration")
    VerifyStatus = field("VerifyStatus")
    ErrorCode = field("ErrorCode")
    ErrorDetail = field("ErrorDetail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskExecutionResultDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskExecutionResultDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskRequest:
    boto3_raw_data: "type_defs.DescribeTaskRequestTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskScheduleDetails:
    boto3_raw_data: "type_defs.TaskScheduleDetailsTypeDef" = dataclasses.field()

    StatusUpdateTime = field("StatusUpdateTime")
    DisabledReason = field("DisabledReason")
    DisabledBy = field("DisabledBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskScheduleDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskScheduleDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2Config:
    boto3_raw_data: "type_defs.Ec2ConfigTypeDef" = dataclasses.field()

    SubnetArn = field("SubnetArn")
    SecurityGroupArns = field("SecurityGroupArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2ConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ec2ConfigTypeDef"]]
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
class ListAgentsRequest:
    boto3_raw_data: "type_defs.ListAgentsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAgentsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationFilter:
    boto3_raw_data: "type_defs.LocationFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationListEntry:
    boto3_raw_data: "type_defs.LocationListEntryTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocationListEntryTypeDef"]
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
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ListTaskExecutionsRequest:
    boto3_raw_data: "type_defs.ListTaskExecutionsRequestTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaskExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskExecutionListEntry:
    boto3_raw_data: "type_defs.TaskExecutionListEntryTypeDef" = dataclasses.field()

    TaskExecutionArn = field("TaskExecutionArn")
    Status = field("Status")
    TaskMode = field("TaskMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskExecutionListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskExecutionListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskFilter:
    boto3_raw_data: "type_defs.TaskFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskListEntry:
    boto3_raw_data: "type_defs.TaskListEntryTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")
    Status = field("Status")
    Name = field("Name")
    TaskMode = field("TaskMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskListEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnPremConfig:
    boto3_raw_data: "type_defs.OnPremConfigTypeDef" = dataclasses.field()

    AgentArns = field("AgentArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnPremConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OnPremConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportDestinationS3:
    boto3_raw_data: "type_defs.ReportDestinationS3TypeDef" = dataclasses.field()

    S3BucketArn = field("S3BucketArn")
    BucketAccessRoleArn = field("BucketAccessRoleArn")
    Subdirectory = field("Subdirectory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportDestinationS3TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportDestinationS3TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportOverride:
    boto3_raw_data: "type_defs.ReportOverrideTypeDef" = dataclasses.field()

    ReportLevel = field("ReportLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ManifestConfig:
    boto3_raw_data: "type_defs.S3ManifestConfigTypeDef" = dataclasses.field()

    ManifestObjectPath = field("ManifestObjectPath")
    BucketAccessRoleArn = field("BucketAccessRoleArn")
    S3BucketArn = field("S3BucketArn")
    ManifestObjectVersionId = field("ManifestObjectVersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ManifestConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ManifestConfigTypeDef"]
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
    Keys = field("Keys")

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
class UpdateAgentRequest:
    boto3_raw_data: "type_defs.UpdateAgentRequestTypeDef" = dataclasses.field()

    AgentArn = field("AgentArn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationEfsRequest:
    boto3_raw_data: "type_defs.UpdateLocationEfsRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")
    AccessPointArn = field("AccessPointArn")
    FileSystemAccessRoleArn = field("FileSystemAccessRoleArn")
    InTransitEncryption = field("InTransitEncryption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLocationEfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationEfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationFsxLustreRequest:
    boto3_raw_data: "type_defs.UpdateLocationFsxLustreRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLocationFsxLustreRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationFsxLustreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationFsxWindowsRequest:
    boto3_raw_data: "type_defs.UpdateLocationFsxWindowsRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")
    Domain = field("Domain")
    User = field("User")
    Password = field("Password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLocationFsxWindowsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationFsxWindowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentListEntry:
    boto3_raw_data: "type_defs.AgentListEntryTypeDef" = dataclasses.field()

    AgentArn = field("AgentArn")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def Platform(self):  # pragma: no cover
        return Platform.make_one(self.boto3_raw_data["Platform"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentListEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentRequest:
    boto3_raw_data: "type_defs.CreateAgentRequestTypeDef" = dataclasses.field()

    ActivationKey = field("ActivationKey")
    AgentName = field("AgentName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    VpcEndpointId = field("VpcEndpointId")
    SubnetArns = field("SubnetArns")
    SecurityGroupArns = field("SecurityGroupArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxLustreRequest:
    boto3_raw_data: "type_defs.CreateLocationFsxLustreRequestTypeDef" = (
        dataclasses.field()
    )

    FsxFilesystemArn = field("FsxFilesystemArn")
    SecurityGroupArns = field("SecurityGroupArns")
    Subdirectory = field("Subdirectory")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxLustreRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxLustreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxWindowsRequest:
    boto3_raw_data: "type_defs.CreateLocationFsxWindowsRequestTypeDef" = (
        dataclasses.field()
    )

    FsxFilesystemArn = field("FsxFilesystemArn")
    SecurityGroupArns = field("SecurityGroupArns")
    User = field("User")
    Password = field("Password")
    Subdirectory = field("Subdirectory")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    Domain = field("Domain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxWindowsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxWindowsRequestTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

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
class CreateAgentResponse:
    boto3_raw_data: "type_defs.CreateAgentResponseTypeDef" = dataclasses.field()

    AgentArn = field("AgentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationAzureBlobResponse:
    boto3_raw_data: "type_defs.CreateLocationAzureBlobResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationAzureBlobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationAzureBlobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationEfsResponse:
    boto3_raw_data: "type_defs.CreateLocationEfsResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationEfsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationEfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxLustreResponse:
    boto3_raw_data: "type_defs.CreateLocationFsxLustreResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxLustreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxLustreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxOntapResponse:
    boto3_raw_data: "type_defs.CreateLocationFsxOntapResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxOntapResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxOntapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxOpenZfsResponse:
    boto3_raw_data: "type_defs.CreateLocationFsxOpenZfsResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxOpenZfsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxOpenZfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxWindowsResponse:
    boto3_raw_data: "type_defs.CreateLocationFsxWindowsResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxWindowsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxWindowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationHdfsResponse:
    boto3_raw_data: "type_defs.CreateLocationHdfsResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationHdfsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationHdfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationNfsResponse:
    boto3_raw_data: "type_defs.CreateLocationNfsResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationNfsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationNfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationObjectStorageResponse:
    boto3_raw_data: "type_defs.CreateLocationObjectStorageResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLocationObjectStorageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationObjectStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationS3Response:
    boto3_raw_data: "type_defs.CreateLocationS3ResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationS3ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationS3ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationSmbResponse:
    boto3_raw_data: "type_defs.CreateLocationSmbResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationSmbResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationSmbResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTaskResponse:
    boto3_raw_data: "type_defs.CreateTaskResponseTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxLustreResponse:
    boto3_raw_data: "type_defs.DescribeLocationFsxLustreResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    SecurityGroupArns = field("SecurityGroupArns")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationFsxLustreResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxLustreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxWindowsResponse:
    boto3_raw_data: "type_defs.DescribeLocationFsxWindowsResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    SecurityGroupArns = field("SecurityGroupArns")
    CreationTime = field("CreationTime")
    User = field("User")
    Domain = field("Domain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationFsxWindowsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxWindowsResponseTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class StartTaskExecutionResponse:
    boto3_raw_data: "type_defs.StartTaskExecutionResponseTypeDef" = dataclasses.field()

    TaskExecutionArn = field("TaskExecutionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTaskExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTaskExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationAzureBlobRequest:
    boto3_raw_data: "type_defs.CreateLocationAzureBlobRequestTypeDef" = (
        dataclasses.field()
    )

    ContainerUrl = field("ContainerUrl")
    AuthenticationType = field("AuthenticationType")

    @cached_property
    def SasConfiguration(self):  # pragma: no cover
        return AzureBlobSasConfiguration.make_one(
            self.boto3_raw_data["SasConfiguration"]
        )

    BlobType = field("BlobType")
    AccessTier = field("AccessTier")
    Subdirectory = field("Subdirectory")
    AgentArns = field("AgentArns")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def CmkSecretConfig(self):  # pragma: no cover
        return CmkSecretConfig.make_one(self.boto3_raw_data["CmkSecretConfig"])

    @cached_property
    def CustomSecretConfig(self):  # pragma: no cover
        return CustomSecretConfig.make_one(self.boto3_raw_data["CustomSecretConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationAzureBlobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationAzureBlobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationObjectStorageRequest:
    boto3_raw_data: "type_defs.CreateLocationObjectStorageRequestTypeDef" = (
        dataclasses.field()
    )

    ServerHostname = field("ServerHostname")
    BucketName = field("BucketName")
    ServerPort = field("ServerPort")
    ServerProtocol = field("ServerProtocol")
    Subdirectory = field("Subdirectory")
    AccessKey = field("AccessKey")
    SecretKey = field("SecretKey")
    AgentArns = field("AgentArns")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    ServerCertificate = field("ServerCertificate")

    @cached_property
    def CmkSecretConfig(self):  # pragma: no cover
        return CmkSecretConfig.make_one(self.boto3_raw_data["CmkSecretConfig"])

    @cached_property
    def CustomSecretConfig(self):  # pragma: no cover
        return CustomSecretConfig.make_one(self.boto3_raw_data["CustomSecretConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLocationObjectStorageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationObjectStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationAzureBlobRequest:
    boto3_raw_data: "type_defs.UpdateLocationAzureBlobRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")
    AuthenticationType = field("AuthenticationType")

    @cached_property
    def SasConfiguration(self):  # pragma: no cover
        return AzureBlobSasConfiguration.make_one(
            self.boto3_raw_data["SasConfiguration"]
        )

    BlobType = field("BlobType")
    AccessTier = field("AccessTier")
    AgentArns = field("AgentArns")

    @cached_property
    def CmkSecretConfig(self):  # pragma: no cover
        return CmkSecretConfig.make_one(self.boto3_raw_data["CmkSecretConfig"])

    @cached_property
    def CustomSecretConfig(self):  # pragma: no cover
        return CustomSecretConfig.make_one(self.boto3_raw_data["CustomSecretConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLocationAzureBlobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationAzureBlobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationObjectStorageRequest:
    boto3_raw_data: "type_defs.UpdateLocationObjectStorageRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    ServerPort = field("ServerPort")
    ServerProtocol = field("ServerProtocol")
    Subdirectory = field("Subdirectory")
    ServerHostname = field("ServerHostname")
    AccessKey = field("AccessKey")
    SecretKey = field("SecretKey")
    AgentArns = field("AgentArns")
    ServerCertificate = field("ServerCertificate")

    @cached_property
    def CmkSecretConfig(self):  # pragma: no cover
        return CmkSecretConfig.make_one(self.boto3_raw_data["CmkSecretConfig"])

    @cached_property
    def CustomSecretConfig(self):  # pragma: no cover
        return CustomSecretConfig.make_one(self.boto3_raw_data["CustomSecretConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLocationObjectStorageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationObjectStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationHdfsRequest:
    boto3_raw_data: "type_defs.CreateLocationHdfsRequestTypeDef" = dataclasses.field()

    @cached_property
    def NameNodes(self):  # pragma: no cover
        return HdfsNameNode.make_many(self.boto3_raw_data["NameNodes"])

    AuthenticationType = field("AuthenticationType")
    AgentArns = field("AgentArns")
    Subdirectory = field("Subdirectory")
    BlockSize = field("BlockSize")
    ReplicationFactor = field("ReplicationFactor")
    KmsKeyProviderUri = field("KmsKeyProviderUri")

    @cached_property
    def QopConfiguration(self):  # pragma: no cover
        return QopConfiguration.make_one(self.boto3_raw_data["QopConfiguration"])

    SimpleUser = field("SimpleUser")
    KerberosPrincipal = field("KerberosPrincipal")
    KerberosKeytab = field("KerberosKeytab")
    KerberosKrb5Conf = field("KerberosKrb5Conf")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationHdfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationHdfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationHdfsResponse:
    boto3_raw_data: "type_defs.DescribeLocationHdfsResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")

    @cached_property
    def NameNodes(self):  # pragma: no cover
        return HdfsNameNode.make_many(self.boto3_raw_data["NameNodes"])

    BlockSize = field("BlockSize")
    ReplicationFactor = field("ReplicationFactor")
    KmsKeyProviderUri = field("KmsKeyProviderUri")

    @cached_property
    def QopConfiguration(self):  # pragma: no cover
        return QopConfiguration.make_one(self.boto3_raw_data["QopConfiguration"])

    AuthenticationType = field("AuthenticationType")
    SimpleUser = field("SimpleUser")
    KerberosPrincipal = field("KerberosPrincipal")
    AgentArns = field("AgentArns")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationHdfsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationHdfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationHdfsRequest:
    boto3_raw_data: "type_defs.UpdateLocationHdfsRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")

    @cached_property
    def NameNodes(self):  # pragma: no cover
        return HdfsNameNode.make_many(self.boto3_raw_data["NameNodes"])

    BlockSize = field("BlockSize")
    ReplicationFactor = field("ReplicationFactor")
    KmsKeyProviderUri = field("KmsKeyProviderUri")

    @cached_property
    def QopConfiguration(self):  # pragma: no cover
        return QopConfiguration.make_one(self.boto3_raw_data["QopConfiguration"])

    AuthenticationType = field("AuthenticationType")
    SimpleUser = field("SimpleUser")
    KerberosPrincipal = field("KerberosPrincipal")
    KerberosKeytab = field("KerberosKeytab")
    KerberosKrb5Conf = field("KerberosKrb5Conf")
    AgentArns = field("AgentArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLocationHdfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationHdfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxProtocolNfs:
    boto3_raw_data: "type_defs.FsxProtocolNfsTypeDef" = dataclasses.field()

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return NfsMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FsxProtocolNfsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FsxProtocolNfsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationS3Request:
    boto3_raw_data: "type_defs.CreateLocationS3RequestTypeDef" = dataclasses.field()

    S3BucketArn = field("S3BucketArn")

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    Subdirectory = field("Subdirectory")
    S3StorageClass = field("S3StorageClass")
    AgentArns = field("AgentArns")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationS3RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationS3RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationS3Response:
    boto3_raw_data: "type_defs.DescribeLocationS3ResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    S3StorageClass = field("S3StorageClass")

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    AgentArns = field("AgentArns")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationS3ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationS3ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationS3Request:
    boto3_raw_data: "type_defs.UpdateLocationS3RequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")
    S3StorageClass = field("S3StorageClass")

    @cached_property
    def S3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["S3Config"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLocationS3RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationS3RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationSmbRequest:
    boto3_raw_data: "type_defs.CreateLocationSmbRequestTypeDef" = dataclasses.field()

    Subdirectory = field("Subdirectory")
    ServerHostname = field("ServerHostname")
    AgentArns = field("AgentArns")
    User = field("User")
    Domain = field("Domain")
    Password = field("Password")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return SmbMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    AuthenticationType = field("AuthenticationType")
    DnsIpAddresses = field("DnsIpAddresses")
    KerberosPrincipal = field("KerberosPrincipal")
    KerberosKeytab = field("KerberosKeytab")
    KerberosKrb5Conf = field("KerberosKrb5Conf")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationSmbRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationSmbRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationSmbResponse:
    boto3_raw_data: "type_defs.DescribeLocationSmbResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    AgentArns = field("AgentArns")
    User = field("User")
    Domain = field("Domain")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return SmbMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    CreationTime = field("CreationTime")
    DnsIpAddresses = field("DnsIpAddresses")
    KerberosPrincipal = field("KerberosPrincipal")
    AuthenticationType = field("AuthenticationType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationSmbResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationSmbResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxProtocolSmb:
    boto3_raw_data: "type_defs.FsxProtocolSmbTypeDef" = dataclasses.field()

    Password = field("Password")
    User = field("User")
    Domain = field("Domain")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return SmbMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FsxProtocolSmbTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FsxProtocolSmbTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxUpdateProtocolSmb:
    boto3_raw_data: "type_defs.FsxUpdateProtocolSmbTypeDef" = dataclasses.field()

    Domain = field("Domain")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return SmbMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    Password = field("Password")
    User = field("User")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FsxUpdateProtocolSmbTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FsxUpdateProtocolSmbTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationSmbRequest:
    boto3_raw_data: "type_defs.UpdateLocationSmbRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")
    ServerHostname = field("ServerHostname")
    User = field("User")
    Domain = field("Domain")
    Password = field("Password")
    AgentArns = field("AgentArns")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return SmbMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    AuthenticationType = field("AuthenticationType")
    DnsIpAddresses = field("DnsIpAddresses")
    KerberosPrincipal = field("KerberosPrincipal")
    KerberosKeytab = field("KerberosKeytab")
    KerberosKrb5Conf = field("KerberosKrb5Conf")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLocationSmbRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationSmbRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskExecutionRequest:
    boto3_raw_data: "type_defs.UpdateTaskExecutionRequestTypeDef" = dataclasses.field()

    TaskExecutionArn = field("TaskExecutionArn")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAgentResponse:
    boto3_raw_data: "type_defs.DescribeAgentResponseTypeDef" = dataclasses.field()

    AgentArn = field("AgentArn")
    Name = field("Name")
    Status = field("Status")
    LastConnectionTime = field("LastConnectionTime")
    CreationTime = field("CreationTime")
    EndpointType = field("EndpointType")

    @cached_property
    def PrivateLinkConfig(self):  # pragma: no cover
        return PrivateLinkConfig.make_one(self.boto3_raw_data["PrivateLinkConfig"])

    @cached_property
    def Platform(self):  # pragma: no cover
        return Platform.make_one(self.boto3_raw_data["Platform"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationAzureBlobResponse:
    boto3_raw_data: "type_defs.DescribeLocationAzureBlobResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    AuthenticationType = field("AuthenticationType")
    BlobType = field("BlobType")
    AccessTier = field("AccessTier")
    AgentArns = field("AgentArns")
    CreationTime = field("CreationTime")

    @cached_property
    def ManagedSecretConfig(self):  # pragma: no cover
        return ManagedSecretConfig.make_one(self.boto3_raw_data["ManagedSecretConfig"])

    @cached_property
    def CmkSecretConfig(self):  # pragma: no cover
        return CmkSecretConfig.make_one(self.boto3_raw_data["CmkSecretConfig"])

    @cached_property
    def CustomSecretConfig(self):  # pragma: no cover
        return CustomSecretConfig.make_one(self.boto3_raw_data["CustomSecretConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationAzureBlobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationAzureBlobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationObjectStorageResponse:
    boto3_raw_data: "type_defs.DescribeLocationObjectStorageResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    AccessKey = field("AccessKey")
    ServerPort = field("ServerPort")
    ServerProtocol = field("ServerProtocol")
    AgentArns = field("AgentArns")
    CreationTime = field("CreationTime")
    ServerCertificate = field("ServerCertificate")

    @cached_property
    def ManagedSecretConfig(self):  # pragma: no cover
        return ManagedSecretConfig.make_one(self.boto3_raw_data["ManagedSecretConfig"])

    @cached_property
    def CmkSecretConfig(self):  # pragma: no cover
        return CmkSecretConfig.make_one(self.boto3_raw_data["CmkSecretConfig"])

    @cached_property
    def CustomSecretConfig(self):  # pragma: no cover
        return CustomSecretConfig.make_one(self.boto3_raw_data["CustomSecretConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationObjectStorageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationObjectStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationEfsResponse:
    boto3_raw_data: "type_defs.DescribeLocationEfsResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")

    @cached_property
    def Ec2Config(self):  # pragma: no cover
        return Ec2ConfigOutput.make_one(self.boto3_raw_data["Ec2Config"])

    CreationTime = field("CreationTime")
    AccessPointArn = field("AccessPointArn")
    FileSystemAccessRoleArn = field("FileSystemAccessRoleArn")
    InTransitEncryption = field("InTransitEncryption")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationEfsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationEfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationNfsResponse:
    boto3_raw_data: "type_defs.DescribeLocationNfsResponseTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")

    @cached_property
    def OnPremConfig(self):  # pragma: no cover
        return OnPremConfigOutput.make_one(self.boto3_raw_data["OnPremConfig"])

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return NfsMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLocationNfsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationNfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentsRequestPaginateTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class ListTaskExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListTaskExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TaskArn = field("TaskArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTaskExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocationsRequestPaginate:
    boto3_raw_data: "type_defs.ListLocationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return LocationFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocationsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocationsRequest:
    boto3_raw_data: "type_defs.ListLocationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return LocationFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLocationsResponse:
    boto3_raw_data: "type_defs.ListLocationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Locations(self):  # pragma: no cover
        return LocationListEntry.make_many(self.boto3_raw_data["Locations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLocationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLocationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskExecutionsResponse:
    boto3_raw_data: "type_defs.ListTaskExecutionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def TaskExecutions(self):  # pragma: no cover
        return TaskExecutionListEntry.make_many(self.boto3_raw_data["TaskExecutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaskExecutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksRequestPaginate:
    boto3_raw_data: "type_defs.ListTasksRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return TaskFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTasksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksRequest:
    boto3_raw_data: "type_defs.ListTasksRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return TaskFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksResponse:
    boto3_raw_data: "type_defs.ListTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tasks(self):  # pragma: no cover
        return TaskListEntry.make_many(self.boto3_raw_data["Tasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportDestination:
    boto3_raw_data: "type_defs.ReportDestinationTypeDef" = dataclasses.field()

    @cached_property
    def S3(self):  # pragma: no cover
        return ReportDestinationS3.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportOverrides:
    boto3_raw_data: "type_defs.ReportOverridesTypeDef" = dataclasses.field()

    @cached_property
    def Transferred(self):  # pragma: no cover
        return ReportOverride.make_one(self.boto3_raw_data["Transferred"])

    @cached_property
    def Verified(self):  # pragma: no cover
        return ReportOverride.make_one(self.boto3_raw_data["Verified"])

    @cached_property
    def Deleted(self):  # pragma: no cover
        return ReportOverride.make_one(self.boto3_raw_data["Deleted"])

    @cached_property
    def Skipped(self):  # pragma: no cover
        return ReportOverride.make_one(self.boto3_raw_data["Skipped"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReportOverridesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReportOverridesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceManifestConfig:
    boto3_raw_data: "type_defs.SourceManifestConfigTypeDef" = dataclasses.field()

    @cached_property
    def S3(self):  # pragma: no cover
        return S3ManifestConfig.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceManifestConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceManifestConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentsResponse:
    boto3_raw_data: "type_defs.ListAgentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Agents(self):  # pragma: no cover
        return AgentListEntry.make_many(self.boto3_raw_data["Agents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxProtocol:
    boto3_raw_data: "type_defs.FsxProtocolTypeDef" = dataclasses.field()

    @cached_property
    def NFS(self):  # pragma: no cover
        return FsxProtocolNfs.make_one(self.boto3_raw_data["NFS"])

    @cached_property
    def SMB(self):  # pragma: no cover
        return FsxProtocolSmb.make_one(self.boto3_raw_data["SMB"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FsxProtocolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FsxProtocolTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FsxUpdateProtocol:
    boto3_raw_data: "type_defs.FsxUpdateProtocolTypeDef" = dataclasses.field()

    @cached_property
    def NFS(self):  # pragma: no cover
        return FsxProtocolNfs.make_one(self.boto3_raw_data["NFS"])

    @cached_property
    def SMB(self):  # pragma: no cover
        return FsxUpdateProtocolSmb.make_one(self.boto3_raw_data["SMB"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FsxUpdateProtocolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FsxUpdateProtocolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationEfsRequest:
    boto3_raw_data: "type_defs.CreateLocationEfsRequestTypeDef" = dataclasses.field()

    EfsFilesystemArn = field("EfsFilesystemArn")
    Ec2Config = field("Ec2Config")
    Subdirectory = field("Subdirectory")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    AccessPointArn = field("AccessPointArn")
    FileSystemAccessRoleArn = field("FileSystemAccessRoleArn")
    InTransitEncryption = field("InTransitEncryption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationEfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationEfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationNfsRequest:
    boto3_raw_data: "type_defs.CreateLocationNfsRequestTypeDef" = dataclasses.field()

    Subdirectory = field("Subdirectory")
    ServerHostname = field("ServerHostname")
    OnPremConfig = field("OnPremConfig")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return NfsMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLocationNfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationNfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationNfsRequest:
    boto3_raw_data: "type_defs.UpdateLocationNfsRequestTypeDef" = dataclasses.field()

    LocationArn = field("LocationArn")
    Subdirectory = field("Subdirectory")
    ServerHostname = field("ServerHostname")
    OnPremConfig = field("OnPremConfig")

    @cached_property
    def MountOptions(self):  # pragma: no cover
        return NfsMountOptions.make_one(self.boto3_raw_data["MountOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLocationNfsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationNfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskReportConfig:
    boto3_raw_data: "type_defs.TaskReportConfigTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return ReportDestination.make_one(self.boto3_raw_data["Destination"])

    OutputType = field("OutputType")
    ReportLevel = field("ReportLevel")
    ObjectVersionIds = field("ObjectVersionIds")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return ReportOverrides.make_one(self.boto3_raw_data["Overrides"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskReportConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskReportConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManifestConfig:
    boto3_raw_data: "type_defs.ManifestConfigTypeDef" = dataclasses.field()

    Action = field("Action")
    Format = field("Format")

    @cached_property
    def Source(self):  # pragma: no cover
        return SourceManifestConfig.make_one(self.boto3_raw_data["Source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManifestConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManifestConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxOntapRequest:
    boto3_raw_data: "type_defs.CreateLocationFsxOntapRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Protocol(self):  # pragma: no cover
        return FsxProtocol.make_one(self.boto3_raw_data["Protocol"])

    SecurityGroupArns = field("SecurityGroupArns")
    StorageVirtualMachineArn = field("StorageVirtualMachineArn")
    Subdirectory = field("Subdirectory")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxOntapRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxOntapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLocationFsxOpenZfsRequest:
    boto3_raw_data: "type_defs.CreateLocationFsxOpenZfsRequestTypeDef" = (
        dataclasses.field()
    )

    FsxFilesystemArn = field("FsxFilesystemArn")

    @cached_property
    def Protocol(self):  # pragma: no cover
        return FsxProtocol.make_one(self.boto3_raw_data["Protocol"])

    SecurityGroupArns = field("SecurityGroupArns")
    Subdirectory = field("Subdirectory")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLocationFsxOpenZfsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLocationFsxOpenZfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxOntapResponse:
    boto3_raw_data: "type_defs.DescribeLocationFsxOntapResponseTypeDef" = (
        dataclasses.field()
    )

    CreationTime = field("CreationTime")
    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")

    @cached_property
    def Protocol(self):  # pragma: no cover
        return FsxProtocol.make_one(self.boto3_raw_data["Protocol"])

    SecurityGroupArns = field("SecurityGroupArns")
    StorageVirtualMachineArn = field("StorageVirtualMachineArn")
    FsxFilesystemArn = field("FsxFilesystemArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLocationFsxOntapResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxOntapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLocationFsxOpenZfsResponse:
    boto3_raw_data: "type_defs.DescribeLocationFsxOpenZfsResponseTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")
    LocationUri = field("LocationUri")
    SecurityGroupArns = field("SecurityGroupArns")

    @cached_property
    def Protocol(self):  # pragma: no cover
        return FsxProtocol.make_one(self.boto3_raw_data["Protocol"])

    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLocationFsxOpenZfsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLocationFsxOpenZfsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationFsxOpenZfsRequest:
    boto3_raw_data: "type_defs.UpdateLocationFsxOpenZfsRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def Protocol(self):  # pragma: no cover
        return FsxProtocol.make_one(self.boto3_raw_data["Protocol"])

    Subdirectory = field("Subdirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLocationFsxOpenZfsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationFsxOpenZfsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLocationFsxOntapRequest:
    boto3_raw_data: "type_defs.UpdateLocationFsxOntapRequestTypeDef" = (
        dataclasses.field()
    )

    LocationArn = field("LocationArn")

    @cached_property
    def Protocol(self):  # pragma: no cover
        return FsxUpdateProtocol.make_one(self.boto3_raw_data["Protocol"])

    Subdirectory = field("Subdirectory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLocationFsxOntapRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLocationFsxOntapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTaskRequest:
    boto3_raw_data: "type_defs.CreateTaskRequestTypeDef" = dataclasses.field()

    SourceLocationArn = field("SourceLocationArn")
    DestinationLocationArn = field("DestinationLocationArn")
    CloudWatchLogGroupArn = field("CloudWatchLogGroupArn")
    Name = field("Name")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Excludes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Excludes"])

    @cached_property
    def Schedule(self):  # pragma: no cover
        return TaskSchedule.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def Includes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Includes"])

    @cached_property
    def ManifestConfig(self):  # pragma: no cover
        return ManifestConfig.make_one(self.boto3_raw_data["ManifestConfig"])

    @cached_property
    def TaskReportConfig(self):  # pragma: no cover
        return TaskReportConfig.make_one(self.boto3_raw_data["TaskReportConfig"])

    TaskMode = field("TaskMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskExecutionResponse:
    boto3_raw_data: "type_defs.DescribeTaskExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    TaskExecutionArn = field("TaskExecutionArn")
    Status = field("Status")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Excludes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Excludes"])

    @cached_property
    def Includes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Includes"])

    @cached_property
    def ManifestConfig(self):  # pragma: no cover
        return ManifestConfig.make_one(self.boto3_raw_data["ManifestConfig"])

    StartTime = field("StartTime")
    EstimatedFilesToTransfer = field("EstimatedFilesToTransfer")
    EstimatedBytesToTransfer = field("EstimatedBytesToTransfer")
    FilesTransferred = field("FilesTransferred")
    BytesWritten = field("BytesWritten")
    BytesTransferred = field("BytesTransferred")
    BytesCompressed = field("BytesCompressed")

    @cached_property
    def Result(self):  # pragma: no cover
        return TaskExecutionResultDetail.make_one(self.boto3_raw_data["Result"])

    @cached_property
    def TaskReportConfig(self):  # pragma: no cover
        return TaskReportConfig.make_one(self.boto3_raw_data["TaskReportConfig"])

    FilesDeleted = field("FilesDeleted")
    FilesSkipped = field("FilesSkipped")
    FilesVerified = field("FilesVerified")

    @cached_property
    def ReportResult(self):  # pragma: no cover
        return ReportResult.make_one(self.boto3_raw_data["ReportResult"])

    EstimatedFilesToDelete = field("EstimatedFilesToDelete")
    TaskMode = field("TaskMode")
    FilesPrepared = field("FilesPrepared")

    @cached_property
    def FilesListed(self):  # pragma: no cover
        return TaskExecutionFilesListedDetail.make_one(
            self.boto3_raw_data["FilesListed"]
        )

    @cached_property
    def FilesFailed(self):  # pragma: no cover
        return TaskExecutionFilesFailedDetail.make_one(
            self.boto3_raw_data["FilesFailed"]
        )

    LaunchTime = field("LaunchTime")
    EndTime = field("EndTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTaskExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskResponse:
    boto3_raw_data: "type_defs.DescribeTaskResponseTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")
    Status = field("Status")
    Name = field("Name")
    CurrentTaskExecutionArn = field("CurrentTaskExecutionArn")
    SourceLocationArn = field("SourceLocationArn")
    DestinationLocationArn = field("DestinationLocationArn")
    CloudWatchLogGroupArn = field("CloudWatchLogGroupArn")
    SourceNetworkInterfaceArns = field("SourceNetworkInterfaceArns")
    DestinationNetworkInterfaceArns = field("DestinationNetworkInterfaceArns")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Excludes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Excludes"])

    @cached_property
    def Schedule(self):  # pragma: no cover
        return TaskSchedule.make_one(self.boto3_raw_data["Schedule"])

    ErrorCode = field("ErrorCode")
    ErrorDetail = field("ErrorDetail")
    CreationTime = field("CreationTime")

    @cached_property
    def Includes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Includes"])

    @cached_property
    def ManifestConfig(self):  # pragma: no cover
        return ManifestConfig.make_one(self.boto3_raw_data["ManifestConfig"])

    @cached_property
    def TaskReportConfig(self):  # pragma: no cover
        return TaskReportConfig.make_one(self.boto3_raw_data["TaskReportConfig"])

    @cached_property
    def ScheduleDetails(self):  # pragma: no cover
        return TaskScheduleDetails.make_one(self.boto3_raw_data["ScheduleDetails"])

    TaskMode = field("TaskMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTaskExecutionRequest:
    boto3_raw_data: "type_defs.StartTaskExecutionRequestTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")

    @cached_property
    def OverrideOptions(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["OverrideOptions"])

    @cached_property
    def Includes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Includes"])

    @cached_property
    def Excludes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Excludes"])

    @cached_property
    def ManifestConfig(self):  # pragma: no cover
        return ManifestConfig.make_one(self.boto3_raw_data["ManifestConfig"])

    @cached_property
    def TaskReportConfig(self):  # pragma: no cover
        return TaskReportConfig.make_one(self.boto3_raw_data["TaskReportConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagListEntry.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTaskExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTaskExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskRequest:
    boto3_raw_data: "type_defs.UpdateTaskRequestTypeDef" = dataclasses.field()

    TaskArn = field("TaskArn")

    @cached_property
    def Options(self):  # pragma: no cover
        return Options.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Excludes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Excludes"])

    @cached_property
    def Schedule(self):  # pragma: no cover
        return TaskSchedule.make_one(self.boto3_raw_data["Schedule"])

    Name = field("Name")
    CloudWatchLogGroupArn = field("CloudWatchLogGroupArn")

    @cached_property
    def Includes(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["Includes"])

    @cached_property
    def ManifestConfig(self):  # pragma: no cover
        return ManifestConfig.make_one(self.boto3_raw_data["ManifestConfig"])

    @cached_property
    def TaskReportConfig(self):  # pragma: no cover
        return TaskReportConfig.make_one(self.boto3_raw_data["TaskReportConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
