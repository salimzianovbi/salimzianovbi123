import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
rect(screen, (200, 200, 200), (0, 0, 500, 500))
circle(screen, (255, 255, 0), (250, 250), 100)
circle(screen, (0, 0, 0), (250, 250), 100, 2)
circle(screen, (255, 50, 0), (210, 230), 23)
circle(screen, (0, 0, 0), (210, 230), 23, 2)
circle(screen, (0, 0, 0), (210, 230), 8)
circle(screen, (255, 50, 0), (290, 230), 18)
circle(screen, (0, 0, 0), (290, 230), 18, 2)
circle(screen, (0, 0, 0), (290, 230), 7)
rect(screen, (0, 0, 0), (205, 300, 85, 18))
line(screen, (0, 0, 0), (150, 165), (240, 215), 14)
line(screen, (0, 0, 0), (260, 215), (340, 180), 14)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()