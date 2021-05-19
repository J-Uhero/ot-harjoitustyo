from datetime import datetime
from repositories.score_repository import score_repository


class ScoresService:
    """Vastaa pelin ennätystulostietojen välittämisestä käyttöliittymälle ja
    pelitulosten talletuksesta.
    """
    def __init__(self):
        """Luo uuden ScoreService-olion, jolla on yhteys
        tietokantakomentoihin.
        """
        self.repository = score_repository

    def get_high_scores(self):
        """Palauttaa parhaat pelitulokset vaikeusasteittain.

        Returns:
            tuple: tuple, jossa parametreina kolme listaa tuloksista
            vaikeusasteiden mukaan.
        """
        easy = self.repository.find_high_scores_by_level("easy", 10)
        medium = self.repository.find_high_scores_by_level("medium", 10)
        hard = self.repository.find_high_scores_by_level("hard", 10)
        return easy, medium, hard

    def new_score(self, name, time, level):
        """Aallettaa uuden pelituloksen tietokantaan ja varmistaa,
        että talletettavat tiedot ovat asiamukaiset.

        Args:
            name ("str"): pelaajan nimeä kuvaava merkkisyöte
            time (float): pelin läpäisyyn kulunut aika liukulukuna esitettynä
            level (str): Pelin vaikeustasoa kuvaava merkkijono
        """
        date = datetime.now()
        if len(name) > 10:
            name = name[:10]
        if len(name) == 0:
            name = "untitled"
        self.repository.create_score(name, time, level, date)

    def is_score_a_high_score(self, time, level):
        """Tarkastaa aika- ja vaikeustasotietojen mukaan, onko aika parempi
        kuin tulostietojen kymmenenneksi paras aika, eli mahtuuko uusi aika
        kymmenen parhaan tuloksen joukkoon.

        Args:
            time (float): pelin läpäisyyn kulunut aika liukulukuna esitettynä
            level (str): pelin vaikeustasoa kuvaava merkkijono

        Returns:
            bool: totuusarvo, joka kertoo oliko tulos kymmenennen parhaan joukossa
        """
        high_scores = self.repository.find_high_scores_by_level(level, 10)
        if len(high_scores) < 10:
            return True
        if high_scores[-1].time > time:
            return True
        return False

    def check_ranking_of_a_score(self, time, level):
        """Palauttaa tiedon, monenneksi paras tulos uusi tulos oli.

        Args:
            time (float): peliaikaa sekuntteina liukulukuna esitettynä
            level (str): vaikeustaso merkkijonona esitettynä

        Returns:
            [int]: sijoitusta kuvaava kokonaisluku
        """
        ranking = self.repository.check_ranking_of_a_score(time, level)
        return ranking[0]+1
