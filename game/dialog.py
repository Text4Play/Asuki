#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 Ruifeng Du All Rights Reserved.
# 
# @Author   : Ruifeng Du
# @File     : &{NAME}.py


def read(index):
    dialogs = []
    text = open(f"assets/text/dialog_{index}.txt").read()
    for i in text.splitlines():
        dialogs.append((i[0:i.find(':')],i[i.find(':') + 1:len(i)]))
    return dialogs
