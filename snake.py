import pygame
import random

pygame.init()

#Colors
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
purp=(150,0,255)

#window settings
dis_width=800
dis_height=800
dis = pygame.display.set_mode((dis_width,dis_width))
pygame.display.set_caption('this caption is completely irrelevant and way longer than it should be but whatever.py')

clock = pygame.time.Clock() #Speed of screen update
snake_block=10  #Size of snake
snake_speed=30  #Speed of snake

#comic sans
font_style = pygame.font.SysFont("comicsansms",25)
score_font = pygame.font.SysFont("comicsansms", 35)

#function to track score
def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, red)
    dis.blit(value, [0,0])

def Your_snake(snake_block, snake_list):
    for x in  snake_list:
        pygame.draw.rect(dis, purp, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/4,dis_height/2])

#function to continue playing instead of exit on game over    
def gameLoop(): 
    game_over = False
    game_close =  False
    
    #default starting pos
    x1=dis_width/2
    y1=dis_height/2
   
    #values to change snake head pos
    x1_change=0
    y1_change=0
    
    snake_List = [] 
    Length_of_snake = 1
    
    #food pos
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True:
            dis.fill(blue)
            message('You lost nerd. Q: Quit C: Play again', red)
            Your_score(Length_of_snake-1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block
                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close=True

        x1+=x1_change
        y1+=y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx,foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                
        Your_snake(snake_block, snake_List)
        Your_score(Length_of_snake-1)
        
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            Length_of_snake+=1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()
    
gameLoop()