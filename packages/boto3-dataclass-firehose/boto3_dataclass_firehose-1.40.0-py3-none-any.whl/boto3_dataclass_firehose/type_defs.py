# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_firehose import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AmazonOpenSearchServerlessBufferingHints:
    boto3_raw_data: "type_defs.AmazonOpenSearchServerlessBufferingHintsTypeDef" = (
        dataclasses.field()
    )

    IntervalInSeconds = field("IntervalInSeconds")
    SizeInMBs = field("SizeInMBs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonOpenSearchServerlessBufferingHintsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonOpenSearchServerlessBufferingHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonOpenSearchServerlessRetryOptions:
    boto3_raw_data: "type_defs.AmazonOpenSearchServerlessRetryOptionsTypeDef" = (
        dataclasses.field()
    )

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonOpenSearchServerlessRetryOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonOpenSearchServerlessRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLoggingOptions:
    boto3_raw_data: "type_defs.CloudWatchLoggingOptionsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    LogGroupName = field("LogGroupName")
    LogStreamName = field("LogStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLoggingOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLoggingOptionsTypeDef"]
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

    SubnetIds = field("SubnetIds")
    RoleARN = field("RoleARN")
    SecurityGroupIds = field("SecurityGroupIds")

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
class VpcConfigurationDescription:
    boto3_raw_data: "type_defs.VpcConfigurationDescriptionTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    RoleARN = field("RoleARN")
    SecurityGroupIds = field("SecurityGroupIds")
    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonopensearchserviceBufferingHints:
    boto3_raw_data: "type_defs.AmazonopensearchserviceBufferingHintsTypeDef" = (
        dataclasses.field()
    )

    IntervalInSeconds = field("IntervalInSeconds")
    SizeInMBs = field("SizeInMBs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonopensearchserviceBufferingHintsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonopensearchserviceBufferingHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonopensearchserviceRetryOptions:
    boto3_raw_data: "type_defs.AmazonopensearchserviceRetryOptionsTypeDef" = (
        dataclasses.field()
    )

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonopensearchserviceRetryOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonopensearchserviceRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentIdOptions:
    boto3_raw_data: "type_defs.DocumentIdOptionsTypeDef" = dataclasses.field()

    DefaultDocumentIdFormat = field("DefaultDocumentIdFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentIdOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentIdOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfiguration:
    boto3_raw_data: "type_defs.AuthenticationConfigurationTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    Connectivity = field("Connectivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BufferingHints:
    boto3_raw_data: "type_defs.BufferingHintsTypeDef" = dataclasses.field()

    SizeInMBs = field("SizeInMBs")
    IntervalInSeconds = field("IntervalInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BufferingHintsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BufferingHintsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CatalogConfiguration:
    boto3_raw_data: "type_defs.CatalogConfigurationTypeDef" = dataclasses.field()

    CatalogARN = field("CatalogARN")
    WarehouseLocation = field("WarehouseLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CatalogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CatalogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyCommand:
    boto3_raw_data: "type_defs.CopyCommandTypeDef" = dataclasses.field()

    DataTableName = field("DataTableName")
    DataTableColumns = field("DataTableColumns")
    CopyOptions = field("CopyOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyCommandTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyCommandTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryStreamEncryptionConfigurationInput:
    boto3_raw_data: "type_defs.DeliveryStreamEncryptionConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    KeyType = field("KeyType")
    KeyARN = field("KeyARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeliveryStreamEncryptionConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliveryStreamEncryptionConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectPutSourceConfiguration:
    boto3_raw_data: "type_defs.DirectPutSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    ThroughputHintInMBs = field("ThroughputHintInMBs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectPutSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectPutSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamSourceConfiguration:
    boto3_raw_data: "type_defs.KinesisStreamSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    KinesisStreamARN = field("KinesisStreamARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamSourceConfigurationTypeDef"]
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
class SchemaConfiguration:
    boto3_raw_data: "type_defs.SchemaConfigurationTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    CatalogId = field("CatalogId")
    DatabaseName = field("DatabaseName")
    TableName = field("TableName")
    Region = field("Region")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseColumnListOutput:
    boto3_raw_data: "type_defs.DatabaseColumnListOutputTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseColumnListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseColumnListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseColumnList:
    boto3_raw_data: "type_defs.DatabaseColumnListTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseColumnListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseColumnListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseListOutput:
    boto3_raw_data: "type_defs.DatabaseListOutputTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseList:
    boto3_raw_data: "type_defs.DatabaseListTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatabaseListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureDescription:
    boto3_raw_data: "type_defs.FailureDescriptionTypeDef" = dataclasses.field()

    Type = field("Type")
    Details = field("Details")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailureDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailureDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecretsManagerConfiguration:
    boto3_raw_data: "type_defs.SecretsManagerConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SecretARN = field("SecretARN")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecretsManagerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecretsManagerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseSourceVPCConfiguration:
    boto3_raw_data: "type_defs.DatabaseSourceVPCConfigurationTypeDef" = (
        dataclasses.field()
    )

    VpcEndpointServiceName = field("VpcEndpointServiceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DatabaseSourceVPCConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseSourceVPCConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseTableListOutput:
    boto3_raw_data: "type_defs.DatabaseTableListOutputTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseTableListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseTableListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseTableList:
    boto3_raw_data: "type_defs.DatabaseTableListTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseTableListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseTableListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeliveryStreamInput:
    boto3_raw_data: "type_defs.DeleteDeliveryStreamInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")
    AllowForceDelete = field("AllowForceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeliveryStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeliveryStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryStreamInput:
    boto3_raw_data: "type_defs.DescribeDeliveryStreamInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")
    Limit = field("Limit")
    ExclusiveStartDestinationId = field("ExclusiveStartDestinationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeliveryStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HiveJsonSerDeOutput:
    boto3_raw_data: "type_defs.HiveJsonSerDeOutputTypeDef" = dataclasses.field()

    TimestampFormats = field("TimestampFormats")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HiveJsonSerDeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HiveJsonSerDeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenXJsonSerDeOutput:
    boto3_raw_data: "type_defs.OpenXJsonSerDeOutputTypeDef" = dataclasses.field()

    ConvertDotsInJsonKeysToUnderscores = field("ConvertDotsInJsonKeysToUnderscores")
    CaseInsensitive = field("CaseInsensitive")
    ColumnToJsonKeyMappings = field("ColumnToJsonKeyMappings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenXJsonSerDeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenXJsonSerDeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectPutSourceDescription:
    boto3_raw_data: "type_defs.DirectPutSourceDescriptionTypeDef" = dataclasses.field()

    ThroughputHintInMBs = field("ThroughputHintInMBs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectPutSourceDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectPutSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryOptions:
    boto3_raw_data: "type_defs.RetryOptionsTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchBufferingHints:
    boto3_raw_data: "type_defs.ElasticsearchBufferingHintsTypeDef" = dataclasses.field()

    IntervalInSeconds = field("IntervalInSeconds")
    SizeInMBs = field("SizeInMBs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchBufferingHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchBufferingHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchRetryOptions:
    boto3_raw_data: "type_defs.ElasticsearchRetryOptionsTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchRetryOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KMSEncryptionConfig:
    boto3_raw_data: "type_defs.KMSEncryptionConfigTypeDef" = dataclasses.field()

    AWSKMSKeyARN = field("AWSKMSKeyARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KMSEncryptionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KMSEncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HiveJsonSerDe:
    boto3_raw_data: "type_defs.HiveJsonSerDeTypeDef" = dataclasses.field()

    TimestampFormats = field("TimestampFormats")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HiveJsonSerDeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HiveJsonSerDeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointBufferingHints:
    boto3_raw_data: "type_defs.HttpEndpointBufferingHintsTypeDef" = dataclasses.field()

    SizeInMBs = field("SizeInMBs")
    IntervalInSeconds = field("IntervalInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpEndpointBufferingHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointBufferingHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointCommonAttribute:
    boto3_raw_data: "type_defs.HttpEndpointCommonAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpEndpointCommonAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointCommonAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointConfiguration:
    boto3_raw_data: "type_defs.HttpEndpointConfigurationTypeDef" = dataclasses.field()

    Url = field("Url")
    Name = field("Name")
    AccessKey = field("AccessKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpEndpointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointDescription:
    boto3_raw_data: "type_defs.HttpEndpointDescriptionTypeDef" = dataclasses.field()

    Url = field("Url")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpEndpointDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointRetryOptions:
    boto3_raw_data: "type_defs.HttpEndpointRetryOptionsTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpEndpointRetryOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaEvolutionConfiguration:
    boto3_raw_data: "type_defs.SchemaEvolutionConfigurationTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaEvolutionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaEvolutionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableCreationConfiguration:
    boto3_raw_data: "type_defs.TableCreationConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableCreationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableCreationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisStreamSourceDescription:
    boto3_raw_data: "type_defs.KinesisStreamSourceDescriptionTypeDef" = (
        dataclasses.field()
    )

    KinesisStreamARN = field("KinesisStreamARN")
    RoleARN = field("RoleARN")
    DeliveryStartTimestamp = field("DeliveryStartTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisStreamSourceDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisStreamSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeliveryStreamsInput:
    boto3_raw_data: "type_defs.ListDeliveryStreamsInputTypeDef" = dataclasses.field()

    Limit = field("Limit")
    DeliveryStreamType = field("DeliveryStreamType")
    ExclusiveStartDeliveryStreamName = field("ExclusiveStartDeliveryStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeliveryStreamsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeliveryStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForDeliveryStreamInput:
    boto3_raw_data: "type_defs.ListTagsForDeliveryStreamInputTypeDef" = (
        dataclasses.field()
    )

    DeliveryStreamName = field("DeliveryStreamName")
    ExclusiveStartTagKey = field("ExclusiveStartTagKey")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForDeliveryStreamInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForDeliveryStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenXJsonSerDe:
    boto3_raw_data: "type_defs.OpenXJsonSerDeTypeDef" = dataclasses.field()

    ConvertDotsInJsonKeysToUnderscores = field("ConvertDotsInJsonKeysToUnderscores")
    CaseInsensitive = field("CaseInsensitive")
    ColumnToJsonKeyMappings = field("ColumnToJsonKeyMappings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenXJsonSerDeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenXJsonSerDeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrcSerDeOutput:
    boto3_raw_data: "type_defs.OrcSerDeOutputTypeDef" = dataclasses.field()

    StripeSizeBytes = field("StripeSizeBytes")
    BlockSizeBytes = field("BlockSizeBytes")
    RowIndexStride = field("RowIndexStride")
    EnablePadding = field("EnablePadding")
    PaddingTolerance = field("PaddingTolerance")
    Compression = field("Compression")
    BloomFilterColumns = field("BloomFilterColumns")
    BloomFilterFalsePositiveProbability = field("BloomFilterFalsePositiveProbability")
    DictionaryKeyThreshold = field("DictionaryKeyThreshold")
    FormatVersion = field("FormatVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrcSerDeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrcSerDeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrcSerDe:
    boto3_raw_data: "type_defs.OrcSerDeTypeDef" = dataclasses.field()

    StripeSizeBytes = field("StripeSizeBytes")
    BlockSizeBytes = field("BlockSizeBytes")
    RowIndexStride = field("RowIndexStride")
    EnablePadding = field("EnablePadding")
    PaddingTolerance = field("PaddingTolerance")
    Compression = field("Compression")
    BloomFilterColumns = field("BloomFilterColumns")
    BloomFilterFalsePositiveProbability = field("BloomFilterFalsePositiveProbability")
    DictionaryKeyThreshold = field("DictionaryKeyThreshold")
    FormatVersion = field("FormatVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrcSerDeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrcSerDeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParquetSerDe:
    boto3_raw_data: "type_defs.ParquetSerDeTypeDef" = dataclasses.field()

    BlockSizeBytes = field("BlockSizeBytes")
    PageSizeBytes = field("PageSizeBytes")
    Compression = field("Compression")
    EnableDictionaryCompression = field("EnableDictionaryCompression")
    MaxPaddingBytes = field("MaxPaddingBytes")
    WriterVersion = field("WriterVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParquetSerDeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParquetSerDeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionField:
    boto3_raw_data: "type_defs.PartitionFieldTypeDef" = dataclasses.field()

    SourceName = field("SourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartitionFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessorParameter:
    boto3_raw_data: "type_defs.ProcessorParameterTypeDef" = dataclasses.field()

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProcessorParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProcessorParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordBatchResponseEntry:
    boto3_raw_data: "type_defs.PutRecordBatchResponseEntryTypeDef" = dataclasses.field()

    RecordId = field("RecordId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRecordBatchResponseEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordBatchResponseEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftRetryOptions:
    boto3_raw_data: "type_defs.RedshiftRetryOptionsTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftRetryOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeBufferingHints:
    boto3_raw_data: "type_defs.SnowflakeBufferingHintsTypeDef" = dataclasses.field()

    SizeInMBs = field("SizeInMBs")
    IntervalInSeconds = field("IntervalInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeBufferingHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeBufferingHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeRetryOptions:
    boto3_raw_data: "type_defs.SnowflakeRetryOptionsTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeRetryOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeRoleConfiguration:
    boto3_raw_data: "type_defs.SnowflakeRoleConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SnowflakeRole = field("SnowflakeRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeRoleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeRoleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeVpcConfiguration:
    boto3_raw_data: "type_defs.SnowflakeVpcConfigurationTypeDef" = dataclasses.field()

    PrivateLinkVpceId = field("PrivateLinkVpceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeVpcConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplunkBufferingHints:
    boto3_raw_data: "type_defs.SplunkBufferingHintsTypeDef" = dataclasses.field()

    IntervalInSeconds = field("IntervalInSeconds")
    SizeInMBs = field("SizeInMBs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SplunkBufferingHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplunkBufferingHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplunkRetryOptions:
    boto3_raw_data: "type_defs.SplunkRetryOptionsTypeDef" = dataclasses.field()

    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SplunkRetryOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplunkRetryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDeliveryStreamEncryptionInput:
    boto3_raw_data: "type_defs.StopDeliveryStreamEncryptionInputTypeDef" = (
        dataclasses.field()
    )

    DeliveryStreamName = field("DeliveryStreamName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopDeliveryStreamEncryptionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDeliveryStreamEncryptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagDeliveryStreamInput:
    boto3_raw_data: "type_defs.UntagDeliveryStreamInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagDeliveryStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagDeliveryStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MSKSourceDescription:
    boto3_raw_data: "type_defs.MSKSourceDescriptionTypeDef" = dataclasses.field()

    MSKClusterARN = field("MSKClusterARN")
    TopicName = field("TopicName")

    @cached_property
    def AuthenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["AuthenticationConfiguration"]
        )

    DeliveryStartTimestamp = field("DeliveryStartTimestamp")
    ReadFromTimestamp = field("ReadFromTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MSKSourceDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MSKSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    Data = field("Data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeliveryStreamEncryptionInput:
    boto3_raw_data: "type_defs.StartDeliveryStreamEncryptionInputTypeDef" = (
        dataclasses.field()
    )

    DeliveryStreamName = field("DeliveryStreamName")

    @cached_property
    def DeliveryStreamEncryptionConfigurationInput(self):  # pragma: no cover
        return DeliveryStreamEncryptionConfigurationInput.make_one(
            self.boto3_raw_data["DeliveryStreamEncryptionConfigurationInput"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDeliveryStreamEncryptionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeliveryStreamEncryptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagDeliveryStreamInput:
    boto3_raw_data: "type_defs.TagDeliveryStreamInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagDeliveryStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagDeliveryStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeliveryStreamOutput:
    boto3_raw_data: "type_defs.CreateDeliveryStreamOutputTypeDef" = dataclasses.field()

    DeliveryStreamARN = field("DeliveryStreamARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeliveryStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeliveryStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeliveryStreamsOutput:
    boto3_raw_data: "type_defs.ListDeliveryStreamsOutputTypeDef" = dataclasses.field()

    DeliveryStreamNames = field("DeliveryStreamNames")
    HasMoreDeliveryStreams = field("HasMoreDeliveryStreams")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeliveryStreamsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeliveryStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForDeliveryStreamOutput:
    boto3_raw_data: "type_defs.ListTagsForDeliveryStreamOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    HasMoreTags = field("HasMoreTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForDeliveryStreamOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForDeliveryStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordOutput:
    boto3_raw_data: "type_defs.PutRecordOutputTypeDef" = dataclasses.field()

    RecordId = field("RecordId")
    Encrypted = field("Encrypted")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRecordOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseSnapshotInfo:
    boto3_raw_data: "type_defs.DatabaseSnapshotInfoTypeDef" = dataclasses.field()

    Id = field("Id")
    Table = field("Table")
    RequestTimestamp = field("RequestTimestamp")
    RequestedBy = field("RequestedBy")
    Status = field("Status")

    @cached_property
    def FailureDescription(self):  # pragma: no cover
        return FailureDescription.make_one(self.boto3_raw_data["FailureDescription"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseSnapshotInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseSnapshotInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryStreamEncryptionConfiguration:
    boto3_raw_data: "type_defs.DeliveryStreamEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KeyARN = field("KeyARN")
    KeyType = field("KeyType")
    Status = field("Status")

    @cached_property
    def FailureDescription(self):  # pragma: no cover
        return FailureDescription.make_one(self.boto3_raw_data["FailureDescription"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeliveryStreamEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliveryStreamEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseSourceAuthenticationConfiguration:
    boto3_raw_data: "type_defs.DatabaseSourceAuthenticationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatabaseSourceAuthenticationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseSourceAuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeserializerOutput:
    boto3_raw_data: "type_defs.DeserializerOutputTypeDef" = dataclasses.field()

    @cached_property
    def OpenXJsonSerDe(self):  # pragma: no cover
        return OpenXJsonSerDeOutput.make_one(self.boto3_raw_data["OpenXJsonSerDe"])

    @cached_property
    def HiveJsonSerDe(self):  # pragma: no cover
        return HiveJsonSerDeOutput.make_one(self.boto3_raw_data["HiveJsonSerDe"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeserializerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeserializerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamicPartitioningConfiguration:
    boto3_raw_data: "type_defs.DynamicPartitioningConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DynamicPartitioningConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamicPartitioningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    NoEncryptionConfig = field("NoEncryptionConfig")

    @cached_property
    def KMSEncryptionConfig(self):  # pragma: no cover
        return KMSEncryptionConfig.make_one(self.boto3_raw_data["KMSEncryptionConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointRequestConfigurationOutput:
    boto3_raw_data: "type_defs.HttpEndpointRequestConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    ContentEncoding = field("ContentEncoding")

    @cached_property
    def CommonAttributes(self):  # pragma: no cover
        return HttpEndpointCommonAttribute.make_many(
            self.boto3_raw_data["CommonAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HttpEndpointRequestConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointRequestConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointRequestConfiguration:
    boto3_raw_data: "type_defs.HttpEndpointRequestConfigurationTypeDef" = (
        dataclasses.field()
    )

    ContentEncoding = field("ContentEncoding")

    @cached_property
    def CommonAttributes(self):  # pragma: no cover
        return HttpEndpointCommonAttribute.make_many(
            self.boto3_raw_data["CommonAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpEndpointRequestConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointRequestConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MSKSourceConfiguration:
    boto3_raw_data: "type_defs.MSKSourceConfigurationTypeDef" = dataclasses.field()

    MSKClusterARN = field("MSKClusterARN")
    TopicName = field("TopicName")

    @cached_property
    def AuthenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["AuthenticationConfiguration"]
        )

    ReadFromTimestamp = field("ReadFromTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MSKSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MSKSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SerializerOutput:
    boto3_raw_data: "type_defs.SerializerOutputTypeDef" = dataclasses.field()

    @cached_property
    def ParquetSerDe(self):  # pragma: no cover
        return ParquetSerDe.make_one(self.boto3_raw_data["ParquetSerDe"])

    @cached_property
    def OrcSerDe(self):  # pragma: no cover
        return OrcSerDeOutput.make_one(self.boto3_raw_data["OrcSerDe"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SerializerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SerializerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionSpecOutput:
    boto3_raw_data: "type_defs.PartitionSpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def Identity(self):  # pragma: no cover
        return PartitionField.make_many(self.boto3_raw_data["Identity"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartitionSpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartitionSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionSpec:
    boto3_raw_data: "type_defs.PartitionSpecTypeDef" = dataclasses.field()

    @cached_property
    def Identity(self):  # pragma: no cover
        return PartitionField.make_many(self.boto3_raw_data["Identity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartitionSpecTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessorOutput:
    boto3_raw_data: "type_defs.ProcessorOutputTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ProcessorParameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessorOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Processor:
    boto3_raw_data: "type_defs.ProcessorTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ProcessorParameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordBatchOutput:
    boto3_raw_data: "type_defs.PutRecordBatchOutputTypeDef" = dataclasses.field()

    FailedPutCount = field("FailedPutCount")
    Encrypted = field("Encrypted")

    @cached_property
    def RequestResponses(self):  # pragma: no cover
        return PutRecordBatchResponseEntry.make_many(
            self.boto3_raw_data["RequestResponses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRecordBatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordBatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordBatchInput:
    boto3_raw_data: "type_defs.PutRecordBatchInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRecordBatchInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRecordBatchInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRecordInput:
    boto3_raw_data: "type_defs.PutRecordInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")

    @cached_property
    def Record(self):  # pragma: no cover
        return Record.make_one(self.boto3_raw_data["Record"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRecordInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRecordInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseSourceDescription:
    boto3_raw_data: "type_defs.DatabaseSourceDescriptionTypeDef" = dataclasses.field()

    Type = field("Type")
    Endpoint = field("Endpoint")
    Port = field("Port")
    SSLMode = field("SSLMode")

    @cached_property
    def Databases(self):  # pragma: no cover
        return DatabaseListOutput.make_one(self.boto3_raw_data["Databases"])

    @cached_property
    def Tables(self):  # pragma: no cover
        return DatabaseTableListOutput.make_one(self.boto3_raw_data["Tables"])

    @cached_property
    def Columns(self):  # pragma: no cover
        return DatabaseColumnListOutput.make_one(self.boto3_raw_data["Columns"])

    SurrogateKeys = field("SurrogateKeys")
    SnapshotWatermarkTable = field("SnapshotWatermarkTable")

    @cached_property
    def SnapshotInfo(self):  # pragma: no cover
        return DatabaseSnapshotInfo.make_many(self.boto3_raw_data["SnapshotInfo"])

    @cached_property
    def DatabaseSourceAuthenticationConfiguration(self):  # pragma: no cover
        return DatabaseSourceAuthenticationConfiguration.make_one(
            self.boto3_raw_data["DatabaseSourceAuthenticationConfiguration"]
        )

    @cached_property
    def DatabaseSourceVPCConfiguration(self):  # pragma: no cover
        return DatabaseSourceVPCConfiguration.make_one(
            self.boto3_raw_data["DatabaseSourceVPCConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseSourceDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseSourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseSourceConfiguration:
    boto3_raw_data: "type_defs.DatabaseSourceConfigurationTypeDef" = dataclasses.field()

    Type = field("Type")
    Endpoint = field("Endpoint")
    Port = field("Port")
    Databases = field("Databases")
    Tables = field("Tables")
    SnapshotWatermarkTable = field("SnapshotWatermarkTable")

    @cached_property
    def DatabaseSourceAuthenticationConfiguration(self):  # pragma: no cover
        return DatabaseSourceAuthenticationConfiguration.make_one(
            self.boto3_raw_data["DatabaseSourceAuthenticationConfiguration"]
        )

    @cached_property
    def DatabaseSourceVPCConfiguration(self):  # pragma: no cover
        return DatabaseSourceVPCConfiguration.make_one(
            self.boto3_raw_data["DatabaseSourceVPCConfiguration"]
        )

    SSLMode = field("SSLMode")
    Columns = field("Columns")
    SurrogateKeys = field("SurrogateKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFormatConfigurationOutput:
    boto3_raw_data: "type_defs.InputFormatConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Deserializer(self):  # pragma: no cover
        return DeserializerOutput.make_one(self.boto3_raw_data["Deserializer"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InputFormatConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputFormatConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationConfiguration:
    boto3_raw_data: "type_defs.S3DestinationConfigurationTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")
    Prefix = field("Prefix")
    ErrorOutputPrefix = field("ErrorOutputPrefix")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    CompressionFormat = field("CompressionFormat")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationDescription:
    boto3_raw_data: "type_defs.S3DestinationDescriptionTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    CompressionFormat = field("CompressionFormat")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    Prefix = field("Prefix")
    ErrorOutputPrefix = field("ErrorOutputPrefix")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationUpdate:
    boto3_raw_data: "type_defs.S3DestinationUpdateTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")
    Prefix = field("Prefix")
    ErrorOutputPrefix = field("ErrorOutputPrefix")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    CompressionFormat = field("CompressionFormat")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deserializer:
    boto3_raw_data: "type_defs.DeserializerTypeDef" = dataclasses.field()

    OpenXJsonSerDe = field("OpenXJsonSerDe")
    HiveJsonSerDe = field("HiveJsonSerDe")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeserializerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeserializerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Serializer:
    boto3_raw_data: "type_defs.SerializerTypeDef" = dataclasses.field()

    @cached_property
    def ParquetSerDe(self):  # pragma: no cover
        return ParquetSerDe.make_one(self.boto3_raw_data["ParquetSerDe"])

    OrcSerDe = field("OrcSerDe")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SerializerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SerializerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputFormatConfigurationOutput:
    boto3_raw_data: "type_defs.OutputFormatConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Serializer(self):  # pragma: no cover
        return SerializerOutput.make_one(self.boto3_raw_data["Serializer"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OutputFormatConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputFormatConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationTableConfigurationOutput:
    boto3_raw_data: "type_defs.DestinationTableConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DestinationTableName = field("DestinationTableName")
    DestinationDatabaseName = field("DestinationDatabaseName")
    UniqueKeys = field("UniqueKeys")

    @cached_property
    def PartitionSpec(self):  # pragma: no cover
        return PartitionSpecOutput.make_one(self.boto3_raw_data["PartitionSpec"])

    S3ErrorOutputPrefix = field("S3ErrorOutputPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DestinationTableConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationTableConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessingConfigurationOutput:
    boto3_raw_data: "type_defs.ProcessingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Enabled = field("Enabled")

    @cached_property
    def Processors(self):  # pragma: no cover
        return ProcessorOutput.make_many(self.boto3_raw_data["Processors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProcessingConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProcessingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDescription:
    boto3_raw_data: "type_defs.SourceDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def DirectPutSourceDescription(self):  # pragma: no cover
        return DirectPutSourceDescription.make_one(
            self.boto3_raw_data["DirectPutSourceDescription"]
        )

    @cached_property
    def KinesisStreamSourceDescription(self):  # pragma: no cover
        return KinesisStreamSourceDescription.make_one(
            self.boto3_raw_data["KinesisStreamSourceDescription"]
        )

    @cached_property
    def MSKSourceDescription(self):  # pragma: no cover
        return MSKSourceDescription.make_one(
            self.boto3_raw_data["MSKSourceDescription"]
        )

    @cached_property
    def DatabaseSourceDescription(self):  # pragma: no cover
        return DatabaseSourceDescription.make_one(
            self.boto3_raw_data["DatabaseSourceDescription"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataFormatConversionConfigurationOutput:
    boto3_raw_data: "type_defs.DataFormatConversionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SchemaConfiguration(self):  # pragma: no cover
        return SchemaConfiguration.make_one(self.boto3_raw_data["SchemaConfiguration"])

    @cached_property
    def InputFormatConfiguration(self):  # pragma: no cover
        return InputFormatConfigurationOutput.make_one(
            self.boto3_raw_data["InputFormatConfiguration"]
        )

    @cached_property
    def OutputFormatConfiguration(self):  # pragma: no cover
        return OutputFormatConfigurationOutput.make_one(
            self.boto3_raw_data["OutputFormatConfiguration"]
        )

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataFormatConversionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataFormatConversionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationTableConfiguration:
    boto3_raw_data: "type_defs.DestinationTableConfigurationTypeDef" = (
        dataclasses.field()
    )

    DestinationTableName = field("DestinationTableName")
    DestinationDatabaseName = field("DestinationDatabaseName")
    UniqueKeys = field("UniqueKeys")
    PartitionSpec = field("PartitionSpec")
    S3ErrorOutputPrefix = field("S3ErrorOutputPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DestinationTableConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationTableConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonOpenSearchServerlessDestinationDescription:
    boto3_raw_data: (
        "type_defs.AmazonOpenSearchServerlessDestinationDescriptionTypeDef"
    ) = dataclasses.field()

    RoleARN = field("RoleARN")
    CollectionEndpoint = field("CollectionEndpoint")
    IndexName = field("IndexName")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return AmazonOpenSearchServerlessBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return AmazonOpenSearchServerlessRetryOptions.make_one(
            self.boto3_raw_data["RetryOptions"]
        )

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def VpcConfigurationDescription(self):  # pragma: no cover
        return VpcConfigurationDescription.make_one(
            self.boto3_raw_data["VpcConfigurationDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonOpenSearchServerlessDestinationDescriptionTypeDef"
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
                "type_defs.AmazonOpenSearchServerlessDestinationDescriptionTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonopensearchserviceDestinationDescription:
    boto3_raw_data: "type_defs.AmazonopensearchserviceDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    DomainARN = field("DomainARN")
    ClusterEndpoint = field("ClusterEndpoint")
    IndexName = field("IndexName")
    TypeName = field("TypeName")
    IndexRotationPeriod = field("IndexRotationPeriod")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return AmazonopensearchserviceBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return AmazonopensearchserviceRetryOptions.make_one(
            self.boto3_raw_data["RetryOptions"]
        )

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def VpcConfigurationDescription(self):  # pragma: no cover
        return VpcConfigurationDescription.make_one(
            self.boto3_raw_data["VpcConfigurationDescription"]
        )

    @cached_property
    def DocumentIdOptions(self):  # pragma: no cover
        return DocumentIdOptions.make_one(self.boto3_raw_data["DocumentIdOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonopensearchserviceDestinationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonopensearchserviceDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchDestinationDescription:
    boto3_raw_data: "type_defs.ElasticsearchDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    DomainARN = field("DomainARN")
    ClusterEndpoint = field("ClusterEndpoint")
    IndexName = field("IndexName")
    TypeName = field("TypeName")
    IndexRotationPeriod = field("IndexRotationPeriod")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return ElasticsearchBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return ElasticsearchRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def VpcConfigurationDescription(self):  # pragma: no cover
        return VpcConfigurationDescription.make_one(
            self.boto3_raw_data["VpcConfigurationDescription"]
        )

    @cached_property
    def DocumentIdOptions(self):  # pragma: no cover
        return DocumentIdOptions.make_one(self.boto3_raw_data["DocumentIdOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ElasticsearchDestinationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointDestinationDescription:
    boto3_raw_data: "type_defs.HttpEndpointDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointConfiguration(self):  # pragma: no cover
        return HttpEndpointDescription.make_one(
            self.boto3_raw_data["EndpointConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return HttpEndpointBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def RequestConfiguration(self):  # pragma: no cover
        return HttpEndpointRequestConfigurationOutput.make_one(
            self.boto3_raw_data["RequestConfiguration"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    RoleARN = field("RoleARN")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return HttpEndpointRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HttpEndpointDestinationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergDestinationDescription:
    boto3_raw_data: "type_defs.IcebergDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DestinationTableConfigurationList(self):  # pragma: no cover
        return DestinationTableConfigurationOutput.make_many(
            self.boto3_raw_data["DestinationTableConfigurationList"]
        )

    @cached_property
    def SchemaEvolutionConfiguration(self):  # pragma: no cover
        return SchemaEvolutionConfiguration.make_one(
            self.boto3_raw_data["SchemaEvolutionConfiguration"]
        )

    @cached_property
    def TableCreationConfiguration(self):  # pragma: no cover
        return TableCreationConfiguration.make_one(
            self.boto3_raw_data["TableCreationConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    RoleARN = field("RoleARN")
    AppendOnly = field("AppendOnly")

    @cached_property
    def CatalogConfiguration(self):  # pragma: no cover
        return CatalogConfiguration.make_one(
            self.boto3_raw_data["CatalogConfiguration"]
        )

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IcebergDestinationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IcebergDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDestinationDescription:
    boto3_raw_data: "type_defs.RedshiftDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    ClusterJDBCURL = field("ClusterJDBCURL")

    @cached_property
    def CopyCommand(self):  # pragma: no cover
        return CopyCommand.make_one(self.boto3_raw_data["CopyCommand"])

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    Username = field("Username")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RedshiftRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3BackupDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3BackupDescription"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftDestinationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeDestinationDescription:
    boto3_raw_data: "type_defs.SnowflakeDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    AccountUrl = field("AccountUrl")
    User = field("User")
    Database = field("Database")
    Schema = field("Schema")
    Table = field("Table")

    @cached_property
    def SnowflakeRoleConfiguration(self):  # pragma: no cover
        return SnowflakeRoleConfiguration.make_one(
            self.boto3_raw_data["SnowflakeRoleConfiguration"]
        )

    DataLoadingOption = field("DataLoadingOption")
    MetaDataColumnName = field("MetaDataColumnName")
    ContentColumnName = field("ContentColumnName")

    @cached_property
    def SnowflakeVpcConfiguration(self):  # pragma: no cover
        return SnowflakeVpcConfiguration.make_one(
            self.boto3_raw_data["SnowflakeVpcConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    RoleARN = field("RoleARN")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return SnowflakeRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return SnowflakeBufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SnowflakeDestinationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplunkDestinationDescription:
    boto3_raw_data: "type_defs.SplunkDestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    HECEndpoint = field("HECEndpoint")
    HECEndpointType = field("HECEndpointType")
    HECToken = field("HECToken")
    HECAcknowledgmentTimeoutInSeconds = field("HECAcknowledgmentTimeoutInSeconds")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return SplunkRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return SplunkBufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SplunkDestinationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplunkDestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessingConfiguration:
    boto3_raw_data: "type_defs.ProcessingConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Processors = field("Processors")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProcessingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProcessingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFormatConfiguration:
    boto3_raw_data: "type_defs.InputFormatConfigurationTypeDef" = dataclasses.field()

    Deserializer = field("Deserializer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputFormatConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputFormatConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputFormatConfiguration:
    boto3_raw_data: "type_defs.OutputFormatConfigurationTypeDef" = dataclasses.field()

    Serializer = field("Serializer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputFormatConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputFormatConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedS3DestinationDescription:
    boto3_raw_data: "type_defs.ExtendedS3DestinationDescriptionTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    CompressionFormat = field("CompressionFormat")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    Prefix = field("Prefix")
    ErrorOutputPrefix = field("ErrorOutputPrefix")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def ProcessingConfiguration(self):  # pragma: no cover
        return ProcessingConfigurationOutput.make_one(
            self.boto3_raw_data["ProcessingConfiguration"]
        )

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3BackupDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3BackupDescription"]
        )

    @cached_property
    def DataFormatConversionConfiguration(self):  # pragma: no cover
        return DataFormatConversionConfigurationOutput.make_one(
            self.boto3_raw_data["DataFormatConversionConfiguration"]
        )

    @cached_property
    def DynamicPartitioningConfiguration(self):  # pragma: no cover
        return DynamicPartitioningConfiguration.make_one(
            self.boto3_raw_data["DynamicPartitioningConfiguration"]
        )

    FileExtension = field("FileExtension")
    CustomTimeZone = field("CustomTimeZone")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExtendedS3DestinationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendedS3DestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationDescription:
    boto3_raw_data: "type_defs.DestinationDescriptionTypeDef" = dataclasses.field()

    DestinationId = field("DestinationId")

    @cached_property
    def S3DestinationDescription(self):  # pragma: no cover
        return S3DestinationDescription.make_one(
            self.boto3_raw_data["S3DestinationDescription"]
        )

    @cached_property
    def ExtendedS3DestinationDescription(self):  # pragma: no cover
        return ExtendedS3DestinationDescription.make_one(
            self.boto3_raw_data["ExtendedS3DestinationDescription"]
        )

    @cached_property
    def RedshiftDestinationDescription(self):  # pragma: no cover
        return RedshiftDestinationDescription.make_one(
            self.boto3_raw_data["RedshiftDestinationDescription"]
        )

    @cached_property
    def ElasticsearchDestinationDescription(self):  # pragma: no cover
        return ElasticsearchDestinationDescription.make_one(
            self.boto3_raw_data["ElasticsearchDestinationDescription"]
        )

    @cached_property
    def AmazonopensearchserviceDestinationDescription(self):  # pragma: no cover
        return AmazonopensearchserviceDestinationDescription.make_one(
            self.boto3_raw_data["AmazonopensearchserviceDestinationDescription"]
        )

    @cached_property
    def SplunkDestinationDescription(self):  # pragma: no cover
        return SplunkDestinationDescription.make_one(
            self.boto3_raw_data["SplunkDestinationDescription"]
        )

    @cached_property
    def HttpEndpointDestinationDescription(self):  # pragma: no cover
        return HttpEndpointDestinationDescription.make_one(
            self.boto3_raw_data["HttpEndpointDestinationDescription"]
        )

    @cached_property
    def SnowflakeDestinationDescription(self):  # pragma: no cover
        return SnowflakeDestinationDescription.make_one(
            self.boto3_raw_data["SnowflakeDestinationDescription"]
        )

    @cached_property
    def AmazonOpenSearchServerlessDestinationDescription(self):  # pragma: no cover
        return AmazonOpenSearchServerlessDestinationDescription.make_one(
            self.boto3_raw_data["AmazonOpenSearchServerlessDestinationDescription"]
        )

    @cached_property
    def IcebergDestinationDescription(self):  # pragma: no cover
        return IcebergDestinationDescription.make_one(
            self.boto3_raw_data["IcebergDestinationDescription"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonOpenSearchServerlessDestinationConfiguration:
    boto3_raw_data: (
        "type_defs.AmazonOpenSearchServerlessDestinationConfigurationTypeDef"
    ) = dataclasses.field()

    RoleARN = field("RoleARN")
    IndexName = field("IndexName")

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    CollectionEndpoint = field("CollectionEndpoint")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return AmazonOpenSearchServerlessBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return AmazonOpenSearchServerlessRetryOptions.make_one(
            self.boto3_raw_data["RetryOptions"]
        )

    S3BackupMode = field("S3BackupMode")
    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonOpenSearchServerlessDestinationConfigurationTypeDef"
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
                "type_defs.AmazonOpenSearchServerlessDestinationConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonOpenSearchServerlessDestinationUpdate:
    boto3_raw_data: "type_defs.AmazonOpenSearchServerlessDestinationUpdateTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    CollectionEndpoint = field("CollectionEndpoint")
    IndexName = field("IndexName")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return AmazonOpenSearchServerlessBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return AmazonOpenSearchServerlessRetryOptions.make_one(
            self.boto3_raw_data["RetryOptions"]
        )

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonOpenSearchServerlessDestinationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonOpenSearchServerlessDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonopensearchserviceDestinationConfiguration:
    boto3_raw_data: (
        "type_defs.AmazonopensearchserviceDestinationConfigurationTypeDef"
    ) = dataclasses.field()

    RoleARN = field("RoleARN")
    IndexName = field("IndexName")

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    DomainARN = field("DomainARN")
    ClusterEndpoint = field("ClusterEndpoint")
    TypeName = field("TypeName")
    IndexRotationPeriod = field("IndexRotationPeriod")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return AmazonopensearchserviceBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return AmazonopensearchserviceRetryOptions.make_one(
            self.boto3_raw_data["RetryOptions"]
        )

    S3BackupMode = field("S3BackupMode")
    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @cached_property
    def DocumentIdOptions(self):  # pragma: no cover
        return DocumentIdOptions.make_one(self.boto3_raw_data["DocumentIdOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonopensearchserviceDestinationConfigurationTypeDef"
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
                "type_defs.AmazonopensearchserviceDestinationConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonopensearchserviceDestinationUpdate:
    boto3_raw_data: "type_defs.AmazonopensearchserviceDestinationUpdateTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    DomainARN = field("DomainARN")
    ClusterEndpoint = field("ClusterEndpoint")
    IndexName = field("IndexName")
    TypeName = field("TypeName")
    IndexRotationPeriod = field("IndexRotationPeriod")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return AmazonopensearchserviceBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return AmazonopensearchserviceRetryOptions.make_one(
            self.boto3_raw_data["RetryOptions"]
        )

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def DocumentIdOptions(self):  # pragma: no cover
        return DocumentIdOptions.make_one(self.boto3_raw_data["DocumentIdOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonopensearchserviceDestinationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonopensearchserviceDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchDestinationConfiguration:
    boto3_raw_data: "type_defs.ElasticsearchDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    IndexName = field("IndexName")

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    DomainARN = field("DomainARN")
    ClusterEndpoint = field("ClusterEndpoint")
    TypeName = field("TypeName")
    IndexRotationPeriod = field("IndexRotationPeriod")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return ElasticsearchBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return ElasticsearchRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")
    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @cached_property
    def DocumentIdOptions(self):  # pragma: no cover
        return DocumentIdOptions.make_one(self.boto3_raw_data["DocumentIdOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ElasticsearchDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchDestinationUpdate:
    boto3_raw_data: "type_defs.ElasticsearchDestinationUpdateTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    DomainARN = field("DomainARN")
    ClusterEndpoint = field("ClusterEndpoint")
    IndexName = field("IndexName")
    TypeName = field("TypeName")
    IndexRotationPeriod = field("IndexRotationPeriod")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return ElasticsearchBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return ElasticsearchRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def DocumentIdOptions(self):  # pragma: no cover
        return DocumentIdOptions.make_one(self.boto3_raw_data["DocumentIdOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ElasticsearchDestinationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointDestinationConfiguration:
    boto3_raw_data: "type_defs.HttpEndpointDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointConfiguration(self):  # pragma: no cover
        return HttpEndpointConfiguration.make_one(
            self.boto3_raw_data["EndpointConfiguration"]
        )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return HttpEndpointBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    RequestConfiguration = field("RequestConfiguration")
    ProcessingConfiguration = field("ProcessingConfiguration")
    RoleARN = field("RoleARN")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return HttpEndpointRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HttpEndpointDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpEndpointDestinationUpdate:
    boto3_raw_data: "type_defs.HttpEndpointDestinationUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EndpointConfiguration(self):  # pragma: no cover
        return HttpEndpointConfiguration.make_one(
            self.boto3_raw_data["EndpointConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return HttpEndpointBufferingHints.make_one(
            self.boto3_raw_data["BufferingHints"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    RequestConfiguration = field("RequestConfiguration")
    ProcessingConfiguration = field("ProcessingConfiguration")
    RoleARN = field("RoleARN")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return HttpEndpointRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpEndpointDestinationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpEndpointDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergDestinationConfiguration:
    boto3_raw_data: "type_defs.IcebergDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")

    @cached_property
    def CatalogConfiguration(self):  # pragma: no cover
        return CatalogConfiguration.make_one(
            self.boto3_raw_data["CatalogConfiguration"]
        )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    DestinationTableConfigurationList = field("DestinationTableConfigurationList")

    @cached_property
    def SchemaEvolutionConfiguration(self):  # pragma: no cover
        return SchemaEvolutionConfiguration.make_one(
            self.boto3_raw_data["SchemaEvolutionConfiguration"]
        )

    @cached_property
    def TableCreationConfiguration(self):  # pragma: no cover
        return TableCreationConfiguration.make_one(
            self.boto3_raw_data["TableCreationConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ProcessingConfiguration = field("ProcessingConfiguration")
    S3BackupMode = field("S3BackupMode")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    AppendOnly = field("AppendOnly")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IcebergDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IcebergDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcebergDestinationUpdate:
    boto3_raw_data: "type_defs.IcebergDestinationUpdateTypeDef" = dataclasses.field()

    DestinationTableConfigurationList = field("DestinationTableConfigurationList")

    @cached_property
    def SchemaEvolutionConfiguration(self):  # pragma: no cover
        return SchemaEvolutionConfiguration.make_one(
            self.boto3_raw_data["SchemaEvolutionConfiguration"]
        )

    @cached_property
    def TableCreationConfiguration(self):  # pragma: no cover
        return TableCreationConfiguration.make_one(
            self.boto3_raw_data["TableCreationConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ProcessingConfiguration = field("ProcessingConfiguration")
    S3BackupMode = field("S3BackupMode")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    RoleARN = field("RoleARN")
    AppendOnly = field("AppendOnly")

    @cached_property
    def CatalogConfiguration(self):  # pragma: no cover
        return CatalogConfiguration.make_one(
            self.boto3_raw_data["CatalogConfiguration"]
        )

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IcebergDestinationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IcebergDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDestinationConfiguration:
    boto3_raw_data: "type_defs.RedshiftDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    ClusterJDBCURL = field("ClusterJDBCURL")

    @cached_property
    def CopyCommand(self):  # pragma: no cover
        return CopyCommand.make_one(self.boto3_raw_data["CopyCommand"])

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    Username = field("Username")
    Password = field("Password")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RedshiftRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    ProcessingConfiguration = field("ProcessingConfiguration")
    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3BackupConfiguration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3BackupConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDestinationUpdate:
    boto3_raw_data: "type_defs.RedshiftDestinationUpdateTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    ClusterJDBCURL = field("ClusterJDBCURL")

    @cached_property
    def CopyCommand(self):  # pragma: no cover
        return CopyCommand.make_one(self.boto3_raw_data["CopyCommand"])

    Username = field("Username")
    Password = field("Password")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return RedshiftRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    ProcessingConfiguration = field("ProcessingConfiguration")
    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3BackupUpdate(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3BackupUpdate"])

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDestinationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeDestinationConfiguration:
    boto3_raw_data: "type_defs.SnowflakeDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    AccountUrl = field("AccountUrl")
    Database = field("Database")
    Schema = field("Schema")
    Table = field("Table")
    RoleARN = field("RoleARN")

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    PrivateKey = field("PrivateKey")
    KeyPassphrase = field("KeyPassphrase")
    User = field("User")

    @cached_property
    def SnowflakeRoleConfiguration(self):  # pragma: no cover
        return SnowflakeRoleConfiguration.make_one(
            self.boto3_raw_data["SnowflakeRoleConfiguration"]
        )

    DataLoadingOption = field("DataLoadingOption")
    MetaDataColumnName = field("MetaDataColumnName")
    ContentColumnName = field("ContentColumnName")

    @cached_property
    def SnowflakeVpcConfiguration(self):  # pragma: no cover
        return SnowflakeVpcConfiguration.make_one(
            self.boto3_raw_data["SnowflakeVpcConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return SnowflakeRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return SnowflakeBufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SnowflakeDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeDestinationUpdate:
    boto3_raw_data: "type_defs.SnowflakeDestinationUpdateTypeDef" = dataclasses.field()

    AccountUrl = field("AccountUrl")
    PrivateKey = field("PrivateKey")
    KeyPassphrase = field("KeyPassphrase")
    User = field("User")
    Database = field("Database")
    Schema = field("Schema")
    Table = field("Table")

    @cached_property
    def SnowflakeRoleConfiguration(self):  # pragma: no cover
        return SnowflakeRoleConfiguration.make_one(
            self.boto3_raw_data["SnowflakeRoleConfiguration"]
        )

    DataLoadingOption = field("DataLoadingOption")
    MetaDataColumnName = field("MetaDataColumnName")
    ContentColumnName = field("ContentColumnName")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ProcessingConfiguration = field("ProcessingConfiguration")
    RoleARN = field("RoleARN")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return SnowflakeRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return SnowflakeBufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeDestinationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplunkDestinationConfiguration:
    boto3_raw_data: "type_defs.SplunkDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    HECEndpoint = field("HECEndpoint")
    HECEndpointType = field("HECEndpointType")

    @cached_property
    def S3Configuration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3Configuration"]
        )

    HECToken = field("HECToken")
    HECAcknowledgmentTimeoutInSeconds = field("HECAcknowledgmentTimeoutInSeconds")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return SplunkRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")
    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return SplunkBufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SplunkDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplunkDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplunkDestinationUpdate:
    boto3_raw_data: "type_defs.SplunkDestinationUpdateTypeDef" = dataclasses.field()

    HECEndpoint = field("HECEndpoint")
    HECEndpointType = field("HECEndpointType")
    HECToken = field("HECToken")
    HECAcknowledgmentTimeoutInSeconds = field("HECAcknowledgmentTimeoutInSeconds")

    @cached_property
    def RetryOptions(self):  # pragma: no cover
        return SplunkRetryOptions.make_one(self.boto3_raw_data["RetryOptions"])

    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3Update(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3Update"])

    ProcessingConfiguration = field("ProcessingConfiguration")

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return SplunkBufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    @cached_property
    def SecretsManagerConfiguration(self):  # pragma: no cover
        return SecretsManagerConfiguration.make_one(
            self.boto3_raw_data["SecretsManagerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SplunkDestinationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplunkDestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataFormatConversionConfiguration:
    boto3_raw_data: "type_defs.DataFormatConversionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SchemaConfiguration(self):  # pragma: no cover
        return SchemaConfiguration.make_one(self.boto3_raw_data["SchemaConfiguration"])

    InputFormatConfiguration = field("InputFormatConfiguration")
    OutputFormatConfiguration = field("OutputFormatConfiguration")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataFormatConversionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataFormatConversionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryStreamDescription:
    boto3_raw_data: "type_defs.DeliveryStreamDescriptionTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")
    DeliveryStreamARN = field("DeliveryStreamARN")
    DeliveryStreamStatus = field("DeliveryStreamStatus")
    DeliveryStreamType = field("DeliveryStreamType")
    VersionId = field("VersionId")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return DestinationDescription.make_many(self.boto3_raw_data["Destinations"])

    HasMoreDestinations = field("HasMoreDestinations")

    @cached_property
    def FailureDescription(self):  # pragma: no cover
        return FailureDescription.make_one(self.boto3_raw_data["FailureDescription"])

    @cached_property
    def DeliveryStreamEncryptionConfiguration(self):  # pragma: no cover
        return DeliveryStreamEncryptionConfiguration.make_one(
            self.boto3_raw_data["DeliveryStreamEncryptionConfiguration"]
        )

    CreateTimestamp = field("CreateTimestamp")
    LastUpdateTimestamp = field("LastUpdateTimestamp")

    @cached_property
    def Source(self):  # pragma: no cover
        return SourceDescription.make_one(self.boto3_raw_data["Source"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliveryStreamDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliveryStreamDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryStreamOutput:
    boto3_raw_data: "type_defs.DescribeDeliveryStreamOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeliveryStreamDescription(self):  # pragma: no cover
        return DeliveryStreamDescription.make_one(
            self.boto3_raw_data["DeliveryStreamDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeliveryStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedS3DestinationConfiguration:
    boto3_raw_data: "type_defs.ExtendedS3DestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")
    Prefix = field("Prefix")
    ErrorOutputPrefix = field("ErrorOutputPrefix")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    CompressionFormat = field("CompressionFormat")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ProcessingConfiguration = field("ProcessingConfiguration")
    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3BackupConfiguration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3BackupConfiguration"]
        )

    DataFormatConversionConfiguration = field("DataFormatConversionConfiguration")

    @cached_property
    def DynamicPartitioningConfiguration(self):  # pragma: no cover
        return DynamicPartitioningConfiguration.make_one(
            self.boto3_raw_data["DynamicPartitioningConfiguration"]
        )

    FileExtension = field("FileExtension")
    CustomTimeZone = field("CustomTimeZone")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExtendedS3DestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendedS3DestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtendedS3DestinationUpdate:
    boto3_raw_data: "type_defs.ExtendedS3DestinationUpdateTypeDef" = dataclasses.field()

    RoleARN = field("RoleARN")
    BucketARN = field("BucketARN")
    Prefix = field("Prefix")
    ErrorOutputPrefix = field("ErrorOutputPrefix")

    @cached_property
    def BufferingHints(self):  # pragma: no cover
        return BufferingHints.make_one(self.boto3_raw_data["BufferingHints"])

    CompressionFormat = field("CompressionFormat")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def CloudWatchLoggingOptions(self):  # pragma: no cover
        return CloudWatchLoggingOptions.make_one(
            self.boto3_raw_data["CloudWatchLoggingOptions"]
        )

    ProcessingConfiguration = field("ProcessingConfiguration")
    S3BackupMode = field("S3BackupMode")

    @cached_property
    def S3BackupUpdate(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3BackupUpdate"])

    DataFormatConversionConfiguration = field("DataFormatConversionConfiguration")

    @cached_property
    def DynamicPartitioningConfiguration(self):  # pragma: no cover
        return DynamicPartitioningConfiguration.make_one(
            self.boto3_raw_data["DynamicPartitioningConfiguration"]
        )

    FileExtension = field("FileExtension")
    CustomTimeZone = field("CustomTimeZone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtendedS3DestinationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtendedS3DestinationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeliveryStreamInput:
    boto3_raw_data: "type_defs.CreateDeliveryStreamInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")
    DeliveryStreamType = field("DeliveryStreamType")

    @cached_property
    def DirectPutSourceConfiguration(self):  # pragma: no cover
        return DirectPutSourceConfiguration.make_one(
            self.boto3_raw_data["DirectPutSourceConfiguration"]
        )

    @cached_property
    def KinesisStreamSourceConfiguration(self):  # pragma: no cover
        return KinesisStreamSourceConfiguration.make_one(
            self.boto3_raw_data["KinesisStreamSourceConfiguration"]
        )

    @cached_property
    def DeliveryStreamEncryptionConfigurationInput(self):  # pragma: no cover
        return DeliveryStreamEncryptionConfigurationInput.make_one(
            self.boto3_raw_data["DeliveryStreamEncryptionConfigurationInput"]
        )

    @cached_property
    def S3DestinationConfiguration(self):  # pragma: no cover
        return S3DestinationConfiguration.make_one(
            self.boto3_raw_data["S3DestinationConfiguration"]
        )

    @cached_property
    def ExtendedS3DestinationConfiguration(self):  # pragma: no cover
        return ExtendedS3DestinationConfiguration.make_one(
            self.boto3_raw_data["ExtendedS3DestinationConfiguration"]
        )

    @cached_property
    def RedshiftDestinationConfiguration(self):  # pragma: no cover
        return RedshiftDestinationConfiguration.make_one(
            self.boto3_raw_data["RedshiftDestinationConfiguration"]
        )

    @cached_property
    def ElasticsearchDestinationConfiguration(self):  # pragma: no cover
        return ElasticsearchDestinationConfiguration.make_one(
            self.boto3_raw_data["ElasticsearchDestinationConfiguration"]
        )

    @cached_property
    def AmazonopensearchserviceDestinationConfiguration(self):  # pragma: no cover
        return AmazonopensearchserviceDestinationConfiguration.make_one(
            self.boto3_raw_data["AmazonopensearchserviceDestinationConfiguration"]
        )

    @cached_property
    def SplunkDestinationConfiguration(self):  # pragma: no cover
        return SplunkDestinationConfiguration.make_one(
            self.boto3_raw_data["SplunkDestinationConfiguration"]
        )

    @cached_property
    def HttpEndpointDestinationConfiguration(self):  # pragma: no cover
        return HttpEndpointDestinationConfiguration.make_one(
            self.boto3_raw_data["HttpEndpointDestinationConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def AmazonOpenSearchServerlessDestinationConfiguration(self):  # pragma: no cover
        return AmazonOpenSearchServerlessDestinationConfiguration.make_one(
            self.boto3_raw_data["AmazonOpenSearchServerlessDestinationConfiguration"]
        )

    @cached_property
    def MSKSourceConfiguration(self):  # pragma: no cover
        return MSKSourceConfiguration.make_one(
            self.boto3_raw_data["MSKSourceConfiguration"]
        )

    @cached_property
    def SnowflakeDestinationConfiguration(self):  # pragma: no cover
        return SnowflakeDestinationConfiguration.make_one(
            self.boto3_raw_data["SnowflakeDestinationConfiguration"]
        )

    @cached_property
    def IcebergDestinationConfiguration(self):  # pragma: no cover
        return IcebergDestinationConfiguration.make_one(
            self.boto3_raw_data["IcebergDestinationConfiguration"]
        )

    @cached_property
    def DatabaseSourceConfiguration(self):  # pragma: no cover
        return DatabaseSourceConfiguration.make_one(
            self.boto3_raw_data["DatabaseSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeliveryStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeliveryStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDestinationInput:
    boto3_raw_data: "type_defs.UpdateDestinationInputTypeDef" = dataclasses.field()

    DeliveryStreamName = field("DeliveryStreamName")
    CurrentDeliveryStreamVersionId = field("CurrentDeliveryStreamVersionId")
    DestinationId = field("DestinationId")

    @cached_property
    def S3DestinationUpdate(self):  # pragma: no cover
        return S3DestinationUpdate.make_one(self.boto3_raw_data["S3DestinationUpdate"])

    @cached_property
    def ExtendedS3DestinationUpdate(self):  # pragma: no cover
        return ExtendedS3DestinationUpdate.make_one(
            self.boto3_raw_data["ExtendedS3DestinationUpdate"]
        )

    @cached_property
    def RedshiftDestinationUpdate(self):  # pragma: no cover
        return RedshiftDestinationUpdate.make_one(
            self.boto3_raw_data["RedshiftDestinationUpdate"]
        )

    @cached_property
    def ElasticsearchDestinationUpdate(self):  # pragma: no cover
        return ElasticsearchDestinationUpdate.make_one(
            self.boto3_raw_data["ElasticsearchDestinationUpdate"]
        )

    @cached_property
    def AmazonopensearchserviceDestinationUpdate(self):  # pragma: no cover
        return AmazonopensearchserviceDestinationUpdate.make_one(
            self.boto3_raw_data["AmazonopensearchserviceDestinationUpdate"]
        )

    @cached_property
    def SplunkDestinationUpdate(self):  # pragma: no cover
        return SplunkDestinationUpdate.make_one(
            self.boto3_raw_data["SplunkDestinationUpdate"]
        )

    @cached_property
    def HttpEndpointDestinationUpdate(self):  # pragma: no cover
        return HttpEndpointDestinationUpdate.make_one(
            self.boto3_raw_data["HttpEndpointDestinationUpdate"]
        )

    @cached_property
    def AmazonOpenSearchServerlessDestinationUpdate(self):  # pragma: no cover
        return AmazonOpenSearchServerlessDestinationUpdate.make_one(
            self.boto3_raw_data["AmazonOpenSearchServerlessDestinationUpdate"]
        )

    @cached_property
    def SnowflakeDestinationUpdate(self):  # pragma: no cover
        return SnowflakeDestinationUpdate.make_one(
            self.boto3_raw_data["SnowflakeDestinationUpdate"]
        )

    @cached_property
    def IcebergDestinationUpdate(self):  # pragma: no cover
        return IcebergDestinationUpdate.make_one(
            self.boto3_raw_data["IcebergDestinationUpdate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDestinationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDestinationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
