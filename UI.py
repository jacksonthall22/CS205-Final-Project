import pygame, sys
from pygame.locals import *

GREEN = [15, 85, 15]
BACKGROUND = [169, 169, 169]

pygame.init()
''' Add icon image for new window '''
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

''' Create window, change window title and background color '''
SCREEN = pygame.display.set_mode((1040, 560))
pygame.display.set_caption('Othello')
SCREEN.fill(BACKGROUND)

''' Add title image '''
title = pygame.image.load('title.png')
SCREEN.blit(title, (20, 10))

''' Parameters needed to draw each tile '''
WIDTH = 64
HEIGHT = 64
START_LEFT = 500
START_TOP = 15
SPACING = 2

''' Main Loop to display each tile '''
# TODO change '8' to the size of the board object
for row in range(8):
    for column in range(8):
        pygame.draw.rect(SCREEN, GREEN, (START_LEFT + (SPACING * column) + (WIDTH * column),
                                         START_TOP + (SPACING * row) + (HEIGHT * row),
                                         WIDTH,
                                         HEIGHT))

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()