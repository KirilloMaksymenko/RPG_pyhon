import pygame
from time import sleep

from map_scene.map_sprite import *
from map_scene.map_config import *
from map_scene.map_functions import *


class MapSceneSetup:
    def __init__(self,game):
        glb_var = GlobalVaribles()
        
        Map(game,glb_var)
        Player(game,glb_var)
        
        self.generate_npc(game,glb_var)
      
    def generate_npc(self,game,glb_var):
        self.data_npc = load_json("scripts\map_scene\json\data_npc.json")["info"]
        for k in self.data_npc:
            NpcPersonage(game,k,glb_var)

class GlobalVaribles:
    def __init__(self):
        self.change_x = 0
        self.change_y = 0
        self.scale = 0

class DialogeSys(pygame.sprite.Sprite):
    def __init__(self,game,name_npc):
        self.data_npc = load_json("scripts\map_scene\json\data_npc.json")
        self.game = game
        self._layer = UI_LAYER
        self.groups = self.game.map_ui
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.image = pygame.Surface([WIN_WIDTH, WIN_HEIGHT])
        self.font = pygame.font.Font(None, 32)

        #Checker mission state quest complited
        self.mission = self.data_npc["info"][name_npc]["missions"]["dialogs"]["mission_"+str(self.data_npc["info"][name_npc]["missions"]["num"])]
        self.state = self.mission["state_num"]
        self.count_txt = 0

        self.visualize()

    def update(self):
        if self.game._isMap:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.count_txt += 1
                # stop the game loop when the dialogue is finished
                #print("len _ "+str(len(self.mission["state_"+str(self.state)])))
                #print("count _ "+str(self.count_txt))
                if self.count_txt == len(self.mission["state_"+str(self.state)]):
                    #print("KILL")
                    try:
                        player_data = load_json("scripts/player_data.json")
                        player_data["spawn_pos"] = self.mission["levels"]["state_"+str(self.state)]
                        player_data["scene"] = "platformer"
                        write_json("scripts/player_data.json",player_data)

                    except:
                        pass
                    self.kill()
                    sleep(0.05)
                else:
                    self.visualize()
                    sleep(0.05)
            
        
            
    def visualize(self):
        #self.image = pygame.Surface([WIN_WIDTH, WIN_HEIGHT])
        pygame.draw.rect(self.image,BROWN,pygame.Rect(0,WIN_HEIGHT - WIN_HEIGHT//3,WIN_WIDTH, WIN_HEIGHT))
        #print(self.mission["state_"+str(self.state)][self.count_txt][1])
        if self.mission["state_"+str(self.state)][self.count_txt][1] != "player":
            #Player img
            pygame.draw.rect(self.image,(0,255,0),pygame.Rect(100,400,100,200))
            
        else:
            #any persone img
            pygame.draw.rect(self.image,(0,0,255),pygame.Rect(1000,400,100,200))
           
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0 #WIN_HEIGHT - WIN_HEIGHT//3
        
        self.text = self.font.render(self.mission["state_"+str(self.state)][self.count_txt][0], True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (300, WIN_HEIGHT - WIN_HEIGHT//3 + 100)
        
        self.image.blit(self.text,self.text_rect)

    


class NpcPersonage(pygame.sprite.Sprite):
    def __init__(self,game,name,glb_var):
        self.glb_var = glb_var
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.map_sprites,self.game.map_npc
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.data_pos = load_json("scripts\map_scene\json\map_seed.json")
        self.data_npc = load_json("scripts\map_scene\json\data_npc.json")

        self.point = self.data_npc["info"][name]["point"] #load_json("/scripts/player_data.json")["point"]

        self.x = self.data_pos["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_x - 16 
        self.y = self.data_pos["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_y - 16


        self.image = pygame.Surface([16, 16])
        pygame.draw.circle(self.image,RED,(8,8),16)
        #self.game.character_spritesheet.get_sprite(16,0,self.width,self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_pos(self):
        self.rect.x = self.data_pos["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_x - 16
        self.rect.y = self.data_pos["positions"][self.point][1][1]* self.glb_var.scale+self.glb_var.change_y - 16

    def update(self):
        if self.game._isMap:
            self.set_pos()
        

class Map(pygame.sprite.Sprite):
    def __init__(self, game,glb_var):

        self.glb_var = glb_var
        self.game = game
        self._layer = MAP_LAYER
        self.groups = self.game.map_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = 0
        self.y = 0

        self.glb_var.scale = 1
        
        self.draw_map()

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_map(self):
        #self.image = pygame.Surface([MAP_WIDTH*self.glb_var.scale, MAP_HEIGHT*self.glb_var.scale])
        self.image = self.game.map_spritesheet.get_map_sprite(0,0,3424,2744,self.glb_var.scale)
        pygame.draw.circle(self.image,RED,(0,0),10)
        #print(self.glb_var.scale)
        data = load_json("scripts\map_scene\json\map_seed.json")
        # for k in data["positions"]:
        #     for i in data["positions"][k][0]:
        #         pygame.draw.line(self.image,RED,(data["positions"][k][1][0]* self.glb_var.scale,data["positions"][k][1][1]* self.glb_var.scale),(data["positions"][i][1][0]* self.glb_var.scale,data["positions"][i][1][1]* self.glb_var.scale),3+int(self.glb_var.scale))
                
        for k in data["positions"]:
            pygame.draw.circle(self.image,WHITE,(data["positions"][k][1][0]* self.glb_var.scale,data["positions"][k][1][1]* self.glb_var.scale),7+int(self.glb_var.scale))

    def update(self):
        if self.game._isMap:
            self.scale_change()

    def scale_change(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.glb_var.scale < 0.8:
            self.glb_var.scale = self.glb_var.scale + 0.1
            self.glb_var.change_x += -270*self.glb_var.scale
            self.glb_var.change_y += -270*self.glb_var.scale
            for sprite in self.game.map_sprites:
                sprite.rect.x += -270*self.glb_var.scale
                sprite.rect.y += -270*self.glb_var.scale
            self.draw_map()
            
        if keys[pygame.K_z] and self.glb_var.scale > 0.3:
            self.glb_var.scale = self.glb_var.scale - 0.1
            self.glb_var.change_x += 270*self.glb_var.scale
            self.glb_var.change_y += 270*self.glb_var.scale
            for sprite in self.game.map_sprites:
                sprite.rect.x += 270*self.glb_var.scale
                sprite.rect.y += 270*self.glb_var.scale
            self.draw_map()
        print(270*self.glb_var.scale) 

class Player(pygame.sprite.Sprite):
    def __init__(self,game,glb_var):
        
        self.glb_var = glb_var
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.map_sprites,self.game.map_player
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.data = load_json("scripts\map_scene\json\map_seed.json")
        self.data_npc = load_json("scripts\map_scene\json\data_npc.json")

        self.point = "1" #load_json("/scripts/player_data.json")["point"]

        self.x = self.data["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_x - 8 
        self.y = self.data["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_y - 8 

        self.image = pygame.Surface([16, 16])
        pygame.draw.circle(self.image,BLUE,(8,8),16)
        #self.game.character_spritesheet.get_sprite(16,0,self.width,self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move_pic(self,A,B):
        a,b,c = find_equation(A,B)
        nbpic = 50
        step = (B[0] - A[0]) / nbpic
        for i in range(nbpic):
            x = A[0] + i*step
            y = (-c-a*x)/b

            #print("x - ",x, " y - ",y)
            self.rect.x = x* self.glb_var.scale+self.glb_var.change_x - 8 
            self.rect.y = y* self.glb_var.scale+self.glb_var.change_y - 8 
            self.game.draw()
            
        
    def move_mouse(self,mouse): 
        n = 20
        if mouse[0]: #if tap to point 8
            x,y = pygame.mouse.get_pos()
            #print(x,y)
            isGet = False
            for k in self.data["positions"]:
                #print(k,"/",self.data["positions"][k][1][0]+n ,self.data["positions"][k][1][0]-n)
                if x < self.data["positions"][k][1][0]* self.glb_var.scale+self.glb_var.change_x+n and x > self.data["positions"][k][1][0]* self.glb_var.scale+self.glb_var.change_x-n and y < self.data["positions"][k][1][1]* self.glb_var.scale+self.glb_var.change_y+n and y > self.data["positions"][k][1][1]* self.glb_var.scale+self.glb_var.change_y-n:
                    press_point = k
                    #print(k," oki")
                    isGet = True
            if isGet == False:
                #print("no")
                return    
                         
            if press_point == self.point:
                return
            path = algorithme_de_Dijkstra(self.point,press_point)
            print(path)
            for p in path[1]:
                if path[1].index(p) == len(path[1]) - 1: 
                    break
                self.move_pic(self.data["positions"][path[1][path[1].index(p)]][1],self.data["positions"][path[1][path[1].index(p)+1]][1])

            self.point = press_point
    
    def scroll_mouse(self,mouse,rel):
        if mouse[2]:
            #print("left")
            #print(rel)
            
            self.ch_x = rel[0]
            self.ch_y = rel[1]
            #print(self.ch_x,self.ch_y)
            for sprite in self.game.map_sprites:
                sprite.rect.x += self.ch_x
                sprite.rect.y += self.ch_y
            self.glb_var.change_x += self.ch_x
            self.glb_var.change_y += self.ch_y
          

    def set_pos(self):
        self.rect.x = self.data["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_x - 8 
        self.rect.y = self.data["positions"][self.point][1][1]* self.glb_var.scale+self.glb_var.change_y - 8 

    def check_npc(self,key):
        if key[pygame.K_SPACE] and self.point in self.data_npc["pos"]:
            DialogeSys(self.game,self.data_npc["pos"][self.point])

    def update(self):
        if self.game._isMap:
            self.movement()

            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()
            rel = pygame.mouse.get_rel()
            self.scroll_mouse(mouse,rel)
            self.check_npc(keys)

    def movement(self):
        mouse = pygame.mouse.get_pressed()
        self.move_mouse(mouse)
        self.set_pos()


