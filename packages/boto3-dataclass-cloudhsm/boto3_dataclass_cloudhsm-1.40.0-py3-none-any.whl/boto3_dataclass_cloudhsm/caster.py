# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudhsm import type_defs as bs_td


class CLOUDHSMCaster:

    def add_tags_to_resource(
        self,
        res: "bs_td.AddTagsToResourceResponseTypeDef",
    ) -> "dc_td.AddTagsToResourceResponse":
        return dc_td.AddTagsToResourceResponse.make_one(res)

    def create_hapg(
        self,
        res: "bs_td.CreateHapgResponseTypeDef",
    ) -> "dc_td.CreateHapgResponse":
        return dc_td.CreateHapgResponse.make_one(res)

    def create_hsm(
        self,
        res: "bs_td.CreateHsmResponseTypeDef",
    ) -> "dc_td.CreateHsmResponse":
        return dc_td.CreateHsmResponse.make_one(res)

    def create_luna_client(
        self,
        res: "bs_td.CreateLunaClientResponseTypeDef",
    ) -> "dc_td.CreateLunaClientResponse":
        return dc_td.CreateLunaClientResponse.make_one(res)

    def delete_hapg(
        self,
        res: "bs_td.DeleteHapgResponseTypeDef",
    ) -> "dc_td.DeleteHapgResponse":
        return dc_td.DeleteHapgResponse.make_one(res)

    def delete_hsm(
        self,
        res: "bs_td.DeleteHsmResponseTypeDef",
    ) -> "dc_td.DeleteHsmResponse":
        return dc_td.DeleteHsmResponse.make_one(res)

    def delete_luna_client(
        self,
        res: "bs_td.DeleteLunaClientResponseTypeDef",
    ) -> "dc_td.DeleteLunaClientResponse":
        return dc_td.DeleteLunaClientResponse.make_one(res)

    def describe_hapg(
        self,
        res: "bs_td.DescribeHapgResponseTypeDef",
    ) -> "dc_td.DescribeHapgResponse":
        return dc_td.DescribeHapgResponse.make_one(res)

    def describe_hsm(
        self,
        res: "bs_td.DescribeHsmResponseTypeDef",
    ) -> "dc_td.DescribeHsmResponse":
        return dc_td.DescribeHsmResponse.make_one(res)

    def describe_luna_client(
        self,
        res: "bs_td.DescribeLunaClientResponseTypeDef",
    ) -> "dc_td.DescribeLunaClientResponse":
        return dc_td.DescribeLunaClientResponse.make_one(res)

    def get_config(
        self,
        res: "bs_td.GetConfigResponseTypeDef",
    ) -> "dc_td.GetConfigResponse":
        return dc_td.GetConfigResponse.make_one(res)

    def list_available_zones(
        self,
        res: "bs_td.ListAvailableZonesResponseTypeDef",
    ) -> "dc_td.ListAvailableZonesResponse":
        return dc_td.ListAvailableZonesResponse.make_one(res)

    def list_hapgs(
        self,
        res: "bs_td.ListHapgsResponseTypeDef",
    ) -> "dc_td.ListHapgsResponse":
        return dc_td.ListHapgsResponse.make_one(res)

    def list_hsms(
        self,
        res: "bs_td.ListHsmsResponseTypeDef",
    ) -> "dc_td.ListHsmsResponse":
        return dc_td.ListHsmsResponse.make_one(res)

    def list_luna_clients(
        self,
        res: "bs_td.ListLunaClientsResponseTypeDef",
    ) -> "dc_td.ListLunaClientsResponse":
        return dc_td.ListLunaClientsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def modify_hapg(
        self,
        res: "bs_td.ModifyHapgResponseTypeDef",
    ) -> "dc_td.ModifyHapgResponse":
        return dc_td.ModifyHapgResponse.make_one(res)

    def modify_hsm(
        self,
        res: "bs_td.ModifyHsmResponseTypeDef",
    ) -> "dc_td.ModifyHsmResponse":
        return dc_td.ModifyHsmResponse.make_one(res)

    def modify_luna_client(
        self,
        res: "bs_td.ModifyLunaClientResponseTypeDef",
    ) -> "dc_td.ModifyLunaClientResponse":
        return dc_td.ModifyLunaClientResponse.make_one(res)

    def remove_tags_from_resource(
        self,
        res: "bs_td.RemoveTagsFromResourceResponseTypeDef",
    ) -> "dc_td.RemoveTagsFromResourceResponse":
        return dc_td.RemoveTagsFromResourceResponse.make_one(res)


cloudhsm_caster = CLOUDHSMCaster()
