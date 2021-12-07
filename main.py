from pypong import *
pygame.init()

screen =pygame.display.set_mode((640, 480))

# define a variable to control the main loop
running = True
started = False

setup_init(pygame, screen)

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        move_player(event)
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "s":
                started = True
    if started:
        update_game(pygame, screen)
    pygame.display.update()
