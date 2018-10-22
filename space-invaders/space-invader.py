import turtle               # allows us to use the turtles library
import os

wn = turtle.Screen()  # creates a graphics window
wn.bgcolor("black")
wn.title("Space Invader")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4) :
  border_pen.fd(600)
  border_pen.lt(90)
border_pen.hideturtle()


## Draw player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


# Move player left and right

def mov_left():
  x = player.xcor()
  x -= playerspeed
  if x < -280 :
    x = 280
  player.setx(x)


def mov_right():
  x = player.xcor()
  x += playerspeed
  if x > 280 :
    x = -280
  player.setx(x)


turtle.listen()
turtle.onkey(mov_left, 'Left')
turtle.onkey(mov_right, 'Right')

delay = input("Press enter to finish")