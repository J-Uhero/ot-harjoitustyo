import pygame as pg
from ui.game_loop import GameLoop
from difficulty import Difficulty

def main():
    difficulty = Difficulty()
    #difficulty.medium()
    square_size = 30

    pg.init()

    display = None  
    gameloop = GameLoop(display, difficulty, square_size)
    gameloop.start()

if __name__ == "__main__":
    main()
