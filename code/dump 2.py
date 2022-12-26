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

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "arc-data-base",
  "private_key_id": "57729cc1ce4f367212f3e59b32adf27b37906e19",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCm9orkircmE4oY\n6+eUaTRMxg7seQGdaxpyYy/Cvz6mPv7LdfpeloXUnxsNd/yJsjCwVjvCcvZqZq3Y\n00+0C4TxU4ubyo34BJdNlKXm6fyvm757/A8cpTgv9znb9vNzEro9GFlTZ9XxYjFF\nXqNyVsUjJQN2XwT66sN6yiwGuiwX0AsXCgO3RCC1skR4QDeCaXbEM9VO/CHrmjdw\nwLKj755/5Ht5MnI9JCqQJP221NyD67wK7Pv/YqsLIEojY4wMlZyc+hstg2Y76x7B\naK7duNyXJHQPm7oQ5grtoEK+oS4SdrlCjPnOtAFkiikdYEOJutJis+w0Q3Fp50In\ne8iUD4tJAgMBAAECgf8VXdqc00aXG8BNmOL1nhhKmAJuALzfzi86EVpUFMJyoRdd\nPe1VPvPnVjsADMxTO4M/mWxvSlh+kPydBcrqfLHPao1HlBuocEsPgpZnIkqZ3R1A\ngKcc+p8b+K1O3togKI4bbC3q+6eLOZoOw624grl3wwHxVYNE6pHlPwujUMFlPuWW\ncfjESm9y2cf1HBzJClAAZk7UYadIhnNQOmkfMMH3i/9tWffjqHoqJ0g6/QJC7/i2\n4vYIIDxomQjO/P/8asYqn9A3LfYu0qb6GGszTc+gANbwSReVaDN5xBwitVMZEAat\n1HcfkJKLW1bHC8T2Xvnya+eAs9KoSYzDhP1g3FECgYEA1kxS+XVyoHSYrssmACgO\n50xvrCOlPjzdmy7XOGDKctFApCyAmx46o6w/LF2gsJYOIY9y6wlbaWtunN+njl0y\nanIVoUnSPTZqhwqIzwn4HHLq+ndhy8BUPExGvEUcZ8zBmrxPNzZicBttpUKWZnH6\nU3ehsnSuwcWkovJ8XWLM+3ECgYEAx3QhOF+OY9Vf5G2T2pS+Is8r2qhk9naNrOFq\nWLcIobSbahr+IlCgg5Ggy2soiM/UJWq8zVChn6frTqEPRNWYwAhYg091K4RjmeZ8\n4d3pVHQr5jPiq5XtFcjxf23i2soB753U6wHt1EYGEr55OaRfvg3g3NZ0koveQtCm\nD+ijsVkCgYEAgAg7rqTX5jujGRNwUbmdJd3J/muRhzywHc3/ccSKT8zrNOsNrx+B\nY1Y+rBAIOFh+etiMjRYbEkHIZVtObUULIQOmHqXPQRkoziOiFyhanwydjSUUPbpb\n2WatAEC+NtnjdcI6Bb+tUlNgz9KXrv870vBvoAIMguLFeUEswlKMK1ECgYA1k1gp\nEGHrJzGu5lBE8pdwOj4JahpUqdu8iIBMfD3xUdY9VirVhNrY/JE4kvw8Y7cUpes5\nK2N+w1hNsq2rS8TQMG22N+29Vr56ZJM/CKDYcqwoFd/ZP1iD9YoJNLcvFfwXJUpA\nJjCASJ7xAgEGHsUpBAlWyLRfePqm7+zrcQ4nYQKBgQCxIYJVn9Jh3A4PomIA0VWE\nayGFXq3kHMHJ0YOo/xc2GifOjEUKACrOWkOnvQnh+WvijhJdUt5PVXZWfxU4j4Uy\nvrCdiiXnlRyddT56kYluIgsBJN+2ThQ0rCLweuB+L4KbTZKdmvKIc3evgrKaCcvr\niRXuBGvrnPkEn+r7MDobHg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-1vqh2@arc-data-base.iam.gserviceaccount.com",
  "client_id": "112266744488263067593",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1vqh2%40arc-data-base.iam.gserviceaccount.com"
})
app = firebase_admin.initialize_app(cred)
db = firestore.client()

#Hello World!
pygame.init()

gameLoop = 1
if gameLoop == 1:
    window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)#, pygame.FULLSCREEN | or in 1080, 720
    wx,wy = pygame.display.get_window_size()

    uNameButton = pygame.Rect(10, 80, 20, 20)
    pWordButton = pygame.Rect(10, 110, 20, 20)
    dSubmitButton = pygame.Rect(10, 210, 20, 20)

    font = pygame.font.SysFont("arialrounded", 20)#, bold = pygame.font.Font.bold

fpsON = 1
def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color(0,0,0))
	return fps_text

text_value_U = ""
text_U = font.render(text_value_U, True, (100, 100, 255))
text_value_P = ""
text_P = font.render(text_value_P, True, (100, 100, 255))

# initializing size of string
N = 7

login = 1
tInputU = False
tInputP = False
dSubmit = False
loginShow = True

res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
print("Session ID: " + str(res))

entered = 0
logONU = False
logONP = False

while True:
    mainClock.tick(0)
    window.fill((255,255,255))
    #fps update
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

        if login == 1:
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

                    if pWordButton.collidepoint(mouse_pos):
                        # prints current location of mouse
                        print('button2 was pressed at {0}'.format(mouse_pos))
                        tInputU = False
                        tInputP = True
                        dSubmit = False
                        print(tInputU)
                        print(tInputP)
                        print(dSubmit)
                    
                    if dSubmitButton.collidepoint(mouse_pos):
                        # prints current location of mouse
                        print('button2 was pressed at {0}'.format(mouse_pos))
                        tInputU = False
                        tInputP = False
                        dSubmit = True
                        print(tInputU)
                        print(tInputP)
                        print(dSubmit)
        
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
                verif = str(sIDCALL[17:24])
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
                #Finish submit loop
                dSubmit = False
            else:
                print(u'No such document!')

    if loginShow == True:
        pygame.draw.rect(window, [255, 0, 0], uNameButton)
        pygame.draw.rect(window, [255, 0, 0], pWordButton)
        pygame.draw.rect(window, [255, 0, 0], dSubmitButton)

        t_u = (241, 241, 255)
        t1_u = pygame.Rect(100, 150, 200, 70)
        pygame.draw.rect(window, t_u, t1_u)
        window.blit(text_U, (100, 150))

        t_p = (241, 241, 255)
        t1_p = pygame.Rect(100, 250, 200, 70)
        pygame.draw.rect(window, t_p, t1_p)
        window.blit(text_P, (100, 250))

    pygame.display.flip()