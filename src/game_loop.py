import pygame as pg
from game_view import GameView

class GameLoop:
    def __init__(self, display, difficulty, square_size):
        self._display = display
        self._gameview = GameView(difficulty, square_size)
        self._stop = False
    
    def start(self):

        while True:
            self._events()
            self._render()

    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                left, middle, right = pg.mouse.get_pressed()
                position_x, position_y = pg.mouse.get_pos()
                if left:
                    self._gameview.push_button(position_x, position_y, "left")
                if right or middle:
                    self._gameview.push_button(position_x, position_y, "right")

    def _render(self):
        self._gameview._sprites.draw(self._display)
        pg.display.update()
        status = self._gameview.check_status()
        if status == 1:
            
        
        


