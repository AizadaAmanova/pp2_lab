import pygame
pygame.init()

screen = pygame.display.set_mode((500,300))
font = pygame.font.Font(None, 36)

text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()