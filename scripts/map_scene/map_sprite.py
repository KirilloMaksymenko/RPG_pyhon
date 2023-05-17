
import pygame
from map_scene.map_config import *
import math
import random

class SpritesheetMap:
    def __init__(self,file):
        
        self.sheet = pygame.image.load(file).convert_alpha()
        

    def get_sprite(self,x,y,width,height,scale):
        sprite = pygame.Surface([width,height])
        
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        sprite = pygame.transform.scale(sprite, (width,height))
        return sprite
    
    def get_map_sprite(self,x,y,width,height,scale):
        sprite = pygame.Surface([width,height])
        
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        
        sprite = pygame.transform.scale(sprite, (width*scale,height*scale))
        return sprite

            
 
