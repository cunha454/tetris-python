import pygame as pg
from config import WIDTH_SCREEN, LENGTH_SCREEN, FPS

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH_SCREEN, LENGTH_SCREEN))
        self.clock = pg.time.Clock()

    def load_screen(self):
        pg.display.flip()

    def enter_loop(self):
        self.loop = True
        while self.loop:
            self.catch_events()
            self.load_screen()
            self.dt = self.clock.tick(FPS)

    def catch_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False