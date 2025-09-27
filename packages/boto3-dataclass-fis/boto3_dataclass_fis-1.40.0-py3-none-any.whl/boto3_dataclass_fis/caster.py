# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_fis import type_defs as bs_td


class FISCaster:

    def create_experiment_template(
        self,
        res: "bs_td.CreateExperimentTemplateResponseTypeDef",
    ) -> "dc_td.CreateExperimentTemplateResponse":
        return dc_td.CreateExperimentTemplateResponse.make_one(res)

    def create_target_account_configuration(
        self,
        res: "bs_td.CreateTargetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.CreateTargetAccountConfigurationResponse":
        return dc_td.CreateTargetAccountConfigurationResponse.make_one(res)

    def delete_experiment_template(
        self,
        res: "bs_td.DeleteExperimentTemplateResponseTypeDef",
    ) -> "dc_td.DeleteExperimentTemplateResponse":
        return dc_td.DeleteExperimentTemplateResponse.make_one(res)

    def delete_target_account_configuration(
        self,
        res: "bs_td.DeleteTargetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteTargetAccountConfigurationResponse":
        return dc_td.DeleteTargetAccountConfigurationResponse.make_one(res)

    def get_action(
        self,
        res: "bs_td.GetActionResponseTypeDef",
    ) -> "dc_td.GetActionResponse":
        return dc_td.GetActionResponse.make_one(res)

    def get_experiment(
        self,
        res: "bs_td.GetExperimentResponseTypeDef",
    ) -> "dc_td.GetExperimentResponse":
        return dc_td.GetExperimentResponse.make_one(res)

    def get_experiment_target_account_configuration(
        self,
        res: "bs_td.GetExperimentTargetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.GetExperimentTargetAccountConfigurationResponse":
        return dc_td.GetExperimentTargetAccountConfigurationResponse.make_one(res)

    def get_experiment_template(
        self,
        res: "bs_td.GetExperimentTemplateResponseTypeDef",
    ) -> "dc_td.GetExperimentTemplateResponse":
        return dc_td.GetExperimentTemplateResponse.make_one(res)

    def get_safety_lever(
        self,
        res: "bs_td.GetSafetyLeverResponseTypeDef",
    ) -> "dc_td.GetSafetyLeverResponse":
        return dc_td.GetSafetyLeverResponse.make_one(res)

    def get_target_account_configuration(
        self,
        res: "bs_td.GetTargetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.GetTargetAccountConfigurationResponse":
        return dc_td.GetTargetAccountConfigurationResponse.make_one(res)

    def get_target_resource_type(
        self,
        res: "bs_td.GetTargetResourceTypeResponseTypeDef",
    ) -> "dc_td.GetTargetResourceTypeResponse":
        return dc_td.GetTargetResourceTypeResponse.make_one(res)

    def list_actions(
        self,
        res: "bs_td.ListActionsResponseTypeDef",
    ) -> "dc_td.ListActionsResponse":
        return dc_td.ListActionsResponse.make_one(res)

    def list_experiment_resolved_targets(
        self,
        res: "bs_td.ListExperimentResolvedTargetsResponseTypeDef",
    ) -> "dc_td.ListExperimentResolvedTargetsResponse":
        return dc_td.ListExperimentResolvedTargetsResponse.make_one(res)

    def list_experiment_target_account_configurations(
        self,
        res: "bs_td.ListExperimentTargetAccountConfigurationsResponseTypeDef",
    ) -> "dc_td.ListExperimentTargetAccountConfigurationsResponse":
        return dc_td.ListExperimentTargetAccountConfigurationsResponse.make_one(res)

    def list_experiment_templates(
        self,
        res: "bs_td.ListExperimentTemplatesResponseTypeDef",
    ) -> "dc_td.ListExperimentTemplatesResponse":
        return dc_td.ListExperimentTemplatesResponse.make_one(res)

    def list_experiments(
        self,
        res: "bs_td.ListExperimentsResponseTypeDef",
    ) -> "dc_td.ListExperimentsResponse":
        return dc_td.ListExperimentsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_target_account_configurations(
        self,
        res: "bs_td.ListTargetAccountConfigurationsResponseTypeDef",
    ) -> "dc_td.ListTargetAccountConfigurationsResponse":
        return dc_td.ListTargetAccountConfigurationsResponse.make_one(res)

    def list_target_resource_types(
        self,
        res: "bs_td.ListTargetResourceTypesResponseTypeDef",
    ) -> "dc_td.ListTargetResourceTypesResponse":
        return dc_td.ListTargetResourceTypesResponse.make_one(res)

    def start_experiment(
        self,
        res: "bs_td.StartExperimentResponseTypeDef",
    ) -> "dc_td.StartExperimentResponse":
        return dc_td.StartExperimentResponse.make_one(res)

    def stop_experiment(
        self,
        res: "bs_td.StopExperimentResponseTypeDef",
    ) -> "dc_td.StopExperimentResponse":
        return dc_td.StopExperimentResponse.make_one(res)

    def update_experiment_template(
        self,
        res: "bs_td.UpdateExperimentTemplateResponseTypeDef",
    ) -> "dc_td.UpdateExperimentTemplateResponse":
        return dc_td.UpdateExperimentTemplateResponse.make_one(res)

    def update_safety_lever_state(
        self,
        res: "bs_td.UpdateSafetyLeverStateResponseTypeDef",
    ) -> "dc_td.UpdateSafetyLeverStateResponse":
        return dc_td.UpdateSafetyLeverStateResponse.make_one(res)

    def update_target_account_configuration(
        self,
        res: "bs_td.UpdateTargetAccountConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateTargetAccountConfigurationResponse":
        return dc_td.UpdateTargetAccountConfigurationResponse.make_one(res)


fis_caster = FISCaster()
