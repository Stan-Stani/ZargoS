import pygame
import sys
import random

WINDOW_SIZE = (800, 600)

def handle_propulsion(x, y, x_component, y_component) :

    keys = pygame.key.get_pressed()
    

    if y > 7/10 * WINDOW_SIZE[1] :
        if keys[pygame.K_RIGHT]:
            x_component += 5
        if keys[pygame.K_LEFT]:
            x_component -= 5
        if keys[pygame.K_DOWN]:
            y_component += 5
        if keys[pygame.K_UP]:
            y_component -= 5
    else :
        pass

    x += x_component
    y += y_component

    return x, y, x_component, y_component


pygame.init()



screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()

eda_logo_large = pygame.image.load("static/eda-icon.png")
eda_logo = pygame.transform.scale(eda_logo_large, (50, 50))
eda_logo_size = eda_logo.get_size()

x, y = WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] * 9/10
x_component = 0
y_component = 0

while True :
    clock.tick(60)
    
    
   
   
    
    x, y, x_component, y_component = handle_propulsion(x, y, x_component, y_component)
    

    print (y_component)
    if y < 7/10 * WINDOW_SIZE[1] and abs(x_component) < 0.01 and abs(y_component) < 0.01:
        x, y = WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] * 9/10
        x_component, y_component = 0, 0


    red_amount = abs(x_component * 5) % 255
    blue_amount = abs(y_component * 5) % 255
    

    screen.fill((red_amount, 127, blue_amount))

    threshold_rect = pygame.Rect(0, 7/10 * WINDOW_SIZE[1], WINDOW_SIZE[0], 10)
    pygame.draw.rect(screen, 'black', threshold_rect)

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

# Friction
    x_component *= .97 # x_component = x_component * .9
    y_component *= .97
    

    pygame.display.update()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()