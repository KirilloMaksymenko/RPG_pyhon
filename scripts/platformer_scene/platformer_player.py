import pygame
from pytmx.util_pygame import load_pygame
import pyscroll
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
        self.lvl = LevelCreate(game,self.glb_var)
        PlayerUI(game)
        Player(game)

       
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        self._layer = TILE_LAYER
        pygame.sprite.Sprite.__init__(self,groups)
        
        self.image = surf
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(topleft=pos)
        self.name = ""
        
class LevelCreate:
    def __init__(self,game,glb):
        self.game = game
        # self.level_obj = load_json("scripts/platformer_scene/json/platformer_levels.json")
        # Platform(game,WIN_WIDTH,"",0,WIN_HEIGHT-10)
        # Platform(game,50,"horizontal",100,500)
        # Platform(game,50,"vertical",700,500)

        # Item(game,"key_yellow",500,500)

        self.tmx_data = load_pygame("source/tmx/maper.tmx")
        
        
        
    def draw_map(self):
        lvl = load_json('scripts/player_data.json')
        
        for layer in self.tmx_data.visible_layers:
            if layer.name in ("block","bg","spawn","map_"+str(lvl['quests']["level_id"])):
               #print("layer"+layer.name)
                if layer.name in ("block","map_"+str(lvl['quests']["level_id"])):
                    group = (self.game.platformer_solid,self.game.platformer_sprites)
                else: 
                    group=self.game.platformer_sprites

                if hasattr(layer,'data'):              
                    for x,y,surf in layer.tiles():
                        pos = (x*46,y*46)
                        Tile(pos=pos,surf=surf,groups=group)

        
        for obj in self.tmx_data.objects:
            #print("obj"+str(lvl['quests']["level_id"]))
            #print(obj.name)
            if obj.name in ("items_spot","spawn","comp") or "obj"+str(lvl['quests']["level_id"]) in obj.name:
                
                #print(obj,obj.name,obj.type)
                pos = obj.x+8,obj.y+10
                #print(str(lvl['quests']['level_id']))
               #print(obj.name.replace(f" obj{str(lvl['quests']['level_id'])}",""))
                item_id = []
                for i in range(4):
                        if lvl["inventory"]["slots"][str(i+1)] != []:
                            item_id.append(lvl["inventory"]["slots"][str(i+1)][2])

                if obj.type == "item":
                   #print("ITEM")
                    if obj.id not in item_id:
                        Item(self.game,obj.image,obj.name.replace(" obj"+str(lvl['quests']["level_id"]),""),obj.x+8,obj.y+10,obj.id)
                       #print(obj.name.replace(" obj"+str(lvl['quests']["level_id"]),""))
                if obj.type =="platform":
                    Platform(self.game,obj.image,obj.name.replace(" obj"+str(lvl['quests']["level_id"]),""),obj.x+8,obj.y+10)
                   #print("platform")
                if obj.type == "dec":
                    Tile(pos=pos,surf=obj.image,groups=(self.game.platformer_sprites))
                if obj.type == "point":
                    Tile(pos=pos,surf=obj.image,groups=(self.game.platformer_point,self.game.platformer_sprites))


            # if obj.image:
            #     Tile(pos=pos,surf=obj.image,groups=self.game.platformer_sprites)

            

class GlobalVaribles:
    def __init__(self):
        self.x_change = 0
        self.y_change = 0
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        super().__init__() 
        self._layer = PLAYER_LAYER
        self.groups = self.game.platformer_player,self.game.platformer_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        #self.image = pygame.image.load("character.png")
        self.image = pygame.Surface((30, 30))
        self.image.fill((128,255,40))
        self.rect = self.image.get_rect()

        self.data = load_json("scripts\player_data.json")
        
        self.items = load_json("scripts\platformer_scene\json\рlatformer_items_info.json")

        self.vec = pygame.math.Vector2 
   
        self.pos = self.vec(self.data["spawn_pos"])
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
                Item(self.game,self.game.platformer.lvl.tmx_data.get_object_by_id(player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])][2]).image,player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])][0],self.rect.x,self.rect.y,player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])][2])
                player_data["inventory"]["slots"][str(player_data["inventory"]["sellected"])] = []
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
                            player_data["inventory"]["slots"][s] = [spr.name,self.items[spr.name],spr.id]
                            write_json("scripts/player_data.json",player_data)
                            spr.kill()
                            break

        hits = pygame.sprite.spritecollide(self,self.game.platformer_point,False)
        if hits:
            for spr in hits:
                if pygame.key.get_pressed()[pygame.K_e]:
                    player_data = load_json("scripts/player_data.json")
                    player_data["scene"] = "map"
                    write_json("scripts/player_data.json",player_data)



              

    def update(self):
        if not self.game._isMap:
            self.key_checker()
            self.gravity()
            self.move()
            self.collide_item()
 
 

 
