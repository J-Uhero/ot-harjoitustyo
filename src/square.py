import pygame as pg
import os

pic_names = {" ": "unopened_grey.png", "0": "empty_grey.png", "1": "one_grey.png",
             "2": "two_grey.png", "3": "three_grey.png", "4": "four_grey.png",
             "5": "five_grey.png", "6": "six_grey.png", "7": "seven_grey.png",
             "8": "eight_grey.png", "x": "mine_grey.png", "f": "flag_grey.png",
             "r": "mine_red.png"}

dirname = os.path.dirname(__file__)

class Square(pg.sprite.Sprite):
    def __init__(self, y, x, square_type, square_size):
        super().__init__()
        self.y = y
        self.x = x
        self.image = pg.image.load(os.path.join(dirname, "assets", pic_names[square_type]))
        self.rect = self.image.get_rect()
        self.rect.y = y * square_size
        self.rect.x = x * square_size

    