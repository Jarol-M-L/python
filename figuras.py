import turtle
v=turtle.Screen()
#triangulo
t=turtle.Turtle()

t.up()
t.goto(-350,100)
t.down()
t.color("black")
t.fillcolor("DodgerBlue")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.end_fill()

#cuadrado

c=turtle.Turtle()

c.up()
c.goto(-230,100)
c.down()

c.color("black")
c.fillcolor("red")
c.begin_fill()
c.forward(100)
c.left(90)
c.forward(100)
c.left(90)
c.forward(100)
c.left(90)
c.forward(100)
c.left(90)
c.end_fill()

#rectangulo

r=turtle.Turtle()

r.up()
r.goto(-30,100)
r.down()

r.color("black")
r.fillcolor("yellow")
r.begin_fill()
r.forward(150)
r.left(90)
r.forward(100)
r.left(90)
r.forward(150)
r.left(90)
r.forward(100)
r.left(90)
r.end_fill()

#circulo

c2=turtle.Turtle()

c2.up()
c2.goto(200,100)
c2.down()

c2.color("black")
c2.fillcolor("MediumSeaGreen")
c2.begin_fill()
c2.circle(50)
c2.end_fill()

#rombo

r2=turtle.Turtle()

r2.up()
r2.goto(-300,-100)
r2.down()


r2.color("black")
r2.fillcolor("yellow")
r2.begin_fill()
r2.left(40)
r2.forward(100)
r2.left(90)
r2.forward(100)
r2.left(90)
r2.forward(100)
r2.left(90)
r2.forward(100)
r2.end_fill()

#romboide

r3=turtle.Turtle()

r3.up()
r3.goto(-210,-100)
r3.down()

r3.color("black")
r3.fillcolor("DodgerBlue")
r3.begin_fill()
r3.forward(150)
r3.left(65)
r3.forward(100)
r3.left(115)
r3.forward(150)
r3.left(65)
r3.forward(100)
r3.end_fill()

#trapecio
t1=turtle.Turtle()

t1.up()
t1.goto(50,-100)
t1.down()

t1.color("black")
t1.fillcolor("MediumSeaGreen")
t1.begin_fill()
t1.forward(50)
t1.left(65)
t1.forward(100)
t1.left(115)
t1.forward(130)
t1.left(115)
t1.forward(103)
t1.end_fill()
#ovalo

o=turtle.Turtle()

o.up()
o.goto(250,-50)
o.down()


o.fillcolor("red")
o.shape("circle")
o.shapesize(4,6,2)


v.exitonclick()