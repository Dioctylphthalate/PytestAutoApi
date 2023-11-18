#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/3/30 14:12
# @Author : YRGS
import pytest
import time
import allure
import requests
import ast
import json
import os

import yaml

from common.setting import ensure_path_sep
from utils.requests_tool.request_control import cache_regular
from utils.logging_tool.log_control import INFO, ERROR, WARNING
from utils.other_tools.models import TestCase
from utils.read_files_tools.clean_files import del_file
from utils.other_tools.allure_data.allure_tools import allure_step, allure_step_no
from utils.cache_process.cache_control import CacheHandler


@pytest.fixture(scope="session", autouse=True)
def clear_report():
    """如clean命名无法删除报告，这里手动删除"""
    del_file(ensure_path_sep("\\report"))


@pytest.fixture(scope="session", autouse=True)
def work_login_init():
    """
    获取登录的cookie
    :return:
    """

    url = "http://39.103.156.18:66/api/auth/oauth/token"
    data = {
        "grant_type": "password",
        "username": "xXCyGNhXS23YpIdfE/PrHw==",
        "password": "xXCyGNhXS23YpIdfE/PrHw=="
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Basic ZWFzeXNvZnQ6ZWFzeXNvZnQ="}
    # 请求登录接口
    res = requests.post(url=url, params=data, verify=True, headers=headers)
    response_cookie = json.loads(res.content)
    cookies = ''
    k = response_cookie["token_type"]
    v = response_cookie["access_token"]
    _cookie = k + " " + v
    # 拿到登录的cookie内容，cookie拿到的是字典类型，转换成对应的格式
    cookies += _cookie
    # 将登录接口中的cookie写入缓存中，其中Authorization是缓存名称
    CacheHandler.update_cache(cache_name='Authorization', value=cookies)

@pytest.fixture(scope="session", autouse=True)
def pre_cache():
    """
    存入所有提前需要的缓存值
    :return:
    """
    config_path = os.path.dirname(os.path.dirname(__file__)) + '/common'
    file_path = os.path.join(config_path, 'basicinfo.yaml')
    with open(file_path, 'r', encoding='utf-8') as f:
        yaml_file = yaml.load(f, Loader=yaml.FullLoader)
        for key in yaml_file:
            CacheHandler.update_cache(cache_name=key, value=yaml_file[key])

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的 item 的 name 和 node_id 的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

    # 期望用例顺序
    # print("收集到的测试用例:%s" % items)
    appoint_items = ["test_login", "test_AddBasicInfo", "test_OwnerGuidFee_all"]    # test_case 文件夹中的测试用例文件运行顺序

    # 指定运行顺序
    run_items = []
    for i in appoint_items:
        for item in items:
            module_item = item.name.split("[")[0]
            if i == module_item:
                run_items.append(item)

    for i in run_items:
        run_index = run_items.index(i)
        items_index = items.index(i)

        if run_index != items_index:
            n_data = items[run_index]
            run_index = items.index(n_data)
            items[items_index], items[run_index] = items[run_index], items[items_index]


def pytest_configure(config):
    config.addinivalue_line("markers", 'smoke')
    config.addinivalue_line("markers", '回归测试')


@pytest.fixture(scope="function", autouse=True)
def case_skip(in_data):
    """处理跳过用例"""
    in_data = TestCase(**in_data)
    if ast.literal_eval(cache_regular(str(in_data.is_run))) is False:
        allure.dynamic.title(in_data.detail)
        allure_step_no(f"请求URL: {in_data.is_run}")
        allure_step_no(f"请求方式: {in_data.method}")
        allure_step("请求头: ", in_data.headers)
        allure_step("请求数据: ", in_data.data)
        allure_step("依赖数据: ", in_data.dependence_case_data)
        allure_step("预期数据: ", in_data.assert_data)
        pytest.skip()


def pytest_terminal_summary(terminalreporter):
    """
    收集测试结果
    """

    _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    _TOTAL = terminalreporter._numcollected
    _TIMES = time.time() - terminalreporter._sessionstarttime
    INFO.logger.info(f"用例总数: {_TOTAL}")
    if _ERROR != 0:
        INFO.logger.error(f"异常用例数: {_ERROR}")
    else:
        INFO.logger.info(f"异常用例数: {_ERROR}")
    if _FAILED != 0:
        ERROR.logger.error(f"失败用例数: {_FAILED}")
    else:
        INFO.logger.info(f"失败用例数: {_FAILED}")
    if _SKIPPED != 0:
        WARNING.logger.warning(f"跳过用例数: {_SKIPPED}")
    else:
        WARNING.logger.info(f"跳过用例数: {_SKIPPED}")
    INFO.logger.info("用例执行时长: %.2f" % _TIMES + " s")

    try:
        _RATE = _PASSED / _TOTAL * 100
        INFO.logger.info("用例成功率: %.2f" % _RATE + " %")
    except ZeroDivisionError:
        INFO.logger.info("用例成功率: 0.00 %")
