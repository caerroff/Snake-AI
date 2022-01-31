import pygame, time
from random import randint
pygame.init()
dis=pygame.display.set_mode((400,300))

pygame.display.set_caption('Snake')

def spawnApple(max_x, max_y):
    x = randint
    apple = (x,y)
    return apple
 
blue=(0,0,255)
red=(255,0,0)
black = (0,0,0)
 
game_over=False # boolean
snake = [] # int list
apple = () # int tuple
snakeLength = 3 # int
x = 200 # int
y = 150 # int
ori = 'E' # char
while not game_over:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ori !='E':
                ori = 'W'
            if event.key == pygame.K_RIGHT and ori !='W':
                ori = 'E'
            if event.key == pygame.K_DOWN and ori !='N':
                ori = 'S'
            if event.key == pygame.K_UP and ori !='S':
                ori = 'N'

    snake.insert(0,(x,y))
    if len(snake) > snakeLength :
        pygame.draw.rect(dis, black, [snake[snakeLength][0],snake[snakeLength][1],10,10])
        snake.pop()
    
    apple = spawnApple(400,300)

    if ori == 'N':
        y = y-10
    if ori == 'E':
        x = x+10
    if ori == 'S':
        y = y+10
    if ori == 'W':
        x = x-10
    if (x,y) in snake:
        game_over = True
    pygame.draw.rect(dis,blue,[x,y,10,10])
    pygame.display.update()
    
    time.sleep(0.125)
    if x<0 or x+10>400 or y<0 or y+10>300:
        game_over = True



time.sleep(2)
pygame.quit()
quit()


