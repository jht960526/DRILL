import Game_framework
import Game_world
import random
import Server

from pico2d import *
from Player import Player

PIXEL_PER_METER = (30.0/0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Enemy:

    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 600), 100
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0
        self.bDead = False
        self.deadCount = 0
        self.deadTime = 0
        self.cx, self.cy = 0, 0

        if Enemy.image == None:
            Enemy.image = load_image("Resource/Enemy1.png")

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 40, 0, 40, 58, self.cx, self.cy)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 40, 0, 40, 58, 0.0, 'h', self.cx, self.cy, 40, 58)
        draw_rectangle(*self.get_collision())
        if self.bDead:
            self.image.clip_draw(80, 0, 40, 58, self.cx, self.cy)

    def update(self):
        self.cx, self.cy = self.x - Server.backGround.window_left, self.y - Server.backGround.window_bottom
        if self.bDead:
            self.deadTime += Game_framework.frame_time
            print("time start")

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * Game_framework.frame_time) % 2
        self.x += self.velocity * Game_framework.frame_time

        if self.x >= 600:
            # 오른쪽 끝에 도달하면 계속 -속도로 바꿈
            self.velocity = -RUN_SPEED_PPS

        elif self.x <= 500:
            # 왼쪽 끝에 도달하면 다시 원래대로
            self.velocity = RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)


    def dead(self):
        self.bDead = True
        self.velocity = 0

    def get_collision(self):
        return self.cx - 20, self.cy - 22, self.cx + 20, self.cy + 22

    def get_enemy_pos(self):
        return self.cx - 10, self.cy + (29 // 2), self.cx + 10, self.cy + 29