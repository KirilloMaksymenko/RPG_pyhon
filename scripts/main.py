#project - RPG_pyhon , Author - Maksymenko Kyrylo

import pygame
from sprite import *

from main_finctions import *

from map_scene.map_player import *
from platformer_scene.platformer_player import *
from config import *
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        
        self.player_data = load_json_m("scripts/player_data.json")
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.scene = self.player_data["scene"] #map/platformer

        
        # self.sprites_sheets()
 
    # def sprites_sheets(self):
    #     self.character_spritesheet = Spritesheet("source/anim/hero_anim.png")



    def layers_create(self):
        self.map_sprites = pygame.sprite.LayeredUpdates()
        self.map_player= pygame.sprite.LayeredUpdates()
        self.map_npc= pygame.sprite.LayeredUpdates()
        self.map_ui= pygame.sprite.LayeredUpdates()

        self.platformer_sprites = pygame.sprite.LayeredUpdates()
        self.platformer_player= pygame.sprite.LayeredUpdates()
        self.platformer_objects= pygame.sprite.LayeredUpdates()
        self.platformer_solid= pygame.sprite.LayeredUpdates()
        self.platformer_npc= pygame.sprite.LayeredUpdates()
        self.platformer_ui= pygame.sprite.LayeredUpdates()

        #self.character_spritesheet = Spritesheet("source/anim/hero_anim.png")
        self.map_spritesheet = SpritesheetMap("source/Map_V2.png")
    
    def map_layers_draw(self):
        self.map_sprites.draw(self.screen)
        self.map_ui.draw(self.screen)
    
    def platformer_layers_draw(self):
        self.platformer_sprites.draw(self.screen)
        self.platformer_ui.draw(self.screen)

    def new(self):

        self.playing = True

        self.layers_create()
     
        self.map = MapSceneSetup(self)
        self.platformer = PlatformerSceneSetup(self)

        self._isMap = True



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.player_data = load_json_m("scripts/player_data.json")
        self.scene = self.player_data["scene"]
        
        if self._isMap == True and self.scene == "platformer":
            
            self._isMap = False
            
        if self._isMap == False and self.scene == "map":
           
            self._isMap = True
            

        if self.scene == "map":
            self.map_sprites.update()
            self.map_ui.update()
        if self.scene == "platformer":
            self.platformer_sprites.update()
            self.platformer_ui.update()
        
        

    def draw(self):
        
        
        if self.scene == "map":
            self.screen.fill(WHITE)
            self.map_layers_draw()
            
        if self.scene == "platformer":
            self.screen.fill(BLACK)
            self.platformer_layers_draw()
            
        
        
        
        self.clock.tick(FPS)
        
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

        self.running = False


    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()

