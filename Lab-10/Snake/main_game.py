import pygame
import random
import psycopg2
from color_palette import *

# Инициализация Pygame
pygame.init()
font = pygame.font.SysFont("Verdana", 30)

# Подключение к БД
conn = psycopg2.connect(
    dbname="snakescore",
    user="postgres",
    password="123456",
    host="localhost"
)
cur = conn.cursor()

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

query_create_table_user_and_userscore = """
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE
    );

    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

execute_query(query_create_table_user_and_userscore)

def get_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def get_user_data(username):
    cur.execute("SELECT id, username FROM users WHERE username = %s", (username,))
    user_data = cur.fetchone()
    if user_data:
        user_id = user_data[0]
        cur.execute("""
            SELECT score, level FROM user_scores 
            WHERE user_id = %s 
            ORDER BY saved_at DESC 
            LIMIT 1
        """, (user_id,))
        last_score = cur.fetchone()
        return {
            "user_id": user_id,
            "score": last_score[0] if last_score else 0,
            "level": last_score[1] if last_score else 1
        }
    return None

def save_user_score(user_id, score, level):
    cur.execute(""" 
        INSERT INTO user_scores (user_id, score, level) 
        VALUES (%s, %s, %s) 
    """, (user_id, score, level))
    conn.commit()

# Размер окна
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((HEIGHT, WIDTH))
CELL = 30

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, score=0, level=1):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13), Point(10, 14), Point(10, 15)]
        self.dx, self.dy = 1, 0
        self.score = score
        self.level = level
        self.length = self.level + 4

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.check_collision_with_self() or self.check_wall_collision():
            pygame.quit()
            quit()

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision_with_self(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.score += food.weight
            food.generate_new_position(self)
            if self.score % 3 == 0:
                self.level += 1
                return True
        return False

class Food:
    def __init__(self):
        self.generate_new_position(None)
        self.weight = random.randint(1, 3)
        self.timer = random.randint(5, 10) * FPS

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_new_position(self, snake):
        while True:
            new_x = random.randint(0, WIDTH // CELL - 1)
            new_y = random.randint(0, HEIGHT // CELL - 1)
            if snake is None or not any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                self.pos = Point(new_x, new_y)
                self.weight = random.randint(1, 3)
                self.timer = random.randint(5, 10) * FPS
                break

FPS = 5
clock = pygame.time.Clock()

# Стартовый экран для ввода имени
input_box = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, 40)
active = False
username = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
text_surface = font.render('Введите имя:', True, color)
input_text = ''

running = True
user_data = None
while running:
    screen.fill((30, 30, 30))
    screen.blit(text_surface, (WIDTH // 4, HEIGHT // 4 - 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    user_data = get_user_data(username)
                    if user_data is None:
                        user_id = get_user(username)
                        user_data = {
                            "user_id": user_id,
                            "score": 0,
                            "level": 1
                        }
                    snake = Snake(score=user_data["score"], level=user_data["level"])
                    FPS = 5 + (snake.level - 1)
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
            input_text = username
            text_surface = font.render(input_text, True, color)

    pygame.draw.rect(screen, color, input_box, 2)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    pygame.display.flip()

# Основной игровой цикл
food = Food()
snake = Snake(score=user_data["score"], level=user_data["level"])

paused = False
while not paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            paused = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                save_user_score(user_data["user_id"], snake.score, snake.level)
                print("Игра на паузе. Счет сохранен.")
                paused = True
                while paused:
                    for pe in pygame.event.get():
                        if pe.type == pygame.QUIT:
                            paused = False
                        if pe.type == pygame.KEYDOWN and pe.key == pygame.K_p:
                            paused = False

    draw_grid_chess()
    snake.move()
    if snake.check_collision(food):
        FPS += 1

    food.timer -= 1
    if food.timer <= 0:
        food.generate_new_position(snake)

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()