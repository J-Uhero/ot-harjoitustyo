import pygame as pg
from status import Status
import os

dirname = os.path.dirname(__file__)

class OptionSurface:
    def __init__(self, difficulty, square_size):
        self._color = (200,200,200)
        self._width = (difficulty.width() * square_size)
        self._height = 60
        self._option_surface = pg.Surface((self._width, self._height))
        self.draw(Status.READY)

    def draw(self, game_status):
        self._option_surface.fill(self._color)
        face = ""
        if game_status == Status.GAMEOVER:
            face = pg.image.load(os.path.join(dirname,
                                              "..",
                                              "assets",
                                              "smiley_dead.png"))
        elif game_status == Status.VICTORY or game_status == Status.NEWSCORE:
            face = pg.image.load(os.path.join(dirname,
                                              "..",
                                              "assets",
                                              "smiley_winner.png"))
        else:
            face = pg.image.load(os.path.join(dirname,
                                              "..",
                                              "assets",
                                              "smiley_basic.png"))
        dest = (self._width / 2 - 25, 5)
        self._option_surface.blit(face, dest)

    def give_surface(self):
        return self._option_surface

    def height(self):
        return self._height

    def width(self):
        return self._width
