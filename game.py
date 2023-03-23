import pygame
import sys
from pypresence import Presence
import time
import json
import math
from math import atan2, degrees, pi
from pygame.locals import *
from datetime import datetime
import os

mainClock = pygame.time.Clock()
clientClock = pygame.time.Clock()
pygame.init()

c = open('config.json')
cfig = json.load(c)

gamePreRender = 1
if gamePreRender == 1:
    debug = cfig['debug_mode']
    debugMode = debug['active']
    fps = debug['fps']
    display = cfig['display']
    display_x = display['x']
    display_y = display['y']
    display_f = display['is-fullscreen?']
    fps_limit = display['fps']

    if display_f == 1:
        window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((display_x,display_y))
    
    wx,wy = pygame.display.get_window_size()

    circle = pygame.image.load("resources/skin/circle.png").convert_alpha()
    circle = pygame.transform.scale(circle, ((display_y*0.9), (display_y*0.9)))

    paddle = pygame.image.load("resources/skin/paddle-fixed.png").convert_alpha()
    paddle = pygame.transform.scale(paddle, ((display_y*0.9), (display_y*0.9)))

    clicker0 = pygame.image.load("resources/skin/clicker0.png").convert_alpha()
    clicker1 = pygame.image.load("resources/skin/clicker1.png").convert_alpha()
    clicker2 = pygame.image.load("resources/skin/clicker2.png").convert_alpha()
    clicker0 = pygame.transform.scale(clicker0, (133, 89))
    clicker1 = pygame.transform.scale(clicker1, (133, 89))
    clicker2 = pygame.transform.scale(clicker2, (133, 89))

    font = pygame.font.SysFont("arialrounded", 20)#, bold = pygame.font.Font.bold

    menuListing = 1

    gameRender = 1

    player_pos = pygame.Vector2((wx/2),(wy/2))
    player = pygame.Rect(player_pos.xy, (2,2))
    player_center = pygame.Vector2(player.center)
    looking_vector = pygame.Vector2(1,1)

def update_fps():
    fps = int(mainClock.get_fps())
    roundfps = (fps /10)
    roundedfps = str(round(roundfps))+"0"   
    fps_text = font.render(roundedfps + " fps", 1, pygame.Color(0,0,0))
    return fps_text
def update_rawtime():
    rawtime = str(int(mainClock.get_rawtime()))
    rawtime_text = font.render(rawtime + " ms", 1, pygame.Color(0,0,0))
    return rawtime_text

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)

files = folders = 0
for _, dirnames, filenames in os.walk('songs'):
    files += len(filenames)
    folders += len(dirnames)
print ("{:,} files, {:,} folders".format(files, folders))

w, h = paddle.get_size()

click = 0

#main loop starts here
while True:
    mainClock.tick(fps_limit)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_z:
                click = 1
        if event.type == KEYDOWN:
            if event.key == K_x:
                click = 2

    mouse_pos = pygame.mouse.get_pos()
    delta = mouse_pos - player_center

    # Calculate the angle 
    angle_to_mouse = math.atan2(delta.y, delta.x)
    looking_vector.xy = (100*math.cos(angle_to_mouse), 100*math.sin(angle_to_mouse))
    angle = int(angle_to_mouse)

    dx = mouse_pos[0] - (wx/2)
    dy = mouse_pos[1] - (wy/2)
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)-90

    if gameRender == 1:
        #Render order is stacked ontop
        window.fill((255,255,255))

        fpsCheckBox = pygame.Rect(10 , 10, 25, 25)
        pygame.draw.rect(window, (255,255,255), fpsCheckBox)

        window.blit(circle, (((wx/2)-((display_y*0.9)/2)), ((wy/2)-((display_y*0.9)/2))))
        blitRotate(window, paddle, ((wx/2),(wy/2)), (w/2, h/2), degs)

        if click == 1:
           window.blit(clicker1, (0, wy-100)) 
        if click == 2:
           window.blit(clicker2, (0, wy-100)) 
        if click == 0:
           window.blit(clicker0, (0, wy-100)) 
            
        if fps == 1:
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

        if debugMode == 1:
            pygame.draw.line(window, (255,50,50), player_center, pygame.mouse.get_pos())

        fpsCheckBox2 = pygame.Rect(10 , 10, 25, 25)
        pygame.draw.rect(window, (0,255,0), fpsCheckBox2)

    pygame.display.flip()