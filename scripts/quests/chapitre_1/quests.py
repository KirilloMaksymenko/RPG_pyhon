import pygame
import time
from config import *
from main_finctions import *


class QuestSys(pygame.sprite.Sprite):
    def __init__(self,game):
        self.data_npc = load_json_m("scripts\map_scene\json\data_npc.json")
        self.data_pers = load_json_m("scripts/player_data.json")
        self.game = game
        self._layer = 0
        self.groups = self.game.map_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.image = pygame.Surface([1,1])
        self.rect = self.image.get_rect()

        self.count_doc = [False,False]
        self.doc_pos = ["",""]

        self.count_apple = [False,False,False]
        self.apple_pos = ["","",""]

        self.count_doc_fin = [False,False,False]
        self.doc_fin_pos = ["","",""]



    def update(self):
        #print(f"self.m_{load_json_m('scripts/player_data.json')['quests']['id']}")
        eval(f"self.m_{str(load_json_m('scripts/player_data.json')['quests']['id'])}()")

    def m_0(self):
        pass

    def m_1(self):
        if load_json_m("scripts/player_data.json")["point"] == "15" and load_json_m('scripts/player_data.json')['quests']["point_start"]=="15":
            d = load_json_m('scripts/player_data.json')
            d['quests']["point_start"] = ""
            write_json_m('scripts/player_data.json',d)
        else:
            self.game.map.m.draw_marker()


        try: 
            if load_json_m("scripts\map_scene\json\data_npc.json")["pos"]["15"] == "Seller":
                pass
        except: 

            d = load_json_m("scripts\map_scene\json\data_npc.json")
            d["info"]["Noname"]["missions"]["dialogs"]["mission_1"]["state_num"] = 0
            write_json_m("scripts\map_scene\json\data_npc.json",d)
        

    
    def m_2(self):
        
        if load_json_m("scripts/player_data.json")["point"] == "72" and load_json_m('scripts/player_data.json')['quests']["point_start"]=="72":
            d = load_json_m('scripts/player_data.json')
            d['quests']["point_start"] = ""
            write_json_m('scripts/player_data.json',d)
        else:
            self.game.map.m.draw_marker()
        
       
        a = load_json_m("scripts\player_data.json")["inventory"]["slots"]
        if load_json_m("scripts\map_scene\json\data_npc.json")["info"]["Seller"]["missions"]["dialogs"]["mission_1"]["state_num"] == 1:
            for i in a:
                if "doc" in a[str(i)]:
                    if a[str(i)][2] == 6:
                        d=load_json_m("scripts\player_data.json")
                        d["inventory"]["slots"][str(i)] = []
                        write_json_m("scripts\player_data.json",d)
                        d = load_json_m("scripts\map_scene\json\data_npc.json")
                        d["info"]["Seller"]["missions"]["dialogs"]["mission_1"]["state_num"] = 2
                        write_json_m("scripts\map_scene\json\data_npc.json",d)

    def m_3(self):
        if load_json_m("scripts/player_data.json")["point"] == "26" and load_json_m('scripts/player_data.json')['quests']["point_start"]=="26":
            d = load_json_m('scripts/player_data.json')
            d['quests']["point_start"] = ""
            write_json_m('scripts/player_data.json',d)
        else:
            self.game.map.m.draw_marker()


        #print("3______",self.count_doc)
        a = load_json_m("scripts\player_data.json")["inventory"]["slots"]
        
        if load_json_m("scripts\map_scene\json\data_npc.json")["info"]["Dr.Miller"]["missions"]["dialogs"]["mission_1"]["state_num"] == 1:
            for i in a:
                if "doc" in a[str(i)]:
                    #print(i,a[str(i)][2])

                    if a[str(i)][2] == 28:
                        #print("28 True")
                        self.count_doc[0] = True
                        self.doc_pos[0] = str(i)
                        continue
                    elif a[str(i)][2] == 27:
                        #print("27 True")
                        self.count_doc[1] = True
                        self.doc_pos[1] = str(i)
                        continue
                    else:
                        if self.count_doc[0] == True:
                            #print("28 False")
                            self.count_doc[0] = False
                            self.doc_pos[0] = ""
                        if self.count_doc[1] == True:
                            #print("27 False")
                            self.count_doc[1] = False
                            self.doc_pos[1] = ""
                        
            if self.count_doc == [True,True]:
                d=load_json_m("scripts\player_data.json")
                for i in range(2):
                    d["inventory"]["slots"][str(self.doc_pos[i])] = []
                write_json_m("scripts\player_data.json",d)
                d = load_json_m("scripts\map_scene\json\data_npc.json")
                d["info"]["Dr.Miller"]["missions"]["dialogs"]["mission_1"]["state_num"] = 2
                write_json_m("scripts\map_scene\json\data_npc.json",d)

            

    def m_4(self):
        if load_json_m("scripts/player_data.json")["point"] == "45" and load_json_m('scripts/player_data.json')['quests']["point_start"]=="45":
            d = load_json_m('scripts/player_data.json')
            d['quests']["point_start"] = ""
            write_json_m('scripts/player_data.json',d)
        else:
            self.game.map.m.draw_marker()

        a = load_json_m("scripts\player_data.json")["inventory"]["slots"]
        #print(self.count_apple)
        if load_json_m("scripts\map_scene\json\data_npc.json")["info"]["Zina"]["missions"]["dialogs"]["mission_1"]["state_num"] == 1:
            for i in a:
                if "apple" in a[str(i)]:
                    #print(i,a[str(i)][2])
                    if a[str(i)][2] == 35:
                        self.count_apple[0] = True
                        self.apple_pos[0] = str(i)
                        continue
                    elif a[str(i)][2] == 33:
                        self.count_apple[1] = True
                        self.apple_pos[1] = str(i)
                        continue
                    elif a[str(i)][2] == 32:
                        self.count_apple[2] = True
                        self.apple_pos[2] = str(i)
                        continue
                    else:
                        if self.count_apple[0] == True:
                            self.count_apple[0] = False
                            self.apple_pos[0] = ""
                        if self.count_apple[1] == True:
                            self.count_apple[1] = False
                            self.apple_pos[1] = ""
                        if self.count_apple[2] == True:
                            self.count_apple[2] = False
                            self.apple_pos[2] = ""

                        
            if self.count_apple == [True,True,True]:
                d=load_json_m("scripts\player_data.json")
                for i in range(3):
                    d["inventory"]["slots"][str(self.apple_pos[i])] = []
                write_json_m("scripts\player_data.json",d)
                d = load_json_m("scripts\map_scene\json\data_npc.json")
                d["info"]["Zina"]["missions"]["dialogs"]["mission_1"]["state_num"] = 2
                write_json_m("scripts\map_scene\json\data_npc.json",d)

    def m_5(self):
        if load_json_m("scripts/player_data.json")["point"] == "59" and load_json_m('scripts/player_data.json')['quests']["point_start"]=="59":
            d = load_json_m('scripts/player_data.json')
            d['quests']["point_start"] = ""
            write_json_m('scripts/player_data.json',d)
        else:
            self.game.map.m.draw_marker()


        a = load_json_m("scripts\player_data.json")["inventory"]["slots"]
        #print("##### ",load_json_m("scripts\map_scene\json\data_npc.json")["info"]["Vasya"]["missions"]["dialogs"]["mission_1"]["state_num"])
        
        if load_json_m("scripts\map_scene\json\data_npc.json")["info"]["Vasya"]["missions"]["dialogs"]["mission_1"]["state_num"] == 1: 
             for i in a:
                if "doc" in a[str(i)]:
                    if a[str(i)][2] == 40:
                        player_data = load_json_m("scripts/player_data.json")
                        for s in player_data["inventory"]["slots"]:
                            if player_data["inventory"]["slots"][s] == []:
                                player_data["inventory"]["slots"][s] = ["doc",[[255, 255, 0], "other"], 41]
                                write_json_m("scripts/player_data.json",player_data)
                                d = load_json_m("scripts\map_scene\json\data_npc.json")
                                d["info"]["Vasya"]["missions"]["dialogs"]["mission_1"]["state_num"] = 2
                                write_json_m("scripts\map_scene\json\data_npc.json",d)

        if load_json_m("scripts\map_scene\json\data_npc.json")["info"]["Vasya"]["missions"]["dialogs"]["mission_1"]["state_num"] == 1:
            #print("@@@ ",load_json_m("scripts/player_data.json")["scene"] == "platformer")
                
            for i in a:
                if "doc" in a[str(i)]:
                    #print(i,a[str(i)][2])
                    if a[str(i)][2] == 34:
                        self.count_doc_fin[0] = True
                        self.doc_fin_pos[0] = str(i)
                        continue
                    elif a[str(i)][2] == 40:
                        self.count_doc_fin[1] = True
                        self.doc_fin_pos[1] = str(i)
                        continue
                    elif a[str(i)][2] == 41:
                        self.count_doc_fin[2] = True
                        self.doc_fin_pos[2] = str(i)
                        continue
                    else:
                        if self.count_doc_fin[0] == True:
                            self.count_doc_fin[0] = False
                            self.doc_fin_pos[0] = ""
                        if self.count_doc_fin[1] == True:
                            self.count_doc_fin[1] = False
                            self.doc_fin_pos[1] = ""
                        if self.count_doc_fin[2] == True:
                            self.count_doc_fin[2] = False
                            self.doc_fin_pos[2] = ""

            if self.count_doc_fin == [True,True,True]:
                d = load_json_m("scripts\map_scene\json\data_npc.json")
                d["info"]["Vasya"]["missions"]["dialogs"]["mission_1"]["state_num"] = 3
                write_json_m("scripts\map_scene\json\data_npc.json",d)


    def m_6(self):
        pass

    def m_7(self):
        if load_json_m("scripts\map_scene\json\data_npc.json")["info"]["robot"]["missions"]["dialogs"]["mission_1"]["state_num"] == 1:
            pygame.draw.rect(self.image, WHITE,pygame.Rect(0,0,WIN_WIDTH,WIN_HEIGHT))
            print("COMING SOON")
            
            
