import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 30

colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

def draw_grid():
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow = False

    def move(self):
        if self.grow:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.grow = False
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or \
           self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL:
            return False
        return True

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow = True
            food.generate_random_pos(self)
            return True
        return False

    def check_self_collision(self):
        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                return True
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if all(self.pos.x != segment.x or self.pos.y != segment.y for segment in snake.body):
                break

FPS = 10
clock = pygame.time.Clock()

food = Food()
snake = Snake()
score = 0
running = True
game_over = False

while running:
    screen.fill(colorBLACK)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP and snake.dy == 0:
                    snake.dx = 0
                    snake.dy = -1

        draw_grid()

        if not snake.move():
            game_over = True

        if snake.check_collision(food):
            score += 1

        if snake.check_self_collision():
            game_over = True

        snake.draw()
        food.draw()

        score_text = font.render(f"Score: {score}", True, colorWHITE)
        screen.blit(score_text, (10, 10))
    else:
        game_over_text = game_over_font.render("GAME OVER", True, colorRED)
        score_text = font.render(f"Final Score: {score}", True, colorWHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()