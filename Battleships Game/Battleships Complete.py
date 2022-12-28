import pygame
import random
import time
import pygame.gfxdraw
from math import sqrt
#importing all of the libraries I need for the program


pygame.init()
pygame.font.init()

#initiating pygame and allowing me to use fonts

gamewidth=1366
gameheight=768
timeDelay=1
#Game window and time delay

playx=890
playy=270
playLength=100
#Play button constants

tutorialx=850
tutorialy=372
tutorialLength=175
#Tutorial button constants

stylex=875
styley=470
styleLength=120
#Style button constants

leaderboardx=805
leaderboardy=568
leaderboardLength=260
#Leaderboard button constants

B_width=65
#Button width constant

aircraftCarrierx=750
aircraftCarriery=245
aircraftCarrierWidth=50
aircraftCarrierLength=275
aircraft_direction='horizontal'
aircraftColumn=11
aircraftRow=11
#Aircraft Carrier constants

destroyerx=750
destroyery=345
destroyerWidth=50
destroyerLength=210
destroyer_direction='horizontal'
destroyerColumn=11
destroyerRow=11
#Destroyer constants

cruiserx=750
cruisery=445
cruiserWidth=50
cruiserLength=160
cruiser_direction='horizontal'
cruiserColumn=11
cruiserRow=11
#Cruiser constants 

submarinex=750
submariney=545
submarineWidth=50
submarineLength=110
submarine_direction='horizontal'
submarineColumn=11
submarineRow=11
#Submarine constants 


grid_width=57.2
grid_height=59
#Grid constants





#setting the constants for the program window

mouseHover=False
def mouseChange():
    global mouseHover
    pygame.mouse.set_visible(False)
    mouseHover=True

    #Subroutine to change the mouse into the hand icon

def HomeScreen():
    homeScreen=pygame.image.load('Home Screen.jpg')
    win.fill((0,0,0))
    homeScreen=pygame.transform.scale(homeScreen,(1366,768))
    win.blit(homeScreen,(0,0))
    pygame.draw.rect(win, (255,0,0), (playx,playy,playLength,B_width),3)
    #play button
    pygame.draw.rect(win, (255,0,0), (tutorialx,tutorialy,tutorialLength,B_width),3)
    #tutorial button
    pygame.draw.rect(win, (255,0,0), (stylex,styley,styleLength,B_width),3)
    #style button
    pygame.draw.rect(win, (255,0,0), (leaderboardx,leaderboardy,leaderboardLength,B_width),3)
    #leaderboard button
    #draws a rectangle for the menu buttons (Surface,Colour,(x,y,length,width),border)
    
def Prep():
    global run
    global mouseHover
    global aircraftCarrier
    global aircraftCarrierx
    global aircraftCarriery
    global aircraftCarrierWidth
    global aircraftCarrierLength
    global aircraft_direction
    global destroyer
    global destroyerx
    global destroyery
    global destroyerWidth
    global destroyerLength
    global destroyer_direction
    global cruiser
    global cruiserx
    global cruisery
    global cruiserWidth
    global cruiserLength
    global cruiser_direction
    global submarine
    global submarinex
    global submariney
    global submarineWidth
    global submarineLength
    global submarine_direction
    global close
    run=True
    while run==True:
        pygame.time.delay(timeDelay)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                close=True
                
                
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            aircraft_placement()
            destroyer_placement()
            cruiser_placement()
            submarine_placement()
            computerCoords()
        #calls the subroutines for getting ship locations

            (x,y)=aircraftCoords[0]
            if x<=10 and y<=10:
                (x,y)=destroyerCoords[0]
                if x<=10 and y<=10:
                    (x,y)=cruiserCoords[0]
                    if x<=10 and y<=10:
                        (x,y)=submarineCoords[0]
                        if x<=10 and y<=10:
                            run=False
                            close=False
            #Final validation on checking every ship is within game boundaries

            



                
        (posx,posy)=pygame.mouse.get_pos()
        if posx>=aircraftCarrierx and posx<=aircraftCarrierx+aircraftCarrierLength and posy>=aircraftCarriery and posy<=aircraftCarriery+aircraftCarrierWidth:
            mouseChange()
            if keys[pygame.K_f]:
                aircraftCarrier=pygame.transform.rotate(aircraftCarrier,-90)
                if aircraftCarrierLength==275:
                    aircraft_direction='vertical'
                elif aircraftCarrierWidth==275:
                    aircraft_direction='horizontal'
                temp=aircraftCarrierLength
                aircraftCarrierLength=aircraftCarrierWidth
                aircraftCarrierWidth=temp
                pygame.time.delay(timeDelay)
            #Flips the aircraft carrier when f is pressed 
            mouse=pygame.mouse.get_pressed()
            if mouse==(True,False,False):
                aircraftCarrierx= int(posx-(aircraftCarrierLength/2))
                aircraftCarriery= int(posy-(aircraftCarrierWidth/2))
            #Moves the aircraft carrier to the users mouse position
        elif posx>=destroyerx and posx<=destroyerx+destroyerLength and posy>=destroyery and posy<=destroyery+destroyerWidth:
            mouseChange()
            if keys[pygame.K_f]:
                destroyer=pygame.transform.rotate(destroyer,-90)
                if destroyerLength==210:
                    destroyer_direction='vertical'
                elif destroyerWidth==210:
                    destroyer_direction='horizontal'
                temp=destroyerLength
                destroyerLength=destroyerWidth
                destroyerWidth=temp
                pygame.time.delay(timeDelay)
            #Flips the destroyer when f is pressed
            mouse=pygame.mouse.get_pressed()
            if mouse==(True,False,False):
                destroyerx= int(posx-(destroyerLength/2))
                destroyery= int(posy-(destroyerWidth/2))
            #Moves the destroyer to the users mouse position
        elif posx>=cruiserx and posx<=cruiserx+cruiserLength and posy>=cruisery and posy<=cruisery+cruiserWidth:
            mouseChange()
            if keys[pygame.K_f]:
                cruiser=pygame.transform.rotate(cruiser,-90)
                if cruiserLength==160:
                    cruiser_direction='vertical'
                elif cruiserWidth==160:
                    cruiser_direction='horizontal'
                temp=cruiserLength
                cruiserLength=cruiserWidth
                cruiserWidth=temp
                pygame.time.delay(timeDelay)
            #Flips the cruiser when f is pressed
            mouse=pygame.mouse.get_pressed()
            if mouse==(True,False,False):
                cruiserx= int(posx-(cruiserLength/2))
                cruisery= int(posy-(cruiserWidth/2))
            #Moves the cruiser to the users mouse position
        
        elif posx>=submarinex and posx<=submarinex+submarineLength and posy>=submariney and posy<=submariney+submarineWidth:
            mouseChange()
            if keys[pygame.K_f]:
                submarine=pygame.transform.rotate(submarine,-90)
                if submarineLength==110:
                    submarine_direction='vertical'
                elif submarineWidth==110:
                    submarine_direction='horizontal'
                temp=submarineLength
                submarineLength=submarineWidth
                submarineWidth=temp
                pygame.time.delay(timeDelay)
            #Flips the submarine when f is pressed
            mouse=pygame.mouse.get_pressed()
            if mouse==(True,False,False):
                submarinex= int(posx-(submarineLength/2))
                submariney= int(posy-(submarineWidth/2))
            #Moves the submarine to the users mouse position
                
        else:
            pygame.mouse.set_visible(True)
            mouseHover=False
            

        #sets the hitboxes for the ships and allows them to be selected and moved



        win.fill((0,0,0))
        win.blit(prepPhaseScreen,(0,0))
        Grid()
        win.blit(aircraftCarrier,(aircraftCarrierx,aircraftCarriery))
        win.blit(destroyer,(destroyerx,destroyery))
        win.blit(cruiser,(cruiserx,cruisery))
        win.blit(submarine,(submarinex,submariney))

        #blits all items onto the window 



        if mouseHover==True:
            win.blit(mouseHand,(posx-5,posy))
                
            
        pygame.display.update()
    run=True

def computerCoords():
    global AIaircraftCoords
    global AIdestroyerCoords
    global AIcruiserCoords
    global AIsubmarineCoords
    orientation=random.randint(0,1)
    if orientation==0:
        i=random.randint(1,5)
        j=random.randint(1,3)
        AIaircraftCoords=[(i,j),(i+1,j),(i+2,j),(i+3,j),(i+4,j)]
        i=random.randint(1,6)
        j=random.randint(4,5)
        AIdestroyerCoords=[(i,j),(i+1,j),(i+2,j),(i+3,j)]
        i=random.randint(1,7)
        j=random.randint(6,7)
        AIcruiserCoords=[(i,j),(i+1,j),(i+2,j)]
        i=random.randint(1,8)
        j=random.randint(8,10)
        AIsubmarineCoords=[(i,j),(i+1,j)]
        #generates the ship coordinates for horizontal ships
    else:
        i=random.randint(1,3)
        j=random.randint(1,5)
        AIaircraftCoords=[(i,j),(i,j+1),(i,j+2),(i,j+3),(i,j+4)]
        i=random.randint(4,5)
        j=random.randint(1,6)
        AIdestroyerCoords=[(i,j),(i,j+1),(i,j+2),(i,j+3)]
        i=random.randint(6,7)
        j=random.randint(1,7)
        AIcruiserCoords=[(i,j),(i,j+1),(i,j+2)]
        i=random.randint(8,10)
        j=random.randint(1,8)
        AIsubmarineCoords=[(i,j),(i,j+1)]
        #generates the ship coordinates for vertical ships
    print(AIaircraftCoords)
    print(AIdestroyerCoords)
    print(AIcruiserCoords)
    print(AIsubmarineCoords)

    
    
    
    

def Grid():
    for j in range(0,10):
        for i in range(0,10):
            pygame.draw.rect(win, (255,255,255), (int(101+(grid_width*i)),int(138+(grid_height*j)),58,58),3)
            #draws the game grid on the screen

def aircraft_placement():
    global aircraftColumn
    global aircraftRow
    global aircraft_direction
    global aircraftCoords
    if aircraft_direction=='horizontal':
        for i in range(0,11):
            if aircraftCarrierx<101:
                aircraftColumn=11
                break
            elif aircraftCarrierx> (int(101+(grid_width*6))):
                aircraftColumn=11
                break
            elif aircraftCarrierx< (int(101+(grid_width*i))):
                aircraftColumn=i
                break
        for j in range(0,11):
            if aircraftCarriery<138:
                aircraftRow=11
                break
            elif aircraftCarriery> (int(138+(grid_height*10))):
                aircraftRow=11
                break
            elif aircraftCarriery< (int(138+(grid_height*j))):
                aircraftRow=j
                break
        aircraftCoords=[(aircraftColumn, aircraftRow),(aircraftColumn+1,aircraftRow),(aircraftColumn+2,aircraftRow),(aircraftColumn+3,aircraftRow),(aircraftColumn+4,aircraftRow)]
        print(aircraftCoords)
        #generates the x and y coordinate for the aircraft carrier when horizontal
    elif aircraft_direction=='vertical':
        for i in range(0,11):
            if aircraftCarrierx<101:
                aircraftColumn=11
                break
            elif aircraftCarrierx> (int(101+(grid_width*10))):
                aircraftColumn=11
                break
            elif aircraftCarrierx< (int(101+(grid_width*i))):
                aircraftColumn=i
                break
        for j in range(0,11):
            if aircraftCarriery<138:
                aircraftRow=11
                break
            elif aircraftCarriery> (int(138+(grid_height*6))):
                aircraftRow=11
                break
            elif aircraftCarriery< (int(138+(grid_height*j))):
                aircraftRow=j
                break
        aircraftCoords=[(aircraftColumn, aircraftRow),(aircraftColumn,aircraftRow+1),(aircraftColumn,aircraftRow+2),(aircraftColumn,aircraftRow+3),(aircraftColumn,aircraftRow+4)]
        print(aircraftCoords)
        #generates the x and y coordinate for the aircraft carrier when vertical
    

def destroyer_placement():
    global destroyerColumn
    global destroyerRow
    global destroyer_direction
    global destroyerCoords
    if destroyer_direction=='horizontal':
        for i in range(0,11):
            if destroyerx<101:
                destroyerColumn=11
                break
            elif destroyerx> (int(101+(grid_width*7))):
                destroyerColumn=11
                break
            elif destroyerx< (int(101+(grid_width*i))):
                destroyerColumn=i
                break
        for j in range(0,11):
            if destroyery<138:
                destroyerRow=11
                break
            elif destroyery> (int(138+(grid_height*10))):
                destroyerRow=11
                break
            elif destroyery< (int(138+(grid_height*j))):
                destroyerRow=j
                break
        destroyerCoords=[(destroyerColumn, destroyerRow),(destroyerColumn+1,destroyerRow),(destroyerColumn+2,destroyerRow),(destroyerColumn+3,destroyerRow)]
        print(destroyerCoords)
        #generates the x and y coordinate for the destroyer when horizontal
    elif destroyer_direction=='vertical':
        for i in range(0,11):
            if destroyerx<101:
                destroyerColumn=11
                break
            elif destroyerx> (int(101+(grid_width*10))):
                destroyerColumn=11
                break
            elif destroyerx< (int(101+(grid_width*i))):
                destroyerColumn=i
                break
        for j in range(0,11):
            if destroyery<138:
                destroyerRow=11
                break
            elif destroyery> (int(138+(grid_height*7))):
                destroyerRow=11
                break
            elif destroyery< (int(138+(grid_height*j))):
                destroyerRow=j
                break

        destroyerCoords=[(destroyerColumn, destroyerRow),(destroyerColumn,destroyerRow+1),(destroyerColumn,destroyerRow+2),(destroyerColumn,destroyerRow+3)]
        print(destroyerCoords)
        #generates the x and y coordinate for the destroyer when vertical


def cruiser_placement():
    global cruiserColumn
    global cruiserRow
    global cruiser_direction
    global cruiserCoords
    if cruiser_direction=='horizontal':
        for i in range(0,11):
            if cruiserx<101:
                cruiserColumn=11
                break
            elif cruiserx> (int(101+(grid_width*8))):
                cruiserColumn=11
                break
            elif cruiserx< (int(101+(grid_width*i))):
                cruiserColumn=i
                break
        for j in range(0,11):
            if cruisery<138:
                cruiserRow=11
                break
            elif cruisery> (int(138+(grid_height*10))):
                cruiserRow=11
                break
            elif cruisery< (int(138+(grid_height*j))):
                cruiserRow=j
                break
        cruiserCoords=[(cruiserColumn, cruiserRow),(cruiserColumn+1,cruiserRow),(cruiserColumn+2,cruiserRow)]
        print(cruiserCoords)
        #generates the x and y coordinate for the cruiser when horizontal
    elif cruiser_direction=='vertical':
        for i in range(0,11):
            if cruiserx<101:
                cruiserColumn=11
                break
            elif cruiserx> (int(101+(grid_width*10))):
                cruiserColumn=11
                break
            elif cruiserx< (int(101+(grid_width*i))):
                cruiserColumn=i
                break
        for j in range(0,11):
            if cruisery<138:
                cruiserRow=11
                break
            elif cruisery> (int(138+(grid_height*8))):
                cruiserRow=11
                break
            elif cruisery< (int(138+(grid_height*j))):
                cruiserRow=j
                break

        cruiserCoords=[(cruiserColumn, cruiserRow),(cruiserColumn,cruiserRow+1),(cruiserColumn,cruiserRow+2)]
        print(cruiserCoords)
        #generates the x and y coordinate for the cruiser when vertical

def submarine_placement():
    global submarineColumn
    global submarineRow
    global submarine_direction
    global submarineCoords
    if submarine_direction=='horizontal':
        for i in range(0,11):
            if submarinex<101:
                submarineColumn=11
                break
            elif submarinex> (int(101+(grid_width*9))):
                submarineColumn=11
                break
            elif submarinex< (int(101+(grid_width*i))):
                submarineColumn=i
                break
        for j in range(0,11):
            if submariney<138:
                submarineRow=11
                break
            elif submariney> (int(138+(grid_height*10))):
                submarineRow=11
                break
            elif submariney< (int(138+(grid_height*j))):
                submarineRow=j
                break
        submarineCoords=[(submarineColumn, submarineRow),(submarineColumn+1,submarineRow)]
        print(submarineCoords)
        #generates the x and y coordinate for the submarine when horizontal
    elif submarine_direction=='vertical':
        for i in range(0,11):
            if submarinex<101:
                submarineColumn=11
                break
            elif submarinex> (int(101+(grid_width*10))):
                submarineColumn=11
                break
            elif submarinex< (int(101+(grid_width*i))):
                submarineColumn=i
                break
        for j in range(0,11):
            if submariney<138:
                submarineRow=11
                break
            elif submariney> (int(138+(grid_height*9))):
                submarineRow=11
                break
            elif submariney< (int(138+(grid_height*j))):
                submarineRow=j
                break

        submarineCoords=[(submarineColumn, submarineRow),(submarineColumn,submarineRow+1)]
        print(submarineCoords)
        #generates the x and y coordinate for the submarine when vertical

def Action():
    global mouseHover
    global grid_width
    global grid_height
    global shootingCoord
    
    pygame.mouse.set_visible(True)
    mouseHover=False
    
    grid_width=57
    grid_height=57.75
    hitLocations=[]
    hitNumber=0
    AIhitLocations=[]
    AIhitNumber=0
    missLocations=[]
    missNumber=0
    AImissLocations=[]
    AImissNumber=0
    playerLocations=[]
    for i in range(0,5):
        playerLocations.append(aircraftCoords[i])
    for i in range(0,4):
        playerLocations.append(destroyerCoords[i])
    for i in range(0,3):
        playerLocations.append(cruiserCoords[i])
    for i in range(0,2):
        playerLocations.append(submarineCoords[i])
    print(playerLocations)
    spacesLeft=13
    #Adds all the users ships to a list

    lossScreen=pygame.image.load('lossScreen.png')
    lossScreen=pygame.transform.scale(lossScreen,(1000,600))
    winScreen=pygame.image.load('winScreen.png')
    winScreen=pygame.transform.scale(winScreen,(1000,600))
    #Loads the loss and win screen 
    
    base_font=pygame.font.Font(None,100)
    shoot=''
    #Loads the text font for the users text
    
    run=True
    while run==True:
        pygame.time.delay(timeDelay)
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                run=False
                
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_BACKSPACE:
                    shoot=shoot[:-1]
                    
                elif event.key==pygame.K_RETURN:
                    yshoot=shoot[:1]
                    xshoot=shoot[1:]
                    print(xshoot)
                    print(yshoot)
                    #Lets the user input text with enter
                    
                    if yshoot.isalpha()==True and xshoot.isdigit()==True:
                        yshoot=yshoot.upper()
                        yshoot=ord(yshoot)-64
                        xshoot=int(xshoot)
                        
                        if xshoot<11 and yshoot<11:
                            shootingCoord=(xshoot,yshoot)
                            print(shootingCoord)
                            
                            if shootingCoord in AIaircraftCoords:
                                AIaircraftCoords.remove(shootingCoord)
                                shipHit(xshoot,yshoot)
                                hitLocations.append((xshoot,yshoot))
                                print(hitLocations)
                                hitNumber=hitNumber+1
                                #checks if the aircraft carrier has been shot
                                
                            elif shootingCoord in AIdestroyerCoords:
                                AIdestroyerCoords.remove(shootingCoord)
                                shipHit(xshoot,yshoot)
                                hitLocations.append((xshoot,yshoot))
                                print(hitLocations)
                                hitNumber=hitNumber+1
                                #checks if the destroyer has been shot
                                
                            elif shootingCoord in AIcruiserCoords:
                                AIcruiserCoords.remove(shootingCoord)
                                shipHit(xshoot,yshoot)
                                hitLocations.append((xshoot,yshoot))
                                print(hitLocations)
                                hitNumber=hitNumber+1
                                #checks if the cruiser has been shot
                                
                                
                            elif shootingCoord in AIsubmarineCoords:
                                AIsubmarineCoords.remove(shootingCoord)
                                shipHit(xshoot,yshoot)
                                hitLocations.append((xshoot,yshoot))
                                print(hitLocations)
                                hitNumber=hitNumber+1
                                #checks if the submarine has been shot
                                
                            else:
                                missLocations.append((xshoot,yshoot))
                                missNumber=missNumber+1
                                
                            shoot=''

                            randomShot=random.randint(0,2)
                            if randomShot==1:
                                AIshoot=random.randint(0,spacesLeft)
                                print(AIshoot)
                                (AIshot)=playerLocations[AIshoot]
                                (AIxshoot,AIyshoot)=AIshot
                                #Shoots a user ship
                            else:
                                repeat=True
                                while repeat==True:
                                    AIxshoot=random.randint(1,10)
                                    AIyshoot=random.randint(1,10)
                                    AIshot=(AIxshoot,AIyshoot)
                                    if AIshot in AImissLocations:
                                        repeat=True
                                    if (AIshot) in aircraftCoords or (AIshot) in destroyerCoords or (AIshot) in cruiserCoords or (AIshot) in submarineCoords:
                                        if AIshot in playerLocations:
                                            repeat=False
                                        else:
                                            repeat=True
                                    else:
                                        repeat=False
                                    #Keeps repeating randomly generating AI shooting coords so it doesn't shoot the same location twice
                                        
                            if (AIshot) in aircraftCoords:
                                playerLocations.remove(AIshot)
                                AIshipHit(AIxshoot,AIyshoot)
                                AIhitLocations.append(AIshot)
                                AIhitNumber=AIhitNumber+1
                                spacesLeft=spacesLeft-1
                                #Checks if the users aircraft carrier is hit
                                
                            elif (AIshot) in destroyerCoords:
                                playerLocations.remove(AIshot)
                                AIshipHit(AIxshoot,AIyshoot)
                                AIhitLocations.append(AIshot)
                                AIhitNumber=AIhitNumber+1
                                spacesLeft=spacesLeft-1
                                #Checks if the users destroyer is hit
                                
                            elif (AIshot) in cruiserCoords:
                                playerLocations.remove(AIshot)
                                AIshipHit(AIxshoot,AIyshoot)
                                AIhitLocations.append(AIshot)
                                AIhitNumber=AIhitNumber+1
                                spacesLeft=spacesLeft-1
                                #Checks if the users cruiser is hit
                                
                            elif (AIshot) in submarineCoords:
                                playerLocations.remove(AIshot)
                                AIshipHit(AIxshoot,AIyshoot)
                                AIhitLocations.append(AIshot)
                                AIhitNumber=AIhitNumber+1
                                spacesLeft=spacesLeft-1
                                #Checks if the users submarine is hit
                                
                            else:
                                AImissLocations.append(AIshot)
                                AImissNumber=AImissNumber+1
                        else:
                            shoot=''
                    else:
                        shoot=''
                    
                    
                        
                        
                        
                        
                elif len(shoot)==3:
                    shoot=shoot
                    
                else:
                    shoot+=event.unicode
            
            
        

        
        
        

        win.fill((0,0,0))
        win.blit(gamePhaseScreen,(0,0))
        Grid1()
        Grid2()
        (aircraftCarrierx,aircraftCarriery)=aircraftCoords[0]
        win.blit(aircraftCarrier, (int(70+(grid_width*(aircraftCarrierx-1))),int(72+(grid_height*(aircraftCarriery-1)))))
        #sets the aircraft carrier x and y coordinates based on the grid coordinates
        (destroyerx,destroyery)=destroyerCoords[0]
        win.blit(destroyer, (int(70+(grid_width*(destroyerx-1))),int(72+(grid_height*(destroyery-1)))))
        #sets the destroyer x and y coordinates based on the grid coordinates
        (cruiserx,cruisery)=cruiserCoords[0]
        win.blit(cruiser, (int(70+(grid_width*(cruiserx-1))),int(72+(grid_height*(cruisery-1)))))
        #sets the cruiser x and y coordinates based on the grid coordinates
        (submarinex,submariney)=submarineCoords[0]
        win.blit(submarine, (int(70+(grid_width*(submarinex-1))),int(72+(grid_height*(submariney-1)))))
        #sets the submarine x and y coordinates based on the grid coordinates
        text_surface=base_font.render(shoot,True,(0,0,0))
        win.blit(text_surface,(590,670))
        for i in range(0,missNumber):
            (markerx,markery)=missLocations[i]
            pygame.draw.circle(win,(255,255,255),(int(789+(grid_width/2)+(grid_width*(markerx-1))),int(85+(grid_height/3)+(grid_height*(markery-1)))),20)
        for i in range(0,hitNumber):
            (markerx,markery)=hitLocations[i]
            pygame.draw.circle(win,(255,0,0),(int(789+(grid_width/2)+(grid_width*(markerx-1))),int(85+(grid_height/3)+(grid_height*(markery-1)))),20)
        for i in range(0,AImissNumber):
            (markerx,markery)=AImissLocations[i]
            pygame.draw.circle(win,(255,255,255),(int(70+(grid_width/2)+(grid_width*(markerx-1))),int(85+(grid_height/3)+(grid_height*(markery-1)))),20)
        for i in range(0,AIhitNumber):
            (markerx,markery)=AIhitLocations[i]
            pygame.draw.circle(win,(255,0,0),(int(70+(grid_width/2)+(grid_width*(markerx-1))),int(85+(grid_height/3)+(grid_height*(markery-1)))),20)
        #Draws all the AI and User hit locations and miss locations on the board
            
        pygame.display.update()
        if hitNumber==14:
            run=False
            win.blit(winScreen,(200,100))
            pygame.display.update()
            pygame.time.delay(5000)
            #Checks if the user has won
            
        elif spacesLeft==-1:
            run=False
            win.blit(lossScreen,(200,100))
            pygame.display.update()
            pygame.time.delay(5000)
            #Checks if the AI has won
        

def Grid1():
    for j in range(0,10):
        for i in range(0,10):
            pygame.draw.rect(win, (255,255,255), (int(68+(grid_width*i)),int(70+(grid_height*j)),57,58),3)
    #Draws the game grid for the user
def Grid2():
    for j in range(0,10):
        for i in range(0,10):
            pygame.draw.rect(win, (255,255,255), (int(789+(grid_width*i)),int(70+(grid_height*j)),57,58),3)
    #Draws the game grid for the AI
    
def shipHit(xshoot,yshoot):
    explosion=pygame.image.load('explosion.png')
    explosion=pygame.transform.scale(explosion,(int(grid_width),int(grid_height)))
    explosionx=int(789+(grid_width*(xshoot-1)))
    explosiony=int(70+(grid_height*(yshoot-1)))
    pygame.draw.rect(win, (255,255,255), (int(805+(grid_width*(xshoot-1))),int(85+(grid_height*(yshoot-1))),25,25),0)
    win.blit(explosion,(explosionx,explosiony))
    #Animates the explosion for when a ship is hit
    
    pygame.display.update()
    pygame.time.delay(500)
    
def AIshipHit(xshoot,yshoot):
    explosion=pygame.image.load('explosion.png')
    explosion=pygame.transform.scale(explosion,(int(grid_width),int(grid_height)))
    explosionx=int(68+(grid_width*(xshoot-1)))
    explosiony=int(70+(grid_height*(yshoot-1)))
    pygame.draw.rect(win, (255,255,255), (int(84+(grid_width*(xshoot-1))),int(85+(grid_height*(yshoot-1))),25,25),0)
    win.blit(explosion,(explosionx,explosiony))
    #Animates the explosion for when the users ship is hit
    pygame.display.update()
    pygame.time.delay(500)
    
        
        
    
        

    

    
win=pygame.display.set_mode((gamewidth,gameheight), pygame.RESIZABLE)
pygame.display.set_caption("Battleships")
icon=pygame.image.load('Icon.ico')
pygame.display.set_icon(icon)
mouseHand=pygame.image.load('mouseHand.png')
mouseHand=pygame.transform.scale(mouseHand,(15,15))


prepPhaseScreen=pygame.image.load('prepPhaseScreen.png')
prepPhaseScreen=pygame.transform.scale(prepPhaseScreen,(1366,768))
gamePhaseScreen=pygame.image.load('Game Phase Screen.png')
gamePhaseScreen=pygame.transform.scale(gamePhaseScreen,(1366,750))

aircraftCarrier=pygame.image.load('aircraftCarrier.png')
aircraftCarrier=pygame.transform.scale(aircraftCarrier,(aircraftCarrierLength,aircraftCarrierWidth))
destroyer=pygame.image.load('destroyer.png')
destroyer=pygame.transform.scale(destroyer,(destroyerLength,destroyerWidth))
cruiser=pygame.image.load('cruiser.png')
cruiser=pygame.transform.scale(cruiser,(cruiserLength,cruiserWidth))
submarine=pygame.image.load('submarine.png')
submarine=pygame.transform.scale(submarine,(submarineLength,submarineWidth))

#Creating the window for the game and other image loading


run=True
while run==True:
    
#starting the game loop
    
    pygame.time.delay(timeDelay)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #testing for if the program is closed at any time

    (posx,posy)=pygame.mouse.get_pos()
    if posx>=playx and posx<=playx+playLength and posy>=playy and posy<=playy+B_width:
        mouseChange()
        mouse=pygame.mouse.get_pressed()
        if mouse==(True,False,False):
            pygame.mouse.set_visible(True)
            Prep()
            if close!=True:
                Action()
                grid_width=57.2
                grid_height=59
            
    elif posx>=tutorialx and posx<=tutorialx+tutorialLength and posy>=tutorialy and posy<=tutorialy+B_width:
        #put tutorial subroutine here
        mouseChange()
        mouse=pygame.mouse.get_pressed()
        if mouse==(True,False,False):
            pygame.mouse.set_visible(True)
            
    elif posx>=stylex and posx<=stylex+styleLength and posy>=styley and posy<=styley+B_width:
        #put style subroutine here
        mouseChange()
        mouse=pygame.mouse.get_pressed()
        if mouse==(True,False,False):
            pygame.mouse.set_visible(True)
            
    elif posx>=leaderboardx and posx<=leaderboardx+leaderboardLength and posy>=leaderboardy and posy<=leaderboardy+B_width:
        #put leaderboard subroutine here
        mouseChange()
        mouse=pygame.mouse.get_pressed()
        if mouse==(True,False,False):
            pygame.mouse.set_visible(True)
            
    else:
        pygame.mouse.set_visible(True)
        mouseHover=False
        #makes the mouse visible if set to invisible previously
            
            
            
            
    




    HomeScreen()

    
    if mouseHover==True:
        win.blit(mouseHand,(posx-5,posy))

        
    pygame.display.update()
    #updating the display with the items I have put before it
    
pygame.quit()
#Closes out the program
