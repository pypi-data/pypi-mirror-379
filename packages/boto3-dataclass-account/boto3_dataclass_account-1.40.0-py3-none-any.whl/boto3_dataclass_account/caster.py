# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_account import type_defs as bs_td


class ACCOUNTCaster:

    def accept_primary_email_update(
        self,
        res: "bs_td.AcceptPrimaryEmailUpdateResponseTypeDef",
    ) -> "dc_td.AcceptPrimaryEmailUpdateResponse":
        return dc_td.AcceptPrimaryEmailUpdateResponse.make_one(res)

    def delete_alternate_contact(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_region(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_region(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account_information(
        self,
        res: "bs_td.GetAccountInformationResponseTypeDef",
    ) -> "dc_td.GetAccountInformationResponse":
        return dc_td.GetAccountInformationResponse.make_one(res)

    def get_alternate_contact(
        self,
        res: "bs_td.GetAlternateContactResponseTypeDef",
    ) -> "dc_td.GetAlternateContactResponse":
        return dc_td.GetAlternateContactResponse.make_one(res)

    def get_contact_information(
        self,
        res: "bs_td.GetContactInformationResponseTypeDef",
    ) -> "dc_td.GetContactInformationResponse":
        return dc_td.GetContactInformationResponse.make_one(res)

    def get_primary_email(
        self,
        res: "bs_td.GetPrimaryEmailResponseTypeDef",
    ) -> "dc_td.GetPrimaryEmailResponse":
        return dc_td.GetPrimaryEmailResponse.make_one(res)

    def get_region_opt_status(
        self,
        res: "bs_td.GetRegionOptStatusResponseTypeDef",
    ) -> "dc_td.GetRegionOptStatusResponse":
        return dc_td.GetRegionOptStatusResponse.make_one(res)

    def list_regions(
        self,
        res: "bs_td.ListRegionsResponseTypeDef",
    ) -> "dc_td.ListRegionsResponse":
        return dc_td.ListRegionsResponse.make_one(res)

    def put_account_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_alternate_contact(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_contact_information(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_primary_email_update(
        self,
        res: "bs_td.StartPrimaryEmailUpdateResponseTypeDef",
    ) -> "dc_td.StartPrimaryEmailUpdateResponse":
        return dc_td.StartPrimaryEmailUpdateResponse.make_one(res)


account_caster = ACCOUNTCaster()
