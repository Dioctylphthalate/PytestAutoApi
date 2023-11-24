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


new_yaml = {"basePriceVos":[{"fldStartDate":"1900-01-01","fldEndDate":"9999-01-01","fldPrice":"5.00","operationType":1}],"fldTypeName":"测试新增周期性科目","priceUpVos":[],"priceDownVos":[],"fpgModels":[],"ladderVos":[],"fldLadderPeriod":0,"fldObjectType":2,"unitPriceTypeId":"","projectGuid":"540262ecda8d4201a2b3cd6f45db15c2","areaGuid":"67e6da69-8aa2-11ee-af7e-00163e1c1703","upAndDownStatus":False,"setOrdinaryThree":False,"setFpg":False,"fldFuncFormula":"","isChange":0,"disposableProject":{"areaId":"67e6da69-8aa2-11ee-af7e-00163e1c1703","priceId":"","projectId":"540262ecda8d4201a2b3cd6f45db15c2","objectIds":["6986ed1b-8aa2-11ee-af7e-00163e1c1703"]}}





add_dict('auth.yaml',  new_yaml)




