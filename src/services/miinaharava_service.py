class Grid:
    def __init__(self, height, length, mines, first_yx):
        self.length = length
        self.height = height
        self.mines = mines
        self.grid = self.create_grid(self.length, self.height)
        self.create_mines(first_yx)

    def create_grid(self, l, h):
        g = []
        for i in range(h):
            g.append([0]*(l))
        return g

    def create_mines(self, first_yx):
        from random import randint
        empty_space_y = [first_yx[0]-1, first_yx[0], first_yx[0]+1]
        empty_space_x = [first_yx[1]-1, first_yx[1], first_yx[1]+1]
        mines_left = self.mines
        while mines_left > 0:
            mine_location = (randint(0, self.height-1), randint(0, self.length-1))
            if self.grid[mine_location[0]][mine_location[1]] != -1:
                if mine_location[0] not in empty_space_y or mine_location[1] not in empty_space_x:
                    self.grid[mine_location[0]][mine_location[1]] = -1
                    self.raise_numbers(mine_location[0],mine_location[1])
                    mines_left -= 1
        
    def raise_numbers(self, mine_h: int, mine_l: int):
        for i in range(mine_h-1, mine_h+2):
            for j in range(mine_l-1, mine_l+2):
                if self.height > i >= 0 and self.length > j >= 0 and self.grid[i][j] > -1:
                    self.grid[i][j] += 1

    def give_coordinate_value(self, y, x):
        return self.grid[y][x]

    def draw(self):
        for r in self.grid:
            print(r)


class View:
    def __init__(self, height: int, length: int, mines: int):
        self.h = height
        self.l = length
        self.mines = mines
        self.flags = mines
        self.view = self.create_view()
        self.first_push = True
        self.grid = None
        self.unopened = height * length
        self.game_ended_to_mine = False
        self.game_ended_to_victory = False
    
    def create_view(self):
        view = []
        for i in range(self.h):
            view.append([" "]*(self.l))
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
            self.grid = Grid(self.h, self.l, self.mines, (y,x))
            self.first_push = False
        elif self.view[y][x] != " ":
            return False 
        value = self.grid.give_coordinate_value(y,x)
        if value == 0:
            self.view[y][x] = "0"
            self.empty_button(y,x)
        elif value == -1:
            self.view[y][x] = "x"
            self.game_ended_to_mine = True
            return True
        else:
            self.view[y][x] = str(value)

        self.unopened -= 1
        if self.unopened == 0:
            self.game_ended_to_victory = True
        return True

    def empty_button(self, y, x):
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if 0 <= i < self.h and 0 <= j < self.l:
                    self.push_left_button(i, j)
    
    def game_over(self):
        return self.game_ended_to_mine
    
    def victory(self):
        return self.game_ended_to_victory

    def give_unopened(self):
        return self.unopened
    
    def give_flags(self):
        return self.flags
    
#if __name__ == "__main__":
    #game = View(9,9,10)
    #for i in game.view:
    #    print(i)
