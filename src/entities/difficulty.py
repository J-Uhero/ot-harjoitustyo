class Difficulty:
    """Luokka, joka kuvaa pelin vaikeustasoa ja sisältää vaikeustasoon
    vaikuttavia muuttujia ja niiden parametreja.
    """
    def __init__(self):
        """Konstruktori, joka alustaa vaikeustasoa ilmentävät muuttujat
        asettaa oletusarvoisesti vaikeustason helpoksi.
        """
        self._height = None
        self._width = None
        self._mines = None
        self._degree = None
        self.easy()

    def height(self):
        return self._height

    def width(self):
        return self._width

    def mines(self):
        return self._mines

    def degree(self):
        return self._degree

    def easy(self):
        self._height = 9
        self._width = 9
        self._mines = 10
        self._degree = "easy"

    def medium(self):
        self._height = 16
        self._width = 16
        self._mines = 40
        self._degree = "medium"

    def hard(self):
        self._height = 16
        self._width = 30
        self._mines = 99
        self._degree = "hard"
