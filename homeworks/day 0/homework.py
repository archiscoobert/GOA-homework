from turtle import *

#we want to paint a house

#step:1   draw a square
speed(10)
width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()
forward(70)
left(90)

color("yellow")
forward(120)       #heght of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 170)
pendown()

color("brown")
begin_fill()
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


penup()
goto(170, 170)
pendown()

begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


penup()
goto(-380,-25)
pendown()

color("green")
begin_fill()
forward(20)
right(90)
forward(750)
right(90)
forward(450)
right(90)
forward(775)
right(450)
end_fill()



exitonclick()