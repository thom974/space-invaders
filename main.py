# GAME INITIALIZATION
import pygame, sys

pygame.init()

# GAME VARIABLES
size = [1080, 720]
screen = pygame.display.set_mode(size)

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
