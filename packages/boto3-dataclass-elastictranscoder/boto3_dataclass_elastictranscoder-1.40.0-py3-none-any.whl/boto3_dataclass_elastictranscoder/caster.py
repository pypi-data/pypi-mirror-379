# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elastictranscoder import type_defs as bs_td


class ELASTICTRANSCODERCaster:

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_pipeline(
        self,
        res: "bs_td.CreatePipelineResponseTypeDef",
    ) -> "dc_td.CreatePipelineResponse":
        return dc_td.CreatePipelineResponse.make_one(res)

    def create_preset(
        self,
        res: "bs_td.CreatePresetResponseTypeDef",
    ) -> "dc_td.CreatePresetResponse":
        return dc_td.CreatePresetResponse.make_one(res)

    def list_jobs_by_pipeline(
        self,
        res: "bs_td.ListJobsByPipelineResponseTypeDef",
    ) -> "dc_td.ListJobsByPipelineResponse":
        return dc_td.ListJobsByPipelineResponse.make_one(res)

    def list_jobs_by_status(
        self,
        res: "bs_td.ListJobsByStatusResponseTypeDef",
    ) -> "dc_td.ListJobsByStatusResponse":
        return dc_td.ListJobsByStatusResponse.make_one(res)

    def list_pipelines(
        self,
        res: "bs_td.ListPipelinesResponseTypeDef",
    ) -> "dc_td.ListPipelinesResponse":
        return dc_td.ListPipelinesResponse.make_one(res)

    def list_presets(
        self,
        res: "bs_td.ListPresetsResponseTypeDef",
    ) -> "dc_td.ListPresetsResponse":
        return dc_td.ListPresetsResponse.make_one(res)

    def read_job(
        self,
        res: "bs_td.ReadJobResponseTypeDef",
    ) -> "dc_td.ReadJobResponse":
        return dc_td.ReadJobResponse.make_one(res)

    def read_pipeline(
        self,
        res: "bs_td.ReadPipelineResponseTypeDef",
    ) -> "dc_td.ReadPipelineResponse":
        return dc_td.ReadPipelineResponse.make_one(res)

    def read_preset(
        self,
        res: "bs_td.ReadPresetResponseTypeDef",
    ) -> "dc_td.ReadPresetResponse":
        return dc_td.ReadPresetResponse.make_one(res)

    def test_role(
        self,
        res: "bs_td.TestRoleResponseTypeDef",
    ) -> "dc_td.TestRoleResponse":
        return dc_td.TestRoleResponse.make_one(res)

    def update_pipeline(
        self,
        res: "bs_td.UpdatePipelineResponseTypeDef",
    ) -> "dc_td.UpdatePipelineResponse":
        return dc_td.UpdatePipelineResponse.make_one(res)

    def update_pipeline_notifications(
        self,
        res: "bs_td.UpdatePipelineNotificationsResponseTypeDef",
    ) -> "dc_td.UpdatePipelineNotificationsResponse":
        return dc_td.UpdatePipelineNotificationsResponse.make_one(res)

    def update_pipeline_status(
        self,
        res: "bs_td.UpdatePipelineStatusResponseTypeDef",
    ) -> "dc_td.UpdatePipelineStatusResponse":
        return dc_td.UpdatePipelineStatusResponse.make_one(res)


elastictranscoder_caster = ELASTICTRANSCODERCaster()
