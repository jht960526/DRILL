from pico2d import *

import game_framework

from Player import Player
from Enemy import Enemy
from Grass import Grass
from BackGround import Stage1

name = "Main_State"

player = None
grass = None
enemy = None
backGround = None

def enter():
    global player, enemy, grass, backGround
    backGround = Stage1()
    player = Player()
    enemy = Enemy()
    grass = Grass()

def exit():
    global player, enemy, grass, backGround
    del backGround
    del player
    del enemy
    del grass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.Player_Handle(event)

def update():
    player.update()

def draw():
    clear_canvas()
    backGround.draw()
    grass.draw()
    player.draw()
    update_canvas()
