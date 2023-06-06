#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 岚风Arrokoth All Rights Reserved.
# 
# @Author   : 岚风Arrokoth
# @File     : &{NAME}.py

import pygame


def load_image_with_alpha(path):
    buffer = pygame.image.load(path)
    buffer.set_alpha(255)
    return buffer

pygame.font.init()
UNIFONT_16 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 16)
UNIFONT_20 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 20)
UNIFONT_24 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 24)

PLAYER = load_image_with_alpha("assets/textures/player_new/player.png")
PLAYER_N_0 = load_image_with_alpha("assets/textures/player_new/player_n_0.png")
PLAYER_N_1 = load_image_with_alpha("assets/textures/player_new/player_n_1.png")
PLAYER_S_0 = load_image_with_alpha("assets/textures/player_new/player_s_0.png")
PLAYER_S_1 = load_image_with_alpha("assets/textures/player_new/player_s_1.png")
PLAYER_W_0 = load_image_with_alpha("assets/textures/player_new/player_w_0.png")
PLAYER_W_1 = load_image_with_alpha("assets/textures/player_new/player_w_1.png")
PLAYER_E_0 = load_image_with_alpha("assets/textures/player_new/player_e_0.png")
PLAYER_E_1 = load_image_with_alpha("assets/textures/player_new/player_e_1.png")

DIALOG_BG = load_image_with_alpha("assets/textures/dialog_bg.png")