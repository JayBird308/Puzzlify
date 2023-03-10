import pygame, pygame_menu, pygame_menu.widgets
import customMenu_theme

pygame.init()

# Set up the window
WIDTH = 1280
HEIGHT = 720
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60
SCREEN = pygame.display.set_mode(WINDOW_SIZE)

# Set up the clock
clock = pygame.time.Clock()

### --> Main Menu Buttons <--- ##
main_menu = pygame_menu.Menu(
    'Welcome to Puzzlify!', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme.customMenu_theme
)
label = main_menu.add.label('0')

def update():
    label.set_title('2')
    main_menu.render()

button = main_menu.add.button('Update', update)

current_menu = main_menu

# Main Loop
while True:
    clock.tick(FPS)

    # Event Handling
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit(0)
    current_menu.update(events)
        
    # If NOT enabled, enable it
    # If enabled, draw to SCREEN
    if current_menu.is_enabled() == False:
        current_menu.enable()
    if current_menu.is_enabled() == True:
        current_menu.draw(SCREEN)

    pygame.display.update()