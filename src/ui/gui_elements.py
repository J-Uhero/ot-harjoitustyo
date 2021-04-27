import pygame_gui
import pygame as pg

class GuiElements:
    def __init__(self, manager, width, surface_height, game_surface_height, square_size, game_view):
        self._manager = manager
        self._width = width
        self._surface_height = surface_height
        self._game_surface_height = game_surface_height
        self._game_view = game_view
        self._new_game_button = None
        self._flag_label = None
        self._clock_label = None
        self.create_basic_elements()

    def create_basic_elements(self):
        self.create_new_game_button()
        self.create_clock_label()
        self.create_flag_label()

    def create_new_game_button(self):
        rect = pg.Rect(10, self._surface_height + self._game_surface_height+10, 100, 30)
        self._new_game_button = pygame_gui.elements.UIButton(relative_rect=rect,
                                                             text="new game",
                                                             manager=self._manager)

    def create_flag_label(self):
        rect = pg.Rect(10, 10, 100, 30)
        flags = self._game_view.give_flags()
        self._flag_label = pygame_gui.elements.UILabel(relative_rect=rect,
                                                       text=f"flags: {flags}",
                                                       manager=self._manager)

    def update_flag_label(self):
        self._flag_label.set_text(text=f"flags: {self._game_view.give_flags()}")

    def create_clock_label(self):
        rect = pg.Rect(self._width-110, 10, 100, 30)
        self._clock_label = pygame_gui.elements.UILabel(relative_rect=rect,
                                                  text=f"time: {self._game_view.give_time()}",
                                                  manager=self._manager)

    def update_clock_label(self, time):
        self._clock_label.set_text(f"time: {time}")

    def give_new_game_button(self):
        return self._new_game_button

    def give_flag_label(self):
        return self._flag_label

    def give_clock_label(self):
        return self._clock_label

    def create_options_button(self):
        pass
