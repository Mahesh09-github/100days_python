from turtle import Turtle,Screen

max = Turtle()
screen = Screen()

def move_forwards():
    max.forward(10)

def move_backwards():
    max.backward(10)

def turn_left():
    new_heading = max.heading() + 10
    max.setheading(new_heading)
def turn_right():
    new_heading = max.heading() + 10
    max.setheading(new_heading)
def clear():
    max.clear()
    max.penup
    max.home()
    max.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()




screen.listen()
turn_left()