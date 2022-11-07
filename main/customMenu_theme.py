import pygame_menu

customImage = pygame_menu.baseimage.BaseImage(image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
                                          drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER)

customMenu_theme = pygame_menu.Theme(background_color = (0,0,0,0), #transparent color
                            title_background_color = (255,0,0),
                            title_font_shadow=True,
                            widget_padding=25)

customMenu_theme.background_color=customImage