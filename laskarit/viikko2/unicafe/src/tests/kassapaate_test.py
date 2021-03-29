import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(450)

    def test_luodun_kassapaatteen_tiedot_oikein(self):
        alkukassa = self.kassapaate.kassassa_rahaa
        myytyja_edullisia = self.kassapaate.edulliset
        myytyja_maukkaita = self.kassapaate.maukkaat
        self.assertEqual((alkukassa, myytyja_edullisia, myytyja_maukkaita), (100000, 0, 0))

    def test_kateisosto_velottaa_oikein_edullisilla(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtorahat), (100240, 260))

    def test_kateisosto_veloittaa_oikein_maukkailla(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtorahat), (100400, 100))

    def test_kateisosto_kasvattaa_myytyjen_maaraa_edullisilla(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_kasvattaa_myytyjen_maaraa_maukkailla(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahamaara_ei_muutu_jos_kateismaksu_ei_ole_riittava_edullisilla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha), (100000, 200))

    def test_rahamaara_ei_muutu_jos_kateismaksu_ei_ole_riittava_edullisilla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha), (100000, 200))

    def test_edullisten_maara_ei_muutu_jos_kateismaksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_maara_ei_muutu_jos_kateismaksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_veloittaa_oikein_edullisilla_kun_rahaa_tarpeeksi(self):
        toteutuiko = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo, toteutuiko), (210, True))
        
    def test_korttiosto_veloittaa_oikein_maukkailla_kun_rahaa_tarpeeksi(self):
        toteutuiko = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo, toteutuiko), (50, True))

    def test_korttiosto_ei_veloita_edullisilla_kun_rahaa_ei_ole_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        toteutuiko = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo, toteutuiko), (210, False))

    def test_korttiosto_ei_veloita_maukkailla_kun_rahaa_ei_ole_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        toteutuiko = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kortti.saldo, toteutuiko), (50, False))

    def test_korttiosto_kasvattaa_edullisia_kun_rahaa_on_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_kasvattaa_maukkaita_kun_rahaa_on_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_kasvata_edullisia_kun_rahaa_ei_ole_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_ei_kasvata_maukkaita_kun_rahaa_ei_ole_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttilataus_positiivisella_summalla_kasvattaa_arvoa_kortilla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 1450)

    def test_korttilataus_positiivisella_summalla_kasvattaa_rahaa_kassassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_korttilataus_nollaa_pienemmilla_ei_muuta_kortin_arvoa(self):
        palautus = self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual((self.kortti.saldo, palautus), (450, None))

    def test_korttilataus_nollaa_pienemmilla_ei_muuta_rahaa_kassassa(self):
        palautus = self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa, palautus), (100000, None))

