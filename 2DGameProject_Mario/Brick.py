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

class Brick:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y

        if Brick.image == None:
            Brick.image = load_image('Resource/brick1.png')

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        pass

    def draw(self):
        self.image.draw(self.cx, self.cy)
        #draw_rectangle(*self.get_collision())

    def get_collision(self):
        return self.cx - 20, self.cy - 20, self.cx + 20, self.cy + 20

    def setup():
        Server.bricks = [
            Brick(350, 230),
            Brick(460, 240),
            Brick(500, 240),
            Brick(730, 240),
            Brick(770, 240)
            #Brick(1120, 260),
            #Brick(1440, 260),
            #Brick(1780, 260)
        ]

class Brick_Q:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.cx, self.cy = self.x, self.y
        self.frame = 0

        if Brick_Q.image == None:
            Brick_Q.image = load_image('Resource/Brick_Q.png')

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 30, self.cx, self.cy)
        #draw_rectangle(*self.get_collision())

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * Game_framework.frame_time) % 3

    def get_collision(self):
        return self.cx - 20, self.cy - 20, self.cx + 20, self.cy + 20

    def setup():
        Server.brick_Q = [
            Brick_Q(580, 270),
            Brick_Q(1230, 270),
            Brick_Q(1530, 270),
            Brick_Q(1880, 270)]