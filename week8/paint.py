import pygame
pygame.init()
window_width,window_height=700,500
fps=60
draw=False
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,255,0)
green=(0,0,255)
mode='pen'
color=black
thickness=5#default radius for the circle and thickness for other modes
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Aruka's Paint")
clock = pygame.time.Clock()
screen.fill(white)
running=True

def drawline(screen, start, end, thickness, color):
    x1,y1= start[0],start[1]
    x2,y2 = end[0],end[1]
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1 
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), thickness)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), thickness)
#start=PreviousPos which is the MOUSEBUTTONDOWN
#end=event.pos which is the MOUSEBUTTONUP
def drawRectangle(screen, start, end, thickness, color):
    x1,y1= start[0],start[1]
    x2,y2 = end[0],end[1]
    width = abs(x1-x2)
    height = abs(y1-y2)
    pygame.draw.rect(screen, pygame.Color(color), (x1, y1, width, height), thickness)


def drawCircle(screen, start, end, thickness, color):
    x1,y1= start[0],start[1]
    x2,y2 = end[0],end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2 
    #x and y here are the center of the circle
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, thickness)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode='rectangle'
            if event.key == pygame.K_2:
                mode='circle'
            if event.key == pygame.K_p:
                mode='pen'
            if event.key == pygame.K_e: #white is used for eraser
                mode='pen'
                color=white
            if event.key == pygame.K_g:
                color =green
            if event.key == pygame.K_b:
                color =black
            if event.key == pygame.K_r:
                color =red
        if event.type==pygame.MOUSEBUTTONDOWN:
            draw=True
            if mode=='circle':
                pygame.draw.circle(screen,color,event.pos,thickness)
            previousPos=event.pos
        if event.type==pygame.MOUSEBUTTONUP:
            if mode=='rectangle':
                drawRectangle(screen,previousPos,event.pos,thickness,color)
            elif mode=='circle':
                drawCircle(screen,previousPos,event.pos,thickness,color)
            else:
                draw=False
        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawline(screen, lastPos, event.pos, thickness, color)
            elif draw and mode == 'erase':
                drawline(screen, lastPos, event.pos, thickness, 'white')
            lastPos = event.pos
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 100, 100))
    pygame.display.flip()
    clock.tick(fps)

