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


new_yaml = {"fldGuid":"af597696-2e61-11ec-a455-a4bb6d58a26d","fldCreateUser":"autouser","fldCreateDate":"2024-03-05","fldModifyUser":"autouser","fldModifyDate":"2024-03-05","fldTenancy":"","fldCode":"SFFKFS014","fldName":"微信专用","fldAttribute":2,"fldPaymentRefund":0,"fldStatus":1,"fldPrePay":0,"fldPaymentCollection":1,"fldOrder":14,"fldAlias":"","fldUseObjectHouse":1,"fldUseObjectCar":1,"fldUseObjectArea":1,"fldInterest":0,"fldResource":"","fldDownTime":"1900-01-01","fldDisplayOrNot":1,"treeDataGuids":[],"treeUserGuids":[]}


add_dict('auth.yaml',  new_yaml)
