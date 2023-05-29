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


WINDOW = pygame.display.set_mode((640, 480))
CLOCK = pygame.time.Clock()

running = True


def run():
    pygame.init()
    assets.load()

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

