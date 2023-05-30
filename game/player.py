#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py
import time

import pygame.sprite

import game


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 4
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.transform.scale(game.assets.PLAYER, (32, 64))
        self.rect = self.image.get_rect()
        self.last_move_time = 0

    def is_blocked(self):
        return game.room.bound_map.get_at((self.rect.x, self.rect.y)) == (0, 0, 0, 255)

    def update(self, *args, **kwargs):
        speed = self.speed
        blocked = self.is_blocked()

        if pygame.K_LCTRL in game.key_pressing or pygame.K_RCTRL in game.key_pressing:
            speed *= 2

        if pygame.K_UP in game.key_pressing or pygame.K_DOWN in game.key_pressing or pygame.K_LEFT in game.key_pressing or pygame.K_RIGHT in game.key_pressing:
            if self.last_move_time <= 0:
                self.last_move_time = time.time()

            move_time = time.time() - self.last_move_time
            ani_state = int(move_time * 1000 / 250) % 2

            if pygame.K_LCTRL in game.key_pressing or pygame.K_RCTRL in game.key_pressing:
                ani_state = int(move_time * 1000 / 125) % 2

            if pygame.K_UP in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_N_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_N_1, (32, 64))

                if self.speed_y < 8:
                    self.speed_y -= speed
            if pygame.K_DOWN in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_S_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_S_1, (32, 64))

                if self.speed_y < 8:
                    self.speed_y += speed
            if pygame.K_LEFT in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_W_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_W_1, (32, 64))

                if self.speed_x < 8:
                    self.speed_x -= speed
            if pygame.K_RIGHT in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_E_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_E_1, (32, 64))

                if self.speed_x < 8:
                    self.speed_x += speed
        else:
            self.last_move_time = 0

        if not blocked:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        else:
            self.speed_x = -self.speed_x
            self.speed_y = -self.speed_y

        self.speed_x = 0
        self.speed_y = 0


INSTANCE = PlayerSprite()
GROUP = pygame.sprite.Group()
GROUP.add(INSTANCE)


def player_tick():
    INSTANCE.update()


def player_render():
    GROUP.draw(game.SURFACE)
