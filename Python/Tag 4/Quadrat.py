import turtle as t

sc = t.Screen()
sc.title("Quadrat!")
sc.setup(800,600)
sc.bgcolor("black")
sc.tracer(0)

def quadrat():
    t.color("blue")
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
quadrat()



while True:
    sc.update()