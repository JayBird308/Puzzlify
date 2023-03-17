
# Author: Chris Aromando - s1171536

import pygame, pygame.locals
import pygame_menu, pygame_menu.font, pygame_menu.themes, pygame_menu.widgets
import pygame_menu.locals, pygame_menu._widgetmanager, pygame_menu.baseimage

# Initialize Pygame
pygame.init()
pygame.mixer.music.load('main/track1.mp3')
pygame.mixer.music.play(-1) # -1 infinitely plays
pygame.mixer.music.set_volume(0.5)

# Define constants
SCREEN_DIMENSIONS = (pygame.display.Info().current_w, pygame.display.Info().current_h)
DEFAULT_DIMENSIONS_X, DEFAULT_DIMENSIONS_Y = 1280, 720
SCREEN_WIDTH, SCREEN_HEIGHT = 0, 0
VOLUME_LEVELS = {0: '0', 1: '', 2: '20', 3: '', 4: '40', 5: '', 6: '60', 7: '', 8: '80', 9: '', 10: '100'}
TOGGLE_FULL = False
SCREEN_FLAGS = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE
FULLSCREEN_FLAGS = pygame.FULLSCREEN | pygame.NOFRAME | pygame.DOUBLEBUF
DIMENSIONS_SELECTOR_ITEMS = [('1024x768', (1024, 768)), ('1280x720', (1280, 720)), ('1600x900', (1600, 900)), 
                            ('1920x1080', (1920, 1080)), ('Fullscreen', SCREEN_DIMENSIONS), ('Custom', (SCREEN_WIDTH, SCREEN_HEIGHT))]

# Create a surface & clock
surface = pygame.display.set_mode((DEFAULT_DIMENSIONS_X, DEFAULT_DIMENSIONS_Y), SCREEN_FLAGS)
FPSCLOCK = pygame.time.Clock()

# Create a menu
menu = pygame_menu.Menu('SETTINGS TEST', DEFAULT_DIMENSIONS_X, DEFAULT_DIMENSIONS_Y, theme=pygame_menu.themes.THEME_BLUE)
WidgetManager = pygame_menu._widgetmanager.WidgetManager(menu)

# Dimensions Selector
dimensions_selector = menu.add.selector('Dimensions: ', 
                                        items=DIMENSIONS_SELECTOR_ITEMS,
                                        selector_id='dimensions_selector', default=1)
dimensions_selector.hide()

# This is the main FRAME that holds it all
WidgetManager.frame_v(width=1000, height=600, frame_id='frame_v', background_color=(0, 145, 135), padding=0)
frame = menu.get_widget('frame_v')

# FRAME FOR TITLE BAR + FRAME FOR CONTENT
frame_title = menu.add.frame_h(width=1000, height=45, frame_id='frame_h', background_color=(20, 100, 150), padding=0)
frame_content = menu.add.frame_v(width=1000, height=225, padding=0)
frame.pack(frame_title)
frame.pack(frame_content)

# TITLE LABEL WIDGET
setting_widget = menu.add.label('Settings', padding=(0,15,0,15), label_id='settings_text', float=True, font_color=(255,255,255), font_size=30)
frame_title.pack(setting_widget, margin=(2, 2))

# Function called once the FRAME is closed
def close_settings():
    # Retrieve widgets by ID
    frame = menu.get_widget('frame_v')
    frame_title = menu.get_widget('frame_h')
    settings_text = menu.get_widget('settings_text')
    close_widget = menu.get_widget('close')
    slider = menu.get_widget('slider_id')
    selector = menu.get_widget('dimensions_selector')
    resize_button = menu.get_widget('resize_button')

    # Hide widgets
    frame.hide()
    frame_title.hide()
    settings_text.hide()
    close_widget.hide()
    slider.hide()
    selector.hide()
    resize_button.hide()

    settings_button = menu.get_widget('settings')
    if settings_button == type(None):
        pass
    else:
        settings_button.show()

# EXIT BUTTON WIDGET
close_widget = menu.add.button(
    'Close', 
    close_settings, 
    padding=(0, 5), 
    background_color=(25, 25, 25),
    font_color=(255,255,255),
    button_id='close'
)            
frame_title.pack(close_widget, align=pygame_menu.locals.ALIGN_RIGHT, margin=(2, 2))

# onchange function for volume slider
def set_volume(value):
    if value == 0:
        pygame.mixer.music.set_volume(0)
    elif value == 1:
        pygame.mixer.music.set_volume(0.1)
    elif value == 2:
        pygame.mixer.music.set_volume(0.2)
    elif value == 3:
        pygame.mixer.music.set_volume(0.3)
    elif value == 4:
        pygame.mixer.music.set_volume(0.4)
    elif value == 5:
        pygame.mixer.music.set_volume(0.5)
    elif value == 6:
        pygame.mixer.music.set_volume(0.6)
    elif value == 7:
        pygame.mixer.music.set_volume(0.7)
    elif value == 8:
        pygame.mixer.music.set_volume(0.8)
    elif value == 9:
        pygame.mixer.music.set_volume(0.9)
    elif value == 10:
        pygame.mixer.music.set_volume(1)

# SLIDER FOR VOLUME
slider = WidgetManager.range_slider(
    title='Volume: ', 
    default=3, 
    range_values=list(VOLUME_LEVELS.keys()),
    slider_text_value_enabled=False,
    value_format=lambda x: VOLUME_LEVELS[x],
    font_color=(255,255,255),
    rangeslider_id='slider_id',
    onchange=lambda value: set_volume(value)
    )
frame_content.pack(slider, margin=(2, 2), align=pygame_menu.locals.ALIGN_CENTER, vertical_position=pygame_menu.locals.POSITION_CENTER)

# WIDGET TO RESIZE WINDOW
dimensions_selector.show()
frame_content.pack(dimensions_selector, margin=(2,2), align=pygame_menu.locals.ALIGN_CENTER, vertical_position=pygame_menu.locals.POSITION_CENTER)

# Function for button to resize the window
def resize_window():
    global surface, SCREEN_DIMENSIONS
    dimen_txtnum, index = dimensions_selector.get_value()
    dimen_txt, dimen_num = dimen_txtnum
    width, height=dimen_num

    if dimen_num == SCREEN_DIMENSIONS:
        surface = pygame.display.set_mode((width, height), FULLSCREEN_FLAGS)
    else:
        surface = pygame.display.set_mode((width, height), SCREEN_FLAGS)
    
    # rescale the menu
    menu.resize(width, height)
    update_dimen_selector()
    update_settings_button_location()

# Button to resize the button ACCORDING to selector
resize_button = menu.add.button('Resize Window', resize_window, button_id='resize_button')
frame_content.pack(resize_button, margin=(2,2), align=pygame_menu.locals.ALIGN_CENTER, vertical_position=pygame_menu.locals.POSITION_CENTER)

def show_settings_widgets():
    # Hides the button that calls the settings Frame & Widgets
    settings_button = menu.get_widget('settings')
    settings_button.hide()

    # Retrieve widgets by ID
    frame = menu.get_widget('frame_v')
    frame_title = menu.get_widget('frame_h')
    settings_text = menu.get_widget('settings_text')
    close_widget = menu.get_widget('close')
    slider = menu.get_widget('slider_id')
    selector = menu.get_widget('dimensions_selector')
    resize_button = menu.get_widget('resize_button')

    # Show widgets
    frame.show()
    frame_title.show()
    settings_text.show()
    close_widget.show()
    slider.show()
    selector.show()
    resize_button.show()

# Settings button on the Menu to call the FRAME
menu.add.button(title='Settings', action=show_settings_widgets, button_id='settings', 
                     font_shadow=False, float=True)

def update_dimen_selector():
    # If the user manually resizes,
    # we change the selector to custom
    dimen_txtnum, index = dimensions_selector.get_value()
    dimen_txt, dimen_num = dimen_txtnum
    
    width, height=dimen_num
    s_width, s_height = (surface.get_width(), surface.get_height())
    
    if (width, height) != (s_width, s_height):
        NEW_LIST = [('1024x768', (1024, 768)), ('1280x720', (1280, 720)), ('1600x900', (1600, 900)), 
                    ('1920x1080', (1920, 1080)), ('Fullscreen', SCREEN_DIMENSIONS), ('Custom', (s_width, s_height))]
        dimensions_selector.update_items(NEW_LIST)
        dimensions_selector.set_value(5)
    menu.render()

def update_settings_button_location():
    settings_button = menu.get_widget('settings')
    x, y = surface.get_width(), surface.get_height()
    modified_x, modified_y = (x - (x / 2) - 70, y - (y / 2) - 60)
    settings_button.translate(modified_x, modified_y)

# Main function
def play():
    global SCREEN_WIDTH, SCREEN_HEIGHT, range_values_discrete, SCREEN_DIMENSIONS, surface, SCREEN_FLAGS, FULLSCREEN_FLAGS

    # HIDE ALL SETTINGS BY DEFAULT & set initial location
    close_settings()
    update_settings_button_location()

    # Main Loop to handle events
    while True:
        FPSCLOCK.tick(15)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.VIDEORESIZE:
                update_dimen_selector()
                if (event.w, event.h) == SCREEN_DIMENSIONS:
                    surface = pygame.display.set_mode((event.w, event.h), FULLSCREEN_FLAGS)
                else:
                    surface = pygame.display.set_mode((event.w, event.h), SCREEN_FLAGS)
                # Resize menu
                menu_w, menu_h = int(event.w), int(event.h)
                menu.resize(menu_w, menu_h)
                update_settings_button_location()

        menu.update(events)

        # Draw the menu on the surface
        menu.draw(surface)

        # Update the display
        pygame.display.update()

play()