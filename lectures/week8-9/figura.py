import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255)) 

pygame.draw.circle(screen, (255, 0, 0), (200, 300), 50)  
pygame.draw.rect(screen, (0, 255, 0), (400, 250, 100, 100))  
pygame.draw.rect(screen, (0, 0, 255), (600, 200, 150, 100))  

pygame.display.flip()  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
