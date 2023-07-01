#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 Ruifeng Du All Rights Reserved.
# 
# @Author   : Ruifeng Du
# @File     : &{NAME}.py

import pygame.image

import game.assets
import game.player

REGISTERED_ROOMS = {}


# Hier kann man den raum aehndern
def switch_room(index, pos):
    game.player.INSTANCE.rect.x = pos[0]
    game.player.INSTANCE.rect.y = pos[1]
    game.current_room = REGISTERED_ROOMS[index]


# Raum klasse
class Room(object):
    # __init__ funktion, Lädt die Textures
    def __init__(self, index):
        self.color_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/color_map.png"), (640, 480))
        self.bound_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/bound_map.png"), (640, 480))
        # Unused
        self.sfx_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/sfx_map.png"), (640, 480))
        self.event_map = pygame.transform.scale(
            game.assets.load_image_with_alpha(f"assets/textures/room/{index}/event_map.png"), (640, 480))
        self.events = []
        self.walk_events = []

    # Event system
    # Der Spieler drückt 'Z'
    def add_event(self, index, event):
        while len(self.events) - 1 < index:
            self.events.append(None)
        self.events[index] = event

    # Der Spieler läuft
    def add_walk_event(self, index, event):
        while len(self.walk_events) - 1 < index:
            self.walk_events.append(None)
        self.walk_events[index] = event

    # Der Spieler drückt 'Z'
    def call_event(self, rect):
        color = self.event_map.get_at((int(rect.x + rect.width / 2), int(rect.y + rect.height / 2)))
        if color[0] == 255:
            self.events[color[1]]()

    # Der Spieler läuft
    def call_move_event(self, rect):
        color = self.event_map.get_at((int(rect.x + rect.width / 2), int(rect.y + rect.height / 2)))
        if color[0] == 127:
            self.walk_events[color[1]]()


# Event system
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
