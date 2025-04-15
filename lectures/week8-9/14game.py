# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# # Начальные параметры
# player_pos = [400, 300]  # Позиция красного шара (игрока)
# target_pos = [random.randint(50, 750), random.randint(50, 550)]  # Позиция синего шара (цели)
# player_radius = 30
# target_radius = 20
# speed = 5
# score = 0  # Баллы

# running = True
# while running:
#     screen.fill((255, 255, 255))  # Очищаем экран

#     # Отображение шариков
#     pygame.draw.circle(screen, (255, 0, 0), player_pos, player_radius)  # Красный шар (игрок)
#     pygame.draw.circle(screen, (0, 0, 255), target_pos, target_radius)  # Синий шар (цель)

#     # Отображение баллов
#     font = pygame.font.Font(None, 36)
#     score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#     screen.blit(score_text, (10, 10))

#     pygame.display.flip()

#     # Управление игроком
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_pos[0] - player_radius > 0:
#         player_pos[0] -= speed
#     if keys[pygame.K_RIGHT] and player_pos[0] + player_radius < 800:
#         player_pos[0] += speed
#     if keys[pygame.K_UP] and player_pos[1] - player_radius > 0:
#         player_pos[1] -= speed
#     if keys[pygame.K_DOWN] and player_pos[1] + player_radius < 600:
#         player_pos[1] += speed

#     # Проверка столкновения (когда игрок касается цели)
#     if abs(player_pos[0] - target_pos[0]) < player_radius and abs(player_pos[1] - target_pos[1]) < player_radius:
#         score += 1  # Увеличиваем баллы
#         target_pos = [random.randint(50, 750), random.randint(50, 550)]  # Новый синий шар в случайном месте

#     # Обработка выхода
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     clock.tick(60)  # Ограничение FPS

# pygame.quit()

# АСТЫНДАҒЫ БОНУС БОЛҒАНДА ҮЛКЕЙЕДІ, ҮСТІ СОЛ ҚАЛПЫ ҚАЛАДЫ

import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Догонялки")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


player_pos = [400, 300]
player_radius = 30
enemy_pos = [random.randint(50, 750), random.randint(50, 550)]
enemy_radius = 20
speed = 5
score = 0  
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(WHITE)

   
    pygame.draw.circle(screen, RED, player_pos, player_radius)
    pygame.draw.circle(screen, BLUE, enemy_pos, enemy_radius)

    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] - player_radius > 0:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT] and player_pos[0] + player_radius < WIDTH:
        player_pos[0] += speed
    if keys[pygame.K_UP] and player_pos[1] - player_radius > 0:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN] and player_pos[1] + player_radius < HEIGHT:
        player_pos[1] += speed

    
    if abs(player_pos[0] - enemy_pos[0]) < player_radius and abs(player_pos[1] - enemy_pos[1]) < player_radius:
        enemy_pos = [random.randint(50, 750), random.randint(50, 550)] 
        player_radius += 3 
        score += 1 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

pygame.quit()
