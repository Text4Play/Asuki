#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py

import pygame.display

import game.player


debug_mode = 0


def render():
    game.SURFACE.fill((0, 0, 0))

    game.SURFACE.blit(game.current_room.color_map, (0, 0))

    if debug_mode == 1:
        game.SURFACE.blit(game.current_room.bound_map, (0, 0))
    elif debug_mode == 2:
        game.SURFACE.blit(game.current_room.event_map, (0, 0))
    elif debug_mode == 3:
        game.SURFACE.blit(game.current_room.sfx_map, (0, 0))

    game.player.player_render()
