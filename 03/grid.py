import turtle as t

t.penup()
height = 150
hor = 150
t.goto(hor,height)
t.pendown()

for i in range(6):
      t.forward(500)
      t.penup()
      height -= 100
      t.goto(hor,height)
      t.pendown()

t.penup()
hor = 150
height = 150
t.goto(hor,height)
t.pendown()
t.right(90)

for i in range(6):
      t.forward(500)
      t.penup()
      hor += 100
      t.goto(hor,height)
      t.pendown()
