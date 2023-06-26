#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py

import pygame.display

import game.assets
import game.player
import game.tick
import game.render
import game.room
import game.dialog

SCENE_SIZE = (640, 480)
SURFACE = pygame.display.set_mode(SCENE_SIZE)
CLOCK = pygame.time.Clock()
ROOMS = []

# Raum events Registrieren
game.room.register_event(0, {
    0: lambda: game.player.INSTANCE.fire_dialog(0),
    1: lambda: game.player.INSTANCE.fire_dialog(1),
})
game.room.register_walk_event(0, {
    0: lambda: game.room.switch_room(1, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
})
game.room.register_event(1, {
    0: lambda: game.player.INSTANCE.fire_dialog(1)
})
game.room.register_walk_event(1, {
    0: lambda: game.room.switch_room(0, (SCENE_SIZE[0] - 16 - game.player.INSTANCE.rect.width, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    1: lambda: game.room.switch_room(2, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
})
game.room.register_event(2, {
    0: lambda: {
        game.player.INSTANCE.fire_dialog(0),
        print("1145141919810")
    },
    1: lambda: print("114514")
})
game.room.register_walk_event(2, {
    0: lambda: game.room.switch_room(1, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    1: lambda: game.room.switch_room(1, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
})

# Ein paar variable
running = True
key_pressing = []
current_room = game.room.REGISTERED_ROOMS[0]


# Initialize
def run():
    print("Initializing Pygame...")
    pygame.init()

    pygame.display.set_caption("Game")
    pygame.mouse.set_visible(False)

    loop()

    pygame.display.quit()


# Main loop
def loop():
    while running:
        tick.tick()
        pygame.display.update()

        render.render()
        pygame.display.flip()

        CLOCK.tick(30)
