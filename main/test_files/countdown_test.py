import pygame
import pygame_menu
import pygame_menu._widgetmanager
import pygame_menu.themes
import pygame_menu.events

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()
TIMEOUT = True

# Define the function to be called on timeout
def on_timeout():
    global TIMEOUT
    if TIMEOUT == True:
        print('Countdown timer has finished!')
        TIMEOUT = False


# Create the menu
menu = pygame_menu.Menu('Countdown Clock Example', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
WidgetManager = pygame_menu._widgetmanager.WidgetManager(menu)

# Define the countdown timer update function
def update_countdown_timer():
    # Calculate the time remaining
    remaining_time = max(0, countdown_end_time - pygame.time.get_ticks())
    minutes = remaining_time // 60000
    seconds = (remaining_time // 1000) % 60

    # Update the countdown timer label
    countdown_timer.set_title('{:01d}:{:02d}'.format(minutes, seconds))

    # If the time has run out, call the on_timeout function
    if remaining_time == 0:
        on_timeout()

# Create the countdown timer label and add it to the menu
countdown_timer = WidgetManager.label('00:00', font_size=50, font_color=(0,0,0))

# Set the end time for the countdown timer
countdown_end_time = pygame.time.get_ticks() + 91000 # 1 second = 1000 ticks

while True:
    FPSCLOCK.tick(60)
    update_countdown_timer()

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
