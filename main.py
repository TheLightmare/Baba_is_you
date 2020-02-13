# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 08:26:01 2020

@author: m.kowalski m.morgenthaler a.billaud
"""

import pygame as pg
from os import path
import sys
from settings import *
from sprites import *

WIDTH = 1200
HEIGHT = 800

class Game() :

  def __init__(self) :
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.key.set_repeat(500, 100)
    self.load_data()
  
  def load_data(self):
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder, "sprites")
    self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
    self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
    self.flag_img = pg.image.load(path.join(img_folder, FLAG_IMG)).convert_alpha()
  def new(self) :
    self.all_sprites = pg.sprite.Group()
    self.player = Player(self, 40, 20)
    self.flag = Flag(self, 300, 200)
    self.walls = []
    for i in range(0, 10) :
      self.walls.append(Wall(self, i*TILESIZE, 100))
  
  def run(self) :
    self.playing = True
    while self.playing :
      self.events()
      self.draw()
      
  def quit(self) :
    pg.quit()
    sys.exit()
  
  def events(self):
    # catch all events here
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.quit()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE] :
      self.quit()

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

  
  
  
  
  
  
  
  