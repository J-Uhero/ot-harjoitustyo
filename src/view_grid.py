from difficulty import Difficulty
from locations_grid import Grid

class ViewGrid:
    def __init__(self, difficulty):
        self.height = difficulty.height()
        self.width = difficulty.width()
        self.mines = difficulty.mines()
        self.flags = difficulty.mines()
        self.view = self.create_view()
        self.first_push = True
        self.grid = None
        self.unopened = self.height * self.width
        self.game_status = None

    def create_view(self):
        view = []
        for i in range(self.height):
            view.append([" "]*(self.width))
        return view

    def coordinates(self, y, x):
        return self.view[y][x]

    def push_right_button(self, y, x):
        if self.view[y][x] == " " and self.flags > 0:
            self.view[y][x] = "f"
            self.flags -= 1
            self.unopened -= 1
            if self.unopened == 0:
                self.victory()
        elif self.view[y][x] == "f":
            self.view[y][x] = " "
            self.flags += 1
            self.unopened += 1
        else:
            return False
        return True

    def push_left_button(self, y, x):
        if self.first_push:
            self.grid = Grid(self.height, self.width, self.mines, (y,x))
            self.first_push = False
        elif self.view[y][x] != " ":
            return False 
        value = self.grid.give_coordinate_value(y,x)
        if value == 0:
            self.view[y][x] = "0"
            self.empty_button(y,x)
        elif value == -1:
            self.view[y][x] = "x"
            self.game_over()
            return True
        else:
            self.view[y][x] = str(value)

        self.unopened -= 1
        if self.unopened == 0:
            self.victory()
        return True

    def empty_button(self, y, x):
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if 0 <= i < self.height and 0 <= j < self.width:
                    self.push_left_button(i, j)

    def open_remaining_mines(self):
        for mine_loc in self.grid.give_mines_locations():
            if self.coordinates(mine_loc[0], mine_loc[1]) == " ":
                self.view[mine_loc[0]][mine_loc[1]] = "x"

    def game_over(self):
        self.game_status = "game_over"
        self.open_remaining_mines()

    def victory(self):
        self.game_status = "victory"

    def give_game_status(self):
        return self.game_status

    def give_unopened(self):
        return self.unopened
    
    def give_flags(self):
        return self.flags
