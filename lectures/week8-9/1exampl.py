# import pygame
# import math
# import time
 
# pygame.init()

# background = pygame.display.set_mode((800,600))
# clock = pygame.time.Clock()

# pygame.display.set_caption("CLOCK")

# lefttarm = pygame.image.load()
# righttarm = pygame.image.load()
# clock = pygame.transform.scale(pygame.image.load())

# righttarm = pygame.transform.scale(righttarm(600,400))
# lefttarm = pygame.transform.scale(lefttarm(800,800))

# done = False

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done == True

# current_time = time.localtime()
# hour = current_time.tm_hour
# minute = current_time.tm_min













import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Window")

running = False

while not running:
    for event in pygame.event.get():
        event.type == pygame.QUIT()
        running = False

pygame.quit()















