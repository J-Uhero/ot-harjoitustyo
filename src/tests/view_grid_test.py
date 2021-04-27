import unittest
from services.view_grid import ViewGrid
from difficulty import Difficulty

class TestView(unittest.TestCase):
    def setUp(self):
        self.difficulty = Difficulty()
        self.random_view = ViewGrid(self.difficulty)


    def test_the_view_is_empty_at_the_beginning(self):
        empty = True
        for i in self.random_view.view:
            for j in i:
                if j != " ":
                    empty = False
        self.assertEqual(empty, True)

    def test_if_the_first_openet_square_is_zero(self):
        self.random_view.push_left_button(4,4)
        content = self.random_view.coordinates(4,4)
        self.assertEqual(content, "0")

    def test_if_flags_on_mines_and_squares_opened_leads_to_victory(self):
        self.random_view.push_left_button(0,0)
        mine_locations = self.random_view.grid.give_mines_locations()

        for location in mine_locations:
            self.random_view.push_right_button(location[0], location[1])
        for i in range(self.random_view.height):
            for j in range(self.random_view.width):
                self.random_view.push_left_button(i,j)

        status = self.random_view.give_game_status()
        flags = self.random_view.give_flags()
        unopened = self.random_view.give_unopened()
        self.assertEqual((status, flags, unopened), ("victory",0,0))
