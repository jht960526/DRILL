import game_framework
from pico2d import *
import main_state

name = "PauseState"

pause_image = None

def enter():
    global pause_image
    pause_image = load_image('pause.png')

    pass


def exit():
    global pause_image
    del(pause_image)
    pass

def draw():
    clear_canvas()
    pause_image.draw(400,300,400,400)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)

def update():
    clear_canvas()
    pause_image.draw(400, 300,400,400)
    update_canvas()