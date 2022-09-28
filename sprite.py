
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

            
    
class Target(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites,self.game.objects
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.animation_loop = 1

        self.target_anim = False
        
        self.image = self.game.target_spritesheet.get_sprite(0,0,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.shoot_anim()

    def shoot_anim(self):
        shoot_animate = [
            self.game.target_spritesheet.get_sprite(0,0,self.width,self.height),
            self.game.target_spritesheet.get_sprite(16,0,self.width,self.height),
            self.game.target_spritesheet.get_sprite(32,0,self.width,self.height),
            self.game.target_spritesheet.get_sprite(48,0,self.width,self.height),
            self.game.target_spritesheet.get_sprite(64,0,self.width,self.height),
            self.game.target_spritesheet.get_sprite(80,0,self.width,self.height),
            self.game.target_spritesheet.get_sprite(96,0,self.width,self.height),
        ]

        if self.target_anim:
           
            self.image = shoot_animate[math.floor(self.animation_loop)]
            self.animation_loop += 0.2
            if self.animation_loop >= 7:
                
                self.target_anim = False
                self.animation_loop = 1
        else:
            hits = pygame.sprite.spritecollide(self,self.game.attacks_layer,False)
            if hits:
                self.target_anim = True
        

        
