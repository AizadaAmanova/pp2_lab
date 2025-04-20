import pygame, sys, random, psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost", database="testdb", user="postgres", password="12345", port="5432"
)
cur = conn.cursor()

# User setup
name = input("Enter your name: ")
cur.execute("SELECT id FROM users WHERE username = %s", (name,))
user = cur.fetchone()

if user is None:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (name,))
    user_id = cur.fetchone()[0]
    print(f"New player registered: {name}")
else:
    user_id = user[0]
    print(f"Welcome back, {name}!")
    cur.execute("SELECT MAX(score) FROM user_scores WHERE user_id = %s", (user_id,))
    best = cur.fetchone()[0]
    if best:
        print(f"Your best score: {best}")

# Game settings
score = 0
FPS = 5
walls = []
WIDTH, HEIGHT = 600, 600
CELL = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 20)

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

def draw_grid():
    for x in range(0, WIDTH, CELL):
        for y in range(0, HEIGHT, CELL):
            pygame.draw.rect(screen, (100, 200, 220), (x, y, CELL, CELL), 1)

def set_level(score):
    global FPS, walls
    walls = []
    if 10 <= score <= 19:
        FPS = 8
        for x in range(0, WIDTH, CELL):
            walls.append((x, 0))
            walls.append((x, HEIGHT - CELL))
        for y in range(0, HEIGHT, CELL):
            walls.append((0, y))
            walls.append((WIDTH - CELL, y))
    elif score >= 20:
        FPS = 12
        for i in range(100, 500, 20):
            walls.append((i, 300))
            walls.append((300, i))
    else:
        FPS = 5

class Snake:
    def __init__(self):
        self.body = [(300, 300)]
        self.dir = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        head = self.body[0]
        x, y = self.dir
        new = ((head[0] + x * CELL) % WIDTH, (head[1] + y * CELL) % HEIGHT)
        if new in self.body or new in walls:
            self.die()
        self.body.insert(0, new)
        if new != food.pos:
            self.body.pop()
        else:
            global score
            score += 1
            food.new()

    def die(self):
        cur.execute("INSERT INTO user_scores (user_id, score) VALUES (%s, %s)", (user_id, score))
        conn.commit()
        print(f"Game Over! Score saved: {name} — {score}")
        pygame.quit()
        sys.exit()

    def turn(self, d):
        if len(self.body) > 1 and (d[0]*-1, d[1]*-1) == self.dir:
            return
        self.dir = d

    def draw(self):
        for p in self.body:
            pygame.draw.rect(screen, (0, 100, 0), (*p, CELL, CELL))

class Food:
    def __init__(self):
        self.new()

    def new(self):
        while True:
            self.pos = (
                random.randint(0, WIDTH // CELL - 1) * CELL,
                random.randint(0, HEIGHT // CELL - 1) * CELL
            )
            if self.pos not in snake.body and self.pos not in walls:
                break

    def draw(self):
        pygame.draw.rect(screen, (200, 0, 0), (*self.pos, CELL, CELL))

snake = Snake()
food = Food()

while True:
    screen.fill((0, 0, 0))
    draw_grid()
    set_level(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: snake.turn(UP)
            elif event.key == pygame.K_DOWN: snake.turn(DOWN)
            elif event.key == pygame.K_LEFT: snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT: snake.turn(RIGHT)
            elif event.key == pygame.K_p:
                cur.execute("INSERT INTO user_scores (user_id, score) VALUES (%s, %s)", (user_id, score))
                conn.commit()
                print(f"Paused and saved: {name} — {score}")

    snake.move()
    snake.draw()
    food.draw()
    for wall in walls:
        pygame.draw.rect(screen, (255, 0, 0), (*wall, CELL, CELL))

    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
    clock.tick(FPS)
