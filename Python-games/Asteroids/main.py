# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
#missing font module
pygame.display.flip()

robot = pygame.image.load("robot.png")
rock =  pygame.image.load("rock.png")
number = 10
to_right = False
to_left = False
to_up = False
to_down = False

rocks = []
xRocks = -200
yRocks = 480
for i in range(number):
    # causes the new random start position to be drawn immediately
    rocks.append([xRocks,yRocks])
 
clock = pygame.time.Clock()
xRobot = 640/2
yRobot = 480 - robot.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
              

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False      
    
    if to_right:
        xRobot += 2
        if xRobot > 640-robot.get_width():
            to_right = False
    if to_left:
        xRobot -= 2
        if xRobot < 0:
            to_left = False
    
    for i in range(number):
        yRobot = 480 - robot.get_height()
        rocks[i][1] += 1
        if rocks[i][1]+rock.get_height() > yRobot and rocks[i][0] in range(int(xRobot), int(xRobot+50)):
            rocks[i][0] = randint(0,width-rock.get_width())
            rocks[i][1] = randint(-200,-20)  
            lineBottom += 20
            pygame.display.flip()

        elif rocks[i][0] < -rock.get_width() or rocks[i][0] > width:
            # new random start point
            rocks[i][0] = randint(0,width-rock.get_width())
            rocks[i][1] = -randint(100,1000)
        
        elif rocks[i][1] > 480+rock.get_height()/2:
            quit()

    screen.fill((0, 0, 0))
    screen.blit(robot, (xRobot, yRobot))
    lineBottom = 30
    pygame.draw.line(screen, (255, 255, 230), (600, 10), (600, lineBottom), 4)
    
    for i in range(number):
        screen.blit(rock, (rocks[i][0], rocks[i][1]))
    pygame.display.flip()
 
    clock.tick(60)