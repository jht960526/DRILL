import game_framework
import game_world
import random

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
        self.x, self.y = random.randint(10, 1500), 180
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0

    def get_bb(self):
        # fill here
            return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0.0,'h',self.x, self.y, 100, 100)

    def update(self):
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
            self.x += self.velocity * game_framework.frame_time
            if self.x >= 1500:
                # 오른쪽 끝에 도달하면 계속 -속도로 바꿈
                self.velocity = -RUN_SPEED_PPS

            elif self.x <= 90:
                # 왼쪽 끝에 도달하면 다시 원래대로
                self.velocity = RUN_SPEED_PPS
            self.dir = clamp(-1, self.velocity, 1)