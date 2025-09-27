# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_data_automation import type_defs as bs_td


class BEDROCK_DATA_AUTOMATIONCaster:

    def create_blueprint(
        self,
        res: "bs_td.CreateBlueprintResponseTypeDef",
    ) -> "dc_td.CreateBlueprintResponse":
        return dc_td.CreateBlueprintResponse.make_one(res)

    def create_blueprint_version(
        self,
        res: "bs_td.CreateBlueprintVersionResponseTypeDef",
    ) -> "dc_td.CreateBlueprintVersionResponse":
        return dc_td.CreateBlueprintVersionResponse.make_one(res)

    def create_data_automation_project(
        self,
        res: "bs_td.CreateDataAutomationProjectResponseTypeDef",
    ) -> "dc_td.CreateDataAutomationProjectResponse":
        return dc_td.CreateDataAutomationProjectResponse.make_one(res)

    def delete_data_automation_project(
        self,
        res: "bs_td.DeleteDataAutomationProjectResponseTypeDef",
    ) -> "dc_td.DeleteDataAutomationProjectResponse":
        return dc_td.DeleteDataAutomationProjectResponse.make_one(res)

    def get_blueprint(
        self,
        res: "bs_td.GetBlueprintResponseTypeDef",
    ) -> "dc_td.GetBlueprintResponse":
        return dc_td.GetBlueprintResponse.make_one(res)

    def get_data_automation_project(
        self,
        res: "bs_td.GetDataAutomationProjectResponseTypeDef",
    ) -> "dc_td.GetDataAutomationProjectResponse":
        return dc_td.GetDataAutomationProjectResponse.make_one(res)

    def list_blueprints(
        self,
        res: "bs_td.ListBlueprintsResponseTypeDef",
    ) -> "dc_td.ListBlueprintsResponse":
        return dc_td.ListBlueprintsResponse.make_one(res)

    def list_data_automation_projects(
        self,
        res: "bs_td.ListDataAutomationProjectsResponseTypeDef",
    ) -> "dc_td.ListDataAutomationProjectsResponse":
        return dc_td.ListDataAutomationProjectsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_blueprint(
        self,
        res: "bs_td.UpdateBlueprintResponseTypeDef",
    ) -> "dc_td.UpdateBlueprintResponse":
        return dc_td.UpdateBlueprintResponse.make_one(res)

    def update_data_automation_project(
        self,
        res: "bs_td.UpdateDataAutomationProjectResponseTypeDef",
    ) -> "dc_td.UpdateDataAutomationProjectResponse":
        return dc_td.UpdateDataAutomationProjectResponse.make_one(res)


bedrock_data_automation_caster = BEDROCK_DATA_AUTOMATIONCaster()
