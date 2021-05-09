import pygame as pg
from ui.game_loop import GameLoop
from entities.difficulty import Difficulty

def main():
    difficulty = Difficulty()
    square_size = 30

    pg.init()
    gameloop = GameLoop(difficulty, square_size)
    gameloop.start()

if __name__ == "__main__":
    main()