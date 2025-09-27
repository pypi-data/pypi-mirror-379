# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_controltower import type_defs as bs_td


class CONTROLTOWERCaster:

    def create_landing_zone(
        self,
        res: "bs_td.CreateLandingZoneOutputTypeDef",
    ) -> "dc_td.CreateLandingZoneOutput":
        return dc_td.CreateLandingZoneOutput.make_one(res)

    def delete_landing_zone(
        self,
        res: "bs_td.DeleteLandingZoneOutputTypeDef",
    ) -> "dc_td.DeleteLandingZoneOutput":
        return dc_td.DeleteLandingZoneOutput.make_one(res)

    def disable_baseline(
        self,
        res: "bs_td.DisableBaselineOutputTypeDef",
    ) -> "dc_td.DisableBaselineOutput":
        return dc_td.DisableBaselineOutput.make_one(res)

    def disable_control(
        self,
        res: "bs_td.DisableControlOutputTypeDef",
    ) -> "dc_td.DisableControlOutput":
        return dc_td.DisableControlOutput.make_one(res)

    def enable_baseline(
        self,
        res: "bs_td.EnableBaselineOutputTypeDef",
    ) -> "dc_td.EnableBaselineOutput":
        return dc_td.EnableBaselineOutput.make_one(res)

    def enable_control(
        self,
        res: "bs_td.EnableControlOutputTypeDef",
    ) -> "dc_td.EnableControlOutput":
        return dc_td.EnableControlOutput.make_one(res)

    def get_baseline(
        self,
        res: "bs_td.GetBaselineOutputTypeDef",
    ) -> "dc_td.GetBaselineOutput":
        return dc_td.GetBaselineOutput.make_one(res)

    def get_baseline_operation(
        self,
        res: "bs_td.GetBaselineOperationOutputTypeDef",
    ) -> "dc_td.GetBaselineOperationOutput":
        return dc_td.GetBaselineOperationOutput.make_one(res)

    def get_control_operation(
        self,
        res: "bs_td.GetControlOperationOutputTypeDef",
    ) -> "dc_td.GetControlOperationOutput":
        return dc_td.GetControlOperationOutput.make_one(res)

    def get_enabled_baseline(
        self,
        res: "bs_td.GetEnabledBaselineOutputTypeDef",
    ) -> "dc_td.GetEnabledBaselineOutput":
        return dc_td.GetEnabledBaselineOutput.make_one(res)

    def get_enabled_control(
        self,
        res: "bs_td.GetEnabledControlOutputTypeDef",
    ) -> "dc_td.GetEnabledControlOutput":
        return dc_td.GetEnabledControlOutput.make_one(res)

    def get_landing_zone(
        self,
        res: "bs_td.GetLandingZoneOutputTypeDef",
    ) -> "dc_td.GetLandingZoneOutput":
        return dc_td.GetLandingZoneOutput.make_one(res)

    def get_landing_zone_operation(
        self,
        res: "bs_td.GetLandingZoneOperationOutputTypeDef",
    ) -> "dc_td.GetLandingZoneOperationOutput":
        return dc_td.GetLandingZoneOperationOutput.make_one(res)

    def list_baselines(
        self,
        res: "bs_td.ListBaselinesOutputTypeDef",
    ) -> "dc_td.ListBaselinesOutput":
        return dc_td.ListBaselinesOutput.make_one(res)

    def list_control_operations(
        self,
        res: "bs_td.ListControlOperationsOutputTypeDef",
    ) -> "dc_td.ListControlOperationsOutput":
        return dc_td.ListControlOperationsOutput.make_one(res)

    def list_enabled_baselines(
        self,
        res: "bs_td.ListEnabledBaselinesOutputTypeDef",
    ) -> "dc_td.ListEnabledBaselinesOutput":
        return dc_td.ListEnabledBaselinesOutput.make_one(res)

    def list_enabled_controls(
        self,
        res: "bs_td.ListEnabledControlsOutputTypeDef",
    ) -> "dc_td.ListEnabledControlsOutput":
        return dc_td.ListEnabledControlsOutput.make_one(res)

    def list_landing_zone_operations(
        self,
        res: "bs_td.ListLandingZoneOperationsOutputTypeDef",
    ) -> "dc_td.ListLandingZoneOperationsOutput":
        return dc_td.ListLandingZoneOperationsOutput.make_one(res)

    def list_landing_zones(
        self,
        res: "bs_td.ListLandingZonesOutputTypeDef",
    ) -> "dc_td.ListLandingZonesOutput":
        return dc_td.ListLandingZonesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def reset_enabled_baseline(
        self,
        res: "bs_td.ResetEnabledBaselineOutputTypeDef",
    ) -> "dc_td.ResetEnabledBaselineOutput":
        return dc_td.ResetEnabledBaselineOutput.make_one(res)

    def reset_enabled_control(
        self,
        res: "bs_td.ResetEnabledControlOutputTypeDef",
    ) -> "dc_td.ResetEnabledControlOutput":
        return dc_td.ResetEnabledControlOutput.make_one(res)

    def reset_landing_zone(
        self,
        res: "bs_td.ResetLandingZoneOutputTypeDef",
    ) -> "dc_td.ResetLandingZoneOutput":
        return dc_td.ResetLandingZoneOutput.make_one(res)

    def update_enabled_baseline(
        self,
        res: "bs_td.UpdateEnabledBaselineOutputTypeDef",
    ) -> "dc_td.UpdateEnabledBaselineOutput":
        return dc_td.UpdateEnabledBaselineOutput.make_one(res)

    def update_enabled_control(
        self,
        res: "bs_td.UpdateEnabledControlOutputTypeDef",
    ) -> "dc_td.UpdateEnabledControlOutput":
        return dc_td.UpdateEnabledControlOutput.make_one(res)

    def update_landing_zone(
        self,
        res: "bs_td.UpdateLandingZoneOutputTypeDef",
    ) -> "dc_td.UpdateLandingZoneOutput":
        return dc_td.UpdateLandingZoneOutput.make_one(res)


controltower_caster = CONTROLTOWERCaster()
