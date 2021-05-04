from entities.difficulty import Difficulty
from services.locations_grid import Grid

class ViewGrid:
    """Luokka, joka vastaa tiedosta, mitä eri ruutuja peliruudukossa sijaitsee missäkin
    kohdissa, ja toiminnallisuuksista, jotka vaikuttavat pelinäkymään.
    """
    def __init__(self, difficulty):
        """Luokan konstruktori

        Args:
            difficulty (Difficulty): Tieto pelin vaikeustasosta, joka vaikuttaa 
            pelinäkymätietoja sisältävän taulukon kokoon.
        """
        self.height = difficulty.height()
        self.width = difficulty.width()
        self.mines = difficulty.mines()
        self.flags = difficulty.mines()
        self.view = self.create_view()
        self._first_push = True
        self.grid = None
        self.unopened = self.height * self.width
        self._game_status = "ready"

    def create_view(self):
        """Luo taulukkon, jossa sijaitsee tiedot pelinäkymän ruutujen tilasta
        ja alustaa taulukkoon tiedot aloitusnäkymästä, jossa kaikki ruudut ovat
        avaamattomia.

        Returns:
            [list]: Palauttaa peliruudukkoa kuvaavan listoja sisältävän listan
        """
        view = []
        for i in range(self.height):
            view.append([" "]*(self.width))
        return view

    def coordinates(self, y, x):
        """Palauttaa tiedon, minkälainen ruutu tietystä peliruudukon
        koordinaatista löytyy

        Args:
            y (int): y-koordinaatti
            x (int): x-koordinaatti

        Returns:
            [str]: ruudun sisältöä kuvaava merkkijono
        """
        return self.view[y][x]

    def push_right_button(self, y, x):
        """Muokkaa pelinäkymätietoja, kun tiettyyn peliruudukon koordinaattia on
        painettu hiiren oikealla painikkeella. Oikealla painikkeella lisätään peliruudukkoon
        lippuja, joita kuvaa "f"-merkkijono.

        Args:
            y (int): y-koordinaatti
            x (int): x-koordinaatti

        Returns:
            boolean: tieto, muuttuiko peliruudukko painalluksesta eli saiko
            lipun laitettua ruutuun.
        """
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
        """Muokkaa pelinäkymätietoja, kun tiettyyn peliruudukon koordinaattia on
        painettu hiiren vasemmalla painikkeella. Vasemmalla painikkeella avataan peliruutuja.
        Jos painallus on pelin ensimmäinen, peli luo Grid-luokan kuvaamaan pelin miinojen ja 
        numeroiden sijainteja ja näkymäruudukkoa päivitetään Grid-luokan mukaan.
        "<space>"-merkki kuvaa avaamatonta ruutua, "0" tyhjää ruutua numerot 1-8 merkkijonoina
        kuvaavat numeroruutuja, "x" on miina, "r" punainen miina, johon pelaaja on osunut,
        "f" on lippu ja "w" on väärässä kohtaa ollut lippu.

        Args:
            y (int): y-koordinaatti
            x (int): x-koordinaatti

        Returns:
            boolean: tieto, muuttoiko peliruudukko painalluksesta eli
            saiko ruudun avattua
        """
        if self._first_push:
            self.grid = Grid(self.height, self.width, self.mines, (y,x))
            self.first_push()
        if self.view[y][x] != " ":
            return False 
        value = self.grid.give_coordinate_value(y,x)
        if value == 0:
            self.view[y][x] = "0"
            self.empty_button(y,x)
        elif value == -1:
            self.view[y][x] = "r"
            self.game_over()
            return True
        else:
            self.view[y][x] = str(value)

        self.unopened -= 1
        if self.unopened == 0:
            self.victory()
        return True

    def empty_button(self, y, x):
        """Luokka avaa tyhjän peliruudun ympärillä olevat ruudut

        Args:
            y (int): y-koordinaatti
            x (int): x-koordinaatti
        """
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if 0 <= i < self.height and 0 <= j < self.width:
                    self.push_left_button(i, j)

    def open_remaining_mines(self):
        """Avaa peliruudukon ruudut, joissa sijaitsee miinoja
        """
        for mine_loc in self.grid.give_mines_locations():
            if self.coordinates(mine_loc[0], mine_loc[1]) == " ":
                self.view[mine_loc[0]][mine_loc[1]] = "x"

    def check_false_flags(self):
        """Tarkistaa, onko pelinäkymään laitettu lippuja kohtiin, joissa
        ei sijaitse miinaa.
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.view[i][j] == "f" and \
                   self.grid.give_coordinate_value(i, j) != -1:
                    self.view[i][j] = "w"

    def first_push(self):
        """Funktio, joka ilmoittaa, että pelin ensimmäinen painallus on
        painettu ja peli on käynnistynyt.
        """
        self._first_push = False
        self._game_status = "started"

    def game_over(self):
        """Muuttaa pelitilan häviöksi.
        """
        self._game_status = "game_over"
        self.open_remaining_mines()
        self.check_false_flags()

    def victory(self):
        """Muuttaa pelitilan voitoksi.
        """
        self._game_status = "victory"

    def give_game_status(self):
        return self._game_status

    def give_unopened(self):
        return self.unopened
    
    def give_flags(self):
        return self.flags
