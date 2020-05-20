# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:32:17 2020

@author: m.kowalski
"""

import pygame as pg

TILESIZE = 48
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BGCOLOR = (0, 0, 0)

PLAYER_HIT_RECT = pg.Rect(0, 0, TILESIZE, TILESIZE)
PLAYER_IMG = "BABA_image.png"

WALL_HIT_RECT = pg.Rect(0, 0, TILESIZE, TILESIZE)
WALL_IMG = "WALL_center_image.png"

FLAG_IMG = "FLAG_image.png"
