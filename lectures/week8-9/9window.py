import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))  
pygame.display.set_caption("Мое первое окно")  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
