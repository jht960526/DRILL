import game_framework

from pico2d import *

PIXEL_PER_METER = (30.0/0.3)
RUN_SPEED_KMPH = 13.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Brick:
    image = None
    def __init__(self):
        self.x, self.y = 300, 230

        if Brick.image == None:
            Brick.image = load_image('Resource/brick1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_collision())

    def get_collision(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Brick_Q:
    image = None

    def __init__(self):
        self.x, self.y = 350, 230
        self.frame = 0

        if Brick_Q.image == None:
            Brick_Q.image = load_image('Resource/Brick_Q.png')

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 30, self.x, self.y)
        draw_rectangle(*self.get_collision())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def get_collision(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20