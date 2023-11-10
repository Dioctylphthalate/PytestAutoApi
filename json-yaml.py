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


new_yaml = {"fldAreaGuid":"5b131245-a387-177d-d212-0fe66addceee","fldOwnerGuid":"662713c0ae234105b7cdeff075777a82","fldSelObjectGuidList":["ded164b2a2904e218ebe15005713fb95"]}
add_dict('auth.yaml',  new_yaml)