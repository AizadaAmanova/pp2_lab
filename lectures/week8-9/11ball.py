import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball_pos = [400, 300]
ball_radius = 30
speed = 5

running = True
while running:
    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  
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
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
