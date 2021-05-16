from services.scores_service import ScoresService
import pygame_gui
import pygame as pg

rankings = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th",
            6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th"}

class NewScoreWindow:
    def __init__(self, manager, game_view, service, difficulty):
        self._manager = manager
        self.score_service = service
        self.difficulty = difficulty.degree()
        self.window = None
        self.enter_button = None
        self.text_entry = None
        self.time = game_view.give_exact_time()
        self.built_new_score_window()

    def built_new_score_window(self):
        rect = pg.Rect(0, 0, 280, 280)
        self.window = pygame_gui.elements.UIWindow(rect=rect,
                                                   manager=self._manager,
                                                   window_display_title="Congratulations!")
        self.built_text_box()

    def built_text_box(self):
        rect = pg.Rect(10, 10, 220, 170)
        text = f"new score! <br>time: {self.time:.2f} seconds <br>level: {self.difficulty}"
        ranking = self.score_service.check_ranking_of_a_score(self.time, self.difficulty)+1
        if ranking <= 10:
            text += f"<br> <br>ranking: {rankings[ranking]} place \
                    <br> <br>insert your name below<br>and press enter"
            self.built_text_entry()
            self.built_enter_button()
        else:
            text += f"<br> <br>score below top 10"

        textbox = pygame_gui.elements.UITextBox(html_text=text,
                                                relative_rect=rect,
                                                manager=self._manager,
                                                container=self.window)

    def built_text_entry(self):
        rect = pg.Rect(10, 180, 120, 30)
        self.text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=rect,
                                                         manager=self._manager,
                                                         container=self.window)
        

    def built_enter_button(self):
        rect = pg.Rect(140, 180, 80, 30)
        self.enter_button = pygame_gui.elements.UIButton(relative_rect=rect,
                                                         text="enter",
                                                         manager=self._manager,
                                                         container=self.window)

    def get_window(self):
        return self.window
    
    def get_enter_button(self):
        return self.enter_button

    def get_text_entry(self):
        return self.text_entry
