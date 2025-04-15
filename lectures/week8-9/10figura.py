import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  

pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50) 

pygame.draw.rect(screen, (0, 255, 0), (200, 150, 100, 50)) 

pygame.draw.line(screen, (0, 0, 255), (100, 500), (700, 500), 5)  

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
