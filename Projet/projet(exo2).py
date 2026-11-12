import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
couleurs = ["cyan", "magenta", "yellow", "orange"]

for i in range(600):
    t.color(couleurs[i % len(couleurs)])
    t.forward(i * 1.2)
    t.left(90)

turtle.done()
