"""
Test.
"""
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))
theme = pygame_menu.themes.THEME_BLUE
theme.background_color = '#ddd'
theme.title_background_color = '#333'
theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE
theme.title_font_color = '#666'
theme.title_font_shadow = False
menu = pygame_menu.Menu('Welcome', 600, 400, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Button 1')
menu.add.vertical_fill()
menu.add.button('Button 2')
menu.add.vertical_fill()
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(surface)
