import turtle
import os
import math
import random
import sys


wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Ballon Shooter Game")

print("Welcome to Ballon Shooter Game")


turtle.register_shape("bow.gif")
turtle.register_shape("""ballon.gif""")
turtle.register_shape("arrow.gif")



player = turtle.Turtle()
player.color("white")
player.shape("bow.gif")
player.penup()
player.speed(0)
player.shapesize(0.8,0.8)
player.setposition(-300, 250)
player.setheading(360)
playerspeed = 25
	
ballon=turtle.Turtle()
ballon.color("yellow")
ballon.shape("ballon.gif")
ballon.penup()
ballon.speed(0)
ballon.shapesize(0.9,0.9)
ballon.setposition(50,250)
 
ballonspeed = 5

arrow = turtle.Turtle()
arrow.color("black")
arrow.shape("arrow.gif")
arrow.penup()
arrow.speed(0)
arrow.setheading(360)
arrow.shapesize(0.6,0.6)
arrow.hideturtle()
arrowspeed = 30
arrowstate = "ready"


score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(220,240) 
scorestring = "Score: %s" %score
score_pen.write(scorestring,False,align ="left",font=("Times_Roman",14,"normal"))
score_pen.hideturtle()

def move_down():
	y =player.ycor()
	y = y - playerspeed
	if y < -250:
		y = -250
	player.sety(y)
	
def move_up():
	y =player.ycor()
	y = y + playerspeed
	if y > 250:
		y =250
	player.sety(y)

def throw_arrow():
	global arrowstate
	if arrowstate == "ready":
		arrowstate = "fire" 
		x = player.xcor()
		y = player.ycor()
		arrow.setposition(x +10,y+5)
		arrow.showturtle()
	
		
turtle.listen()
turtle.onkey(move_down,"Down")
turtle.onkey(move_up,"Up")	
turtle.onkey(throw_arrow,"space")	

def blast(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 30:
		return True
	else:
		return False
	
while True:
	y = ballon.ycor()
	x = ballon.xcor()
	y = y - ballonspeed
	ballon.sety(y)
	if y <  -260:
		y = 250
		x = random.randint(-200, 200)
	ballon.setx(x)
	ballon.sety(y)

	
	if arrowstate == "fire":
		x = arrow.xcor()
		x = x + arrowspeed
		arrow.setx(x)
	
	
	if arrow.xcor()>310:
		arrow.hideturtle()
		arrowstate = "ready"
	
	if blast(arrow, ballon):
			arrow.hideturtle()
			arrowstate = "ready"
			arrow.setposition(500,0)
			ballon.setposition(50,250)
			score = score + 1
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring,False,align ="left",font=("Times_Roman",14,"normal"))
			
	
	
