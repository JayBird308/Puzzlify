
# Author: Chris Aromando - s1171536

import pygame, pygame.locals
import pygame_menu, pygame_menu.font, pygame_menu.themes, pygame_menu.widgets
import pygame_menu.locals, pygame_menu._widgetmanager, pygame_menu.baseimage

# Define constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Main play method to drive the program
def play():
    global SCREEN_WIDTH, SCREEN_HEIGHT

    # Initialize Pygame
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPSCLOCK = pygame.time.Clock()

    # Create a menu
    menu = pygame_menu.Menu('SETTINGS TEST', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
    WidgetManager = pygame_menu._widgetmanager.WidgetManager(menu)

    # Single value
    menu.add.range_slider(
        title='Choose a number', 
        default=50, 
        range_values=(0, 100), 
        increment=1,
        rangeslider_id='range_slider',
        value_format=lambda x: str(int(x))
        )

    # Range
    menu.add.range_slider(
        title='Pick a range', 
        default=(7, 10), 
        range_values=(1, 10), 
        increment=1
        )

    # Discrete value
    range_values_discrete = {0: '0', 1: '20', 2: '40', 3: '60', 4: '80', 5: '100'}
    menu.add.range_slider(
        title='Pick a letter', 
        default=3, 
        range_values=list(range_values_discrete.keys()),
        slider_text_value_enabled=False,
        value_format=lambda x: range_values_discrete[x]
        )

    # Numeric discrete range
    menu.add.range_slider(
        title='Pick a discrete range', 
        default=(2, 4), 
        range_values=[0, 1, 2, 3, 4, 5], 
        increment=1
        )

    # Main Loop to handle events
    while True:
        FPSCLOCK.tick(15)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        menu.update(events)

        # Draw the menu on the surface
        menu.draw(surface)

        # Update the display
        pygame.display.flip()

play()