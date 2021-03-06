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

    self.flag_object_img = pg.image.load(path.join(img_folder, FLAG_OBJECT_IMG)).convert_alpha()

    self.is_object_img = pg.image.load(path.join(img_folder, IS_OBJECT_IMG)).convert_alpha()

    self.push_object_img = pg.image.load(path.join(img_folder, PUSH_OBJECT_IMG)).convert_alpha()

    self.box_object_img = pg.image.load(path.join(img_folder, BOX_OBJECT_IMG)).convert_alpha()

    self.key_object_img = pg.image.load(path.join(img_folder, KEY_OBJECT_IMG)).convert_alpha()

    self.rock_object_img = pg.image.load(path.join(img_folder, ROCK_OBJECT_IMG)).convert_alpha()
    
    self.you_object_img = pg.image.load(path.join(img_folder, YOU_OBJECT_IMG)).convert_alpha()
    
    self.baba_object_img = pg.image.load(path.join(img_folder, BABA_OBJECT_IMG)).convert_alpha()

    self.stop_object_img = pg.image.load(path.join(img_folder, STOP_OBJECT_IMG)).convert_alpha()

    self.winn_object_img = pg.image.load(path.join(img_folder, WINN_OBJECT_IMG)).convert_alpha()

    

  def new(self) :
    self.bruh = pg.sprite.Group()
    self.all_sprites = pg.sprite.Group()

    self.objects = pg.sprite.Group()

    self.objects_is = pg.sprite.Group()

    self.objects_names = pg.sprite.Group()

    self.objects_atributes = pg.sprite.Group()

    self.walls = pg.sprite.Group()
    self.babas = pg.sprite.Group()
    self.rocks = pg.sprite.Group()
    self.flags = pg.sprite.Group()


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

          if tile == 'F':

            Flag_object(self, col*TILESIZE, row*TILESIZE)

          if tile == 'b':

            Baba(self, col*TILESIZE, row*TILESIZE)
            
          if tile == 'Y':

            You_object(self, col*TILESIZE, row*TILESIZE)
            
          if tile == 'B':

            Baba_object(self, col*TILESIZE, row*TILESIZE)

          if tile == "r" :
            
            Rock(self, col*TILESIZE, row*TILESIZE)

          if tile == "R" :

            Rock_object(self, col*TILESIZE, row*TILESIZE)

          if tile == 'S' :

            Stop_object(self, col*TILESIZE, row*TILESIZE)

          if tile == '9':

            Winn_object(self, col*TILESIZE, row*TILESIZE)



    self.player = Player(self, col*TILESIZE, row*TILESIZE)
    self.scan_map()

  def run(self) :

    self.playing = True

    while self.playing :

      self.events()

      self.update()

      self.draw()
      
      self.scan_map()

      for Play in self.player_group :
        for obj in self.all_sprites :
          if Play.x == obj.x and Play.y == obj.y and obj.collision_type == 'w':
            self.playing=game_won()


      



  def update(self):

    # update portion of the game loop

    self.all_sprites.update()



   

  def quit(self) :

    pg.quit()

    sys.exit()



  def scan_map(self) :
    self.player_group = self.bruh
    self.previous_time = 1
    
    for obj in self.all_sprites :
        obj.collision_type = 0

    for is_obj in self.objects_is :

      for names_obj in self.objects_names :

        for names_obj_2 in self.objects_names :
          is_obj.collision_type = 'p'
          names_obj_2.collision_type = 'p'
          names_obj.collision_type = 'p'

          if self.previous_time == 0 and ((is_obj.x - TILESIZE == names_obj.x and is_obj.x + TILESIZE == names_obj_2.x) and (is_obj.y == names_obj.y and is_obj.y == names_obj_2.y)) or ((is_obj.y - TILESIZE == names_obj.y and is_obj.y + TILESIZE == names_obj_2.y) and (is_obj.x == names_obj.x and is_obj.x == names_obj_2.x)):
            self.previous_time = 1
            

          else :
            self.previous_time = 0
            
            
        for atributes_obj in self.objects_atributes :
          is_obj.collision_type = 'p'
          atributes_obj.collision_type = 'p'
          names_obj.collision_type = 'p'

          if ((is_obj.x - TILESIZE == names_obj.x and is_obj.x + TILESIZE == atributes_obj.x) or (is_obj.x + TILESIZE == names_obj.x and is_obj.x - TILESIZE == atributes_obj.x)) and (is_obj.y == names_obj.y and is_obj.y == atributes_obj.y) or ((is_obj.y - TILESIZE == names_obj.y and is_obj.y + TILESIZE == atributes_obj.y) or (is_obj.y + TILESIZE == names_obj.y and is_obj.y - TILESIZE == atributes_obj.y)) and (is_obj.x == names_obj.x and is_obj.x == atributes_obj.x):
       
            if type(atributes_obj) == Push_object :
                
                if type(names_obj) == Wall_object :
                  for obj in self.walls :
                    obj.collision_type = 'p'
                    
                if type(names_obj) == Rock_object :
                  for obj in self.rocks :
                    obj.collision_type = 'p'

                if type(names_obj) == Baba_object :
                  for obj in self.babas :
                    obj.collision_type = 'p'
                    
                if type(names_obj) == Flag_object :
                  for obj in self.flags :
                    obj.collision_type = 'p'
                    
                    
            if type(atributes_obj) == Stop_object :
            
                if type(names_obj) == Flag_object :
                  for obj in self.flags :
                    obj.collision_type = 's'
                
                if type(names_obj) == Wall_object :
                  for obj in self.walls :
                    obj.collision_type = 's'
                    
                if type(names_obj) == Baba_object :
                  for obj in self.babas :
                    obj.collision_type = 's'

                if type(names_obj) == Rock_object :
                  for obj in self.rocks :
                    obj.collision_type = 's'
                

            if type(atributes_obj) == Winn_object :

                if type(names_obj) == Wall_object :
                  for obj in self.walls :
                    obj.collision_type = 'w'

                if type(names_obj) == Flag_object :
                  for obj in self.flags :
                    obj.collision_type = 'w'

                if type(names_obj) == Baba_object :
                  for obj in self.babas :
                    obj.collision_type = 'w'
                    
                if type(names_obj) == Rock_object :
                  for obj in self.rocks :
                    obj.collision_type = 'w'
            
            if type(atributes_obj) == You_object :

                if type(names_obj) == Baba_object :
                  self.player_group = self.babas

                if type(names_obj) == Wall_object :
                  self.player_group = self.walls

                if type(names_obj) == Rock_object :
                  self.player_group = self.rocks

                if type(names_obj) == Flag_object :
                  self.player_group = self.flags
    
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

        if event.key == pg.K_q :

          self.console()



  def draw(self):

    self.screen.fill(BGCOLOR)

    self.all_sprites.draw(self.screen)

    pg.display.flip()


  def console(self) :
    print("> game console, enter command : ")
    cmd = str(input("> "))
    try:
      exec(cmd)
    except:
      print("> ERROR")

game = Game()

def game_intro():
    print("title screen")
    bg_intro = pg.image.load("Background.png").convert_alpha()
    game.screen.blit(bg_intro, (233, 199))
    pg.display.flip()
    loop = bool(True)
    while loop:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("start")
                    loop = bool(False)
                    return bool(False)
                if event.key == pg.K_ESCAPE:
                    print("shutdown")
                    loop = bool(False)
                    return bool(True)

def game_loop():
    game = Game()
    game.new()
    return game.run()
    
def game_lost():
    print("game_lost")
    bg_lost = pg.image.load("Giveup.png").convert_alpha()
    screen.blit(bg_lost, (235, 192))
    pg.display.flip()
    loop = bool(True)
    while loop:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("restart")
                    loop = bool(False)
                    return bool(False)
                if event.key == pg.K_ESCAPE:
                    print("out")
                    loop = bool(False)
                    return bool(True)
    
def game_won():
    print("game is won")
    bg_won = pg.image.load("Thanks.png").convert_alpha()
    game.screen.blit(bg_won, (235, 192))
    pg.display.flip()
    loop = bool(True)
    while loop:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("restart")
                    loop = bool(False)
                    return bool(False)
                if event.key == pg.K_ESCAPE:
                    print("shutdown")
                    game.quit()


  

finished=game_intro()
while (not finished):
    print("finished",finished)
    if (not finished):
        lost=game_loop()
        if (lost):
            finished=game_lost()
        else:
            finished=game_won()
pg.quit()
