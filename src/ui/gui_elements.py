import pygame_gui
import pygame as pg
from ui.options import Options

class GuiElements:
    """Luokka eri Pygame Gui -kirjaston elementeille
    """
    def __init__(self, manager, width, surface_height, game_surface_height, square_size, difficulty, game_view):
        """[summary]

        Args:
            manager (manager): Pygame Gui -manageri, joka huolehtii elementtien päivitteämisestä ruudulle
            width (int): peliruudun leveys
            surface_height (int): pelin ylätason korkeus
            game_surface_height (int): peliruudukon korkeus
            difficulty (Difficulty): Pelin vaikeusasteolio
            game_view (GameView): Pelinäkymästä vastaava olio 
        """
        self._manager = manager
        self._width = width
        self._surface_height = surface_height
        self._game_surface_height = game_surface_height
        self._game_view = game_view
        self._difficulty = difficulty
        self._new_game_button = None
        self._flag_label = None
        self._clock_label = None
        self._drop_menu = Options(difficulty, square_size, manager)
        self.create_basic_elements()

    def create_basic_elements(self):
        """Luo pelin käynnistyttyä pelinäkymässä esiintyvät peruselementit
        """
        self.create_new_game_button()
        self.create_clock_label()
        self.create_flag_label()
        #self.create_winning_table()

    def create_new_game_button(self):
        rect = pg.Rect(10, self._surface_height + self._game_surface_height+10, 80, 30)
        self._new_game_button = pygame_gui.elements.UIButton(relative_rect=rect,
                                                             text="new game",
                                                             manager=self._manager)

    def create_flag_label(self):
        rect = pg.Rect(self._width - 180, 10, 80, 30)
        flags = self._game_view.give_flags()
        self._flag_label = pygame_gui.elements.UILabel(relative_rect=rect,
                                                       text=f"flags: {flags}",
                                                       manager=self._manager)

    def update_flag_label(self):
        self._flag_label.set_text(text=f"flags: {self._game_view.give_flags()}")

    def create_clock_label(self):
        rect = pg.Rect(self._width-90, 10, 80, 30)
        self._clock_label = pygame_gui.elements.UILabel(relative_rect=rect,
                                                        text=f"time: {self._game_view.give_time()}",
                                                        manager=self._manager)

    def update_clock_label(self, time):
        self._clock_label.set_text(f"time: {time}")

    def create_options_button(self):
        rect = pg.Rect(self._width-80, self._surface_height + self._game_surface_height+10, 70, 30)
        self._options_button = pygame_gui.elements.UIButton(relative_rect=rect,
                                                            text="options", manager=self._manager)
        #options = ["easy", "medium", "hard"]
        #self._options_button = pygame_gui.elements.UISelectionList(relative_rect, item_list, manager)

    def create_winning_table(self):
        rect = pg.Rect(10, self._surface_height+10, 250, 250)
        self._winning_table = pygame_gui.elements.UIWindow(rect=rect, manager=self._manager)
        rect2 = pg.Rect(10, 10, 80, 30)
        text_box = pygame_gui.elements.UITextEntryLine(relative_rect=rect2, manager=self._manager,
                                                       container=self._winning_table)

    def give_new_game_button(self):
        return self._new_game_button

    def give_flag_label(self):
        return self._flag_label

    def give_clock_label(self):
        return self._clock_label

    def give_options_button(self):
        return self._options_button
