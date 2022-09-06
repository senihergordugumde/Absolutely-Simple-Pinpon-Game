#Sınıflara ayır
#Nesne Tabanlı Programla!

import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Absolutely Simple Pinpon Game")
assets = ["heart.png","zxf.jpg"]

bg = pygame.image.load(assets[1])
bg = pygame.transform.scale(bg,(800,600))
#Player
player_x = 400
player_y = 550
player2_x = 400
player2_y = 50
#Ball
ball_x = random.randint(0,795)
ball_y = random.randint(0,450)
spawn = True
#Heart
heart_x = random.randint(0,745)
heart_y = random.randint(0,450)
heart_spawn = False
#Player Move Mechanics
move_left = False
move_right = False
#Ball Move Mechanics
color = (255,255,255)
ball_move_up = False
ball_move_down = True
ball_move_left = True
ball_move_right = False
ball_vel=4
playervel = 5*2
#Values
skor = 0
player2_lives = 3
pause = False
stop = False
main_menu = True
spawn_time = 0
font = pygame.font.Font("font/poxel-font.ttf",35)
fps = 90
ball_touch_count = 0
heart_box = False
player1_lives = 3
#player2

player2_move_right = False
player2_move_left = False

while True:
    pygame.time.Clock().tick(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player2_move_right = True
            if event.key == pygame.K_LEFT:
                player2_move_left = True
            if event.key == pygame.K_ESCAPE:
                pause = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player2_move_right = False
            if event.key == pygame.K_LEFT:
                player2_move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False

    #Player Controls
    if stop == False:
        if player2_move_left:
            player2_x -= playervel
        if player2_move_right:
            player2_x += playervel
        if move_right:
            player_x += playervel
        if move_left:
            player_x -= playervel
        if player_x <= 4:
            player_x = 4
        if player_x>= 695:
            player_x = 695
        if player2_x <= 4:
            player2_x = 4
        if player2_x >= 695:
            player2_x = 695
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        player = pygame.draw.rect(screen,(255,0,0),pygame.Rect(player_x,player_y,100,10))
        player2 = pygame.draw.rect(screen,(0,0,255),pygame.Rect(player2_x,player2_y,100,10))

        if spawn == True:
            ball = pygame.draw.rect(screen,(255,255,255),pygame.Rect(ball_x,ball_y,10,10))

        #Ball Movement
        if ball_move_left:
            ball_x -= ball_vel
            if ball_x <= 0:
                ball_move_left = False
                ball_move_right = True
        if ball_move_right:
            ball_x += ball_vel
            if ball_x >= 799:
                ball_move_left = True
                ball_move_right = False
        if ball_move_up:
            ball_y -= ball_vel
            if pygame.Rect.colliderect(player2,ball):
                ball_move_down = True
                ball_move_up = False
                spawn_time += 1
                ball_touch_count +=1
                color = (0,0,255)
            if ball_y <= 0:
                spawn = False
                ball_y = random.randint(589,599)
                ball_x = random.randint(0,795)
                player2_lives -= 1

        if ball_move_down:
            ball_y += ball_vel
            if pygame.Rect.colliderect(player,ball):
                ball_move_down = False
                ball_move_up = True
                skor += 1
                spawn_time += 1
                ball_touch_count +=1

        if ball_y >= 600:
            spawn = False
            ball_y = random.randint(0,1)
            ball_x = random.randint(0,795)
            player1_lives -= 1

        if ball_y <= 600:
            spawn = True

        if ball_touch_count >= 5:
            heart_spawn = False
        if ball_touch_count >= 7:
            heart_spawn = False
            ball_touch_count = 0
    #Heart
    heart = pygame.image.load(assets[0])
    if heart_spawn:
        heart_box = pygame.Rect(heart_x+25,heart_y+17,15,18)
        screen.blit(heart,(heart_x,heart_y))
        if pygame.Rect.colliderect(heart_box,ball):
            heart_x = random.randint(0,785)
            heart_y = random.randint(0,450)
        #    lives += 1
            heart_spawn = False
            ball_touch_count = 0
    draw_skor = font.render("Player 1: {} ".format(player1_lives),True,(255,0,0))
    draw_lives = font.render("Player 2: {}".format(player2_lives),True,(0,0,255))
    screen.blit(draw_skor,(10,0))
    screen.blit(draw_lives,(600,0))
    if player2_lives <= 0 or player1_lives <= 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = False
        pos = pygame.mouse.get_pos()
        stop = True
        restrat_text = font.render(" Restrat",True,(255,255,255))
        quit_text = font.render("Quit",True,(255,255,255))
        restrat_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,130,152,39),2)
        quit_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,180,152,39),2)
        screen.blit(restrat_text,(310,130))
        screen.blit(quit_text,(350,180))
        if event.type == pygame.MOUSEBUTTONUP:
            if restrat_text_rect.collidepoint(pos):
                ball_x = random.randint(0,795)
                ball_y = random.randint(0,450)
                stop = False
                player2_lives = 3
                player1_lives = 3
            if quit_text_rect.collidepoint(pos):
                pygame.quit()
                sys.exit()

    if pause == True:
        stop = True
        continue_text = font.render("Continue",True,(255,255,255))
        quit_text = font.render("Quit",True,(255,255,255))
        continue_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,130,152,39),2)
        quit_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,180,152,39),2)

        screen.blit(continue_text,(310,130))
        screen.blit(quit_text,(350,180))
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if continue_text_rect.collidepoint(pos):
                pause = False
                stop = False
            if quit_text_rect.collidepoint(pos):
                pygame.quit()
                sys.exit()

    pygame.display.update()
