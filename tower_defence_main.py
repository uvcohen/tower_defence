# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:52:58 2017

@author: ucapy
"""

import pygame as pyg
import sys
from tower_defence_enemy import Enemy
from tower_defence_tower import Tower
from tower_defence_image import Image
import tower_defence_factors as f

pyg.init()

#------------------------------------------------------------------------------
# set up window
dis_sz_x = 690 #display size
dis_sz_y = 480  #int(dis_sz_x / 1.78)

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

FPS = 15 # frames per second setting
fpsClock = pyg.time.Clock()

#define variables
count_animation = 0
count_kill = 0
coins = 100
lives = 50
run_wave = False
enemy_start_pos_y = dis_sz_y / 2 + 26
display_lives = 0
display_coins = 0

# set up the window
window = pyg.display.set_mode((dis_sz_x, dis_sz_y), 0, 32)
pyg.display.set_caption('Tower defence!')
#create background
background = Image('img/background_image.jpeg', [0,0])
brick_background = Image('img/brick_background.png', [0,380])
#wave button
wave_button_pressed = Image('img/wave_button_pressed.png', [dis_sz_x - 100, dis_sz_y - 90])
wave_button_unpressed = Image('img/wave_button_unpressed.png', [dis_sz_x - 100, dis_sz_y - 90])
#Show lives & coins
font = pyg.font.SysFont("Times New Roman", 18, False, False)

enemy1 = Enemy(-40, enemy_start_pos_y, 100, 1)
enemy2 = Enemy(-70, enemy_start_pos_y, 100, 1)
enemys = [enemy1, enemy2]
"""
enemys_dic = {
        enemy1 : Enemy(-10, dis_sz_y / 2 + 26, 100, 1),
        enemy2 : Enemy(-30, dis_sz_y / 2 + 26, 100, 1)
        }
MAYBE I NEED A DICTONARY?!
enemys = {}
for i in range(0, 20):
    enemys['enemy_%s' % i] = Enemy(-10 * i, 10, 100, 1) #enemys[newkey] = [newvariable] 
"""
#create tower
tower1 = Tower(60, dis_sz_y - 70, 2, 1, 100, 20)
tower2 = Tower(90, dis_sz_y - 70, 2, 1, 100, 20)
towers = [tower1]
#create enemy images
images_tower = {
        0: tower1.img_0,
        }
prefix = "img/BODY_skeleton_%s-%s.png"
global enemy_image_list
enemy_image_list = []
for i in range(0, 4):
    enemy_image_list.append([""] * 9)
for i in range(0, 4): # up:0 left: 1 down: 2 right: 3
    for n in range(0, 9):
        enemy_image_list[i][n] = (pyg.image.load(prefix % (i, n)))

def enemy_animation(z):
    if f.factors_9(count_animation) == True:
        window.blit(enemy_image_list[z][8], (enemy.x_pos, enemy.y_pos)) 
    elif f.factors_8(count_animation) == True:
        window.blit(enemy_image_list[z][7], (enemy.x_pos, enemy.y_pos)) 
    elif f.factors_7(count_animation) == True:
        window.blit(enemy_image_list[z][6], (enemy.x_pos, enemy.y_pos))
    elif f.factors_6(count_animation) == True:
        window.blit(enemy_image_list[z][5], (enemy.x_pos, enemy.y_pos)) 
    elif f.factors_5(count_animation) == True:
        window.blit(enemy_image_list[z][4], (enemy.x_pos, enemy.y_pos))        
    elif f.factors_4(count_animation) == True and not f.factors_8(count_animation):
        window.blit(enemy_image_list[z][3], (enemy.x_pos, enemy.y_pos))
    elif f.factors_3(count_animation) == True and not f.factors_6(count_animation) and not \
    f.factors_9(count_animation):
        window.blit(enemy_image_list[z][2], (enemy.x_pos, enemy.y_pos))
    elif f.factors_2(count_animation) == True and not f.factors_4(count_animation) and not \
    f.factors_6(count_animation) and not f.factors_8(count_animation):
        window.blit(enemy_image_list[z][1], (enemy.x_pos, enemy.y_pos))
    else:
        window.blit(enemy_image_list[z][0], (enemy.x_pos, enemy.y_pos))

while True: # the main game loop
    #create images
    window.blit(background.image, background.rect)
    window.blit(brick_background.image, brick_background.rect)
    window.blit(wave_button_unpressed.image, wave_button_unpressed.rect)
    display_lives = font.render('Lives: ' + str(lives), 1, BLACK)
    window.blit(display_lives, (520, 30))
    display_coins = font.render('Coins: ' + str(coins), 1, BLACK)
    window.blit(display_coins, (420, 30))
    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
            
        if event.type == pyg.MOUSEBUTTONDOWN:
            mouse_pos = pyg.mouse.get_pos()
            
            if wave_button_unpressed.rect.collidepoint(mouse_pos):
                window.blit(wave_button_pressed.image, wave_button_pressed.rect)
                print('button was pressed at {0}'.format(mouse_pos))
                run_wave = True
            
            for tower in towers:
                if tower.rect.collidepoint(mouse_pos) and \
                tower.price < coins and tower.pos_set == False:
                    while tower.pos_set == False:
                        tower.x_pos = mouse_pos[0]
                        tower.y_pos = mouse_pos[1]                        
                        if event.type == pyg.MOUSEBUTTONDOWN:
                            tower.set_position(pyg.mouse.get_pos()) #set tower posiiton
                            coins -= tower.price                      
   
    #main tower/enemy loops
    for tower in towers:
        window.blit(images_tower[0], (tower.x_pos, tower.y_pos))
        for enemy in enemys:
            if enemy.alive == True and run_wave == True: #move enemy if alive
                if enemy.y_pos == enemy_start_pos_y:
                    enemy.move("right")
                    enemy_animation(3)
                if enemy.y_pos == 50:
                    enemy.move("right")
                    enemy_animation(3)
                if enemy.x_pos == 50 or enemy.x_pos == 220 or \
                enemy.x_pos == 400 or enemy.x_pos == 580:
                    enemy.move("up")
                    enemy_animation(0)
                if enemy.x_pos == 136 or enemy.x_pos == 136 + 180 or \
                enemy.x_pos == 136 + 360:
                    enemy.move("down")
                    enemy_animation(2)
                if enemy.x_pos == dis_sz_x:
                    lives -= 1
                    print (lives)
                    enemy.kill()                    
            if enemy.x_pos >= (tower.x_pos - tower.sight_range) and \
            enemy.y_pos >= (tower.y_pos - tower.sight_range) and \
            enemy.x_pos <= (tower.x_pos + tower.sight_range) and \
            enemy.y_pos <= (tower.y_pos + tower.sight_range): #damage enemy if in range
                enemy.health -= tower.damage
                print (enemy.health)
                if not enemy.check_alive(): #kill enemy if health == 0
                    enemy.kill()
                    count_kill += 1
                    coins += 10                    
            if count_kill == len(enemys):
                run_wave = False
       
    count_animation += 2


    pyg.display.flip()
    fpsClock.tick(FPS)