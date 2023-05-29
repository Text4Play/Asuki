import math
import time

import pygame.sprite

import asuki.assets
import asuki.game


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 4
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.transform.scale(asuki.assets.PLAYER, (32, 64))
        self.rect = self.image.get_rect()
        self.last_move_time = 0

    def update(self, *args, **kwargs):
        speed = self.speed
        if pygame.K_LCTRL in asuki.game.keys_pressing or pygame.K_RCTRL in asuki.game.keys_pressing:
            speed *= 2

        if pygame.K_UP in asuki.game.keys_pressing or pygame.K_DOWN in asuki.game.keys_pressing or pygame.K_LEFT in asuki.game.keys_pressing or pygame.K_RIGHT in asuki.game.keys_pressing:
            if self.last_move_time <= 0:
                self.last_move_time = time.time()

            move_time = time.time() - self.last_move_time
            ani_state = int(move_time * 1000 / 250) % 2

            if pygame.K_LCTRL in asuki.game.keys_pressing or pygame.K_RCTRL in asuki.game.keys_pressing:
                ani_state = int(move_time * 1000 / 125) % 2

            if pygame.K_UP in asuki.game.keys_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_N_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_N_1, (32, 64))

                if self.speed_y < 8:
                    self.speed_y -= speed
            if pygame.K_DOWN in asuki.game.keys_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_S_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_S_1, (32, 64))

                if self.speed_y < 8:
                    self.speed_y += speed
            if pygame.K_LEFT in asuki.game.keys_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_W_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_W_1, (32, 64))

                if self.speed_x < 8:
                    self.speed_x -= speed
            if pygame.K_RIGHT in asuki.game.keys_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_E_0, (32, 64))
                else:
                    self.image = pygame.transform.scale(asuki.assets.PLAYER_E_1, (32, 64))

                if self.speed_x < 8:
                    self.speed_x += speed
        else:
            self.last_move_time = 0

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.speed_x = 0
        self.speed_y = 0
