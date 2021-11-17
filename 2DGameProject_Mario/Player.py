import game_framework
import random
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0/ 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 9

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class IdleState:

    def Enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += RUN_SPEED_PPS
        elif event == SPACE:
            player.Jump()
        player.timer = 1000

    def Exit(player, event):
        if event == SPACE:
            player.Jump()
        pass

    def Do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
        player.timer -= 1

    def Draw(player):
        if player.dir == 1:
            player.idleImage[0].clip_draw(int(player.frame) * 90, 0, 80, 102, player.x, player.y)
        else:
            player.idleImage[1].clip_draw(int(player.frame) * 90, 0, 80, 102, player.x, player.y)

class RunState:

    def Enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += RUN_SPEED_PPS
        player.dir = clamp(-1, player.velocity, 1)
        pass

    def Exit(player, event):
        if event == SPACE:
            player.Jump()
        pass

    def Do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
        player.x += player.velocity * game_framework.frame_time
        player.x = clamp(25, player.x, 1600 - 25)

    def Draw(player):
        if player.dir == 1:
            player.runImage[0].clip_draw(int(player.frame) * 90, 0, 80, 102, player.x, player.y)
        else:
            player.runImage[1].clip_draw(int(player.frame) * 90, 0, 80, 102, player.x, player.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
}

class Player:

    def __init__(self):
        # Status
        self.x, self.y = 10, 90
        self.fallSpeed = 0
        self.velocity = 10
        self.frame = 0
        self.dir = 1
        self.jumpCount = 0
        self.cur_state = IdleState
        self.cur_state.Enter(self, None)
        self.event_que = []
        # image load
        self.image = load_image("Resource/mario_right_run.png")
        self.runImage = [load_image("Resource/Mario_Right_Run.png"), load_image("Resource/Mario_Left_Run.png")]
        self.idleImage = [load_image("Resource/Mario_Right_Idle.png"), load_image("Resource/Mario_Left_Idle.png")]
        # Check
        self.bIsJump = False

    def Add_event(self, event):
        self.event_que.insert(0, event)

    def Update(self):
        self.cur_state.Do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.Exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.Enter(self, event)
        if self.bIsJump:
            self.y += -1 * self.fallSpeed
            self.fallSpeed += 1
            delay(0.003)
            if self.y <= 90:
                self.y = 90


    def Draw(self):
        self.cur_state.Draw(self)
        #self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (225, 225, 0))


    def Player_Handle(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.Add_event(key_event)

    def Jump(self):
        self.bIsJump = True
        self.fallSpeed = -13
        self.jumpCount += 1
        #if self.jumpCount == 2:
            #self.bIsJump = False
            #self.jumpCount = 0