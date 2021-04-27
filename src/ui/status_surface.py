import pygame as pg

class StatusSurface:
    def __init__(self, difficulty, square_size):
        self._width = difficulty.width() * square_size
        self._height = 50
        self._color = (100,100,100)
        self._status_surface = pg.Surface((self._width, self._height))
        self._status_surface.fill(self._color)

    def give_surface(self):
        return self._status_surface

    def height(self):
        return self._height

    def width(self):
        return self._width
