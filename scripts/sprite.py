
import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self,file):
        
        self.sheet = pygame.image.load(file).convert_alpha()
        

    def get_sprite(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        sprite = pygame.transform.scale(sprite, (width, height))
        return sprite


        
