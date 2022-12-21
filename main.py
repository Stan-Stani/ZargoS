import pygame
import sys
import random



pygame.init()

WINDOW_SIZE = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()

eda_logo_large = pygame.image.load("static/eda-icon.png")
eda_logo = pygame.transform.scale(eda_logo_large, (75, 75))
eda_logo_size = eda_logo.get_size()

x, y = 0, 0
x_component = 5
y_component = 5

while True :
    clock.tick(60)

   
    

    


    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x_component += 5
    if keys[pygame.K_LEFT]:
        x_component -= 5
    if keys[pygame.K_DOWN]:
        y_component += 5
    if keys[pygame.K_UP]:
        y_component -= 5

    x += x_component
    y += y_component


    red_amount = abs(x_component * 5) % 255
    blue_amount = abs(y_component * 5) % 255
    

    screen.fill((red_amount, 127, blue_amount))

    keys = pygame.key.get_pressed()

    screen.blit(eda_logo, (x, y))

    # x += x_component * random.random() * 10
    if x >= 800 - eda_logo_size[0]:
        x = 800 - eda_logo_size[0]
        x_component *= -1
    elif x <= 0:
        x = 0
        x_component *= -1
    
    if y >= 600 - eda_logo_size[1]:
        y = 600 - eda_logo_size[1]
        y_component *= -1
    elif y <= 0:
        y = 0
        y_component *= -1

    x_component *= .9 # x_component = x_component * .9
    y_component *= .9
    

    pygame.display.update()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()