import pygame_menu
import sys
import os

# font settings
font = pygame_menu.font.FONT_NEVIS
widgetFontSize = 80
titleFontSize = 100

file = "main/images/puzzle1menu.png"
os.path.isfile(file)

if os.name == 'nt':
    file = "main\\images\\puzzle1menu.png"

# set path for custom image for use in theme
customImage = pygame_menu.baseimage.BaseImage(file,
                            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)

# create custom theme
customMenu_theme = pygame_menu.Theme(background_color = (238,242,226,0), 
                            title_background_color = (248,218,91),
                            title_font_color = (0,0,0,0),
                            title_font = font,
                            title_font_size = titleFontSize,
                            title_font_shadow=True,
                            widget_padding=25,
                            widget_background_color = (238,242,226,0),
                            widget_font = font,
                            widget_font_size = widgetFontSize,
                            widget_selection_effect = pygame_menu.widgets.LeftArrowSelection())

customMenu_theme.background_color=customImage