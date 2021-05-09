import pygame as pg
import pygame_gui
from ui.game_surface import GameSurface
from ui.options_surface import OptionSurface
from ui.status_surface import StatusSurface
from ui.gui_elements import GuiElements
from ui.options import Options
from ui.score_window import ScoreWindow
from ui.new_score_window import NewScoreWindow
from status import Status
from game_status import GameStatus

class GameDisplay:
    """Pelin näyttöä kuvaava luokka
    """
    def __init__(self, difficulty, square_size, game_view, game_status, scores_service):
        """Luokan konstruktori

        Args:
            difficulty (Difficulty): pelin vaikeustasoa kuvaava olio
            square_size (int): yhden peliruudun sivun pituus
            game_view (GameView): pelinäkymää kuvaava luokka
        """
        self.game_surface = GameSurface(difficulty, square_size)
        self.option_surface = OptionSurface(difficulty, square_size)
        self.status_surface = StatusSurface(difficulty, square_size)
        self._height = self.game_surface.height() + self.option_surface.height() + \
                       self.status_surface.height()
        self._width = difficulty.width() * square_size
        self.game_status = game_status
        self.game_view = game_view
        self._square_size = square_size
        self._difficulty = difficulty
        self.score_service = scores_service
        self.new_score_window = None
        self.built_display()
        self.built_elements(square_size)
        self.update_display()


    def built_display(self):
        """Luo Pygamen pelinäytön ja asettaa sille nimen
        """
        self._display = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption("Miinaharava")

    def update_display(self):
        """Päivittää näytön: asettaa sille sen eri alustat, päivittää peliruudun
        käyttöjärjestelmäelementtien tiedot ja piirtää ne näyttöön.
        """
        self._display.blit(self.give_status_surface(), (0, 0))
        self._display.blit(self.give_game_surface(), (0, self.status_surface.height()))
        self._display.blit(self.give_option_surface(), (0, self.game_surface.height() + 
                           self.status_surface.height()))
        self.check_victory()
        self.update_elements()
        self.manager_draw_ui()

    def check_victory(self):
        if self.game_status.get_status() == Status.VICTORY:
            self.game_status.set_status(Status.NEWSCORE)
            self.new_score_window = NewScoreWindow(self.manager,
                                                   self.game_view,
                                                   self.score_service,
                                                   self._difficulty)

    def built_elements(self, square_size):
        """Luo pelin aloitusnäkymässä esiintyvät käyttöjärjestelmäelementit

        Args:
            square_size (int): peliruudukon yhden ruudun sivun pituus
        """
        self.manager = pygame_gui.UIManager((self._width, self._height))
        self.elements = GuiElements(self.manager, self._width, self.option_surface.height(),
                               self.game_surface.height(), self._square_size, self._difficulty,
                               self.game_view)

    def built_score_table(self):
        height = self._difficulty.height() * self._square_size
        ScoreWindow(self.manager, self._width, height, self._square_size)
        #self.new_score_window = NewScoreWindow(self.manager, self.game_view, self.score_service, self._difficulty)

    def update_elements(self):
        """Päivittää pelin käyttöliittymäelementit
        """
        time = self.game_view.give_time()
        self.elements.update_clock_label(time)
        self.elements.update_flag_label()

    def manager_draw_ui(self):
        """Piirtää käyttöliittymäelementit näyttöön.
        """
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
    
    def give_scores_button(self):
        return self.elements.give_scores_button()

    def give_surface_height(self):
        return self.status_surface.height()

    def give_drop_menu(self):
        return

    def get_enter_score_button(self):
        return self.new_score_window.get_enter_button()

    def get_new_score_window(self):
        return self.new_score_window.get_window()

    def get_scores_text_entry(self):
        return self.new_score_window.get_text_entry()

    def check_if_coordinates_in_game_surface(self, position_x, position_y):
        y_max_height = self.give_surface_height() + self.game_surface.height()
        if 0 <= position_x <= self._width \
            and self.give_surface_height() <= position_y <= y_max_height:
            return True
        return False
