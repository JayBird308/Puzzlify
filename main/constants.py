import pygame, pygame_menu
# import ctypes
from typing import Tuple, Any, Optional, List
from customMenu_theme import *

pygame.init()

infoObject = pygame.display.Info()
# SCREEN = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# WIDTH = infoObject.current_w
# HEIGHT = infoObject.current_h
FPS = 60

clock: Optional['pygame.time.Clock'] = pygame.time.Clock()
main_menu: Optional['pygame_menu.Menu'] = pygame_menu.Menu(
    '     Welcome to Puzzlify!', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme
)