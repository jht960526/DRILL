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
FRAMES_PER_ACTION = 20

name = 'Life'
class Life:
    image1 = None
    image2 = None
    image3 = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y
        self.frame = 0

        if Life.image1 == None:
            Life.image1 = load_image('Resource/s1.png')

        if Life.image2 == None:
            Life.image2 = load_image('Resource/s2.png')

        if Life.image3 == None:
            Life.image3 = load_image('Resource/s3.png')

    def draw(self):
        if Server.player.life == 3:
            self.image3.draw(self.x, self.y)

        if Server.player.life == 2:
            self.image2.draw(self.x, self.y)

        if Server.player.life == 1:
            self.image1.draw(self.x, self.y)

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * Game_framework.frame_time) % 4

    def get_collision(self):
        return self.cx - 15, self.cy - 15, self.cx + 15, self.cy + 15

    def setup():
        Server.life = [Life(70, 560)]