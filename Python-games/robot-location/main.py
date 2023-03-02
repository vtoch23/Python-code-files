import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]-robot.get_width()/2
            y = event.pos[1]-robot.get_height()/2

            window.fill((0, 0, 0))
            window.blit(robot, (randint(0,640-robot.get_width()), randint(0,480-robot.get_height())))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()