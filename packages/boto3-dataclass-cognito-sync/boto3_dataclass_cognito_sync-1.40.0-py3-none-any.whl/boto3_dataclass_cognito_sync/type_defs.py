# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cognito_sync import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BulkPublishRequest:
    boto3_raw_data: "type_defs.BulkPublishRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkPublishRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkPublishRequestTypeDef"]
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
class CognitoStreams:
    boto3_raw_data: "type_defs.CognitoStreamsTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    RoleArn = field("RoleArn")
    StreamingStatus = field("StreamingStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CognitoStreamsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CognitoStreamsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dataset:
    boto3_raw_data: "type_defs.DatasetTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedBy = field("LastModifiedBy")
    DataStorage = field("DataStorage")
    NumRecords = field("NumRecords")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityPoolUsageRequest:
    boto3_raw_data: "type_defs.DescribeIdentityPoolUsageRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeIdentityPoolUsageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityPoolUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityPoolUsage:
    boto3_raw_data: "type_defs.IdentityPoolUsageTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    SyncSessionsCount = field("SyncSessionsCount")
    DataStorage = field("DataStorage")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityPoolUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityPoolUsageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityUsageRequest:
    boto3_raw_data: "type_defs.DescribeIdentityUsageRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIdentityUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityUsage:
    boto3_raw_data: "type_defs.IdentityUsageTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    IdentityPoolId = field("IdentityPoolId")
    LastModifiedDate = field("LastModifiedDate")
    DatasetCount = field("DatasetCount")
    DataStorage = field("DataStorage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityUsageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBulkPublishDetailsRequest:
    boto3_raw_data: "type_defs.GetBulkPublishDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBulkPublishDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBulkPublishDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCognitoEventsRequest:
    boto3_raw_data: "type_defs.GetCognitoEventsRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCognitoEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCognitoEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityPoolConfigurationRequest:
    boto3_raw_data: "type_defs.GetIdentityPoolConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityPoolConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityPoolConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PushSyncOutput:
    boto3_raw_data: "type_defs.PushSyncOutputTypeDef" = dataclasses.field()

    ApplicationArns = field("ApplicationArns")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PushSyncOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PushSyncOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityPoolUsageRequest:
    boto3_raw_data: "type_defs.ListIdentityPoolUsageRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityPoolUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoolUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecordsRequest:
    boto3_raw_data: "type_defs.ListRecordsRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")
    LastSyncCount = field("LastSyncCount")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    SyncSessionToken = field("SyncSessionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecordsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecordsRequestTypeDef"]
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

    Key = field("Key")
    Value = field("Value")
    SyncCount = field("SyncCount")
    LastModifiedDate = field("LastModifiedDate")
    LastModifiedBy = field("LastModifiedBy")
    DeviceLastModifiedDate = field("DeviceLastModifiedDate")

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
class PushSync:
    boto3_raw_data: "type_defs.PushSyncTypeDef" = dataclasses.field()

    ApplicationArns = field("ApplicationArns")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PushSyncTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PushSyncTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDeviceRequest:
    boto3_raw_data: "type_defs.RegisterDeviceRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    Platform = field("Platform")
    Token = field("Token")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetCognitoEventsRequest:
    boto3_raw_data: "type_defs.SetCognitoEventsRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    Events = field("Events")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetCognitoEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetCognitoEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribeToDatasetRequest:
    boto3_raw_data: "type_defs.SubscribeToDatasetRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")
    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribeToDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribeToDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsubscribeFromDatasetRequest:
    boto3_raw_data: "type_defs.UnsubscribeFromDatasetRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")
    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UnsubscribeFromDatasetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnsubscribeFromDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BulkPublishResponse:
    boto3_raw_data: "type_defs.BulkPublishResponseTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BulkPublishResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BulkPublishResponseTypeDef"]
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
class GetBulkPublishDetailsResponse:
    boto3_raw_data: "type_defs.GetBulkPublishDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    BulkPublishStartTime = field("BulkPublishStartTime")
    BulkPublishCompleteTime = field("BulkPublishCompleteTime")
    BulkPublishStatus = field("BulkPublishStatus")
    FailureMessage = field("FailureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBulkPublishDetailsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBulkPublishDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCognitoEventsResponse:
    boto3_raw_data: "type_defs.GetCognitoEventsResponseTypeDef" = dataclasses.field()

    Events = field("Events")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCognitoEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCognitoEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDeviceResponse:
    boto3_raw_data: "type_defs.RegisterDeviceResponseTypeDef" = dataclasses.field()

    DeviceId = field("DeviceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetResponse:
    boto3_raw_data: "type_defs.DeleteDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Dataset(self):  # pragma: no cover
        return Dataset.make_one(self.boto3_raw_data["Dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Dataset(self):  # pragma: no cover
        return Dataset.make_one(self.boto3_raw_data["Dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Datasets(self):  # pragma: no cover
        return Dataset.make_many(self.boto3_raw_data["Datasets"])

    Count = field("Count")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityPoolUsageResponse:
    boto3_raw_data: "type_defs.DescribeIdentityPoolUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityPoolUsage(self):  # pragma: no cover
        return IdentityPoolUsage.make_one(self.boto3_raw_data["IdentityPoolUsage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeIdentityPoolUsageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityPoolUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityPoolUsageResponse:
    boto3_raw_data: "type_defs.ListIdentityPoolUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityPoolUsages(self):  # pragma: no cover
        return IdentityPoolUsage.make_many(self.boto3_raw_data["IdentityPoolUsages"])

    MaxResults = field("MaxResults")
    Count = field("Count")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentityPoolUsageResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoolUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityUsageResponse:
    boto3_raw_data: "type_defs.DescribeIdentityUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityUsage(self):  # pragma: no cover
        return IdentityUsage.make_one(self.boto3_raw_data["IdentityUsage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeIdentityUsageResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityPoolConfigurationResponse:
    boto3_raw_data: "type_defs.GetIdentityPoolConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")

    @cached_property
    def PushSync(self):  # pragma: no cover
        return PushSyncOutput.make_one(self.boto3_raw_data["PushSync"])

    @cached_property
    def CognitoStreams(self):  # pragma: no cover
        return CognitoStreams.make_one(self.boto3_raw_data["CognitoStreams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIdentityPoolConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityPoolConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityPoolConfigurationResponse:
    boto3_raw_data: "type_defs.SetIdentityPoolConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")

    @cached_property
    def PushSync(self):  # pragma: no cover
        return PushSyncOutput.make_one(self.boto3_raw_data["PushSync"])

    @cached_property
    def CognitoStreams(self):  # pragma: no cover
        return CognitoStreams.make_one(self.boto3_raw_data["CognitoStreams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetIdentityPoolConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityPoolConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecordsResponse:
    boto3_raw_data: "type_defs.ListRecordsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    Count = field("Count")
    DatasetSyncCount = field("DatasetSyncCount")
    LastModifiedBy = field("LastModifiedBy")
    MergedDatasetNames = field("MergedDatasetNames")
    DatasetExists = field("DatasetExists")
    DatasetDeletedAfterRequestedSyncCount = field(
        "DatasetDeletedAfterRequestedSyncCount"
    )
    SyncSessionToken = field("SyncSessionToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecordsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecordsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecordsResponse:
    boto3_raw_data: "type_defs.UpdateRecordsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["Records"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecordsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecordsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordPatch:
    boto3_raw_data: "type_defs.RecordPatchTypeDef" = dataclasses.field()

    Op = field("Op")
    Key = field("Key")
    SyncCount = field("SyncCount")
    Value = field("Value")
    DeviceLastModifiedDate = field("DeviceLastModifiedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordPatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordPatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityPoolConfigurationRequest:
    boto3_raw_data: "type_defs.SetIdentityPoolConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    PushSync = field("PushSync")

    @cached_property
    def CognitoStreams(self):  # pragma: no cover
        return CognitoStreams.make_one(self.boto3_raw_data["CognitoStreams"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetIdentityPoolConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityPoolConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecordsRequest:
    boto3_raw_data: "type_defs.UpdateRecordsRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DatasetName = field("DatasetName")
    SyncSessionToken = field("SyncSessionToken")
    DeviceId = field("DeviceId")

    @cached_property
    def RecordPatches(self):  # pragma: no cover
        return RecordPatch.make_many(self.boto3_raw_data["RecordPatches"])

    ClientContext = field("ClientContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecordsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
