# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:25:37 2020

@author: m.kowalski
"""
from time import*
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
    if self.collide_with_walls(dx, dy) != 1 :
      l=self.collide_with_objects(dx, dy)
   
      dx=l[0]
      dy=l[1]
      self.x += dx
      self.y += dy
    

  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

  def collide_with_walls(self, dx=0, dy=0):
    for wall in self.game.walls:
      if wall.x == self.x + TILESIZE*dx and wall.y == self.y + TILESIZE*dy:
        return 1
      
    return 0

  def update(self) :
    self.rect.x = self.x 
    self.rect.y = self.y 


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
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

  
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
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l
  
class Box(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.box_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

class Key(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.key_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

class Rock(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.Rock_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

class Tile(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.tile_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

class Wall_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects_names, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.wall_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l
            

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y

class Box_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects_names, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.box_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y

class Key_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects_names, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.key_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y


class Rock_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects_names, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.rock_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    
    
    
    
class Is_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects_is, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.is_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
class Push_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.groups = game.all_sprites, game.objects_atributes, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.push_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide_with_objects(self, dx=0, dy=0):
    for obj in self.game.objects:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if (dx!=0 and obj.x <WIDTH-TILESIZE and obj.x>0) or (dy!=0 and obj.y <HEIGHT-TILESIZE and obj.y>0) :
            l=obj.collide_with_objects(dx,dy)
            dx=l[0]
            dy=l[1]
            obj.x += dx
            obj.y += dy
        else :
            dy=0
            dx=0
    l=[dx,dy]
    return l

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
