# import the pygame module, so you can use it
from pypong import *
import pygame
# initialize the pygame module
pygame.init()

screen =pygame.display.set_mode((640, 480))
setup_init(pygame, screen)

# define a variable to control the main loop
running = True

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

    pygame.display.update()