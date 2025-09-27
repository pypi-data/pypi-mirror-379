# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_arc_zonal_shift import type_defs as bs_td


class ARC_ZONAL_SHIFTCaster:

    def cancel_practice_run(
        self,
        res: "bs_td.CancelPracticeRunResponseTypeDef",
    ) -> "dc_td.CancelPracticeRunResponse":
        return dc_td.CancelPracticeRunResponse.make_one(res)

    def cancel_zonal_shift(
        self,
        res: "bs_td.ZonalShiftTypeDef",
    ) -> "dc_td.ZonalShift":
        return dc_td.ZonalShift.make_one(res)

    def create_practice_run_configuration(
        self,
        res: "bs_td.CreatePracticeRunConfigurationResponseTypeDef",
    ) -> "dc_td.CreatePracticeRunConfigurationResponse":
        return dc_td.CreatePracticeRunConfigurationResponse.make_one(res)

    def delete_practice_run_configuration(
        self,
        res: "bs_td.DeletePracticeRunConfigurationResponseTypeDef",
    ) -> "dc_td.DeletePracticeRunConfigurationResponse":
        return dc_td.DeletePracticeRunConfigurationResponse.make_one(res)

    def get_autoshift_observer_notification_status(
        self,
        res: "bs_td.GetAutoshiftObserverNotificationStatusResponseTypeDef",
    ) -> "dc_td.GetAutoshiftObserverNotificationStatusResponse":
        return dc_td.GetAutoshiftObserverNotificationStatusResponse.make_one(res)

    def get_managed_resource(
        self,
        res: "bs_td.GetManagedResourceResponseTypeDef",
    ) -> "dc_td.GetManagedResourceResponse":
        return dc_td.GetManagedResourceResponse.make_one(res)

    def list_autoshifts(
        self,
        res: "bs_td.ListAutoshiftsResponseTypeDef",
    ) -> "dc_td.ListAutoshiftsResponse":
        return dc_td.ListAutoshiftsResponse.make_one(res)

    def list_managed_resources(
        self,
        res: "bs_td.ListManagedResourcesResponseTypeDef",
    ) -> "dc_td.ListManagedResourcesResponse":
        return dc_td.ListManagedResourcesResponse.make_one(res)

    def list_zonal_shifts(
        self,
        res: "bs_td.ListZonalShiftsResponseTypeDef",
    ) -> "dc_td.ListZonalShiftsResponse":
        return dc_td.ListZonalShiftsResponse.make_one(res)

    def start_practice_run(
        self,
        res: "bs_td.StartPracticeRunResponseTypeDef",
    ) -> "dc_td.StartPracticeRunResponse":
        return dc_td.StartPracticeRunResponse.make_one(res)

    def start_zonal_shift(
        self,
        res: "bs_td.ZonalShiftTypeDef",
    ) -> "dc_td.ZonalShift":
        return dc_td.ZonalShift.make_one(res)

    def update_autoshift_observer_notification_status(
        self,
        res: "bs_td.UpdateAutoshiftObserverNotificationStatusResponseTypeDef",
    ) -> "dc_td.UpdateAutoshiftObserverNotificationStatusResponse":
        return dc_td.UpdateAutoshiftObserverNotificationStatusResponse.make_one(res)

    def update_practice_run_configuration(
        self,
        res: "bs_td.UpdatePracticeRunConfigurationResponseTypeDef",
    ) -> "dc_td.UpdatePracticeRunConfigurationResponse":
        return dc_td.UpdatePracticeRunConfigurationResponse.make_one(res)

    def update_zonal_autoshift_configuration(
        self,
        res: "bs_td.UpdateZonalAutoshiftConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateZonalAutoshiftConfigurationResponse":
        return dc_td.UpdateZonalAutoshiftConfigurationResponse.make_one(res)

    def update_zonal_shift(
        self,
        res: "bs_td.ZonalShiftTypeDef",
    ) -> "dc_td.ZonalShift":
        return dc_td.ZonalShift.make_one(res)


arc_zonal_shift_caster = ARC_ZONAL_SHIFTCaster()
