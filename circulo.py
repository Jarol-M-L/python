import turtle
v=turtle.Screen()
radio=float(input("ingrese el radio:"))
coordenada_x=float(input("ingrese las coordenadas x:"))
coordenada_y=float(input("ingrese las coordenadas y:"))

v=turtle.Screen()

#circulo
c=turtle.Turtle()
c.color('red')
c.circle(radio)

c.up()
c.goto(coordenada_x,coordenada_y)
c.down()

v.exitonclick()