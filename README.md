# Ohjelmistotekniikan harjoitustyö
## Miinaharava
Miinaharava-pelissä on tarkoitus avata peliruudukon ruutuja ja niistä saatavien numerovihjeiden avulla kartoittaa peliruudukossa olevat miinat. Ruutujen numerovihjeet kertovat, kuinka montaa eri miinaa ruudun ympärillä sijaitsee, ja miinojen kohdalle on asetettava lippuja, joita on käytettävänä yhtä monta kuin on miinoja. Pelin läpäisee, kun kaikki miinat saa kartoitettua ja muut ruudut avattua osumatta itse miinaan.

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
* [Arkkitehtuurikuvaus](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Ohjeet
Kun pelin käynnistää pelin suorituskomennolla, voi aluksi valita, haluaako peliä pelata graafisella käyttöliittymällä vai tekstikäyttöliittymällä. Komennolla **"1"** voi käynnistää graafisen käyttöliittymän ja komennolla **"2"** voi pelata tekstikäyttöliittymällä. Graafinen käyttöliittymä käyttää toimiakseen pygame-kirjastoa, jonka voi asentaa komennolla **"pip3 install pygame"**, jos sitä ei ole valmiiksi asennettuna. Peli päättyy, kun kaikki pommit on kartoitettu lipuilla tai kun pelaaja osuu miinaan. Graafista käyttöliittymää käyttäessä, peli tulee käynnistää tällöin uudestaan, jos haluaa jatkaa pelaamista. Tekstikäyttöliittymän on tarkoitus olla vain väliaikainen ratkaisu, mutta pidän sen pelissä toistaiseksi mukana, vaikkei sitä löytyne lopullisesta pelistä. 
