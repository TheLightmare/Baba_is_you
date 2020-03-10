import pygame as pg

WIDTH = 1000
HEIGHT = 1000
TILESIZE = 32
GREEN = (0, 255, 0)

class Snake(pg.sprite.Sprite) :
    def __init__(self, game, coords, lenght) :
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE - 2, TILESIZE - 2))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.coords = coords
        
    def update(self) :
        self.rect.x = self.coords[0]
        self.rect.y = self.coords[1]


class Game() :
    def __init__(self) :
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)

    def new(self) :
        self.all_sprites = pg.sprite.Group()
        self.lenght = 3
        direction = 1
        self.snake = []
        for i in range(10, 10 + self.lenght) :
            self.snake.append(Snake(self, [i*TILESIZE, 0], 3))

    def update(self) :
        self.partie = True
        while self.partie :
            self.events()
            for self.part in self.snake :
                self.part.update()
            self.draw()

    def events(self) :
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                if event.key == pg.K_LEFT:
                    self.move(direction = 3)
                if event.key == pg.K_RIGHT:
                    self.move(direction = 1)
                if event.key == pg.K_UP:
                    self.move(direction = 2)
                if event.key == pg.K_DOWN:
                    self.move(direction = 4)


    def move(self, direction) :
        
        if direction == 1 :
            for self.part in self.snake :
                for i in range(0, len(self.part.coords), 2) :
                    self.part.coords[i] += TILESIZE
        if direction == 4 :
            for self.part in self.snake :
                for i in range(1, len(self.part.coords), 2) :
                    self.part.coords[i] += TILESIZE
                    
    def draw(self) :
        self.all_sprites.draw(self.screen)
        pg.display.flip()



g = Game()

while True :
    g.new()
    g.update()
            
