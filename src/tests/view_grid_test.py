import unittest
from services.view_grid import ViewGrid
from entities.difficulty import Difficulty
from status import Status
from game_status import GameStatus

class TestViewGrid(unittest.TestCase):
    def setUp(self):
        self.difficulty = Difficulty()
        self.game_status = GameStatus()
        self.random_view = ViewGrid(self.difficulty, self.game_status)

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
        self.assertEqual((status.get_status(), flags, unopened), (Status.VICTORY,0,0))

    def test_if_the_victory_when_flags_are_putted_last(self):
        self.random_view.push_left_button(0,0)
        mine_locations = self.random_view.grid.give_mines_locations()

        for i in range(self.random_view.height):
            for j in range(self.random_view.width):
                if (i,j) not in mine_locations:
                    self.random_view.push_left_button(i,j)
        for location in mine_locations:
            self.random_view.push_right_button(location[0], location[1])

        status = self.random_view.give_game_status()
        flags = self.random_view.give_flags()
        unopened = self.random_view.give_unopened()
        self.assertEqual((status.get_status(), flags, unopened), (Status.VICTORY,0,0))

    def test_flag_cant_be_opened(self):
        self.random_view.push_right_button(0, 0)
        status1 = self.random_view.coordinates(0, 0)
        self.random_view.push_left_button(0, 0)
        status2 = self.random_view.coordinates(0, 0)
        self.random_view.push_right_button(0, 0)
        status3 = self.random_view.coordinates(0, 0)
        self.random_view.push_left_button(0, 0)
        status4 = self.random_view.coordinates(0, 0)
        self.assertEqual((status1, status2, status3, status4), ("f", "f", " ", "0"))

    def test_flags_cant_be_placed_if_they_all_are_used(self):
        flags = self.random_view.give_flags()
        for i in range(2):
            for j in range(5):
                self.random_view.push_right_button(i, j)
        self.random_view.push_right_button(3, 6)
        status = self.random_view.coordinates(3, 6)

        self.assertEqual((flags, status), (10, " "))

    def test_mines_are_opened_when_game_over(self):
        self.random_view.push_left_button(0, 0)
        mines = self.random_view.grid.give_mines_locations()
        self.random_view.push_left_button(mines[0][0], mines[0][1])
        status_list = []
        for i in range(0,len(mines)):
            status_list.append(self.random_view.coordinates(mines[i][0], mines[i][1]))
        print(mines)
        print(status_list)
        self.assertEqual(status_list, ["r","x","x","x","x","x","x","x","x","x"])

    def test_if_difficulties_have_right_sizes_and_amoud_of_mines(self):
        self.random_view.push_left_button(0, 0)
        height1 = self.random_view.height
        width1 = self.random_view.width
        mines1 = len(self.random_view.grid.give_mines_locations())

        self.difficulty.medium()
        self.game_status = GameStatus()
        self.random_view = ViewGrid(self.difficulty, self.game_status)
        self.random_view.push_left_button(0, 0)
        height2 = self.random_view.height
        width2 = self.random_view.width
        mines2 = len(self.random_view.grid.give_mines_locations())

        self.difficulty.hard()
        self.game_status = GameStatus()
        self.random_view = ViewGrid(self.difficulty, self.game_status)
        self.random_view.push_left_button(0, 0)
        height3 = self.random_view.height
        width3 = self.random_view.width
        mines3 = len(self.random_view.grid.give_mines_locations())
        results = (width1, height1, mines1, width2,
                   height2, mines2, width3, height3, mines3)
        self.assertEqual(results, (9,9,10,16,16,40,30,16,99))

    def test_if_the_flag_in_a_wrong_places_gives_right_answer(self):
        self.random_view.push_left_button(0, 0)
        mine_locations = self.random_view.grid.give_mines_locations()
        coord_y = None
        coord_x = None
        not_found = True
        while not_found:
            for i in range(self.random_view.height):
                for j in range(self.random_view.width):
                    if not_found and (i,j) not in mine_locations:
                        if self.random_view.coordinates(i, j) == " ":
                            self.random_view.push_right_button(i, j)
                            coord_y = i
                            coord_x = j
                            not_found = False
            if not_found:
                self.game_status = GameStatus()
                self.random_view = ViewGrid(self.difficulty, self.game_status)
        self.random_view.push_left_button(mine_locations[0][0], mine_locations[0][1])
        result = self.random_view.coordinates(coord_y, coord_x)
        self.assertEqual(result, "w")
