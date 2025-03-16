import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey clock")

leftarm = pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lab7/left_hand.png")

rightarm = pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lab7/right_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lab7/clock.png"), (800, 600))

rightarm = pygame.transform.scale(rightarm, (650, 600))  
leftarm = pygame.transform.scale(leftarm, (800, 800))  

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    minute_angle = - (minute * 6 + (second / 60) * 6)  
    second_angle = - (second * 6)  

    screen.fill((255, 255, 255))

    screen.blit(mainclock, (0, 0))

    rotated_rightarm = pygame.transform.rotate(rightarm, minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(400, 300))
    screen.blit(rotated_rightarm, rightarmrect)

    rotated_leftarm = pygame.transform.rotate(leftarm, second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(400, 300))
    screen.blit(rotated_leftarm, leftarmrect)

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()