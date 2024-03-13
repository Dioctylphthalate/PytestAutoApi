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


new_yaml = {"nodeTypeGuid":"info","exclude":False,"fldAreaGuid":["5b131245-a387-177d-d212-0fe66addceee"],"fldAttribute":[],"fldEndDate":"","fldExcludeFee":[4],"fldExcludeQiFei":False,"fldIsBeforeFee":True,"fldLiveType":[],"fldObjectList":[],"fldOwnerList":[],"fldProjectList":[],"fldStartDate":"","fldStatisticsDate":"","operatorDate":"","income":False,"incomeSource":False,"isPage":False,"memoryAdr":"","modelType":0,"pageIndex":0,"pageSize":100,"projectMode":0,"selectDate":"2024-2","selectType":2,"timeType":0,"excludeZero":False}





add_dict('auth.yaml',  new_yaml)
