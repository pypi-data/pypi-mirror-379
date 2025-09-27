# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appfabric import type_defs as bs_td


class APPFABRICCaster:

    def batch_get_user_access_tasks(
        self,
        res: "bs_td.BatchGetUserAccessTasksResponseTypeDef",
    ) -> "dc_td.BatchGetUserAccessTasksResponse":
        return dc_td.BatchGetUserAccessTasksResponse.make_one(res)

    def connect_app_authorization(
        self,
        res: "bs_td.ConnectAppAuthorizationResponseTypeDef",
    ) -> "dc_td.ConnectAppAuthorizationResponse":
        return dc_td.ConnectAppAuthorizationResponse.make_one(res)

    def create_app_authorization(
        self,
        res: "bs_td.CreateAppAuthorizationResponseTypeDef",
    ) -> "dc_td.CreateAppAuthorizationResponse":
        return dc_td.CreateAppAuthorizationResponse.make_one(res)

    def create_app_bundle(
        self,
        res: "bs_td.CreateAppBundleResponseTypeDef",
    ) -> "dc_td.CreateAppBundleResponse":
        return dc_td.CreateAppBundleResponse.make_one(res)

    def create_ingestion(
        self,
        res: "bs_td.CreateIngestionResponseTypeDef",
    ) -> "dc_td.CreateIngestionResponse":
        return dc_td.CreateIngestionResponse.make_one(res)

    def create_ingestion_destination(
        self,
        res: "bs_td.CreateIngestionDestinationResponseTypeDef",
    ) -> "dc_td.CreateIngestionDestinationResponse":
        return dc_td.CreateIngestionDestinationResponse.make_one(res)

    def get_app_authorization(
        self,
        res: "bs_td.GetAppAuthorizationResponseTypeDef",
    ) -> "dc_td.GetAppAuthorizationResponse":
        return dc_td.GetAppAuthorizationResponse.make_one(res)

    def get_app_bundle(
        self,
        res: "bs_td.GetAppBundleResponseTypeDef",
    ) -> "dc_td.GetAppBundleResponse":
        return dc_td.GetAppBundleResponse.make_one(res)

    def get_ingestion(
        self,
        res: "bs_td.GetIngestionResponseTypeDef",
    ) -> "dc_td.GetIngestionResponse":
        return dc_td.GetIngestionResponse.make_one(res)

    def get_ingestion_destination(
        self,
        res: "bs_td.GetIngestionDestinationResponseTypeDef",
    ) -> "dc_td.GetIngestionDestinationResponse":
        return dc_td.GetIngestionDestinationResponse.make_one(res)

    def list_app_authorizations(
        self,
        res: "bs_td.ListAppAuthorizationsResponseTypeDef",
    ) -> "dc_td.ListAppAuthorizationsResponse":
        return dc_td.ListAppAuthorizationsResponse.make_one(res)

    def list_app_bundles(
        self,
        res: "bs_td.ListAppBundlesResponseTypeDef",
    ) -> "dc_td.ListAppBundlesResponse":
        return dc_td.ListAppBundlesResponse.make_one(res)

    def list_ingestion_destinations(
        self,
        res: "bs_td.ListIngestionDestinationsResponseTypeDef",
    ) -> "dc_td.ListIngestionDestinationsResponse":
        return dc_td.ListIngestionDestinationsResponse.make_one(res)

    def list_ingestions(
        self,
        res: "bs_td.ListIngestionsResponseTypeDef",
    ) -> "dc_td.ListIngestionsResponse":
        return dc_td.ListIngestionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_user_access_tasks(
        self,
        res: "bs_td.StartUserAccessTasksResponseTypeDef",
    ) -> "dc_td.StartUserAccessTasksResponse":
        return dc_td.StartUserAccessTasksResponse.make_one(res)

    def update_app_authorization(
        self,
        res: "bs_td.UpdateAppAuthorizationResponseTypeDef",
    ) -> "dc_td.UpdateAppAuthorizationResponse":
        return dc_td.UpdateAppAuthorizationResponse.make_one(res)

    def update_ingestion_destination(
        self,
        res: "bs_td.UpdateIngestionDestinationResponseTypeDef",
    ) -> "dc_td.UpdateIngestionDestinationResponse":
        return dc_td.UpdateIngestionDestinationResponse.make_one(res)


appfabric_caster = APPFABRICCaster()
