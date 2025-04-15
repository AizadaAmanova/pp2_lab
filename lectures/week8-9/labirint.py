import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Позиция шара
ball_pos = [50, 50]
ball_radius = 20
ball_speed = 5  

# Стены лабиринта
walls = [
    pygame.Rect(100, 100, 200, 20),  
    pygame.Rect(300, 200, 20, 200),  
    pygame.Rect(500, 300, 200, 20),  
]

# Выход
exit_rect = pygame.Rect(700, 500, 50, 50)

running = True
while running:
    screen.fill(WHITE)

    # Рисуем стены
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    # Рисуем выход
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Рисуем шарик
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    new_pos = ball_pos[:]  

    if keys[pygame.K_LEFT]:
        new_pos[0] -= ball_speed
    if keys[pygame.K_RIGHT]:
        new_pos[0] += ball_speed
    if keys[pygame.K_UP]:
        new_pos[1] -= ball_speed
    if keys[pygame.K_DOWN]:
        new_pos[1] += ball_speed

    # Ограничение по границам экрана
    new_pos[0] = max(ball_radius, min(WIDTH - ball_radius, new_pos[0]))
    new_pos[1] = max(ball_radius, min(HEIGHT - ball_radius, new_pos[1]))

    # Проверяем столкновение со стенами
    ball_rect = pygame.Rect(new_pos[0] - ball_radius, new_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)
    if not any(ball_rect.colliderect(wall) for wall in walls):
        ball_pos = new_pos  

    # Проверяем выход
    if ball_rect.colliderect(exit_rect):
        print("Ты прошел лабиринт!")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  

pygame.quit()
