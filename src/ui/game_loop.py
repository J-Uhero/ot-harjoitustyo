import pygame as pg
import pygame_gui
from services.game_view import GameView
from ui.game_display import GameDisplay

class GameLoop:
    def __init__(self, display, difficulty, square_size):
        self._difficulty = difficulty
        self._square_size = square_size
        self._gameview = GameView(difficulty, square_size)
        self._display = GameDisplay(difficulty, square_size, self._gameview)
        self._stop = False
        self._clock = pg.time.Clock()

    def start(self):

        while True:  
            self._events()
            self._render()

            time_delta = self._clock.tick(60)/1000.0
            self._display.manager_update_time_delta(time_delta)

    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                left, middle, right = pg.mouse.get_pressed()
                position_x, position_y = pg.mouse.get_pos()
                if self._display.check_if_coordinates_in_game_surface(position_x, position_y):
                    position_y -= self._display.give_surface_height()
                    if left:
                        self._gameview.push_button(position_x, position_y, "left")
                    if right or middle:
                        self._gameview.push_button(position_x, position_y, "right")

            if event.type == pg.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self._display.give_new_game_button():
                        #self._gameview = GameView(self._difficulty, self._square_size)
                        self._gameview.new_game()

            self._display.manager_process_event(event)


    def _render(self):
        self._gameview._sprites.draw(self._display.give_game_surface())
        self._display.update_display()
        pg.display.update()

