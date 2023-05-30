#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py

import pygame


ASSETS = {}


def load_image_with_alpha(path):
    buffer = pygame.image.load(path)
    buffer.set_alpha(256)
    return buffer


PLAYER = load_image_with_alpha("assets/textures/player_new/player.png")
PLAYER_N_0 = load_image_with_alpha("assets/textures/player_new/player_n_0.png")
PLAYER_N_1 = load_image_with_alpha("assets/textures/player_new/player_n_1.png")
PLAYER_S_0 = load_image_with_alpha("assets/textures/player_new/player_s_0.png")
PLAYER_S_1 = load_image_with_alpha("assets/textures/player_new/player_s_1.png")
PLAYER_W_0 = load_image_with_alpha("assets/textures/player_new/player_w_0.png")
PLAYER_W_1 = load_image_with_alpha("assets/textures/player_new/player_w_1.png")
PLAYER_E_0 = load_image_with_alpha("assets/textures/player_new/player_e_0.png")
PLAYER_E_1 = load_image_with_alpha("assets/textures/player_new/player_e_1.png")


def load():
    print("Loading assets...")
    ASSETS["ICON"] = pygame.image.load("assets/icon.png")