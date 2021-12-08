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

name = 'Font'
R, G, B = 255, 255, 255
class Font:
    image = None
    font = None


    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y
        self.frame = 0
        self.playTime = 0

        if Font.image == None:
            Font.image = load_image('Resource/coin.png')

        if Font.font == None:
            Font.font = load_font('Resource/font/font.ttf')

    def draw(self):
        global R,G,B
        #self.image.clip_draw(int(self.frame) * 40, 0, 40, 30, self.cx, self.cy)
        self.font.draw(self.x, self.y, 'Time: %f' % self.playTime, (R, G, B))
        #draw_rectangle(*self.get_collision())

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * Game_framework.frame_time) % 4
        self.playTime += Game_framework.frame_time

    def get_collision(self):
        return self.cx - 15, self.cy - 15, self.cx + 15, self.cy + 15

    def coin_appear(self):
        self.bappear = True

    def setup():
        Server.fonts = [Font(600, 550)]