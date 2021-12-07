from pico2d import *
import Server
from Player import Player

class Stage1:
    def __init__(self):
        self.image = load_image('Resource/background_level1.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def update(self):
        self.window_left = clamp(0, int(Server.player.x) - Server.backGround.canvas_width // 2,
                                 Server.backGround.w - Server.backGround.canvas_width)
        self.window_bottom = clamp(0, int(Server.player.y) - Server.backGround.canvas_height // 2,
                                   Server.backGround.h - Server.backGround.canvas_height)
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, Server.backGround.canvas_width,
                                       Server.backGround.canvas_height, 0, 0)
        #self.image.draw(800//2, 600//2)

    def handle_event(self, event):
        pass