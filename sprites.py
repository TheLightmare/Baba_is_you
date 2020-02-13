# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:25:37 2020

@author: m.kowalski
"""

import pygame as pg
from settings import *

class Player(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.player_img
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.hit_rect = PLAYER_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

class Wall(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.wall_img
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  
class Flag(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.flag_img
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
    