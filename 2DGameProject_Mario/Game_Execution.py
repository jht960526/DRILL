import game_framework
import pico2d

import Main_State

pico2d.open_canvas(800, 600)
game_framework.run(Main_State)
pico2d.close_canvas()