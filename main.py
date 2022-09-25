#project - RPG_pyhon , Author - Maksymenko Kyrylo

import pygame
from sprite import *
from resourse import *
from config import *
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        
        
        
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.running = True

        self.character_spritesheet = Spritesheet("source/anim/hero_anim.png")
        self.block_spritesheet = Spritesheet('source/block.png')
        self.resourse_sprite_sheet = Spritesheet('source/resourses.png')
        self.terrain_spritesheet = Spritesheet('source/tile_grass.png')

    
    def scale_pos(self,n):
        return n+n*3

    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j,colum in enumerate(row):
                Ground(self,self.scale_pos(j), self.scale_pos(i))
                if colum == "B":
                    Block(self,self.scale_pos(j), self.scale_pos(i))
                if colum == "P":
                    Tree(self,self.scale_pos(j+2), self.scale_pos(i+2))
                    self.player = Player(self,self.scale_pos(j), self.scale_pos(i))
        for i in range(50):
            Tree(self,self.scale_pos(random.randint(0,50)),self.scale_pos(random.randint(0,50)))

        self.player.center_cam()

    def new(self):

        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.resourses = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        
        
        
       
        
    
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
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

