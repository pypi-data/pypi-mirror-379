# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_evs import type_defs as bs_td


class EVSCaster:

    def associate_eip_to_vlan(
        self,
        res: "bs_td.AssociateEipToVlanResponseTypeDef",
    ) -> "dc_td.AssociateEipToVlanResponse":
        return dc_td.AssociateEipToVlanResponse.make_one(res)

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateEnvironmentResponse":
        return dc_td.CreateEnvironmentResponse.make_one(res)

    def create_environment_host(
        self,
        res: "bs_td.CreateEnvironmentHostResponseTypeDef",
    ) -> "dc_td.CreateEnvironmentHostResponse":
        return dc_td.CreateEnvironmentHostResponse.make_one(res)

    def delete_environment(
        self,
        res: "bs_td.DeleteEnvironmentResponseTypeDef",
    ) -> "dc_td.DeleteEnvironmentResponse":
        return dc_td.DeleteEnvironmentResponse.make_one(res)

    def delete_environment_host(
        self,
        res: "bs_td.DeleteEnvironmentHostResponseTypeDef",
    ) -> "dc_td.DeleteEnvironmentHostResponse":
        return dc_td.DeleteEnvironmentHostResponse.make_one(res)

    def disassociate_eip_from_vlan(
        self,
        res: "bs_td.DisassociateEipFromVlanResponseTypeDef",
    ) -> "dc_td.DisassociateEipFromVlanResponse":
        return dc_td.DisassociateEipFromVlanResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentResponseTypeDef",
    ) -> "dc_td.GetEnvironmentResponse":
        return dc_td.GetEnvironmentResponse.make_one(res)

    def list_environment_hosts(
        self,
        res: "bs_td.ListEnvironmentHostsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentHostsResponse":
        return dc_td.ListEnvironmentHostsResponse.make_one(res)

    def list_environment_vlans(
        self,
        res: "bs_td.ListEnvironmentVlansResponseTypeDef",
    ) -> "dc_td.ListEnvironmentVlansResponse":
        return dc_td.ListEnvironmentVlansResponse.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentsResponse":
        return dc_td.ListEnvironmentsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


evs_caster = EVSCaster()
