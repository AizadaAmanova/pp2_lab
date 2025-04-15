import pygame
import random

pygame.init()

# Window size
WIDTH, HEIGHT = 600, 600
CELL = 30

# Colors
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_grid():
    """ Draws a grid on the screen. """
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    """ Represents a point (x, y) in the grid. """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow = False  # Flag to grow the snake

    def move(self):
        """ Moves the snake in the current direction. """
        if self.grow:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.grow = False

        # Move body parts
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Move head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Check screen boundaries
        if self.body[0].x >= WIDTH // CELL:
            self.body[0].x = 0
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        if self.body[0].y >= HEIGHT // CELL:
            self.body[0].y = 0
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1

    def draw(self):
        """ Draws the snake on the screen. """
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))  # Head
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))  # Body

    def check_collision(self, food):
        """ Checks if the snake eats food. """
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow = True
            food.generate_random_pos(self)

    def check_self_collision(self):
        """ Checks if the snake collides with itself. """
        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                return True
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        """ Draws the food on the screen. """
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake):
        """ Generates a random position for food, avoiding the snake's body. """
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)

            # Ensure food does not spawn inside the snake
            if all(self.pos.x != segment.x or self.pos.y != segment.y for segment in snake.body):
                break

# FPS control
FPS = 10
clock = pygame.time.Clock()

food = Food()
snake = Snake()

running = True
while running:
    screen.fill(colorBLACK)

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
    snake.move()
    snake.check_collision(food)

    # Check if snake hits itself
    if snake.check_self_collision():
        print("Game Over!")
        running = False

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
