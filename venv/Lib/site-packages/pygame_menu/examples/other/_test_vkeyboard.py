"""
pygame-menu
https://github.com/ppizarror/pygame-menu

EXAMPLE - TEST
Test virtual keyboard, https://github.com/Faylixe/pygame-vkeyboard.
"""

import sys

sys.path.insert(0, '../../')
sys.path.insert(0, '../../../')

import pygame
import pygame_menu
# noinspection PyUnresolvedReferences
from pygame_vkeyboard import *
from pygame_menu.examples import create_example_window

FPS = 30

surface = create_example_window('Example - Test', (500, 500))
clock = pygame.time.Clock()

menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)

user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)


def consumer(text: str) -> None:
    """
    Text from virtual keyboard to input.
    """
    user_name.set_value(text)


# Initializes and activates the keyboard
# noinspection PyUnresolvedReferences
layout = VKeyboardLayout(VKeyboardLayout.AZERTY)
# noinspection PyUnresolvedReferences
keyboard = VKeyboard(surface, consumer, layout)

while True:

    # Tick
    clock.tick(FPS)

    surface.fill((0, 0, 0))

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if keyboard.is_enabled():
                keyboard.disable()
            else:
                keyboard.enable()

    # Main menu
    menu.update(events)
    keyboard.update(events)

    menu.draw(surface)
    if keyboard.is_enabled():
        user_name.translate(0, -50)
        keyboard.draw(surface, force=True)
    else:
        user_name.translate(0, 0)

    # Flip surface
    pygame.display.flip()
