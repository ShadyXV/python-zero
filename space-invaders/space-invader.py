import turtle               # allows us to use the turtles library
import os
import math
import random

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


## Choose number of enemies
number_of_enemies = 5

## Create an empty list
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
  enemies.append(turtle.Turtle())

for enemy in enemies:
  ## Enemy
  enemy.color("red")
  enemy.shape("circle")
  enemy.penup()
  enemy.speed(0)
  x = random.randint(-200, 200)
  y = random.randint(100, 250)
  enemy.setposition(x, y)


enemyspeed = 2

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

def isCollision(t1, t2):
  distance = math.sqrt( math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2) )
  if distance < 15 :
    return True
  else :
    return False

## event listener
turtle.listen()
turtle.onkey(mov_left, 'Left')
turtle.onkey(mov_right, 'Right')
turtle.onkey(fire_bullet,'space')

## game loop
while True:

  for enemy in enemies :
    # Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move all enemies down
    if enemy.xcor() > 280:
      for e in enemies:
        y = e.ycor()
        y -= 40
        e.sety(y)
      enemyspeed *=-1

    #Move all enemies down
    if enemy.xcor() < -280:
      for e in enemies:
        y = e.ycor()
        y -= 40
        e.sety(y)
      enemyspeed *=-1


    ## Collision detction bullet and enemy
    if isCollision(bullet, enemy):
      #Reset bullet
      bullet.hideturtle()
      bulletstate= "ready"
      bullet.setposition(0, -400)
      #reset enemy
      x = random.randint(-200, 200)
      y = random.randint(100, 250)
      enemy.setposition(x, y)

    if isCollision(player, enemy) :
      player.hideturtle()
      enemy.hideturtle()
      break;


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