import pygame
from random import randint
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x1, y1 = randint(320,590), randint(-100,0)
x2, y2 = randint(0,270), randint(-100,0)
x3, y3 = randint(320,590), randint(-100,0)
x4, y4 = randint(0,270), randint(-100,0)
x5, y5 = randint(320,590), randint(-100,0)
x6, y6 = randint(0,590), randint(-100,0)
x7, y7 = randint(0,590), randint(-100,0)
x8, y8 = randint(0,590), randint(-100,0)
x9, y9 = randint(0,590), randint(-100,0)

velocity = 1
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    y1 += velocity
    if velocity > 0 and y1+robot.get_height() >= 480 and x1 >= 320:
        y1 = 480 - robot.get_height()
        x1+=velocity
    y2 += velocity
    if velocity > 0 and y2+robot.get_height() >= 480 and x2 <= 270:
        y2 = 480 - robot.get_height()
        x2-=velocity 

    y3 += velocity
    if velocity > 0 and y3+robot.get_height() >= 480 and x3 >= 320:
        y3 = 480 - robot.get_height()
        x3+=velocity 

    y4 += velocity
    if velocity > 0 and y4+robot.get_height()  >= 480 and x4 <= 270:
        y4 = 480 - robot.get_height()
        x4-=velocity 

    y5 += velocity
    if velocity > 0 and y5+robot.get_height() >= 480 and x5 >= 320:
        y5 = 480 - robot.get_height()
        x5+=velocity                
   
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, y1))
    screen.blit(robot, (x2, y2))
    pygame.display.flip()
 
    clock.tick(120)