"""
Test file.
"""
import pygame_menu
from pygame_menu.examples import create_example_window

surface = create_example_window('Example - Simple', (600, 400))
menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)


def save_to_file() -> None:
    """Save data to a file."""
    with open('_test_saveparams.cfg', 'w') as f:
        f.write(f'USERNAME={menu.get_widget("username").get_value()}')


menu.add.text_input('Name: ', textinput_id='username', default='John Doe', maxchar=10)
menu.add.button('Save', save_to_file)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
