# the robot should catch the coin and avoid the monsters

import os
import pygame
from pygame.locals import *
from random import randint
from random import choice
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(("Monsters invasion"))
# font module is unavaiable on my machine so I couldn't include points, which is why
# I have added a line at the bottom of the screen which increases with each hit of the coin
# and once it reaches the end of the screen the level is passed
robot = pygame.image.load("robot.png")
coin = pygame.image.load("coin.png")
monster =  pygame.image.load("monster.png")
# number of monsters
number = 15
# number of dots, which are only distractions
numberDots = 50

xmonsters = -200
ymonsters = 480

xDots = -10
yDots = 480

xRobot = randint(0, width-robot.get_width())
yRobot = randint(0, height-robot.get_height())

xCoin = 300
yCoin = 200

to_right = False
to_left = False
to_up = False
to_down = False
double_speed = False

monsters = []
dots = []

pygame.display.flip()

# random location of dots and monsters
for i in range(numberDots):  
    dots.append([xDots, yDots])

for i in range(number):
    monsters.append([xmonsters,ymonsters])

clock = pygame.time.Clock()
endLine = 20
while True:
    for event in pygame.event.get():
        # robot movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True    

            if event.key == pygame.K_LSHIFT:
                double_speed = True

            coinMiddleX = xCoin+coin.get_width()/2
            coinMiddleY = yCoin+coin.get_height()/2

            # robot hit coin, coin appears in a random location
            # possible improvement here would be the area which hits the coin, currently the hit
            # is detected only in the middle of the coin

            hit_x = coinMiddleX >= xRobot and coinMiddleX <= xRobot+robot.get_width()
            hit_y = coinMiddleY >= yRobot and coinMiddleY <= yRobot+robot.get_height()
            
            if hit_x and hit_y:
                xCoin = randint(0, width-coin.get_width())
                yCoin = randint(0, height-coin.get_height())
                endLine += 20
                pygame.draw.line(window, "green", (0,470), (endLine, 470), 3)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False         
            if event.key == pygame.K_LSHIFT:
                double_speed = False
        if event.type == pygame.QUIT:
            exit()
        elif endLine >= 640:
            print("Level complete")
            exit()
    if to_right:
        xRobot += 4
    if to_left:
        xRobot -= 4
    if to_up:
        yRobot -= 4
    if to_down:
        yRobot += 4        
    if double_speed and to_right:
        xRobot += 8
    # when left Shift is pressed the robot moves twice as fast
    if double_speed and to_left:
        xRobot -= 8 
    if double_speed and to_up:
        yRobot -= 8 
    if double_speed and to_down:
        yRobot += 8            
    
    # if the robot reaches the end of the screen, it appears back from the other side, which makes it
    # easier to escape but also more dangerous as it could hit a monster on the other side
    if xRobot >= width:
        xRobot = 0
    if yRobot >= height:
        yRobot = 0
    if xRobot+robot.get_width() < 0:
        xRobot = 640-robot.get_width()
    if yRobot+robot.get_height() < 0:
        yRobot = 480-robot.get_height()

    for i in range(number):
        # monster and dots movement down
        monsters[i][1] += 1
        dots[i][1] += 2
        
        monsterMiddleX = monsters[i][0] + monster.get_width()/2
        monsterMiddleY = monsters[i][1] + monster.get_height()/2

        # area of improvement - the robot currently hits the middle of the monster

        hit_x = monsterMiddleX >= xRobot and monsterMiddleX <= xRobot+robot.get_width()
        hit_y = monsterMiddleY >= yRobot and monsterMiddleY <= yRobot+robot.get_height()

        if monsters[i][0] >= 0 and monsters[i][0] <= 620 and monsters[i][1] <= height-monster.get_height() and monsters[i][1] >= 0 and hit_x and hit_y:
            print("You hit a monster") 
            endLine = 20
            pygame.draw.line(window, "green", (0,470), (endLine, 470), 3)
            quit()

        elif monsters[i][1] > height:
            # new random start point
            monsters[i][0] = randint(0,width-monster.get_width())
            monsters[i][1] = -randint(100,1000)
            
        elif dots[i][1] > height:
            dots[i][0] = randint(0,width-5)
            dots[i][1] = -randint(100,1000)

    window.fill((255, 255, 255))
    
    for i in range(number):   
        window.blit(monster, (monsters[i][0], monsters[i][1]))
    
    colours = ["pink", "green", "red"]
    sizes = [5, 3, 4, 6, 10]
    
    # I couldn't figure out why the dots flash rather than appearing in random colours and sizes
    # which was the goal
    for i in range(numberDots):
        pygame.draw.circle(window, pygame.Color(choice(colours)), (dots[i][0], dots[i][1]), choice(sizes))

    window.blit(robot, (xRobot, yRobot))
    window.blit(coin, (xCoin, yCoin))
    pygame.draw.line(window, "green", (0,470), (endLine, 470), 3)
    pygame.display.flip()

    clock.tick(60)