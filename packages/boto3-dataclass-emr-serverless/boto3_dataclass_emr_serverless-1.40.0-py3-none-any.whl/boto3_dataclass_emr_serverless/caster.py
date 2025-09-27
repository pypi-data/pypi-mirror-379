# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_emr_serverless import type_defs as bs_td


class EMR_SERVERLESSCaster:

    def cancel_job_run(
        self,
        res: "bs_td.CancelJobRunResponseTypeDef",
    ) -> "dc_td.CancelJobRunResponse":
        return dc_td.CancelJobRunResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_dashboard_for_job_run(
        self,
        res: "bs_td.GetDashboardForJobRunResponseTypeDef",
    ) -> "dc_td.GetDashboardForJobRunResponse":
        return dc_td.GetDashboardForJobRunResponse.make_one(res)

    def get_job_run(
        self,
        res: "bs_td.GetJobRunResponseTypeDef",
    ) -> "dc_td.GetJobRunResponse":
        return dc_td.GetJobRunResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_job_run_attempts(
        self,
        res: "bs_td.ListJobRunAttemptsResponseTypeDef",
    ) -> "dc_td.ListJobRunAttemptsResponse":
        return dc_td.ListJobRunAttemptsResponse.make_one(res)

    def list_job_runs(
        self,
        res: "bs_td.ListJobRunsResponseTypeDef",
    ) -> "dc_td.ListJobRunsResponse":
        return dc_td.ListJobRunsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_job_run(
        self,
        res: "bs_td.StartJobRunResponseTypeDef",
    ) -> "dc_td.StartJobRunResponse":
        return dc_td.StartJobRunResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)


emr_serverless_caster = EMR_SERVERLESSCaster()
