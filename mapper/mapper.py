import pygame
import sys
from pypresence import Presence
import time
import json
from pygame.locals import *
from datetime import datetime
import os

mainClock = pygame.time.Clock()
clientClock = pygame.time.Clock()
pygame.init()

window = pygame.display.set_mode((1080,720))
font = pygame.font.SysFont("arialrounded", 20)#, bold = pygame.font.Font.bold
wx,wy = pygame.display.get_window_size()

logoH = pygame.image.load("resources/arc-logo-updated.png").convert_alpha()
logoH = pygame.transform.scale(logoH, (100, 100))

songFileLoadButton = pygame.Rect(63, 5, 200, 24)
text_value_SFL = ""
text_SFL = font.render(text_value_SFL, True, (100, 100, 255))
song_info = ""
text_info_print = font.render(song_info, True, (100, 100, 255))
helperText1 = "map folder location and name"
helperText1Out = font.render(helperText1, True, (100, 100, 255))

fileLoadScreen = 1
fileLoadScreenEnter = False

c = open('config.json')
cfig = json.load(c)

debug = cfig['debug_mode']
debugMode = debug['active']
display = cfig['display']
fps_limit = display['fps']

fpsON = 1
def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render(fps + " fps", 1, pygame.Color(0,0,0))
	return fps_text
rawTimeON = 1
def update_rawtime():
    rawtime = str(int(mainClock.get_rawtime()))
    rawtime_text = font.render(rawtime + " ms", 1, pygame.Color(0,0,0))
    return rawtime_text

while True:
    mainClock.tick(fps_limit) #fps cap
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    song_info = str(os.listdir("songs/"+text_value_SFL))
                    text_info_print = font.render(song_info, True, (0, 0, 0))

    if fileLoadScreen == True:
        songFileLoadButton = pygame.Rect(63, 5, 400, 24)
        pygame.draw.rect(window, [155, 224, 241], songFileLoadButton)
        window.blit(text_SFL, (68, 5))
        window.blit(text_info_print, (69, 100))
        window.blit(helperText1Out, (68, 25))
    
    if fpsON == 1:
        newFPS = int(mainClock.get_fps())
        rawTime = int(mainClock.get_rawtime())
        fpsR = (255,0,0)
        fpsO = (255,165,0)
        fpsY = (255,255,0)
        fpsL = (165,255,0)
        fpsG = (0,255,0)
        fpsBox = pygame.Rect((wx - 85) , (wy - 30), 100, 25)
        rawtimeBox = pygame.Rect((wx - 70) , (wy - 56), 100, 23)
        if newFPS >= (fps_limit / 6):
            pygame.draw.rect(window, fpsR, fpsBox)
        if newFPS >= (fps_limit / 5):
            pygame.draw.rect(window, fpsO, fpsBox)
        if newFPS >= (fps_limit / 4):
            pygame.draw.rect(window, fpsY, fpsBox)
        if newFPS >= (fps_limit / 3):
            pygame.draw.rect(window, fpsL, fpsBox)
        if newFPS >= (fps_limit / 2):
            pygame.draw.rect(window, fpsG, fpsBox)
        if rawTime <= 5:
            pygame.draw.rect(window, fpsR, rawtimeBox)
        if rawTime == 4:
            pygame.draw.rect(window, fpsO, rawtimeBox)
        if rawTime == 3:
            pygame.draw.rect(window, fpsY, rawtimeBox)
        if rawTime == 2:
            pygame.draw.rect(window, fpsL, rawtimeBox)
        if rawTime == 1:
            pygame.draw.rect(window, fpsG, rawtimeBox)
        window.blit(update_fps(), ((wx - 80),(wy - 31)))
        window.blit(update_rawtime(), ((wx - 69),(wy - 56)))
    
    pygame.display.flip()