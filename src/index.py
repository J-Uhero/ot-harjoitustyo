import tkinter
#from ui.miinaharava_ui import Ui
import ui.miinaharava_teksti_ui as teksti_ui

def main():
    #window = tkinter.Tk()
    #window.title("Miinaharava")
    #ui = Ui(window)
    #ui.start()
    #window.mainloop()
    
    #tarkoitukseni on luoda ohjelmaan graafinen käyttöliittymä, mutten ole vielä saanut sitä tehtyä:
    #ongelmia oli yrittäessäni tehdä tkinterillä kahden loopin sisällä kahden eri funktionaalisuuden nappuloita.
    #tein nyt ohjelmalogiikan testaamista varten yksinkertaisen tekstikäyttöliittymän, mutta sitä ei ole tarkoitus
    #sisällyttää lopulliseen ohjelmaan.

    ui = teksti_ui.Ui()
    ui.start()

if __name__ == "__main__":
    main()