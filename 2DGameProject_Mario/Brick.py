import game_framework

from pico2d import *

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
        #return self.x - 30/2, self.y, self.x + 30 / 2, self.y + 30 / 2
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
