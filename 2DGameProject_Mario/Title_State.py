from pico2d import *

import Game_framework
import Main_State
import Game_world
import random

name = "TitleState"
image = None
font = None
time = 0
R, G, B = 255, 255, 255

def enter():
    global image, font, bgm
    image = load_image('Resource/Title_State800x600.png')
    font = load_font('Resource/font/super-mario-64.ttf')
    bgm = load_music('Resource/sound/mario.wav')
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
                Game_framework.change_state(Main_State)
    pass

def update():
    global time, R, G, B
    for game_object in Game_world.all_objects():
        game_object.update()

    time += Game_framework.frame_time
    if time >= 0.2:
        time = 0
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

def draw():
    global image,R, G, B
    clear_canvas()
    image.draw(800 // 2, 600 // 2)
    font.draw(800 * 0.25, 600 * 0.3, 'Press SpaceBar To Start', (R, G, B))
    update_canvas()
    pass