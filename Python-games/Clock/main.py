import pygame
import math
from datetime import datetime

time = datetime.now()
timeHour = time.hour
timeMinute = time.minute
timeSecond = time.second
pygame.init()
display = pygame.display.set_mode((640, 480))


clock = pygame.time.Clock()

angle1 = 0
angle2 = .6
angle3 = .9
radius = 150
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    lineX= 320+math.cos(angle1+2*math.pi*1/10)*radius
    lineY = 240+math.sin(angle1+2*math.pi*1/10)*radius
    

    
    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 200)
    pygame.draw.circle(display, (0, 0, 0), (320, 240), 196)
    pygame.draw.circle(display, (0, 0, 0), (320, 240), 15)
     
    line = pygame.draw.line(display, (255, 255, 230), (320, 240), (lineX, lineY), 4)
    pygame.display.flip()

    angle1 += 0.115
    angle2 += 0.0006
    angle3 += 0.00006
    clock.tick(1)        