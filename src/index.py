import ui.miinaharava_teksti_ui as teksti_ui
import pygame_index

def main():

    print("haluatko pelata graafisella käyttöliittymällä vai tekstikäyttöliittymällä?")
    print("1: graafinen")
    print("2: teksti")
    command = input("komento: ")
    if command == "1":
        pygame_index.main()
    elif command == "2":
        ui = teksti_ui.Ui()  
        ui.start()

if __name__ == "__main__":
    main()