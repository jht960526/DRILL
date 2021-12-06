from pico2d import *
import server
from Player import Player

class Stage1:
    def __init__(self):
        self.image = load_image('Resource/background_level1.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 800 * 3
        self.h = 600

    def update(self):
        self.window_left = clamp(0, int(server.player.x) - server.backGround.canvas_width // 2,
                                 server.backGround.w - server.backGround.canvas_width)
        self.window_bottom = clamp(0, int(server.player.y) - server.backGround.canvas_height // 2,
                                   server.backGround.h - server.backGround.canvas_height)
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.backGround.canvas_width,
                                       server.backGround.canvas_height, 0, 0)
        #self.image.draw(800//2, 600//2)

    def handle_event(self, event):
        pass