# Ohjelmistotekniikan harjoitustyö
## Miinaharava
Miinaharava-pelissä on tarkoitus avata peliruudukon ruutuja ja niistä saatavien numerovihjeiden avulla kartoittaa peliruudukossa olevat miinat. Ruutujen numerovihjeet kertovat, kuinka monta miinaa ruudun ympärillä sijaitsee. Miinojen kohdalle on asetettava lippuja, joita on käytettävänä yhtä monta kuin miinoja on. Pelin läpäisee, kun kaikki miinat saa kartoitettua ja muut ruudut avattua osumatta itse miinaan.

### Dokumentaatio
* [harjoitustyön vaatimusmäärittely](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [harjoitustyön työtuntikirjanpito](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [arkkitehtuurikuvaus](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [käyttöohje](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
* [testausdokumentti](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/testikattavuus.md)

### Komentorivitoiminnot

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
Kattavuusraportin voi tulostaa komentoriville komennolla:
```bash
poetry run invoke coverage-report
```
HTML-kattavuusraportin saa luotua komennolla:
```bash
poetry run invoke coverage-report-html
```
Pylint-arvioinnin koodista saa komennolla:
```bash
poetry run invoke lint
```

### Versiot
[final (loppupalautus)](https://github.com/J-Uhero/ot-harjoitustyo/releases/tag/viikko7)

[first release](https://github.com/J-Uhero/ot-harjoitustyo/releases/tag/viikko5)

[2th release](https://github.com/J-Uhero/ot-harjoitustyo/releases/tag/viikko6)

### Deadlinen jälkeinen huomio
Ikäväkseni huomasin, että ohjelmaan oli huolimattomuuttani jäänyt bugi, joka aiheuttaa ohjelman kaatumisen, kun ohjelman ScoresService-luokka hakee tietokannasta pelaajan sijoitusta tietokannan ollessa tyhjä. Buginen funktio päätyi aiemmin ongelmatta toimineen ohjelman käyttöön vasta loppumetreillä luokan testien päivittelyn yhteydessä ja tekemästäni testiluokastanikin on testattu funktion toimivuus vain silloin, kun siihen on jo tallennettu tietoja. Tein nyt jälkikäteen korjauksen ohjelmakoodiini, koska halusin ohjelmastani toimivan version ja mainita huomanneeni virheen, vaikkakin liian myöhään. Teen nyt uuden releasen tähän alle tiedostaen toki, että varsinainen loppupalautukseni on se, joka on arvioinnin kohteena.

[korjattu versio 19.05.2021](https://github.com/J-Uhero/ot-harjoitustyo/releases/tag/korjattu_versio_19.5.2021)
