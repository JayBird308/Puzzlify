
# Author: Chris Aromando - s1171536

import pygame, pygame.locals
import pygame_menu, pygame_menu.font, pygame_menu.themes, pygame.color, pygame_menu.baseimage
import pygame_menu.widgets, pygame_menu.locals, pygame_menu._widgetmanager
import random

# Define constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clickable Banner Test")
FPSCLOCK = pygame.time.Clock()

# Create a menu
menu = pygame_menu.Menu('Clickable Banner Test', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_SOLARIZED)
WidgetManager = pygame_menu._widgetmanager.WidgetManager(menu)

selection_color_test = (125,0,0,255)
selection_test = pygame_menu.widgets.LeftArrowSelection(arrow_size=(20, 30), arrow_right_margin=5, blink_ms=500)

banner_image_file = 'main\\test_files\\banner_test.png'
banner_image = pygame_menu.baseimage.BaseImage(banner_image_file, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
banner_image.scale(0.5, 0.5, True)

WidgetManager.clock(
    clock_format='%I:%M:%S %p',
    clock_id='clock_test_id',
)

# PROGRESS CONSTANT
UPDATE_VALUE = False

def toggle_onchange(current_state_value, **kwargs):
    global UPDATE_VALUE
    if current_state_value == True:
        UPDATE_VALUE = True
        print('Toggled to TRUE')
    elif current_state_value == False:
        UPDATE_VALUE = False
        print('Toggled to FALSE')

def add_to_progress():
    global UPDATE_VALUE
    progress_bar = menu.get_widget('progressbar_test_id')
    current_num = progress_bar.get_value()
    if UPDATE_VALUE == True:
        if current_num == 100:
            progress_bar.set_value(0)
        else:
            progress_bar.set_value(current_num + 5)
        menu.render()
    else:
        print('CANNOT UPDATE!~~')

WidgetManager.toggle_switch(
    title='Toggle Add Progress',
    default=False,
    toggleswitch_id='toggleswitch_test_id',
    onchange=toggle_onchange
)
WidgetManager.progress_bar(
    title='Progress Bar',
    default=50,
    progressbar_id='progressbar_test_id'
)

b1 = WidgetManager.banner(
    image=banner_image,
    action=add_to_progress,
    align=pygame_menu.locals.ALIGN_LEFT,
    border_inflate=(5,5),
    button_id='banner_test_id',
    selection_color=[125,0,0,255],
    selection_effect=selection_test,
    padding=(0,25,0,25),
    shadow_type='rectangular',
    shadow_radius=100,
    shadow_width=25
)

test_image = pygame_menu.BaseImage(
    image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU
).scale(0.4,0.4)

b2 = WidgetManager.banner(
    image=test_image,
    action=None,
    align=pygame_menu.locals.ALIGN_RIGHT,
    border_inflate=(5,5),
    button_id='banner_test_id_2',
    selection_color=[125,0,0,255],
    selection_effect=selection_test,
    padding=(0,0,0,0),
    shadow_type='ellipse',
    shadow_radius=100,
    shadow_width=25
)

# Create a Frame widget to hold the images
frame = WidgetManager.frame_h(1000, 600)
frame.pack(b1, align=pygame_menu.locals.ALIGN_LEFT, vertical_position=pygame_menu.locals.POSITION_CENTER)
frame.pack(b2, align=pygame_menu.locals.ALIGN_LEFT, vertical_position=pygame_menu.locals.POSITION_CENTER)

# Main play method to drive the program
def play():
    while True:
        FPSCLOCK.tick(60)

        # Handle events
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