import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle1 = 0
angle2 = angle1+36
angle3 = angle2+36
angle4 = angle3+36
angle5 = angle4+36
angle6 = angle5+36
angle7 = angle6+36
angle8 = angle7+36
angle9 = angle8+36
angle10 = angle9+36
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320+math.cos(angle1)*100-robot.get_width()/2
    y = 240+math.sin(angle1)*100-robot.get_height()/2
    x2 = 320+math.cos(angle2)*100-robot.get_width()/2
    y2 = 240+math.sin(angle2)*100-robot.get_height()/2
    x3 = 320+math.cos(angle3)*100-robot.get_width()/2
    y3 = 240+math.sin(angle3)*100-robot.get_height()/2
    x4 = 320+math.cos(angle4)*100-robot.get_width()/2
    y4 = 240+math.sin(angle4)*100-robot.get_height()/2
    x5 = 320+math.cos(angle5)*100-robot.get_width()/2
    y5 = 240+math.sin(angle5)*100-robot.get_height()/2
    x6 = 320+math.cos(angle6)*100-robot.get_width()/2
    y6 = 240+math.sin(angle6)*100-robot.get_height()/2
    x7 = 320+math.cos(angle7)*100-robot.get_width()/2
    y7 = 240+math.sin(angle7)*100-robot.get_height()/2
    x8 = 320+math.cos(angle8)*100-robot.get_width()/2
    y8 = 240+math.sin(angle8)*100-robot.get_height()/2
    x9 = 320+math.cos(angle9)*100-robot.get_width()/2
    y9 = 240+math.sin(angle9)*100-robot.get_height()/2
    x10 = 320+math.cos(angle10)*100-robot.get_width()/2
    y10 = 240+math.sin(angle10)*100-robot.get_height()/2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    window.blit(robot, (x3, y3))
    window.blit(robot, (x4, y4))
    window.blit(robot, (x5, y5))
    window.blit(robot, (x6, y6))
    window.blit(robot, (x7, y7))
    window.blit(robot, (x8, y8))
    window.blit(robot, (x9, y9))
    window.blit(robot, (x10, y10))
    
    pygame.display.flip()

    angle1 += 0.01
    angle2 += 0.01
    angle3 += 0.01
    angle4 += 0.01
    angle5 += 0.01
    angle6 += 0.01
    angle7 += 0.01
    angle8 += 0.01
    angle9 += 0.01
    angle10 += 0.01
    clock.tick(60)