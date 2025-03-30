import pygame
import sys
import random

pygame.init()

# Параметры игры
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface(screen.get_size()).convert()
clock = pygame.time.Clock()

FOOD_TIMEOUT = 5000  # Время до появления новой еды

# Функция для отрисовки сетки
def draw_grid(surface):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = (93, 216, 228) if (x + y) % 2 == 0 else (84, 194, 205)
            pygame.draw.rect(surface, color, rect)

# Класс змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.alive = True

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction

    def move(self):
        if not self.alive:
            return
        
        head_x, head_y = self.get_head_position()
        x, y = self.direction
        new_pos = (head_x + x * GRID_SIZE, head_y + y * GRID_SIZE)
        
        # Проверка на столкновение со стеной
        if new_pos[0] < 0 or new_pos[0] >= WIDTH or new_pos[1] < 0 or new_pos[1] >= HEIGHT:
            self.alive = False
            return
        
        # Проверка на столкновение с самой собой
        if new_pos in self.positions[1:]:
            self.alive = False
            return
        
        self.positions.insert(0, new_pos)
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, self.color, (*pos, GRID_SIZE, GRID_SIZE))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# Класс еды
class Food:
    def __init__(self):
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (*self.position, GRID_SIZE, GRID_SIZE))

# Инициализация игры
snake = Snake()
food = Food()
score = 0
FPS = 5

font = pygame.font.SysFont("monospace", 16)
game_over_font = pygame.font.SysFont("monospace", 36)

# Игровой цикл
while True:
    snake.handle_keys()
    draw_grid(surface)
    snake.move()

    # Проверка времени еды
    if pygame.time.get_ticks() - food.spawn_time > FOOD_TIMEOUT:
        food.randomize_position()

    # Проверка на поедание еды
    if snake.alive and snake.get_head_position() == food.position:
        snake.length += 1
        score += 1
        FPS += 1
        food.randomize_position()

    # Отрисовка элементов
    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (5, 10))
    
    # Если игра окончена
    if not snake.alive:
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(FPS)
