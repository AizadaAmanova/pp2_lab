import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
timer = 0  
ball_pos = [400, 300]
ball_speed = 5

running = True
while running:
    screen.fill((255, 255, 255))  # Белый фон

    # Отображаем таймер
    timer_text = font.render(f"Time: {timer // 60} sec", True, (0, 0, 0))
    screen.blit(timer_text, (10, 10))

    # Двигаем шар
    ball_pos[0] += ball_speed
    if ball_pos[0] > WIDTH or ball_pos[0] < 0:
        ball_speed = -ball_speed

    pygame.draw.circle(screen, (255, 0, 0), ball_pos, 30)  # Красный шар

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer += 1  
    clock.tick(60)  # Ограничение FPS до 60 кадров в секунду

pygame.quit()


# take this code game and implement re starting. for example. when pressing the R key the game is going 
# to reset and start from the beginning


import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface(screen.get_size()).convert()
clock = pygame.time.Clock()

FOOD_TIMEOUT = 5000


def draw_grid(surface):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = (93, 216, 228) if (x + y) % 2 == 0 else (84, 194, 205)
            pygame.draw.rect(surface, color, rect)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
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

        if new_pos[0] < 0 or new_pos[0] >= WIDTH or new_pos[1] < 0 or new_pos[1] >= HEIGHT:
            self.alive = False
            return

        if new_pos in self.positions[1:]:
            self.alive = False
            return

        self.positions.insert(0, new_pos)
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, self.color, (*pos, GRID_SIZE, GRID_SIZE))


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


def reset_game():
    global snake, food, score, FPS
    snake.reset()
    food.randomize_position()
    score = 0
    FPS = 5


snake = Snake()
food = Food()
score = 0
FPS = 5

font = pygame.font.SysFont("monospace", 16)
game_over_font = pygame.font.SysFont("monospace", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(UP)
            elif event.key == pygame.K_DOWN:
                snake.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.turn(RIGHT)
            elif event.key == pygame.K_r:
                reset_game()

    draw_grid(surface)
    snake.move()

    if pygame.time.get_ticks() - food.spawn_time > FOOD_TIMEOUT:
        food.randomize_position()

    if snake.alive and snake.get_head_position() == food.position:
        snake.length += 1
        score += 1
        FPS += 1
        food.randomize_position()

    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (5, 10))

    if not snake.alive:
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)