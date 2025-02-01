from turtle import *
import turtle
import random
turtle.bgcolor('black')
turtle.color('green')
begin_fill()
speed('slowest')
shape('circle')
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)

left(10)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)

left(10)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
left(10)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
hideturtle()
end_fill()

heart=turtle.Turtle()
heart.penup()
heart.speed('slowest')
heart.shape('circle')
heart.goto(0,-50)
heart.color('red')
heart.begin_fill()
heart.left(50)
heart.forward(70) 
heart.circle(30, 200)  
heart.right(140)
heart.circle(30, 200) 
heart.forward(70)
heart.hideturtle()
heart.end_fill()

def write_text(text, x, y):
    tex=turtle.Turtle()
    tex.speed('slowest')
    tex.hideturtle()
    tex.color('white')
    tex.penup()
    tex.goto(x, y)
    tex.pendown()
    tex.write(text, align="center", font=("Arial", 15, "bold"))

star = turtle.Turtle()
star.shape('circle')
star.hideturtle()
star.color('yellow')
star.speed('slowest')
star.penup()
import time
screen = turtle.Screen()
screen.tracer(200)

def draw_star(size):
    star.begin_fill()
    star.pendown()
    for _ in range(5): 
        star.forward(size)
        star.right(144)
    star.penup()
    star.end_fill()

def move_star():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    star.goto(x, y)

def writer(text, x, y, col, a):
    texi=turtle.Turtle()
    texi.speed('slowest')
    texi.hideturtle()
    texi.color(col)
    texi.penup()
    texi.goto(x, y)
    texi.pendown()
    texi.write(text, align="center", font=("Arial", a, "bold"))
    
def wri(text, x, y, a):
    te=turtle.Turtle()
    te.speed('fastest')
    te.hideturtle()
    te.color('#ff0055')
    te.penup()
    te.goto(x, y)
    te.pendown()
    te.write(text, align="center", font=("Arial", a, "bold"))

for i in range(201):
    if(i==10):
        turtle.bgcolor('#14AAF5')
    if(i==25):
        write_text("HAPPY MONTHAVERSARY MY FOUR LEAF CLOVER!", 0, 10)
    if(i==40):
        write_text("I Love You Arush Baby MWUAHHHH!!!!", 0, -20)
    if(i==55):
        write_text("God Bless You Always Baby :)", 0, -75)
    if(i==70):
        write_text("You're Beautiful.", 0, -105)
    if(i==85):
        write_text("CHEERS TO US AND OUR FUTURE!!!", 0, 105)
    if(i==100):
        write_text("ARUSH IS THE BEST AND I LOVE HIM <3 <3 <3", 0, 75)
    if(i==115):
        turtle.bgcolor('#FF91A4')
    if(i==150):
        writer("Can't wait to win chicken dinner, make you dinner, and be your dinner forever ;)",0,-300, 'black', 12)
    if(i==200):
        screen=turtle.Screen()
        for j in range(10,700, 50):
            screen.clear()
            wri("💋", 0, -300, j)
        bgcolor('#00754e')
        writer("I LOVE YOU ∞", 0, 0, 'black', 50)
    time.sleep(0.1)
    move_star()
    draw_star(random.randint(20, 50))
    screen.update()
    star.clear()

done()