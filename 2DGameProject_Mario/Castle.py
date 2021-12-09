import Game_framework
import Server

from pico2d import *

PIXEL_PER_METER = (30.0/0.3)
RUN_SPEED_KMPH = 12.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Castle:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y

        if Castle.image == None:
            Castle.image = load_image('Resource/tower.png')

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        pass

    def draw(self):
        self.image.draw(self.cx, self.cy)
        #draw_rectangle(*self.get_collision())

    def get_collision(self):
        return self.cx - 70, self.cy - 170, self.cx + 30, self.cy

    def setup():
        Server.castle = [
            Castle(2350, 250),
        ]