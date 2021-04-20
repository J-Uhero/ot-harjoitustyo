import pygame as pg
from view_grid import ViewGrid
# from game_view import GameView
from game_loop import GameLoop
from difficulty import Difficulty

def main():
    difficulty = Difficulty()
    height = difficulty.height()
    width = difficulty.width()
    square_size = 30
    display_height = height * square_size
    display_width = width * square_size

    pg.init()
    display = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption("Miinaharava")
    # display.fill((0,0,0))
    # pg.display.flip()
    # gameview = GameView(difficulty, square_size)
    gameloop = GameLoop(display, difficulty, square_size)
    gameloop.start()

if __name__ == "__main__":
    main()
