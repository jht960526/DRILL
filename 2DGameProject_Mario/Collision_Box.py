import Game_framework
import Server

from pico2d import *

class Collision_Box:
    def __init__(self):
        self.x, self.y = 1018, 133
        self.cx, self.cy = self.x, self.y

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        pass

    def draw(self):
        draw_rectangle(*self.get_collision())

    def get_collision(self):
        return self.cx - 35, self.cy - 50, self.cx + 35, self.cy + 35

    #def setup(self):
        #Server.collision_boxs = [Collision_Box(),]