import pygame
import math
import os
os.environ["SDL_VIDEODRIVER"] = "directfb" 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
ball = pygame.image.load("ball.png")
 
x = 0
y = 0
ball_x = 2
ball_y = 2
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    x += ball_x
    y += ball_y
 
    if x == 0 or x+ball.get_width() == width:
        ball_x = -ball_x
    if y == 0 or y+ball.get_height() == height:
        ball_y = -ball_y
 
    screen.fill((0, 0, 0))
    screen.blit(ball, (x, y))
    pygame.display.flip()
 
    clock.tick(60)