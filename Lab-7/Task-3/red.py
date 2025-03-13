import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((800, 480))

COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_radius = 25
movement_speed = 20

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                circle_y = max(circle_radius, circle_y - movement_speed)
            elif event.key == pygame.K_DOWN:
                circle_y = min(HEIGHT - circle_radius, circle_y + movement_speed)
            elif event.key == pygame.K_LEFT:
                circle_x = max(circle_radius, circle_x - movement_speed)
            elif event.key == pygame.K_RIGHT:
                circle_x = min(WIDTH - circle_radius, circle_x + movement_speed)
    
    screen.fill(COLOR_WHITE)
    pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), circle_radius)
    
    pygame.display.flip()