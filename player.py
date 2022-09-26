import pygame
from config import *
import math
from sprite import *



class Player(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
        
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = "down"
        self.animation_loop = 1

        self.collide_x = False
        self.collide_y = False
        
        self.image = self.game.character_spritesheet.get_sprite(16,0,self.width,self.height)
        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

    def center_cam(self):
        for sprite in self.game.all_sprites:
            sprite.rect.x -= self.x - WIN_WIDTH//2
            sprite.rect.y -= self.y - WIN_HEIGHT//2

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.collide_resourses("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")
        self.collide_resourses("y")

        
        if self.collide_x:
            self.x_change_cam = 0
        else:
            self.x_change_cam = self.x_change
        
        if self.collide_y:
            self.y_change_cam = 0
        else:
            self.y_change_cam = self.y_change

        for sprite in self.game.all_sprites:
            sprite.rect.x -= self.x_change_cam
            sprite.rect.y -= self.y_change_cam

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            
            self.x_change -= PLAYER_SPEED
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = "right"
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = "down"
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.facing = "down-right"
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.facing = "down-left"
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.facing = "up-right"
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.facing = "up-left"


    def collide_resourses(self,direction):
        self.collide_res_y_1 = True
        self.collide_res_y_2 = True

        if direction == "y":
            hits = pygame.sprite.spritecollide(self,self.game.resourses,False)
            if hits:
                for spr in hits:
                    if self.rect.y < spr.rect.y:
                        if self.collide_res_y_1:
                            self.collide_res_y_2 = True
                            self.collide_res_y_1 = False
                            self.game.all_sprites.change_layer(spr,PLAYER_LAYER+1)
                            print("2 layer 3")
                    else:
                        if self.collide_res_y_2:
                            self.collide_res_y_1 = True
                            self.collide_res_y_2 = False
                            self.game.all_sprites.change_layer(spr,PLAYER_LAYER-1)
                            print("layer 5")
            else:
                self.collide_res_y_1 = True
                self.collide_res_y_2 = True  

    def collide_blocks(self,direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self,self.game.blocks,False)
            if hits:
                
                self.collide_x = True
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
            else:
                self.collide_x = False
        if direction == "y":
            hits = pygame.sprite.spritecollide(self,self.game.blocks,False)
            if hits:
                
                self.collide_y = True
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
            else: 
                self.collide_y = False

    def base_attack(self):
        attack_anim = [
            self.game.base_attack_spritesheet.get_sprite(0,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(16,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(32,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(48,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(64,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(80,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(96,0,self.width,self.height),
            self.game.base_attack_spritesheet.get_sprite(112,0,self.width,self.height),
        ]
        

    def animate(self):
        up_animate = [
            self.game.character_spritesheet.get_sprite(0,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,16,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,16,self.width,self.height),]
        down_animate = [
            self.game.character_spritesheet.get_sprite(0,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,32,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,32,self.width,self.height),]
        up_left_animate = [
            self.game.character_spritesheet.get_sprite(0,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,48,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,48,self.width,self.height),]
        up_right_animate = [
            self.game.character_spritesheet.get_sprite(0,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,64,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,64,self.width,self.height),]
        down_right_animate = [
            self.game.character_spritesheet.get_sprite(0,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,80,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,80,self.width,self.height),]
        down_left_animate = [
            self.game.character_spritesheet.get_sprite(0,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,96,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,96,self.width,self.height),]
        right_animate = [
            self.game.character_spritesheet.get_sprite(0,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,112,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,112,self.width,self.height),]
        left_animate = [
            self.game.character_spritesheet.get_sprite(0,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(16,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(32,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(48,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(64,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(80,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(96,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(112,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(128,128,self.width,self.height),
            self.game.character_spritesheet.get_sprite(144,128,self.width,self.height),]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = down_animate[0]
            else:
                self.image = down_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.y_change == 0:
                self.image = up_animate[0]
            else:
                self.image = up_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:
                self.image = right_animate[0]
            else:
                self.image = right_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.x_change == 0:
                self.image = left_animate[0]
            else:
                self.image = left_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "down-right":
            if self.x_change == 0:
                self.image = down_right_animate[0]
            else:
                self.image = down_right_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "down-left":
            if self.x_change == 0:
                self.image = down_left_animate[0]
            else:
                self.image = down_left_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "up-right":
            if self.x_change == 0:
                self.image = up_right_animate[0]
            else:
                self.image = up_right_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1
        if self.facing == "up-left":
            if self.x_change == 0:
                self.image = up_left_animate[0]
            else:
                self.image = up_left_animate[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= 10:
                    self.animation_loop = 1

            