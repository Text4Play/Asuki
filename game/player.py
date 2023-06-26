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


# Hit box
def is_blocked(x, y, w, h):
    def is_hit(x, y):
        return game.current_room.bound_map.get_at((x, y))[0] == 255

    if x < 1 or x + w + 1 > game.current_room.bound_map.get_size()[0] or y < 1 or y + h + 1 > \
            game.current_room.bound_map.get_size()[1]:
        return True

    return is_hit(x, y) or is_hit(x + w, y) or is_hit(x, y + h) or is_hit(x + w, y + h)


# Spieler klasse
class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.size = (48, 96)
        self.speed = 4
        self.image = pygame.transform.scale(game.assets.PLAYER, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = (640 / 2.0) - (self.size[0] / 2.0)
        self.rect.y = (480 / 2.0) - (self.size[1] / 2.0)
        self.last_move_time = 0
        self.talking = False
        self.session = None
        self.session_index = 0
        self.talking_text = ""

    def is_blocked(self):
        return is_blocked(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    # Bewegung
    def movement(self):
        speed = self.speed

        direction_x = 0
        direction_y = 0

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
                    self.image = pygame.transform.scale(game.assets.PLAYER_N_0, self.size)
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_N_1, self.size)

                direction_y = -1
            if pygame.K_DOWN in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_S_0, self.size)
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_S_1, self.size)

                direction_y = 1
            if pygame.K_LEFT in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_W_0, self.size)
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_W_1, self.size)

                direction_x = -1
            if pygame.K_RIGHT in game.key_pressing:
                if ani_state == 0:
                    self.image = pygame.transform.scale(game.assets.PLAYER_E_0, self.size)
                else:
                    self.image = pygame.transform.scale(game.assets.PLAYER_E_1, self.size)

                direction_x = 1
        else:
            self.last_move_time = 0

        self.rect.x += speed * direction_x
        if self.is_blocked():
            self.rect.x -= speed * direction_x

        self.rect.y += speed * direction_y
        if self.is_blocked():
            self.rect.y -= speed * direction_y

    # Update
    def update(self, *args, **kwargs):
        if self.session is None:
            self.talking = False

        if not self.talking:
            self.movement()
        
        game.current_room.call_move_event(self.rect)

    # Event calling
    def key_down(self, key):
        if not self.talking:
            if key == pygame.K_z:
                game.current_room.call_event(self.rect)
        else:
            if key == pygame.K_z:
                if len(self.session) <= self.session_index:
                    self.talking = False
                else:
                    self.dialog()
                    self.session_index += 1
    
    def fire_dialog(self, index):
        self.talking = True
        self.session = game.dialog.read(index)
        self.session_index = 0
        self.dialog()
        self.session_index += 1
    
    def dialog(self):
        name = self.session[self.session_index][0]
        text = self.session[self.session_index][1]
        self.talking_text = f"{name}\\n{text}"
    
    def render_dialog(self, surface):
        img = pygame.transform.scale(game.assets.DIALOG_BG, (560, 175))
        padding = (game.SCENE_SIZE[0] - img.get_width()) / 2
        surface.blit(img, (int(padding), int(game.SCENE_SIZE[1] - img.get_height() - padding)))
        j = 0
        for i in self.talking_text.split("\\n"):
            text = None
            if j == 0:
                text = game.assets.UNIFONT_24.render(i, True, pygame.color.Color(255, 255, 255))
            else:
                text = game.assets.UNIFONT_20.render(i, True, pygame.color.Color(255, 255, 255))
            surface.blit(text, (int(padding) + 16 + min(1, j) * 12, int(game.SCENE_SIZE[1] - img.get_height() - padding) + 12 + min(1, j) * 8 + (j * 20)))
            j += 1


# Ein paar variable
INSTANCE = PlayerSprite()
GROUP = pygame.sprite.Group()
GROUP.add(INSTANCE)


def player_tick():
    INSTANCE.update()


def player_render():
    GROUP.draw(game.SURFACE)
    if INSTANCE.talking:
        INSTANCE.render_dialog(game.SURFACE)
