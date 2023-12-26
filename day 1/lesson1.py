from turtle import *


#we want to paint house

#step 1: draw square

speed(30)
width(7)
color("blue")
forward (200)
left (90) 

forward (200)
left (90) 

forward (200)
left (90) 

forward (200)
left (90) 
#end of square

#now drawin a door

forward (70)
color("yellow")
left (90)
forward(120) #height of a door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200,200)
pendown()

#window 1

color("green")
begin_fill()
left(30)
forward(60)
right(90)
forward(75)
right(90)
forward(60)
end_fill()

#window 2

penup()
goto(75,200)
pendown()

right(180)
begin_fill()
forward(60)
right(90)
forward(75)
right(90)
forward(60)
right(90)
forward(75)
end_fill()









exitonclick()