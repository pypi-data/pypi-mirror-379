# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_braket import type_defs as bs_td


class BRAKETCaster:

    def cancel_job(
        self,
        res: "bs_td.CancelJobResponseTypeDef",
    ) -> "dc_td.CancelJobResponse":
        return dc_td.CancelJobResponse.make_one(res)

    def cancel_quantum_task(
        self,
        res: "bs_td.CancelQuantumTaskResponseTypeDef",
    ) -> "dc_td.CancelQuantumTaskResponse":
        return dc_td.CancelQuantumTaskResponse.make_one(res)

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_quantum_task(
        self,
        res: "bs_td.CreateQuantumTaskResponseTypeDef",
    ) -> "dc_td.CreateQuantumTaskResponse":
        return dc_td.CreateQuantumTaskResponse.make_one(res)

    def get_device(
        self,
        res: "bs_td.GetDeviceResponseTypeDef",
    ) -> "dc_td.GetDeviceResponse":
        return dc_td.GetDeviceResponse.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResponseTypeDef",
    ) -> "dc_td.GetJobResponse":
        return dc_td.GetJobResponse.make_one(res)

    def get_quantum_task(
        self,
        res: "bs_td.GetQuantumTaskResponseTypeDef",
    ) -> "dc_td.GetQuantumTaskResponse":
        return dc_td.GetQuantumTaskResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def search_devices(
        self,
        res: "bs_td.SearchDevicesResponseTypeDef",
    ) -> "dc_td.SearchDevicesResponse":
        return dc_td.SearchDevicesResponse.make_one(res)

    def search_jobs(
        self,
        res: "bs_td.SearchJobsResponseTypeDef",
    ) -> "dc_td.SearchJobsResponse":
        return dc_td.SearchJobsResponse.make_one(res)

    def search_quantum_tasks(
        self,
        res: "bs_td.SearchQuantumTasksResponseTypeDef",
    ) -> "dc_td.SearchQuantumTasksResponse":
        return dc_td.SearchQuantumTasksResponse.make_one(res)


braket_caster = BRAKETCaster()
