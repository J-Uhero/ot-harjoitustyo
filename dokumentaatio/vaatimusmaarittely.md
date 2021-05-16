# Miinaharava

## Sovelluksen tarkoitus
Sovelluksessa on tarkoitus toteuttaa perustoiminnallisuudeltaan klassinen Miinaharava-peli.
Pelissä painetaan ruudukon avaamattimia ruutuja ja yritetään kartoittaa niistä saatavilla
numerovihjeillä, missä laudan ruuduissa on miinoja osumatta itse niihin. Pelin läpäisee, kun
kaikki miinat on kartoitettu ja merkattu ja muut ruudut avattu.

## Käyttäjäroolit
* sovelluksessa on vain normaaleja käyttäjärooleja, joilla voi pelata peliä
  ja kirjata omia tuloksia ylös.
  
## Näkymä
* Pelissä on kokoaijan näkyvillä pelinäkymä, jonka koko riippuu vaikeustasosta. Alussa Peli alkaa easy-vaikeustasolla, jonka peliruudukko on 9x9-kokoinen. Näkymässä on lisäksi ylä- ja alapaneelit, joissa näkyy tietoja pelin kulusta ja sijaitsee napit uuden pelin käynnistämiseen, huipputulosten katsomiseen ja pelin vaikeustason valitsemiseen. Pelin huipputulokset aukeavat scores-painikkeesta painaessa pelinäkymän päälle omaan ilmoitusikkunaan, jonka voi klikata ruksista pois. Lisäksi pelin läpäisyn yhteydessä aukeaa oma ikkuna, jossa lukee pelin läpäisyyn kulunut aika, vaikeustaso ja mahdollinen sijoitus. Tämän saa myös ruksilla suljettuna tai sijoittuessa 10 parhaan joukkoon, myös nimimerkin antamisen yhteydestä painamalla tekstisyötössä koneen enter-painiketta tai sen vieressä olevaa käyttöliittymän enter-painiketta.

## Toiminnallisuudet
* Peli arpoo miinoja ruudukon eri kohtiin.
* Pelaajan ensimmäisenä painamassa peliruudussa ei voi osua vielä miinaan.
* Miinojen vieressä olevissa ruuduissa kerrotaan numerolla, montaako miinaa ruutu 
  koskettaa sivuilla tai kulmillansa.
* Painettu ruutu paljastaa, onko ruudussa miina, numero vai tyhjää. Ruutuun voi laittaa
  lippumerkin, jos epäilee, että siinä on miina.
* Tyhjää ruutua painettaessa aukeaa myös sen vieressä olevat tyhjät- ja numeroruudut.
* Peli loppuu joko kun kaikki miinat on merkattu tai pelaaja osuu miinaan.
* Jos pelaaja saa kaikki miinat merkattua, kirjataan hänen tulos ylös, jos peliaika on kymmenen parhaan ajan joukossa vaikeustasokohtaisesti. Pelaaja voi antaa
  oman nimimerkin, joka tallennetaan ja näkyy hupputulosten joukossa ajan kanssa.
* Pelaaja voi katsoa huipputuloksia pelinäkymässä olevaa nappia painamalla.
* Pelissä on kello, joka käynnistyy, kun avataan ensimmäinen ruutu.
* Pelissä on voi aloittaa uuden pelin nappia painamalla käynnistämättä koko sovellusta uudestaan.
* Kun pelaaja osuu miinaa, peli näyttää, jos jokin lippu oli paikassa, jossa ei ollut miinaa.
* Pelaaja voi vaihtaa pelatessa vaikeustasoja, jotka vaikuttavat ruudukon kokoon ja miinojen määrään: helppo (ruutuja 9x9, miinoja 10), keskivaikea (ruutuja 16x16, miinoja 40) ja vaikea (ruutuja 30x16, miinoja 99).

## Toimintaympäristö ja rajoitteet
* Peli vaatii toimiakseen Pythonista vähintään version 3.6.
* Pelin toimii Cubli-Linux- ja MacOS-käyttöjärjestelmillä.
* Käyttäjien tiedot tallennetaan paikallisesti tietokantana koneen muistiin.
* Pelillä on graafinen käyttöliittymä, joka muodostaa peliruudukon ja muut tarvittavat
  napit ja valikot. Käyttöliittymä on toteutettu Pygame ja Pygame Gui -kirjastoja hyödyntäen.
