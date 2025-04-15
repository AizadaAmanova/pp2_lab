import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
ball_pos = [400, 300]
ball_radius = 30
speed = [5, 5]

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
    pygame.display.flip()

    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]

    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= 800:
        speed[0] = -speed[0]
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= 600:
        speed[1] = -speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)

pygame.quit()
