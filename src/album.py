from time import sleep, time

import math
import operator
from functools import reduce

from PIL import ImageGrab, ImageOps, Image  # pip install Pillow
import keyboard  # pip install keyboard



class Album:
    def __init__(self, position, direction="up"):
        self.position = position
        self.direction = "down" if direction == "down" else "up"

    def _open_HoF(self):
        pass

    def _find_player(self):
        pass

    def _attack(self):
        pass

    def find_and_kill_player(self):
        self._find_player()
        self._attack()
        print("player killed")
        t_before = time()
        self._find_player()
        t_after = time()
        return math.ceil(t_after - t_before)  # searching time
