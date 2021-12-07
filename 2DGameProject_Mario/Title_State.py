from pico2d import *

import Game_framework
import Main_State
import Game_world

name = "TitleState"
image = None

def enter():
    global image
    image = load_image('Resource/Title_State800x600.png')
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
    for game_object in Game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    image.draw(800 // 2, 600 // 2)
    update_canvas()
    pass