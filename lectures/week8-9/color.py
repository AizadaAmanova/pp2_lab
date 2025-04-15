#Смена цвета объекта

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball_pos = [400, 300]
ball_radius = 30
speed = 5
ball_color = (255, 0, 0)  # Красный цвет

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:  
        ball_color = (255, 0, 0)  # Красный
    if keys[pygame.K_2]:  
        ball_color = (0, 255, 0)  # Зеленый
    if keys[pygame.K_3]:  
        ball_color = (0, 0, 255)  # Синий

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
