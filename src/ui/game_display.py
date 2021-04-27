import pygame as pg
import pygame_gui
from ui.game_surface import GameSurface
from ui.options_surface import OptionSurface
from ui.status_surface import StatusSurface
from ui.gui_elements import GuiElements

class GameDisplay:
    def __init__(self, difficulty, square_size, game_view):
        self.game_surface = GameSurface(difficulty, square_size)
        self.option_surface = OptionSurface(difficulty, square_size)
        self.status_surface = StatusSurface(difficulty, square_size)
        self._height = self.game_surface.height() + self.option_surface.height() + \
                       self.status_surface.height()
        self._width = difficulty.width() * square_size
        self.game_view = game_view

        self.built_display()
        self.built_elements(square_size)
        self.update_display()

    def built_display(self):
        self._display = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption("Miinaharava")

    def update_display(self):
        self._display.blit(self.give_status_surface(), (0, 0))
        self._display.blit(self.give_game_surface(), (0, self.status_surface.height()))
        self._display.blit(self.give_option_surface(), (0, self.game_surface.height() + 
                           self.status_surface.height()))
        self.update_elements()
        self.manager_draw_ui()

    def built_elements(self, square_size):
        self.manager = pygame_gui.UIManager((self._width, self._height))
        self.elements = GuiElements(self.manager, self._width, self.option_surface.height(),
                               self.game_surface.height(), square_size, self.game_view)

    def update_elements(self):
        time = self.game_view.give_time()
        self.elements.update_clock_label(time)
        self.elements.update_flag_label()

    def manager_draw_ui(self):
        self.manager.draw_ui(self._display)

    def manager_update_time_delta(self, time_delta):
        self.manager.update(time_delta)

    def manager_process_event(self, event):
        self.manager.process_events(event)

    def give_display(self):
        return self._display

    def give_status_surface(self):
        return self.status_surface.give_surface()

    def give_game_surface(self):
        return self.game_surface.give_surface()

    def give_option_surface(self):
        return self.option_surface.give_surface()

    def give_new_game_button(self):
        return self.elements.give_new_game_button()

    def give_flag_label(self):
        return self.elements.give_flag_label()

    def give_clock_label(self):
        return self.elements.give_clock_label()

    def give_surface_height(self):
        return self.status_surface.height()

    def check_if_coordinates_in_game_surface(self, position_x, position_y):
        y_max_height = self.give_surface_height() + self.game_surface.height()
        if 0 <= position_x <= self._width and self.give_surface_height() <= position_y <= y_max_height:
            return True
        return False
