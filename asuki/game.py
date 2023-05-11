import threading
import time

import asuki.objects.gameobject
import asuki.assets
import pygame

# Update and Render are separated
keys_pressing = []
game_objects = {}
running = True
surface: pygame.Surface


def init():
    global surface

    game_objects["test"] = asuki.objects.gameobject.GameObject(0, 0, 32, 32, asuki.assets.ICON)

    pygame.init()
    pygame.font.init()

    surface = pygame.display.set_mode((640, 480))
    pygame.display.init()
    pygame.display.set_caption("Game")
    pygame.display.set_icon(asuki.assets.ICON)


def loop():
    global running

    thread = threading.Thread(target=render_loop)
    thread.start()

    update_loop()

    pygame.display.quit()


def render_loop():
    fps = 0
    fps_buffer = 0
    timer = get_time()
    global running
    while running:
        surface.fill((0, 0, 0))
        render()
        fps_buffer += 1
        if get_time() - timer >= 1000:
            fps = fps_buffer
            fps_buffer = 0
            timer = get_time()
        r = pygame.font.SysFont("assets/font/unifont-15.0.01.ttf", 16).render(f"FPS: {fps}", False, (255, 255, 255))
        surface.blit(r, (0, 0))
        pygame.display.update()
        pygame.display.flip()


def update_loop():
    clock = pygame.time.Clock()

    while running:
        update()
        print(keys_pressing)
        clock.tick(20)


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
            if key in keys_pressing:
                keys_pressing.remove(event.key)


def render():
    global surface

    surface.blit(asuki.assets.ICON, (0, 0))
    # for obj in game_objects:
    #     surface.blit(obj.image, (0, 0), (32, 32))


def get_time() -> int:
    return round(time.time() * 1000)
