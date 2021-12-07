from pico2d import *

import Game_framework
import Game_world
import Server

from Player import Player
from Enemy import Enemy
from BackGround import Stage1
from Brick import Brick, Brick_Q
from Collision_Box import Collision_Box

name = "Main_State"


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

def mario_left_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_left_box()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_right_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_right_box()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_bottom_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_bottom_box()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_top_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_top_box()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def cylinder_colliside(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True


def enter():
    global grass
    Server.backGround = Stage1()
    Game_world.add_object(Server.backGround, 0)

    Server.bricks = [Brick() for i in range(1)]
    Game_world.add_objects(Server.bricks, 0)

    Server.bricks_Q = [Brick_Q() for i in range(1)]
    Game_world.add_objects(Server.bricks_Q, 0)

    Server.collision_boxs = [Collision_Box() for i in range(1)]
    Game_world.add_objects(Server.collision_boxs, 0)

    Server.enemies = [Enemy() for i in range(1)]
    Game_world.add_objects(Server.enemies, 0)

    Server.player = Player()
    Game_world.add_object(Server.player, 1)


def exit():
    Game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Game_framework.quit()
        else:
            Server.player.player_Handle(event)

def update():
    for game_object in Game_world.all_objects():
        game_object.update()

        for enemy in Server.enemies:
            if collide(Server.player, enemy):
                if mario_enemy_head(Server.player, enemy):
                    enemy.dead()
                    if Server.player.y > enemy.y:
                        Server.player.jump()
                        print("Jump")
            if enemy.deadTime >= 1:
                Game_world.remove_object(enemy)
                Server.enemies.remove(enemy)
                print("delete")

        for brick in Server.bricks:
            if mario_right_collision(Server.player, brick):
                print("BLICK COLLISION")
                Server.player.x = brick.x - 65

            if mario_top_collision(Server.player, brick):
                Server.player.y = brick.y - 80

            if mario_left_collision(Server.player, brick):
                print("BLICK COLLISION")
                Server.player.x = brick.x + 65

            if mario_bottom_collision(Server.player, brick):
                print("b_collision_box Collision")
                Server.player.fallSpeed = 0

        for brick_Q in Server.bricks_Q:
            if mario_right_collision(Server.player, brick_Q):
                print("BLICK COLLISION")
                Server.player.x = brick_Q.x - 65

            if mario_top_collision(Server.player, brick_Q):
                Game_world.remove_object(brick_Q)
                Server.bricks_Q.remove(brick_Q)


            if mario_left_collision(Server.player, brick_Q):
                print("BLICK COLLISION")
                Server.player.x = brick_Q.x + 65

            if mario_bottom_collision(Server.player, brick_Q):
                print("b_collision_box Collision")
                Server.player.fallSpeed = 0

        for collision_box in Server.collision_boxs:
            if mario_left_collision(Server.player, collision_box):
                print("l_collision_box Collision")
                Server.player.x = collision_box.x + 80

            if mario_right_collision(Server.player, collision_box):
                print("r_collision_box Collision")
                Server.player.x = collision_box.x - 80

            if mario_bottom_collision(Server.player, collision_box):
                print("b_collision_box Collision")
                Server.player.fallSpeed = 0


def draw():
    clear_canvas()
    for game_object in Game_world.all_objects():
        game_object.draw()
    update_canvas()
