#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py

import pygame


ASSETS = {}


def load():
    print("Loading assets...")
    ASSETS["ICON"] = pygame.image.load("assets/icon.png")
