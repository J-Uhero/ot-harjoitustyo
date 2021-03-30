# Miinaharava

## Sovelluksen tarkoitus
Sovelluksessa on tarkoitus toteuttaa perustoiminnallisuudeltaan klassinen Miinaharava-peli.
Pelissä painetaan ruudukon ruutuja ja yritetään kartoittaa niistä saatavilla
numerovihjeillä, missä laudan ruuduissa on miinoja osumatta itse sellaiseen.

## Käyttäjäroolit
* sovelluksessa on vain normaaleja käyttäjärooleja, joilla voi pelata peliä
  ja kirjata omia tuloksia ylös. Erillistä ylläpitokäyttäjäroolia ei tarvita.

## Toiminnallisuudet
* Käyttäjä voi valita pelin vaikeustason eli peliruudukon koon ja miinojen määrän.
* Peli arpoo miinoja ruudukon eri kohtiin.
* Pelaajan ensimmäisenä painamassa peliruudussa ei voi osua vielä miinaan.
* Miinojen vieressä olevissa ruuduissa kerrotaan numerolla, montaako miinaa ruutu
  koskettaa sivuilla tai kulmillansa.
* Painettu ruutu paljastaa, onko ruudussa miina, numero vai tyhjää. Ruutuun voi laittaa
  merkin, jos epäilee, että siinä on miina.
* Peli loppuu joko kun kaikki miinat on merkattu tai pelaaja osuu miinaan. 
* Jos pelaaja saa kaikki miinat merkattua, kirjataan hänen tulos ylös. Pelaaja voi antaa
  oman nimimerkin, jonka lisäksi tallennetaan kauan pelin läpäisy kesti, vaikeustaso ja
  päivämäärä ja kellonaika.

## Toimintaympäristö ja rajoitteet
* Peli toteutetaan Pythonilla (vähintään versio 3.6).
* Pelin tulee toimia Linux- ja MacOS-käyttöjärjestelmillä. Linuxin kohdalla tarkoitetaan
  laitoksen koneita, joissa on cubbli-linux-käyttöjärjestelmä.
* Käyttäjien tiedot tallennetaan paikallisesti tietokantana koneen muistiin.
* Pelillä on graafinen käyttöliittymä, joka muodostaa peliruudukon ja muut tarvittavat
  napit ja valikot (toteutetaan Tkinterillä tai Pygamella).

