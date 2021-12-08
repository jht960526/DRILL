import Game_framework
import Server

from pico2d import *
from Player import Player

PIXEL_PER_METER = (30.0/0.3)
RUN_SPEED_KMPH = 12.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 20

name = 'Coin Count'
R, G, B = 255, 255, 255
class Coin_Count:
    font = None


    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y
        self.frame = 0
        self.playTime = 0

        if Coin_Count.font == None:
            Coin_Count.font = load_font('Resource/font/font.ttf')

    def draw(self):
        global R,G,B
        self.font.draw(self.x, self.y, 'Coin: %d' % Server.player.coin_Count, (R, G, B))

    def update(self):
        self.playTime += Game_framework.frame_time

    def setup():
        Server.coin_counts = [Coin_Count(400, 550)]