import pygame as pg
from difficulty import Difficulty
from services.view_grid import ViewGrid
from square import Square

class GameView:
    def __init__(self, difficulty, square_size):
        self._difficulty = difficulty
        self._square_size = square_size
        self._sprites = pg.sprite.Group()
        self._grid = None
        self.new_game()
        self._initialized_sprites()
        self._continue_game = True

    def new_game(self):
        self.set_display_size()
        self._grid = ViewGrid(self._difficulty)

    def set_display_size(self):
        pass

    def _initialized_sprites(self):
        for y in range(self._difficulty.height()):
            for x in range(self._difficulty.width()):
                square_type = self._grid.coordinates(y, x)
                self._sprites.add(Square(y, x, square_type, self._square_size))

    def push_button(self, pos_x, pos_y, button):
        if self._continue_game:
            y = ((pos_x - 1) // self._square_size)
            x = ((pos_y - 1) // self._square_size)
            if button == "left":
                self._grid.push_left_button(x, y)
            if button == "right":
                self._grid.push_right_button(x, y)
            self.check_status()

        self._initialized_sprites()

    def check_status(self):
        status = self._grid.give_game_status()
        if status == "game_over":
            self._continue_game = False
            return 1
        if status == "victory":
            self._continue_game = False
            return 2
        return 0
