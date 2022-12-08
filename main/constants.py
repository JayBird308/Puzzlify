import pygame, pygame_menu, ctypes
from typing import Tuple, Any, Optional, List
from customMenu_theme import *

pygame.init()

USER32 = ctypes.windll.user32

# WIDTH = USER32.GetSystemMetrics(0) # Monitor Resolution Width
# HEIGHT = USER32.GetSystemMetrics(1) # Monitor Resolution Height

# Testing Window Dimensions
WIDTH = 1280
HEIGHT = 720

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60

clock: Optional['pygame.time.Clock'] = pygame.time.Clock()
main_menu: Optional['pygame_menu.Menu'] = pygame_menu.Menu(
    '     Welcome to Puzzlify!', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme
)