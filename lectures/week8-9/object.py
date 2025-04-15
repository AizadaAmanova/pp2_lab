# 2.2. Спавн объектов
# Задача: Каждые 2 секунды появляется новый объект.

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

objects = []
spawn_timer = 0

running = True
while running:
    screen.fill((255, 255, 255))

    for obj in objects:
        pygame.draw.circle(screen, (0, 0, 255), obj, 20)

    spawn_timer += clock.get_time()
    if spawn_timer > 2000:  # Каждые 2 секунды (2000 мс)
        objects.append([random.randint(50, 750), random.randint(50, 550)])
        spawn_timer = 0

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
