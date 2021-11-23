import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

name = "MainState"

boy = None
grass = None
balls = []
brick = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def brick_Collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if bottom_b == top_a:
        return True

    return False

def check_side(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if right_a == left_b:
        return True

    return False



def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global bricks
    bricks = [Brick(300+300*i, 100+50*i) for i in range(5)]
    game_world.add_objects(bricks, 1)



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
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for ball in balls.copy():
        if collide(ball, grass):
            ball.stop()
        if collide(ball, boy):
            balls.remove(ball)
            game_world.remove_object(ball)

    for brick in bricks:
        if collide(boy, brick):
            boy_l, boy_b, boy_r, boy_t = boy.get_bb()
            brick_l, brick_b, brick_r, brick_t = brick.get_bb()
            boy.y = brick.y + 45
            # 벽돌 크기에 맞춰서 clamp인자를 적용하면 벽돌과 충돌하기 어려워서 좀 더 크게 잡음
            boy.x = clamp(brick.x - 100, boy.x + game_framework.frame_time * brick.speed, brick.x + 100)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






