import pygame
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Example")

pygame.mixer.music.load("C:/Users/Acer/Desktop/pp2_lab/lectures/background.wav")
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    sound = pygame.mixer.Sound("C:/Users/Acer/Desktop/pp2_lab/lectures/coin.mp3")
    sound.play()


    screen.fill((255, 255, 255))
    pygame.display.flip()


pygame.quit()
sys.exit()