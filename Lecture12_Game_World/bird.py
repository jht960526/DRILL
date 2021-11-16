import game_framework
import game_world
from pico2d import *

PIXEL_PER_METER = (30.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 190
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0
        self.imagePos = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
                         [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                         [0, 0], [1, 0], [2, 0], [3, 0]]

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.imagePos[int(self.frame)][1] * 183, self.imagePos[int(self.frame)][0] * 168,
                                 180, 166, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.imagePos[int(self.frame)][0] * 183,
                                           self.imagePos[int(self.frame)][1] * 168, 180, 166,
                                           0.0,'h',self.x, self.y, 180, 166)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1500:
            self.velocity = -RUN_SPEED_PPS
        elif self.x <= 90:
            self.velocity = RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)