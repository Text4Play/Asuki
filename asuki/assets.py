import pygame.image


def load_image_with_alpha(path):
    buffer = pygame.image.load(path)
    buffer.set_alpha(128)
    return buffer


ICON = load_image_with_alpha("assets/textures/doge.png")
