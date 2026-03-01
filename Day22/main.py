from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()


#Setting up the screen
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Creating objects
right_pd = Paddle((350,0))
left_pd = Paddle((-350,0))
ball = Ball()
scorecard = Scorecard()

#Enabling screen to take actions from keyboard
screen.listen()
screen.onkey(right_pd.go_up,"Up")

screen.onkey(right_pd.go_down,"Down")
screen.onkey(left_pd.go_up,"w")
screen.onkey(left_pd.go_down,"s")

is_game_on = True
#While loop
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move() 

    #when Hits the wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce back
        ball.bounce_ycor()

    #Ball hits the paddle
    if ball.distance(right_pd) < 50 and ball.xcor() > 320 or ball.distance(left_pd) < 50 and ball.xcor() < -320:
        ball.bounce_xcor()

    if ball.xcor() > 380:
        ball.ball_reset()
        scorecard.l_point()
        
    if ball.xcor() < -380:
        ball.ball_reset()
        scorecard.r_point()
        
        















screen.exitonclick()