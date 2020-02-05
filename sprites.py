# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:25:37 2020

@author: m.kowalski
"""

import pygame as pg
from settings import *

class Player() :
  def __init__(self, game, x, y) :
    self.game = game
    self.image = pg.Surface((TILESIZE, TILESIZE))
    self.image.fill(YELLOW)
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
