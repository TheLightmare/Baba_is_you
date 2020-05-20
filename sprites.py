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
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = PLAYER_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

  def move(self, dx=0, dy=0):
    self.collide_with_objects(dx, dy)
    self.x += dx
    self.y += dy

  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == (self.x + dx)*TILESIZE and obj.y == (self.y + dy)*TILESIZE:
        obj.x += dx*TILESIZE
        obj.y += dy*TILESIZE
        print(obj.x, obj.y)

  def update(self) :
    self.rect.x = self.x * TILESIZE
    self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.walls
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.wall_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
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
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

class Wall_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.wall_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y


class Is_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.is_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
class Push_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.push_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
