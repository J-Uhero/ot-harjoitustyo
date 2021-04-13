from services.miinaharava_service import View

# tämän tekstikäyttöliittymän on tarkoitus olla väliaikainen ratkaisu ohjelmalogiikan testaamiseen,
# ennen kuin saan tehtyä toimivan graafisen käyttöliittymän.

class Ui:
    def __init__(self):
        self.game_view = None
        self.height = 9
        self.width = 9

    def start(self):
        self.game_view = View(self.height, self.width, 10)
        self.play_game()

    def play_game(self):
        print()
        print("miinaharava")
        print(f"size of grid: {self.width} x {self.height}")
        self.main_loop()
    
    def print_game_viewgrid(self):
        line = "---" + "----" * self.width
        print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
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
                return
            elif command == "1":
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
            print()
            print("1: open a square")
            print("2: place/displace a flag")
            print("0: exit")
            command = input("command: ")

            if command == "0":
                return
            elif command == "1":
                x, y = self.ask_coordinates()
                self.game_view.push_left_button(x, y)
            elif command == "2":
                x, y = self.ask_coordinates()
                self.game_view.push_right_button(x, y)

            if self.game_view.game_over():
                print()
                self.print_game_viewgrid()
                print()
                print("oh! you hit to a mine! game over")
                return
            if self.game_view.victory():
                print()
                self.print_game_viewgrid()
                print()
                print("congratulations! you win!")
                return