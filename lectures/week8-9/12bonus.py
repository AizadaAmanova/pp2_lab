# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# ball_pos = [400, 300]
# ball_radius = 30
# bonus_pos = [random.randint(50, 750), random.randint(50, 550)]
# speed = 5

# running = True
# while running:
#     screen.fill((255, 255, 255))
    
#     pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  # Красный шар
#     pygame.draw.circle(screen, (0, 255, 0), bonus_pos, 15)  # Зеленый бонус
    
#     pygame.display.flip()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and ball_pos[0] - ball_radius > 0:
#         ball_pos[0] -= speed
#     if keys[pygame.K_RIGHT] and ball_pos[0] + ball_radius < 800:
#         ball_pos[0] += speed
#     if keys[pygame.K_UP] and ball_pos[1] - ball_radius > 0:
#         ball_pos[1] -= speed
#     if keys[pygame.K_DOWN] and ball_pos[1] + ball_radius < 600:
#         ball_pos[1] += speed

#     # Проверка столкновения с бонусом
#     if abs(ball_pos[0] - bonus_pos[0]) < 30 and abs(ball_pos[1] - bonus_pos[1]) < 30:
#         bonus_pos = [random.randint(50, 750), random.randint(50, 550)]  # Новый бонус

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     clock.tick(60)  # Ограничиваем FPS для плавного движения

# pygame.quit()

# шарик увеличивается

# import pygame
# import random

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# ball_pos = [400, 300]
# ball_radius = 30
# bonus_pos = [random.randint(50, 750), random.randint(50, 550)]
# speed = 5

# running = True
# while running:
#     screen.fill((255, 255, 255))
    
#     pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  # Красный шарик
#     pygame.draw.circle(screen, (0, 255, 0), bonus_pos, 15)  # Зеленый бонус
    
#     pygame.display.flip()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and ball_pos[0] - ball_radius > 0:
#         ball_pos[0] -= speed
#     if keys[pygame.K_RIGHT] and ball_pos[0] + ball_radius < 800:
#         ball_pos[0] += speed
#     if keys[pygame.K_UP] and ball_pos[1] - ball_radius > 0:
#         ball_pos[1] -= speed
#     if keys[pygame.K_DOWN] and ball_pos[1] + ball_radius < 600:
#         ball_pos[1] += speed

#     # Проверяем, коснулся ли шарик бонуса
#     if abs(ball_pos[0] - bonus_pos[0]) < ball_radius and abs(ball_pos[1] - bonus_pos[1]) < ball_radius:
#         ball_radius += 5  # Увеличиваем размер шарика
#         bonus_pos = [random.randint(50, 750), random.randint(50, 550)]  # Новый бонус
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     clock.tick(60)  # Плавность

# pygame.quit()


#БАЛЛМЕН

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36) 

ball_pos = [400, 300]
ball_radius = 30
bonus_pos = [random.randint(50, 750), random.randint(50, 550)]
speed = 5
score = 0 

running = True
while running:
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  
    pygame.draw.circle(screen, (0, 255, 0), bonus_pos, 15)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_pos[0] - ball_radius > 0:
        ball_pos[0] -= speed
    if keys[pygame.K_RIGHT] and ball_pos[0] + ball_radius < 800:
        ball_pos[0] += speed
    if keys[pygame.K_UP] and ball_pos[1] - ball_radius > 0:
        ball_pos[1] -= speed
    if keys[pygame.K_DOWN] and ball_pos[1] + ball_radius < 600:
        ball_pos[1] += speed

    if abs(ball_pos[0] - bonus_pos[0]) < ball_radius and abs(ball_pos[1] - bonus_pos[1]) < ball_radius:
        ball_radius += 5 
        score += 1  
        bonus_pos = [random.randint(50, 750), random.randint(50, 550)]  # Новый бонус
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # Плавность

pygame.quit()
