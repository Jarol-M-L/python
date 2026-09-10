import turtle
v=turtle.Screen()

#cuadrado
c=turtle.Turtle()

c.up()
c.goto(-200,-200)
c.down()

c.color("black")
c.pensize(5)
c.fillcolor("yellow")
c.begin_fill()
c.forward(500)
c.left(90)
c.forward(500)
c.left(90)
c.forward(500)
c.left(90)
c.forward(500)
c.left(90)
c.end_fill()

#m

m=turtle.Turtle()

m.up()
m.goto(-100,-50)
m.down()

m.color("red")
m.pensize(7)
m.left(90)
m.forward(250)
m.left(225)
m.forward(100)
m.left(90)
m.forward(100)
m.left(225)
m.forward(250)

#l

l=turtle.Turtle()

l.up()
l.goto(250,-50)
l.down()

l.color("red")
l.pensize(7)
l.left(180)
l.forward(150)
l.left(270)
l.forward(250)
v.exitonclick()