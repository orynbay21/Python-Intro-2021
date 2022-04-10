#collision check with the walls
import pygame
import random
green=(0,100,0)
black=(0,0,0)
red=(255,0,0)
grey=(69,69,69)
yellow=(250,253,15)
pygame.init()
window_width,window_height=500,500
screen=pygame.display.set_mode((window_width,window_height))
class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  
        self.radius = 10
        self.dx = 5 
        self.dy = 0
        self.add_size = False
        self.speed = 25
        self.score=0
        self.level=1
        self.running=True
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (black), element, self.radius)
    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.add_size = False
    def message1(self):
        font = pygame.font.SysFont("comicsansms", 20)
        text1 = font.render("Current level: "+str(self.level), True,black)
        return text1
    def message2(self):
        font = pygame.font.SysFont("comicsansms", 20)
        text2 = font.render("Current score: "+str(self.score), True,black)
        return text2
    def move(self):
        if self.add_size:
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1]+= self.dy
        if self.elements[0][0] > window_width: 
            self.elements[0][0]=0 
        elif self.elements[0][0]<0: 
            self.elements[0][0]=window_width
        if self.elements[0][1] >window_height: 
            self.elements[0][1] =0
        elif self.elements[0][1]<0: 
            self.elements[0][1]=window_height
    def collision_check(self):
        if snake.level>=2:
            if self.elements[0][0]>=300 and self.elements[0][0]<=340 and self.elements[0][1]>=0 and self.elements[0][1]<=150:
                self.running=False
            elif self.elements[0][0]>=150 and self.elements[0][0]<=200 and self.elements[0][1]>=300 and self.elements[0][1]<=window_height:
                self.running=False
            return self.running
        else:
            return self.running
    def eat(self, foodx1, foody1):
        if foodx1 <= self.elements[0][0] <= foodx1 + 10 and foody1 <= self.elements[0][1] <= foody1 + 10:
            self.score+=1
            if self.score % 3 == 0:
                self.speed += 5
                self.level+=1
            return True
        return False  
    def walls(self):
        if self.level>=2:
            return True
class Food:
    def __init__(self):
        self.x = random.randint(1, window_width)
        self.y = random.randint(1, window_height)

    def gen(self):
        self.x = random.randint(1, window_width)
        self.y = random.randint(1, window_height)
        if snake.level>=2:
            if self.x>=300 and self.x<=340:
                self.y=random.randint(151,window_height)
            elif self.x>=150 and self.x<=200:
                self.y=random.randint(1,300)
    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, 10, 10))

snake = Snake(100, 100) #100,100 is the initial position
food1 = Food()
FPS = 30
d = 5
clock = pygame.time.Clock()
while snake.collision_check():
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d
    if snake.eat(food1.x, food1.y):
        snake.add_size = True
        food1.gen()
    snake.move()
    screen.fill(green)
    screen.blit(snake.message1(),(10,10))
    screen.blit(snake.message2(),(30,30))
    if(snake.walls()):
        pygame.draw.rect(screen,grey, pygame.Rect(300,0,40,150))
#syntax pygame.draw.rect(surface, color, pygame.Rect(leftx,lefty,width,height))
        pygame.draw.rect(screen,grey,pygame.Rect(150,300,50,200))
    snake.draw()
    food1.draw()
    pygame.display.flip()
pygame.quit()