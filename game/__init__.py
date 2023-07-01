#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 Ruifeng Du All Rights Reserved.
# 
# @Author   : Ruifeng Du
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
# Es gibt normale Events und Lauf-event
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
        game.player.INSTANCE.fire_dialog(2)
    },
})
game.room.register_walk_event(2, {
    0: lambda: game.room.switch_room(1, (SCENE_SIZE[0] - 16 - game.player.INSTANCE.rect.width, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2 - 96)),
    1: lambda: game.room.switch_room(3, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    2: lambda: game.room.switch_room(4, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
})

game.room.register_event(3, {
    0: lambda: game.player.INSTANCE.fire_dialog(3),
    1: lambda: game.player.INSTANCE.fire_dialog(4)
})
game.room.register_walk_event(3, {
    0: lambda: game.room.switch_room(2, (SCENE_SIZE[0] / 2 - game.player.INSTANCE.rect.width / 2, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2 - 96))
})

game.room.register_event(4, {
})
game.room.register_walk_event(4, {
    0: lambda: game.room.switch_room(2, (SCENE_SIZE[0] - 16 - game.player.INSTANCE.rect.width, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    1: lambda: game.room.switch_room(5, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
})

game.room.register_event(5, {
})
game.room.register_walk_event(5, {
    0: lambda: game.room.switch_room(4, (SCENE_SIZE[0] - 16 - game.player.INSTANCE.rect.width, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    1: lambda: game.room.switch_room(6, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
})

game.room.register_event(6, {
})
game.room.register_walk_event(6, {
    0: lambda: game.room.switch_room(5, (SCENE_SIZE[0] - 16 - game.player.INSTANCE.rect.width, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    1: lambda: game.room.switch_room(7, (16, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2 + 64))
})

game.room.register_event(7, {
    0: lambda: {
        player.INSTANCE.fire_dialog(233),
        game.room.switch_room(0, (SCENE_SIZE[0] / 2 - game.player.INSTANCE.rect.width / 2, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2))
    }
})
game.room.register_walk_event(7, {
    0: lambda: game.room.switch_room(6, (SCENE_SIZE[0] - 16 - game.player.INSTANCE.rect.width, SCENE_SIZE[1] / 2 - game.player.INSTANCE.rect.height / 2)),
    1: lambda: print("You Won!"),
    2: lambda: print("You Won!")
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

    # Loop
    loop()

    # Destroy
    pygame.display.quit()


# Main loop
def loop():
    # Jeder 1/30 Sekunde ein mal update
    while running:
        # Update
        tick.tick()
        pygame.display.update()

        # Render
        render.render()
        pygame.display.flip()

        CLOCK.tick(30)
