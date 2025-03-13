import pygame
from pygame import Vector2
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

reference_dict = {}
def load_image(image_name):
    image = pygame.image.load(f'Lab-7/Task-1/{image_name}.png')
    reference_dict[image_name] = image

load_image('clock')
load_image('min_hand')
load_image('sec_hand')

clock_image = reference_dict['clock']
clock_rect = clock_image.get_rect(topleft=(-150, -50))
pivot = clock_rect.center 

def rotate_on_pivot(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rect

class Hand:
    def __init__(self, pivot, name, is_minute_hand=False):
        self.pivot = pivot
        self.is_minute_hand = is_minute_hand

        now = datetime.now()
        if is_minute_hand:
            self.angle = - (6 * now.minute + 0.1 * now.second)  
        else:
            self.angle = - (6 * now.second) 

        print(f"Min {6 * now.minute + 0.1 * now.second} Sec {6 * now.second}")
 
        offset = Vector2()
        offset.from_polar((0, self.angle))
        self.pos = self.pivot + offset

        self.image_orig = reference_dict[name]
        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot)

    def update(self):
        now = datetime.now()
        if self.is_minute_hand:
            self.angle = - (6 * now.minute + 0.1 * now.second) 
        else:
            self.angle = - (6 * now.second)

        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

sec_hand = Hand(pivot, 'sec_hand')
min_hand = Hand(pivot, 'min_hand', is_minute_hand=True)

done = False
while not done:
    dt = clock.tick(60) * 0.001
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(reference_dict['clock'], (-150, -50))

    min_hand.update()
    sec_hand.update()

    min_hand.draw(screen)
    sec_hand.draw(screen)

    pygame.display.flip()