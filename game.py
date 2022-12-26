#HOW TO EXPORT TO EXE
#in vscode terminal, run:
#   python -m auto_py_to_exe

import pygame
mainClock = pygame.time.Clock()
import sys
from pypresence import Presence
import time
from pygame.locals import *

#firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#int game
pygame.init()
#change this if you want to die!
gameLoop = 1
gameruntime = True #why tf does this exist
menu = True
lobby = False
game  = False

# Fetch the service account key JSON file contents
cred = credentials.Certificate("arc-data-base-firebase-adminsdk-1vqh2-57729cc1ce.json")
firebase_admin.initialize_app(cred)
#main game loop for loading
if gameLoop == 1:
    #other variables for nesting
    rescaleValues = 1

    #game variables
    play = 0
    settings = 0
    gameplay = 0

    #icon image load and display
    programIcon = pygame.image.load('resources\Arc-logo.png')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption('arc')

    #window set
    window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    wx,wy = pygame.display.get_window_size()

    #discord
    presenceON = 1
    client_id = "1052448160972292237"
    RPC = Presence(client_id)
    RPC.connect()

    #image loading
    logo = pygame.image.load("resources\Arc-logo.png").convert_alpha()
    menuSettings = pygame.image.load("resources\Arc-menu-settings.png").convert_alpha()
    menuPlay = pygame.image.load("resources\Arc-menu-play.png").convert_alpha()

    #font loading
    font = pygame.font.SysFont("Arial", 20)

    #sound loading
    select = pygame.mixer.Sound("sounds\select.wav")

#rescaling images
if rescaleValues == 1:
    #from 1,000 x 1,000 to desired size
    rescaleCenter = ((500,500))
    logo = pygame.transform.scale(logo, rescaleCenter)
    rescaleCenter2 = ((300,300))
    logo2 = pygame.transform.scale(logo, rescaleCenter2)
    rescaleCenter3 = ((200,200))
    menuSettings = pygame.transform.scale(menuSettings, rescaleCenter3)
    rescaleCenter4 = ((200,200))
    menuPlay = pygame.transform.scale(menuPlay, rescaleCenter4)
    pygame.display.flip()

events = pygame.event.get()

#Update def for fps
fpsON = 1
def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color(0,0,0))
	return fps_text

hitNum = 0 #100, 200, 300
comboNum = 0 #x multiplyer
scoreCalc1 = hitNum * comboNum
def scoreCalc():
    print("test")

#firebase check
ref = db.reference('https://console.firebase.google.com/u/0/project/arc-data-base/database/arc-data-base-default-rtdb/data/~2F/Users')
print(ref.get())

while menu == True:
    #fps update
    mainClock.tick(0)
    window.fill((255,255,255))

    if play == 0:
        window.blit(logo, (((wx/2)-250),((wy/2)-250)))
    
    if play == 1:
        window.blit(logo2, (((wx/2)-150),((wy/2)-150)))

        window.blit(menuSettings, (((wx/2)-350),((wy/2)-100)))
        window.blit(menuPlay, (((wx/2)+150),((wy/2)-100)))

        #fps update display
        if fpsON == 1:
            bar = (241, 241, 255)
            bar1 = pygame.Rect(0, 0, wx, 70)
            pygame.draw.rect(window, bar, bar1)
            newFPS = int(mainClock.get_fps())
            fpsR = (255,0,0)
            fpsO = (255,165,0)
            fpsY = (255,255,0)
            fpsL = (165,255,0)
            fpsG = (0,255,0)
            fpsBox = pygame.Rect(0 , 17, 60, 30)
            if newFPS >= 15:
                pygame.draw.rect(window, fpsR, fpsBox)
            if newFPS >= 30:
                pygame.draw.rect(window, fpsO, fpsBox)
            if newFPS >= 60:
                pygame.draw.rect(window, fpsY, fpsBox)
            if newFPS >= 120:
                pygame.draw.rect(window, fpsL, fpsBox)
            if newFPS >= 180:
                pygame.draw.rect(window, fpsG, fpsBox)
            window.blit(update_fps(), (10,20))
    
    if presenceON == 1:
        RPC.update(
            large_image="arc-logo",
            large_text="Browsing menu",
            details="Browsing menu",
            state="under development!",
            party_size=[1,100],
            buttons=[{"label":"Track development here","url":"https://github.com/KittenzExe/arc"}]
            )

    
    #Closing the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if play == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play += 1
                    print("Hello World!")
                    print(play)
                    pygame.mixer.Sound.play(select)
                    pygame.mixer.music.stop()
        if play == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    settings += 1
                    print("settings")
                    print(settings)
        if play == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameplay += 1
                    print("gameplay")
                    menu = False
                    lobby = True
                    time.sleep(0.1)
                    pygame.display.update()
                    print(gameplay)

    pygame.display.update()

while lobby == True:
    #fps update
    mainClock.tick(0)
    window.fill((55,55,55))

    #fps update display
    if fpsON == 1:
        newFPS = int(mainClock.get_fps())
        fpsR = (255,0,0)
        fpsO = (255,165,0)
        fpsY = (255,255,0)
        fpsL = (165,255,0)
        fpsG = (0,255,0)
        fpsBox = pygame.Rect(0 , 17, 60, 30)
        if newFPS >= 15:
            pygame.draw.rect(window, fpsR, fpsBox)
        if newFPS >= 30:
            pygame.draw.rect(window, fpsO, fpsBox)
        if newFPS >= 60:
            pygame.draw.rect(window, fpsY, fpsBox)
        if newFPS >= 120:
            pygame.draw.rect(window, fpsL, fpsBox)
        if newFPS >= 180:
            pygame.draw.rect(window, fpsG, fpsBox)
        window.blit(update_fps(), (10,20))

    if presenceON == 1:
        RPC.update(
            large_image="arc-logo",
            large_text="Browsing menu",
            state="under development!",
            start=int(time.time())
            )
    
    #Closing the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                lobby = False
                game = True
                time.sleep(0.1)
                pygame.display.update()
                print(gameplay)
    
    pygame.display.update()

while game == True:
    #fps update
    mainClock.tick(0)
    window.fill((200,200,200))

    #fps update display
    if fpsON == 1:
        newFPS = int(mainClock.get_fps())
        fpsR = (255,0,0)
        fpsO = (255,165,0)
        fpsY = (255,255,0)
        fpsL = (165,255,0)
        fpsG = (0,255,0)
        fpsBox = pygame.Rect(0 , 17, 60, 30)
        if newFPS >= 15:
            pygame.draw.rect(window, fpsR, fpsBox)
        if newFPS >= 30:
            pygame.draw.rect(window, fpsO, fpsBox)
        if newFPS >= 60:
            pygame.draw.rect(window, fpsY, fpsBox)
        if newFPS >= 120:
            pygame.draw.rect(window, fpsL, fpsBox)
        if newFPS >= 180:
            pygame.draw.rect(window, fpsG, fpsBox)
        window.blit(update_fps(), (10,20))

    
    #Closing the window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                lobby = False
                game = True
                time.sleep(0.1)
                pygame.display.update()
                print(gameplay)


    pygame.display.update()