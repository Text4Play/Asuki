#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py
import pygame.display

import game
import game.player


def tick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            game.key_pressing.append(event.key)
        if event.type == pygame.KEYUP:
            if event.key in game.key_pressing:
                game.key_pressing.remove(event.key)

    game.player.player_tick()
