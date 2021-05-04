# Ohjelmistotekniikan harjoitustyö
## Miinaharava
Miinaharava-pelissä on tarkoitus avata peliruudukon ruutuja ja niistä saatavien numerovihjeiden avulla kartoittaa peliruudukossa olevat miinat. Ruutujen numerovihjeet kertovat, kuinka monta miinaa ruudun ympärillä sijaitsee. Miinojen kohdalle on asetettava lippuja, joita on käytettävänä yhtä monta kuin miinoja on. Pelin läpäisee, kun kaikki miinat saa kartoitettua ja muut ruudut avattua osumatta itse miinaan.

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
* [käyttöohje](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

### Versiot
[first release](https://github.com/J-Uhero/ot-harjoitustyo/releases/tag/viikko5)
