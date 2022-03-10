import turtle
a=0
b=0
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pencolor("green")
t.goto(0,200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a=a+3
    b=b+1