from services.scores_service import ScoresService
import pygame_gui
import pygame as pg

class ScoreWindow:
    def __init__(self, manager, width, height, square_size):
        self._manager = manager
        self.rect = pg.Rect(0, 0, width * square_size, height * square_size)
        self.window = None
        self.service = ScoresService()
        self.build_high_score_window()

    def build_high_score_window(self):
        rect2 = pg.Rect(0, 0, 300, 350)
        self.window = pygame_gui.elements.UIWindow(rect=rect2,
                                              manager=self._manager,
                                              window_display_title="High Scores")
        rect3 = pg.Rect(0, 0, 230, 200)
        stats = pygame_gui.elements.UITextBox(html_text=self.high_score_text(),
                                              relative_rect=rect3,
                                              manager=self._manager,
                                              container=self.window)

    def high_score_text(self):
        texts = ["name:", "time:"]
        easy, medium, hard = self.service.get_high_scores()

        line = f"   {texts[0]:10}{texts[1]}<br>"
        text = "Easy: <br>" + line
        text += self.print_score_list(easy)

        text += "<br> <br>Medium: <br>" + line
        text += self.print_score_list(medium)
        
        text += "<br> <br>Hard: <br>" + line
        text += self.print_score_list(hard)
        kopio = text
        kopio.replace("<br>","\n")
        return text

    def print_score_list(self, score_list):
        text = ""
        if len(score_list) < 1:
            text += "—"
        rank = 1
        vali = "  "
        for score in score_list:
            if rank > 9:
                vali = " "
            text += f"{rank}.{vali}{score.name:10}{score.time:.2f} <br>"
            rank += 1
        return text




