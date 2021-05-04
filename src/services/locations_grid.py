class Grid:
    """Luokka joka arpoo miinojen sijainnit ja säilöö miinojen ja lukujen
    sijaintitietoja
    """
    def __init__(self, height, width, mines, first_yx):
        """Luokan konstruktori.

        Args:
            height (int): peliruudukon korkeus
            width (int): peliruudukon leveys
            mines (int): miinojen määrä
            first_yx (tuple): y- ja x-koordinaatit ruudun sijainnista, jonka pelaaja
            on ensimmäisenä avannut
        """
        self.width = width
        self.height = height
        self.mines = mines
        self.grid = self.create_grid(self.width, self.height)
        self._mines_locations = []
        self.create_mines(first_yx)

    def create_grid(self, width, height):
        """Luo ruuduton johon tallennetaan miinojen ja numeroiden sijainteja
        ja alustaa ruudukon ruudut tyhjiksi.

        Args:
            width (int): ruudukon leveys
            height (int): ruudukon korkeus

        Returns:
            list: taulukkolista, joka kuvastaa peliruudukon sijaintitietoja
        """
        grid = []
        for i in range(height):
            grid.append([0]*(width))
        return grid

    def create_mines(self, first_yx):
        """Sijoittelee sattumanvaraisesti miinat taulukkoon, niin ettei
        aloituspainalluksen kohtaan ja sen välittömään läheisyyteen sijoitu miinoja

        Args:
            first_yx (tuple): aloituspainalluksen y- ja x-koordinaatit
        """
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
        """Korottaa miinojen ympärillä olevien ruutujen numeroarvoa.

        Args:
            mine_h (int): miinan sijainti korkeussuunnassa eli y-koordinaatin arvo
            mine_w (int): miinan sijainti leveyssuunnassa eli x-koordinaatin arvo
        """
        for i in range(mine_h-1, mine_h+2):
            for j in range(mine_w-1, mine_w+2):
                if self.height > i >= 0 and self.width > j >= 0 and self.grid[i][j] > -1:
                    self.grid[i][j] += 1

    def give_coordinate_value(self, coord_y, coord_x):
        """Palauttaa tiedon, mitä peliruudukon tietyssä ruudussa sijaitsee

        Args:
            coord_y (int): y-koordinaatti
            coord_x (int): x-koordinaatti
        Returns:
            int: peliruudukon sisältöä kuvaava kokonaisluku: -1 on miina, 0 tyhjä ja
            numerot siitä ylöspäin peliruudun numeroita
        """
        return self.grid[coord_y][coord_x]
    
    def give_mines_locations(self):
        """Palauttaa tiedon peliruudukon miinojen sijainnista.

        Returns:
            list: palauttaa listan tupleja, jotka ilmentävät miinojen sijaintien
            y- ja x-koordinaatteja
        """
        return self._mines_locations
