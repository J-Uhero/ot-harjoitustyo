import pygame as pg
import os

dirname = os.path.dirname(__file__)

class StatusSurface:
    def __init__(self, difficulty, square_size):
        self._width = difficulty.width() * square_size
        self._height = 50
        self._color = (100,100,100)
        self._status_surface = pg.Surface((self._width, self._height))
        self._status_surface.fill(self._color)
        self.place_images()

    def place_images(self):
        clock_logo = pg.image.load(os.path.join(dirname,
                                                "..",
                                                "assets",
                                                "clock_transparent_purple.png"))
        clock_dest = (self._width-85, 10)
        flag_logo = pg.image.load(os.path.join(dirname,
                                               "..",
                                               "assets",
                                               "flag_transparent.png"))
        flag_dest = (self._width-175,10)

        self._status_surface.blit(clock_logo, clock_dest)
        self._status_surface.blit(flag_logo, flag_dest)

    def give_surface(self):
        return self._status_surface

    def height(self):
        return self._height

    def width(self):
        return self._width
