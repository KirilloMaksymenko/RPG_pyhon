import pygame
from time import sleep

from platformer_scene.platformer_function import *
from platformer_scene.platformer_config import *
from platformer_scene.platformer_sprite import *


class PlayerUI:
    def __init__(self,game):
        PlayerInventory(game)
        #PlayerStats(game)
        print("UI")

class PlayerStats(pygame.sprite.Sprite):
    def __init__(self,game):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.platformer_ui
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.font = pygame.font.Font(None, 32)

        self.x = 0
        self.y = 0
    def draw_stat(self):
        self.image = pygame.Surface([300, 300])
        data = load_json("scripts\player_data.json")

        pygame.draw.circle(self.image,WHITE,(50,50),50)
        
        pygame.draw.rect(self.image, RED,pygame.Rect(120,20,(data["player_stats"]["health"]/data["player_stats"]["health_max"])*150,20))
        pygame.draw.rect(self.image, GREEN,pygame.Rect(120,50,(data["player_stats"]["ex"]/data["player_stats"]["ex_max"])*150,20))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.set_colorkey(BLACK)
        
    def update(self):
        if not self.game._isMap:
            self.draw_stat()


class PlayerInventory(pygame.sprite.Sprite):
    def __init__(self,game):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.platformer_ui
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.font = pygame.font.Font(None, 32)
        
        self._isVisible = False
        self.image = pygame.Surface([210, 26])
        self.rect = self.image.get_rect

        
    def draw_inv(self):
        self.image = pygame.Surface([210, 26])
        data = load_json("scripts\player_data.json")["inventory"]
        if self._isVisible:
            for i in range(4):
                pygame.draw.rect(self.image, RED,pygame.Rect((i*50),0,26,26))
                if data["slots"][str(i+1)] != []:
                    #print(self.game.platformer.lvl.tmx_data.get_object_by_id(data["slots"][str(i+1)][2]))
                    self.image.blit(self.game.platformer.lvl.tmx_data.get_object_by_id(data["slots"][str(i+1)][2]).image,pygame.Rect((i*50)+3,0+3,20,20))
                    #pygame.draw.rect(self.image, (data["slots"][str(i+1)][1][0][0],data["slots"][str(i+1)][1][0][1],data["slots"][str(i+1)][1][0][2]),pygame.Rect((i*50)+3,0+3,20,20))#img
                pygame.draw.rect(self.image, WHITE,pygame.Rect(((data["sellected"]-1)*50),0,26,26),1)
        
        
        self.rect = self.image.get_rect()
        for sp in self.game.platformer_player:
            self.rect.x = sp.rect.x -70
            self.rect.y = sp.rect.y -50
        self.image.set_colorkey(BLACK)

    def check_open(self):
        press = pygame.key.get_pressed()
        if press[pygame.K_i]:
            self._isVisible = not self._isVisible
            sleep(0.5)

    
    

    def update(self):
        if not self.game._isMap:
            self.draw_inv()
            self.check_open()
