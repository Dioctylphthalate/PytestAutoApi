#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2021/11/25 23:24
# @Author : 余少琪

import time
from datetime import datetime


def countMilliseconds():
    """
    计算时间
    :return:
    """
    access_start = datetime.now()
    access_end = datetime.now()
    access_delta = (access_end - access_start).seconds * 1000
    return access_delta


def Timestamp_conversion(timeStr: str) -> int:
    """
    时间戳转换，将日期格式转换成时间戳
    :param timeStr: 时间
    :return:
    """

    try:
        datetimeFormat = datetime.strptime(str(timeStr), "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(datetimeFormat.timetuple()) * 1000.0 + datetimeFormat.microsecond / 1000.0)
        return timestamp
    except ValueError:
        raise '日期格式错误, 需要传入得格式为 "%Y-%m-%d %H:%M:%S" '


def Time_conversion(timeNum: int):
    """
    时间戳转换成日期
    :param timeNum:
    :return:
    """
    if isinstance(timeNum, int):
        timeStamp = float(timeNum / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    else:
        raise "请传入正确的时间戳"


def NowTime() -> str:
    """
    获取当前时间, 日期格式: 2021-12-11 12:39:25
    :return:
    """
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


if __name__ == '__main__':
    print(NowTime())
    Time_conversion(1547450538000)
