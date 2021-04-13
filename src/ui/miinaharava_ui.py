from tkinter import Tk, ttk, Button
import tkinter as tk
#import pygame
from services.miinaharava_service import Grid, View
from functools import partial

class Ui:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._height = 9
        self._width = 9
        self._difficulity = None
        self._game = None
        self._frame = tk.Frame(master=self._root)
        self._frame.pack()

    def start(self):
        #self.current_view = self.difficulty_view()
        #self.difficulty_view()
        self.new_game()

    def difficulty_view(self):
        label = ttk.Label(master=self._root, text="Set the digree of dificulty:")
        easy_button = ttk.Radiobutton(master=self._root, text="Easy (9x9 grid and 10 mines)")
        medium_button = ttk.Radiobutton(master=self._root, text="Medium")
        label.pack()
        easy_button.pack()
        medium_button.pack()

    def new_game(self):
        self.game = View(9,9,10)
        self.game.create_view()
        self.create_game_view()
        #self.test_button()

    def test_button(self):
        def handle_click(event):
            print("The button was clicked!")

        button = tk.Button(text="Click me!")

        button.bind("<Button-2>", handle_click)
        button.pack()

    def create_game_view(self):
        def right_button_pushed(event):
                    #self.game.push_right_button(y, x)
                    print("right")
        def left_button_pushed(event):
                    #self.game.push_left_button(y, x)
                    print("left")
        for i in range(self._height):
            for j in range(self._width):
                #def handler1(event, self=self, i=i, j=j):
                #    return self.left_button_pushed(event, i, j)
                button = tk.Button(master=self._frame, width=4, height=2, text=f"{self.game.coordinates(i,j)}")
                button.grid(row=i, column=j, sticky="nsew")
                button.pack()
                button.bind("<button-1>", left_button_pushed)
                button.bind("<button-2>", right_button_pushed)
        
                #self._frame.focus_set()

    #def left_button_pushed(self, event):
        #self.game.push_left_button(y, x)
    #    print("jee")

    #def right_button_pushed(self, event):
        #self.game.push_right_button(y, x)
    #    print("jee jee")


def main():
    window = Tk()
    window.title("Miinaharava")
    ui = Ui(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
