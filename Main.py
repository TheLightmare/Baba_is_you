"""

Created on Wed Feb  5 08:26:01 2020

@author: m.kowalski m.morgenthaler a.billaud

"""



import pygame as pg

from os import path

import sys

from settings import *

from sprites import *

from tilemap import *





class Game() :



  def __init__(self) :

    self.screen = pg.display.set_mode((WIDTH, HEIGHT))

    pg.key.set_repeat(500, 100)

    self.load_data()

    self.wall_collision = 1

  

  def load_data(self):

    game_folder = path.dirname(__file__)

    img_folder = path.join(game_folder, "sprites")

    self.map = Map(path.join(game_folder, 'map.txt'))

    self.baba_img = pg.image.load(path.join(img_folder, BABA_IMG)).convert_alpha()

    self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()

    self.flag_img = pg.image.load(path.join(img_folder, FLAG_IMG)).convert_alpha()

    self.box_img = pg.image.load(path.join(img_folder, BOX_IMG)).convert_alpha()

    self.key_img = pg.image.load(path.join(img_folder, KEY_IMG)).convert_alpha()

    self.rock_img = pg.image.load(path.join(img_folder, ROCK_IMG)).convert_alpha()



    self.wall_object_img = pg.image.load(path.join(img_folder, WALL_OBJECT_IMG)).convert_alpha()

    self.is_object_img = pg.image.load(path.join(img_folder, IS_OBJECT_IMG)).convert_alpha()

    self.push_object_img = pg.image.load(path.join(img_folder, PUSH_OBJECT_IMG)).convert_alpha()

    self.box_object_img = pg.image.load(path.join(img_folder, BOX_OBJECT_IMG)).convert_alpha()

    self.key_object_img = pg.image.load(path.join(img_folder, KEY_OBJECT_IMG)).convert_alpha()

    self.rock_object_img = pg.image.load(path.join(img_folder, ROCK_OBJECT_IMG)).convert_alpha()
    
    self.you_object_img = pg.image.load(path.join(img_folder, YOU_OBJECT_IMG)).convert_alpha()
    
    self.baba_object_img = pg.image.load(path.join(img_folder, BABA_OBJECT_IMG)).convert_alpha()

    

  def new(self) :
    self.bruh = pg.sprite.Group()
    self.all_sprites = pg.sprite.Group()

    self.objects = pg.sprite.Group()

    self.objects_is = pg.sprite.Group()

    self.objects_names = pg.sprite.Group()

    self.objects_atributes = pg.sprite.Group()

    self.walls = pg.sprite.Group()

    self.babas = pg.sprite.Group()


    self.player_group = pg.sprite.Group()

    for row, tiles in enumerate(self.map.data):

        for col, tile in enumerate(tiles):

          if tile == 'w':

            Wall(self, col*TILESIZE, row*TILESIZE)

          if tile == 'W':

            Wall_object(self, col*TILESIZE, row*TILESIZE)

          if tile == 'I':

            Is_object(self, col*TILESIZE, row*TILESIZE)

          if tile == 'P':

            Push_object(self, col*TILESIZE, row*TILESIZE)

          if tile == 'f':

            Flag(self, col*TILESIZE, row*TILESIZE)

          if tile == 'b':

            Baba(self, col*TILESIZE, row*TILESIZE)
            
          if tile == 'Y':

            You_object(self, col*TILESIZE, row*TILESIZE)
            
          if tile == 'B':

            Baba_object(self, col*TILESIZE, row*TILESIZE)


    self.player = Player(self, col*TILESIZE, row*TILESIZE)
    self.scan_map()

  def run(self) :

    self.playing = True

    while self.playing :

      self.events()

      self.update()

      self.draw()
      
      self.scan_map()
      



  def update(self):

    # update portion of the game loop

    self.all_sprites.update()



   

  def quit(self) :

    pg.quit()

    sys.exit()



  def scan_map(self) :
    self.player_group = self.bruh
    
    for obj in self.all_sprites :
        obj.collision_type = 0

    for is_obj in self.objects_is :

      for names_obj in self.objects_names :

        for atributes_obj in self.objects_atributes :
          is_obj.collision_type = 'p'
          atributes_obj.collision_type = 'p'
          names_obj.collision_type = 'p'

          if ((is_obj.x - TILESIZE == names_obj.x and is_obj.x + TILESIZE == atributes_obj.x) or (is_obj.x + TILESIZE == names_obj.x and is_obj.x - TILESIZE == atributes_obj.x)) and (is_obj.y == names_obj.y and is_obj.y == atributes_obj.y) or ((is_obj.y - TILESIZE == names_obj.y and is_obj.y + TILESIZE == atributes_obj.y) or (is_obj.y + TILESIZE == names_obj.y and is_obj.y - TILESIZE == atributes_obj.y)) and (is_obj.x == names_obj.x and is_obj.x == atributes_obj.x):
       
            if type(atributes_obj) == Push_object :
                
                if type(names_obj) == Wall_object :
                  for obj in self.walls :
                    obj.collision_type = 'p'
                    
                if type(names_obj) == Wall_object :
                  for obj in self.babas :
                    obj.collision_type = 'p'
                    
                    
            if type(atributes_obj) == Stop_object :
                
                if type(names_obj) == Wall_object :
                  for obj in self.walls :
                    obj.collision_type = 's'
                    
                if type(names_obj) == Wall_object :
                  for obj in self.babas :
                    obj.collision_type = 's'
                    
            if type(atributes_obj) == You_object :

                if type(names_obj) == Baba_object :
                  self.player_group = self.babas

                if type(names_obj) == Wall_object :
                  self.player_group = self.walls
    
    for obj in self.player_group : 
      obj.collision_type = 'player'
                  
                
                

                

  

  def events(self):

    # catch all events here

    for event in pg.event.get():

      if event.type == pg.QUIT:

        self.quit()

      if event.type == pg.KEYDOWN:

        if event.key == pg.K_ESCAPE:

          self.quit()

        if event.key == pg.K_LEFT :

          for i in range (0,TILESIZE):

            self.player.move(dx=-1)

            self.update()

            self.draw()

        if event.key == pg.K_RIGHT :

          for i in range (0,TILESIZE):

            self.player.move(dx=1)

            self.update()

            self.draw()

        if event.key == pg.K_UP :

          for i in range (0,TILESIZE):

            self.player.move(dy=-1)

            self.update()

            self.draw()

        if event.key == pg.K_DOWN :

          for i in range (0,TILESIZE):

            self.player.move(dy=1)

            self.update()

            self.draw()



  def draw(self):

    self.screen.fill(BGCOLOR)

    self.all_sprites.draw(self.screen)

    pg.display.flip()



  def show_start_screen(self):

    pass

            

game = Game()



game.show_start_screen()

game.new()

game.run()