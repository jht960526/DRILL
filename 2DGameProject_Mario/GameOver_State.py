from pico2d import *

import Game_framework
import Title_State
import Game_world
import random

name = "GameOver State"

def enter():
    global image, bgm
    image = load_image('Resource/over.png')
    bgm = load_music('Resource/sound/gameover_bgm.wav')
    bgm.play()
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Game_framework.change_state(Title_State)
    pass

def update():
    for game_object in Game_world.all_objects():
        game_object.update()


def draw():
    global image
    clear_canvas()
    image.draw(800 // 2, 600 // 2)
    update_canvas()
    pass