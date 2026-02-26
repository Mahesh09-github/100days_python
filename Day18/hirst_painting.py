import turtle as t
import random
t.colormode(255)
mark = t.Turtle()
mark.speed("fastest")
mark.penup()
mark.hideturtle()

#combination of rgb colors extracted using colorgram
my_colors = [  (212, 157, 88), (37, 93, 167), (147, 13, 59), (164, 42, 92), (164, 159, 20), (158, 76, 35), (238, 214, 81), (60, 123, 36), (194, 99, 137), (64, 49, 30), (150, 220, 191), (29, 37, 82), (69, 98, 25), (196, 135, 147), (130, 161, 190), (79, 130, 179), (152, 174, 143), (218, 172, 187), (217, 179, 172), (112, 144, 95), (180, 97, 81), (43, 49, 88), (175, 191, 215), (167, 207, 214), (109, 16, 44), (150, 15, 0)]

#to change positon of tutle from center
mark.setheading(225)
mark.forward(300)
mark.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    mark.dot(20,random.choice(my_colors))
    mark.forward(50)
    
    #condition to make turn left and move forward after every 10 dots
    if dot_count % 10 == 0:
        mark.setheading(90)
        mark.forward(50)
        mark.setheading(180)
        mark.forward(500)
        mark.setheading(0)


screen = t.Screen()
screen.exitonclick()
