# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:32:17 2020

@author: m.kowalski
"""

import pygame as pg

WIDTH = 1008
HEIGHT = 1008

TILESIZE = 48
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BGCOLOR = (0, 0, 0)

PLAYER_HIT_RECT = pg.Rect(0, 0, TILESIZE, TILESIZE)
BABA_IMG = "BABA_image.png"
BABA_OBJECT_IMG = "BABA_object.png"
YOU_OBJECT_IMG = "YOU_special_object.png"

WALL_HIT_RECT = pg.Rect(0, 0, TILESIZE, TILESIZE)
WALL_IMG = "WALL_center_image.png"
WALL_OBJECT_IMG = "WALL_object.png"

IS_OBJECT_IMG = "IS_white_object.png"
STOP_OBJECT_IMG = "STOP_special_object.png"

PUSH_OBJECT_IMG = "PUSH_special_object.png"

FLAG_IMG = "FLAG_image.png"
FLAG_OBJECT_IMG = "FLAG_object.png"
WINN_OBJECT_IMG = "WIN_special_object.png"

BOX_IMG = "BOX_image.png"
BOX_OBJECT_IMG = "BOX_object.png"

KEY_IMG = "KEY_image.png"
KEY_OBJECT_IMG = "KEY_object.png"

TILE_IMG = "TILE_image.png"

ROCK_IMG = "ROCK_image.png"
ROCK_OBJECT_IMG = "ROCK_object.png"

STOP_OBJECT_IMG = "STOP_special_object.png"
