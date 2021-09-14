import turtle as t

t.penup()
height = 250
hor = 10
t.goto(hor,height)
t.pendown()

for i in range(6):
      t.forward(500)
      t.penup()
      height -= 100
      t.goto(hor,height)
      t.pendown()

t.penup()
hor = 10
height = 250
t.goto(hor,height)
t.pendown()
t.right(90)

for i in range(6):
      t.forward(500)
      t.penup()
      hor += 100
      t.goto(hor,height)
      t.pendown()
