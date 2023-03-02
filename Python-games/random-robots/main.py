from random import randint
import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))



for i in range(1000):
    x = randint(0,640)
    y = randint(0,480)
    screen.blit(robot, (x, y))

pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()