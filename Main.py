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

    self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()

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

    self.all_sprites = pg.sprite.Group()

    self.objects = pg.sprite.Group()

    self.objects_is = pg.sprite.Group()

    self.objects_names = pg.sprite.Group()

    self.objects_atributes = pg.sprite.Group()

    self.walls = pg.sprite.Group()

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

          if tile == 'p':

            self.player = Player(self, col*TILESIZE, row*TILESIZE)
            
          if tile == 'Y':

            You_object(self, col*TILESIZE, row*TILESIZE)
            
          if tile == 'B':

            Baba_object(self, col*TILESIZE, row*TILESIZE)


  

  def run(self) :

    self.playing = True

    while self.playing :

      self.events()

      self.update()

      self.draw()



  def update(self):

    # update portion of the game loop

    self.all_sprites.update()

    self.scan_map()

   

  def quit(self) :

    pg.quit()

    sys.exit()



  def scan_map(self) :

    for is_obj in self.objects_is :

      for names_obj in self.objects_names :

        for atributes_obj in self.objects_atributes :

          if ((is_obj.x - TILESIZE == names_obj.x and is_obj.x + TILESIZE == atributes_obj.x) or (is_obj.x + TILESIZE == names_obj.x and is_obj.x - TILESIZE == atributes_obj.x)) and (is_obj.y == names_obj.y and is_obj.y == atributes_obj.y) or ((is_obj.y - TILESIZE == names_obj.y and is_obj.y + TILESIZE == atributes_obj.y) or (is_obj.y + TILESIZE == names_obj.y and is_obj.y - TILESIZE == atributes_obj.y)) and (is_obj.x == names_obj.x and is_obj.x == atributes_obj.x):

            if type(names_obj) == Wall_object and type(atributes_obj) == Push_object :

                self.wall_collision = 2

  

  def events(self):

    # catch all events here

    for event in pg.event.get():

      if event.type == pg.QUIT:

        self.quit()

      if event.type == pg.KEYDOWN:

        if event.key == pg.K_ESCAPE:

          self.quit()

        if event.key == pg.K_LEFT and self.player.x>0:

          for i in range (0,TILESIZE):

            self.player.move(dx=-1)

            self.update()

            self.draw()

        if event.key == pg.K_RIGHT and self.player.x<WIDTH-TILESIZE:

          for i in range (0,TILESIZE):

            self.player.move(dx=1)

            self.update()

            self.draw()

        if event.key == pg.K_UP and self.player.y>0:

          for i in range (0,TILESIZE):

            self.player.move(dy=-1)

            self.update()

            self.draw()

        if event.key == pg.K_DOWN and self.player.y<HEIGHT-TILESIZE:

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
