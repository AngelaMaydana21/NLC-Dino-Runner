import pygame.font

from dino_runner.utils.constants import SCREEN_WIDTH,SCREEN_HEIGHT
FONT_STYLE = 'freesansbold.ttf'
COLOR1 = (115, 119, 203)
COLOR2 = (236, 37, 90)

def get_data_element(points, type, x_pos, y_pos):

    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render('{}'.format(type)+': {}'.format(points), True, COLOR1)
    text_rect = text.get_rect()
    text_rect.center = (x_pos, y_pos)
    return text, text_rect

def get_centered_message(message, width = SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2):

    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, COLOR1)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect


