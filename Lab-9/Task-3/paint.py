import pygame
import sys
import math

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Настройки кисти
brush_size = 10
DRAWING_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

# Состояния рисования
drawing = False
last_pos = (0, 0)
shape = 'line'  # Текущая выбранная фигура

# Списки для хранения нарисованных объектов
lines = []
rectangles = []
circles = []
squares = []
right_triangles = []
equilateral_triangles = []
rhombuses = []

# Временные объекты для отображения при рисовании
temp_rectangle = None
temp_circle = None
temp_square = None
temp_right_triangle = None
temp_equilateral_triangle = None
temp_rhombus = None
start_pos = None

# Палитра цветов
color_palette = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (0, 0, 0),  # Black
    (255, 0, 255),  # Magenta
    (0, 255, 255)  # Cyan
]
color_index = 0  

def draw_objects():
    screen.fill(BACKGROUND_COLOR)
    
    # Рисуем все сохраненные фигуры
    for rectangle in rectangles:
        pygame.draw.rect(screen, rectangle[1], rectangle[0], rectangle[2])
    for circle in circles:
        pygame.draw.circle(screen, circle[1], circle[0][0], circle[0][1], circle[2])
    for square in squares:
        pygame.draw.rect(screen, square[1], square[0], square[2])
    for triangle in right_triangles:
        pygame.draw.polygon(screen, triangle[1], triangle[0], triangle[2])
    for triangle in equilateral_triangles:
        pygame.draw.polygon(screen, triangle[1], triangle[0], triangle[2])
    for rhombus in rhombuses:
        pygame.draw.polygon(screen, rhombus[1], rhombus[0], rhombus[2])
    for line in lines:
        pygame.draw.line(screen, line[2], line[0], line[1], line[3])
    
    # Рисуем временные фигуры (которые еще рисуются)
    if temp_rectangle:
        pygame.draw.rect(screen, DRAWING_COLOR, temp_rectangle, brush_size)
    if temp_circle:
        pygame.draw.circle(screen, DRAWING_COLOR, temp_circle[0], int(temp_circle[1]), brush_size)
    if temp_square:
        pygame.draw.rect(screen, DRAWING_COLOR, temp_square, brush_size)
    if temp_right_triangle:
        pygame.draw.polygon(screen, DRAWING_COLOR, temp_right_triangle, brush_size)
    if temp_equilateral_triangle:
        pygame.draw.polygon(screen, DRAWING_COLOR, temp_equilateral_triangle, brush_size)
    if temp_rhombus:
        pygame.draw.polygon(screen, DRAWING_COLOR, temp_rhombus, brush_size)
    
    pygame.display.flip()

def calculate_equilateral_triangle(start, end):
    x1, y1 = start
    x2, y2 = end
    
    # Вычисляем длину стороны
    side_length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # Вычисляем высоту треугольника
    height = (3**0.5 / 2) * side_length
    
    # Определяем направление рисования
    if x2 < x1:
        side_length = -side_length
    
    # Третья вершина
    x3 = x1 + side_length / 2
    y3 = y1 - height
    
    return [(x1, y1), (x2, y2), (x3, y3)]

def calculate_rhombus(start, end):
    x1, y1 = start
    x2, y2 = end
    
    # Центр ромба
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    # Половина диагоналей
    dx = abs(x2 - x1) / 2
    dy = abs(y2 - y1) / 2
    
    # Вершины ромба
    return [
        (center_x, center_y - dy),  # Верхняя
        (center_x + dx, center_y),   # Правая
        (center_x, center_y + dy),   # Нижняя
        (center_x - dx, center_y)    # Левая
    ]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if shape == 'rectangle' and temp_rectangle:
                rectangles.append((temp_rectangle, DRAWING_COLOR, brush_size))
                temp_rectangle = None
            elif shape == 'circle' and temp_circle:
                circles.append(((temp_circle[0], int(temp_circle[1])), DRAWING_COLOR, brush_size))
                temp_circle = None
            elif shape == 'square' and temp_square:
                squares.append((temp_square, DRAWING_COLOR, brush_size))
                temp_square = None
            elif shape == 'right_triangle' and temp_right_triangle:
                right_triangles.append((temp_right_triangle, DRAWING_COLOR, brush_size))
                temp_right_triangle = None
            elif shape == 'equilateral_triangle' and temp_equilateral_triangle:
                equilateral_triangles.append((temp_equilateral_triangle, DRAWING_COLOR, brush_size))
                temp_equilateral_triangle = None
            elif shape == 'rhombus' and temp_rhombus:
                rhombuses.append((temp_rhombus, DRAWING_COLOR, brush_size))
                temp_rhombus = None

        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape == 'line':
                lines.append((last_pos, event.pos, DRAWING_COLOR, brush_size))
            elif shape == 'erase':
                lines.append((last_pos, event.pos, BACKGROUND_COLOR, brush_size))
            elif shape == 'rectangle':
                temp_rectangle = (min(start_pos[0], event.pos[0]), 
                                 min(start_pos[1], event.pos[1]), 
                                 abs(event.pos[0] - start_pos[0]), 
                                 abs(event.pos[1] - start_pos[1]))
            elif shape == 'circle':
                radius = ((event.pos[0] - start_pos[0]) ** 2 + (event.pos[1] - start_pos[1]) ** 2) ** 0.5
                temp_circle = (start_pos, radius)
            elif shape == 'square':
                size = max(abs(event.pos[0] - start_pos[0]), abs(event.pos[1] - start_pos[1]))
                temp_square = (min(start_pos[0], event.pos[0]), 
                              min(start_pos[1], event.pos[1]), 
                              size, size)
            elif shape == 'right_triangle':
                temp_right_triangle = [
                    start_pos,
                    (start_pos[0], event.pos[1]),
                    event.pos
                ]
            elif shape == 'equilateral_triangle':
                temp_equilateral_triangle = calculate_equilateral_triangle(start_pos, event.pos)
            elif shape == 'rhombus':
                temp_rhombus = calculate_rhombus(start_pos, event.pos)
            last_pos = event.pos

        elif event.type == pygame.KEYDOWN:
            # Выбор инструментов
            if event.key == pygame.K_e:
                shape = 'erase'  
            elif event.key == pygame.K_r:
                shape = 'rectangle'  
            elif event.key == pygame.K_c:
                shape = 'circle'  
            elif event.key == pygame.K_l:
                shape = 'line' 
            elif event.key == pygame.K_s:
                shape = 'square'
            elif event.key == pygame.K_t:
                shape = 'right_triangle' 
            elif event.key == pygame.K_y:
                shape = 'equilateral_triangle' 
            elif event.key == pygame.K_h:
                shape = 'rhombus'  
            
            elif event.key == pygame.K_1:
                color_index = 0
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_2:
                color_index = 1
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_3:
                color_index = 2
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_4:
                color_index = 3
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_5:
                color_index = 4
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_6:
                color_index = 5
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_o:
                brush_size += 1
                if brush_size > 50:
                    brush_size = 50
            elif event.key == pygame.K_p:
                brush_size -= 1
                if brush_size < 1:
                    brush_size = 1
    
    draw_objects()
    clock.tick(60)