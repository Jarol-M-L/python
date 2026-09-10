import turtle
v=turtle.Screen()

#rojo
r=turtle.Turtle()

r.color('red')
r.shape('arrow')
r.pensize(10)
r.forward(100)

#amarrillo

a=turtle.Turtle()

a.up()
a.goto(120,30)
a.down()

a.color('#B8860B')
a.shape('arrow')
a.pensize(10)
a.left(90)
a.forward(100)

#verde

g=turtle.Turtle()

g.up()
g.goto(100,160)
g.down()

g.color('green')
g.shape('arrow')
g.pensize(10)
g.left(180)
g.forward(100)

#azul

b=turtle.Turtle()

b.up()
b.goto(-20,120)
b.down()

b.color('blue')
b.shape('arrow')
b.pensize(10)
b.left(270)
b.forward(100)








v.exitonclick()