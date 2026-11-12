import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

def arbre(longueur, niveau):
    if niveau == 0:
        return
    t.forward(longueur)
    t.left(60)
    arbre(longueur * 0.7, niveau - 1)
    t.right(120)
    arbre(longueur * 0.7, niveau - 1)
    t.left(60)
    t.backward(longueur)

arbre(100, 7)
turtle.done()
