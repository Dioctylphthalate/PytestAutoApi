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


new_yaml = {"bankPayAccountModel":'',"fldAreaGuid":"5b131245-a387-177d-d212-0fe66addceee","fldObjectId":"7901af1f-8b60-b706-4b33-5522c3047121","fldImmigrationTime":"","fldIsOwner":0,"newAddBillModel":[],"ownerInfomationRelationOwnerVos":[{"fldType":1,"fldContent":"13546356354","fldAreaGuid":"5b131245-a387-177d-d212-0fe66addceee"}],"fldRelation":"1级","naturalPersonModel":{"fldCardNum":"","fldCardType":"","fldBirthday":"","fldSex":"","fldNation":"","fldMarriage":"","fldEducation":"","fldName":"赵钱孙李","fldType":1},"legalPersonModel":'null',"fldOwnerGuid":"ae683f51-3d38-92b9-dbfe-b7dd78ccdea7","fldPhotoGuid":"","fldDesc":""}




add_dict('auth.yaml',  new_yaml)