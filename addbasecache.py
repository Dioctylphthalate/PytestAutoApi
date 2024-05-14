#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Author : wangke
# @Time : 2024/4/19 15:51

from flask import Flask, request, jsonify
import yaml
import os
from common.setting import root_path
from flask_cors import CORS
import logging

log = logging.getLogger("monitor.default")
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.debug = True



# 定义一个简单的接口
@app.route('/editcache', methods=['POST'])
def edit_cache():
    # 获取 POST 请求中的 JSON 数据
    req_data = request.form
    req_data = dict(req_data)
    file_path = os.path.join(root_path() + '/common', 'basicinfo.yaml')
    with open(file_path, 'w', encoding='utf-8') as f1:
        yaml.dump(req_data, stream=f1, allow_unicode=True, sort_keys=False)
        print('更新配置成功')
    f1.close()

    # 返回成功消息
    return jsonify({'code': 200, 'message': '数据已更新'})


# POST 接口，用于读取数据
@app.route('/readcache', methods=['POST'])
def read_one_dict():
    file_path = os.path.join(root_path() + '/common', 'basicinfo.yaml')
    with open(file_path, 'r', encoding='utf-8') as f:
        yaml_file = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    response = {
        "code": 200,
        "message": "操作成功",
        "result": yaml_file
    }
    # 将响应转换为 JSON 格式并返回
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=1235)
