from repositories.score_repository import score_repository
from datetime import datetime

class ScoresService:
    def __init__(self):
        self.repository = score_repository

    def get_high_scores(self):
        easy = self.repository.find_high_scores_by_level("easy", 10)
        medium = self.repository.find_high_scores_by_level("medium", 10)
        hard = self.repository.find_high_scores_by_level("hard", 10)
        return easy, medium, hard

    def get_scores_by_name(self, name):
        return self.repository.find_score_by_name(name)      

    def new_score(self, name, time, level):
        date = datetime.now()
        if len(name) > 10:
            name = name[:10]
        if len(name) == 0:
            name = "nimetön"
        self.repository.create_score(name, time, level, date)

    def is_score_a_high_score(time, level):
        high_scores = self.repository.find_high_scores_by_level(level, 10)
        if high_scores[-1].time > time:
            return True
        return False

    def check_ranking_of_a_score(self, time, level):
        ranking = self.repository.check_ranking_of_a_score(time, level)
        return ranking[0]



