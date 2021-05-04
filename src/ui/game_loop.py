import pygame as pg
import pygame_gui
from services.game_view import GameView
from ui.game_display import GameDisplay

class GameLoop:
    """ Pelinäppäinten painalluksista ja näytön päivittämisestä vastaavan pelisilmukkaolio.
    """
    def __init__(self, difficulty, square_size):
        """Konstruktori, joka luo GameLoop-olion.

        Args:
            difficulty (Difficulty): Vaikeustaso-olio, joka kertoo peliruutujen määrän ja sen myötä pelinäytön
                                     koon yhdessä peliruudukon ruutujen koon kanssa.           
            square_size (int): Kokonaisluku, joka kertoo yhden peliruudun koon.
        """
        self._difficulty = difficulty
        self._square_size = square_size
        self._gameview = None
        self._display = None
        self._stop = None
        self._clock = None
        self._build_game()

    def _build_game(self,):
        """Luo pelinäytön ja -näkymän 
        """
        self._gameview = GameView(self._difficulty, self._square_size)
        self._display = GameDisplay(self._difficulty, self._square_size, self._gameview)
        self._stop = False
        self._clock = pg.time.Clock()

    def start(self):
        """Funktio, joka käynnistää siinä olevan pelisilmukan, jossa koko peli pyörii.
        """

        while True:

            self._events()
            self._render()

            time_delta = self._clock.tick(60)/1000.0
            self._display.manager_update_time_delta(time_delta)

    def _events(self):
        """Vastaa pelin tapahtumista eli nappien painalluksista.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                left, middle, right = pg.mouse.get_pressed()
                position_x, position_y = pg.mouse.get_pos()
                keys = pg.key.get_pressed()
                if self._display.check_if_coordinates_in_game_surface(position_x, position_y):
                    position_y -= self._display.give_surface_height()
                    if left:
                        if keys[pg.K_LALT] or keys[pg.K_RALT]:
                            self._gameview.push_button(position_x, position_y, "right")
                        else:
                            self._gameview.push_button(position_x, position_y, "left")
                    if right or middle:
                        self._gameview.push_button(position_x, position_y, "right")

            if event.type == pg.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self._display.give_new_game_button():
                        self._gameview.new_game()
                        self._stop = False
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.text == "easy":
                        self._difficulty.easy()
                    if event.text == "medium":
                        self._difficulty.medium()
                    if event.text == "hard":
                        self._difficulty.hard()
                    self._build_game()
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    pass

            self._display.manager_process_event(event)


    def _render(self):
        """Päivittää pelinäytön ulkoasun.
        """
        if self._stop:
            pass
        else:
            self._gameview._sprites.draw(self._display.give_game_surface())
        self._display.update_display()
        pg.display.update()

