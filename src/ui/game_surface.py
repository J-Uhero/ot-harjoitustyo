import pygame as pg

class GameSurface:
    def __init__(self, difficulty, square_size):
        self._height = difficulty.height() * square_size
        self._width = difficulty.width() * square_size
        self._game_surface = pg.Surface((self._width, self._height))
        self._game_surface.fill((100, 100, 100))

    def give_surface(self):
        return self._game_surface

    def give_game_view(self):
        return self._gameview

    def height(self):
        return self._height

    def width(self):
        return self._width

    