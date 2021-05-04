import pygame_gui
import pygame as pg

class Options:
    def __init__(self, difficulty, square_size, manager):
        self._difficulty = difficulty
        self._square_size = square_size
        self._manager = manager
        self.difficulty_choice()
    
    def difficulty_choice(self):
        difficulties = ["easy", "medium", "hard"]
        starting = f"{self._difficulty.degree()}"
        rect = pg.Rect(5, 10, 80, 30)
        self._difficulty_choice = pygame_gui.elements.UIDropDownMenu(options_list=difficulties,
                                                                     starting_option=starting,
                                                                     relative_rect=rect,
                                                                     manager=self._manager)
