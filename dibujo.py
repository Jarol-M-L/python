import turtle
v=turtle.Screen()

#cielo
 
c=turtle.Turtle()
c.speed(0)

c.up()
c.goto(-200,-200)
c.down()

c.color("black")
c.fillcolor("blue")
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

c.hideturtle()

#paSto
p=turtle.Turtle()
p.speed(0)

p.up()
p.goto(-198,-198)
p.down()

p.color("ForestGreen")
p.fillcolor("ForestGreen")
p.begin_fill()
p.forward(498)
p.left(90)
p.forward(264)
p.left(90)
p.forward(498)
p.left(90)
p.forward(264)
p.left(90)


p.end_fill()
p.hideturtle()

#carretera


c2=turtle.Turtle()
c2.speed(0)

c2.up()
c2.goto(-100,-200)
c2.down()


c2.begin_fill()
c2.fillcolor("black")

c2.forward(200)
c2.left(100)
c2.forward(270)
c2.left(80)
c2.forward(120)
c2.left(82)
c2.forward(272)

c2.end_fill()
c2.hideturtle()
#carretera2
b=turtle.Turtle()
b.speed(0)

b.up()
b.goto(-10,-200)
b.down()


b.begin_fill()
b.fillcolor("white")

b.forward(30)
b.left(94)
b.forward(270)
b.left(80)
b.forward(3)
b.left(94)
b.forward(272)

b.end_fill()
b.hideturtle()

#sol

s=turtle.Turtle()
s.speed(0)

s.up()
s.goto(70,200)
s.down()


s.fillcolor("SeaShell")
s.begin_fill()
s.circle(50)
s.end_fill()

s.hideturtle()

#nube1

n1=turtle.Turtle()
n1.speed(0)

n1.up()
n1.goto(120,200)
n1.down()

n1.color("#DCDCDC")
n1.fillcolor("#DCDCDC")
n1.begin_fill()
n1.circle(50)
n1.end_fill()

n1.hideturtle()

#nube2

n2=turtle.Turtle()
n2.speed(0)


n2.up()
n2.goto(140,180)
n2.down()

n2.color("#DCDCDC")
n2.fillcolor("#DCDCDC")
n2.begin_fill()
n2.circle(50)
n2.end_fill()
n2.hideturtle()

#nube3

n3=turtle.Turtle()
n3.speed(0)


n3.up()
n3.goto(150,200)
n3.down()

n3.color("#DCDCDC")
n3.fillcolor("#DCDCDC")
n3.begin_fill()
n3.circle(50)
n3.end_fill()

n3.hideturtle()

#nube4

n4=turtle.Turtle()
n4.speed(0)


n4.up()
n4.goto(190,200)
n4.down()

n4.color("#DCDCDC")
n4.fillcolor("#DCDCDC")
n4.begin_fill()
n4.circle(50)
n4.end_fill()
n4.hideturtle()
#nube5

n5=turtle.Turtle()
n5.speed(0)


n5.up()
n5.goto(200,180)
n5.down()

n5.color("#DCDCDC")
n5.fillcolor("#DCDCDC")
n5.begin_fill()
n5.circle(50)
n5.end_fill()
n5.hideturtle()
#nube6

n6=turtle.Turtle()
n6.speed(0)


n6.up()
n6.goto(-120,200)
n6.down()

n6.color("#DCDCDC")
n6.fillcolor("#DCDCDC")
n6.begin_fill()
n6.circle(50)
n6.end_fill()
n6.hideturtle()
#nube7

n7=turtle.Turtle()
n7.speed(0)


n7.up()
n7.goto(-80,180)
n7.down()

n7.color("#DCDCDC")
n7.fillcolor("#DCDCDC")
n7.begin_fill()
n7.circle(50)
n7.end_fill()
n7.hideturtle()
#nube8

n8=turtle.Turtle()
n8.speed(0)


n8.up()
n8.goto(-80,202)
n8.down()

n8.color("#DCDCDC")
n8.fillcolor("#DCDCDC")
n8.begin_fill()
n8.circle(50)
n8.end_fill()
n8.hideturtle()

#nube9

n9=turtle.Turtle()
n9.speed(0)


n9.up()
n9.goto(-60,200)
n9.down()

n9.color("#DCDCDC")
n9.fillcolor("#DCDCDC")
n9.begin_fill()
n9.circle(50)
n9.end_fill()
n9.hideturtle()

#nube10

n10=turtle.Turtle()
n10.speed(0)


n10.up()
n10.goto(-60,180)
n10.down()

n10.color("#DCDCDC")
n10.fillcolor("#DCDCDC")
n10.begin_fill()
n10.circle(50)
n10.end_fill()
n10.hideturtle()

#estrella1
e=turtle.Turtle()
e.speed(0)

e.up()
e.goto(150,150)
e.down()

e.color("yellow")
e.fillcolor("yellow")
e.begin_fill()
e.forward(20)
e.left(144)
e.forward(20)
e.left(144)
e.forward(20)
e.left(144)
e.forward(20)
e.left(144)
e.forward(20)
e.end_fill()
e.hideturtle()

#estrella2

e2=turtle.Turtle()
e2.speed(0)

e2.up()
e2.goto(25,110)
e2.down()

e2.color("yellow")
e2.fillcolor("yellow")
e2.begin_fill()
e2.forward(20)
e2.left(144)
e2.forward(20)
e2.left(144)
e2.forward(20)
e2.left(144)
e2.forward(20)
e2.left(144)
e2.forward(20)
e2.end_fill()
e2.hideturtle()

#estrella3


e3=turtle.Turtle()
e3.speed(0)

e3.up()
e3.goto(10,160)
e3.down()

e3.color("yellow")
e3.fillcolor("yellow")
e3.begin_fill()
e3.forward(20)
e3.left(144)
e3.forward(20)
e3.left(144)
e3.forward(20)
e3.left(144)
e3.forward(20)
e3.left(144)
e3.forward(20)
e3.end_fill()
e3.hideturtle()

#estrella4

e4=turtle.Turtle()
e4.speed(0)

e4.up()
e4.goto(0,150)
e4.down()

e4.color("yellow")
e4.fillcolor("yellow")
e4.begin_fill()
e4.forward(20)
e4.left(144)
e4.forward(20)
e4.left(144)
e4.forward(20)
e4.left(144)
e4.forward(20)
e4.left(144)
e4.forward(20)
e4.end_fill()
e4.hideturtle()

#estrella5

e5=turtle.Turtle()
e5.speed(0)
e5.up()
e5.goto(100,140)
e5.down()

e5.color("yellow")
e5.fillcolor("yellow")
e5.begin_fill()
e5.forward(20)
e5.left(144)
e5.forward(20)
e5.left(144)
e5.forward(20)
e5.left(144)
e5.forward(20)
e5.left(144)
e5.forward(20)
e5.end_fill()
e5.hideturtle()

#estrella6

e6=turtle.Turtle()
e6.speed(0)

e6.up()
e6.goto(-110,170)
e6.down()

e6.color("yellow")
e6.fillcolor("yellow")
e6.begin_fill()
e6.forward(20)
e6.left(144)
e6.forward(20)
e6.left(144)
e6.forward(20)
e6.left(144)
e6.forward(20)
e6.left(144)
e6.forward(20)
e6.end_fill()
e6.hideturtle()

#estrella7

e7=turtle.Turtle()
e7.speed(0)

e7.up()
e7.goto(-120,180)
e7.down()

e7.color("yellow")
e7.fillcolor("yellow")
e7.begin_fill()
e7.forward(20)
e7.left(144)
e7.forward(20)
e7.left(144)
e7.forward(20)
e7.left(144)
e7.forward(20)
e7.left(144)
e7.forward(20)
e7.end_fill()
e7.hideturtle()

#semaforo

m=turtle.Turtle()
m.speed(0)

m.up()
m.goto(100,-200)
m.down()

m.color("SaddleBrown")
m.fillcolor("SaddleBrown")
m.begin_fill()
m.forward(10)
m.left(90)
m.forward(50)
m.left(90)
m.forward(10)
m.left(90)
m.forward(50)
m.left(90)
m.end_fill()
m.hideturtle()


#semaforo2

m2=turtle.Turtle()
m2.speed(0)

m2.up()
m2.goto(95,-160)
m2.down()

m2.color("PowderBlue")
m2.fillcolor("PowderBlue")
m2.begin_fill()
m2.forward(20)
m2.left(90)
m2.forward(35)
m2.left(90)
m2.forward(20)
m2.left(90)
m2.forward(35)
m2.left(90)
m2.end_fill()
m2.hideturtle()

#semaforo3

m3=turtle.Turtle()
m3.speed(0)

m3.up()
m3.goto(105,-140)
m3.down()

m3.color("red")
m3.fillcolor("red")
m3.begin_fill()
m3.circle(6)
m3.end_fill()
m3.hideturtle()

#semaforo4

m4=turtle.Turtle()
m4.speed(0)

m4.up()
m4.goto(105,-160)
m4.down()

m4.color("green")
m4.fillcolor("green")
m4.begin_fill()
m4.circle(6)
m4.end_fill()
m4.hideturtle()

#casa1

ca=turtle.Turtle()
ca.speed(0)

ca.up()
ca.goto(105,-10)
ca.down()

ca.color("Salmon")
ca.fillcolor("Salmon")
ca.begin_fill()
ca.forward(80)
ca.left(120)
ca.forward(80)
ca.left(120)
ca.forward(80)
ca.left(120)
ca.end_fill()
ca.hideturtle()

#casa2

ca2=turtle.Turtle()
ca2.speed(0)

ca2.up()
ca2.goto(105,-90)
ca2.down()

ca2.color("SandyBrown")
ca2.fillcolor("SandyBrown")
ca2.begin_fill()
ca2.forward(80)
ca2.left(90)
ca2.forward(80)
ca2.left(90)
ca2.forward(80)
ca2.left(90)
ca2.end_fill()
ca2.hideturtle()

#casa3

ca3=turtle.Turtle()
ca3.speed(0)

ca3.up()
ca3.goto(135,-90)
ca3.down()

ca3.color("Sienna")
ca3.fillcolor("Sienna")
ca3.begin_fill()
ca3.forward(20)
ca3.left(90)
ca3.forward(30)
ca3.left(90)
ca3.forward(20)
ca3.left(90)
ca3.forward(30)
ca3.end_fill()
ca3.hideturtle()

#casa4

ca4=turtle.Turtle()
ca4.speed(0)
ca4.up()
ca4.goto(115,-55)
ca4.down()
ca4.color("MediumTurquoise")
ca4.fillcolor("MediumTurquoise")
ca4.begin_fill()
ca4.forward(55)
ca4.left(90)
ca4.forward(40)
ca4.left(90)
ca4.forward(55)
ca4.left(90)
ca4.forward(40)
ca4.left(90)
ca4.end_fill()
ca4.hideturtle()




v.exitonclick()()