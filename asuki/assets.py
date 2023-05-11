import pygame.image


def load_image_with_alpha(path):
    buffer = pygame.image.load(path)
    buffer.set_alpha(256)
    return buffer


ICON = load_image_with_alpha("assets/textures/doge.png")
PLAYER = load_image_with_alpha("assets/textures/player/player.png")
PLAYER_N = load_image_with_alpha("assets/textures/player/player_n.png")
PLAYER_S = load_image_with_alpha("assets/textures/player/player_s.png")
PLAYER_W = load_image_with_alpha("assets/textures/player/player_w.png")
PLAYER_E = load_image_with_alpha("assets/textures/player/player_e.png")

pygame.font.init()
UNIFONT_14 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 14)
UNIFONT_24 = pygame.font.Font("assets/font/unifont-15.0.01.ttf", 24)
