import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))
images = (pygame.image.load("robot.png"),
          pygame.image.load("robot.png"))
robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
step = robot.get_width()/10
beginning = 0+width
beginning2 = 10+height
end = 610-width*3
beginning2 = 5+height
end2 = 480-height*2
for i in range(10):
    for x in range(beginning, end, 45):
        for y in range(beginning2, end2, 23):
            window.blit(robot, (x, y))    
            x+=10
            y-=10

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


