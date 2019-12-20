import turtle
from random import randint

# TODO ask user

screen = turtle.Screen()
screen.title("Welcome to the turtle course!")
screen.setup(width=1500, height=1000, startx=0, starty=0)

# Setup Turtle & positioning
raphael = turtle.Turtle()
raphael.color('red')
raphael.penup()
raphael.shape('turtle')
raphael.setpos(-690, -400)
raphael.position()

# TO REFACTO with array
donatello = turtle.Turtle()
donatello.shape('turtle')
donatello.color('purple')
donatello.penup()
donatello.setpos(-690, -200)

michelangelo = turtle.Turtle()
michelangelo.shape('turtle')
michelangelo.color('orange')
michelangelo.penup()
michelangelo.setpos(-690, 0)

leonardo = turtle.Turtle()
leonardo.shape('turtle')
leonardo.color('deep sky blue')
leonardo.penup()
leonardo.setpos(-690, 200)

splinter = turtle.Turtle()
splinter.shape('turtle')
splinter.color('Dark Slate Gray')
splinter.penup()
splinter.setpos(-690, 400)

# Setup to write course
raphael.pendown()
donatello.pendown()
michelangelo.pendown()
leonardo.pendown()
splinter.pendown()
raphael.speed(10)
donatello.speed(10)
michelangelo.speed(10)
leonardo.speed(10)
splinter.speed(10)

Turtles = [raphael, donatello, michelangelo, leonardo, splinter]

while michelangelo.xcor() != 690 and raphael.xcor() != 690 and donatello.xcor() != 690 and leonardo.xcor() != 690 and splinter.xcor() != 690:
    rand = randint(0, 4)
    Turtles[rand].fd(5)

# TO DO get and show result ( no time)
