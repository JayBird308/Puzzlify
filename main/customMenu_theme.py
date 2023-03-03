import pygame_menu, pygame_menu.widgets, pygame_menu.locals
import os

# font settings
font = pygame_menu.font.FONT_NEVIS
widgetFontSize = 50
titleFontSize = 80

file = "main/images/puzzle0menu.png"
os.path.isfile(file)

if os.name == 'nt':
    file = "main\\images\\puzzle0menu.png"

# set path for custom image for use in theme
customImage = pygame_menu.baseimage.BaseImage(file,
                            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)

# create custom theme
customMenu_theme = pygame_menu.Theme(
                            title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE, 
                            title_background_color = (80,120,240),
                            title_font_color = (10,10,10),
                            title_font = font,
                            title_font_size = titleFontSize,
                            title_font_shadow=False,
                            widget_alignment = pygame_menu.locals.ALIGN_CENTER,
                            widget_border_width = 2,
                            widget_margin = (0, 25),
                            widget_padding=25,
                            widget_background_color = (80,120,240),
                            widget_font = font,
                            widget_font_color = (50,50,50),
                            widget_font_shadow = True,
                            widget_font_shadow_offset = 1,
                            widget_font_size = widgetFontSize,
                            widget_selection_effect = pygame_menu.widgets.HighlightSelection(),
                            widget_tab_size = 25,
                            selection_color = (220,230,255))


customMenu_theme.background_color=customImage