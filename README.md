# Ohjelmistotekniikan harjoitustyö
## Miinaharava
Miinaharava-pelissä on tarkoitus avata peliruudukon ruutuja ja niistä saatavien numerovihjeiden avulla kartoittaa peliruudukossa olevat miinat. Ruutujen numerovihjeet kertovat, kuinka monta miinaa ruudun ympärillä sijaitsee. Miinojen kohdalle on asetettava lippuja, joita on käytettävänä yhtä monta kuin miinoja on. Pelin läpäisee, kun kaikki miinat saa kartoitettua ja muut ruudut avattua osumatta itse miinaan.

###Versiot
[first release](https://github.com/J-Uhero/ot-harjoitustyo/releases/tag/viikko5)

Peli suoritetaan komennolla:
```bash
poetry run invoke start
```
Testien ajaminen onnistuu komennolla:
```bash
poetry run invoke test
```
Teskikattavuutta voi testata komennolla:
```bash
poetry run invoke coverage
```
Kattavuusraportin voi tulostaa komennolla:
```bash
poetry run invoke coverage-report
```
Pylint-arvioinnin koodista saa komennolla:
```bash
poetry run invoke lint
```
### Dokumentaatio
* [harjoitustyön vaatimusmäärittely](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [harjoitustyön työtuntikirjanpito](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [arkkitehtuurikuvaus](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Ohjeet
Peli käynnistämiseen tarvitaan Poetry. Mikäli Poetryä ei ole entuudestaan asennettuna, sen asentamiseen löydät ohjeet vaikka [kurssimateriaalista](https://ohjelmistotekniikka-hy.github.io/python/poetry). Voit tarkistaa, onko poetry asennettuna komennolla "poetry --version".

Peli vaatii toimiakseen Pythonista vähintään version 3.6 ja se käyttää Pythonin Pygame ja Pygame Gui -kirjastoja. Voit asentaa ohjelman riippuvuudet poetryn avulla komennolla:
```bash
poetry install
```
Kun pelin käynnistää pelin suorituskomennolla ("poetry run invoke start"), voi aluksi valita, haluaako peliä pelata graafisella käyttöliittymällä vai tekstikäyttöliittymällä. Komennolla **"1"** voi käynnistää graafisen käyttöliittymän ja komennolla **"2"** voi pelata tekstikäyttöliittymällä. Pelaaminen graafisella käyttäliittymällä on suositeltavaa. Peli päättyy, kun kaikki pommit on kartoitettu lipuilla tai kun pelaaja osuu miinaan. 
