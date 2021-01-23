import pygame
import random

from pygame import *
                      
 
                                                   
pygame.init()

width, height = 740, 500
screen = pygame.display.set_mode((width, height))
player = [pygame.transform.scale(pygame.image.load("Resources/Balljump-1(2).png"), (100,100)), pygame.transform.scale(pygame.image.load("Resources/Balljump-1.png"),(100,100))]
launch = [pygame.transform.scale(pygame.image.load("Resources/Balljump-1.png"), (100,100)), pygame.transform.scale(pygame.image.load("Resources/Balljump-1(2).png"), (100,100)),pygame.transform.scale(pygame.image.load("Resources/Balljump-2.png"), (100,100)),pygame.transform.scale(pygame.image.load("Resources/Balljump-3.png"), (100,100)), pygame.transform.scale(pygame.image.load("Resources/Balljump-4.png"),(100,100))]
shoot = [pygame.transform.scale(pygame.image.load("Resources/Balljump-5.png"), (100, 100)), pygame.transform.scale(pygame.image.load("Resources/Balljump-6.png"), (100, 100))]
ball = pygame.transform.scale(pygame.image.load("Resources/ball.png"), (100,100))
blue = (0, 0, 128)
white = (255, 255, 255)

janimation, danimation, movable, motionactivate, limit_reached, nojump = False, False, False, False, False, False
jumplock = True
ballrelease, ballregain = False, False
fr = pygame.time.Clock()
c = 0
i = 0
p = 0
x, y = 0, 300
score = 0
a, b, rpos = 0, 0, 0
xpos, ypos = 17, 313 

# Background image source: https://www.freepik.com/free-vector/floral-ornamental-abstract-background_6189902.htm#page=1&query=black%20background&position=40
background = pygame.image.load("Resources/back.jpg")


gamestart = False


def basketball():
    
    #Draw basketball
    
    global rpos, xpos, ypos, ballregain
    if gamestart == True and ballrelease == False:

        if nojump == True:

            if c % 2 == 0:
                screen.blit(ball, (xpos, ypos + 24))
            
            if c % 2 == 1:
                screen.blit(ball, (xpos + 2 , ypos ))
    

        
        if nojump == False and motionactivate == True:
            
            if p // 4 == 0:
                screen.blit(ball, (xpos, ypos)) 
            if p // 4 == 1:
                screen.blit(ball, (xpos-2, ypos-5))
            if p // 4 == 2:
                screen.blit(ball, (xpos-2, ypos-7))
            if p // 4 == 3:
                screen.blit(ball, (xpos-2, ypos-11))
            if p// 4 == 4:
                screen.blit(ball, (xpos-2, ypos-13))
        
        if janimation == True:
            rpos = y -13
            screen.blit(ball, (xpos, rpos))
    
    rposNew = 400 - rpos
    
    if gamestart == True and ballrelease == True:
        
       
        if rpos <= 325:
            
            screen.blit(ball, (xpos, rpos))
        
            if xpos <= 700:
                ballregain = False
                xpos += (rposNew / 20)
                print("rpos is: " + str(rpos) + " xpos is: " + str(xpos))
                rpos = (-1*((xpos/600)**2))+((xpos)/150)+rpos
                
            
        if xpos > 700 or rpos > 325:
            xpos = 17
            ballregain = True
        

def player_animations():

    # Animations while the user makes no input
    global c
    global player
    global i

    if nojump == True:
        
        if c % 2 == 0 and i<= 10:
            if i<10:
                screen.blit(player[c], (0, 300))
                i += 1
            if i == 10: 
                c += 1
                i += 1
        
        
        elif c % 2 == 1 and i<= 20:
            if i>10 and i<20:
                screen.blit(player[c], (0, 300))
                i += 1
            if i == 20:
                c -= 1
                i += 1
        
        elif i>20:
            i = 0
            screen.blit(player[c], (0, 300))
    
    if nojump == False:
        screen.fill(0)

def screen_text():

    global score
    global nojump
    global movable

    if nojump == True:

        font = pygame.font.Font("Resources/android.ttf", 16)
        text2 = font.render("Hold space to throw the ball", True, white)
        textRect2 = text2.get_rect()
        textRect2.center = (width // 2, height // 2 + 200)
        screen.blit(text2, textRect2)
        movable = True

    font = pygame.font.Font("Resources/android.ttf", 16)
    text2 = font.render("Score: "+ str(score), True, white)
    textRect2 = text2.get_rect()
    textRect2.center = (width // 2 - 300, height // 2 - 200)
    screen.blit(text2, textRect2)    

def player_jump():

    # Initial animations before the player jumps
    global p, nojump, movable, x, y, janimation, danimation, a, b, motionactivate, limit_reached
    global jumplock, ballrelease, ballregain
    

    if movable == True and keypress[K_SPACE]:
        #print(pygame.time.get_ticks())
        
        motionactivate = True
        #print(nojump)
        #if p >= 19:
        #    p = 0    
    if motionactivate == True:
        #screen.fill(0)
        nojump = False     
        if p < 21:
            screen.blit(launch[p // 4], (0, 300))
            p += 1

        if p == 20: 
            a = pygame.time.get_ticks()
            janimation = True
            p += 1
            
            
    
    #elif keypress[K_SPACE]:
        # what to do when jump is completed
    

    if janimation == True and limit_reached == False:
        
        if keypress[K_SPACE] and pygame.KEYDOWN and jumplock == True:
            b = pygame.time.get_ticks()
            if y > 239:
                y = ((b - a) / -25) + 310
            if y >= 305:
                screen.fill(0)
                screen.blit(shoot[0], (x, y))
            if y < 305 and y > 240:
                screen.blit(shoot[1], (x,y))
            if y <= 239:
                screen.blit(shoot[0], (x, y))
                danimation = True
                limit_reached = True
                #print(danimation)

    if event.type == pygame.KEYUP:
        if event.key == K_SPACE:
            danimation = True
            motionactivate = False
            ballrelease = True
    if danimation == True:
        jumplock = False    
    if danimation == True or limit_reached == True:
        #print("poopc "+ str(y))
        if y < 310:
            screen.blit(shoot[0], (x, y))
            y += 2
            #
            # print("zag")
                #print("poop: " + str(pygame.KEYUP) + " key down is: " + str(pygame.KEYDOWN))
        if y >= 310:
            nojump = True
            danimation = False
            janimation = False
            movable = False
            limit_reached = False
            p = 0
            jumplock = True
            if ballregain == True:
              
                ballrelease = False

            #print("y value is: "+ str(y)+ " a is: "+ str(a) + " b is: "+ str(b)) 
        

        
while 1:
    
    keypress = pygame.key.get_pressed()
    fr.tick(30)
    screen.fill(0)

    if keypress[K_RETURN]:
        gamestart = True

    if gamestart == False:
        #screen.fill(0)
        screen.blit(background, (0,0))

        # Draw opening texts
        font = pygame.font.Font("Resources/android.ttf", 64)
        text = font.render("Portal Hoop", True, white)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2 - 100)
        screen.blit(text, textRect)

        font = pygame.font.Font("Resources/android.ttf", 18)
        text2 = font.render("Press Return to start", True, white)
        textRect2 = text2.get_rect()
        textRect2.center = (width // 2, height // 2 + 100)
        screen.blit(text2, textRect2)

        nojump = True

    
    # Check if any

    if gamestart == True:
        #screen.fill(0)
        
        player_animations()
        player_jump()
        basketball()
        screen_text()
       
        
        

    pygame.display.flip()
    pygame.display.set_caption("Portal Hoop")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit(0)



