import math

import pygame.sprite

import asuki.assets
import asuki.game


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 8
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.transform.scale(asuki.assets.PLAYER, (32, 32))
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        if pygame.K_w in asuki.game.keys_pressing or pygame.K_s in asuki.game.keys_pressing or pygame.K_a in asuki.game.keys_pressing or pygame.K_d in asuki.game.keys_pressing:
            if pygame.K_w in asuki.game.keys_pressing:
                self.image = pygame.transform.scale(asuki.assets.PLAYER_N, (32, 32))
                if self.speed_y < 8:
                    self.speed_y -= self.speed
            if pygame.K_s in asuki.game.keys_pressing:
                self.image = pygame.transform.scale(asuki.assets.PLAYER_S, (32, 32))
                if self.speed_y < 8:
                    self.speed_y += self.speed
            if pygame.K_a in asuki.game.keys_pressing:
                self.image = pygame.transform.scale(asuki.assets.PLAYER_W, (32, 32))
                if self.speed_x < 8:
                    self.speed_x -= self.speed
            if pygame.K_d in asuki.game.keys_pressing:
                self.image = pygame.transform.scale(asuki.assets.PLAYER_E, (32, 32))
                if self.speed_x < 8:
                    self.speed_x += self.speed
        else:
            self.image = pygame.transform.scale(asuki.assets.PLAYER, (32, 32))

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.speed_x *= 0
        self.speed_y *= 0
