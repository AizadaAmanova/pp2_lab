# import pygame
# pygame. init()

# wigth, heigth = 800,800
# screen = pygame.display.set_mode((wigth,heigth))

# player_image = pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lectures/clock.png")
# player_x, player_y = 100, 100

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0,0,0))
#     screen.blit(player_image,(player_x, player_y))
#     pygame.display.flip()

# pygame.quit()







import pygame
import sys

pygame.init()

width, heigth = 800,900
screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Micky")

image = pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lectures/clock.png")
image_x, image_y = 700, 700






running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_x -= 5

    # if keys[pygame.K_RIGHT]:
    #     image_y += 5

    image = pygame.transform.scale(image,(image_x, image_y))
    screen.blit(image,(50,50))
    pygame.display.flip()

pygame.quit()
sys.exit()