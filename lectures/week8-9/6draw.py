import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Geometric Shapes Examples")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    pygame.draw.rect(screen, (255, 0, 0),(100, 100, 200, 150))
    pygame.draw.circle(screen, (0, 0, 255), (400,300), 50)
    pygame.draw.line(screen, (0, 255, 0), (100, 100), (400, 400), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()