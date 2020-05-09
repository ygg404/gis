#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/08 09:59
# @Author  : YGG
# @File    : ShortUuid.py
# @Description:

import uuid


def short_uuid():
    uuidChars = ("a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
             "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
             "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z")

    uuidstr = str(uuid.uuid4()).replace('-', '')
    result = ''
    for i in range(0,8):
        sub = uuidstr[i * 4: i * 4 + 4]
        x = int(sub,16)
        result += uuidChars[x % 0x3E]
    return result