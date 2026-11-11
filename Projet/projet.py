import turtle

nombre = int(input("Combien de pétales voulez-vous ? : "))
taille = int(input("Quelle taille pour les pétales ? : "))

couleur1 = input("Première couleur(En anglais) : ")
couleur2 = input("Deuxième couleur(En anglais) : ")
couleur3 = input("Troisième couleur(En anglais) : ")

t = turtle.Turtle()
t.speed(0)

turtle.bgcolor("black")

def petale():
    t.circle(taille, 60)
    t.left(120)
    t.circle(taille, 60)
    t.left(120)

for i in range(nombre):
    if i % 3 == 0:
        t.color(couleur1)
    elif i % 3 == 1:
        t.color(couleur2)
    else:
        t.color(couleur3)

    petale()
    t.left(360 / nombre)

turtle.done()
