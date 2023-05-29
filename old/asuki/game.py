import threading
import time

import asuki.objects.gameobject
import asuki.assets
import asuki.player
import pygame

# Update and Render are separated
keys_pressing = []
running = True
surface: pygame.Surface

player = asuki.player.PlayerSprite()
sprites = pygame.sprite.Group()


def init():
    global surface

    sprites.add(player)

    pygame.init()
    pygame.font.init()

    surface = pygame.display.set_mode((640, 480))
    pygame.display.init()
    pygame.display.set_caption("Game")
    pygame.display.set_icon(asuki.assets.ICON)
    pygame.mouse.set_visible(False)


def loop():
    global running

    thread = threading.Thread(target=render_loop)
    thread.start()

    update_loop()

    thread.join(0)
    pygame.display.quit()


def render_loop():
    clock = pygame.time.Clock()
    fps = 0
    fps_buffer = 0
    timer = get_time()
    global running
    while running:
        surface.fill((127, 0, 0))
        render()
        fps_buffer += 1
        if get_time() - timer >= 1000:
            fps = fps_buffer
            fps_buffer = 0
            timer = get_time()
        r = asuki.assets.UNIFONT_14.render(f"FPS: {fps}", False, (255, 255, 255))
        surface.blit(r, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        # clock.tick.py(30)


def update_loop():
    clock = pygame.time.Clock()

    while running:
        update()
        # print(keys_pressing)
        clock.tick(30)


def update():
    global running

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = event.key
            keys_pressing.append(key)
        if event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_F4:
                pygame.display.toggle_fullscreen()
            if key in keys_pressing:
                keys_pressing.remove(key)

    sprites.update()


def render():
    global surface

    sprites.draw(surface)


def get_time() -> int:
    return round(time.time() * 1000)
