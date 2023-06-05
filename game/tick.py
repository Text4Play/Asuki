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
            game.player.INSTANCE.key_down(event.key)
            if event.key == pygame.K_F1:
                game.render.debug_mode = 1
            elif event.key == pygame.K_F2:
                game.render.debug_mode = 2
            elif event.key == pygame.K_F3:
                game.render.debug_mode = 3
            elif event.key == pygame.K_F4:
                game.render.debug_mode = 0
        if event.type == pygame.KEYUP:
            if event.key in game.key_pressing:
                game.key_pressing.remove(event.key)

    game.player.player_tick()
