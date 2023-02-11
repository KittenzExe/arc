import pygame
import sys
from pypresence import Presence
import time
from pygame.locals import *
from datetime import datetime
import os

mainClock = pygame.time.Clock()
clientClock = pygame.time.Clock()
pygame.init()

window = pygame.display.set_mode((1080,720))
font = pygame.font.SysFont("arialrounded", 20)#, bold = pygame.font.Font.bold

logoH = pygame.image.load("resources/arc-logo-updated.png").convert_alpha()
logoH = pygame.transform.scale(logoH, (100, 100))

songFileLoadButton = pygame.Rect(63, 5, 200, 24)
text_value_SFL = ""
text_SFL = font.render(text_value_SFL, True, (100, 100, 255))
helperText1 = "map folder name"
helperText1Out = font.render(helperText1, True, (100, 100, 255))

fileLoadScreen = 1
fileLoadScreenEnter = False

while True:
    mainClock.tick(999) #fps cap
    window.fill((255,255,255))

    window.blit(logoH, (0,620))

    if fileLoadScreen == True:
        songFileLoadButton = pygame.Rect(63, 5, 200, 24)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position
            if songFileLoadButton.collidepoint(mouse_pos):
                # prints current location of mouse
                print('button was pressed at {0}'.format(mouse_pos))
                fileLoadScreenEnter = True
        if fileLoadScreen == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text_value_SFL = text_value_SFL[:-1]
                    text_SFL = font.render(text_value_SFL, True, (0, 0, 0))
            if event.type == pygame.TEXTINPUT:
                text_value_SFL += event.text
                text_SFL = font.render(text_value_SFL, True, (0, 0, 0))

    if fileLoadScreen == True:
        songFileLoadButton = pygame.Rect(63, 5, 200, 24)
        pygame.draw.rect(window, [155, 224, 241], songFileLoadButton)
        window.blit(text_SFL, (68, 5))
        window.blit(helperText1Out, (68, 25))
    
    pygame.display.flip()