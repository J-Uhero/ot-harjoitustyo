# Miinaharava

## Sovelluksen tarkoitus
Sovelluksessa on tarkoitus toteuttaa perustoiminnallisuudeltaan klassinen Miinaharava-peli.
Pelissä painetaan ruudukon avaamattimia ruutuja ja yritetään kartoittaa niistä saatavilla
numerovihjeillä, missä laudan ruuduissa on miinoja osumatta itse niihin. Pelin läpäisee, kun
kaikki miinat on kartoitettu ja merkattu ja muut ruudut avattu.

## Käyttäjäroolit
* sovelluksessa on vain normaaleja käyttäjärooleja, joilla voi pelata peliä
  ja kirjata omia tuloksia ylös. Erillistä ylläpitokäyttäjäroolia ei tarvittane.

## Toiminnallisuudet
* Peli arpoo miinoja ruudukon eri kohtiin. *tehty*
* Pelaajan ensimmäisenä painamassa peliruudussa ei voi osua vielä miinaan. *tehty*
* Miinojen vieressä olevissa ruuduissa kerrotaan numerolla, montaako miinaa ruutu 
  koskettaa sivuilla tai kulmillansa. *tehty*
* Painettu ruutu paljastaa, onko ruudussa miina, numero vai tyhjää. Ruutuun voi laittaa
  merkin, jos epäilee, että siinä on miina. *tehty*
* Peli loppuu joko kun kaikki miinat on merkattu tai pelaaja osuu miinaan. *tehty **uusi***
* Jos pelaaja saa kaikki miinat merkattua, kirjataan hänen tulos ylös. Pelaaja voi antaa
  oman nimimerkin, jonka lisäksi tallennetaan kauan pelin läpäisy kesti, vaikeustaso ja
  päivämäärä ja kellonaika.
* Pelissä on kello, joka käynnistyy, kun painetaan ensimmäistä ruutua *(lisätty)*
* Pelissä on voi aloittaa uuden pelin käynnistämättä sitä uudestaan (painamalla naamaa) *(lisätty)*

## Toimintaympäristö ja rajoitteet
* Peli toteutetaan Pythonilla (vähintään versio 3.6).
* Pelin tulee toimia Linux- ja MacOS-käyttöjärjestelmillä. Linuxin kohdalla tarkoitetaan
  laitoksen koneita, joissa on cubbli-linux-käyttöjärjestelmä.
* Käyttäjien tiedot tallennetaan paikallisesti tietokantana koneen muistiin.
* Pelillä on graafinen käyttöliittymä, joka muodostaa peliruudukon ja muut tarvittavat
  napit ja valikot (toteutetaan Tkinterillä tai Pygamella).
  
## Kehitysideoita
* Erilaisia vaikeustasoja voi lisätä eli pelaaja voi valita peliruudukon koon ja miinojen määrän.
* Vierekkäisten tyhjien ruutujen ja niiden viereisten numeroruutujen automaattinen
  aukeaminen painettaessa yhtä tyhjää ruutua pelitahdin jouhevoittamiseksi.
* Graafista ulkoasua voi kehittää persoonalliseen suuntaan ja siitä voi tehdä myös osittain 
  asetuksista käsin säädettävän esim. värityksen osalta.
* Kentät voivat poiketa myös muodoltaan.

