import pygame
from time import sleep

from platformer_scene.platformer_function import *
from platformer_scene.platformer_config import *
from platformer_scene.platformer_sprite import *
from platformer_scene.platformer_objects import *
from platformer_scene.platformer_interface import *


class PlatformerSceneSetup:
    def __init__(self,game):
        self.game = game
        self.glb_var = GlobalVaribles()
        LevelCreate(game,self.glb_var)
        PlayerUI(game)
        Player(game)

       
        
class LevelCreate:
    def __init__(self,game,glb):
        
        self.level_obj = load_json("scripts/platformer_scene/json/platformer_levels.json")
        Platform(game,WIN_WIDTH,"",0,WIN_HEIGHT-10)
        Platform(game,50,"horizontal",100,500)
        Platform(game,50,"vertical",700,500)

        Item(game,"key_yellow",500,500)
        
        

class GlobalVaribles:
    def __init__(self):
        self.x_change = 0
        self.y_change = 0
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        super().__init__() 
        self.groups = self.game.platformer_player,self.game.platformer_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        #self.image = pygame.image.load("character.png")
        self.image = pygame.Surface((30, 30))
        self.image.fill((128,255,40))
        self.rect = self.image.get_rect()

        self.data = load_json("scripts\player_data.json")
        self.items = load_json("scripts\platformer_scene\json\рlatformer_items_info.json")

        self.vec = pygame.math.Vector2 
   
        self.pos = self.vec((10, 360))
        self.vel = self.vec(0,0)
        self.acc = self.vec(0,0)
 
    def move(self):
        self.acc = self.vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
                 
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
             
        self.rect.midbottom = self.pos
        
 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, self.game.platformer_solid, False)
        if hits:
           self.vel.y = -15
    
    def key_checker(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            
            self.jump()

        if key[pygame.K_q]:
            player_data = load_json("scripts/player_data.json")
            if player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])] != []:
                Item(self.game,player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])][0],self.rect.x,self.rect.y)
                player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])] = []
                write_json("scripts/player_data.json",player_data)

        if key[pygame.K_m]:
            player_data = load_json("scripts/player_data.json")
            player_data["scene"] = "map"
            write_json("scripts/player_data.json",player_data)
      
        if key[pygame.K_1]:
            player_data = load_json("scripts/player_data.json")
            player_data["inventory"]["sellected"] = 1
            write_json("scripts/player_data.json",player_data)
        if key[pygame.K_2]:
            player_data = load_json("scripts/player_data.json")
            player_data["inventory"]["sellected"] = 2
            write_json("scripts/player_data.json",player_data)
        if key[pygame.K_3]:
            player_data = load_json("scripts/player_data.json")
            player_data["inventory"]["sellected"] = 3
            write_json("scripts/player_data.json",player_data)
        if key[pygame.K_4]:
            player_data = load_json("scripts/player_data.json")
            player_data["inventory"]["sellected"] = 4
            write_json("scripts/player_data.json",player_data)
    
    def gravity(self):

        hits = pygame.sprite.spritecollide(self ,self.game.platformer_solid, False)
        if self.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
        if hits:
            if hits[0].name == "horizontal":
                self.pos.x += hits[0].vel*hits[0].direction

    def collide_item(self,):

        hits = pygame.sprite.spritecollide(self,self.game.platformer_objects,False)
        if hits:
            
            for spr in hits:
                if pygame.key.get_pressed()[pygame.K_e]:
                    player_data = load_json("scripts/player_data.json")
                    for s in player_data["inventory"]["slots"]:
                        if player_data["inventory"]["slots"][s] == []:
                            player_data["inventory"]["slots"][s] = [spr.name,self.items[spr.name]]
                            write_json("scripts/player_data.json",player_data)
                            spr.kill()
                            break



              

    def update(self):
        if not self.game._isMap:
            self.key_checker()
            self.gravity()
            self.move()
            self.collide_item()
 
 

 
