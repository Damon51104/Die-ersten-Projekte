import turtle as t

sc = t.Screen()
sc.title("ADA")
sc.setup(800,600)
sc.bgcolor("black")
sc.tracer(0)

Leonardo = t
Leonardo = t.color("blue")

#A von "A"DA

t.forward(250)
t.backward(500)
t.goto(y=200, x=-200)
t.goto(y=0, x=-150)
t.penup()
t.goto(y=80, x=-230)
t.pendown()
t.forward(60)
t.penup()

#D von A"D"A

t.goto(y=0, x=-100)
t.pendown()
t.circle(100,180)
t.left(90)
t.forward(200)
t.penup()

#A von AD"A"

t.goto(y=0, x=25)
t.pendown()
t.goto(y=200, x=80)
t.goto(y=0, x=140)
t.penup()
t.goto(y=80, x=80)
t.pendown()
t.left(90)
t.forward(35)
t.backward(70)
t.penup()

t.goto(x=0, y=0)

while True:
    sc.update()