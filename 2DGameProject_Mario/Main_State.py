from pico2d import *

import game_framework
import game_world

from Player import Player
from Enemy import Enemy
from Grass import Grass
from BackGround import Stage1
from Brick import Brick

name = "Main_State"

player = None
grass = None
enemy = None
backGround = None
brick = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if bottom_a > top_b and right_a > left_b: return True
    if bottom_a > top_b and left_a > right_b: return True

def brick_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if top_a > bottom_b and right_a > left_b: return True
    if top_a > bottom_b and left_a > right_b: return True


def enter():
    global player, enemy, grass, backGround
    backGround = Stage1()
    game_world.add_object(backGround, 0)

    brick = Brick()
    game_world.add_object(brick, 0)

    grass = Grass()
    game_world.add_object(grass, 0)

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
        #if brick_collide(player, brick):
            #print("BLICK COLLISION")
            #game_world.remove_object(brick)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
