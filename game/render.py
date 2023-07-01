#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 Ruifeng Du All Rights Reserved.
# 
# @Author   : Ruifeng Du
# @File     : &{NAME}.py

import game.player


debug_mode = 0


# Zeichnen
def render():
    # Hintergrund Farbe
    game.SURFACE.fill((0, 0, 0))

    # Hintergrund bild
    game.SURFACE.blit(game.current_room.color_map, (0, 0))

    # Debug
    if debug_mode == 1:
        game.SURFACE.blit(game.current_room.bound_map, (0, 0))
    elif debug_mode == 2:
        game.SURFACE.blit(game.current_room.event_map, (0, 0))
    elif debug_mode == 3:
        game.SURFACE.blit(game.current_room.sfx_map, (0, 0))

    # Spieler
    game.player.player_render()
