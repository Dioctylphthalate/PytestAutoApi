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


case_id = ['addbasic_01', 'addbasic_02', 'addbasic_03', 'addbasic_04', 'addbasic_05', 'addbasic_06', 'addbasic_07']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("测试平台接口")
@allure.feature("基础中台模块")
class TestAddbasicinfo:

    @allure.story("基础中台接口")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_AddBasicInfo(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_AddBasicInfo.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
