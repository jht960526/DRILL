from pico2d import *

import game_framework
import game_world

from Player import Player
from Enemy import Enemy
from Grass import Grass
from BackGround import Stage1

name = "Main_State"

player = None
grass = None
enemy = None
backGround = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    #if left_a > right_b: return False
    #if right_a < left_b: return False
    #if top_a < bottom_b: return False
    if bottom_a > top_b: return True
    #if bottom_a < top_b: return True

    #return False


def enter():
    global player, enemy, grass, backGround
    backGround = Stage1()
    game_world.add_object(backGround, 0)

    grass = Grass()
    game_world.add_object(grass, 1)

    enemy = Enemy()
    game_world.add_object(enemy, 1)

    player = Player()
    game_world.add_object(player, 1)



def exit():
    game_world.clear()

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
            player.player_Handle(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
        if collide(player, enemy):
            print("COLLISION")
            game_world.remove_object(enemy)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
