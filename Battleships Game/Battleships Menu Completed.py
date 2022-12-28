import pygame
import random
import time
import pygame.gfxdraw
from math import sqrt
#importing all of the libraries I need for the program



mouseHover=False
def mouseChange():
    global mouseHover
    pygame.mouse.set_visible(False)
    mouseHover=True

    #Subroutine to change the mouse into the hand icon


pygame.init()
pygame.font.init()

#initiating pygame and allowing me to use fonts

gamewidth=1366
gameheight=768
timeDelay=1

#setting the constants for the program window

playx=890
playy=270
playLength=100

tutorialx=850
tutorialy=372
tutorialLength=175

stylex=875
styley=470
styleLength=120

leaderboardx=805
leaderboardy=568
leaderboardLength=260

B_width=65

def HomeScreen():
    homeScreen=pygame.image.load('Home Screen.jpg')
    win.fill((0,0,0))
    homeScreen=pygame.transform.scale(homeScreen,(gamewidth,gameheight))
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


win=pygame.display.set_mode((gamewidth,gameheight), pygame.RESIZABLE)
pygame.display.set_caption("Battleships")
icon=pygame.image.load('Icon.ico')
pygame.display.set_icon(icon)
mouseHand=pygame.image.load('mouseHand.png')
mouseHand=pygame.transform.scale(mouseHand,(15,15))

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
        #put play subroutine here
        mouseChange()
        mouse=pygame.mouse.get_pressed()
        if mouse==(True,False,False):
            pygame.mouse.set_visible(True)
        
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
