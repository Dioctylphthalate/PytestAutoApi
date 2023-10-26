#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Author : wangke
# @Time : 2023/10/26 14:31
import os
import yaml


def add_dict(filename, new_yaml):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/Config', filename)
    with open(file_path, 'w', encoding='utf-8') as f1:
        yaml.dump(new_yaml, stream=f1, allow_unicode=True, sort_keys=False)
        print('更新配置成功')
    f1.close()
    return new_yaml


new_yaml = {"bankPayAccountModel":"","fldAreaGuid":"33734acda31f4c1888771a04d11efa26","fldObjectId":"5c73116893c84bc4bf21b6c31e232642","fldImmigrationTime":"","fldIsOwner":0,"newAddBillModel":[],"ownerInfomationRelationOwnerVos":[],"fldRelation":"","naturalPersonModel":{"fldCardNum":"","fldCardType":"","fldBirthday":"","fldSex":"","fldNation":"","fldMarriage":"","fldEducation":"","fldName":"sdff","fldType":1},"legalPersonModel":"","fldOwnerGuid":"0a031367-0ca0-0a9f-494c-725c9034a003","fldPhotoGuid":"","fldDesc":""}
add_dict('auth.yaml',  new_yaml)