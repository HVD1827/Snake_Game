import datetime
import math
import pygame
import time
import random

# Initialize the game
pygame.init()
global score_snake 

# Colors
white = (255, 255, 255)
yellow = (205, 205, 52)
black = (0, 0, 0)
red = (255, 30, 40)
green = (0, 255, 0)
dark_blue = (0, 0, 200)
orange = (255, 165, 0)
Olive_Green = (0, 128, 0)
Ligth_Green = (50, 205, 50)
Light_Yellow = (255, 255, 153)
# Screen parameters
dis_width = 800
dis_height = 600

# Creating the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
play_button = pygame.Rect(50, 500, 250, 80)
exit_button = pygame.Rect(500, 500, 250, 80)

background_image = pygame.image.load('background.jfif')
background_image = pygame.transform.scale(background_image, (dis_width, dis_height))
# Clock
clock = pygame.time.Clock()
snake_block = 10


font_style = pygame.font.SysFont(None, 50)



def score(score1):
    small_font = pygame.font.SysFont(None, 25)
    score2 = small_font.render(score1, True, dark_blue)
    dis.blit(score2, [20, 5])

def hiscore():
    small_font = pygame.font.SysFont(None, 25) 
    score2 = small_font.render(f"Highest Score:{highscore}", True, dark_blue)
    dis.blit(score2, [650, 5])

def message(score, color):
    mess = font_style.render(score, True, color)
    dis.blit(mess, [dis_width / 3.2, dis_height / 6])

def draw_apple(x, y, block_size, color):
    # Draw the colored part of the apple
    pygame.draw.circle(dis, color, (x + block_size // 2, y + block_size // 2), block_size // 2)
    # Draw the green stem
    pygame.draw.rect(dis, green, [x + block_size // 2 - block_size // 8, y, block_size // 2 + 2, block_size // 4])
    pygame.draw.rect(dis, green, [x + block_size // 2 - block_size // 8, y - 4, block_size // 4, block_size // 2])

global color
def gameLoop():  # main function
    global highscore
    # highscore = 0
    snake_speed = 16  
    global apple_appearance_time 
    apple_display_duration = 8500 

    game_over = False
    game_close = False
    score_snake = 0
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(40, dis_height - snake_block) / 10.0) * 10.0
    color = red
    apple_appearance_time = pygame.time.get_ticks()  # the time interval for the apple appearance

    while not game_over:

        while game_close == True:
            if highscore < (Length_of_snake-1):
                highscore = Length_of_snake-1
            dis.fill(black)
            mouse = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse):
                pygame.draw.rect(dis, white, play_button)
            else:
                pygame.draw.rect(dis, green, play_button)
            if exit_button.collidepoint(mouse):
                pygame.draw.rect(dis, white, exit_button)
            else:
                pygame.draw.rect(dis, red, exit_button)

            text_start = font_style.render("PLAY AGAIN", True, dark_blue)
            dis.blit(text_start, ((play_button.x + 20, play_button.y + 20)))

            text_end = font_style.render("QUIT", True, black)
            dis.blit(text_end, (exit_button.x + 85, exit_button.y + 20))

            message(f"Your Score is : {Length_of_snake-1} ", white)
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            game = False
            if play_button.collidepoint(mouse):
                game == True

            while game == True:
                def draw_button():
                    pygame.draw.rect(dis, white, play_button)

                if play_button.collidepoint(mouse):
                    draw_button()
                else:
                    game == False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.collidepoint(event.pos):
                        game_over = True
                        game_close = False
                    if play_button.collidepoint(event.pos):
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Check if the apple should be updated
        current_time = pygame.time.get_ticks()
        if current_time - apple_appearance_time > apple_display_duration:
            # generate a new appl in case it is not present
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(40, dis_height - snake_block) / 10.0) * 10.0
            color = random.choice([red, dark_blue, yellow])
            apple_appearance_time = pygame.time.get_ticks()  
            
        draw_apple(foodx, foody, snake_block, color)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        count = 0
        for x in snake_List:
            if count%3 == 0:
                pygame.draw.rect(dis,Olive_Green,[x[0], x[1], snake_block, snake_block])
                count = count + 1
            elif count%3 == 1 :
                pygame.draw.rect(dis,Ligth_Green,[x[0], x[1], snake_block, snake_block])      
                count = count + 1
            elif count%3 == 2:           
                pygame.draw.rect(dis, Light_Yellow ,[x[0], x[1], snake_block, snake_block])
                count = count+1
            
        score(f"Your Score:{Length_of_snake-1}")
        hiscore()
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            if color == red:
                Length_of_snake += 1
            elif color == dark_blue:
                Length_of_snake += 2
            elif color == yellow:
                Length_of_snake += 4

            # Generating a new apple
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(40, dis_height - snake_block) / 10.0) * 10.0
            color = random.choice([red, dark_blue, yellow])  
            apple_appearance_time = pygame.time.get_ticks()  

        clock.tick(15) 

    pygame.quit()
    quit()

def home_screen():
    home = True
    while home:
        dis.blit(background_image, (0, 0))
        message("Press Enter to Start", white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    home = False

highscore = 0
home_screen()
gameLoop()
