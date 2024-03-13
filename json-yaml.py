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


new_yaml = {"dataFreshness":2,"excludeZero":False,"nodeTypename":"项目","nodeTypeGuid":"info","copyfldAreaGuid":[{"id":"7fc3e9c2-e114-11ee-9935-00163e251185","fldGuid":"5b131245-a387-177d-d212-0fe66addceee","fldPguid":"c318035c08fa45e7981cdb6e0cb8d774","fldTypeKey":"area","fldName":"麓山国际","fldTypeName":"项目","fldOrder":2,"nodeType":0,"fldCode":"0013022010202","children":[],"holidayStatus":'',"fldStatus":1,"fldAssemblyName":'',"hasRight":1,"addSlotShow":False,"show":False}],"copyfldObjectList":[],"copyfldowlist":[],"copyProjectList":[],"modelType":3,"fldExcludeFee":[4],"fldAreaGuid":["5b131245-a387-177d-d212-0fe66addceee"],"fldObjectList":[],"fldOwnerList":[],"fldProjectList":[],"timeType":0,"chargeDate":'',"fldStartDate":"","fldEndDate":"","fldStatisticsDate":"","fldLiveType":[],"fldIsBeforeFee":True,"exclude":False,"fldAttribute":[],"queryId":"","fldGarageList":[],"pageIndex":1,"pageSize":100}

add_dict('auth.yaml',  new_yaml)
