# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 13:36:25 2017

@author: ucapy
"""
import pygame as pyg

class Image(pyg.sprite.Sprite):
    
    def __init__(self, image_file, location):
        
        pyg.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pyg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        


        
        