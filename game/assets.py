#!/user/bin/python3
# _*_ coding: utf-8 _*_
# 
# Copyright (C) 2023 Ruifeng Du All Rights Reserved.
# 
# @Author   : Ruifeng Du
# @File     : &{NAME}.py

import pygame


def load_image_with_alpha(path):
    buffer = pygame.image.load(path)
    buffer.set_alpha(255)
    return buffer

# Die Ressourcen
pygame.font.init()
UNIFONT_12 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 12)
UNIFONT_14 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 14)
UNIFONT_16 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 16)
UNIFONT_20 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 20)
UNIFONT_24 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 24)
UNIFONT_32 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 32)

PLAYER_RES_ROOT = "assets/textures/boc/"
PLAYER = load_image_with_alpha(f"{PLAYER_RES_ROOT}player.png")
PLAYER_N_0 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_n_0.png")
PLAYER_N_1 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_n_1.png")
PLAYER_S_0 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_s_0.png")
PLAYER_S_1 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_s_1.png")
PLAYER_W_0 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_w_0.png")
PLAYER_W_1 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_w_1.png")
PLAYER_E_0 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_e_0.png")
PLAYER_E_1 = load_image_with_alpha(f"{PLAYER_RES_ROOT}player_e_1.png")

DIALOG_BG = load_image_with_alpha("assets/textures/dialog_bg.png")
