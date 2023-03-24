import pygame
import pygame_menu

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Menu Window Resizer")

# Create a menu
menu = pygame_menu.Menu('Window Resizer', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_DEFAULT)

# Create a selector for window dimensions
dimensions_selector = menu.add.selector('Dimensions: ', [('640x480', (640, 480)), ('800x600', (800, 600)), ('1024x768', (1024, 768))])
dimensions_selector.set_default_value((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a button to resize the window
def resize_window():
    global surface, menu

    dimen_txtnum, index = dimensions_selector.get_value()
    dimen_txt, dimen_num = dimen_txtnum
    width, height=dimen_num

    # sets the window size
    surface = pygame.display.set_mode((width, height))

    # rescale the menu
    menu.resize(width, height)
    
    
menu.add.button('Resize Window', resize_window)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw the menu on the surface
    menu.draw(surface)
    menu.update(pygame.event.get())

    # Update the display
    pygame.display.update()
