from pico2d import *

class Brick:
    image = None
    def __init__(self):
        self.x, self.y = 300, 250

        if Brick.image == None:
            self.image = load_image('Resource/brick1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_collision())

    def get_collision(self):
        return self.x - 20, self.y - 34, self.x + 20, self.y + 34