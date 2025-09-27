# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_backup_gateway import type_defs as bs_td


class BACKUP_GATEWAYCaster:

    def associate_gateway_to_server(
        self,
        res: "bs_td.AssociateGatewayToServerOutputTypeDef",
    ) -> "dc_td.AssociateGatewayToServerOutput":
        return dc_td.AssociateGatewayToServerOutput.make_one(res)

    def create_gateway(
        self,
        res: "bs_td.CreateGatewayOutputTypeDef",
    ) -> "dc_td.CreateGatewayOutput":
        return dc_td.CreateGatewayOutput.make_one(res)

    def delete_gateway(
        self,
        res: "bs_td.DeleteGatewayOutputTypeDef",
    ) -> "dc_td.DeleteGatewayOutput":
        return dc_td.DeleteGatewayOutput.make_one(res)

    def delete_hypervisor(
        self,
        res: "bs_td.DeleteHypervisorOutputTypeDef",
    ) -> "dc_td.DeleteHypervisorOutput":
        return dc_td.DeleteHypervisorOutput.make_one(res)

    def disassociate_gateway_from_server(
        self,
        res: "bs_td.DisassociateGatewayFromServerOutputTypeDef",
    ) -> "dc_td.DisassociateGatewayFromServerOutput":
        return dc_td.DisassociateGatewayFromServerOutput.make_one(res)

    def get_bandwidth_rate_limit_schedule(
        self,
        res: "bs_td.GetBandwidthRateLimitScheduleOutputTypeDef",
    ) -> "dc_td.GetBandwidthRateLimitScheduleOutput":
        return dc_td.GetBandwidthRateLimitScheduleOutput.make_one(res)

    def get_gateway(
        self,
        res: "bs_td.GetGatewayOutputTypeDef",
    ) -> "dc_td.GetGatewayOutput":
        return dc_td.GetGatewayOutput.make_one(res)

    def get_hypervisor(
        self,
        res: "bs_td.GetHypervisorOutputTypeDef",
    ) -> "dc_td.GetHypervisorOutput":
        return dc_td.GetHypervisorOutput.make_one(res)

    def get_hypervisor_property_mappings(
        self,
        res: "bs_td.GetHypervisorPropertyMappingsOutputTypeDef",
    ) -> "dc_td.GetHypervisorPropertyMappingsOutput":
        return dc_td.GetHypervisorPropertyMappingsOutput.make_one(res)

    def get_virtual_machine(
        self,
        res: "bs_td.GetVirtualMachineOutputTypeDef",
    ) -> "dc_td.GetVirtualMachineOutput":
        return dc_td.GetVirtualMachineOutput.make_one(res)

    def import_hypervisor_configuration(
        self,
        res: "bs_td.ImportHypervisorConfigurationOutputTypeDef",
    ) -> "dc_td.ImportHypervisorConfigurationOutput":
        return dc_td.ImportHypervisorConfigurationOutput.make_one(res)

    def list_gateways(
        self,
        res: "bs_td.ListGatewaysOutputTypeDef",
    ) -> "dc_td.ListGatewaysOutput":
        return dc_td.ListGatewaysOutput.make_one(res)

    def list_hypervisors(
        self,
        res: "bs_td.ListHypervisorsOutputTypeDef",
    ) -> "dc_td.ListHypervisorsOutput":
        return dc_td.ListHypervisorsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_virtual_machines(
        self,
        res: "bs_td.ListVirtualMachinesOutputTypeDef",
    ) -> "dc_td.ListVirtualMachinesOutput":
        return dc_td.ListVirtualMachinesOutput.make_one(res)

    def put_bandwidth_rate_limit_schedule(
        self,
        res: "bs_td.PutBandwidthRateLimitScheduleOutputTypeDef",
    ) -> "dc_td.PutBandwidthRateLimitScheduleOutput":
        return dc_td.PutBandwidthRateLimitScheduleOutput.make_one(res)

    def put_hypervisor_property_mappings(
        self,
        res: "bs_td.PutHypervisorPropertyMappingsOutputTypeDef",
    ) -> "dc_td.PutHypervisorPropertyMappingsOutput":
        return dc_td.PutHypervisorPropertyMappingsOutput.make_one(res)

    def put_maintenance_start_time(
        self,
        res: "bs_td.PutMaintenanceStartTimeOutputTypeDef",
    ) -> "dc_td.PutMaintenanceStartTimeOutput":
        return dc_td.PutMaintenanceStartTimeOutput.make_one(res)

    def start_virtual_machines_metadata_sync(
        self,
        res: "bs_td.StartVirtualMachinesMetadataSyncOutputTypeDef",
    ) -> "dc_td.StartVirtualMachinesMetadataSyncOutput":
        return dc_td.StartVirtualMachinesMetadataSyncOutput.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.TagResourceOutputTypeDef",
    ) -> "dc_td.TagResourceOutput":
        return dc_td.TagResourceOutput.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.UntagResourceOutputTypeDef",
    ) -> "dc_td.UntagResourceOutput":
        return dc_td.UntagResourceOutput.make_one(res)

    def update_gateway_information(
        self,
        res: "bs_td.UpdateGatewayInformationOutputTypeDef",
    ) -> "dc_td.UpdateGatewayInformationOutput":
        return dc_td.UpdateGatewayInformationOutput.make_one(res)

    def update_gateway_software_now(
        self,
        res: "bs_td.UpdateGatewaySoftwareNowOutputTypeDef",
    ) -> "dc_td.UpdateGatewaySoftwareNowOutput":
        return dc_td.UpdateGatewaySoftwareNowOutput.make_one(res)

    def update_hypervisor(
        self,
        res: "bs_td.UpdateHypervisorOutputTypeDef",
    ) -> "dc_td.UpdateHypervisorOutput":
        return dc_td.UpdateHypervisorOutput.make_one(res)


backup_gateway_caster = BACKUP_GATEWAYCaster()
