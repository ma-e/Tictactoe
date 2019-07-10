#from __future__ import unicode_literals
import pygame
from pygame.locals import *


#music
pygame.init()
pygame.mixer.init()
music = pygame.mixer.music.load('music/moonlight.wav')
beep = pygame.mixer.Sound('music/enemy.wav')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(1.88)


#imagie
width,height = 300, 333
screen = pygame.display.set_mode((width, height))
board = pygame.image.load("img/board.png").convert()
O = pygame.image.load("img/o.png").convert()
X = pygame.image.load("img/x.png").convert()
xwin = pygame.image.load("img/xwin.png").convert()
owin = pygame.image.load("img/owin.png").convert()
gameover = pygame.image.load("img/gameover.png").convert()
draw= pygame.image.load("img/draw.png").convert()
screen.fill(0)
screen.blit(board,(0,0))


#game conditions
mousex = 0
mousey = 0
plist = []
img = X
cell1 = (15,65)
cell2 = (110,65)
cell3 = (210,65)
cell4 = (15,150)
cell5 = (110,150)
cell6 = (210,150)
cell7 = (15,245)
cell8 = (110,245)
cell9 = (210,245)

cell1_occupied = False
cell2_occupied = False
cell3_occupied = False
cell4_occupied = False
cell5_occupied = False
cell6_occupied = False
cell7_occupied = False
cell8_occupied = False
cell9_occupied = False

occupied = False,False,False,False,False,False,False,False,False




#set win
winlist = [[cell1,cell4,cell7],[cell1,cell2,cell3],[cell4,cell5,cell6],[cell7,cell8,cell9],[cell2,cell5,cell8],[cell3,cell6,cell9],[cell1,cell5,cell9],[cell3,cell5,cell7]]


#paint board
def paintBoard():
    for i in plist:
        screen.blit(i[0],i[1])
    pygame.display.update()


#get postion
def set_move(mousex,mousey,img):
    
    global cell1_occupied
    global cell2_occupied
    global cell3_occupied
    global cell4_occupied
    global cell5_occupied
    global cell6_occupied
    global cell7_occupied
    global cell8_occupied
    global cell9_occupied
    
    if ((mousex>=15) and (mousex<=109))and ((mousey>=65) and (mousey<=149)) and (cell1_occupied == False):
        plist.append([img,cell1])
        cell1_occupied = img
    elif ((mousex>110) and (mousex<=209))and ((mousey>=65) and (mousey<=149)) and (cell2_occupied == False):
        plist.append([img,cell2])
        cell2_occupied = img
    elif ((mousex>210) and (mousex<=305))and ((mousey>=65) and (mousey<=150))and (cell3_occupied == False):
        plist.append([img,cell3])
        cell3_occupied = img
    elif ((mousex>=15) and (mousex<=109))and ((mousey>=149) and (mousey<=219))and (cell4_occupied == False):
        plist.append([img,cell4])
        cell4_occupied = img
    elif ((mousex>=110) and (mousex<=209))and((mousey>=150) and (mousey<=219))and (cell5_occupied == False):
        plist.append([img,cell5])
        cell5_occupied = img
    elif ((mousex>=210) and (mousex<=309))and((mousey>=150) and (mousey<=245))and (cell6_occupied == False):
        plist.append([img,cell6])
        cell6_occupied = img
    elif ((mousex>=15) and (mousex<=109))and((mousey>=245) and (mousey<=310))and (cell7_occupied == False):
        plist.append([img,cell7])
        cell7_occupied = img
    elif ((mousex>=110) and (mousex<=205))and((mousey>=245) and (mousey<=310))and (cell8_occupied == False):
        plist.append([img,cell8])
        cell8_occupied = img
    elif ((mousex>=210) and (mousex<=309))and((mousey>=245) and (mousey<=310))and (cell9_occupied == False):
        plist.append([img,cell9])
        cell9_occupied = img


def player_wins(img):
    
    if  img == O and \
        ((cell1_occupied == img and cell2_occupied == img and cell3_occupied == img ) or \
        (cell4_occupied == img and cell5_occupied == img and cell6_occupied == img ) or \
        (cell7_occupied == img and cell8_occupied == img and cell9_occupied == img ) or \
        (cell1_occupied == img and cell4_occupied == img and cell7_occupied == img ) or \
        (cell2_occupied == img and cell5_occupied == img and cell8_occupied == img ) or \
        (cell3_occupied == img and cell6_occupied == img and cell9_occupied == img ) or \
        (cell1_occupied == img and cell5_occupied == img and cell9_occupied == img ) or \
        (cell3_occupied == img and cell5_occupied == img and cell7_occupied == img )):
        plist.append([owin,(0,0)])
        
    elif img == X and \
        ((cell1_occupied == img and cell2_occupied == img and cell3_occupied == img) or \
        (cell4_occupied == img and cell5_occupied == img and cell6_occupied == img ) or \
        (cell7_occupied == img and cell8_occupied == img and cell9_occupied == img ) or \
        (cell1_occupied == img and cell4_occupied == img and cell7_occupied == img ) or \
        (cell2_occupied == img and cell5_occupied == img and cell8_occupied == img ) or \
        (cell3_occupied == img and cell6_occupied == img and cell9_occupied == img ) or \
        (cell1_occupied == img and cell5_occupied == img and cell9_occupied == img ) or \
        (cell3_occupied == img and cell5_occupied == img and cell7_occupied == img )):
        plist.append([xwin,(0,0)])

    else:
        if (cell1_occupied == X or cell1_occupied == O) and (cell2_occupied == X or cell2_occupied == O) and\
            (cell3_occupied == X or cell3_occupied == O) and (cell4_occupied == X or cell4_occupied == O) \
            and (cell5_occupied == X or cell5_occupied == O) and (cell6_occupied == X or cell6_occupied == O)\
            and (cell7_occupied == X or cell7_occupied == O) and (cell8_occupied == X or cell8_occupied == O) \
            and (cell9_occupied == X or cell9_occupied == O):
            plist.append([draw,(0,0)])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex ,mousey = event.pos
            mmouse_clicked = True
            if not (img == X):
                img = X
                beep.play()
            else:
                img = O
                beep.play()



            #print "setting img is O? {}". format(img==O)
            
            set_move(mousex,mousey,img)
            player_wins(X)
            player_wins(O)
            pygame.display.update()

        
        paintBoard()





#A = ((mousex>=110) and (mousex<=210))
#B = ((mousey<=240) and (mousey<=330))
#print ("left side: {}".format(A))
#print ("right side: {}".format(B))








