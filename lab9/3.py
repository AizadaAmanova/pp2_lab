import pygame  # Импортируем библиотеку pygame
import math  # Импортируем библиотеку math для математических операций

pygame.init()  # Инициализируем pygame

# Создаём окно размером 800x600
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  # Заполняем экран белым цветом

# Определяем цвета в формате RGB
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_BLUE = (0, 0, 255)
C_GREEN = (0, 255, 0)

# Инициализация переменных
color = C_BLACK  # Текущий цвет рисования
saved_color = color  # Сохранённый цвет (для переключения с ластика обратно)
radius = 5  # Толщина линий
clock = pygame.time.Clock()  # Создаём объект для управления частотой кадров

drawing = False  # Флаг рисования
last_pos = None  # Последняя позиция мыши
shape = "circle"  # Текущая форма для рисования (по умолчанию круг)
eraser_mode = False  # Флаг режима ластика

running = True  # Главный флаг работы программы
while running:
    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Если закрыли окно
            running = False  # Завершаем программу

        if event.type == pygame.KEYDOWN:  # Обработка нажатий клавиш
            # Выбор формы для рисования
            if event.key == pygame.K_PLUS:
                shape = "circle"
            elif event.key == pygame.K_MINUS:
                shape = "rect"
            elif event.key == pygame.K_SPACE:
                shape = "line"
            elif event.key == pygame.K_4:
                shape = "square"
            elif event.key == pygame.K_5:
                shape = "right_triangle"
            elif event.key == pygame.K_6:
                shape = "equilateral_triangle"
            elif event.key == pygame.K_7:
                shape = "rhombus"
            
            # Выбор цвета
            elif event.key == pygame.K_1:
                color = C_RED
                saved_color = color
                eraser_mode = False
            elif event.key == pygame.K_2:
                color = C_GREEN
                saved_color = color
                eraser_mode = False
            elif event.key == pygame.K_3:
                color = C_BLUE
                saved_color = color
                eraser_mode = False
            elif event.key == pygame.K_0:
                color = C_WHITE  # Белый цвет для закрашивания (ластик)
                saved_color = color
                eraser_mode = False
            elif event.key == pygame.K_9:
                color = C_BLACK
                saved_color = color
                eraser_mode = False
            elif event.key == pygame.K_e:
                color = C_WHITE  # Включаем режим ластика
                eraser_mode = True
            elif event.key == pygame.K_b:
                color = saved_color  # Возвращаем цвет кисти
                eraser_mode = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
            drawing = True
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:  # Если кнопка мыши отпущена
            if drawing:
                current_pos = event.pos
                if shape == "circle":  # Рисуем круг
                    center = ((last_pos[0] + current_pos[0]) // 2,
                              (last_pos[1] + current_pos[1]) // 2)
                    radius_circle = max(abs(current_pos[0] - last_pos[0]) // 2,
                                        abs(current_pos[1] - last_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, radius_circle)
                elif shape == "rect":  # Рисуем прямоугольник
                    rect = pygame.Rect(min(last_pos[0], current_pos[0]),
                                       min(last_pos[1], current_pos[1]),
                                       abs(current_pos[0] - last_pos[0]),
                                       abs(current_pos[1] - last_pos[1]))
                    pygame.draw.rect(screen, color, rect)
                elif shape == "line":  # Рисуем линию
                    pygame.draw.line(screen, color, last_pos, current_pos, radius)
                elif shape == "square":  # Рисуем квадрат
                    dx = current_pos[0] - last_pos[0]
                    dy = current_pos[1] - last_pos[1]
                    side = min(abs(dx), abs(dy))
                    start_x, start_y = last_pos
                    if dx >= 0 and dy >= 0:
                        rect = pygame.Rect(start_x, start_y, side, side)
                    elif dx < 0 and dy >= 0:
                        rect = pygame.Rect(start_x - side, start_y, side, side)
                    elif dx >= 0 and dy < 0:
                        rect = pygame.Rect(start_x, start_y - side, side, side)
                    else:
                        rect = pygame.Rect(start_x - side, start_y - side, side, side)
                    pygame.draw.rect(screen, color, rect)
                elif shape == "right_triangle":  # Рисуем прямоугольный треугольник
                    pygame.draw.polygon(screen, color, [last_pos, 
                                                          (current_pos[0], last_pos[1]), 
                                                          (last_pos[0], current_pos[1])])
                elif shape == "equilateral_triangle":  # Рисуем равносторонний треугольник
                    x1, y1 = last_pos
                    x2, y2 = current_pos
                    side_length = math.hypot(x2 - x1, y2 - y1)
                    mid = ((x1 + x2) / 2, (y1 + y2) / 2)
                    height = (math.sqrt(3) / 2) * side_length
                    dx, dy = x2 - x1, y2 - y1
                    perp = (-dy, dx)
                    length = math.hypot(perp[0], perp[1])
                    if length != 0:
                        perp = (perp[0] / length, perp[1] / length)
                    third_vertex = (mid[0] + perp[0] * height, mid[1] + perp[1] * height)
                    pygame.draw.polygon(screen, color, [last_pos, current_pos, third_vertex])
                elif shape == "rhombus":  # Рисуем ромб
                    x1, y1 = last_pos
                    x2, y2 = current_pos
                    mid_top = ((x1 + x2) / 2, y1)
                    mid_bottom = ((x1 + x2) / 2, y2)
                    mid_left = (x1, (y1 + y2) / 2)
                    mid_right = (x2, (y1 + y2) / 2)
                    pygame.draw.polygon(screen, color, [mid_top, mid_right, mid_bottom, mid_left])
            drawing = False
            last_pos = None

    pygame.display.update()
    clock.tick(120)

pygame.quit()  # Завершаем работу pygame
