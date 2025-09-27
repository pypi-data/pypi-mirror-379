# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dataexchange import type_defs as bs_td


class DATAEXCHANGECaster:

    def accept_data_grant(
        self,
        res: "bs_td.AcceptDataGrantResponseTypeDef",
    ) -> "dc_td.AcceptDataGrantResponse":
        return dc_td.AcceptDataGrantResponse.make_one(res)

    def cancel_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_data_grant(
        self,
        res: "bs_td.CreateDataGrantResponseTypeDef",
    ) -> "dc_td.CreateDataGrantResponse":
        return dc_td.CreateDataGrantResponse.make_one(res)

    def create_data_set(
        self,
        res: "bs_td.CreateDataSetResponseTypeDef",
    ) -> "dc_td.CreateDataSetResponse":
        return dc_td.CreateDataSetResponse.make_one(res)

    def create_event_action(
        self,
        res: "bs_td.CreateEventActionResponseTypeDef",
    ) -> "dc_td.CreateEventActionResponse":
        return dc_td.CreateEventActionResponse.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_revision(
        self,
        res: "bs_td.CreateRevisionResponseTypeDef",
    ) -> "dc_td.CreateRevisionResponse":
        return dc_td.CreateRevisionResponse.make_one(res)

    def delete_asset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_data_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_data_set(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_action(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_revision(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_asset(
        self,
        res: "bs_td.GetAssetResponseTypeDef",
    ) -> "dc_td.GetAssetResponse":
        return dc_td.GetAssetResponse.make_one(res)

    def get_data_grant(
        self,
        res: "bs_td.GetDataGrantResponseTypeDef",
    ) -> "dc_td.GetDataGrantResponse":
        return dc_td.GetDataGrantResponse.make_one(res)

    def get_data_set(
        self,
        res: "bs_td.GetDataSetResponseTypeDef",
    ) -> "dc_td.GetDataSetResponse":
        return dc_td.GetDataSetResponse.make_one(res)

    def get_event_action(
        self,
        res: "bs_td.GetEventActionResponseTypeDef",
    ) -> "dc_td.GetEventActionResponse":
        return dc_td.GetEventActionResponse.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResponseTypeDef",
    ) -> "dc_td.GetJobResponse":
        return dc_td.GetJobResponse.make_one(res)

    def get_received_data_grant(
        self,
        res: "bs_td.GetReceivedDataGrantResponseTypeDef",
    ) -> "dc_td.GetReceivedDataGrantResponse":
        return dc_td.GetReceivedDataGrantResponse.make_one(res)

    def get_revision(
        self,
        res: "bs_td.GetRevisionResponseTypeDef",
    ) -> "dc_td.GetRevisionResponse":
        return dc_td.GetRevisionResponse.make_one(res)

    def list_data_grants(
        self,
        res: "bs_td.ListDataGrantsResponseTypeDef",
    ) -> "dc_td.ListDataGrantsResponse":
        return dc_td.ListDataGrantsResponse.make_one(res)

    def list_data_set_revisions(
        self,
        res: "bs_td.ListDataSetRevisionsResponseTypeDef",
    ) -> "dc_td.ListDataSetRevisionsResponse":
        return dc_td.ListDataSetRevisionsResponse.make_one(res)

    def list_data_sets(
        self,
        res: "bs_td.ListDataSetsResponseTypeDef",
    ) -> "dc_td.ListDataSetsResponse":
        return dc_td.ListDataSetsResponse.make_one(res)

    def list_event_actions(
        self,
        res: "bs_td.ListEventActionsResponseTypeDef",
    ) -> "dc_td.ListEventActionsResponse":
        return dc_td.ListEventActionsResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_received_data_grants(
        self,
        res: "bs_td.ListReceivedDataGrantsResponseTypeDef",
    ) -> "dc_td.ListReceivedDataGrantsResponse":
        return dc_td.ListReceivedDataGrantsResponse.make_one(res)

    def list_revision_assets(
        self,
        res: "bs_td.ListRevisionAssetsResponseTypeDef",
    ) -> "dc_td.ListRevisionAssetsResponse":
        return dc_td.ListRevisionAssetsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def revoke_revision(
        self,
        res: "bs_td.RevokeRevisionResponseTypeDef",
    ) -> "dc_td.RevokeRevisionResponse":
        return dc_td.RevokeRevisionResponse.make_one(res)

    def send_api_asset(
        self,
        res: "bs_td.SendApiAssetResponseTypeDef",
    ) -> "dc_td.SendApiAssetResponse":
        return dc_td.SendApiAssetResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_asset(
        self,
        res: "bs_td.UpdateAssetResponseTypeDef",
    ) -> "dc_td.UpdateAssetResponse":
        return dc_td.UpdateAssetResponse.make_one(res)

    def update_data_set(
        self,
        res: "bs_td.UpdateDataSetResponseTypeDef",
    ) -> "dc_td.UpdateDataSetResponse":
        return dc_td.UpdateDataSetResponse.make_one(res)

    def update_event_action(
        self,
        res: "bs_td.UpdateEventActionResponseTypeDef",
    ) -> "dc_td.UpdateEventActionResponse":
        return dc_td.UpdateEventActionResponse.make_one(res)

    def update_revision(
        self,
        res: "bs_td.UpdateRevisionResponseTypeDef",
    ) -> "dc_td.UpdateRevisionResponse":
        return dc_td.UpdateRevisionResponse.make_one(res)


dataexchange_caster = DATAEXCHANGECaster()
