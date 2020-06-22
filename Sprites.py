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
    self.image = pg.Surface((0, 0)) #surface nulle et vide
    self.game = game
    self.rect = pg.Rect(x, y, TILESIZE, TILESIZE)
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = PLAYER_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

  def move(self, dx=0, dy=0):
    for player_obj in self.game.player_group :
        player_obj.collision_type='player'
    
    for player_obj in self.game.player_group :
      if player_obj.collision_type == 'player':
        if player_obj.x+dx<=HEIGHT-TILESIZE and player_obj.x+dx>=0 and player_obj.y+dy<WIDTH-TILESIZE and player_obj.y+dy>=0:
            l=player_obj.collide(dx, dy)
            dx=l[0]
            dy=l[1]
            player_obj.x += dx
            player_obj.y += dy

  def update(self) :
    self.rect.x = self.x 
    self.rect.y = self.y 


class Stop_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
    self.groups = game.all_sprites, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.stop_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y

  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :

            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
            
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
            
        
            
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    

class Wall(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 0
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
    
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y


class Baba(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 0
    self.groups = game.all_sprites, game.babas
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.baba_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y

  
class Flag(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 0
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    
    
    
    
  
class Box(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 0
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    

class Key(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 0
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y

class Rock(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 0
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    
    
class Tile(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type=0
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
  

class Wall_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y

class Box_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y

class Key_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y


class Rock_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    
class Baba_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
    self.groups = game.all_sprites, game.objects_names, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.baba_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    
class Is_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
class Push_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
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
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l
    
  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
    
    
    
class You_object(pg.sprite.Sprite) :
  def __init__(self, game, x, y) :
    self.collision_type = 'p'
    self.groups = game.all_sprites, game.objects_atributes, game.objects
    pg.sprite.Sprite.__init__(self, self.groups)
    self.game = game
    self.image = game.you_object_img
    self.rect = self.image.get_rect()
    self.rect.center = (x + TILESIZE/2, y + TILESIZE/2)
    self.hit_rect = WALL_HIT_RECT
    self.hit_rect.center = self.rect.center
    self.x = x
    self.y = y
  def collide(self, dx=0, dy=0):
    for obj in self.game.all_sprites:
      if obj.x == self.x+TILESIZE*dx and obj.y == self.y+TILESIZE*dy:
        if obj.collision_type == 'p' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
              
        elif obj.collision_type == 's' :
            dx=0
            dy=0
        elif obj.collision_type == 'player' :
            if obj.x+dx<=HEIGHT-TILESIZE and obj.x+dx>=0 and obj.y+dy<WIDTH-TILESIZE and obj.y+dy>=0 :
              obj.collision_type=0
              l=obj.collide(dx,dy)
              dx=l[0]
              dy=l[1]
              obj.x += dx
              obj.y += dy
            else :
              dy=0
              dx=0
        
              
        l=[dx,dy]
        return l
    l=[dx,dy]
    return l

  def update(self) :
    self.rect.x = self.x
    self.rect.y = self.y
    
