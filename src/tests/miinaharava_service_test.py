import unittest
from services.miinaharava_service import Grid, View

class TestView(unittest.TestCase):
    def setUp(self):
        self.view = View(9,9,10)

    def test_the_view_is_empty_at_the_beginning(self):
        empty = True
        for i in self.view.view:
            for j in i:
                if j != " ":
                    empty = False
        self.assertEqual(empty, True)

    def test_if_the_first_openet_square_is_zero(self):
        self.view.push_left_button(4,4)
        content = self.view.coordinates(4,4)
        self.assertEqual(content, "0")
