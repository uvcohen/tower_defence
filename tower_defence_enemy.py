# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:13:23 2017

@author: ucapy
"""
#import tower_defence_main moved further down
import pygame as pyg

class Enemy(object):
       
      
    def __init__(self, x_pos, y_pos, health, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = health
        self.speed = speed
        self.alive = True
        

 #   def __getitem__(self, key):
  #      return enemy_image_list[key]
 
    def check_alive(self):
        if self.health <= 0:
            self.alive = False
        #print (self.alive)
        return self.alive
    
    def kill(self):
        self.x_pos = 10
        self.y_pos = 10
        self.move("stop")
                           
    
    def move(self, direction):
        if direction == 'right':
            self.x_pos += self.speed
        elif direction == 'down':
            self.y_pos += self.speed
        elif direction == 'left':
            self.x_pos -= self.speed
        elif direction == 'up':
            self.y_pos -= self.speed
        elif direction == "stop":
            self.x_pos = 10
            self.y_pos = 10            
        return direction, self.x_pos, self.y_pos

        
        