
# Author: Chris Aromando - s1171536

import pygame, pygame.locals
import pygame_menu, pygame_menu.font, pygame_menu.themes, pygame_menu.widgets
import pygame_menu.locals, pygame_menu._widgetmanager, pygame_menu.baseimage

# Define constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
range_values_discrete = {0: '0', 1: '', 2: '20', 3: '', 4: '40', 5: '', 6: '60', 7: '', 8: '80', 9: '', 10: '100'}

# Main play method to drive the program
def play():
    global SCREEN_WIDTH, SCREEN_HEIGHT, range_values_discrete

    # Initialize Pygame
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPSCLOCK = pygame.time.Clock()

    # Create a menu
    menu = pygame_menu.Menu('SETTINGS TEST', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
    WidgetManager = pygame_menu._widgetmanager.WidgetManager(menu)

    # Function called once the settings button is clicked
    def open_settings():
        # Hides the button that calls the settings Frame & Widgets
        settings_button = menu.get_widget('settings')
        settings_button.hide()

        # This is the main FRAME that holds it all
        WidgetManager.frame_v(width=1000, height=600, frame_id='frame_v', background_color=(0, 145, 135), padding=0)
        frame = menu.get_widget('frame_v')

        # FRAME FOR TITLE + FRAME FOR CONTENT
        frame_title = menu.add.frame_h(width=1000, height=45, frame_id='frame_h', background_color=(20, 100, 150), padding=0)
        frame_content = menu.add.frame_v(width=1000, height=225, padding=0)
        frame.pack(frame_title)
        frame.pack(frame_content)

        # TITLE LABEL WIDGET
        setting_widget = menu.add.label('Settings', padding=(0,15,0,15), label_id='settings_text', float=True, font_color=(255,255,255), font_size=30)
        frame_title.pack(setting_widget, margin=(2, 2))

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

        # SLIDER FOR VOLUME
        slider = WidgetManager.range_slider(
            title='Volume: ', 
            default=3, 
            range_values=list(range_values_discrete.keys()),
            slider_text_value_enabled=False,
            value_format=lambda x: range_values_discrete[x],
            font_color=(255,255,255),
            rangeslider_id='slider_id'
            )
        frame_content.pack(slider, margin=(2, 2), align=pygame_menu.locals.ALIGN_CENTER, vertical_position=pygame_menu.locals.POSITION_CENTER)

        # WIDGET TO RESIZE WINDOW

    # Settings button on the Menu to call the FRAME
    WidgetManager.button(title='Settings', action=open_settings, button_id='settings', font_shadow=False, align=pygame_menu.locals.ALIGN_CENTER)
    settings_button = menu.get_widget('settings')
    settings_button.set_position(SCREEN_WIDTH/2-50, SCREEN_HEIGHT/2)

    # Function called once the FRAME is closed
    def close_settings():
        frame = menu.get_widget('frame_v')
        frame_title = menu.get_widget('frame_h')
        settings_text = menu.get_widget('settings_text')
        close_widget = menu.get_widget('close')
        menu.remove_widget(frame)
        menu.remove_widget(frame_title)
        menu.remove_widget(settings_text)
        menu.remove_widget(close_widget)

        settings_button = menu.get_widget('settings')
        settings_button.show()

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