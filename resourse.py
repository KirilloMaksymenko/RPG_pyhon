import pygame
from config import *
import math
from sprite import *




class Tree(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        

        self.game = game 
        self._layer = RESOURSE_LAYER
        self.groups = self.game.all_sprites,self.game.objects
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.resourse_sprite_sheet.get_sprite(0,0,self.width,self.height)
        
        self.rect = self.image.get_rect(topleft = (x,y))
        self.rect.x = self.x
        self.rect.y = self.y
        

