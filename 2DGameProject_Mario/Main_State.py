from pico2d import *

import game_framework
import game_world

from Player import Player
from Enemy import Enemy
from Grass import Grass
from BackGround import Stage1
from Brick import Brick, Brick_Q

name = "Main_State"

player = None
grass = None
enemies = None
backGround = None
bricks = None
bricks_Q = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_enemy_head(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_pos()
    left_b, bottom_b, right_b, top_b = b.get_enemy_pos()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def side_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a + 8 > right_b: return False
    if right_a < left_b + 8: return False
    return True

def brick_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True


def enter():
    global player, enemies, grass, backGround, bricks, bricks_Q
    backGround = Stage1()
    game_world.add_object(backGround, 0)

    bricks = [Brick() for i in range(1)]
    game_world.add_objects(bricks, 0)

    bricks_Q = [Brick_Q() for i in range(1)]
    game_world.add_objects(bricks_Q, 0)

    grass = Grass()
    game_world.add_object(grass, 0)

    enemies = [Enemy() for i in range(1)]
    game_world.add_objects(enemies, 0)

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

        for enemy in enemies:
            if collide(player, enemy):
                if mario_enemy_head(player, enemy):
                    enemy.dead()
                    if player.y > enemy.y:
                        player.jump()
                        print("Jump")
            if enemy.deadTime >= 1:
                game_world.remove_object(enemy)
                print("delete")


        for brick in bricks:
            if brick_collide(player, brick):
                print("BLICK COLLISION")
                game_world.remove_object(brick)

        for brick_Q in bricks_Q:
            if brick_collide(player, brick_Q):
                print("Brick_Q Collision")
                game_world.remove_object(brick_Q)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
