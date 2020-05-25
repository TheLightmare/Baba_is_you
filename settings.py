# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:32:17 2020

@author: m.kowalski
"""

import pygame as pg

WIDTH = 1000
HEIGHT = 1000

TILESIZE = 48
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BGCOLOR = (0, 0, 0)

PLAYER_HIT_RECT = pg.Rect(0, 0, TILESIZE, TILESIZE)
PLAYER_IMG = "BABA_image.png"

WALL_HIT_RECT = pg.Rect(0, 0, TILESIZE, TILESIZE)
WALL_IMG = "WALL_center_image.png"
WALL_OBJECT_IMG = "WALL_object.png"

IS_OBJECT_IMG = "IS_white_object.png"

PUSH_OBJECT_IMG = "PUSH_special_object.png"

FLAG_IMG = "FLAG_image.png"

