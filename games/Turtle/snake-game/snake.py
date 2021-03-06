import turtle               # allows us to use the turtles library
import os
import math
import random

wn = turtle.Screen()  # creates a graphics window
wn.bgcolor("black")
wn.title("Snake")

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


## snake
snakes = []
snakes.append(turtle.Turtle()) ## add the head to the snake
snakeSpeed = 10
headPositionX = 0
headPositionY = - 250
snakeX = 0
snakeY = 0
snakeDiff = 5

#Food
food = turtle.Turtle()
x = random.randint(-290, 290)
y = random.randint( -290, 290)
food.speed(3)
food.color("red")
food.up()
food.penup()
food.setposition(x, y)
food.pendown()
food.shape("circle")
food.pensize(3)
food.pendown()

def mov_up():
    global snakeY, snakeX
    snakeX = 0
    snakeY = 1

def mov_down():
    global snakeY, snakeX
    snakeX = 0
    snakeY = -1


def mov_right():
    global snakeX, snakeY
    snakeX = 1
    snakeY = 0

def mov_left():
    global snakeX, snakeY
    snakeX = -1
    snakeY = 0

def isCollision(t1, t2):
  distance = math.sqrt( math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2) )
  if distance < 15 :
    return True
  else :
    return False

## event listener
turtle.listen()
turtle.onkey(mov_up, 'Up')
turtle.onkey(mov_down, 'Down')
turtle.onkey(mov_left, 'Left')
turtle.onkey(mov_right, 'Right')

while True:

    if snakeX != 0:
        headPositionX = headPositionX + snakeX * snakeSpeed

    if snakeY != 0:
        headPositionY = headPositionY + snakeY * snakeSpeed

    listNumber = len(snakes)
    head = snakes[0]
    snakePosX = headPositionX
    snakePosY = headPositionY
    if headPositionX > 290:
        snakePosX = -290
        headPositionX = snakePosX

    if headPositionX < -290:
        snakePosX = 290
        headPositionX = snakePosX

    if headPositionY > 290:
        snakePosY = -290
        headPositionY = snakePosY

    if headPositionY < -290:
        snakePosY = 290
        headPositionY = snakePosY

    head.color("blue")
    head.shape("square")
    head.penup()
    head.speed(0)
    head.setposition(snakePosX ,snakePosY)
    head.setheading(90)


    for i in range(1, listNumber, 1):
        body = snakes[i]
        prevX = snakePosX + 15 * i * snakeX
        prevY = snakePosY + 15 * i * snakeY
        body.color("blue")
        body.shape("square")
        body.penup()
        body.speed(0)
        body.setheading(90)
        body.setposition(prevX, prevY)

    if isCollision(snakes[0], food):
        snakes.append(turtle.Turtle())
        x = random.randint(-290, 290)
        y = random.randint( -290, 290)
        food.up()
        food.pendown()
        food.speed(0)
        food.setx(x)
        food.sety(y)
        food.clear()


delay = input("Press enter to finish")