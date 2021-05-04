
### Ohjeet
Peli käynnistämiseen tarvitaan Poetry. Mikäli Poetryä ei ole entuudestaan asennettuna, sen asentamiseen löydät ohjeet vaikka [kurssimateriaalista](https://ohjelmistotekniikka-hy.github.io/python/poetry). Voit tarkistaa, onko poetry asennettuna komennolla "poetry --version".

Peli vaatii toimiakseen Pythonista vähintään [version 3.6](https://www.python.org/downloads/) ja se käyttää Pythonin Pygame ja Pygame Gui -kirjastoja. Voit asentaa ohjelman riippuvuudet poetryn avulla komennolla:
```bash
poetry install
```
Kun pelin käynnistää pelin suorituskomennolla ("poetry run invoke start"), voi aluksi valita, haluaako peliä pelata graafisella käyttöliittymällä vai tekstikäyttöliittymällä. Komennolla **"1"** voi käynnistää graafisen käyttöliittymän ja komennolla **"2"** voi pelata tekstikäyttöliittymällä. Pelaaminen graafisella käyttäliittymällä on suositeltavaa. Peli päättyy, kun kaikki pommit on kartoitettu lipuilla tai kun pelaaja osuu miinaan. 
