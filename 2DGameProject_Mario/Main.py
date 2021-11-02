import random
from pico2d import *

class Player:
    def __init__(self):
        self.x, self.y = 10, 90
        self.vel = 100
        self.frame = random.randint(0, 8)
        self.image = load_image("Resource/mario_right_run.png")
        self.runImage = [load_image("Resource/Mario_Right_Run.png"), load_image("Resource/Mario_Left_Run.png")]
        self.idleImage = [load_image("Resource/Mario_Right_Idle.png"), load_image("Resource/Mario_Left_Idle.png")]
        self.frame = 0
        self.bIsRight = True
        self.dir = 0
        self.bIsRun = True
        self.bIsJump = True
        self.jumpCount = 10

    def update(self):
       self.frame = (self.frame + 1) % 9

    def draw(self):
        if self.dir == 0 and self.bIsRight == True:
            self.idleImage[0].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)
        elif self.dir == 0 and self.bIsRight == False:
            self.idleImage[1].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)
        elif self.dir != 0 and self.bIsRight == True:
            self.runImage[0].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)
        elif self.dir != 0 and self.bIsRight == False:
            self.runImage[1].clip_draw(self.frame * 90, 0, 80, 102, self.x, self.y)

    def walk(self):

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.bIsRun = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir += 1
                    self.bIsRight = True
                elif event.key == SDLK_LEFT:
                    self.dir -= 1
                    self.bIsRight = False
                elif event.key == SDLK_ESCAPE:
                    self.bIsRun = False
                elif event.key == SDLK_SPACE:
                    if self.y < 600 - 102 - self.vel:
                        self.y += self.vel

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                    self.bIsRight = True
                elif event.key == SDLK_LEFT:
                    self.dir += 1
                    self.bIsRight = False
                elif event.key == SDLK_SPACE:
                    if self.y > self.vel:
                        self.y -= self.vel
        self.x += self.dir * 10


class Enemy:
    def __init__(self):
        self.x, self.y = 300, 90
        self.frame = random.randint(0, 2)
        self.image = load_image("Resource/Enemy1.png")
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 87, self.x, self.y)


open_canvas()
grass = load_image('Resource/grass.png')
background = load_image('Resource/MarioBackground1.png')
player = Player()
enemy = Enemy()
frame = 0

while player.bIsRun:
    player.walk()

    player.update()
    enemy.update()
    clear_canvas()
    background.draw(800//2, 600//2)
    grass.draw(400, 30)
    enemy.draw()
    player.draw()
    update_canvas()
    delay(0.07)

close_canvas()

