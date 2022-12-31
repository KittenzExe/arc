import pygame
mainClock = pygame.time.Clock()
import sys
from pypresence import Presence
import time
from pygame.locals import *
from datetime import datetime
import base64

import string
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate("/Users/KittenzExe/Desktop/arc-data-base-firebase-adminsdk-1vqh2-57729cc1ce.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

#Hello World!!
pygame.init()

gameLoop = 1
if gameLoop == 1:
    window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)#, pygame.FULLSCREEN | or in 1080, 720
    wx,wy = pygame.display.get_window_size()

    logoH = pygame.image.load("resources/arc-logo-updated.png").convert_alpha()
    logoH = pygame.transform.scale(logoH, (500, 500))

    rndBG = 0
    rndBG = random.randint(1 , 2)
    randBG = str(rndBG)
    homeBG = pygame.image.load("songs/"+ randBG+"/background.png")
    homeBG = pygame.transform.scale(homeBG, (wx, wy))

    font = pygame.font.SysFont("arialrounded", 20)#, bold = pygame.font.Font.bold

fpsON = 1
def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render(fps + " fps", 1, pygame.Color(0,0,0))
	return fps_text
def update_rawtime():
    rawtime = str(int(mainClock.get_rawtime()))
    rawtime_text = font.render(rawtime + " ms", 1, pygame.Color(0,0,0))
    return rawtime_text

text_value_U = ""
text_U = font.render(text_value_U, True, (100, 100, 255))
text_value_P = ""
text_P = font.render(text_value_P, True, (100, 100, 255))
userTemp = "Username"
passwordTemp = "Password"
tempU = font.render(userTemp, True, (0, 0, 0))
tempP = font.render(passwordTemp, True, (0, 0, 0))
uT = True
pT = True

# initializing size of string
N = 7

login = 1
tInputU = False
tInputP = False
dSubmit = False
loginShow = True

menu = 0

uName = ''
uScore = ''
uPP = ''

res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
print("Session ID: " + str(res))

entered = 0
logONU = False
logONP = False

print(randBG)
flashBG = 1

while True:
    mainClock.tick(999)

    if flashBG == 1:
        window.blit(homeBG, (0,0))
        time.sleep(0.0000001)
        flashBG = 0

    window.blit(logoH, (((wx/2)-250), ((wy/2)-250)))
    bar = (124, 124, 124)
    bar1 = pygame.Rect(0, 0, wx, 70)
    pygame.draw.rect(window, bar, bar1)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                login = 1
                menu = 0
                flashBG = 1

    if login == 1:

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

        uNameButton = pygame.Rect(63, 5, 200, 24)
        pWordButton = pygame.Rect(63, 34, 200, 24)
        dSubmitButton = pygame.Rect(5, 5, 53, 53)
        logoButton = pygame.Rect(((wx/2)-250), ((wy/2)-250), 500, 500)

        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if uNameButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    tInputU = True
                    tInputP = False
                    dSubmit = False
                    print(tInputU)
                    print(tInputP)
                    print(dSubmit)
                    uT = False

                if pWordButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button2 was pressed at {0}'.format(mouse_pos))
                    tInputU = False
                    tInputP = True
                    dSubmit = False
                    print(tInputU)
                    print(tInputP)
                    print(dSubmit)
                    pT = False
                
                if dSubmitButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button3 was pressed at {0}'.format(mouse_pos))
                    tInputU = False
                    tInputP = False
                    dSubmit = True
                    print(tInputU)
                    print(tInputP)
                    print(dSubmit)
                
                if logoButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('logo was pressed at {0}'.format(mouse_pos))
                    print("logo clicked!")
                    menu = 1
                    login = 0

        if tInputU == True:
            if event.type == pygame.KEYDOWN:
                logOnU = True
                if event.key == pygame.K_BACKSPACE:
                    text_value_U = text_value_U[:-1]
                    text_U = font.render(text_value_U, True, (0, 0, 0))
                if event.key == pygame.K_RETURN:
                    print(text_value_U)
            if event.type == pygame.TEXTINPUT:
                text_value_U += event.text
                text_U = font.render(text_value_U, True, (0, 0, 0))

        if tInputP == True:
            if event.type == pygame.KEYDOWN:
                logOnP = True
                if event.key == pygame.K_BACKSPACE:
                    text_value_P = text_value_P[:-1]
                    text_P = font.render(text_value_P, True, (0, 0, 0))
                if event.key == pygame.K_RETURN:
                    print(text_value_P)
            if event.type == pygame.TEXTINPUT:
                text_value_P += event.text
                text_P = font.render(text_value_P, True, (0, 0, 0))
        
        if dSubmit == True:
            #Username Handler
            doc_ref1 = db.collection(u'spindal users').document(u''+text_value_U)
            doc1 = doc_ref1.get()
            entered += 1
            print(entered)
            if doc1.exists:
                doc_ref1.set({
                    u'3-uName': text_value_U,
                    u'2-curveConnected': 0,
                    u'1-sessionID': res,
                }, merge=True)
            else:
                print(u'No such document!')
            
            #Password Handler
            message_bytes_P = text_value_P.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes_P)
            base64_message_p = base64_bytes.decode('ascii')
            doc_ref1 = db.collection(u'spindal users').document(u''+text_value_U)
            doc1 = doc_ref1.get()
            entered += 1
            print(entered)
            if doc1.exists:
                doc_ref1.set({
                    u'4-pWord': base64_message_p,
                }, merge=True)
            else:
                print(u'No such document!')
            
            #Verif. Handler
            print("Data Sent! Awaiting Verification of client...")
            datab = firestore.client()
            docu = text_value_U
            doc_ref2 = datab.collection(u'spindal users').document(u''+text_value_U)
            doc2 = doc_ref2.get()
            #Weird delay between sending and recieving...
            if doc2.exists:
                print(f'Document data: {doc2.to_dict()}')
                sIDCALL = (f"{doc2.to_dict()}")
                verif = str(doc2.to_dict()['1-sessionID'])
                print(verif)
                if verif == res:
                    print("verified!")
                    print("have fun playing!")
                    loginShow = False
                    login = 2
                    doc_ref1.set({
                    u'2-curveConnected': 1
                }, merge=True)
                else:
                    print("verification failed. please restart")
                
                uName = str(doc2.to_dict()['3-uName'])
                uScore = str(doc2.to_dict()['5-score'])
                uPP = str(doc2.to_dict()['6-pp'])
                print(uName+" , "+uScore+" , "+uPP)

                #Finish submit loop
                dSubmit = False
            else:
                print(u'No such document!')

    if loginShow == True:
        pygame.draw.rect(window, [240, 240, 240], uNameButton)
        window.blit(text_U, (68, 5))

        pygame.draw.rect(window, [240, 240, 240], pWordButton)
        window.blit(text_P, (68, 34))

        pygame.draw.rect(window, [240, 240, 240], dSubmitButton)

        if uT == True:
            window.blit(tempU, (68, 5))
        if pT == True:
            window.blit(tempP, (68, 34))
    
    if loginShow == False:
        uNamePrint = font.render(uName, True, (155, 224, 241))
        uScorePrint = font.render('Score: '+uScore, True, (252, 218, 156))
        uPPPrint = font.render('PP: '+uPP, True, (162, 172, 235))
        window.blit(uNamePrint, (5, 5))
        window.blit(uScorePrint, (5, 25))
        window.blit(uPPPrint, (5, 45))

    if menu == 1:
        window.fill((240,240,240))

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