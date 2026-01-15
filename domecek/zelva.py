from turtle import *
from math import sqrt
from random import randint

def domecek(a):
    """Nakreslí klasický domeček jedním tahem."""
    c = a * sqrt(2)  # délka úhlopříčky
    
    left(45)
    forward(c)       # první úhlopříčka
    left(90)
    forward(c/2)     # levá strana střechy
    left(90)
    forward(c/2)     # pravá strana střechy
    left(90)
    forward(c)       # druhá úhlopříčka
    left(135)
    forward(a)       # spodní strana
    left(90)
    forward(a)       # pravá strana
    left(90)
    forward(a)       # horní strana
    left(90)
    forward(a)       # levá strana
    left(90)         # vrátit orientaci na původní

# --- Nastavení turtle ---
speed(0)
showturtle()
bgcolor("skyblue")

# --- Domečky do kruhu ---
num_houses = 20      # sníženo pro přehlednost
radius = 200 

for i in range(num_houses):
    size = randint(30, 60)
    angle = (360 / num_houses) * i

    penup()
    goto(0, 0)          # návrat do středu
    setheading(angle)   # otočení směrem k obvodu
    forward(radius)     # přesun na obvod
    # Natočení tak, aby domeček stál "podlahou" ke středu nebo ven
    setheading(angle - 90) 
    pendown()

    color("brown")      # volitelné: barva domečku
    domecek(size)

exitonclick()