import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.15")

    def test_rahan_ottaminen_vahentaa_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_otettaessa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palauttaa_true_jos_rahan_ottaminen_onnistui(self):
        totuusarvo = self.maksukortti.ota_rahaa(5)
        self.assertEqual(totuusarvo, True)
    
    def test_palauttaa_false_jos_rahan_ottaminen_ei_onnistu(self):
        totuusarvo = self.maksukortti.ota_rahaa(11)
        self.assertEqual(totuusarvo, False)