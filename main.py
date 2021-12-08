# GAME INITIALIZATION
import pygame, sys

pygame.init()

# GAME VARIABLES
size = [1080, 720]
screen = pygame.display.set_mode(size)
bg_color = (255,255,255)

# CREATING THE SHIP
ship = pygame.image.load('data/ship.png')
ship_x = 700
ship_y = 360
ship_left = False
ship_right = False 

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ship_left = True 
            if event.key == pygame.K_d:
                ship_right = True
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_a:
                ship_left = False 
            if event.key == pygame.K_d:
                ship_right = False

    if ship_left: 
        ship_x -= 1
    if ship_right: 
        ship_x += 1

    screen.fill(bg_color)
    

    screen.blit(ship, (ship_x, ship_y))
    pygame.display.flip()
