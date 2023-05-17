
import pygame
from map_scene.map_config import *
import numpy as np
import math
import random

class SpritesheetMap:
    def __init__(self,file):
        self.c = 0
        self.sheet = pygame.image.load(file)
        

    def get_sprite(self,x,y,width,height,scale):
        
        sprite = pygame.Surface([width,height])
        
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        sprite = pygame.transform.scale(sprite, (width*scale,height*scale))

        return sprite
    
    def get_map_sprite(self,x,y,width,height,scale):
        sprite = pygame.Surface([width,height])
        
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        
        sprite = pygame.transform.scale(sprite, (width*scale,height*scale))
        return sprite

    def halo_sprite(self,x,y,width,height,scale):
        self.c += 1
        sprite = pygame.Surface([width,height])
        
        hologram_image = self.sheet.copy()

        blue_tint = (0, 0, 255) 
        pixels_blue = pygame.surfarray.pixels3d(hologram_image)
        pixels_blue[:] = pixels_blue[:] // 9
        pixels_blue[:] = pixels_blue[:] * np.array(blue_tint)[None, None, :]
        del pixels_blue

        hologram_image.set_alpha(128)

        sprite_mask = pygame.mask.from_surface(self.sheet)

        self.sheet.set_colorkey((0, 0, 0))
        self.sheet.set_alpha(255)

        for i in range(100): 
            pygame.draw.rect(self.sheet,(0,0,0),pygame.Rect(0,i*7,640,2 ))

        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(WHITE)
        sprite.blit(hologram_image,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
            
        return sprite
            
 
