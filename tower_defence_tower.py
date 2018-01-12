# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:57:11 2017

@author: ucapy
"""

import pygame as pyg

class Tower(object):
    
    def __init__(self, x_pos, y_pos, damage, fire_rate, sight_range, price):
        pyg.sprite.Sprite.__init__(self)
        image_file = 'img/tower.png'
        self.image = pyg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x_pos, y_pos
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pos_set = False
        self.damage = damage
        self.fire_rate = fire_rate
        self.sight_range = sight_range
        self.price = price
        self.bought = False
        
        
        self.img_0 = pyg.image.load('img/tower.png')

        
    def set_position(self, pos):
        self.x_pos, self.y_pos = pos
        self.x_pos -= 30
        self.y_pos -= 30
        self.pos_set = True
        
        
  