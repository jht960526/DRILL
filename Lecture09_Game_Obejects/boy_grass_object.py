from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x , self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 799), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.y -= 5

    def draw(self):
        self.image.draw(self.x, self.y)
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy = Boy()
grass = Grass()
ball = Ball()
team = [Boy() for i in range(11)]
bigBallTeam = [Ball() for j in range(20)]
smallBallTeam = [Ball() for k in range(20)]

running = True

# game main loop code
while running:
    handle_events()

    boy.update()
    for boy in team:
        boy.update()
    for ball in bigBallTeam:
        ball.update()
    clear_canvas()
    grass.draw()
    boy.draw()
    ball.draw()
    for boy in team:
        boy.draw()
    for ball in bigBallTeam:
        ball.draw()
    ##for ball in smallBallTeam:
        ##ball.draw()

    update_canvas()

    delay(0.05)


# finalization code
close_canvas()