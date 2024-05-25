try:
    import pygame, time
except ImportError:
    print("Cannot import pygame, try 'pip3 install pygame'")
from random import randint
class Snake:
    def __init__(self):
        self.name = "Snake"
        self.dis = pygame.display.set_mode((400,300))
        self.blue=(0,0,255)
        self.red=(255,0,0)
        self.black = (0,0,0)
        self.game_over=False # boolean
        pygame.display.set_caption('Snake')
        self.snake = [] # int list
        self.apple = () # int tuple
        self.snakeLength = 3 # int
        self.x = 200 # int
        self.y = 150 # int
        self.ori = 'E' # char

    def init(self):
        pygame.init()



    def spawnApple(self, max_x, max_y):
        x = randint(0,max_x)
        y = randint(0,max_y)
        x = (x//10) * 10
        y = (y//10) * 10
        apple = (x,y)
        if apple in self.snake:
            x = randint(0,max_x)
            y = randint(0,max_y)
            x = (x//10) * 10
            y = (y//10) * 10
            apple = (x,y)
        return apple
    
    def run(self):
        while not self.game_over:
    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.ori !='E':
                        self.ori = 'W'
                    if event.key == pygame.K_RIGHT and self.ori !='W':
                        self.ori = 'E'
                    if event.key == pygame.K_DOWN and self.ori !='N':
                        self.ori = 'S'
                    if event.key == pygame.K_UP and self.ori !='S':
                        self.ori = 'N'

            self.snake.insert(0,(self.x,self.y))
            if len(self.snake) > self.snakeLength :
                pygame.draw.rect(self.dis, self.black, [self.snake[self.snakeLength][0],self.snake[self.snakeLength][1],10,10])
                self.snake.pop()
        
            if self.apple == ():
                self.apple = self.spawnApple(400,300)
                pygame.draw.rect(self.dis, self.red, [self.apple[0], self.apple[1], 10,10])

            if self.x == self.apple[0] and self.y == self.apple[1]:
                self.snakeLength += 1
                self.apple = self.spawnApple(400,300)
                pygame.draw.rect(self.dis, self.red, [self.apple[0], self.apple[1], 10,10])

            if self.ori == 'N':
                self.y = self.y-10
            if self.ori == 'E':
                self.x = self.x+10
            if self.ori == 'S':
                self.y = self.y+10
            if self.ori == 'W':
                self.x = self.x-10
            if (self.x,self.y) in self.snake:
                self.game_over = True

            pygame.draw.rect(self.dis,self.blue,[self.x,self.y,10,10])
            pygame.display.update()
            
            time.sleep(0.125)
            if self.x<0 or self.x+10>400 or self.y<0 or self.y+10>300:
                self.game_over = True
                return self.snakeLength
    
    
 
if __name__ == "__main__":
    snake = Snake()
    snake.init()
    score = snake.run()
    print(f"score: {score}")
    
