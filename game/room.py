#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py
import pygame.image

import game.assets
import game.player


REGISTERED_ROOMS = {}


def switch_room(index, pos):
    game.player.INSTANCE.rect.x = pos[0]
    game.player.INSTANCE.rect.y = pos[1]
    game.current_room = REGISTERED_ROOMS[index]


class Room(object):
    def __init__(self, index):
        self.color_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/color_map.png"), (640, 480))
        self.bound_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/bound_map.png"), (640, 480))
        self.sfx_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/sfx_map.png"), (640, 480))
        self.event_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/event_map.png"), (640, 480))
        self.events = []
        self.walk_events = []

    def add_event(self, index, event):
        while len(self.events) - 1 < index:
            self.events.append(None)
        self.events[index] = event

    def add_walk_event(self, index, event):
        while len(self.walk_events) - 1 < index:
            self.walk_events.append(None)
        self.walk_events[index] = event

    def call_event(self, rect):
        color = self.event_map.get_at((int(rect.x + rect.width / 2), int(rect.y + rect.height / 2)))
        if color[0] == 255:
            self.events[color[1]]()

    def call_move_event(self, rect):
        color = self.event_map.get_at((int(rect.x + rect.width / 2), int(rect.y + rect.height / 2)))
        if color[0] == 127:
            self.walk_events[color[1]]()


def register_event(index, events):
    try:
        room = REGISTERED_ROOMS[index]
    except:
        room = Room(index)
    
    for e in events.keys():
        room.add_event(e, events[e])
    REGISTERED_ROOMS[index] = room
    return room


def register_walk_event(index, events):
    try:
        room = REGISTERED_ROOMS[index]
    except:
        room = Room(index)
    
    for e in events.keys():
        room.add_walk_event(e, events[e])
    REGISTERED_ROOMS[index] = room
    return room
