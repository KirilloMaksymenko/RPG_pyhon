import pygame
from time import sleep

from platformer_scene.platformer_function import *
from platformer_scene.platformer_config import *
from platformer_scene.platformer_sprite import *

class Platform(pygame.sprite.Sprite):
    def __init__(self,game,wight,name,x,y):
        super().__init__()
        self.game = game
        self.groups = self.game.platformer_solid,self.game.platformer_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.image = pygame.Surface((wight, 20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.name = name
        self.c = 0
        self.direction = 1
        self.vel = 0
        self.rect.x = x
        self.rect.y = y


    def vertical_move(self):
        self.vel = 1
        if self.c >= 100:
            self.c = 0
            self.direction = self.direction * -1
        self.rect.y += self.vel * self.direction
        self.c = self.c + 1
    
    def horizontal_move(self):
        self.vel = 1
        if self.c >= 100:
            self.c = 0
            self.direction = self.direction * -1
        self.rect.x += self.vel * self.direction
        self.c = self.c + 1

    def update(self):
        if not self.game._isMap:
            if self.name == "vertical":
                self.vertical_move()
            if self.name == "horizontal":
                self.horizontal_move()
    

class pol(pygame.sprite.Sprite):
    def __init__(self,game):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.platformer_ui
        pygame.sprite.Sprite.__init__(self,self.groups)

        
        self.font = pygame.font.Font(None, 32)

        self.x = 50
        self.y = 200

        
    def update(self):
        if not self.game._isMap:
            x,y = pygame.mouse.get_pos()
            self.image = pygame.Surface([100, 100])
            self.text = self.font.render(f"{x},{y}", True, (255, 255, 255))
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (50,10)
            
            self.image.blit(self.text,self.text_rect)
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y


class Item(pygame.sprite.Sprite):
    def __init__(self,game,name,x,y):
        super().__init__()
        self.game = game
        self.groups = self.game.platformer_objects,self.game.platformer_solid,self.game.platformer_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        item_data = load_json("scripts/platformer_scene/json/рlatformer_items_info.json")[name]
        self.name = name
        self.image = pygame.Surface((20, 20))
        self.image.fill((item_data[0][0],item_data[0][1],item_data[0][2]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    
    


