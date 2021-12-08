import Game_framework
import Server

from pico2d import *

class Collision_Box3:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        pass

    def draw(self):
        draw_rectangle(*self.get_collision3())

    def get_collision3(self):
        return self.cx - 30, self.cy - 50, self.cx + 35, self.cy + 115

    def setup():
        Server.collision_boxs3 = [Collision_Box3(1640, 133),
                                  Collision_Box3(2027, 133)]