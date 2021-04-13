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

### Dokumentaatio
* [harjoitustyön vaatimusmäärittely](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [harjoitustyön työtuntikirjanpito](https://github.com/J-Uhero/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
