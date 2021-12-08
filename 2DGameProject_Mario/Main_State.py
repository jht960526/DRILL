from pico2d import *

import Game_framework
import Game_world
import Server

from Player import Player
from Enemy import Enemy
from BackGround import Stage1
from Brick import Brick, Brick_Q
from Collision_Box import Collision_Box
from Collision_Box2 import Collision_Box2
from Collision_Box3 import Collision_Box3
from Coin import Coin

name = "Main_State"

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## collision_box1
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

## collision_box2
def mario_left_collision2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_left_box()
    left_b, bottom_b, right_b, top_b = b.get_collision2()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_right_collision2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_right_box()
    left_b, bottom_b, right_b, top_b = b.get_collision2()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_bottom_collision2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_bottom_box()
    left_b, bottom_b, right_b, top_b = b.get_collision2()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_top_collision2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_top_box()
    left_b, bottom_b, right_b, top_b = b.get_collision2()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## collision_box3
def mario_left_collision3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_left_box()
    left_b, bottom_b, right_b, top_b = b.get_collision3()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_right_collision3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_right_box()
    left_b, bottom_b, right_b, top_b = b.get_collision3()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_bottom_collision3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_bottom_box()
    left_b, bottom_b, right_b, top_b = b.get_collision3()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def mario_top_collision3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mario_top_box()
    left_b, bottom_b, right_b, top_b = b.get_collision3()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## cylinder_collision
def cylinder_colliside(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## enemy_left_collision
def enemy_left_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_enemy_left()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## enemy_right_collision
def enemy_right_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_enemy_right()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## enemy_left_collision2
def enemy_left_collision2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_enemy_left()
    left_b, bottom_b, right_b, top_b = b.get_collision2()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## enemy_right_collision2
def enemy_right_collision2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_enemy_right()
    left_b, bottom_b, right_b, top_b = b.get_collision2()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## enemy_left_collision3
def enemy_left_collision3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_enemy_left()
    left_b, bottom_b, right_b, top_b = b.get_collision3()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## enemy_right_collision3
def enemy_right_collision3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_enemy_right()
    left_b, bottom_b, right_b, top_b = b.get_collision3()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

## coin collision
def coin_collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_collision()
    left_b, bottom_b, right_b, top_b = b.get_collision()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False

    return True

def enter():
    Collision_Box.setup()
    Collision_Box2.setup()
    Collision_Box3.setup()
    Enemy.setup()
    Coin.setup()

    # stage1
    Server.backGround = Stage1()
    Game_world.add_object(Server.backGround, 0)

    # brick
    Server.bricks = [Brick() for i in range(1)]
    Game_world.add_objects(Server.bricks, 0)

    # brick_Q
    Server.bricks_Q = [Brick_Q() for i in range(1)]
    Game_world.add_objects(Server.bricks_Q, 0)

    # Coin

    # Collision_Box
    Game_world.add_objects(Server.collision_boxs, 0)
    Game_world.add_objects(Server.collision_boxs2, 0)
    Game_world.add_objects(Server.collision_boxs3, 0)

    # Enemy
    #Server.enemies = [Enemy() for i in range(1)]
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

        # enemy
        for enemy in Server.enemies:
            if mario_bottom_collision(Server.player, enemy):
                enemy.dead()
                if Server.player.y > enemy.y:
                    Server.player.jump()
                    print("Jump")

            if enemy.deadTime >= 1:
                Game_world.remove_object(enemy)
                Server.enemies.remove(enemy)

            if mario_right_collision(Server.player, enemy):
                Server.player.x = enemy.x - 80

            if mario_left_collision(Server.player, enemy):
                Server.player.x = enemy.x + 80

            # enemy collision_box1
            for collision_box in Server.collision_boxs:
                if enemy_left_collision(enemy, collision_box):
                    enemy.velocity *= -1
                    enemy.x = collision_box.x + 80


                if enemy_right_collision(enemy, collision_box):
                    enemy.velocity *= -1
                    enemy.x = collision_box.x - 80


            # enemy collision_box2
            for collision_box2 in Server.collision_boxs2:
                if enemy_left_collision2(enemy, collision_box2):
                    enemy.velocity *= -1
                    enemy.x = collision_box2.x + 80


                if enemy_right_collision2(enemy, collision_box2):
                    enemy.velocity *= -1
                    enemy.x = collision_box2.x - 80


            # enemy collision_box3
            for collision_box3 in Server.collision_boxs3:
                if enemy_left_collision3(enemy, collision_box3):
                    enemy.velocity *= -1
                    enemy.x = collision_box3.x + 80


                if enemy_right_collision3(enemy, collision_box3):
                    enemy.velocity *= -1
                    enemy.x = collision_box3.x - 80


        # brick
        for brick in Server.bricks:
            if mario_right_collision(Server.player, brick):
                Server.player.x = brick.x - 65

            if mario_top_collision(Server.player, brick):
                Server.player.y = brick.y - 80

            if mario_left_collision(Server.player, brick):
                Server.player.x = brick.x + 65

            if mario_bottom_collision(Server.player, brick):
                Server.player.fallSpeed = 0

        # brick_Q
        for brick_Q in Server.bricks_Q:
            if mario_right_collision(Server.player, brick_Q):
                Server.player.x = brick_Q.x - 65

            if mario_top_collision(Server.player, brick_Q):
                Game_world.remove_object(brick_Q)
                Server.bricks_Q.remove(brick_Q)
                Game_world.add_objects(Server.coins, 0)
                for coin in Server.coins:
                    coin.coin_appear()

            if mario_left_collision(Server.player, brick_Q):
                Server.player.x = brick_Q.x + 65

            if mario_bottom_collision(Server.player, brick_Q):
                Server.player.fallSpeed = 0

        # coin
        for coin in Server.coins:
            if coin.appearTime >= 0.2:
                Game_world.remove_object(coin)
                Server.coins.remove(coin)
            #if coin_collision(Server.player, coin):
                #Game_world.remove_object(coin)
                #Server.coins.remove(coin)

        # collision_box1
        for collision_box in Server.collision_boxs:
            if mario_left_collision(Server.player, collision_box):
                Server.player.x = collision_box.x + 80

            if mario_right_collision(Server.player, collision_box):
                Server.player.x = collision_box.x - 80

            if mario_bottom_collision(Server.player, collision_box):
                Server.player.fallSpeed = 0

        # collision_box2
        for collision_box2 in Server.collision_boxs2:
            if mario_left_collision2(Server.player, collision_box2):
                Server.player.x = collision_box2.x + 80

            if mario_right_collision2(Server.player, collision_box2):
                Server.player.x = collision_box2.x - 80

            if mario_bottom_collision2(Server.player, collision_box2):
                Server.player.fallSpeed = 0

        # collision_box3
        for collision_box3 in Server.collision_boxs3:
            if mario_left_collision3(Server.player, collision_box3):
                Server.player.x = collision_box3.x + 80

            if mario_right_collision3(Server.player, collision_box3):
                Server.player.x = collision_box3.x - 80

            if mario_bottom_collision3(Server.player, collision_box3):
                Server.player.fallSpeed = 0


def draw():
    clear_canvas()
    for game_object in Game_world.all_objects():
        game_object.draw()
    update_canvas()
