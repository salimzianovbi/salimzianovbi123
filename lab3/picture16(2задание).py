import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 847))

rect(screen, (184, 197, 201), (0, 0, 600, 847))
rect(screen, (255, 255, 255), (0, 535, 600, 535))
rect(screen, (82, 108, 103), (0, 539, 600, 535))
ellipse(screen, (169, 187,187), (-100, 45, 550, 150))
rect(screen, (220, 228, 227), (468, 15, 120, 540))
surface_1 = pygame.Surface((550, 150), pygame.SRCALPHA)
ellipse(surface_1, (169, 187, 187, 128), (0, 0, 550, 150))
screen.blit(surface_1, (177, -10))

ellipse(screen, (169, 187,187), (-300, 365, 650, 150))
rect(screen, (148, 168, 173), (12, 15, 120, 540))
rect(screen, (148, 173, 168), (157, 42, 120, 530))
rect(screen, (184, 201, 197), (97, 122, 120, 510))


rect(screen, (111, 146, 139), (400, 150, 120, 510))

surface_2 = pygame.Surface((550, 150), pygame.SRCALPHA)
ellipse(surface_2, (169, 187, 187, 128), (0, 0, 550, 120))
screen.blit(surface_2, (178, 210))


ellipse(screen, (108, 134, 129), (40, 670, 170, 45))
ellipse(screen, (108, 134, 129), (-85, 610, 170, 45))
ellipse(screen, (184, 201, 197), (-15, 720, 800, 180))

surface_3 = pygame.Surface((550, 150), pygame.SRCALPHA)
ellipse(surface_3, (169, 187, 187, 128), (0, 0, 170, 45))
screen.blit(surface_3, (40, 720))



def car(x, y, r):
    ellipse(screen,(0, 0, 0), (x/r, y/r, 40/r, 5/r))
    rect(screen,(0, 205, 255), ((x+20)/r, (y-30)/r, 250/r, 40/r))
    rect(screen,(0, 205, 255), ((x+65)/r, (y-60)/r, 125/r, 40/r))
    rect(screen,(255, 255, 255), ((x+75)/r, (y-52)/r, 40/r, 20/r))
    rect(screen,(255, 255, 255), ((x+135)/r, (y-52)/r, 40/r, 20/r))
    circle(screen,(0, 0, 0),((x+65)/r, (y+10)/r), 20/r)
    circle(screen,(0, 0, 0),((x+235)/r, (y+10)/r), 20/r)


car(215, 760, 1)
car(300,1300,2)
car(900,1390,2)
car(60,1600,2)













pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
