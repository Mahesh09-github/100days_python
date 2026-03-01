from turtle import Screen
from snake import Snake
from scoreboard import Score
from drop_food import Food
import time

screen = Screen()

#Screen setup for game
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Objects
snake = Snake()
food = Food()
score = Score()

starting_positions = [(0,0),(-20,0),(-40,0)]

#making the snake take control from  keyboard
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

#loop to keep goin on
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting Food collision.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.score_update()

    #Hit Wall   
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score.game_over()

    #hits its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()