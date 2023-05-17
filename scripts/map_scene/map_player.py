import pygame
from time import sleep

from map_scene.map_sprite import *
from map_scene.map_config import *
from map_scene.map_functions import *


class MapSceneSetup:
    def __init__(self,game):
        self.glb_var = GlobalVaribles()
        
        self.p = Player(game,self.glb_var)
        self.m = Map(game,self.glb_var)
        
        
        self.generate_npc(game,self.glb_var)
      
    def generate_npc(self,game,glb_var):
        self.data_npc = load_json("scripts\map_scene\json\data_npc.json")["info"]
        for k in self.data_npc:
            NpcPersonage(game,k,glb_var)

class GlobalVaribles:
    def __init__(self):
        self.p_x = 0
        self.p_y = 0
        self.change_x = 0
        self.change_y = 0
        self.scale = 0
        self._isDialog = False
        self.point = 1

class DialogeSys(pygame.sprite.Sprite):
    def __init__(self,game,name_npc,glb_var):
        self.data_npc = load_json("scripts\map_scene\json\data_npc.json")
        self.data_pers = load_json("scripts/player_data.json")
        self.game = game
        self._layer = UI_LAYER
        self.groups = self.game.map_ui
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.image = pygame.Surface([WIN_WIDTH, WIN_HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0 #WIN_HEIGHT - WIN_HEIGHT//3

        
        self.font = pygame.font.Font(None, 32)

        #Checker mission state quest complited
        self.name_npc = name_npc
        self.glb_var = glb_var

        self.mission = self.data_npc["info"][self.name_npc]["missions"]["dialogs"]["mission_"+str(self.data_npc["info"][self.name_npc]["missions"]["num"])]
 
        self.state = self.mission["state_num"]
        player_data = load_json("scripts/player_data.json")
        if self.state == 0:
            pass
        elif self.mission["levels"]["state_"+str(self.state)]["type"]=="pltf":
            player_data["scene"] = "platformer"
        

        self.count_txt = 0

        self.visualize()

    def update(self):
        self.game.draw()
        if self.game._isMap:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                #print(self.count_txt)
    
                if self.count_txt == len(self.mission["state_"+str(self.state)]):
                    #print("KILL")
                    try:

                        
                        player_data = load_json("scripts/player_data.json")
                        
                        player_data["quests"]["name_npc"] = self.name_npc
                        player_data["quests"]["id"] = self.mission["levels"]["state_"+str(self.state)]["id"]
                        player_data["quests"]["point_start"] = self.mission["levels"]["state_"+str(self.state)]["point_st"]
                        player_data["quests"]["level_id"] = self.mission["levels"]["state_"+str(self.state)]["level_id"]
                        write_json("scripts/player_data.json",player_data)
                        if self.mission["levels"]["state_"+str(self.state)]["type"]=="pltf":
                            
                            player_data["scene"] = "platformer"
                            self.game.platformer.lvl.draw_map()
                        write_json("scripts/player_data.json",player_data)

                        self.kill()

                        

                        

                    except Exception as e:
                        print(e)
                else:
                    self.visualize()
                    self.count_txt += 1
                    sleep(0.2)

            
        
            
    def visualize(self):
        self.game.draw()
        self.image = pygame.Surface([WIN_WIDTH, WIN_HEIGHT])
        #pygame.draw.rect(self.image,BROWN,pygame.Rect(0,WIN_HEIGHT - WIN_HEIGHT//3,WIN_WIDTH, WIN_HEIGHT))
        #print(self.mission["state_"+str(self.state)][self.count_txt][1])
        self.personage = self.game.avatar_npc["main"].halo_sprite(0,0,WIN_WIDTH, WIN_HEIGHT,0.7)
        self.pers_rect = self.personage.get_rect()
        self.pers_rect.x = 0
        self.pers_rect.y = 270

        self.npc = self.game.avatar_npc[self.name_npc].halo_sprite(0,0,WIN_WIDTH, WIN_HEIGHT,0.7)
        self.npc_rect = self.npc.get_rect()
        self.npc_rect.x = 950
        self.npc_rect.y = 190

        self.backgraund_img = self.game.bg_map[self.data_npc["info"][self.name_npc]["point"]].get_sprite(0,0,WIN_WIDTH, WIN_HEIGHT,1.35)
        self.image.blit(self.backgraund_img,self.backgraund_img.get_rect())
        #self.text = self.font.render(, True, (255, 255, 255))
        #self.text_rect = self.text_surface.get_rect()
        
        if self.mission["state_"+str(self.state)][self.count_txt][1] == "player":
            #Player img
            self.dlg_pers = self.game.avatar_npc["dlg_pn_1"].get_sprite(0,0,WIN_WIDTH, WIN_HEIGHT,2)
            self.dlg_pers_rect = self.dlg_pers.get_rect()
            self.dlg_pers_rect.x = 100
            self.dlg_pers_rect.y = 10
            self.image.blit(self.dlg_pers,self.dlg_pers_rect)
            self.text_rect_x = 200
            self.text_rect_y = 80
            max_line_width = 200
            
            #pygame.draw.rect(self.image,(0,255,0),pygame.Rect(100,400,100,200))
            
        else:
            #any persone img
            self.dlg_npc = self.game.avatar_npc["dlg_pn_2"].get_sprite(0,0,WIN_WIDTH, WIN_HEIGHT,2)
            self.dlg_npc_rect = self.dlg_npc.get_rect()
            self.dlg_npc_rect.x = 650
            self.dlg_npc_rect.y = 10
            self.image.blit(self.dlg_npc,self.dlg_npc_rect)
            self.text_rect_x = 780
            self.text_rect_y = 80
            max_line_width = 300

            #pygame.draw.rect(self.image,(0,0,255),pygame.Rect(1000,400,100,200))
           
        text = self.mission["state_"+str(self.state)][self.count_txt][0]      

        words = text.split()
        lines = []

        current_line = ''
        for word in words:
            if self.font.size(current_line + word)[0] <= max_line_width:
                current_line += word + ' '
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)

        text_surfaces = []
        y = 0
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_surfaces.append(text_surface)
            y += text_surface.get_height()
        
        r = 0
        for text_surface in text_surfaces:
            
            self.image.blit(text_surface, (self.text_rect_x,self.text_rect_y+r))
            r += text_surface.get_height()
        #self.image.fill(WHITE)
        
        self.image.blit(self.npc,self.npc_rect)
        self.image.blit(self.personage,self.pers_rect)
        
        #self.image.blit(self.text_surface,self.text_rect)
        

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
        pygame.draw.circle(self.image,BLUE,(8,8),8)
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

        self.glb_var.scale = 0.2
        
        self.draw_map()

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.glb_var.change_x += (WIN_WIDTH -self.image.get_width())//2
        self.rect.x += (WIN_WIDTH -self.image.get_width())//2

        

    def draw_map(self):
        #self.image = pygame.Surface([MAP_WIDTH*self.glb_var.scale, MAP_HEIGHT*self.glb_var.scale])
        self.image = self.game.map_spritesheet.get_map_sprite(0,0,3424,2744,self.glb_var.scale)
        # pygame.draw.circle(self.image,RED,(0,0),10)
        #print(self.glb_var.scale)
        data = load_json("scripts\map_scene\json\map_seed.json")
        # for k in data["positions"]:
        #     for i in data["positions"][k][0]:
        #         pygame.draw.line(self.image,RED,(data["positions"][k][1][0]* self.glb_var.scale,data["positions"][k][1][1]* self.glb_var.scale),(data["positions"][i][1][0]* self.glb_var.scale,data["positions"][i][1][1]* self.glb_var.scale),3+int(self.glb_var.scale))
        
        for k in data["positions"]:
            pygame.draw.circle(self.image,WHITE,(data["positions"][k][1][0]* self.glb_var.scale,data["positions"][k][1][1]* self.glb_var.scale),7+int(self.glb_var.scale))

        p = load_json('scripts/player_data.json')["quests"]["point_start"]     
        
    def draw_marker(self):
        data = load_json("scripts\map_scene\json\map_seed.json")
        p = load_json('scripts/player_data.json')["quests"]["point_start"]  
        if p !="":
            
            pygame.draw.circle(self.image,RED,(data["positions"][p][1][0]* self.glb_var.scale,data["positions"][p][1][1]* self.glb_var.scale),10+int(self.glb_var.scale))

    
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
        #print(270*self.glb_var.scale) 

class Player(pygame.sprite.Sprite):
    def __init__(self,game,glb_var):
        
        self.glb_var = glb_var
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.map_sprites,self.game.map_player
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.data = load_json("scripts\map_scene\json\map_seed.json")
        self.data_npc = load_json("scripts/map_scene/json/data_npc.json")
        self.data_pers = load_json("scripts/player_data.json")

        self.point = str(self.data_pers["point"])
        

        self.x = self.data["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_x - 8 
        self.y = self.data["positions"][self.point][1][0]* self.glb_var.scale+self.glb_var.change_y - 8 

        self.glb_var.p_x = self.x
        self.glb_var.p_x = self.y

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
        n = 5
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
            #print(path)
            for p in path[1]:
                if path[1].index(p) == len(path[1]) - 1: 
                    break
                self.move_pic(self.data["positions"][path[1][path[1].index(p)]][1],self.data["positions"][path[1][path[1].index(p)+1]][1])

            self.point = press_point
            data_pers = load_json("scripts/player_data.json")
            data_pers["point"] = self.point
            write_json("scripts/player_data.json",data_pers)
    
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
        if self.glb_var._isDialog == True and self.point != self.last_pos:
            self.glb_var._isDialog = False

        if key[pygame.K_SPACE] and self.point in self.data_npc["pos"] and self.glb_var._isDialog == False:
            DialogeSys(self.game,self.data_npc["pos"][self.point],self.glb_var)
            self.glb_var._isDialog = True
            self.last_pos = self.point

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


