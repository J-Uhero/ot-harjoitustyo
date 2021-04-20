class Grid:
    def __init__(self, height, width, mines, first_yx):
        self.width = width
        self.height = height
        self.mines = mines
        self.grid = self.create_grid(self.width, self.height)
        self._mines_locations = []
        self.create_mines(first_yx)

    def create_grid(self, width, height):
        grid = []
        for i in range(height):
            grid.append([0]*(width))
        return grid

    def create_mines(self, first_yx):
        from random import randint
        empty_space_y = [first_yx[0]-1, first_yx[0], first_yx[0]+1]
        empty_space_x = [first_yx[1]-1, first_yx[1], first_yx[1]+1]
        mines_left = self.mines
        while mines_left > 0:
            mine_location = (randint(0, self.height-1), randint(0, self.width-1))
            if self.grid[mine_location[0]][mine_location[1]] != -1:
                if mine_location[0] not in empty_space_y or mine_location[1] not in empty_space_x:
                    self.grid[mine_location[0]][mine_location[1]] = -1
                    self._mines_locations.append(mine_location)
                    self.raise_numbers(mine_location[0],mine_location[1])
                    mines_left -= 1

    def raise_numbers(self, mine_h: int, mine_w: int):
        for i in range(mine_h-1, mine_h+2):
            for j in range(mine_w-1, mine_w+2):
                if self.height > i >= 0 and self.width > j >= 0 and self.grid[i][j] > -1:
                    self.grid[i][j] += 1

    def give_coordinate_value(self, coord_y, coord_x):
        return self.grid[coord_y][coord_x]
    
    def give_mines_locations(self):
        return self._mines_locations
