import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x1 = 640/2
y1 = 480/2
x2 = 300
y2 = 300

to_right1 = False
to_right2 = False
to_left1 = False
to_left2 = False
to_up1 = False
to_down1 = False
to_up2 = False
to_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_a:
                to_left2 = True    
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_d:
                to_right2 = True    
            if event.key == pygame.K_UP:
                to_up1 = True
            if event.key == pygame.K_w:
                to_up2 = True

            if event.key == pygame.K_DOWN:
                to_down1 = True 
            if event.key == pygame.K_s:
                to_down2 = True        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                to_left1 = False
                to_left2 = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                to_right1 = False
                to_right2 = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                to_up1 = False
                to_up2 = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                to_down1 = False
                to_down2 = False        

        if event.type == pygame.QUIT:
            exit()

    if to_right1:
        x1 += 2
        if x1 > 640-robot.get_width():
            to_right1 = False
    if to_right2:
        x2 += 2
        if x2 > 640-robot.get_width():
            to_right2 = False        
    if to_left1:
        x1 -= 2
        if x1 < 0:
            to_left1 = False
    if to_left2:
        x2 -= 2
        if x2 < 0:
            to_left2 = False        
    if to_up1:
        y1 -= 2
        if y1 < 0:
            to_up1 = False
    if to_up2:
        y2 -= 2
        if y2 < 0:
            to_up2 = False        
    if to_down1:
        y1 += 2 
        if y1 > 480-robot.get_height():
            to_down1 = False  
    if to_down2:
        y2 += 2
        if y2 > 480-robot.get_height():
            to_down2 = False               

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)