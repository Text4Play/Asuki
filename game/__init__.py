#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py
import pygame.display

import game.assets
import game.tick
import game.render
import game.room

SCENE_SIZE = (640, 480)
SURFACE = pygame.display.set_mode(SCENE_SIZE)
CLOCK = pygame.time.Clock()
ROOMS = []

game.room.register(0, {
    0: lambda: game.room.switch_room(1, (1, 1)),
    1: lambda: print("1145141919810")
})
game.room.register(1, {
    0: lambda: game.room.switch_room(0, (1, 1)),
    1: lambda: print("1145141919810")
})

running = True
key_pressing = []
current_room = game.room.REGISTERED_ROOMS[0]


def run():
    print("Initializing Pygame...")
    pygame.init()

    pygame.display.set_caption("Asuki")
    pygame.mouse.set_visible(False)

    loop()

    pygame.display.quit()


def loop():
    while running:
        tick.tick()
        pygame.display.update()

        render.render()
        pygame.display.flip()

        CLOCK.tick(30)


def change_room(target_room, pos):
    print(pos[0], pos[1])
