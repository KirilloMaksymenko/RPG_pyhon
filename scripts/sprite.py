
import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self,file):
        
        self.sheet = pygame.image.load(file).convert_alpha()
        

    # def get_sprite(self,x,y,width,height,c_x=0,c_y=0):
    #     print("main ",x,y,width,height,c_x,c_y)
    #     sprite = pygame.Surface([width,height])
        
    #     sprite.blit(self.sheet,(c_x,c_y),(x,y,width,height))
    #     sprite.set_colorkey(BLACK)
    #     sprite = pygame.transform.scale(sprite, (width, height))
    #     return sprite


        
