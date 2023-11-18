#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2022/6/2 11:30
# @Author  : YRGS
# @Email   : 1603453211@qq.com
# @File    : set_current_request_cache
# @describe:
"""
import json
from typing import Text
from jsonpath import jsonpath
from utils.other_tools.exceptions import ValueNotFoundError
from utils.cache_process.cache_control import CacheHandler


class SetCurrentRequestCache:
    """将用例中的请求或者响应内容存入缓存"""

    def __init__(self, current_request_set_cache, request_data, response_data):
        self.current_request_set_cache = current_request_set_cache
        self.request_data = request_data
        self.response_data = response_data.text

    def _update_cache(self, value, cache_name):
        """更新缓存"""
        CacheHandler.update_cache(cache_name=cache_name, value=value)

    def _get_jsonpath_value(self, data, jsonpath_value):
        """根据 JSONPath 获取值"""
        result = jsonpath(data, jsonpath_value)
        if result is not False:
            return result[0]
        else:
            raise ValueNotFoundError(
                "缓存设置失败，程序中未检测到需要缓存的数据。"
                f"请求参数: {data}"
                f"提取的 JSONPath 内容: {jsonpath_value}"
            )

    def set_request_cache(self, jsonpath_value, cache_name):
        """将接口的请求参数存入缓存"""
        request_value = self._get_jsonpath_value(self.request_data, jsonpath_value)
        self._update_cache(request_value, cache_name)

    def set_response_cache(self, jsonpath_value, cache_name):
        """将响应结果存入缓存"""
        response_value = self._get_jsonpath_value(json.loads(self.response_data), jsonpath_value)
        self._update_cache(response_value, cache_name)

    def set_caches_main(self):
        """设置缓存"""
        if self.current_request_set_cache is not None:
            for item in self.current_request_set_cache:
                jsonpath_value = item.jsonpath
                cache_name = item.name
                cache_list = item.cache_list

                if cache_list:
                    values = []
                    response_json = json.loads(self.response_data)
                    for match in jsonpath(response_json, jsonpath_value):
                        for entry in match:
                            value = entry.get(cache_list)
                            if value:
                                values.append(value)
                    if item.type == 'request':
                        self.set_request_cache(values, cache_name)
                    elif item.type == 'response':
                        self._update_cache(values, cache_name)
                else:
                    if item.type == 'request':
                        self.set_request_cache(jsonpath_value, cache_name)
                    elif item.type == 'response':
                        self.set_response_cache(jsonpath_value, cache_name)