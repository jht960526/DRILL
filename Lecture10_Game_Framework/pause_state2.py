import game_framework
from pico2d import *
import main_state

name = "PauseState"
logo_time = 0.0
pause_image = True

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    global logo_time
    global pause_image

    if logo_time > 0.3:
        logo_time = 0
        if pause_image == True:
            pause_image = False
        else:
            pause_image = True

    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    if pause_image == True:
        image.clip_draw(0, 0, 900, 900, 400, 300, 200, 200)
    update_canvas()



def handle_events():
    global logo_time
    global pause_image
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
            logo_time = 0.0
            pause_image = True


def pause(): pass


def resume(): pass