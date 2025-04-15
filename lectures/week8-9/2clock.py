import pygame
import time
import math

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("Clock")

# Загружаем изображения
leftarm = pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lectures/left_hand.png")
rightarm = pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lectures/right_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("C:/Users/Acer/Desktop/pp2_lab/lectures/clock.png"), (800, 500))

# Масштабируем изображения
leftarm = pygame.transform.scale(leftarm, (650, 500))
rightarm = pygame.transform.scale(rightarm, (800, 700))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Завершаем цикл при выходе

    # Получаем текущее время
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Вычисляем углы поворота
    minute_angle = - (minute * 6 + (second / 60) * 6)
    second_angle = - (second * 6)

    # Очищаем экран
    screen.fill((255, 255, 255))
    screen.blit(mainclock, (0, 0))

    # Рисуем минутную стрелку
    rotated_rightarm = pygame.transform.rotate(rightarm, minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(400, 300))
    screen.blit(rotated_rightarm, rightarmrect)

    # Рисуем секундную стрелку
    rotated_leftarm = pygame.transform.rotate(leftarm, second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(400, 300))
    screen.blit(rotated_leftarm, leftarmrect)


    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
