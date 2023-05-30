#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py
import pygame.display

import game.player


def render():
    game.SURFACE.fill((0, 0, 0))

    game.SURFACE.blit(game.room.color_map, (0, 0))

    game.player.player_render()
