'''
(only with minutes and seconds) 
which is synchronized with system clock.
Use Mickey's right hand as minutes arrow 
and left - as seconds.
'''
import pygame
mainclock=pygame.time.Clock()
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,598))
img=pygame.image.load('clock.png')
img2=pygame.image.load('sec.png')

angle=0
centerx=400
centery=598/2
running=True
while running:
    angle+=1
    screen.blit(img,(0,0))
    mx,my=pygame.mouse.get_pos()
    img2_copy=pygame.transform.rotate(img2,angle)
    screen.blit(img2_copy,(centerx-140,centery-300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
    mainclock.tick(60)