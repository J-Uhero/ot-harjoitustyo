import unittest
import build
from services.scores_service import ScoresService

class TestScoresService(unittest.TestCase):
    def setUp(self):
        build.build()
        self.service = ScoresService()
        level = "easy"
        time = 20.0000
        name = "TestName"
        for i in range(10):
            name += str(i)
            time += 1
            self.service.new_score(name, time, level)

    def test_ranking_of_a_score(self):
        level = "easy"
        time = 21.5000
        ranking = self.service.check_ranking_of_a_score(time, level)
        self.assertEqual(ranking, 2)

    def test_is_score_a_high_score(self):
        level = "easy"
        time1 = 40.0000
        result1 = self.service.is_score_a_high_score(time1, level)
        time2 = 25.0000
        result2 = self.service.is_score_a_high_score(time2, level)
        self.assertEqual((result1, result2), (False, True))

    def test_that_the_ranking_of_a_score_is_right(self):
        level = "easy"
        time1 = 19.0000
        result1 = self.service.check_ranking_of_a_score(time1, level)
        time2 = 24.0500
        result2 = self.service.check_ranking_of_a_score(time2, level)
        self.assertEqual((result1, result2), (1, 5))

    def test_that_the_list_has_right_length(self):
        self.service.new_score("TestName", 25.0000, "easy")
        diff1 = self.service.get_high_scores()
        self.service.new_score("TestName", 25.0000, "easy")
        self.service.new_score("TestName2", 25.0000, "hard")
        diff2 = self.service.get_high_scores()
        self.assertEqual((len(diff1[0]), len(diff1[2]), len(diff2[0]),len(diff2[2])),
                         (10, 0, 10, 1))

    def test_if_the_names_are_right(self):
        self.service.new_score("TooooooLongName", 25.0000, "medium")
        self.service.new_score("", 25.0000, "hard")
        diff = self.service.get_high_scores()
        self.assertEqual((len(diff[1][0].name), diff[2][0].name), (10, "untitled"))
