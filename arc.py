import pygame
mainClock = pygame.time.Clock()
import sys
from pypresence import Presence
import time
from pygame.locals import *

import string
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate('arc-data-base-firebase-adminsdk-1vqh2-57729cc1ce.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


pygame.init()

gameLoop = 1
if gameLoop == 1:
    window = pygame.display.set_mode((500,500))#pygame.FULLSCREEN
    wx,wy = pygame.display.get_window_size()

    font = pygame.font.SysFont("Arial", 20)

fpsON = 1
def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color(0,0,0))
	return fps_text


threeHund = 567
twoHund = 5
oneHund = 13

comboFinal = threeHund + twoHund + oneHund
threeFinal = threeHund * comboFinal
twoFinal = twoHund * comboFinal
oneFinal = oneHund * comboFinal
scoreFinal = threeFinal + twoFinal + oneFinal

print(scoreFinal)

doc_ref = db.collection(u'users').document(u'test')
doc_ref.set({
    u'uName': u'Test',
    u'recentScoreNumber': scoreFinal
})

text_value = ""
text = font.render(text_value, True, (255, 255, 255))

# initializing size of string
N = 7

res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
print("Session ID: " + str(res))

while True:
    #fps update
    mainClock.tick(0)
    window.fill((255,255,255))
    window.blit(text, (100, 150))

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
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text_value = text_value[:-1]
                text = font.render(text_value, True, (0, 0, 0))
            if event.key == pygame.K_RETURN:
                print(text_value) 
        if event.type == pygame.TEXTINPUT:
            text_value += event.text
            text = font.render(text_value, True, (0, 0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                doc_ref = db.collection(u'users').document(u'test1')
                doc_ref.set({
                    u'uName': text_value,
                    u'sessionID': res
                })
                print("Data Sent! Awaiting Verification of client...")
                time.sleep(1)
                users = db.pygame.event.get()
                print(users.val())



    
    pygame.display.flip()

