# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudcontrol import type_defs as bs_td


class CLOUDCONTROLCaster:

    def cancel_resource_request(
        self,
        res: "bs_td.CancelResourceRequestOutputTypeDef",
    ) -> "dc_td.CancelResourceRequestOutput":
        return dc_td.CancelResourceRequestOutput.make_one(res)

    def create_resource(
        self,
        res: "bs_td.CreateResourceOutputTypeDef",
    ) -> "dc_td.CreateResourceOutput":
        return dc_td.CreateResourceOutput.make_one(res)

    def delete_resource(
        self,
        res: "bs_td.DeleteResourceOutputTypeDef",
    ) -> "dc_td.DeleteResourceOutput":
        return dc_td.DeleteResourceOutput.make_one(res)

    def get_resource(
        self,
        res: "bs_td.GetResourceOutputTypeDef",
    ) -> "dc_td.GetResourceOutput":
        return dc_td.GetResourceOutput.make_one(res)

    def get_resource_request_status(
        self,
        res: "bs_td.GetResourceRequestStatusOutputTypeDef",
    ) -> "dc_td.GetResourceRequestStatusOutput":
        return dc_td.GetResourceRequestStatusOutput.make_one(res)

    def list_resource_requests(
        self,
        res: "bs_td.ListResourceRequestsOutputTypeDef",
    ) -> "dc_td.ListResourceRequestsOutput":
        return dc_td.ListResourceRequestsOutput.make_one(res)

    def list_resources(
        self,
        res: "bs_td.ListResourcesOutputTypeDef",
    ) -> "dc_td.ListResourcesOutput":
        return dc_td.ListResourcesOutput.make_one(res)

    def update_resource(
        self,
        res: "bs_td.UpdateResourceOutputTypeDef",
    ) -> "dc_td.UpdateResourceOutput":
        return dc_td.UpdateResourceOutput.make_one(res)


cloudcontrol_caster = CLOUDCONTROLCaster()
