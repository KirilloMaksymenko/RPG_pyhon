import pygame
from platformer_scene.platformer_config import *
import math
import random

class SpritesheetPlatformer:
    def __init__(self,file):
        
        self.sheet = pygame.image.load(file).convert_alpha()
        

    def get_sprite(self,x,y,width,height,id):
        sprite = pygame.Surface([44,4])
        
        sprite.blit(self.sheet,(0,0),(x,y,44,44))
        sprite.set_colorkey(BLACK)
        sprite = pygame.transform.scale(sprite, (44, 44))
        return sprite

            
 
