# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_application_signals import type_defs as bs_td


class APPLICATION_SIGNALSCaster:

    def batch_get_service_level_objective_budget_report(
        self,
        res: "bs_td.BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef",
    ) -> "dc_td.BatchGetServiceLevelObjectiveBudgetReportOutput":
        return dc_td.BatchGetServiceLevelObjectiveBudgetReportOutput.make_one(res)

    def batch_update_exclusion_windows(
        self,
        res: "bs_td.BatchUpdateExclusionWindowsOutputTypeDef",
    ) -> "dc_td.BatchUpdateExclusionWindowsOutput":
        return dc_td.BatchUpdateExclusionWindowsOutput.make_one(res)

    def create_service_level_objective(
        self,
        res: "bs_td.CreateServiceLevelObjectiveOutputTypeDef",
    ) -> "dc_td.CreateServiceLevelObjectiveOutput":
        return dc_td.CreateServiceLevelObjectiveOutput.make_one(res)

    def get_service(
        self,
        res: "bs_td.GetServiceOutputTypeDef",
    ) -> "dc_td.GetServiceOutput":
        return dc_td.GetServiceOutput.make_one(res)

    def get_service_level_objective(
        self,
        res: "bs_td.GetServiceLevelObjectiveOutputTypeDef",
    ) -> "dc_td.GetServiceLevelObjectiveOutput":
        return dc_td.GetServiceLevelObjectiveOutput.make_one(res)

    def list_service_dependencies(
        self,
        res: "bs_td.ListServiceDependenciesOutputTypeDef",
    ) -> "dc_td.ListServiceDependenciesOutput":
        return dc_td.ListServiceDependenciesOutput.make_one(res)

    def list_service_dependents(
        self,
        res: "bs_td.ListServiceDependentsOutputTypeDef",
    ) -> "dc_td.ListServiceDependentsOutput":
        return dc_td.ListServiceDependentsOutput.make_one(res)

    def list_service_level_objective_exclusion_windows(
        self,
        res: "bs_td.ListServiceLevelObjectiveExclusionWindowsOutputTypeDef",
    ) -> "dc_td.ListServiceLevelObjectiveExclusionWindowsOutput":
        return dc_td.ListServiceLevelObjectiveExclusionWindowsOutput.make_one(res)

    def list_service_level_objectives(
        self,
        res: "bs_td.ListServiceLevelObjectivesOutputTypeDef",
    ) -> "dc_td.ListServiceLevelObjectivesOutput":
        return dc_td.ListServiceLevelObjectivesOutput.make_one(res)

    def list_service_operations(
        self,
        res: "bs_td.ListServiceOperationsOutputTypeDef",
    ) -> "dc_td.ListServiceOperationsOutput":
        return dc_td.ListServiceOperationsOutput.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesOutputTypeDef",
    ) -> "dc_td.ListServicesOutput":
        return dc_td.ListServicesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_service_level_objective(
        self,
        res: "bs_td.UpdateServiceLevelObjectiveOutputTypeDef",
    ) -> "dc_td.UpdateServiceLevelObjectiveOutput":
        return dc_td.UpdateServiceLevelObjectiveOutput.make_one(res)


application_signals_caster = APPLICATION_SIGNALSCaster()
