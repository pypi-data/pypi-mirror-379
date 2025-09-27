# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apptest import type_defs as bs_td


class APPTESTCaster:

    def create_test_case(
        self,
        res: "bs_td.CreateTestCaseResponseTypeDef",
    ) -> "dc_td.CreateTestCaseResponse":
        return dc_td.CreateTestCaseResponse.make_one(res)

    def create_test_configuration(
        self,
        res: "bs_td.CreateTestConfigurationResponseTypeDef",
    ) -> "dc_td.CreateTestConfigurationResponse":
        return dc_td.CreateTestConfigurationResponse.make_one(res)

    def create_test_suite(
        self,
        res: "bs_td.CreateTestSuiteResponseTypeDef",
    ) -> "dc_td.CreateTestSuiteResponse":
        return dc_td.CreateTestSuiteResponse.make_one(res)

    def get_test_case(
        self,
        res: "bs_td.GetTestCaseResponseTypeDef",
    ) -> "dc_td.GetTestCaseResponse":
        return dc_td.GetTestCaseResponse.make_one(res)

    def get_test_configuration(
        self,
        res: "bs_td.GetTestConfigurationResponseTypeDef",
    ) -> "dc_td.GetTestConfigurationResponse":
        return dc_td.GetTestConfigurationResponse.make_one(res)

    def get_test_run_step(
        self,
        res: "bs_td.GetTestRunStepResponseTypeDef",
    ) -> "dc_td.GetTestRunStepResponse":
        return dc_td.GetTestRunStepResponse.make_one(res)

    def get_test_suite(
        self,
        res: "bs_td.GetTestSuiteResponseTypeDef",
    ) -> "dc_td.GetTestSuiteResponse":
        return dc_td.GetTestSuiteResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_test_cases(
        self,
        res: "bs_td.ListTestCasesResponseTypeDef",
    ) -> "dc_td.ListTestCasesResponse":
        return dc_td.ListTestCasesResponse.make_one(res)

    def list_test_configurations(
        self,
        res: "bs_td.ListTestConfigurationsResponseTypeDef",
    ) -> "dc_td.ListTestConfigurationsResponse":
        return dc_td.ListTestConfigurationsResponse.make_one(res)

    def list_test_run_steps(
        self,
        res: "bs_td.ListTestRunStepsResponseTypeDef",
    ) -> "dc_td.ListTestRunStepsResponse":
        return dc_td.ListTestRunStepsResponse.make_one(res)

    def list_test_run_test_cases(
        self,
        res: "bs_td.ListTestRunTestCasesResponseTypeDef",
    ) -> "dc_td.ListTestRunTestCasesResponse":
        return dc_td.ListTestRunTestCasesResponse.make_one(res)

    def list_test_runs(
        self,
        res: "bs_td.ListTestRunsResponseTypeDef",
    ) -> "dc_td.ListTestRunsResponse":
        return dc_td.ListTestRunsResponse.make_one(res)

    def list_test_suites(
        self,
        res: "bs_td.ListTestSuitesResponseTypeDef",
    ) -> "dc_td.ListTestSuitesResponse":
        return dc_td.ListTestSuitesResponse.make_one(res)

    def start_test_run(
        self,
        res: "bs_td.StartTestRunResponseTypeDef",
    ) -> "dc_td.StartTestRunResponse":
        return dc_td.StartTestRunResponse.make_one(res)

    def update_test_case(
        self,
        res: "bs_td.UpdateTestCaseResponseTypeDef",
    ) -> "dc_td.UpdateTestCaseResponse":
        return dc_td.UpdateTestCaseResponse.make_one(res)

    def update_test_configuration(
        self,
        res: "bs_td.UpdateTestConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateTestConfigurationResponse":
        return dc_td.UpdateTestConfigurationResponse.make_one(res)

    def update_test_suite(
        self,
        res: "bs_td.UpdateTestSuiteResponseTypeDef",
    ) -> "dc_td.UpdateTestSuiteResponse":
        return dc_td.UpdateTestSuiteResponse.make_one(res)


apptest_caster = APPTESTCaster()
