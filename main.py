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

WIDTH = 600
HEIGHT = 500


class Game() :

  def __init__(self) :
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.key.set_repeat(500, 100)
    
  def new(self) :
    self.all_sprites = pg.sprite.Group()
    self.player = Player(self, 10, 10)
  
  def run(self) :
    self.playing = True
    while self.playing :
      self.events()
    
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

while True :
  game.show_start_screen()
  game.new()
  game.run()
  
  
  
  
  
  
  
  
  