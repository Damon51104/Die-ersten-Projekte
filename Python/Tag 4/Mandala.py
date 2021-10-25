import turtle as t

sc = t.Screen()
sc.title("Quadrat!")
sc.setup(800,800)
sc.bgcolor("black")

counter = 0

while counter <32:
    def quadrat():
        t.speed(0)
        t.color("#c6e2ff")
        t.forward(100)
        t.left(80)
        t.forward(110)
        t.left(90)
        t.forward(120)
        t.left(80)
        t.forward(130)
        t.left(90)
    quadrat()
    
    counter += 1

sc.exitonclick()