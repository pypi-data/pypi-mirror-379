# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortIncompleteMultipartUpload:
    boto3_raw_data: "type_defs.AbortIncompleteMultipartUploadTypeDef" = (
        dataclasses.field()
    )

    DaysAfterInitiation = field("DaysAfterInitiation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AbortIncompleteMultipartUploadTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortIncompleteMultipartUploadTypeDef"]
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
class AccelerateConfiguration:
    boto3_raw_data: "type_defs.AccelerateConfigurationTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccelerateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccelerateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Owner:
    boto3_raw_data: "type_defs.OwnerTypeDef" = dataclasses.field()

    DisplayName = field("DisplayName")
    ID = field("ID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OwnerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OwnerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlTranslation:
    boto3_raw_data: "type_defs.AccessControlTranslationTypeDef" = dataclasses.field()

    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlTranslationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlTranslationTypeDef"]
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
class AnalyticsS3BucketDestination:
    boto3_raw_data: "type_defs.AnalyticsS3BucketDestinationTypeDef" = (
        dataclasses.field()
    )

    Format = field("Format")
    Bucket = field("Bucket")
    BucketAccountId = field("BucketAccountId")
    Prefix = field("Prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsS3BucketDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsS3BucketDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopySource:
    boto3_raw_data: "type_defs.CopySourceTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopySourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopySourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketDownloadFileRequest:
    boto3_raw_data: "type_defs.BucketDownloadFileRequestTypeDef" = dataclasses.field()

    Key = field("Key")
    Filename = field("Filename")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketDownloadFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketDownloadFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketInfo:
    boto3_raw_data: "type_defs.BucketInfoTypeDef" = dataclasses.field()

    DataRedundancy = field("DataRedundancy")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bucket:
    boto3_raw_data: "type_defs.BucketTypeDef" = dataclasses.field()

    Name = field("Name")
    CreationDate = field("CreationDate")
    BucketRegion = field("BucketRegion")
    BucketArn = field("BucketArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketUploadFileRequest:
    boto3_raw_data: "type_defs.BucketUploadFileRequestTypeDef" = dataclasses.field()

    Filename = field("Filename")
    Key = field("Key")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketUploadFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketUploadFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CORSRuleOutput:
    boto3_raw_data: "type_defs.CORSRuleOutputTypeDef" = dataclasses.field()

    AllowedMethods = field("AllowedMethods")
    AllowedOrigins = field("AllowedOrigins")
    ID = field("ID")
    AllowedHeaders = field("AllowedHeaders")
    ExposeHeaders = field("ExposeHeaders")
    MaxAgeSeconds = field("MaxAgeSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CORSRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CORSRuleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CORSRule:
    boto3_raw_data: "type_defs.CORSRuleTypeDef" = dataclasses.field()

    AllowedMethods = field("AllowedMethods")
    AllowedOrigins = field("AllowedOrigins")
    ID = field("ID")
    AllowedHeaders = field("AllowedHeaders")
    ExposeHeaders = field("ExposeHeaders")
    MaxAgeSeconds = field("MaxAgeSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CORSRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CORSRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSVInput:
    boto3_raw_data: "type_defs.CSVInputTypeDef" = dataclasses.field()

    FileHeaderInfo = field("FileHeaderInfo")
    Comments = field("Comments")
    QuoteEscapeCharacter = field("QuoteEscapeCharacter")
    RecordDelimiter = field("RecordDelimiter")
    FieldDelimiter = field("FieldDelimiter")
    QuoteCharacter = field("QuoteCharacter")
    AllowQuotedRecordDelimiter = field("AllowQuotedRecordDelimiter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CSVInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CSVInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSVOutput:
    boto3_raw_data: "type_defs.CSVOutputTypeDef" = dataclasses.field()

    QuoteFields = field("QuoteFields")
    QuoteEscapeCharacter = field("QuoteEscapeCharacter")
    RecordDelimiter = field("RecordDelimiter")
    FieldDelimiter = field("FieldDelimiter")
    QuoteCharacter = field("QuoteCharacter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CSVOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CSVOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Checksum:
    boto3_raw_data: "type_defs.ChecksumTypeDef" = dataclasses.field()

    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChecksumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChecksumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientDownloadFileRequest:
    boto3_raw_data: "type_defs.ClientDownloadFileRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    Filename = field("Filename")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientDownloadFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientDownloadFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientGeneratePresignedPostRequest:
    boto3_raw_data: "type_defs.ClientGeneratePresignedPostRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Key = field("Key")
    Fields = field("Fields")
    Conditions = field("Conditions")
    ExpiresIn = field("ExpiresIn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ClientGeneratePresignedPostRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientGeneratePresignedPostRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientUploadFileRequest:
    boto3_raw_data: "type_defs.ClientUploadFileRequestTypeDef" = dataclasses.field()

    Filename = field("Filename")
    Bucket = field("Bucket")
    Key = field("Key")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientUploadFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientUploadFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFunctionConfigurationOutput:
    boto3_raw_data: "type_defs.CloudFunctionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Event = field("Event")
    Events = field("Events")
    CloudFunction = field("CloudFunction")
    InvocationRole = field("InvocationRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudFunctionConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFunctionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFunctionConfiguration:
    boto3_raw_data: "type_defs.CloudFunctionConfigurationTypeDef" = dataclasses.field()

    Id = field("Id")
    Event = field("Event")
    Events = field("Events")
    CloudFunction = field("CloudFunction")
    InvocationRole = field("InvocationRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFunctionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFunctionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommonPrefix:
    boto3_raw_data: "type_defs.CommonPrefixTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommonPrefixTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommonPrefixTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompletedPart:
    boto3_raw_data: "type_defs.CompletedPartTypeDef" = dataclasses.field()

    ETag = field("ETag")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    PartNumber = field("PartNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompletedPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CompletedPartTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    HttpErrorCodeReturnedEquals = field("HttpErrorCodeReturnedEquals")
    KeyPrefixEquals = field("KeyPrefixEquals")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyObjectResult:
    boto3_raw_data: "type_defs.CopyObjectResultTypeDef" = dataclasses.field()

    ETag = field("ETag")
    LastModified = field("LastModified")
    ChecksumType = field("ChecksumType")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyObjectResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyObjectResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyPartResult:
    boto3_raw_data: "type_defs.CopyPartResultTypeDef" = dataclasses.field()

    ETag = field("ETag")
    LastModified = field("LastModified")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyPartResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyPartResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationInfo:
    boto3_raw_data: "type_defs.LocationInfoTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionCredentials:
    boto3_raw_data: "type_defs.SessionCredentialsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionRequest:
    boto3_raw_data: "type_defs.CreateSessionRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    SessionMode = field("SessionMode")
    ServerSideEncryption = field("ServerSideEncryption")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultRetention:
    boto3_raw_data: "type_defs.DefaultRetentionTypeDef" = dataclasses.field()

    Mode = field("Mode")
    Days = field("Days")
    Years = field("Years")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefaultRetentionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultRetentionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketAnalyticsConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteBucketAnalyticsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketAnalyticsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketAnalyticsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketCorsRequestBucketCorsDelete:
    boto3_raw_data: "type_defs.DeleteBucketCorsRequestBucketCorsDeleteTypeDef" = (
        dataclasses.field()
    )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketCorsRequestBucketCorsDeleteTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketCorsRequestBucketCorsDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketCorsRequest:
    boto3_raw_data: "type_defs.DeleteBucketCorsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketCorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketCorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketEncryptionRequest:
    boto3_raw_data: "type_defs.DeleteBucketEncryptionRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBucketEncryptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketIntelligentTieringConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteBucketIntelligentTieringConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketIntelligentTieringConfigurationRequestTypeDef"
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
                "type_defs.DeleteBucketIntelligentTieringConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketInventoryConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteBucketInventoryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketInventoryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketInventoryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketLifecycleRequestBucketLifecycleConfigurationDelete:
    boto3_raw_data: "type_defs.DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef" = (dataclasses.field())

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef"
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
                "type_defs.DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketLifecycleRequestBucketLifecycleDelete:
    boto3_raw_data: (
        "type_defs.DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef"
    ) = dataclasses.field()

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef"
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
                "type_defs.DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketLifecycleRequest:
    boto3_raw_data: "type_defs.DeleteBucketLifecycleRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketLifecycleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketLifecycleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketMetadataConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteBucketMetadataConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketMetadataConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketMetadataConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketMetadataTableConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteBucketMetadataTableConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketMetadataTableConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketMetadataTableConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketMetricsConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteBucketMetricsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketMetricsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketMetricsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketOwnershipControlsRequest:
    boto3_raw_data: "type_defs.DeleteBucketOwnershipControlsRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketOwnershipControlsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketOwnershipControlsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketPolicyRequestBucketPolicyDelete:
    boto3_raw_data: "type_defs.DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef" = (
        dataclasses.field()
    )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketPolicyRequest:
    boto3_raw_data: "type_defs.DeleteBucketPolicyRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketReplicationRequest:
    boto3_raw_data: "type_defs.DeleteBucketReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBucketReplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketRequestBucketDelete:
    boto3_raw_data: "type_defs.DeleteBucketRequestBucketDeleteTypeDef" = (
        dataclasses.field()
    )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBucketRequestBucketDeleteTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketRequestBucketDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketRequest:
    boto3_raw_data: "type_defs.DeleteBucketRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketTaggingRequestBucketTaggingDelete:
    boto3_raw_data: "type_defs.DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef" = (
        dataclasses.field()
    )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketTaggingRequest:
    boto3_raw_data: "type_defs.DeleteBucketTaggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketWebsiteRequestBucketWebsiteDelete:
    boto3_raw_data: "type_defs.DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef" = (
        dataclasses.field()
    )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketWebsiteRequest:
    boto3_raw_data: "type_defs.DeleteBucketWebsiteRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketWebsiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketWebsiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMarkerReplication:
    boto3_raw_data: "type_defs.DeleteMarkerReplicationTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMarkerReplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMarkerReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectTaggingRequest:
    boto3_raw_data: "type_defs.DeleteObjectTaggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletedObject:
    boto3_raw_data: "type_defs.DeletedObjectTypeDef" = dataclasses.field()

    Key = field("Key")
    VersionId = field("VersionId")
    DeleteMarker = field("DeleteMarker")
    DeleteMarkerVersionId = field("DeleteMarkerVersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletedObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeletedObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Error:
    boto3_raw_data: "type_defs.ErrorTypeDef" = dataclasses.field()

    Key = field("Key")
    VersionId = field("VersionId")
    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePublicAccessBlockRequest:
    boto3_raw_data: "type_defs.DeletePublicAccessBlockRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePublicAccessBlockRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePublicAccessBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationResult:
    boto3_raw_data: "type_defs.DestinationResultTypeDef" = dataclasses.field()

    TableBucketType = field("TableBucketType")
    TableBucketArn = field("TableBucketArn")
    TableNamespace = field("TableNamespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationResultTypeDef"]
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

    ReplicaKmsKeyID = field("ReplicaKmsKeyID")

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
class Encryption:
    boto3_raw_data: "type_defs.EncryptionTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KMSKeyId = field("KMSKeyId")
    KMSContext = field("KMSContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionTypeDef"]]
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
class ErrorDocument:
    boto3_raw_data: "type_defs.ErrorDocumentTypeDef" = dataclasses.field()

    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExistingObjectReplication:
    boto3_raw_data: "type_defs.ExistingObjectReplicationTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExistingObjectReplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExistingObjectReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterRule:
    boto3_raw_data: "type_defs.FilterRuleTypeDef" = dataclasses.field()

    Name = field("Name")
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
class GetBucketAccelerateConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketAccelerateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketAccelerateConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAccelerateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketAclRequest:
    boto3_raw_data: "type_defs.GetBucketAclRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketAclRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAclRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketAnalyticsConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketAnalyticsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketAnalyticsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAnalyticsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketCorsRequest:
    boto3_raw_data: "type_defs.GetBucketCorsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketCorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketCorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketEncryptionRequest:
    boto3_raw_data: "type_defs.GetBucketEncryptionRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketEncryptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketIntelligentTieringConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetBucketIntelligentTieringConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketIntelligentTieringConfigurationRequestTypeDef"
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
                "type_defs.GetBucketIntelligentTieringConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketInventoryConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketInventoryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketInventoryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketInventoryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketLifecycleConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLifecycleRequest:
    boto3_raw_data: "type_defs.GetBucketLifecycleRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketLifecycleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLifecycleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLocationRequest:
    boto3_raw_data: "type_defs.GetBucketLocationRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketLocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLoggingRequest:
    boto3_raw_data: "type_defs.GetBucketLoggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketLoggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLoggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetadataConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketMetadataConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetadataConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetadataConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetadataTableConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketMetadataTableConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetadataTableConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetadataTableConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetricsConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketMetricsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetricsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetricsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketNotificationConfigurationRequestRequest:
    boto3_raw_data: (
        "type_defs.GetBucketNotificationConfigurationRequestRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketNotificationConfigurationRequestRequestTypeDef"
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
                "type_defs.GetBucketNotificationConfigurationRequestRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketOwnershipControlsRequest:
    boto3_raw_data: "type_defs.GetBucketOwnershipControlsRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketOwnershipControlsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketOwnershipControlsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketPolicyRequest:
    boto3_raw_data: "type_defs.GetBucketPolicyRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyStatus:
    boto3_raw_data: "type_defs.PolicyStatusTypeDef" = dataclasses.field()

    IsPublic = field("IsPublic")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketPolicyStatusRequest:
    boto3_raw_data: "type_defs.GetBucketPolicyStatusRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketPolicyStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketPolicyStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketReplicationRequest:
    boto3_raw_data: "type_defs.GetBucketReplicationRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketRequestPaymentRequest:
    boto3_raw_data: "type_defs.GetBucketRequestPaymentRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBucketRequestPaymentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketRequestPaymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketTaggingRequest:
    boto3_raw_data: "type_defs.GetBucketTaggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketVersioningRequest:
    boto3_raw_data: "type_defs.GetBucketVersioningRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketVersioningRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketVersioningRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexDocument:
    boto3_raw_data: "type_defs.IndexDocumentTypeDef" = dataclasses.field()

    Suffix = field("Suffix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedirectAllRequestsTo:
    boto3_raw_data: "type_defs.RedirectAllRequestsToTypeDef" = dataclasses.field()

    HostName = field("HostName")
    Protocol = field("Protocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedirectAllRequestsToTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedirectAllRequestsToTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketWebsiteRequest:
    boto3_raw_data: "type_defs.GetBucketWebsiteRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketWebsiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketWebsiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAclRequest:
    boto3_raw_data: "type_defs.GetObjectAclRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAclRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAclRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectPart:
    boto3_raw_data: "type_defs.ObjectPartTypeDef" = dataclasses.field()

    PartNumber = field("PartNumber")
    Size = field("Size")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectPartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAttributesRequest:
    boto3_raw_data: "type_defs.GetObjectAttributesRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    ObjectAttributes = field("ObjectAttributes")
    VersionId = field("VersionId")
    MaxParts = field("MaxParts")
    PartNumberMarker = field("PartNumberMarker")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLockLegalHold:
    boto3_raw_data: "type_defs.ObjectLockLegalHoldTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLockLegalHoldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLockLegalHoldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectLegalHoldRequest:
    boto3_raw_data: "type_defs.GetObjectLegalHoldRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectLegalHoldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectLegalHoldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectLockConfigurationRequest:
    boto3_raw_data: "type_defs.GetObjectLockConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetObjectLockConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectLockConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLockRetentionOutput:
    boto3_raw_data: "type_defs.ObjectLockRetentionOutputTypeDef" = dataclasses.field()

    Mode = field("Mode")
    RetainUntilDate = field("RetainUntilDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLockRetentionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLockRetentionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectRetentionRequest:
    boto3_raw_data: "type_defs.GetObjectRetentionRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectRetentionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectRetentionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectTaggingRequest:
    boto3_raw_data: "type_defs.GetObjectTaggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectTorrentRequest:
    boto3_raw_data: "type_defs.GetObjectTorrentRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectTorrentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectTorrentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicAccessBlockConfiguration:
    boto3_raw_data: "type_defs.PublicAccessBlockConfigurationTypeDef" = (
        dataclasses.field()
    )

    BlockPublicAcls = field("BlockPublicAcls")
    IgnorePublicAcls = field("IgnorePublicAcls")
    BlockPublicPolicy = field("BlockPublicPolicy")
    RestrictPublicBuckets = field("RestrictPublicBuckets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PublicAccessBlockConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublicAccessBlockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicAccessBlockRequest:
    boto3_raw_data: "type_defs.GetPublicAccessBlockRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicAccessBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicAccessBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlacierJobParameters:
    boto3_raw_data: "type_defs.GlacierJobParametersTypeDef" = dataclasses.field()

    Tier = field("Tier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlacierJobParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlacierJobParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grantee:
    boto3_raw_data: "type_defs.GranteeTypeDef" = dataclasses.field()

    Type = field("Type")
    DisplayName = field("DisplayName")
    EmailAddress = field("EmailAddress")
    ID = field("ID")
    URI = field("URI")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GranteeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GranteeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadBucketRequest:
    boto3_raw_data: "type_defs.HeadBucketRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadBucketRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadBucketRequestTypeDef"]
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
class Initiator:
    boto3_raw_data: "type_defs.InitiatorTypeDef" = dataclasses.field()

    ID = field("ID")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InitiatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InitiatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JSONInput:
    boto3_raw_data: "type_defs.JSONInputTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JSONInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JSONInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tiering:
    boto3_raw_data: "type_defs.TieringTypeDef" = dataclasses.field()

    Days = field("Days")
    AccessTier = field("AccessTier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TieringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TieringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryFilter:
    boto3_raw_data: "type_defs.InventoryFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InventoryFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventorySchedule:
    boto3_raw_data: "type_defs.InventoryScheduleTypeDef" = dataclasses.field()

    Frequency = field("Frequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryScheduleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSEKMS:
    boto3_raw_data: "type_defs.SSEKMSTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSEKMSTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSEKMSTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataTableEncryptionConfiguration:
    boto3_raw_data: "type_defs.MetadataTableEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    SseAlgorithm = field("SseAlgorithm")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetadataTableEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataTableEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JSONOutput:
    boto3_raw_data: "type_defs.JSONOutputTypeDef" = dataclasses.field()

    RecordDelimiter = field("RecordDelimiter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JSONOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JSONOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordExpiration:
    boto3_raw_data: "type_defs.RecordExpirationTypeDef" = dataclasses.field()

    Expiration = field("Expiration")
    Days = field("Days")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordExpirationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordExpirationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExpirationOutput:
    boto3_raw_data: "type_defs.LifecycleExpirationOutputTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    ExpiredObjectDeleteMarker = field("ExpiredObjectDeleteMarker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExpirationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExpirationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoncurrentVersionExpiration:
    boto3_raw_data: "type_defs.NoncurrentVersionExpirationTypeDef" = dataclasses.field()

    NoncurrentDays = field("NoncurrentDays")
    NewerNoncurrentVersions = field("NewerNoncurrentVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoncurrentVersionExpirationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoncurrentVersionExpirationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoncurrentVersionTransition:
    boto3_raw_data: "type_defs.NoncurrentVersionTransitionTypeDef" = dataclasses.field()

    NoncurrentDays = field("NoncurrentDays")
    StorageClass = field("StorageClass")
    NewerNoncurrentVersions = field("NewerNoncurrentVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoncurrentVersionTransitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoncurrentVersionTransitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitionOutput:
    boto3_raw_data: "type_defs.TransitionOutputTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketAnalyticsConfigurationsRequest:
    boto3_raw_data: "type_defs.ListBucketAnalyticsConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ContinuationToken = field("ContinuationToken")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketAnalyticsConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketAnalyticsConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketIntelligentTieringConfigurationsRequest:
    boto3_raw_data: (
        "type_defs.ListBucketIntelligentTieringConfigurationsRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")
    ContinuationToken = field("ContinuationToken")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketIntelligentTieringConfigurationsRequestTypeDef"
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
                "type_defs.ListBucketIntelligentTieringConfigurationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketInventoryConfigurationsRequest:
    boto3_raw_data: "type_defs.ListBucketInventoryConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ContinuationToken = field("ContinuationToken")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketInventoryConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketInventoryConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketMetricsConfigurationsRequest:
    boto3_raw_data: "type_defs.ListBucketMetricsConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ContinuationToken = field("ContinuationToken")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketMetricsConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketMetricsConfigurationsRequestTypeDef"]
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
class ListBucketsRequest:
    boto3_raw_data: "type_defs.ListBucketsRequestTypeDef" = dataclasses.field()

    MaxBuckets = field("MaxBuckets")
    ContinuationToken = field("ContinuationToken")
    Prefix = field("Prefix")
    BucketRegion = field("BucketRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBucketsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoryBucketsRequest:
    boto3_raw_data: "type_defs.ListDirectoryBucketsRequestTypeDef" = dataclasses.field()

    ContinuationToken = field("ContinuationToken")
    MaxDirectoryBuckets = field("MaxDirectoryBuckets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDirectoryBucketsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoryBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartUploadsRequest:
    boto3_raw_data: "type_defs.ListMultipartUploadsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    KeyMarker = field("KeyMarker")
    MaxUploads = field("MaxUploads")
    Prefix = field("Prefix")
    UploadIdMarker = field("UploadIdMarker")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultipartUploadsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartUploadsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectVersionsRequest:
    boto3_raw_data: "type_defs.ListObjectVersionsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    KeyMarker = field("KeyMarker")
    MaxKeys = field("MaxKeys")
    Prefix = field("Prefix")
    VersionIdMarker = field("VersionIdMarker")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")
    OptionalObjectAttributes = field("OptionalObjectAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectsRequest:
    boto3_raw_data: "type_defs.ListObjectsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    Marker = field("Marker")
    MaxKeys = field("MaxKeys")
    Prefix = field("Prefix")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    OptionalObjectAttributes = field("OptionalObjectAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectsV2Request:
    boto3_raw_data: "type_defs.ListObjectsV2RequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    MaxKeys = field("MaxKeys")
    Prefix = field("Prefix")
    ContinuationToken = field("ContinuationToken")
    FetchOwner = field("FetchOwner")
    StartAfter = field("StartAfter")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    OptionalObjectAttributes = field("OptionalObjectAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectsV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectsV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Part:
    boto3_raw_data: "type_defs.PartTypeDef" = dataclasses.field()

    PartNumber = field("PartNumber")
    LastModified = field("LastModified")
    ETag = field("ETag")
    Size = field("Size")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsRequest:
    boto3_raw_data: "type_defs.ListPartsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    UploadId = field("UploadId")
    MaxParts = field("MaxParts")
    PartNumberMarker = field("PartNumberMarker")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPartsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataEntry:
    boto3_raw_data: "type_defs.MetadataEntryTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3TablesDestinationResult:
    boto3_raw_data: "type_defs.S3TablesDestinationResultTypeDef" = dataclasses.field()

    TableBucketArn = field("TableBucketArn")
    TableName = field("TableName")
    TableArn = field("TableArn")
    TableNamespace = field("TableNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3TablesDestinationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3TablesDestinationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3TablesDestination:
    boto3_raw_data: "type_defs.S3TablesDestinationTypeDef" = dataclasses.field()

    TableBucketArn = field("TableBucketArn")
    TableName = field("TableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3TablesDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3TablesDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTimeValue:
    boto3_raw_data: "type_defs.ReplicationTimeValueTypeDef" = dataclasses.field()

    Minutes = field("Minutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationTimeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTimeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueConfigurationDeprecatedOutput:
    boto3_raw_data: "type_defs.QueueConfigurationDeprecatedOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Event = field("Event")
    Events = field("Events")
    Queue = field("Queue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.QueueConfigurationDeprecatedOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueConfigurationDeprecatedOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicConfigurationDeprecatedOutput:
    boto3_raw_data: "type_defs.TopicConfigurationDeprecatedOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Events = field("Events")
    Event = field("Event")
    Topic = field("Topic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TopicConfigurationDeprecatedOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicConfigurationDeprecatedOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectDownloadFileRequest:
    boto3_raw_data: "type_defs.ObjectDownloadFileRequestTypeDef" = dataclasses.field()

    Filename = field("Filename")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectDownloadFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectDownloadFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreStatus:
    boto3_raw_data: "type_defs.RestoreStatusTypeDef" = dataclasses.field()

    IsRestoreInProgress = field("IsRestoreInProgress")
    RestoreExpiryDate = field("RestoreExpiryDate")

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
class ObjectUploadFileRequest:
    boto3_raw_data: "type_defs.ObjectUploadFileRequestTypeDef" = dataclasses.field()

    Filename = field("Filename")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectUploadFileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectUploadFileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnershipControlsRule:
    boto3_raw_data: "type_defs.OwnershipControlsRuleTypeDef" = dataclasses.field()

    ObjectOwnership = field("ObjectOwnership")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnershipControlsRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnershipControlsRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionedPrefix:
    boto3_raw_data: "type_defs.PartitionedPrefixTypeDef" = dataclasses.field()

    PartitionDateSource = field("PartitionDateSource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionedPrefixTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartitionedPrefixTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Progress:
    boto3_raw_data: "type_defs.ProgressTypeDef" = dataclasses.field()

    BytesScanned = field("BytesScanned")
    BytesProcessed = field("BytesProcessed")
    BytesReturned = field("BytesReturned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProgressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProgressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketPolicyRequestBucketPolicyPut:
    boto3_raw_data: "type_defs.PutBucketPolicyRequestBucketPolicyPutTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ConfirmRemoveSelfBucketAccess = field("ConfirmRemoveSelfBucketAccess")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketPolicyRequestBucketPolicyPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketPolicyRequestBucketPolicyPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketPolicyRequest:
    boto3_raw_data: "type_defs.PutBucketPolicyRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Policy = field("Policy")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ConfirmRemoveSelfBucketAccess = field("ConfirmRemoveSelfBucketAccess")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestPaymentConfiguration:
    boto3_raw_data: "type_defs.RequestPaymentConfigurationTypeDef" = dataclasses.field()

    Payer = field("Payer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestPaymentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestPaymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketVersioningRequestBucketVersioningEnable:
    boto3_raw_data: (
        "type_defs.PutBucketVersioningRequestBucketVersioningEnableTypeDef"
    ) = dataclasses.field()

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    MFA = field("MFA")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketVersioningRequestBucketVersioningEnableTypeDef"
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
                "type_defs.PutBucketVersioningRequestBucketVersioningEnableTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersioningConfiguration:
    boto3_raw_data: "type_defs.VersioningConfigurationTypeDef" = dataclasses.field()

    MFADelete = field("MFADelete")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersioningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersioningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketVersioningRequestBucketVersioningSuspend:
    boto3_raw_data: (
        "type_defs.PutBucketVersioningRequestBucketVersioningSuspendTypeDef"
    ) = dataclasses.field()

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    MFA = field("MFA")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketVersioningRequestBucketVersioningSuspendTypeDef"
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
                "type_defs.PutBucketVersioningRequestBucketVersioningSuspendTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueConfigurationDeprecated:
    boto3_raw_data: "type_defs.QueueConfigurationDeprecatedTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Event = field("Event")
    Events = field("Events")
    Queue = field("Queue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueConfigurationDeprecatedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueConfigurationDeprecatedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordsEvent:
    boto3_raw_data: "type_defs.RecordsEventTypeDef" = dataclasses.field()

    Payload = field("Payload")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordsEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordsEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Redirect:
    boto3_raw_data: "type_defs.RedirectTypeDef" = dataclasses.field()

    HostName = field("HostName")
    HttpRedirectCode = field("HttpRedirectCode")
    Protocol = field("Protocol")
    ReplaceKeyPrefixWith = field("ReplaceKeyPrefixWith")
    ReplaceKeyWith = field("ReplaceKeyWith")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedirectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RedirectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaModifications:
    boto3_raw_data: "type_defs.ReplicaModificationsTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaModificationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaModificationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestProgress:
    boto3_raw_data: "type_defs.RequestProgressTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestProgressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RequestProgressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanRange:
    boto3_raw_data: "type_defs.ScanRangeTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionByDefault:
    boto3_raw_data: "type_defs.ServerSideEncryptionByDefaultTypeDef" = (
        dataclasses.field()
    )

    SSEAlgorithm = field("SSEAlgorithm")
    KMSMasterKeyID = field("KMSMasterKeyID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerSideEncryptionByDefaultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionByDefaultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SseKmsEncryptedObjects:
    boto3_raw_data: "type_defs.SseKmsEncryptedObjectsTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SseKmsEncryptedObjectsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SseKmsEncryptedObjectsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stats:
    boto3_raw_data: "type_defs.StatsTypeDef" = dataclasses.field()

    BytesScanned = field("BytesScanned")
    BytesProcessed = field("BytesProcessed")
    BytesReturned = field("BytesReturned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicConfigurationDeprecated:
    boto3_raw_data: "type_defs.TopicConfigurationDeprecatedTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Events = field("Events")
    Event = field("Event")
    Topic = field("Topic")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicConfigurationDeprecatedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicConfigurationDeprecatedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortMultipartUploadOutput:
    boto3_raw_data: "type_defs.AbortMultipartUploadOutputTypeDef" = dataclasses.field()

    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AbortMultipartUploadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortMultipartUploadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartUploadOutput:
    boto3_raw_data: "type_defs.CompleteMultipartUploadOutputTypeDef" = (
        dataclasses.field()
    )

    Location = field("Location")
    Bucket = field("Bucket")
    Key = field("Key")
    Expiration = field("Expiration")
    ETag = field("ETag")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")
    ServerSideEncryption = field("ServerSideEncryption")
    VersionId = field("VersionId")
    SSEKMSKeyId = field("SSEKMSKeyId")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompleteMultipartUploadOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMultipartUploadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketOutput:
    boto3_raw_data: "type_defs.CreateBucketOutputTypeDef" = dataclasses.field()

    Location = field("Location")
    BucketArn = field("BucketArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultipartUploadOutput:
    boto3_raw_data: "type_defs.CreateMultipartUploadOutputTypeDef" = dataclasses.field()

    AbortDate = field("AbortDate")
    AbortRuleId = field("AbortRuleId")
    Bucket = field("Bucket")
    Key = field("Key")
    UploadId = field("UploadId")
    ServerSideEncryption = field("ServerSideEncryption")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestCharged = field("RequestCharged")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMultipartUploadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultipartUploadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectOutput:
    boto3_raw_data: "type_defs.DeleteObjectOutputTypeDef" = dataclasses.field()

    DeleteMarker = field("DeleteMarker")
    VersionId = field("VersionId")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectTaggingOutput:
    boto3_raw_data: "type_defs.DeleteObjectTaggingOutputTypeDef" = dataclasses.field()

    VersionId = field("VersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectTaggingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectTaggingOutputTypeDef"]
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
class GetBucketAccelerateConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketAccelerateConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketAccelerateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAccelerateConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLocationOutput:
    boto3_raw_data: "type_defs.GetBucketLocationOutputTypeDef" = dataclasses.field()

    LocationConstraint = field("LocationConstraint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketLocationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketPolicyOutput:
    boto3_raw_data: "type_defs.GetBucketPolicyOutputTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketRequestPaymentOutput:
    boto3_raw_data: "type_defs.GetBucketRequestPaymentOutputTypeDef" = (
        dataclasses.field()
    )

    Payer = field("Payer")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBucketRequestPaymentOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketRequestPaymentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketVersioningOutput:
    boto3_raw_data: "type_defs.GetBucketVersioningOutputTypeDef" = dataclasses.field()

    Status = field("Status")
    MFADelete = field("MFADelete")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketVersioningOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketVersioningOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectOutput:
    boto3_raw_data: "type_defs.GetObjectOutputTypeDef" = dataclasses.field()

    Body = field("Body")
    DeleteMarker = field("DeleteMarker")
    AcceptRanges = field("AcceptRanges")
    Expiration = field("Expiration")
    Restore = field("Restore")
    LastModified = field("LastModified")
    ContentLength = field("ContentLength")
    ETag = field("ETag")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")
    MissingMeta = field("MissingMeta")
    VersionId = field("VersionId")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentRange = field("ContentRange")
    ContentType = field("ContentType")
    Expires = field("Expires")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    ServerSideEncryption = field("ServerSideEncryption")
    Metadata = field("Metadata")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    BucketKeyEnabled = field("BucketKeyEnabled")
    StorageClass = field("StorageClass")
    RequestCharged = field("RequestCharged")
    ReplicationStatus = field("ReplicationStatus")
    PartsCount = field("PartsCount")
    TagCount = field("TagCount")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetObjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetObjectOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectTorrentOutput:
    boto3_raw_data: "type_defs.GetObjectTorrentOutputTypeDef" = dataclasses.field()

    Body = field("Body")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectTorrentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectTorrentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadBucketOutput:
    boto3_raw_data: "type_defs.HeadBucketOutputTypeDef" = dataclasses.field()

    BucketArn = field("BucketArn")
    BucketLocationType = field("BucketLocationType")
    BucketLocationName = field("BucketLocationName")
    BucketRegion = field("BucketRegion")
    AccessPointAlias = field("AccessPointAlias")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadBucketOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadBucketOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadObjectOutput:
    boto3_raw_data: "type_defs.HeadObjectOutputTypeDef" = dataclasses.field()

    DeleteMarker = field("DeleteMarker")
    AcceptRanges = field("AcceptRanges")
    Expiration = field("Expiration")
    Restore = field("Restore")
    ArchiveStatus = field("ArchiveStatus")
    LastModified = field("LastModified")
    ContentLength = field("ContentLength")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")
    ETag = field("ETag")
    MissingMeta = field("MissingMeta")
    VersionId = field("VersionId")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    ContentRange = field("ContentRange")
    Expires = field("Expires")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    ServerSideEncryption = field("ServerSideEncryption")
    Metadata = field("Metadata")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    BucketKeyEnabled = field("BucketKeyEnabled")
    StorageClass = field("StorageClass")
    RequestCharged = field("RequestCharged")
    ReplicationStatus = field("ReplicationStatus")
    PartsCount = field("PartsCount")
    TagCount = field("TagCount")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadObjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLifecycleConfigurationOutput:
    boto3_raw_data: "type_defs.PutBucketLifecycleConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    TransitionDefaultMinimumObjectSize = field("TransitionDefaultMinimumObjectSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketLifecycleConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLifecycleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectAclOutput:
    boto3_raw_data: "type_defs.PutObjectAclOutputTypeDef" = dataclasses.field()

    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectAclOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectAclOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectLegalHoldOutput:
    boto3_raw_data: "type_defs.PutObjectLegalHoldOutputTypeDef" = dataclasses.field()

    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectLegalHoldOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectLegalHoldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectLockConfigurationOutput:
    boto3_raw_data: "type_defs.PutObjectLockConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutObjectLockConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectLockConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectOutput:
    boto3_raw_data: "type_defs.PutObjectOutputTypeDef" = dataclasses.field()

    Expiration = field("Expiration")
    ETag = field("ETag")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")
    ServerSideEncryption = field("ServerSideEncryption")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    Size = field("Size")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutObjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutObjectOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectRetentionOutput:
    boto3_raw_data: "type_defs.PutObjectRetentionOutputTypeDef" = dataclasses.field()

    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectRetentionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectRetentionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectTaggingOutput:
    boto3_raw_data: "type_defs.PutObjectTaggingOutputTypeDef" = dataclasses.field()

    VersionId = field("VersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectTaggingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectTaggingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreObjectOutput:
    boto3_raw_data: "type_defs.RestoreObjectOutputTypeDef" = dataclasses.field()

    RequestCharged = field("RequestCharged")
    RestoreOutputPath = field("RestoreOutputPath")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreObjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadPartOutput:
    boto3_raw_data: "type_defs.UploadPartOutputTypeDef" = dataclasses.field()

    ServerSideEncryption = field("ServerSideEncryption")
    ETag = field("ETag")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadPartOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadPartOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortMultipartUploadRequestMultipartUploadAbort:
    boto3_raw_data: (
        "type_defs.AbortMultipartUploadRequestMultipartUploadAbortTypeDef"
    ) = dataclasses.field()

    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatchInitiatedTime = field("IfMatchInitiatedTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AbortMultipartUploadRequestMultipartUploadAbortTypeDef"
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
                "type_defs.AbortMultipartUploadRequestMultipartUploadAbortTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortMultipartUploadRequest:
    boto3_raw_data: "type_defs.AbortMultipartUploadRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    UploadId = field("UploadId")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatchInitiatedTime = field("IfMatchInitiatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AbortMultipartUploadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortMultipartUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultipartUploadRequestObjectInitiateMultipartUpload:
    boto3_raw_data: (
        "type_defs.CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef"
    ) = dataclasses.field()

    ACL = field("ACL")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    Expires = field("Expires")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef"
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
                "type_defs.CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultipartUploadRequestObjectSummaryInitiateMultipartUpload:
    boto3_raw_data: "type_defs.CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef" = (dataclasses.field())

    ACL = field("ACL")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    Expires = field("Expires")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef"
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
                "type_defs.CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultipartUploadRequest:
    boto3_raw_data: "type_defs.CreateMultipartUploadRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Key = field("Key")
    ACL = field("ACL")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    Expires = field("Expires")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMultipartUploadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultipartUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectRequestObjectDelete:
    boto3_raw_data: "type_defs.DeleteObjectRequestObjectDeleteTypeDef" = (
        dataclasses.field()
    )

    MFA = field("MFA")
    VersionId = field("VersionId")
    RequestPayer = field("RequestPayer")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatch = field("IfMatch")
    IfMatchLastModifiedTime = field("IfMatchLastModifiedTime")
    IfMatchSize = field("IfMatchSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteObjectRequestObjectDeleteTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectRequestObjectDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectRequestObjectSummaryDelete:
    boto3_raw_data: "type_defs.DeleteObjectRequestObjectSummaryDeleteTypeDef" = (
        dataclasses.field()
    )

    MFA = field("MFA")
    VersionId = field("VersionId")
    RequestPayer = field("RequestPayer")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatch = field("IfMatch")
    IfMatchLastModifiedTime = field("IfMatchLastModifiedTime")
    IfMatchSize = field("IfMatchSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteObjectRequestObjectSummaryDeleteTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectRequestObjectSummaryDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectRequestObjectVersionDelete:
    boto3_raw_data: "type_defs.DeleteObjectRequestObjectVersionDeleteTypeDef" = (
        dataclasses.field()
    )

    MFA = field("MFA")
    RequestPayer = field("RequestPayer")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatch = field("IfMatch")
    IfMatchLastModifiedTime = field("IfMatchLastModifiedTime")
    IfMatchSize = field("IfMatchSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteObjectRequestObjectVersionDeleteTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectRequestObjectVersionDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectRequest:
    boto3_raw_data: "type_defs.DeleteObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    MFA = field("MFA")
    VersionId = field("VersionId")
    RequestPayer = field("RequestPayer")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatch = field("IfMatch")
    IfMatchLastModifiedTime = field("IfMatchLastModifiedTime")
    IfMatchSize = field("IfMatchSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectRequestObjectGet:
    boto3_raw_data: "type_defs.GetObjectRequestObjectGetTypeDef" = dataclasses.field()

    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectRequestObjectGetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectRequestObjectGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectRequestObjectSummaryGet:
    boto3_raw_data: "type_defs.GetObjectRequestObjectSummaryGetTypeDef" = (
        dataclasses.field()
    )

    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetObjectRequestObjectSummaryGetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectRequestObjectSummaryGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectRequestObjectVersionGet:
    boto3_raw_data: "type_defs.GetObjectRequestObjectVersionGetTypeDef" = (
        dataclasses.field()
    )

    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetObjectRequestObjectVersionGetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectRequestObjectVersionGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectRequest:
    boto3_raw_data: "type_defs.GetObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetObjectRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadObjectRequestObjectVersionHead:
    boto3_raw_data: "type_defs.HeadObjectRequestObjectVersionHeadTypeDef" = (
        dataclasses.field()
    )

    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HeadObjectRequestObjectVersionHeadTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadObjectRequestObjectVersionHeadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadObjectRequest:
    boto3_raw_data: "type_defs.HeadObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeadObjectRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExpiration:
    boto3_raw_data: "type_defs.LifecycleExpirationTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    ExpiredObjectDeleteMarker = field("ExpiredObjectDeleteMarker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExpirationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExpirationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectIdentifier:
    boto3_raw_data: "type_defs.ObjectIdentifierTypeDef" = dataclasses.field()

    Key = field("Key")
    VersionId = field("VersionId")
    ETag = field("ETag")
    LastModifiedTime = field("LastModifiedTime")
    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLockRetention:
    boto3_raw_data: "type_defs.ObjectLockRetentionTypeDef" = dataclasses.field()

    Mode = field("Mode")
    RetainUntilDate = field("RetainUntilDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLockRetentionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLockRetentionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenameObjectRequest:
    boto3_raw_data: "type_defs.RenameObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    RenameSource = field("RenameSource")
    DestinationIfMatch = field("DestinationIfMatch")
    DestinationIfNoneMatch = field("DestinationIfNoneMatch")
    DestinationIfModifiedSince = field("DestinationIfModifiedSince")
    DestinationIfUnmodifiedSince = field("DestinationIfUnmodifiedSince")
    SourceIfMatch = field("SourceIfMatch")
    SourceIfNoneMatch = field("SourceIfNoneMatch")
    SourceIfModifiedSince = field("SourceIfModifiedSince")
    SourceIfUnmodifiedSince = field("SourceIfUnmodifiedSince")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RenameObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenameObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transition:
    boto3_raw_data: "type_defs.TransitionTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransitionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketAccelerateConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketAccelerateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def AccelerateConfiguration(self):  # pragma: no cover
        return AccelerateConfiguration.make_one(
            self.boto3_raw_data["AccelerateConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketAccelerateConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketAccelerateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMarkerEntry:
    boto3_raw_data: "type_defs.DeleteMarkerEntryTypeDef" = dataclasses.field()

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    Key = field("Key")
    VersionId = field("VersionId")
    IsLatest = field("IsLatest")
    LastModified = field("LastModified")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMarkerEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMarkerEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsAndOperatorOutput:
    boto3_raw_data: "type_defs.AnalyticsAndOperatorOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsAndOperatorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsAndOperator:
    boto3_raw_data: "type_defs.AnalyticsAndOperatorTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketTaggingOutput:
    boto3_raw_data: "type_defs.GetBucketTaggingOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagSet(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketTaggingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketTaggingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectTaggingOutput:
    boto3_raw_data: "type_defs.GetObjectTaggingOutputTypeDef" = dataclasses.field()

    VersionId = field("VersionId")

    @cached_property
    def TagSet(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectTaggingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectTaggingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntelligentTieringAndOperatorOutput:
    boto3_raw_data: "type_defs.IntelligentTieringAndOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IntelligentTieringAndOperatorOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntelligentTieringAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntelligentTieringAndOperator:
    boto3_raw_data: "type_defs.IntelligentTieringAndOperatorTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntelligentTieringAndOperatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntelligentTieringAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleAndOperatorOutput:
    boto3_raw_data: "type_defs.LifecycleRuleAndOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifecycleRuleAndOperatorOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleAndOperator:
    boto3_raw_data: "type_defs.LifecycleRuleAndOperatorTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsAndOperatorOutput:
    boto3_raw_data: "type_defs.MetricsAndOperatorOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AccessPointArn = field("AccessPointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsAndOperatorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsAndOperator:
    boto3_raw_data: "type_defs.MetricsAndOperatorTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AccessPointArn = field("AccessPointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleAndOperatorOutput:
    boto3_raw_data: "type_defs.ReplicationRuleAndOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationRuleAndOperatorOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleAndOperator:
    boto3_raw_data: "type_defs.ReplicationRuleAndOperatorTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tagging:
    boto3_raw_data: "type_defs.TaggingTypeDef" = dataclasses.field()

    @cached_property
    def TagSet(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagSet"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaggingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaggingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsExportDestination:
    boto3_raw_data: "type_defs.AnalyticsExportDestinationTypeDef" = dataclasses.field()

    @cached_property
    def S3BucketDestination(self):  # pragma: no cover
        return AnalyticsS3BucketDestination.make_one(
            self.boto3_raw_data["S3BucketDestination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsExportDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsExportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectRequestBucketPutObject:
    boto3_raw_data: "type_defs.PutObjectRequestBucketPutObjectTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    ACL = field("ACL")
    Body = field("Body")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ContentType = field("ContentType")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    Expires = field("Expires")
    IfMatch = field("IfMatch")
    IfNoneMatch = field("IfNoneMatch")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    WriteOffsetBytes = field("WriteOffsetBytes")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutObjectRequestBucketPutObjectTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectRequestBucketPutObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectRequestObjectPut:
    boto3_raw_data: "type_defs.PutObjectRequestObjectPutTypeDef" = dataclasses.field()

    ACL = field("ACL")
    Body = field("Body")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ContentType = field("ContentType")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    Expires = field("Expires")
    IfMatch = field("IfMatch")
    IfNoneMatch = field("IfNoneMatch")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    WriteOffsetBytes = field("WriteOffsetBytes")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectRequestObjectPutTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectRequestObjectPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectRequestObjectSummaryPut:
    boto3_raw_data: "type_defs.PutObjectRequestObjectSummaryPutTypeDef" = (
        dataclasses.field()
    )

    ACL = field("ACL")
    Body = field("Body")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ContentType = field("ContentType")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    Expires = field("Expires")
    IfMatch = field("IfMatch")
    IfNoneMatch = field("IfNoneMatch")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    WriteOffsetBytes = field("WriteOffsetBytes")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutObjectRequestObjectSummaryPutTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectRequestObjectSummaryPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectRequest:
    boto3_raw_data: "type_defs.PutObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    ACL = field("ACL")
    Body = field("Body")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ContentType = field("ContentType")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    Expires = field("Expires")
    IfMatch = field("IfMatch")
    IfNoneMatch = field("IfNoneMatch")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    WriteOffsetBytes = field("WriteOffsetBytes")
    Metadata = field("Metadata")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutObjectRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadPartRequestMultipartUploadPartUpload:
    boto3_raw_data: "type_defs.UploadPartRequestMultipartUploadPartUploadTypeDef" = (
        dataclasses.field()
    )

    Body = field("Body")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UploadPartRequestMultipartUploadPartUploadTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadPartRequestMultipartUploadPartUploadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadPartRequest:
    boto3_raw_data: "type_defs.UploadPartRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    PartNumber = field("PartNumber")
    UploadId = field("UploadId")
    Body = field("Body")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadPartRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WriteGetObjectResponseRequest:
    boto3_raw_data: "type_defs.WriteGetObjectResponseRequestTypeDef" = (
        dataclasses.field()
    )

    RequestRoute = field("RequestRoute")
    RequestToken = field("RequestToken")
    Body = field("Body")
    StatusCode = field("StatusCode")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    AcceptRanges = field("AcceptRanges")
    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentLength = field("ContentLength")
    ContentRange = field("ContentRange")
    ContentType = field("ContentType")
    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    DeleteMarker = field("DeleteMarker")
    ETag = field("ETag")
    Expires = field("Expires")
    Expiration = field("Expiration")
    LastModified = field("LastModified")
    MissingMeta = field("MissingMeta")
    Metadata = field("Metadata")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    PartsCount = field("PartsCount")
    ReplicationStatus = field("ReplicationStatus")
    RequestCharged = field("RequestCharged")
    Restore = field("Restore")
    ServerSideEncryption = field("ServerSideEncryption")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSEKMSKeyId = field("SSEKMSKeyId")
    StorageClass = field("StorageClass")
    TagCount = field("TagCount")
    VersionId = field("VersionId")
    BucketKeyEnabled = field("BucketKeyEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WriteGetObjectResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WriteGetObjectResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketCopyRequest:
    boto3_raw_data: "type_defs.BucketCopyRequestTypeDef" = dataclasses.field()

    @cached_property
    def CopySource(self):  # pragma: no cover
        return CopySource.make_one(self.boto3_raw_data["CopySource"])

    Key = field("Key")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    SourceClient = field("SourceClient")
    Config = field("Config")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketCopyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketCopyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientCopyRequest:
    boto3_raw_data: "type_defs.ClientCopyRequestTypeDef" = dataclasses.field()

    @cached_property
    def CopySource(self):  # pragma: no cover
        return CopySource.make_one(self.boto3_raw_data["CopySource"])

    Bucket = field("Bucket")
    Key = field("Key")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    SourceClient = field("SourceClient")
    Config = field("Config")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientCopyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientCopyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectCopyRequest:
    boto3_raw_data: "type_defs.ObjectCopyRequestTypeDef" = dataclasses.field()

    @cached_property
    def CopySource(self):  # pragma: no cover
        return CopySource.make_one(self.boto3_raw_data["CopySource"])

    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    SourceClient = field("SourceClient")
    Config = field("Config")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectCopyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectCopyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketDownloadFileobjRequest:
    boto3_raw_data: "type_defs.BucketDownloadFileobjRequestTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Fileobj = field("Fileobj")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketDownloadFileobjRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketDownloadFileobjRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketUploadFileobjRequest:
    boto3_raw_data: "type_defs.BucketUploadFileobjRequestTypeDef" = dataclasses.field()

    Fileobj = field("Fileobj")
    Key = field("Key")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketUploadFileobjRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketUploadFileobjRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientDownloadFileobjRequest:
    boto3_raw_data: "type_defs.ClientDownloadFileobjRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Key = field("Key")
    Fileobj = field("Fileobj")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientDownloadFileobjRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientDownloadFileobjRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientUploadFileobjRequest:
    boto3_raw_data: "type_defs.ClientUploadFileobjRequestTypeDef" = dataclasses.field()

    Fileobj = field("Fileobj")
    Bucket = field("Bucket")
    Key = field("Key")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientUploadFileobjRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientUploadFileobjRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectDownloadFileobjRequest:
    boto3_raw_data: "type_defs.ObjectDownloadFileobjRequestTypeDef" = (
        dataclasses.field()
    )

    Fileobj = field("Fileobj")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectDownloadFileobjRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectDownloadFileobjRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectUploadFileobjRequest:
    boto3_raw_data: "type_defs.ObjectUploadFileobjRequestTypeDef" = dataclasses.field()

    Fileobj = field("Fileobj")
    ExtraArgs = field("ExtraArgs")
    Callback = field("Callback")
    Config = field("Config")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectUploadFileobjRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectUploadFileobjRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketsOutput:
    boto3_raw_data: "type_defs.ListBucketsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Buckets(self):  # pragma: no cover
        return Bucket.make_many(self.boto3_raw_data["Buckets"])

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    ContinuationToken = field("ContinuationToken")
    Prefix = field("Prefix")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBucketsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoryBucketsOutput:
    boto3_raw_data: "type_defs.ListDirectoryBucketsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Buckets(self):  # pragma: no cover
        return Bucket.make_many(self.boto3_raw_data["Buckets"])

    ContinuationToken = field("ContinuationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDirectoryBucketsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoryBucketsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketCorsOutput:
    boto3_raw_data: "type_defs.GetBucketCorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CORSRules(self):  # pragma: no cover
        return CORSRuleOutput.make_many(self.boto3_raw_data["CORSRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketCorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketCorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompletedMultipartUpload:
    boto3_raw_data: "type_defs.CompletedMultipartUploadTypeDef" = dataclasses.field()

    @cached_property
    def Parts(self):  # pragma: no cover
        return CompletedPart.make_many(self.boto3_raw_data["Parts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompletedMultipartUploadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompletedMultipartUploadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyObjectOutput:
    boto3_raw_data: "type_defs.CopyObjectOutputTypeDef" = dataclasses.field()

    @cached_property
    def CopyObjectResult(self):  # pragma: no cover
        return CopyObjectResult.make_one(self.boto3_raw_data["CopyObjectResult"])

    Expiration = field("Expiration")
    CopySourceVersionId = field("CopySourceVersionId")
    VersionId = field("VersionId")
    ServerSideEncryption = field("ServerSideEncryption")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyObjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyObjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadPartCopyOutput:
    boto3_raw_data: "type_defs.UploadPartCopyOutputTypeDef" = dataclasses.field()

    CopySourceVersionId = field("CopySourceVersionId")

    @cached_property
    def CopyPartResult(self):  # pragma: no cover
        return CopyPartResult.make_one(self.boto3_raw_data["CopyPartResult"])

    ServerSideEncryption = field("ServerSideEncryption")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKeyMD5 = field("SSECustomerKeyMD5")
    SSEKMSKeyId = field("SSEKMSKeyId")
    BucketKeyEnabled = field("BucketKeyEnabled")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadPartCopyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadPartCopyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketConfiguration:
    boto3_raw_data: "type_defs.CreateBucketConfigurationTypeDef" = dataclasses.field()

    LocationConstraint = field("LocationConstraint")

    @cached_property
    def Location(self):  # pragma: no cover
        return LocationInfo.make_one(self.boto3_raw_data["Location"])

    @cached_property
    def Bucket(self):  # pragma: no cover
        return BucketInfo.make_one(self.boto3_raw_data["Bucket"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionOutput:
    boto3_raw_data: "type_defs.CreateSessionOutputTypeDef" = dataclasses.field()

    ServerSideEncryption = field("ServerSideEncryption")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return SessionCredentials.make_one(self.boto3_raw_data["Credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLockRule:
    boto3_raw_data: "type_defs.ObjectLockRuleTypeDef" = dataclasses.field()

    @cached_property
    def DefaultRetention(self):  # pragma: no cover
        return DefaultRetention.make_one(self.boto3_raw_data["DefaultRetention"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectLockRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectLockRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectsOutput:
    boto3_raw_data: "type_defs.DeleteObjectsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Deleted(self):  # pragma: no cover
        return DeletedObject.make_many(self.boto3_raw_data["Deleted"])

    RequestCharged = field("RequestCharged")

    @cached_property
    def Errors(self):  # pragma: no cover
        return Error.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryTableConfigurationResult:
    boto3_raw_data: "type_defs.InventoryTableConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationState = field("ConfigurationState")
    TableStatus = field("TableStatus")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["Error"])

    TableName = field("TableName")
    TableArn = field("TableArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InventoryTableConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryTableConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3KeyFilterOutput:
    boto3_raw_data: "type_defs.S3KeyFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def FilterRules(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["FilterRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3KeyFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3KeyFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3KeyFilter:
    boto3_raw_data: "type_defs.S3KeyFilterTypeDef" = dataclasses.field()

    @cached_property
    def FilterRules(self):  # pragma: no cover
        return FilterRule.make_many(self.boto3_raw_data["FilterRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3KeyFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3KeyFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketPolicyStatusOutput:
    boto3_raw_data: "type_defs.GetBucketPolicyStatusOutputTypeDef" = dataclasses.field()

    @cached_property
    def PolicyStatus(self):  # pragma: no cover
        return PolicyStatus.make_one(self.boto3_raw_data["PolicyStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketPolicyStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketPolicyStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAttributesParts:
    boto3_raw_data: "type_defs.GetObjectAttributesPartsTypeDef" = dataclasses.field()

    TotalPartsCount = field("TotalPartsCount")
    PartNumberMarker = field("PartNumberMarker")
    NextPartNumberMarker = field("NextPartNumberMarker")
    MaxParts = field("MaxParts")
    IsTruncated = field("IsTruncated")

    @cached_property
    def Parts(self):  # pragma: no cover
        return ObjectPart.make_many(self.boto3_raw_data["Parts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAttributesPartsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAttributesPartsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectLegalHoldOutput:
    boto3_raw_data: "type_defs.GetObjectLegalHoldOutputTypeDef" = dataclasses.field()

    @cached_property
    def LegalHold(self):  # pragma: no cover
        return ObjectLockLegalHold.make_one(self.boto3_raw_data["LegalHold"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectLegalHoldOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectLegalHoldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectLegalHoldRequest:
    boto3_raw_data: "type_defs.PutObjectLegalHoldRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @cached_property
    def LegalHold(self):  # pragma: no cover
        return ObjectLockLegalHold.make_one(self.boto3_raw_data["LegalHold"])

    RequestPayer = field("RequestPayer")
    VersionId = field("VersionId")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectLegalHoldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectLegalHoldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectRetentionOutput:
    boto3_raw_data: "type_defs.GetObjectRetentionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Retention(self):  # pragma: no cover
        return ObjectLockRetentionOutput.make_one(self.boto3_raw_data["Retention"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectRetentionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectRetentionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicAccessBlockOutput:
    boto3_raw_data: "type_defs.GetPublicAccessBlockOutputTypeDef" = dataclasses.field()

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicAccessBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicAccessBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPublicAccessBlockRequest:
    boto3_raw_data: "type_defs.PutPublicAccessBlockRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPublicAccessBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPublicAccessBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grant:
    boto3_raw_data: "type_defs.GrantTypeDef" = dataclasses.field()

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGrant:
    boto3_raw_data: "type_defs.TargetGrantTypeDef" = dataclasses.field()

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetGrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetGrantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadBucketRequestWaitExtra:
    boto3_raw_data: "type_defs.HeadBucketRequestWaitExtraTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeadBucketRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadBucketRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadBucketRequestWait:
    boto3_raw_data: "type_defs.HeadBucketRequestWaitTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeadBucketRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadBucketRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadObjectRequestWaitExtra:
    boto3_raw_data: "type_defs.HeadObjectRequestWaitExtraTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeadObjectRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadObjectRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeadObjectRequestWait:
    boto3_raw_data: "type_defs.HeadObjectRequestWaitTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    IfMatch = field("IfMatch")
    IfModifiedSince = field("IfModifiedSince")
    IfNoneMatch = field("IfNoneMatch")
    IfUnmodifiedSince = field("IfUnmodifiedSince")
    Range = field("Range")
    ResponseCacheControl = field("ResponseCacheControl")
    ResponseContentDisposition = field("ResponseContentDisposition")
    ResponseContentEncoding = field("ResponseContentEncoding")
    ResponseContentLanguage = field("ResponseContentLanguage")
    ResponseContentType = field("ResponseContentType")
    ResponseExpires = field("ResponseExpires")
    VersionId = field("VersionId")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    RequestPayer = field("RequestPayer")
    PartNumber = field("PartNumber")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumMode = field("ChecksumMode")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeadObjectRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeadObjectRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipartUpload:
    boto3_raw_data: "type_defs.MultipartUploadTypeDef" = dataclasses.field()

    UploadId = field("UploadId")
    Key = field("Key")
    Initiated = field("Initiated")
    StorageClass = field("StorageClass")

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def Initiator(self):  # pragma: no cover
        return Initiator.make_one(self.boto3_raw_data["Initiator"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultipartUploadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MultipartUploadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSerialization:
    boto3_raw_data: "type_defs.InputSerializationTypeDef" = dataclasses.field()

    @cached_property
    def CSV(self):  # pragma: no cover
        return CSVInput.make_one(self.boto3_raw_data["CSV"])

    CompressionType = field("CompressionType")

    @cached_property
    def JSON(self):  # pragma: no cover
        return JSONInput.make_one(self.boto3_raw_data["JSON"])

    Parquet = field("Parquet")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputSerializationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSerializationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryEncryptionOutput:
    boto3_raw_data: "type_defs.InventoryEncryptionOutputTypeDef" = dataclasses.field()

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMS.make_one(self.boto3_raw_data["SSEKMS"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryEncryptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryEncryption:
    boto3_raw_data: "type_defs.InventoryEncryptionTypeDef" = dataclasses.field()

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMS.make_one(self.boto3_raw_data["SSEKMS"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryTableConfiguration:
    boto3_raw_data: "type_defs.InventoryTableConfigurationTypeDef" = dataclasses.field()

    ConfigurationState = field("ConfigurationState")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return MetadataTableEncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryTableConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryTableConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryTableConfigurationUpdates:
    boto3_raw_data: "type_defs.InventoryTableConfigurationUpdatesTypeDef" = (
        dataclasses.field()
    )

    ConfigurationState = field("ConfigurationState")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return MetadataTableEncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InventoryTableConfigurationUpdatesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryTableConfigurationUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSerialization:
    boto3_raw_data: "type_defs.OutputSerializationTypeDef" = dataclasses.field()

    @cached_property
    def CSV(self):  # pragma: no cover
        return CSVOutput.make_one(self.boto3_raw_data["CSV"])

    @cached_property
    def JSON(self):  # pragma: no cover
        return JSONOutput.make_one(self.boto3_raw_data["JSON"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputSerializationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputSerializationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JournalTableConfigurationResult:
    boto3_raw_data: "type_defs.JournalTableConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    TableStatus = field("TableStatus")
    TableName = field("TableName")

    @cached_property
    def RecordExpiration(self):  # pragma: no cover
        return RecordExpiration.make_one(self.boto3_raw_data["RecordExpiration"])

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["Error"])

    TableArn = field("TableArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JournalTableConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JournalTableConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JournalTableConfiguration:
    boto3_raw_data: "type_defs.JournalTableConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def RecordExpiration(self):  # pragma: no cover
        return RecordExpiration.make_one(self.boto3_raw_data["RecordExpiration"])

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return MetadataTableEncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JournalTableConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JournalTableConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JournalTableConfigurationUpdates:
    boto3_raw_data: "type_defs.JournalTableConfigurationUpdatesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecordExpiration(self):  # pragma: no cover
        return RecordExpiration.make_one(self.boto3_raw_data["RecordExpiration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JournalTableConfigurationUpdatesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JournalTableConfigurationUpdatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOutput:
    boto3_raw_data: "type_defs.RuleOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")
    Status = field("Status")

    @cached_property
    def Expiration(self):  # pragma: no cover
        return LifecycleExpirationOutput.make_one(self.boto3_raw_data["Expiration"])

    ID = field("ID")

    @cached_property
    def Transition(self):  # pragma: no cover
        return TransitionOutput.make_one(self.boto3_raw_data["Transition"])

    @cached_property
    def NoncurrentVersionTransition(self):  # pragma: no cover
        return NoncurrentVersionTransition.make_one(
            self.boto3_raw_data["NoncurrentVersionTransition"]
        )

    @cached_property
    def NoncurrentVersionExpiration(self):  # pragma: no cover
        return NoncurrentVersionExpiration.make_one(
            self.boto3_raw_data["NoncurrentVersionExpiration"]
        )

    @cached_property
    def AbortIncompleteMultipartUpload(self):  # pragma: no cover
        return AbortIncompleteMultipartUpload.make_one(
            self.boto3_raw_data["AbortIncompleteMultipartUpload"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketsRequestPaginate:
    boto3_raw_data: "type_defs.ListBucketsRequestPaginateTypeDef" = dataclasses.field()

    Prefix = field("Prefix")
    BucketRegion = field("BucketRegion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBucketsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoryBucketsRequestPaginate:
    boto3_raw_data: "type_defs.ListDirectoryBucketsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDirectoryBucketsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoryBucketsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultipartUploadsRequestPaginate:
    boto3_raw_data: "type_defs.ListMultipartUploadsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    Prefix = field("Prefix")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultipartUploadsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartUploadsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    Prefix = field("Prefix")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")
    OptionalObjectAttributes = field("OptionalObjectAttributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObjectVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectsRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectsRequestPaginateTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    Prefix = field("Prefix")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    OptionalObjectAttributes = field("OptionalObjectAttributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectsV2RequestPaginate:
    boto3_raw_data: "type_defs.ListObjectsV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Delimiter = field("Delimiter")
    EncodingType = field("EncodingType")
    Prefix = field("Prefix")
    FetchOwner = field("FetchOwner")
    StartAfter = field("StartAfter")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    OptionalObjectAttributes = field("OptionalObjectAttributes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectsV2RequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectsV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsRequestPaginate:
    boto3_raw_data: "type_defs.ListPartsRequestPaginateTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    UploadId = field("UploadId")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPartsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartsOutput:
    boto3_raw_data: "type_defs.ListPartsOutputTypeDef" = dataclasses.field()

    AbortDate = field("AbortDate")
    AbortRuleId = field("AbortRuleId")
    Bucket = field("Bucket")
    Key = field("Key")
    UploadId = field("UploadId")
    PartNumberMarker = field("PartNumberMarker")
    NextPartNumberMarker = field("NextPartNumberMarker")
    MaxParts = field("MaxParts")
    IsTruncated = field("IsTruncated")

    @cached_property
    def Parts(self):  # pragma: no cover
        return Part.make_many(self.boto3_raw_data["Parts"])

    @cached_property
    def Initiator(self):  # pragma: no cover
        return Initiator.make_one(self.boto3_raw_data["Initiator"])

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    StorageClass = field("StorageClass")
    RequestCharged = field("RequestCharged")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPartsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListPartsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataTableConfigurationResult:
    boto3_raw_data: "type_defs.MetadataTableConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3TablesDestinationResult(self):  # pragma: no cover
        return S3TablesDestinationResult.make_one(
            self.boto3_raw_data["S3TablesDestinationResult"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MetadataTableConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataTableConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataTableConfiguration:
    boto3_raw_data: "type_defs.MetadataTableConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def S3TablesDestination(self):  # pragma: no cover
        return S3TablesDestination.make_one(self.boto3_raw_data["S3TablesDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataTableConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataTableConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metrics:
    boto3_raw_data: "type_defs.MetricsTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def EventThreshold(self):  # pragma: no cover
        return ReplicationTimeValue.make_one(self.boto3_raw_data["EventThreshold"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTime:
    boto3_raw_data: "type_defs.ReplicationTimeTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Time(self):  # pragma: no cover
        return ReplicationTimeValue.make_one(self.boto3_raw_data["Time"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigurationDeprecatedResponse:
    boto3_raw_data: "type_defs.NotificationConfigurationDeprecatedResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TopicConfiguration(self):  # pragma: no cover
        return TopicConfigurationDeprecatedOutput.make_one(
            self.boto3_raw_data["TopicConfiguration"]
        )

    @cached_property
    def QueueConfiguration(self):  # pragma: no cover
        return QueueConfigurationDeprecatedOutput.make_one(
            self.boto3_raw_data["QueueConfiguration"]
        )

    @cached_property
    def CloudFunctionConfiguration(self):  # pragma: no cover
        return CloudFunctionConfigurationOutput.make_one(
            self.boto3_raw_data["CloudFunctionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotificationConfigurationDeprecatedResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationDeprecatedResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Object:
    boto3_raw_data: "type_defs.ObjectTypeDef" = dataclasses.field()

    Key = field("Key")
    LastModified = field("LastModified")
    ETag = field("ETag")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")
    Size = field("Size")
    StorageClass = field("StorageClass")

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def RestoreStatus(self):  # pragma: no cover
        return RestoreStatus.make_one(self.boto3_raw_data["RestoreStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectVersion:
    boto3_raw_data: "type_defs.ObjectVersionTypeDef" = dataclasses.field()

    ETag = field("ETag")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")
    Size = field("Size")
    StorageClass = field("StorageClass")
    Key = field("Key")
    VersionId = field("VersionId")
    IsLatest = field("IsLatest")
    LastModified = field("LastModified")

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def RestoreStatus(self):  # pragma: no cover
        return RestoreStatus.make_one(self.boto3_raw_data["RestoreStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnershipControlsOutput:
    boto3_raw_data: "type_defs.OwnershipControlsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return OwnershipControlsRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnershipControlsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnershipControlsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnershipControls:
    boto3_raw_data: "type_defs.OwnershipControlsTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return OwnershipControlsRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OwnershipControlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnershipControlsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetObjectKeyFormatOutput:
    boto3_raw_data: "type_defs.TargetObjectKeyFormatOutputTypeDef" = dataclasses.field()

    SimplePrefix = field("SimplePrefix")

    @cached_property
    def PartitionedPrefix(self):  # pragma: no cover
        return PartitionedPrefix.make_one(self.boto3_raw_data["PartitionedPrefix"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetObjectKeyFormatOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetObjectKeyFormatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetObjectKeyFormat:
    boto3_raw_data: "type_defs.TargetObjectKeyFormatTypeDef" = dataclasses.field()

    SimplePrefix = field("SimplePrefix")

    @cached_property
    def PartitionedPrefix(self):  # pragma: no cover
        return PartitionedPrefix.make_one(self.boto3_raw_data["PartitionedPrefix"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetObjectKeyFormatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetObjectKeyFormatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProgressEvent:
    boto3_raw_data: "type_defs.ProgressEventTypeDef" = dataclasses.field()

    @cached_property
    def Details(self):  # pragma: no cover
        return Progress.make_one(self.boto3_raw_data["Details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProgressEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProgressEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketRequestPaymentRequestBucketRequestPaymentPut:
    boto3_raw_data: (
        "type_defs.PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef"
    ) = dataclasses.field()

    @cached_property
    def RequestPaymentConfiguration(self):  # pragma: no cover
        return RequestPaymentConfiguration.make_one(
            self.boto3_raw_data["RequestPaymentConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef"
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
                "type_defs.PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketRequestPaymentRequest:
    boto3_raw_data: "type_defs.PutBucketRequestPaymentRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def RequestPaymentConfiguration(self):  # pragma: no cover
        return RequestPaymentConfiguration.make_one(
            self.boto3_raw_data["RequestPaymentConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutBucketRequestPaymentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketRequestPaymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketVersioningRequestBucketVersioningPut:
    boto3_raw_data: "type_defs.PutBucketVersioningRequestBucketVersioningPutTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VersioningConfiguration(self):  # pragma: no cover
        return VersioningConfiguration.make_one(
            self.boto3_raw_data["VersioningConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    MFA = field("MFA")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketVersioningRequestBucketVersioningPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketVersioningRequestBucketVersioningPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketVersioningRequest:
    boto3_raw_data: "type_defs.PutBucketVersioningRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def VersioningConfiguration(self):  # pragma: no cover
        return VersioningConfiguration.make_one(
            self.boto3_raw_data["VersioningConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    MFA = field("MFA")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketVersioningRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketVersioningRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRule:
    boto3_raw_data: "type_defs.RoutingRuleTypeDef" = dataclasses.field()

    @cached_property
    def Redirect(self):  # pragma: no cover
        return Redirect.make_one(self.boto3_raw_data["Redirect"])

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionRule:
    boto3_raw_data: "type_defs.ServerSideEncryptionRuleTypeDef" = dataclasses.field()

    @cached_property
    def ApplyServerSideEncryptionByDefault(self):  # pragma: no cover
        return ServerSideEncryptionByDefault.make_one(
            self.boto3_raw_data["ApplyServerSideEncryptionByDefault"]
        )

    BucketKeyEnabled = field("BucketKeyEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerSideEncryptionRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSelectionCriteria:
    boto3_raw_data: "type_defs.SourceSelectionCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def SseKmsEncryptedObjects(self):  # pragma: no cover
        return SseKmsEncryptedObjects.make_one(
            self.boto3_raw_data["SseKmsEncryptedObjects"]
        )

    @cached_property
    def ReplicaModifications(self):  # pragma: no cover
        return ReplicaModifications.make_one(
            self.boto3_raw_data["ReplicaModifications"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceSelectionCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceSelectionCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatsEvent:
    boto3_raw_data: "type_defs.StatsEventTypeDef" = dataclasses.field()

    @cached_property
    def Details(self):  # pragma: no cover
        return Stats.make_one(self.boto3_raw_data["Details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatsEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatsEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Delete:
    boto3_raw_data: "type_defs.DeleteTypeDef" = dataclasses.field()

    @cached_property
    def Objects(self):  # pragma: no cover
        return ObjectIdentifier.make_many(self.boto3_raw_data["Objects"])

    Quiet = field("Quiet")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsFilterOutput:
    boto3_raw_data: "type_defs.AnalyticsFilterOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return AnalyticsAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsFilter:
    boto3_raw_data: "type_defs.AnalyticsFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return AnalyticsAndOperator.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyticsFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalyticsFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntelligentTieringFilterOutput:
    boto3_raw_data: "type_defs.IntelligentTieringFilterOutputTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return IntelligentTieringAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntelligentTieringFilterOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntelligentTieringFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntelligentTieringFilter:
    boto3_raw_data: "type_defs.IntelligentTieringFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return IntelligentTieringAndOperator.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntelligentTieringFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntelligentTieringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleFilterOutput:
    boto3_raw_data: "type_defs.LifecycleRuleFilterOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @cached_property
    def And(self):  # pragma: no cover
        return LifecycleRuleAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsFilterOutput:
    boto3_raw_data: "type_defs.MetricsFilterOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    AccessPointArn = field("AccessPointArn")

    @cached_property
    def And(self):  # pragma: no cover
        return MetricsAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsFilter:
    boto3_raw_data: "type_defs.MetricsFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    AccessPointArn = field("AccessPointArn")

    @cached_property
    def And(self):  # pragma: no cover
        return MetricsAndOperator.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricsFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricsFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleFilterOutput:
    boto3_raw_data: "type_defs.ReplicationRuleFilterOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return ReplicationRuleAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleFilter:
    boto3_raw_data: "type_defs.ReplicationRuleFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return ReplicationRuleAndOperator.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketTaggingRequestBucketTaggingPut:
    boto3_raw_data: "type_defs.PutBucketTaggingRequestBucketTaggingPutTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tagging(self):  # pragma: no cover
        return Tagging.make_one(self.boto3_raw_data["Tagging"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketTaggingRequestBucketTaggingPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketTaggingRequestBucketTaggingPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketTaggingRequest:
    boto3_raw_data: "type_defs.PutBucketTaggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def Tagging(self):  # pragma: no cover
        return Tagging.make_one(self.boto3_raw_data["Tagging"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectTaggingRequest:
    boto3_raw_data: "type_defs.PutObjectTaggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")

    @cached_property
    def Tagging(self):  # pragma: no cover
        return Tagging.make_one(self.boto3_raw_data["Tagging"])

    VersionId = field("VersionId")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    RequestPayer = field("RequestPayer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageClassAnalysisDataExport:
    boto3_raw_data: "type_defs.StorageClassAnalysisDataExportTypeDef" = (
        dataclasses.field()
    )

    OutputSchemaVersion = field("OutputSchemaVersion")

    @cached_property
    def Destination(self):  # pragma: no cover
        return AnalyticsExportDestination.make_one(self.boto3_raw_data["Destination"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StorageClassAnalysisDataExportTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageClassAnalysisDataExportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyObjectRequestObjectCopyFrom:
    boto3_raw_data: "type_defs.CopyObjectRequestObjectCopyFromTypeDef" = (
        dataclasses.field()
    )

    CopySource = field("CopySource")
    ACL = field("ACL")
    CacheControl = field("CacheControl")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    CopySourceIfMatch = field("CopySourceIfMatch")
    CopySourceIfModifiedSince = field("CopySourceIfModifiedSince")
    CopySourceIfNoneMatch = field("CopySourceIfNoneMatch")
    CopySourceIfUnmodifiedSince = field("CopySourceIfUnmodifiedSince")
    Expires = field("Expires")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    Metadata = field("Metadata")
    MetadataDirective = field("MetadataDirective")
    TaggingDirective = field("TaggingDirective")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    CopySourceSSECustomerAlgorithm = field("CopySourceSSECustomerAlgorithm")
    CopySourceSSECustomerKey = field("CopySourceSSECustomerKey")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ExpectedSourceBucketOwner = field("ExpectedSourceBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CopyObjectRequestObjectCopyFromTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyObjectRequestObjectCopyFromTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyObjectRequestObjectSummaryCopyFrom:
    boto3_raw_data: "type_defs.CopyObjectRequestObjectSummaryCopyFromTypeDef" = (
        dataclasses.field()
    )

    CopySource = field("CopySource")
    ACL = field("ACL")
    CacheControl = field("CacheControl")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    CopySourceIfMatch = field("CopySourceIfMatch")
    CopySourceIfModifiedSince = field("CopySourceIfModifiedSince")
    CopySourceIfNoneMatch = field("CopySourceIfNoneMatch")
    CopySourceIfUnmodifiedSince = field("CopySourceIfUnmodifiedSince")
    Expires = field("Expires")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    Metadata = field("Metadata")
    MetadataDirective = field("MetadataDirective")
    TaggingDirective = field("TaggingDirective")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    CopySourceSSECustomerAlgorithm = field("CopySourceSSECustomerAlgorithm")
    CopySourceSSECustomerKey = field("CopySourceSSECustomerKey")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ExpectedSourceBucketOwner = field("ExpectedSourceBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CopyObjectRequestObjectSummaryCopyFromTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyObjectRequestObjectSummaryCopyFromTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyObjectRequest:
    boto3_raw_data: "type_defs.CopyObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    CopySource = field("CopySource")
    Key = field("Key")
    ACL = field("ACL")
    CacheControl = field("CacheControl")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    ContentType = field("ContentType")
    CopySourceIfMatch = field("CopySourceIfMatch")
    CopySourceIfModifiedSince = field("CopySourceIfModifiedSince")
    CopySourceIfNoneMatch = field("CopySourceIfNoneMatch")
    CopySourceIfUnmodifiedSince = field("CopySourceIfUnmodifiedSince")
    Expires = field("Expires")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWriteACP = field("GrantWriteACP")
    Metadata = field("Metadata")
    MetadataDirective = field("MetadataDirective")
    TaggingDirective = field("TaggingDirective")
    ServerSideEncryption = field("ServerSideEncryption")
    StorageClass = field("StorageClass")
    WebsiteRedirectLocation = field("WebsiteRedirectLocation")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    SSEKMSKeyId = field("SSEKMSKeyId")
    SSEKMSEncryptionContext = field("SSEKMSEncryptionContext")
    BucketKeyEnabled = field("BucketKeyEnabled")
    CopySourceSSECustomerAlgorithm = field("CopySourceSSECustomerAlgorithm")
    CopySourceSSECustomerKey = field("CopySourceSSECustomerKey")
    RequestPayer = field("RequestPayer")
    Tagging = field("Tagging")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ExpectedSourceBucketOwner = field("ExpectedSourceBucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyObjectRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadPartCopyRequestMultipartUploadPartCopyFrom:
    boto3_raw_data: (
        "type_defs.UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef"
    ) = dataclasses.field()

    CopySource = field("CopySource")
    CopySourceIfMatch = field("CopySourceIfMatch")
    CopySourceIfModifiedSince = field("CopySourceIfModifiedSince")
    CopySourceIfNoneMatch = field("CopySourceIfNoneMatch")
    CopySourceIfUnmodifiedSince = field("CopySourceIfUnmodifiedSince")
    CopySourceRange = field("CopySourceRange")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    CopySourceSSECustomerAlgorithm = field("CopySourceSSECustomerAlgorithm")
    CopySourceSSECustomerKey = field("CopySourceSSECustomerKey")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ExpectedSourceBucketOwner = field("ExpectedSourceBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef"
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
                "type_defs.UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadPartCopyRequest:
    boto3_raw_data: "type_defs.UploadPartCopyRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    CopySource = field("CopySource")
    Key = field("Key")
    PartNumber = field("PartNumber")
    UploadId = field("UploadId")
    CopySourceIfMatch = field("CopySourceIfMatch")
    CopySourceIfModifiedSince = field("CopySourceIfModifiedSince")
    CopySourceIfNoneMatch = field("CopySourceIfNoneMatch")
    CopySourceIfUnmodifiedSince = field("CopySourceIfUnmodifiedSince")
    CopySourceRange = field("CopySourceRange")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")
    CopySourceSSECustomerAlgorithm = field("CopySourceSSECustomerAlgorithm")
    CopySourceSSECustomerKey = field("CopySourceSSECustomerKey")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ExpectedSourceBucketOwner = field("ExpectedSourceBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadPartCopyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadPartCopyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CORSConfiguration:
    boto3_raw_data: "type_defs.CORSConfigurationTypeDef" = dataclasses.field()

    CORSRules = field("CORSRules")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CORSConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CORSConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartUploadRequestMultipartUploadComplete:
    boto3_raw_data: (
        "type_defs.CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MultipartUpload(self):  # pragma: no cover
        return CompletedMultipartUpload.make_one(self.boto3_raw_data["MultipartUpload"])

    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")
    MpuObjectSize = field("MpuObjectSize")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatch = field("IfMatch")
    IfNoneMatch = field("IfNoneMatch")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef"
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
                "type_defs.CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteMultipartUploadRequest:
    boto3_raw_data: "type_defs.CompleteMultipartUploadRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Key = field("Key")
    UploadId = field("UploadId")

    @cached_property
    def MultipartUpload(self):  # pragma: no cover
        return CompletedMultipartUpload.make_one(self.boto3_raw_data["MultipartUpload"])

    ChecksumCRC32 = field("ChecksumCRC32")
    ChecksumCRC32C = field("ChecksumCRC32C")
    ChecksumCRC64NVME = field("ChecksumCRC64NVME")
    ChecksumSHA1 = field("ChecksumSHA1")
    ChecksumSHA256 = field("ChecksumSHA256")
    ChecksumType = field("ChecksumType")
    MpuObjectSize = field("MpuObjectSize")
    RequestPayer = field("RequestPayer")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    IfMatch = field("IfMatch")
    IfNoneMatch = field("IfNoneMatch")
    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompleteMultipartUploadRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteMultipartUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketRequestBucketCreate:
    boto3_raw_data: "type_defs.CreateBucketRequestBucketCreateTypeDef" = (
        dataclasses.field()
    )

    ACL = field("ACL")

    @cached_property
    def CreateBucketConfiguration(self):  # pragma: no cover
        return CreateBucketConfiguration.make_one(
            self.boto3_raw_data["CreateBucketConfiguration"]
        )

    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    ObjectLockEnabledForBucket = field("ObjectLockEnabledForBucket")
    ObjectOwnership = field("ObjectOwnership")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBucketRequestBucketCreateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketRequestBucketCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketRequestServiceResourceCreateBucket:
    boto3_raw_data: (
        "type_defs.CreateBucketRequestServiceResourceCreateBucketTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")
    ACL = field("ACL")

    @cached_property
    def CreateBucketConfiguration(self):  # pragma: no cover
        return CreateBucketConfiguration.make_one(
            self.boto3_raw_data["CreateBucketConfiguration"]
        )

    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    ObjectLockEnabledForBucket = field("ObjectLockEnabledForBucket")
    ObjectOwnership = field("ObjectOwnership")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBucketRequestServiceResourceCreateBucketTypeDef"
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
                "type_defs.CreateBucketRequestServiceResourceCreateBucketTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketRequest:
    boto3_raw_data: "type_defs.CreateBucketRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ACL = field("ACL")

    @cached_property
    def CreateBucketConfiguration(self):  # pragma: no cover
        return CreateBucketConfiguration.make_one(
            self.boto3_raw_data["CreateBucketConfiguration"]
        )

    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    ObjectLockEnabledForBucket = field("ObjectLockEnabledForBucket")
    ObjectOwnership = field("ObjectOwnership")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLockConfiguration:
    boto3_raw_data: "type_defs.ObjectLockConfigurationTypeDef" = dataclasses.field()

    ObjectLockEnabled = field("ObjectLockEnabled")

    @cached_property
    def Rule(self):  # pragma: no cover
        return ObjectLockRule.make_one(self.boto3_raw_data["Rule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLockConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigurationFilterOutput:
    boto3_raw_data: "type_defs.NotificationConfigurationFilterOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Key(self):  # pragma: no cover
        return S3KeyFilterOutput.make_one(self.boto3_raw_data["Key"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotificationConfigurationFilterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAttributesOutput:
    boto3_raw_data: "type_defs.GetObjectAttributesOutputTypeDef" = dataclasses.field()

    DeleteMarker = field("DeleteMarker")
    LastModified = field("LastModified")
    VersionId = field("VersionId")
    RequestCharged = field("RequestCharged")
    ETag = field("ETag")

    @cached_property
    def Checksum(self):  # pragma: no cover
        return Checksum.make_one(self.boto3_raw_data["Checksum"])

    @cached_property
    def ObjectParts(self):  # pragma: no cover
        return GetObjectAttributesParts.make_one(self.boto3_raw_data["ObjectParts"])

    StorageClass = field("StorageClass")
    ObjectSize = field("ObjectSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAttributesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlPolicy:
    boto3_raw_data: "type_defs.AccessControlPolicyTypeDef" = dataclasses.field()

    @cached_property
    def Grants(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["Grants"])

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketAclOutput:
    boto3_raw_data: "type_defs.GetBucketAclOutputTypeDef" = dataclasses.field()

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def Grants(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["Grants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketAclOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAclOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAclOutput:
    boto3_raw_data: "type_defs.GetObjectAclOutputTypeDef" = dataclasses.field()

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def Grants(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["Grants"])

    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAclOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAclOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    CannedACL = field("CannedACL")

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return Grant.make_many(self.boto3_raw_data["AccessControlList"])

    @cached_property
    def Tagging(self):  # pragma: no cover
        return Tagging.make_one(self.boto3_raw_data["Tagging"])

    @cached_property
    def UserMetadata(self):  # pragma: no cover
        return MetadataEntry.make_many(self.boto3_raw_data["UserMetadata"])

    StorageClass = field("StorageClass")

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
class ListMultipartUploadsOutput:
    boto3_raw_data: "type_defs.ListMultipartUploadsOutputTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    KeyMarker = field("KeyMarker")
    UploadIdMarker = field("UploadIdMarker")
    NextKeyMarker = field("NextKeyMarker")
    Prefix = field("Prefix")
    Delimiter = field("Delimiter")
    NextUploadIdMarker = field("NextUploadIdMarker")
    MaxUploads = field("MaxUploads")
    IsTruncated = field("IsTruncated")

    @cached_property
    def Uploads(self):  # pragma: no cover
        return MultipartUpload.make_many(self.boto3_raw_data["Uploads"])

    EncodingType = field("EncodingType")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @cached_property
    def CommonPrefixes(self):  # pragma: no cover
        return CommonPrefix.make_many(self.boto3_raw_data["CommonPrefixes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMultipartUploadsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultipartUploadsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryS3BucketDestinationOutput:
    boto3_raw_data: "type_defs.InventoryS3BucketDestinationOutputTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Format = field("Format")
    AccountId = field("AccountId")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return InventoryEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InventoryS3BucketDestinationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryS3BucketDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryS3BucketDestination:
    boto3_raw_data: "type_defs.InventoryS3BucketDestinationTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Format = field("Format")
    AccountId = field("AccountId")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return InventoryEncryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryS3BucketDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryS3BucketDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBucketMetadataInventoryTableConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateBucketMetadataInventoryTableConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def InventoryTableConfiguration(self):  # pragma: no cover
        return InventoryTableConfigurationUpdates.make_one(
            self.boto3_raw_data["InventoryTableConfiguration"]
        )

    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBucketMetadataInventoryTableConfigurationRequestTypeDef"
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
                "type_defs.UpdateBucketMetadataInventoryTableConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectObjectContentRequest:
    boto3_raw_data: "type_defs.SelectObjectContentRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    Expression = field("Expression")
    ExpressionType = field("ExpressionType")

    @cached_property
    def InputSerialization(self):  # pragma: no cover
        return InputSerialization.make_one(self.boto3_raw_data["InputSerialization"])

    @cached_property
    def OutputSerialization(self):  # pragma: no cover
        return OutputSerialization.make_one(self.boto3_raw_data["OutputSerialization"])

    SSECustomerAlgorithm = field("SSECustomerAlgorithm")
    SSECustomerKey = field("SSECustomerKey")

    @cached_property
    def RequestProgress(self):  # pragma: no cover
        return RequestProgress.make_one(self.boto3_raw_data["RequestProgress"])

    @cached_property
    def ScanRange(self):  # pragma: no cover
        return ScanRange.make_one(self.boto3_raw_data["ScanRange"])

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectObjectContentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectObjectContentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectParameters:
    boto3_raw_data: "type_defs.SelectParametersTypeDef" = dataclasses.field()

    @cached_property
    def InputSerialization(self):  # pragma: no cover
        return InputSerialization.make_one(self.boto3_raw_data["InputSerialization"])

    ExpressionType = field("ExpressionType")
    Expression = field("Expression")

    @cached_property
    def OutputSerialization(self):  # pragma: no cover
        return OutputSerialization.make_one(self.boto3_raw_data["OutputSerialization"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfigurationResult:
    boto3_raw_data: "type_defs.MetadataConfigurationResultTypeDef" = dataclasses.field()

    @cached_property
    def DestinationResult(self):  # pragma: no cover
        return DestinationResult.make_one(self.boto3_raw_data["DestinationResult"])

    @cached_property
    def JournalTableConfigurationResult(self):  # pragma: no cover
        return JournalTableConfigurationResult.make_one(
            self.boto3_raw_data["JournalTableConfigurationResult"]
        )

    @cached_property
    def InventoryTableConfigurationResult(self):  # pragma: no cover
        return InventoryTableConfigurationResult.make_one(
            self.boto3_raw_data["InventoryTableConfigurationResult"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataConfigurationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfiguration:
    boto3_raw_data: "type_defs.MetadataConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def JournalTableConfiguration(self):  # pragma: no cover
        return JournalTableConfiguration.make_one(
            self.boto3_raw_data["JournalTableConfiguration"]
        )

    @cached_property
    def InventoryTableConfiguration(self):  # pragma: no cover
        return InventoryTableConfiguration.make_one(
            self.boto3_raw_data["InventoryTableConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBucketMetadataJournalTableConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateBucketMetadataJournalTableConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def JournalTableConfiguration(self):  # pragma: no cover
        return JournalTableConfigurationUpdates.make_one(
            self.boto3_raw_data["JournalTableConfiguration"]
        )

    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBucketMetadataJournalTableConfigurationRequestTypeDef"
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
                "type_defs.UpdateBucketMetadataJournalTableConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLifecycleOutput:
    boto3_raw_data: "type_defs.GetBucketLifecycleOutputTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return RuleOutput.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketLifecycleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLifecycleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetadataTableConfigurationResult:
    boto3_raw_data: "type_defs.GetBucketMetadataTableConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetadataTableConfigurationResult(self):  # pragma: no cover
        return MetadataTableConfigurationResult.make_one(
            self.boto3_raw_data["MetadataTableConfigurationResult"]
        )

    Status = field("Status")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetadataTableConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetadataTableConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketMetadataTableConfigurationRequest:
    boto3_raw_data: "type_defs.CreateBucketMetadataTableConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def MetadataTableConfiguration(self):  # pragma: no cover
        return MetadataTableConfiguration.make_one(
            self.boto3_raw_data["MetadataTableConfiguration"]
        )

    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBucketMetadataTableConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketMetadataTableConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Account = field("Account")
    StorageClass = field("StorageClass")

    @cached_property
    def AccessControlTranslation(self):  # pragma: no cover
        return AccessControlTranslation.make_one(
            self.boto3_raw_data["AccessControlTranslation"]
        )

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def ReplicationTime(self):  # pragma: no cover
        return ReplicationTime.make_one(self.boto3_raw_data["ReplicationTime"])

    @cached_property
    def Metrics(self):  # pragma: no cover
        return Metrics.make_one(self.boto3_raw_data["Metrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectsOutput:
    boto3_raw_data: "type_defs.ListObjectsOutputTypeDef" = dataclasses.field()

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")
    NextMarker = field("NextMarker")
    Name = field("Name")
    Prefix = field("Prefix")
    Delimiter = field("Delimiter")
    MaxKeys = field("MaxKeys")
    EncodingType = field("EncodingType")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @cached_property
    def Contents(self):  # pragma: no cover
        return Object.make_many(self.boto3_raw_data["Contents"])

    @cached_property
    def CommonPrefixes(self):  # pragma: no cover
        return CommonPrefix.make_many(self.boto3_raw_data["CommonPrefixes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListObjectsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectsV2Output:
    boto3_raw_data: "type_defs.ListObjectsV2OutputTypeDef" = dataclasses.field()

    IsTruncated = field("IsTruncated")
    Name = field("Name")
    Prefix = field("Prefix")
    Delimiter = field("Delimiter")
    MaxKeys = field("MaxKeys")
    EncodingType = field("EncodingType")
    KeyCount = field("KeyCount")
    ContinuationToken = field("ContinuationToken")
    NextContinuationToken = field("NextContinuationToken")
    StartAfter = field("StartAfter")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @cached_property
    def Contents(self):  # pragma: no cover
        return Object.make_many(self.boto3_raw_data["Contents"])

    @cached_property
    def CommonPrefixes(self):  # pragma: no cover
        return CommonPrefix.make_many(self.boto3_raw_data["CommonPrefixes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectsV2OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectsV2OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectVersionsOutput:
    boto3_raw_data: "type_defs.ListObjectVersionsOutputTypeDef" = dataclasses.field()

    IsTruncated = field("IsTruncated")
    KeyMarker = field("KeyMarker")
    VersionIdMarker = field("VersionIdMarker")
    NextKeyMarker = field("NextKeyMarker")
    NextVersionIdMarker = field("NextVersionIdMarker")

    @cached_property
    def Versions(self):  # pragma: no cover
        return ObjectVersion.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def DeleteMarkers(self):  # pragma: no cover
        return DeleteMarkerEntry.make_many(self.boto3_raw_data["DeleteMarkers"])

    Name = field("Name")
    Prefix = field("Prefix")
    Delimiter = field("Delimiter")
    MaxKeys = field("MaxKeys")
    EncodingType = field("EncodingType")
    RequestCharged = field("RequestCharged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @cached_property
    def CommonPrefixes(self):  # pragma: no cover
        return CommonPrefix.make_many(self.boto3_raw_data["CommonPrefixes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectVersionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketOwnershipControlsOutput:
    boto3_raw_data: "type_defs.GetBucketOwnershipControlsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OwnershipControls(self):  # pragma: no cover
        return OwnershipControlsOutput.make_one(
            self.boto3_raw_data["OwnershipControls"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBucketOwnershipControlsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketOwnershipControlsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingEnabledOutput:
    boto3_raw_data: "type_defs.LoggingEnabledOutputTypeDef" = dataclasses.field()

    TargetBucket = field("TargetBucket")
    TargetPrefix = field("TargetPrefix")

    @cached_property
    def TargetGrants(self):  # pragma: no cover
        return TargetGrant.make_many(self.boto3_raw_data["TargetGrants"])

    @cached_property
    def TargetObjectKeyFormat(self):  # pragma: no cover
        return TargetObjectKeyFormatOutput.make_one(
            self.boto3_raw_data["TargetObjectKeyFormat"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingEnabledOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingEnabledOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketWebsiteOutput:
    boto3_raw_data: "type_defs.GetBucketWebsiteOutputTypeDef" = dataclasses.field()

    @cached_property
    def RedirectAllRequestsTo(self):  # pragma: no cover
        return RedirectAllRequestsTo.make_one(
            self.boto3_raw_data["RedirectAllRequestsTo"]
        )

    @cached_property
    def IndexDocument(self):  # pragma: no cover
        return IndexDocument.make_one(self.boto3_raw_data["IndexDocument"])

    @cached_property
    def ErrorDocument(self):  # pragma: no cover
        return ErrorDocument.make_one(self.boto3_raw_data["ErrorDocument"])

    @cached_property
    def RoutingRules(self):  # pragma: no cover
        return RoutingRule.make_many(self.boto3_raw_data["RoutingRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketWebsiteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketWebsiteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebsiteConfiguration:
    boto3_raw_data: "type_defs.WebsiteConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ErrorDocument(self):  # pragma: no cover
        return ErrorDocument.make_one(self.boto3_raw_data["ErrorDocument"])

    @cached_property
    def IndexDocument(self):  # pragma: no cover
        return IndexDocument.make_one(self.boto3_raw_data["IndexDocument"])

    @cached_property
    def RedirectAllRequestsTo(self):  # pragma: no cover
        return RedirectAllRequestsTo.make_one(
            self.boto3_raw_data["RedirectAllRequestsTo"]
        )

    @cached_property
    def RoutingRules(self):  # pragma: no cover
        return RoutingRule.make_many(self.boto3_raw_data["RoutingRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebsiteConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebsiteConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfigurationOutput:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return ServerSideEncryptionRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfiguration:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return ServerSideEncryptionRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectObjectContentEventStream:
    boto3_raw_data: "type_defs.SelectObjectContentEventStreamTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Records(self):  # pragma: no cover
        return RecordsEvent.make_one(self.boto3_raw_data["Records"])

    @cached_property
    def Stats(self):  # pragma: no cover
        return StatsEvent.make_one(self.boto3_raw_data["Stats"])

    @cached_property
    def Progress(self):  # pragma: no cover
        return ProgressEvent.make_one(self.boto3_raw_data["Progress"])

    Cont = field("Cont")
    End = field("End")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SelectObjectContentEventStreamTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectObjectContentEventStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigurationDeprecated:
    boto3_raw_data: "type_defs.NotificationConfigurationDeprecatedTypeDef" = (
        dataclasses.field()
    )

    TopicConfiguration = field("TopicConfiguration")
    QueueConfiguration = field("QueueConfiguration")
    CloudFunctionConfiguration = field("CloudFunctionConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotificationConfigurationDeprecatedTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationDeprecatedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectsRequestBucketDeleteObjects:
    boto3_raw_data: "type_defs.DeleteObjectsRequestBucketDeleteObjectsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Delete(self):  # pragma: no cover
        return Delete.make_one(self.boto3_raw_data["Delete"])

    MFA = field("MFA")
    RequestPayer = field("RequestPayer")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteObjectsRequestBucketDeleteObjectsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectsRequestBucketDeleteObjectsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectsRequest:
    boto3_raw_data: "type_defs.DeleteObjectsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def Delete(self):  # pragma: no cover
        return Delete.make_one(self.boto3_raw_data["Delete"])

    MFA = field("MFA")
    RequestPayer = field("RequestPayer")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectRetentionRequest:
    boto3_raw_data: "type_defs.PutObjectRetentionRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    Retention = field("Retention")
    RequestPayer = field("RequestPayer")
    VersionId = field("VersionId")
    BypassGovernanceRetention = field("BypassGovernanceRetention")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectRetentionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectRetentionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    Prefix = field("Prefix")
    Status = field("Status")
    Expiration = field("Expiration")
    ID = field("ID")
    Transition = field("Transition")

    @cached_property
    def NoncurrentVersionTransition(self):  # pragma: no cover
        return NoncurrentVersionTransition.make_one(
            self.boto3_raw_data["NoncurrentVersionTransition"]
        )

    @cached_property
    def NoncurrentVersionExpiration(self):  # pragma: no cover
        return NoncurrentVersionExpiration.make_one(
            self.boto3_raw_data["NoncurrentVersionExpiration"]
        )

    @cached_property
    def AbortIncompleteMultipartUpload(self):  # pragma: no cover
        return AbortIncompleteMultipartUpload.make_one(
            self.boto3_raw_data["AbortIncompleteMultipartUpload"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntelligentTieringConfigurationOutput:
    boto3_raw_data: "type_defs.IntelligentTieringConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Status = field("Status")

    @cached_property
    def Tierings(self):  # pragma: no cover
        return Tiering.make_many(self.boto3_raw_data["Tierings"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return IntelligentTieringFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IntelligentTieringConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntelligentTieringConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntelligentTieringConfiguration:
    boto3_raw_data: "type_defs.IntelligentTieringConfigurationTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Status = field("Status")

    @cached_property
    def Tierings(self):  # pragma: no cover
        return Tiering.make_many(self.boto3_raw_data["Tierings"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return IntelligentTieringFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntelligentTieringConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntelligentTieringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleOutput:
    boto3_raw_data: "type_defs.LifecycleRuleOutputTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Expiration(self):  # pragma: no cover
        return LifecycleExpirationOutput.make_one(self.boto3_raw_data["Expiration"])

    ID = field("ID")
    Prefix = field("Prefix")

    @cached_property
    def Filter(self):  # pragma: no cover
        return LifecycleRuleFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def Transitions(self):  # pragma: no cover
        return TransitionOutput.make_many(self.boto3_raw_data["Transitions"])

    @cached_property
    def NoncurrentVersionTransitions(self):  # pragma: no cover
        return NoncurrentVersionTransition.make_many(
            self.boto3_raw_data["NoncurrentVersionTransitions"]
        )

    @cached_property
    def NoncurrentVersionExpiration(self):  # pragma: no cover
        return NoncurrentVersionExpiration.make_one(
            self.boto3_raw_data["NoncurrentVersionExpiration"]
        )

    @cached_property
    def AbortIncompleteMultipartUpload(self):  # pragma: no cover
        return AbortIncompleteMultipartUpload.make_one(
            self.boto3_raw_data["AbortIncompleteMultipartUpload"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleFilter:
    boto3_raw_data: "type_defs.LifecycleRuleFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return Tag.make_one(self.boto3_raw_data["Tag"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")
    And = field("And")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsConfigurationOutput:
    boto3_raw_data: "type_defs.MetricsConfigurationOutputTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Filter(self):  # pragma: no cover
        return MetricsFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsConfiguration:
    boto3_raw_data: "type_defs.MetricsConfigurationTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Filter(self):  # pragma: no cover
        return MetricsFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageClassAnalysis:
    boto3_raw_data: "type_defs.StorageClassAnalysisTypeDef" = dataclasses.field()

    @cached_property
    def DataExport(self):  # pragma: no cover
        return StorageClassAnalysisDataExport.make_one(
            self.boto3_raw_data["DataExport"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageClassAnalysisTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageClassAnalysisTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketCorsRequestBucketCorsPut:
    boto3_raw_data: "type_defs.PutBucketCorsRequestBucketCorsPutTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CORSConfiguration(self):  # pragma: no cover
        return CORSConfiguration.make_one(self.boto3_raw_data["CORSConfiguration"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketCorsRequestBucketCorsPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketCorsRequestBucketCorsPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketCorsRequest:
    boto3_raw_data: "type_defs.PutBucketCorsRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def CORSConfiguration(self):  # pragma: no cover
        return CORSConfiguration.make_one(self.boto3_raw_data["CORSConfiguration"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketCorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketCorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectLockConfigurationOutput:
    boto3_raw_data: "type_defs.GetObjectLockConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObjectLockConfiguration(self):  # pragma: no cover
        return ObjectLockConfiguration.make_one(
            self.boto3_raw_data["ObjectLockConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetObjectLockConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectLockConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectLockConfigurationRequest:
    boto3_raw_data: "type_defs.PutObjectLockConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def ObjectLockConfiguration(self):  # pragma: no cover
        return ObjectLockConfiguration.make_one(
            self.boto3_raw_data["ObjectLockConfiguration"]
        )

    RequestPayer = field("RequestPayer")
    Token = field("Token")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutObjectLockConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectLockConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionConfigurationOutput:
    boto3_raw_data: "type_defs.LambdaFunctionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    LambdaFunctionArn = field("LambdaFunctionArn")
    Events = field("Events")
    Id = field("Id")

    @cached_property
    def Filter(self):  # pragma: no cover
        return NotificationConfigurationFilterOutput.make_one(
            self.boto3_raw_data["Filter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueConfigurationOutput:
    boto3_raw_data: "type_defs.QueueConfigurationOutputTypeDef" = dataclasses.field()

    QueueArn = field("QueueArn")
    Events = field("Events")
    Id = field("Id")

    @cached_property
    def Filter(self):  # pragma: no cover
        return NotificationConfigurationFilterOutput.make_one(
            self.boto3_raw_data["Filter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicConfigurationOutput:
    boto3_raw_data: "type_defs.TopicConfigurationOutputTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")
    Events = field("Events")
    Id = field("Id")

    @cached_property
    def Filter(self):  # pragma: no cover
        return NotificationConfigurationFilterOutput.make_one(
            self.boto3_raw_data["Filter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigurationFilter:
    boto3_raw_data: "type_defs.NotificationConfigurationFilterTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NotificationConfigurationFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketAclRequestBucketAclPut:
    boto3_raw_data: "type_defs.PutBucketAclRequestBucketAclPutTypeDef" = (
        dataclasses.field()
    )

    ACL = field("ACL")

    @cached_property
    def AccessControlPolicy(self):  # pragma: no cover
        return AccessControlPolicy.make_one(self.boto3_raw_data["AccessControlPolicy"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutBucketAclRequestBucketAclPutTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketAclRequestBucketAclPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketAclRequest:
    boto3_raw_data: "type_defs.PutBucketAclRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ACL = field("ACL")

    @cached_property
    def AccessControlPolicy(self):  # pragma: no cover
        return AccessControlPolicy.make_one(self.boto3_raw_data["AccessControlPolicy"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketAclRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketAclRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectAclRequestObjectAclPut:
    boto3_raw_data: "type_defs.PutObjectAclRequestObjectAclPutTypeDef" = (
        dataclasses.field()
    )

    ACL = field("ACL")

    @cached_property
    def AccessControlPolicy(self):  # pragma: no cover
        return AccessControlPolicy.make_one(self.boto3_raw_data["AccessControlPolicy"])

    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    RequestPayer = field("RequestPayer")
    VersionId = field("VersionId")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutObjectAclRequestObjectAclPutTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectAclRequestObjectAclPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutObjectAclRequest:
    boto3_raw_data: "type_defs.PutObjectAclRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    ACL = field("ACL")

    @cached_property
    def AccessControlPolicy(self):  # pragma: no cover
        return AccessControlPolicy.make_one(self.boto3_raw_data["AccessControlPolicy"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    RequestPayer = field("RequestPayer")
    VersionId = field("VersionId")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutObjectAclRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutObjectAclRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLocation:
    boto3_raw_data: "type_defs.OutputLocationTypeDef" = dataclasses.field()

    @cached_property
    def S3(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryDestinationOutput:
    boto3_raw_data: "type_defs.InventoryDestinationOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3BucketDestination(self):  # pragma: no cover
        return InventoryS3BucketDestinationOutput.make_one(
            self.boto3_raw_data["S3BucketDestination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryDestinationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryDestination:
    boto3_raw_data: "type_defs.InventoryDestinationTypeDef" = dataclasses.field()

    @cached_property
    def S3BucketDestination(self):  # pragma: no cover
        return InventoryS3BucketDestination.make_one(
            self.boto3_raw_data["S3BucketDestination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetadataConfigurationResult:
    boto3_raw_data: "type_defs.GetBucketMetadataConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetadataConfigurationResult(self):  # pragma: no cover
        return MetadataConfigurationResult.make_one(
            self.boto3_raw_data["MetadataConfigurationResult"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetadataConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetadataConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketMetadataConfigurationRequest:
    boto3_raw_data: "type_defs.CreateBucketMetadataConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def MetadataConfiguration(self):  # pragma: no cover
        return MetadataConfiguration.make_one(
            self.boto3_raw_data["MetadataConfiguration"]
        )

    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBucketMetadataConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketMetadataConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetadataTableConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketMetadataTableConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GetBucketMetadataTableConfigurationResult(self):  # pragma: no cover
        return GetBucketMetadataTableConfigurationResult.make_one(
            self.boto3_raw_data["GetBucketMetadataTableConfigurationResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetadataTableConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetadataTableConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleOutput:
    boto3_raw_data: "type_defs.ReplicationRuleOutputTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    ID = field("ID")
    Priority = field("Priority")
    Prefix = field("Prefix")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ReplicationRuleFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def SourceSelectionCriteria(self):  # pragma: no cover
        return SourceSelectionCriteria.make_one(
            self.boto3_raw_data["SourceSelectionCriteria"]
        )

    @cached_property
    def ExistingObjectReplication(self):  # pragma: no cover
        return ExistingObjectReplication.make_one(
            self.boto3_raw_data["ExistingObjectReplication"]
        )

    @cached_property
    def DeleteMarkerReplication(self):  # pragma: no cover
        return DeleteMarkerReplication.make_one(
            self.boto3_raw_data["DeleteMarkerReplication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRule:
    boto3_raw_data: "type_defs.ReplicationRuleTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    ID = field("ID")
    Priority = field("Priority")
    Prefix = field("Prefix")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ReplicationRuleFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def SourceSelectionCriteria(self):  # pragma: no cover
        return SourceSelectionCriteria.make_one(
            self.boto3_raw_data["SourceSelectionCriteria"]
        )

    @cached_property
    def ExistingObjectReplication(self):  # pragma: no cover
        return ExistingObjectReplication.make_one(
            self.boto3_raw_data["ExistingObjectReplication"]
        )

    @cached_property
    def DeleteMarkerReplication(self):  # pragma: no cover
        return DeleteMarkerReplication.make_one(
            self.boto3_raw_data["DeleteMarkerReplication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketOwnershipControlsRequest:
    boto3_raw_data: "type_defs.PutBucketOwnershipControlsRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    OwnershipControls = field("OwnershipControls")
    ContentMD5 = field("ContentMD5")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketOwnershipControlsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketOwnershipControlsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLoggingOutput:
    boto3_raw_data: "type_defs.GetBucketLoggingOutputTypeDef" = dataclasses.field()

    @cached_property
    def LoggingEnabled(self):  # pragma: no cover
        return LoggingEnabledOutput.make_one(self.boto3_raw_data["LoggingEnabled"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketLoggingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLoggingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingEnabled:
    boto3_raw_data: "type_defs.LoggingEnabledTypeDef" = dataclasses.field()

    TargetBucket = field("TargetBucket")
    TargetPrefix = field("TargetPrefix")

    @cached_property
    def TargetGrants(self):  # pragma: no cover
        return TargetGrant.make_many(self.boto3_raw_data["TargetGrants"])

    TargetObjectKeyFormat = field("TargetObjectKeyFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingEnabledTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingEnabledTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketWebsiteRequestBucketWebsitePut:
    boto3_raw_data: "type_defs.PutBucketWebsiteRequestBucketWebsitePutTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WebsiteConfiguration(self):  # pragma: no cover
        return WebsiteConfiguration.make_one(
            self.boto3_raw_data["WebsiteConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketWebsiteRequestBucketWebsitePutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketWebsiteRequestBucketWebsitePutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketWebsiteRequest:
    boto3_raw_data: "type_defs.PutBucketWebsiteRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def WebsiteConfiguration(self):  # pragma: no cover
        return WebsiteConfiguration.make_one(
            self.boto3_raw_data["WebsiteConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketWebsiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketWebsiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketEncryptionOutput:
    boto3_raw_data: "type_defs.GetBucketEncryptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfigurationOutput.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketEncryptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectObjectContentOutput:
    boto3_raw_data: "type_defs.SelectObjectContentOutputTypeDef" = dataclasses.field()

    Payload = field("Payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectObjectContentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectObjectContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketNotificationRequest:
    boto3_raw_data: "type_defs.PutBucketNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfigurationDeprecated.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketNotificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketIntelligentTieringConfigurationOutput:
    boto3_raw_data: (
        "type_defs.GetBucketIntelligentTieringConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def IntelligentTieringConfiguration(self):  # pragma: no cover
        return IntelligentTieringConfigurationOutput.make_one(
            self.boto3_raw_data["IntelligentTieringConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketIntelligentTieringConfigurationOutputTypeDef"
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
                "type_defs.GetBucketIntelligentTieringConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketIntelligentTieringConfigurationsOutput:
    boto3_raw_data: (
        "type_defs.ListBucketIntelligentTieringConfigurationsOutputTypeDef"
    ) = dataclasses.field()

    IsTruncated = field("IsTruncated")
    ContinuationToken = field("ContinuationToken")
    NextContinuationToken = field("NextContinuationToken")

    @cached_property
    def IntelligentTieringConfigurationList(self):  # pragma: no cover
        return IntelligentTieringConfigurationOutput.make_many(
            self.boto3_raw_data["IntelligentTieringConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketIntelligentTieringConfigurationsOutputTypeDef"
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
                "type_defs.ListBucketIntelligentTieringConfigurationsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLifecycleConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketLifecycleConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return LifecycleRuleOutput.make_many(self.boto3_raw_data["Rules"])

    TransitionDefaultMinimumObjectSize = field("TransitionDefaultMinimumObjectSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketLifecycleConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLifecycleConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetricsConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketMetricsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MetricsConfiguration(self):  # pragma: no cover
        return MetricsConfigurationOutput.make_one(
            self.boto3_raw_data["MetricsConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetricsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetricsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketMetricsConfigurationsOutput:
    boto3_raw_data: "type_defs.ListBucketMetricsConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    IsTruncated = field("IsTruncated")
    ContinuationToken = field("ContinuationToken")
    NextContinuationToken = field("NextContinuationToken")

    @cached_property
    def MetricsConfigurationList(self):  # pragma: no cover
        return MetricsConfigurationOutput.make_many(
            self.boto3_raw_data["MetricsConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketMetricsConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketMetricsConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsConfigurationOutput:
    boto3_raw_data: "type_defs.AnalyticsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def StorageClassAnalysis(self):  # pragma: no cover
        return StorageClassAnalysis.make_one(
            self.boto3_raw_data["StorageClassAnalysis"]
        )

    @cached_property
    def Filter(self):  # pragma: no cover
        return AnalyticsFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsConfiguration:
    boto3_raw_data: "type_defs.AnalyticsConfigurationTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def StorageClassAnalysis(self):  # pragma: no cover
        return StorageClassAnalysis.make_one(
            self.boto3_raw_data["StorageClassAnalysis"]
        )

    @cached_property
    def Filter(self):  # pragma: no cover
        return AnalyticsFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigurationResponse:
    boto3_raw_data: "type_defs.NotificationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TopicConfigurations(self):  # pragma: no cover
        return TopicConfigurationOutput.make_many(
            self.boto3_raw_data["TopicConfigurations"]
        )

    @cached_property
    def QueueConfigurations(self):  # pragma: no cover
        return QueueConfigurationOutput.make_many(
            self.boto3_raw_data["QueueConfigurations"]
        )

    @cached_property
    def LambdaFunctionConfigurations(self):  # pragma: no cover
        return LambdaFunctionConfigurationOutput.make_many(
            self.boto3_raw_data["LambdaFunctionConfigurations"]
        )

    EventBridgeConfiguration = field("EventBridgeConfiguration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotificationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreRequest:
    boto3_raw_data: "type_defs.RestoreRequestTypeDef" = dataclasses.field()

    Days = field("Days")

    @cached_property
    def GlacierJobParameters(self):  # pragma: no cover
        return GlacierJobParameters.make_one(
            self.boto3_raw_data["GlacierJobParameters"]
        )

    Type = field("Type")
    Tier = field("Tier")
    Description = field("Description")

    @cached_property
    def SelectParameters(self):  # pragma: no cover
        return SelectParameters.make_one(self.boto3_raw_data["SelectParameters"])

    @cached_property
    def OutputLocation(self):  # pragma: no cover
        return OutputLocation.make_one(self.boto3_raw_data["OutputLocation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestoreRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestoreRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryConfigurationOutput:
    boto3_raw_data: "type_defs.InventoryConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Destination(self):  # pragma: no cover
        return InventoryDestinationOutput.make_one(self.boto3_raw_data["Destination"])

    IsEnabled = field("IsEnabled")
    Id = field("Id")
    IncludedObjectVersions = field("IncludedObjectVersions")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return InventorySchedule.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return InventoryFilter.make_one(self.boto3_raw_data["Filter"])

    OptionalFields = field("OptionalFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryConfiguration:
    boto3_raw_data: "type_defs.InventoryConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Destination(self):  # pragma: no cover
        return InventoryDestination.make_one(self.boto3_raw_data["Destination"])

    IsEnabled = field("IsEnabled")
    Id = field("Id")
    IncludedObjectVersions = field("IncludedObjectVersions")

    @cached_property
    def Schedule(self):  # pragma: no cover
        return InventorySchedule.make_one(self.boto3_raw_data["Schedule"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return InventoryFilter.make_one(self.boto3_raw_data["Filter"])

    OptionalFields = field("OptionalFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InventoryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InventoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketMetadataConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketMetadataConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GetBucketMetadataConfigurationResult(self):  # pragma: no cover
        return GetBucketMetadataConfigurationResult.make_one(
            self.boto3_raw_data["GetBucketMetadataConfigurationResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketMetadataConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketMetadataConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationOutput:
    boto3_raw_data: "type_defs.ReplicationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Role = field("Role")

    @cached_property
    def Rules(self):  # pragma: no cover
        return ReplicationRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfiguration:
    boto3_raw_data: "type_defs.ReplicationConfigurationTypeDef" = dataclasses.field()

    Role = field("Role")

    @cached_property
    def Rules(self):  # pragma: no cover
        return ReplicationRule.make_many(self.boto3_raw_data["Rules"])

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
class PutBucketEncryptionRequest:
    boto3_raw_data: "type_defs.PutBucketEncryptionRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ServerSideEncryptionConfiguration = field("ServerSideEncryptionConfiguration")
    ContentMD5 = field("ContentMD5")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketEncryptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketEncryptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleConfiguration:
    boto3_raw_data: "type_defs.LifecycleConfigurationTypeDef" = dataclasses.field()

    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketIntelligentTieringConfigurationRequest:
    boto3_raw_data: (
        "type_defs.PutBucketIntelligentTieringConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Bucket = field("Bucket")
    Id = field("Id")
    IntelligentTieringConfiguration = field("IntelligentTieringConfiguration")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketIntelligentTieringConfigurationRequestTypeDef"
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
                "type_defs.PutBucketIntelligentTieringConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRule:
    boto3_raw_data: "type_defs.LifecycleRuleTypeDef" = dataclasses.field()

    Status = field("Status")
    Expiration = field("Expiration")
    ID = field("ID")
    Prefix = field("Prefix")
    Filter = field("Filter")
    Transitions = field("Transitions")

    @cached_property
    def NoncurrentVersionTransitions(self):  # pragma: no cover
        return NoncurrentVersionTransition.make_many(
            self.boto3_raw_data["NoncurrentVersionTransitions"]
        )

    @cached_property
    def NoncurrentVersionExpiration(self):  # pragma: no cover
        return NoncurrentVersionExpiration.make_one(
            self.boto3_raw_data["NoncurrentVersionExpiration"]
        )

    @cached_property
    def AbortIncompleteMultipartUpload(self):  # pragma: no cover
        return AbortIncompleteMultipartUpload.make_one(
            self.boto3_raw_data["AbortIncompleteMultipartUpload"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecycleRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketMetricsConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketMetricsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    MetricsConfiguration = field("MetricsConfiguration")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketMetricsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketMetricsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketAnalyticsConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketAnalyticsConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalyticsConfiguration(self):  # pragma: no cover
        return AnalyticsConfigurationOutput.make_one(
            self.boto3_raw_data["AnalyticsConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketAnalyticsConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketAnalyticsConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketAnalyticsConfigurationsOutput:
    boto3_raw_data: "type_defs.ListBucketAnalyticsConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    IsTruncated = field("IsTruncated")
    ContinuationToken = field("ContinuationToken")
    NextContinuationToken = field("NextContinuationToken")

    @cached_property
    def AnalyticsConfigurationList(self):  # pragma: no cover
        return AnalyticsConfigurationOutput.make_many(
            self.boto3_raw_data["AnalyticsConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketAnalyticsConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketAnalyticsConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionConfiguration:
    boto3_raw_data: "type_defs.LambdaFunctionConfigurationTypeDef" = dataclasses.field()

    LambdaFunctionArn = field("LambdaFunctionArn")
    Events = field("Events")
    Id = field("Id")
    Filter = field("Filter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueueConfiguration:
    boto3_raw_data: "type_defs.QueueConfigurationTypeDef" = dataclasses.field()

    QueueArn = field("QueueArn")
    Events = field("Events")
    Id = field("Id")
    Filter = field("Filter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueueConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueueConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicConfiguration:
    boto3_raw_data: "type_defs.TopicConfigurationTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")
    Events = field("Events")
    Id = field("Id")
    Filter = field("Filter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreObjectRequestObjectRestoreObject:
    boto3_raw_data: "type_defs.RestoreObjectRequestObjectRestoreObjectTypeDef" = (
        dataclasses.field()
    )

    VersionId = field("VersionId")

    @cached_property
    def RestoreRequest(self):  # pragma: no cover
        return RestoreRequest.make_one(self.boto3_raw_data["RestoreRequest"])

    RequestPayer = field("RequestPayer")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreObjectRequestObjectRestoreObjectTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreObjectRequestObjectRestoreObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreObjectRequestObjectSummaryRestoreObject:
    boto3_raw_data: (
        "type_defs.RestoreObjectRequestObjectSummaryRestoreObjectTypeDef"
    ) = dataclasses.field()

    VersionId = field("VersionId")

    @cached_property
    def RestoreRequest(self):  # pragma: no cover
        return RestoreRequest.make_one(self.boto3_raw_data["RestoreRequest"])

    RequestPayer = field("RequestPayer")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RestoreObjectRequestObjectSummaryRestoreObjectTypeDef"
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
                "type_defs.RestoreObjectRequestObjectSummaryRestoreObjectTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreObjectRequest:
    boto3_raw_data: "type_defs.RestoreObjectRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Key = field("Key")
    VersionId = field("VersionId")

    @cached_property
    def RestoreRequest(self):  # pragma: no cover
        return RestoreRequest.make_one(self.boto3_raw_data["RestoreRequest"])

    RequestPayer = field("RequestPayer")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketInventoryConfigurationOutput:
    boto3_raw_data: "type_defs.GetBucketInventoryConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InventoryConfiguration(self):  # pragma: no cover
        return InventoryConfigurationOutput.make_one(
            self.boto3_raw_data["InventoryConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketInventoryConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketInventoryConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBucketInventoryConfigurationsOutput:
    boto3_raw_data: "type_defs.ListBucketInventoryConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    ContinuationToken = field("ContinuationToken")

    @cached_property
    def InventoryConfigurationList(self):  # pragma: no cover
        return InventoryConfigurationOutput.make_many(
            self.boto3_raw_data["InventoryConfigurationList"]
        )

    IsTruncated = field("IsTruncated")
    NextContinuationToken = field("NextContinuationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBucketInventoryConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBucketInventoryConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketReplicationOutput:
    boto3_raw_data: "type_defs.GetBucketReplicationOutputTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationConfiguration(self):  # pragma: no cover
        return ReplicationConfigurationOutput.make_one(
            self.boto3_raw_data["ReplicationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketReplicationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketReplicationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketLoggingStatus:
    boto3_raw_data: "type_defs.BucketLoggingStatusTypeDef" = dataclasses.field()

    LoggingEnabled = field("LoggingEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketLoggingStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketLoggingStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLifecycleRequestBucketLifecyclePut:
    boto3_raw_data: "type_defs.PutBucketLifecycleRequestBucketLifecyclePutTypeDef" = (
        dataclasses.field()
    )

    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @cached_property
    def LifecycleConfiguration(self):  # pragma: no cover
        return LifecycleConfiguration.make_one(
            self.boto3_raw_data["LifecycleConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketLifecycleRequestBucketLifecyclePutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLifecycleRequestBucketLifecyclePutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLifecycleRequest:
    boto3_raw_data: "type_defs.PutBucketLifecycleRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @cached_property
    def LifecycleConfiguration(self):  # pragma: no cover
        return LifecycleConfiguration.make_one(
            self.boto3_raw_data["LifecycleConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketLifecycleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLifecycleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketAnalyticsConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketAnalyticsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    AnalyticsConfiguration = field("AnalyticsConfiguration")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketAnalyticsConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketAnalyticsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketInventoryConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketInventoryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    Id = field("Id")
    InventoryConfiguration = field("InventoryConfiguration")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketInventoryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketInventoryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketReplicationRequest:
    boto3_raw_data: "type_defs.PutBucketReplicationRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ReplicationConfiguration = field("ReplicationConfiguration")
    ChecksumAlgorithm = field("ChecksumAlgorithm")
    Token = field("Token")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLoggingRequestBucketLoggingPut:
    boto3_raw_data: "type_defs.PutBucketLoggingRequestBucketLoggingPutTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BucketLoggingStatus(self):  # pragma: no cover
        return BucketLoggingStatus.make_one(self.boto3_raw_data["BucketLoggingStatus"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketLoggingRequestBucketLoggingPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLoggingRequestBucketLoggingPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLoggingRequest:
    boto3_raw_data: "type_defs.PutBucketLoggingRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")

    @cached_property
    def BucketLoggingStatus(self):  # pragma: no cover
        return BucketLoggingStatus.make_one(self.boto3_raw_data["BucketLoggingStatus"])

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketLoggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLoggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketLifecycleConfiguration:
    boto3_raw_data: "type_defs.BucketLifecycleConfigurationTypeDef" = (
        dataclasses.field()
    )

    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketLifecycleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketLifecycleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    TopicConfigurations = field("TopicConfigurations")
    QueueConfigurations = field("QueueConfigurations")
    LambdaFunctionConfigurations = field("LambdaFunctionConfigurations")
    EventBridgeConfiguration = field("EventBridgeConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPut:
    boto3_raw_data: "type_defs.PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef" = (dataclasses.field())

    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @cached_property
    def LifecycleConfiguration(self):  # pragma: no cover
        return BucketLifecycleConfiguration.make_one(
            self.boto3_raw_data["LifecycleConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")
    TransitionDefaultMinimumObjectSize = field("TransitionDefaultMinimumObjectSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef"
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
                "type_defs.PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @cached_property
    def LifecycleConfiguration(self):  # pragma: no cover
        return BucketLifecycleConfiguration.make_one(
            self.boto3_raw_data["LifecycleConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")
    TransitionDefaultMinimumObjectSize = field("TransitionDefaultMinimumObjectSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketLifecycleConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketNotificationConfigurationRequestBucketNotificationPut:
    boto3_raw_data: "type_defs.PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef" = (dataclasses.field())

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")
    SkipDestinationValidation = field("SkipDestinationValidation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef"
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
                "type_defs.PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    ExpectedBucketOwner = field("ExpectedBucketOwner")
    SkipDestinationValidation = field("SkipDestinationValidation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
