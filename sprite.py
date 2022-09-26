
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
        sprite = pygame.transform.scale(sprite, (64, 64))
        return sprite



    
class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game 
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites,self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.block_spritesheet.get_sprite(0,0,self.width,self.height)
        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    

class Ground(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game 
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(0,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

        