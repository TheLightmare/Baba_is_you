"""
Created on Wed Feb  5 08:26:01 2020
@author: m.kowalski m.morgenthaler a.billaud
"""
from os import path
import pygame as pg
from settings import *
from sprites import *
from tilemap import *

finished=bool(False)
lost=bool(False)

pg.init()
screen = pg.display.set_mode((1152, 768))
pg.key.set_repeat(500, 100)
game_folder = path.dirname(__file__)

class Game():

    def __init__(self):
        self.wall_collision = 1
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, "map.txt"))
        img_folder = path.join(game_folder, "sprites")
        self.baba_img = pg.image.load(path.join(img_folder, BABA_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.flag_img = pg.image.load(path.join(img_folder, FLAG_IMG)).convert_alpha()
        self.box_img = pg.image.load(path.join(img_folder, BOX_IMG)).convert_alpha()
        self.key_img = pg.image.load(path.join(img_folder, KEY_IMG)).convert_alpha()
        self.rock_img = pg.image.load(path.join(img_folder, ROCK_IMG)).convert_alpha()
        self.wall_object_img = pg.image.load(path.join(img_folder, WALL_OBJECT_IMG)).convert_alpha()
        self.is_object_img = pg.image.load(path.join(img_folder, IS_OBJECT_IMG)).convert_alpha()
        self.push_object_img = pg.image.load(path.join(img_folder, PUSH_OBJECT_IMG)).convert_alpha()
        self.box_object_img = pg.image.load(path.join(img_folder, BOX_OBJECT_IMG)).convert_alpha()
        self.key_object_img = pg.image.load(path.join(img_folder, KEY_OBJECT_IMG)).convert_alpha()
        self.rock_object_img = pg.image.load(path.join(img_folder, ROCK_OBJECT_IMG)).convert_alpha()
        self.you_object_img = pg.image.load(path.join(img_folder, YOU_OBJECT_IMG)).convert_alpha()
        self.baba_object_img = pg.image.load(path.join(img_folder, BABA_OBJECT_IMG)).convert_alpha()

    def new(self) :
        self.all_sprites = pg.sprite.Group()
        self.objects = pg.sprite.Group()
        self.objects_is = pg.sprite.Group()
        self.objects_names = pg.sprite.Group()
        self.objects_attributes = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.babas = pg.sprite.Group()
        self.flag = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        irow = 0
        icol = 0
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col*TILESIZE, row*TILESIZE)
                if tile == 'W':
                    Wall_object(self, col*TILESIZE, row*TILESIZE)
                if tile == 'I':
                    Is_object(self, col*TILESIZE, row*TILESIZE)
                if tile == 'P':
                    Push_object(self, col*TILESIZE, row*TILESIZE)
                if tile == 'f':
                    self.flag = Flag(self, col*TILESIZE, row*TILESIZE)
                if tile == 'b':
                    Baba(self, col*TILESIZE, row*TILESIZE)
                    irow = row
                    icol = col
                if tile == 'Y':
                    You_object(self, col*TILESIZE, row*TILESIZE)
                if tile == 'B':
                    Baba_object(self, col*TILESIZE, row*TILESIZE)
        self.player = Player(self, icol*TILESIZE, irow*TILESIZE)

    def events(self):
    # catch all events here
        for event in pg.event.get():
            # button pressed
            if event.type == pg.KEYDOWN:
                print("event.type=",self.player.x,self.player.y)
                print("event.type=",self.map.width,self.map.height)
                if event.key == pg.K_ESCAPE:
                    return bool(True)

                if ((event.key == pg.K_LEFT) and (self.player.x>0)):
                    print("left")
                    """for i in range (0,TILESIZE):
                    self.player.move(dx=-1)
                    self.update()
                    self.draw()"""
                    self.player.move(dx=-TILESIZE)

                if ((event.key == pg.K_RIGHT) and (self.player.x<self.map.width-TILESIZE)):
                    print("right")
                    """for i in range (0,TILESIZE):
                    self.player.move(dx=1)
                    self.update()
                    self.draw()"""
                    self.player.move(dx=TILESIZE)

                if ((event.key == pg.K_UP) and (self.player.y>0)):
                    print("up")
                    """for i in range (0,TILESIZE):
                    self.player.move(dy=-1)
                    self.update()
                    self.draw()"""
                    self.player.move(dy=-TILESIZE)

                if ((event.key == pg.K_DOWN) and (self.player.y<self.map.height-TILESIZE)):
                    print("down")
                    """for i in range (0,TILESIZE):
                    self.player.move(dy=1)
                    self.update()
                    self.draw()"""
                    self.player.move(dy=TILESIZE)
        return bool(False)

    def scan_map(self) :
        for is_obj in self.objects_is :
            for names_obj in self.objects_names :
                for attributes_obj in self.objects_attributes :
                    if ((is_obj.x - TILESIZE == names_obj.x and is_obj.x + TILESIZE == attributes_obj.x) or (is_obj.x + TILESIZE == names_obj.x and is_obj.x - TILESIZE == attributes_obj.x)) and (is_obj.y == names_obj.y and is_obj.y == attributes_obj.y) or ((is_obj.y - TILESIZE == names_obj.y and is_obj.y + TILESIZE == attributes_obj.y) or (is_obj.y + TILESIZE == names_obj.y and is_obj.y - TILESIZE == attributes_obj.y)) and (is_obj.x == names_obj.x and is_obj.x == attributes_obj.x):
                        if type(names_obj) == Wall_object and type(attributes_obj) == Push_object :
                            self.wall_collision = 2
                        if type(attributes_obj) == You_object :
                            if type(names_obj) == Baba_object :
                                self.player_group = self.babas
                            if type(names_obj) == Wall_object :
                                self.player_group = self.walls

    def update(self):
    # update portion of the game loop
        self.all_sprites.update()
        self.scan_map()

    def draw(self):
        screen.fill(BGCOLOR)
        self.all_sprites.draw(screen)
        pg.display.flip()

    def run(self):
        self.playing = True
        while self.playing:
            escape=self.events()
            self.update()
            self.draw()
            if (self.flag.x == self.player.x):
                if (self.flag.y == self.player.y):
                    return bool(False)
            if escape:
                self.playing = bool(False)
        return bool(True)        


def game_intro():
    print("game_intro")
    bg_intro = pg.image.load("Background.png").convert_alpha()
    screen.blit(bg_intro, (233, 199))
    pg.display.flip()
    loop = bool(True)
    while loop:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("go")
                    loop = bool(False)
                    return bool(False)
                if event.key == pg.K_ESCAPE:
                    print("out")
                    loop = bool(False)
                    return bool(True)

def game_loop():
    print("game_loop")
    game = Game()
    game.new()
    return game.run()
    
def game_lost():
    print("game_lost")
    bg_lost = pg.image.load("Giveup.png").convert_alpha()
    screen.blit(bg_lost, (235, 192))
    pg.display.flip()
    loop = bool(True)
    while loop:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("restart")
                    loop = bool(False)
                    return bool(False)
                if event.key == pg.K_ESCAPE:
                    print("out")
                    loop = bool(False)
                    return bool(True)
    
def game_won():
    print("game_won")
    bg_won = pg.image.load("Thanks.png").convert_alpha()
    screen.blit(bg_won, (235, 192))
    pg.display.flip()
    loop = bool(True)
    while loop:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("restart")
                    loop = bool(False)
                    return bool(False)
                if event.key == pg.K_ESCAPE:
                    print("out")
                    loop = bool(False)
                    return bool(True)

finished=game_intro()
while (not finished):
    print("finished",finished)
    if (not finished):
        lost=game_loop()
        if (lost):
            finished=game_lost()
        else:
            finished=game_won()
pg.quit()

