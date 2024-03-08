#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024-03-08 09:35:06


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['batchbilling-01', 'batchbilling-02', 'batchbilling_03']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("测试平台接口")
@allure.feature("批量计费模块")
class TestBatchbilling:

    @allure.story("批量计费接口")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_BatchBilling(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_BatchBilling.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
