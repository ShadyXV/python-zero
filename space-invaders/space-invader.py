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



## Enemy
enmey = turtle.Turtle()
enmey.color("red")
enmey.shape("circle")
enmey.penup()
enmey.speed(0)
enmey.setposition(-200, 250)
enmeyspeed = 2

## Draw player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


# Player weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Bullet state

bulletstate = "ready"

# Move player left and right

def mov_left():
  x = player.xcor()
  x -= playerspeed
  if x < -280 :
    x = -280
  player.setx(x)


def mov_right():
  x = player.xcor()
  x += playerspeed
  if x > 280 :
    x = 280
  player.setx(x)

def fire_bullet():
  # declare bullet state as global if it is changed
  global bulletstate
  if bulletstate == "ready":
    bulletstate = "fire"
    # move bullet to initial state i.e just above player
    x = player.xcor()
    y = player.ycor() + 10 # just above player
    bullet.setposition(x, y)
    bullet.showturtle()

## event listener
turtle.listen()
turtle.onkey(mov_left, 'Left')
turtle.onkey(mov_right, 'Right')
turtle.onkey(fire_bullet,'space')

## game loop
while True:
  # Move the enemy
  x = enmey.xcor()
  x += enmeyspeed
  enmey.setx(x)

  if enmey.xcor() > 280:
    y = enmey.ycor()
    y -= 40
    enmeyspeed *=-1
    enmey.sety(y)

  if enmey.xcor() < -280:
    y = enmey.ycor()
    y -= 40
    enmeyspeed *=-1
    enmey.sety(y)

  #Move the bullet
  if bulletstate == "fire":
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

  #Bullet boundary
  if bullet.ycor() > 275:
    bullet.hideturtle()
    bulletstate = "ready"

delay = input("Press enter to finish")