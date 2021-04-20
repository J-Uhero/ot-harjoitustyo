from view_grid import ViewGrid
from difficulty import Difficulty

# tämän tekstikäyttöliittymän on tarkoitus olla väliaikainen ratkaisu ohjelmalogiikan testaamiseen,
# ennen kuin saan tehtyä kokonaisuudessaan toimivan graafisen käyttöliittymän.

class Ui:
    def __init__(self):
        self.game_view = None
        self.difficulty = Difficulty()
        self.height = self.difficulty.height()
        self.width = self.difficulty.width()

    def start(self):
        self.game_view = ViewGrid(self.difficulty)
        self.play_game()

    def play_game(self):
        print()
        print("miinaharava")
        print(f"size of grid: {self.width} x {self.height}")
        self.main_loop()

    def print_game_viewgrid(self):
        first_line = "  |"
        for i in range(self.width):
            first_line += f" {i} |"
        print(first_line)
        line = "---" + "----" * self.width
        print(line)

        for i in range(self.height):
            row = f"{i} |"
            for j in range(self.width):
                content = self.game_view.coordinates(i,j)
                row += f" {content} |"
            print(row)
            print(line)

    def main_loop(self):
        while True:
            print()
            print("1: new game")
            print("0: quit")
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.game_loop()

    def ask_coordinates(self):
        try:
            row = int(input("give an index of a row: "))
            seg = int(input("give an index of a column: "))
            return (row, seg)
        except:
            print("invalid command")

    def game_loop(self):
        while True:
            print()
            print("flags left:", self.game_view.give_flags())
            print("unopened squares:", self.game_view.give_unopened())
            print()
            self.print_game_viewgrid()
            if self.status() is False:
                break
            print()
            print("1: open a square")
            print("2: place/displace a flag")
            print("0: exit")
            command = input("command: ")

            if command == "0":
                return
            coord_x, coord_y = self.ask_coordinates()
            if command == "1":
                self.game_view.push_left_button(coord_x, coord_y)
            if command == "2":
                self.game_view.push_right_button(coord_x, coord_y)

    def status(self):
        status = self.game_view.give_game_status()
        if status == "game_over":
            print("game over")
            return False
        if status == "victory":
            print("victory!")
            return False
        return True
