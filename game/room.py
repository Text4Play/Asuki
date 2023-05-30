#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py
import pygame.image

import game.assets


class Room(object):
    def __init__(self, room_id):
        self.color_map = game.assets.load_image_with_alpha(f"assets/textures/room/{room_id}/color_map.png")
        self.bound_map = game.assets.load_image_with_alpha(f"assets/textures/room/{room_id}/bound_map.png")
        self.sfx_map = game.assets.load_image_with_alpha(f"assets/textures/room/{room_id}/sfx_map.png")
        self.event_map = game.assets.load_image_with_alpha(f"assets/textures/room/{room_id}/event_map.png")

