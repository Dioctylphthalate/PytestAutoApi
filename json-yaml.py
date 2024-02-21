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


new_yaml = {"fldAreaGuid":"5b131245-a387-177d-d212-0fe66addceee","fldOwnerGuid":"9fff6e05e5d049bba970489f4816a4a7","fldPublicGuid":"","fldCurObjectGuid":"6231df584a994a56b164e2bb48374f5f","fldSelObjectGuidList":["6231df584a994a56b164e2bb48374f5f"]}



add_dict('auth.yaml',  new_yaml)
