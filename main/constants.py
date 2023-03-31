import pygame, pygame_menu
import customMenu_theme

pygame.init()

infoObject = pygame.display.Info()
# WIDTH = infoObject.current_w
# HEIGHT = infoObject.current_h
# SCREEN = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

# Test Variables
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
DIFFICULTY = 0

clock = pygame.time.Clock()
main_menu = pygame_menu.Menu(
    'Welcome to Puzzlify!', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme.customMenu_theme
)
accountStatsMenu = pygame_menu.Menu(
    'Account Statistics', 
    WIDTH, HEIGHT, 
    theme = customMenu_theme.customMenu_theme)