from pico2d import *
import random

class Enemy:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(300, 350), 90
        self.frame = random.randint(0, 2)
        if Enemy.image == None:
            Enemy.image = load_image("Resource/Enemy1.png")

    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 87, self.x, self.y)