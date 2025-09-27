# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cognito_sync import type_defs as bs_td


class COGNITO_SYNCCaster:

    def bulk_publish(
        self,
        res: "bs_td.BulkPublishResponseTypeDef",
    ) -> "dc_td.BulkPublishResponse":
        return dc_td.BulkPublishResponse.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.DeleteDatasetResponseTypeDef",
    ) -> "dc_td.DeleteDatasetResponse":
        return dc_td.DeleteDatasetResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_identity_pool_usage(
        self,
        res: "bs_td.DescribeIdentityPoolUsageResponseTypeDef",
    ) -> "dc_td.DescribeIdentityPoolUsageResponse":
        return dc_td.DescribeIdentityPoolUsageResponse.make_one(res)

    def describe_identity_usage(
        self,
        res: "bs_td.DescribeIdentityUsageResponseTypeDef",
    ) -> "dc_td.DescribeIdentityUsageResponse":
        return dc_td.DescribeIdentityUsageResponse.make_one(res)

    def get_bulk_publish_details(
        self,
        res: "bs_td.GetBulkPublishDetailsResponseTypeDef",
    ) -> "dc_td.GetBulkPublishDetailsResponse":
        return dc_td.GetBulkPublishDetailsResponse.make_one(res)

    def get_cognito_events(
        self,
        res: "bs_td.GetCognitoEventsResponseTypeDef",
    ) -> "dc_td.GetCognitoEventsResponse":
        return dc_td.GetCognitoEventsResponse.make_one(res)

    def get_identity_pool_configuration(
        self,
        res: "bs_td.GetIdentityPoolConfigurationResponseTypeDef",
    ) -> "dc_td.GetIdentityPoolConfigurationResponse":
        return dc_td.GetIdentityPoolConfigurationResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_identity_pool_usage(
        self,
        res: "bs_td.ListIdentityPoolUsageResponseTypeDef",
    ) -> "dc_td.ListIdentityPoolUsageResponse":
        return dc_td.ListIdentityPoolUsageResponse.make_one(res)

    def list_records(
        self,
        res: "bs_td.ListRecordsResponseTypeDef",
    ) -> "dc_td.ListRecordsResponse":
        return dc_td.ListRecordsResponse.make_one(res)

    def register_device(
        self,
        res: "bs_td.RegisterDeviceResponseTypeDef",
    ) -> "dc_td.RegisterDeviceResponse":
        return dc_td.RegisterDeviceResponse.make_one(res)

    def set_cognito_events(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_identity_pool_configuration(
        self,
        res: "bs_td.SetIdentityPoolConfigurationResponseTypeDef",
    ) -> "dc_td.SetIdentityPoolConfigurationResponse":
        return dc_td.SetIdentityPoolConfigurationResponse.make_one(res)

    def update_records(
        self,
        res: "bs_td.UpdateRecordsResponseTypeDef",
    ) -> "dc_td.UpdateRecordsResponse":
        return dc_td.UpdateRecordsResponse.make_one(res)


cognito_sync_caster = COGNITO_SYNCCaster()
