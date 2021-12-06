from pico2d import *

class Stage1:
    def __init__(self):
        self.image = load_image('Resource/background_level1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800//2, 600//2)