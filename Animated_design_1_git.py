import pygame,sys
from math import cos,sin
from pygame.locals import *
import random

pygame.init()

fps=15
fpsClock=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((1500,1500),0,32)
pygame.display.set_caption("Animated Design ")
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
cr=(220,255,250)
tree=pygame.draw.circle(DISPLAYSURF,blue,(223,257),20,4)
catImg=pygame.image.load('cat.png')
catx=1000
caty=300
dire='right'
t=0.1
n=[blue,green,black,red]
x=0


while True:
    DISPLAYSURF.fill(cr)

    rx1=[]
    ry1=[]
    rx2=[]
    ry2=[]
    for s in range(8):
        rx1.append(random.randint(900,1400))
        ry1.append(random.randint(100,500))
        rx2.append(random.randint(900,1400))
        ry2.append(random.randint(100,500))
        
        
    pygame.draw.line(DISPLAYSURF,n[(random.randint(0,3))],(rx1[(random.randint(0,7))],ry1[(random.randint(0,7))]),(rx2[(random.randint(0,7))],ry2[(random.randint(0,7))]),3)
    pygame.draw.line(DISPLAYSURF,n[(random.randint(0,3))],(rx1[(random.randint(0,7))],ry1[(random.randint(0,7))]),(rx2[(random.randint(0,7))],ry2[(random.randint(0,7))]),3)
    pygame.draw.line(DISPLAYSURF,n[(random.randint(0,3))],(rx1[(random.randint(0,7))],ry1[(random.randint(0,7))]),(rx2[(random.randint(0,7))],ry2[(random.randint(0,7))]),3)
    pygame.draw.line(DISPLAYSURF,n[(random.randint(0,3))],(rx1[(random.randint(0,7))],ry1[(random.randint(0,7))]),(rx2[(random.randint(0,7))],ry2[(random.randint(0,7))]),3)

    del rx1[:]
    del rx2[:]
    del ry1[:]
    del ry2[:]

    fontobj=pygame.font.Font('freesansbold.ttf',22)
    textobj=fontobj.render('ishank agarwal',True,green,blue)
    textrectobj=textobj.get_rect()
    textrectobj.center=(1000,700)
    for i in range(1,360):
        
        pygame.draw.circle(DISPLAYSURF,n[x],(int(400-200*cos(i)),int(400-200*sin(i))),180,1)
        x=x+1;
        if (x==4):
            x=0
            



    pixObj=pygame.PixelArray(DISPLAYSURF)
    pixObj[480][380]=black
    pixObj[480][381]=black
    pixObj[481][380]=black
    pixObj[481][381]=black
    pixObj[482][381]=black
    pixObj[481][382]=black
    pixObj[483][381]=black
    pixObj[481][383]=black
    pixObj[484][381]=black
    pixObj[481][384]=black

    del pixObj

    
    if dire=='right':
        catx+=20
        if catx==1100:
            dire='down'
    elif dire=='down':
        caty+=20
        if caty==400:
            dire='left'
    elif dire=='left':
        catx-=20
        if catx==900:
            dire='up'
    elif dire=='up':
        caty-=20
        if caty==200:
            dire='right'

    DISPLAYSURF.blit(catImg,(catx,caty))
    
    
    t+=0.1
    DISPLAYSURF.blit(catImg,(int(350-200*cos(t)),int(350-200*sin(t))))
    DISPLAYSURF.blit(textobj,textrectobj)
    
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(fps)
