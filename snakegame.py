import pygame
import time
import random

pygame.init()

dis_width = 800
dis_height = 600

pygame.display.set_mode((dis_width, dis_height))
dis = pygame.display.set_mode((800,600))

pygame.display.set_caption("._.")

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 102)
green = (50, 153, 213)
purple = (184, 151, 219)

pygame.display.update()

snake_block = 10
snake_speed = 15

x1 = 300 
y1 = 300

snake_list = []
length_of_snake = 1

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None,50)
score_font = pygame.font.SysFont("comicsansms", 50)

def Your_score(score):
    value = font_style.render("Your Score: " + score)
    dis.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, x[0] , x[1], snake_block, snake_block)

def gameLoop():

        game_over = False 
        game_close = False


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/6])

    def gameLoop():

        game_over = False 
        game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("loosa", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_q:
                        game_over = True
                        game_close = False
                        pygame.quit()
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_speed
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_speed
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_speed
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_speed
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        pygame.draw.rect(dis, purple,[foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black,[x1, y1, snake_block, snake_block])
        pygame.display.update()

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            #for x == snake_head:
            game_close = True
        
        if x1 == foodx and y1 == foody:
            print (".|.")
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            length_of_snake +-1
    
    pygame.display.update()
    time.sleep(2)

    clock.tick(30)

    pygame.quit()

    quit()

gameLoop()
