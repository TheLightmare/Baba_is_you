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
    self.image = pg.Surface((TILESIZE, TILESIZE))
    self.image.fill(YELLOW)
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.x = x
    self.y = y
