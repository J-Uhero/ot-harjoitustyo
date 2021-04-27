import pygame as pg

class OptionSurface:
    def __init__(self, difficulty, square_size):
        self._color = (200,200,200)
        self._width = (difficulty.width() * square_size)
        self._height = 50
        self._option_surface = pg.Surface((self._width, self._height))
        self._option_surface.fill(self._color)

    def give_surface(self):
        return self._option_surface

    def height(self):
        return self._height

    def width(self):
        return self._width
