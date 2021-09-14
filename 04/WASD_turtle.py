import turtle

window = turtle.Screen()
hong = turtle.Turtle()
hong.shape('turtle')
hong.stamp()

def up():
      hong.setheading(90)
      hong.forward(50)
      hong.stamp()

def down():
      hong.setheading(-90)
      hong.forward(50)
      hong.stamp()

def right():
      hong.setheading(0)
      hong.forward(50)
      hong.stamp()
      
def left():
      hong.setheading(180)
      hong.forward(50)
      hong.stamp()

def restart():
      hong.reset()
      hong.stamp()

window.onkey(up,"Up")
window.onkey(up,"w")
window.onkey(down,"s")
window.onkey(right,"d")
window.onkey(left,"a")
window.onkey(restart,'Escape')
window.listen()
