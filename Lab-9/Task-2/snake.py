import pygame
import random
from color_palette import *

pygame.init()
# Размер окна
WIDTH = 600
HEIGHT = 600
# Сам экран
screen = pygame.display.set_mode((HEIGHT, WIDTH))
# Размер клеток
CELL = 30

# Функция отрисовки шахматного поля
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки (используется для змеи и еды)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс Змеи
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13), Point(10, 14), Point(10, 15)]
        self.dx, self.dy = 1, 0  # Направление движения
        self.score, self.level = 0, 1  # Очки и уровень

    def move(self):
        # Перемещаем сегменты змеи
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y
        
        # Перемещаем голову змеи
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Проверка столкновений
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
            for _ in range(food.weight):  # Добавляем сегменты змеи в зависимости от веса еды
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.score += food.weight
            food.generate_new_position(self)
            if self.score % 3 == 0:
                self.level += 1
                return True
        return False

# Класс Еды
class Food:
    def __init__(self):
        self.generate_new_position(None)
        self.weight = random.randint(1, 3)  # Вес еды (1-3 очка)
        self.timer = random.randint(5, 10) * FPS  # Время исчезновения еды

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_new_position(self, snake):
        while True:
            new_x = random.randint(0, WIDTH // CELL - 1)
            new_y = random.randint(0, HEIGHT // CELL - 1)
            if snake is None or not any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                self.pos = Point(new_x, new_y)
                self.weight = random.randint(1, 3)  # Случайный вес еды
                self.timer = random.randint(5, 10) * FPS  # Случайное время исчезновения
                break

FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()

running = True
while running:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1
    
    # Отрисовка шахматного поля
    draw_grid_chess()
    
    # Двигаем змею и проверяем столкновения с едой
    snake.move()
    if snake.check_collision(food):
        FPS += 1  # Ускорение игры при съедании еды
    
    # Таймер исчезновения еды
    food.timer -= 1
    if food.timer <= 0:
        food.generate_new_position(snake)
    
    # Отрисовка змеи и еды
    snake.draw()
    food.draw()
    
    # Отображение очков и уровня
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
