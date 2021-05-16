import pygame as pg
from services.view_grid import ViewGrid
from entities.square import Square
from entities.clock import Clock
from status import Status

class GameView:
    """Luokka vastaa pelinäkymän spritejen ylläpidosta, pelin jatkuvuudesta
    ja välittää käyttöliittymän painallukset peliruudukkoa
    ylläpitävälle ViewGrid-luokalle.
    """
    def __init__(self, difficulty, square_size, status):
        """[summary]

        Args:
            difficulty (Difficulty): Pelin vaikeustasoa kuvastava luokka.
            square_size (int): Peliruudukon yhden ruudun leveys/korkeus.
            status (GameStatus): Luokka, joka välittää tietoa pelin tilasta
            muille luokille.
        """
        self._difficulty = difficulty
        self._square_size = square_size
        self._sprites = pg.sprite.Group()
        self._game_clock = Clock()
        self.game_status = status
        self.new_game()
        self._initialized_sprites()
        self._continue_game = True

    def new_game(self):
        """Alustaa uuden pelin asettamalla kellon ja pelistatuksen
        vastaamaan alkavaa peliä ja luo uuden peliruudukon.
        """
        self._game_clock.reset()
        self.game_status.set_status(Status.READY)
        self._grid = ViewGrid(self._difficulty, self.game_status)
        self._initialized_sprites()
        self._continue_game = True

    def _initialized_sprites(self):
        """Päivittää pelin spritet peliruudukon tietojen mukaan.
        """
        self._sprites.empty()
        for y in range(self._difficulty.height()):
            for x in range(self._difficulty.width()):
                square_type = self._grid.coordinates(y, x)
                self._sprites.add(Square(y, x, square_type, self._square_size))

    def push_button(self, pos_x, pos_y, button):
        """Välittää tiedot napin painalluksesta peliruudukolle ja käynnistää
        pelikellon ensimmäisen painalluksen yhteydessä.

        Args:
            pos_x (int): painalluksen kohta näyttöliittymän pelialustan x-akselilla
            pos_y (int): painalluksen kohta näyttöliittymän pelialustan y-akselilla
            button ("str"]): tieto, onko oikean vai vasemman napin painallus
        """
        if self.game_status.get_status() == Status.READY:
            self._game_clock.start()
        if self._continue_game:
            coord_y = ((pos_x) // self._square_size)
            coord_x = ((pos_y) // self._square_size)
            if button == "left":
                self._grid.push_left_button(coord_x, coord_y)
            if button == "right":
                self._grid.push_right_button(coord_x, coord_y)
            self.check_status()
        self._initialized_sprites()

    def check_status(self):
        """Tarkistaa pelitilan ja pysäyttää pelin, jos tarpeen.
        """
        if self.game_status.get_status() == Status.GAMEOVER:
            self._game_clock.stop()
            self._continue_game = False
        if self.game_status.get_status() == Status.VICTORY:
            self._continue_game = False
            self._game_clock.stop()

    def pause(self):
        """Pysäyttää pelin.
        """
        if self._continue_game:
            self._continue_game = False

    def stop_pause(self):
        """Poistaa pelin pysäytyksen.
        """
        if not self._continue_game:
            self._continue_game = True

    def give_time(self):
        """Palauttaa pelikellon ajankohdan sekuntteina.

        Returns:
            int: pelikellon aika sekunttien tarkkuudella
        """
        return self._game_clock.give_time_in_seconds()

    def give_exact_time(self):
        """Palauttaa pelikellon täsmällisen ajankohdan

        Returns:
            float: pelikellon täsmällinen aika
        """
        return self._game_clock.give_exact_time()

    def give_flags(self):
        """Palauttaa pelin lippujen jäljelläolevan määrän.

        Returns:
            int: pelin lippujen käytettävissä oleva määrä
        """
        return self._grid.give_flags()
