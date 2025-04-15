import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_pos = [400, 300]
bot_pos = [random.randint(50, 750), random.randint(50, 550)]
speed = 5
bot_speed = 3

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), player_pos, 30)  
    pygame.draw.circle(screen, (0, 0, 255), bot_pos, 30)  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_pos[0] -= speed
    if keys[pygame.K_RIGHT]: player_pos[0] += speed
    if keys[pygame.K_UP]: player_pos[1] -= speed
    if keys[pygame.K_DOWN]: player_pos[1] += speed

    
    distance = math.dist(player_pos, bot_pos)
    if distance < 200: 
        if player_pos[0] < bot_pos[0]: bot_pos[0] += bot_speed
        if player_pos[0] > bot_pos[0]: bot_pos[0] -= bot_speed
        if player_pos[1] < bot_pos[1]: bot_pos[1] += bot_speed
        if player_pos[1] > bot_pos[1]: bot_pos[1] -= bot_speed

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
