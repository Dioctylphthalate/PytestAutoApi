#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024-03-22 11:19:05


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['summary_list', 'project_summary_list', 'item_subject_summary_list', 'item_charge_method_list', 'resource_schedule_list', 'owner_detail__list', 'owner_resource_detail', 'bill_detail', 'checklist_detail']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("测试平台接口")
@allure.feature("报表模块")
class TestPaidreport:

    @allure.story("实收报表")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_PaidReport(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_PaidReport.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
