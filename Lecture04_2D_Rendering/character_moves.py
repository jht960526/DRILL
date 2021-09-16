from pico2d import *
import math
import time

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here

grass.draw_now(400,30)
character.draw_now(400,90)
while True:
      x = 400
      y = 90
      degree = -90
      
      while (x < 800):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,90)
            x = x+2
            delay(0.01)
      
      while(y < 600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(800,y)
            y = y + 2
            delay(0.01)
      
      while(x > 0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,600)
            x = x - 2
            delay(0.01)
      
      while(y > 90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(0,y)
            y = y - 2
            delay(0.01)
      
      while(x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,90)
            x = x + 2
            delay(0.01)
      while(degree > -450):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            radian = math.radians(degree)
            x = 400+210*math.cos(radian)
            y = 300+210*math.sin(radian)
            degree = degree - 1
            delay(0.01)
            

close_canvas()
