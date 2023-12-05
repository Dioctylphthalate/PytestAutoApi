#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Author : wangke
# @Time : 2023/10/26 14:31
import os
import yaml
from common.setting import root_path


def add_dict(filename, new_yaml):
    file_path = os.path.join(root_path() + '/common', filename)
    with open(file_path, 'w', encoding='utf-8') as f1:
        yaml.dump(new_yaml, stream=f1, allow_unicode=True, sort_keys=False)
        print('更新配置成功')
    f1.close()
    return new_yaml


new_yaml = {"dinfoGuid":"7137330045541945344","infoGuid":"","keys":"batchBilling","domainGuid":"4a358d7af3e44777a14c80ba0cfe0115","operatorGuid":"易软王科","taList":[],"valueGuid":"${ttt}","businessTitle":""}




add_dict('auth.yaml',  new_yaml)




