import random
from pico2d import *

class Player:

    def __init__(self):
        # Status
        self.x, self.y = 10, 90
        self.fallSpeed = 0
        self.frame = random.randint(1, 8)
        self.dir = 0
        self.jumpCount = 0
        # image load
        self.image = load_image("Resource/mario_right_run.png")
        self.runImage = [load_image("Resource/Mario_Right_Run.png"), load_image("Resource/Mario_Left_Run.png")]
        self.idleImage = [load_image("Resource/Mario_Right_Idle.png"), load_image("Resource/Mario_Left_Idle.png")]
        # Check
        self.bIsRight = True
        self.bIsRun = True
        self.bIsJump = False

    def update(self):
        self.frame = (self.frame + 1) % 9
        self.x += self.dir * 10
        if self.bIsJump:
            self.y += -1 * self.fallSpeed
            self.fallSpeed += 1
            delay(0.003)
            if self.y <= 90:
                self.y = 90


    def draw(self):
        if self.dir == 0 and self.bIsRight:
            self.idleImage[0].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)
        elif self.dir == 0 and not self.bIsRight:
            self.idleImage[1].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)
        elif self.dir != 0 and self.bIsRight:
            self.runImage[0].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)
        elif self.dir != 0 and not self.bIsRight:
            self.runImage[1].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)


    def Player_Handle(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.bIsRun = False

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.bIsRight = True
                    self.dir += 1
                elif event.key == SDLK_LEFT:
                    self.bIsRight = False
                    self.dir -= 1
                elif event.key == SDLK_ESCAPE:
                    self.bIsRun = False
                elif event.key == SDLK_SPACE:
                    self.Jump()

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
        print('player excute')
    def Jump(self):
        self.bIsJump = True
        self.fallSpeed = -13
        self.jumpCount += 1
        if self.jumpCount == 2:
            self.bIsJump = False
            self.jumpCount = 0