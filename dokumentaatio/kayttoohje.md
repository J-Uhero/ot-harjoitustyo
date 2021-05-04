
### Ohjeet
Peli käynnistämiseen tarvitaan Poetry. Mikäli Poetryä ei ole entuudestaan asennettuna, sen asentamiseen löydät ohjeet vaikka [OhTe:n kurssimateriaalista](https://ohjelmistotekniikka-hy.github.io/python/poetry). Voit tarkistaa, onko poetry asennettuna komennolla "poetry --version".

Peli vaatii toimiakseen Pythonista vähintään [version 3.6](https://www.python.org/downloads/) ja se käyttää Pythonin Pygame ja Pygame Gui -kirjastoja. Voit asentaa ohjelman riippuvuudet poetryn avulla komennolla:
```bash
poetry install
```
Peli käynnistetään suorituskomennolla:
```bash
poetry run invoke start
```

## Pelaaminen

Suorituskomento avaa pelinäkymän:

![pelinakyma](./kuvat/miinaharava-nakyma-viikko6-easy.png)

Pelinäkymän vasempaa yläkulman kohtaa, jossa lukee "easy", painamalla avautuu on valikko, josta voi vaihtaa pelin vaikeusastetta. Vaikeusaste vaikuttaa peliruudukon kokoon ja miinojen määrään.

Pelissä pelaajan tulee avata hiirellä peliruudukon ruutuja. Ensimmäinen painallus hiiren vasemmalla näppäimellä käynnistää pelin. Pelin numeroruudut kertovat, kuinka montaa eri miinaa ruudun sivut ja kulmat koskettavat. Näiden numerovihjeiden avulla pelaajan tulee päätellä, missä pelin ruuduissa miinat sijaitsevat. Pelaajan tulee asettaa lippuja ruutuihin, joissa pelaaja epäilee miinojen olevan. Lippuja on käytettävissä yhtä monta, kuin miinoja on. Asettaminen tapahtuu hiiren oikeallla näppäimellä tai hiiren vasemmalla näppäimellä samalla, kun ALT-näppäin on painettuna pohjaan. Pelaajaaja häviää pelin avattuaan ruudun, jossa sijaitsee miina ja läpäisee pelin kartoitettuaan lipuilla kaikki miinat ja avattuaan muut ruudut. Pelin voi käynnistää uudestaan "new game"-näppäimestä.
