# # # 2.1. Гравитация
# # # Задача: Сделать, чтобы шарик падал вниз и отскакивал от земли.

# # import pygame

# # pygame.init()
# # screen = pygame.display.set_mode((800, 600))
# # clock = pygame.time.Clock()

# # ball_pos = [400, 300]
# # # ball_radius = 30
# # gravity = 0.5
# # speed_y = 0

# # running = True
# # while running:
# #     screen.fill((255, 255, 255))
# #     pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
# #     pygame.display.flip()

# #     speed_y += gravity  # Ускорение падения
# #     ball_pos[1] += speed_y  

# #     if ball_pos[1] + ball_radius > 600:  # Отскок от земли
# #         ball_pos[1] = 600 - ball_radius
# #         speed_y = -speed_y * 0.7  # Теряется часть скорости

# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     clock.tick(60)

# # pygame.quit()

# ГРАВИТАЦИЯ ТЕК


# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# ball_pos = [400, 500]  # Начальная позиция (ближе к земле)
# ball_radius = 30
# gravity = 0.5  # Сила гравитации
# speed_y = 0  # Начальная вертикальная скорость
# jump_power = -10  # Сила прыжка

# running = True
# while running:
#     screen.fill((255, 255, 255))  
#     pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  
#     pygame.display.flip()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and ball_pos[1] + ball_radius >= 600:  
#         speed_y = jump_power  # Прыжок вверх

#     speed_y += gravity  # Гравитация увеличивает скорость вниз
#     ball_pos[1] += speed_y  

#     if ball_pos[1] + ball_radius > 600:  # Если шарик на земле
#         ball_pos[1] = 600 - ball_radius  # Исправляем позицию
#         speed_y = 0  # Обнуляем скорость, чтобы не проваливался

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     clock.tick(60)

# pygame.quit()

# КНОПКАНЫ БАСКАНДА СЕКІРЕДІ



# ОҢҒА СОЛҒА ЖҮРІП СЕКІРЕДІ

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball_pos = [400, 500]  # Начальная позиция (ближе к земле)
ball_radius = 30
gravity = 0.5  # Гравитация
speed_y = 0  # Вертикальная скорость
jump_power = -10  # Сила прыжка
speed_x = 5  # Скорость движения влево-вправо

running = True
while running:
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    
    # Движение влево и вправо
    if keys[pygame.K_LEFT] and ball_pos[0] - ball_radius > 0:
        ball_pos[0] -= speed_x
    if keys[pygame.K_RIGHT] and ball_pos[0] + ball_radius < 800:
        ball_pos[0] += speed_x
    
    # Прыжок
    if keys[pygame.K_UP] and ball_pos[1] + ball_radius >= 600:
        speed_y = jump_power  

    # Гравитация
    speed_y += gravity  
    ball_pos[1] += speed_y  

    # Ограничение пола
    if ball_pos[1] + ball_radius > 600:  
        ball_pos[1] = 600 - ball_radius  
        speed_y = 0  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
